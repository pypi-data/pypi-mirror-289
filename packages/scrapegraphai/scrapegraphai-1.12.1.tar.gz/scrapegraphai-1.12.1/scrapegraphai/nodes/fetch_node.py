""""
FetchNode Module
"""

import json
from typing import List, Optional
from langchain_openai import ChatOpenAI
import pandas as pd
import requests
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.documents import Document
from ..utils.cleanup_html import cleanup_html
from ..docloaders import ChromiumLoader
from ..docloaders.browser_base import browser_base_fetch
from ..utils.convert_to_md import convert_to_md
from ..utils.logging import get_logger
from .base_node import BaseNode


class FetchNode(BaseNode):
    """
    A node responsible for fetching the HTML content of a specified URL and updating
    the graph's state with this content. It uses ChromiumLoader to fetch
    the content from a web page asynchronously (with proxy protection).

    This node acts as a starting point in many scraping workflows, preparing the state
    with the necessary HTML content for further processing by subsequent nodes in the graph.

    Attributes:
        headless (bool): A flag indicating whether the browser should run in headless mode.
        verbose (bool): A flag indicating whether to print verbose output during execution.

    Args:
        input (str): Boolean expression defining the input keys needed from the state.
        output (List[str]): List of output keys to be updated in the state.
        node_config (Optional[dict]): Additional configuration for the node.
        node_name (str): The unique identifier name for the node, defaulting to "Fetch".
    """

    def __init__(
        self,
        input: str,
        output: List[str],
        node_config: Optional[dict] = None,
        node_name: str = "Fetch",
    ):
        super().__init__(node_name, "node", input, output, 1, node_config)

        self.headless = (
            True if node_config is None else node_config.get("headless", True)
        )
        self.verbose = (
            False if node_config is None else node_config.get("verbose", False)
        )
        self.use_soup = (
            False if node_config is None else node_config.get("use_soup", False)
        )
        self.loader_kwargs = (
            {} if node_config is None else node_config.get("loader_kwargs", {})
        )
        self.llm_model = (
            {} if node_config is None else node_config.get("llm_model", {})
        )
        self.force = (
            False if node_config is None else node_config.get("force", False)
        )
        self.script_creator = (
            False if node_config is None else node_config.get("script_creator", False)
        )
        self.openai_md_enabled = (
            False if node_config is None else node_config.get("script_creator", False)
        )

        self.cut = (
            False if node_config is None else node_config.get("cut", True)
        )

        self.browser_base = node_config.get("browser_base")

    def execute(self, state):
        """
        Executes the node's logic to fetch HTML content from a specified URL and
        update the state with this content.

        Args:
            state (dict): The current state of the graph. The input keys will be used
                            to fetch the correct data types from the state.

        Returns:
            dict: The updated state with a new output key containing the fetched HTML content.

        Raises:
            KeyError: If the input key is not found in the state, indicating that the
                    necessary information to perform the operation is missing.
        """

        self.logger.info(f"--- Executing {self.node_name} Node ---")

        # Interpret input keys based on the provided input expression
        input_keys = self.get_input_keys(state)
        # Fetching data from the state based on the input keys
        input_data = [state[key] for key in input_keys]

        source = input_data[0]
        if (
            input_keys[0] == "json_dir"
            or input_keys[0] == "xml_dir"
            or input_keys[0] == "csv_dir"
            or input_keys[0] == "pdf_dir"
            or input_keys[0] == "md_dir"
        ):
            compressed_document = [
                source
            ]

            state.update({self.output[0]: compressed_document})
            return state
        # handling pdf
        elif input_keys[0] == "pdf":


            loader = PyPDFLoader(source)
            compressed_document = loader.load()
            state.update({self.output[0]: compressed_document})
            return state

        elif input_keys[0] == "csv":
            compressed_document = [
                Document(
                    page_content=str(pd.read_csv(source)), metadata={"source": "csv"}
                )
            ]
            state.update({self.output[0]: compressed_document})
            return state
        elif input_keys[0] == "json":
            f = open(source, encoding="utf-8")
            compressed_document = [
                Document(page_content=str(json.load(f)), metadata={"source": "json"})
            ]
            state.update({self.output[0]: compressed_document})
            return state

        elif input_keys[0] == "xml":
            with open(source, "r", encoding="utf-8") as f:
                data = f.read()
            compressed_document = [
                Document(page_content=data, metadata={"source": "xml"})
            ]
            state.update({self.output[0]: compressed_document})
            return state
        elif input_keys[0] == "md":
            with open(source, "r", encoding="utf-8") as f:
                data = f.read()
            compressed_document = [
                Document(page_content=data, metadata={"source": "md"})
            ]
            state.update({self.output[0]: compressed_document})
            return state

        elif self.input == "pdf_dir":
            pass

        elif not source.startswith("http"):
            self.logger.info(f"--- (Fetching HTML from: {source}) ---")
            if not source.strip():
                raise ValueError("No HTML body content found in the local source.")

            parsed_content = source

            if isinstance(self.llm_model, ChatOpenAI) and not self.script_creator or self.force and not self.script_creator:

                parsed_content = convert_to_md(source)
            else:
                parsed_content = source

            compressed_document = [
                Document(page_content=parsed_content, metadata={"source": "local_dir"})
            ]

        elif self.use_soup:
            self.logger.info(f"--- (Fetching HTML from: {source}) ---")
            response = requests.get(source)
            if response.status_code == 200:
                if not response.text.strip():
                    raise ValueError("No HTML body content found in the response.")

                if not self.cut:
                    parsed_content = cleanup_html(response, source)

                if  (isinstance(self.llm_model, ChatOpenAI)
                     and not self.script_creator) or (self.force and not self.script_creator):
                    parsed_content = convert_to_md(source, input_data[0])

                compressed_document = [Document(page_content=parsed_content)]
            else:
                self.logger.warning(
                    f"Failed to retrieve contents from the webpage at url: {source}"
                )

        else:
            self.logger.info(f"--- (Fetching HTML from: {source}) ---")
            loader_kwargs = {}

            if self.node_config is not None:
                loader_kwargs = self.node_config.get("loader_kwargs", {})

            if self.browser_base is not None:
                data =  browser_base_fetch(self.browser_base.get("api_key"),
                                            self.browser_base.get("project_id"), [source])

                document = [Document(page_content=content,
                                    metadata={"source": source}) for content in data]
            else:
                loader = ChromiumLoader([source], headless=self.headless, **loader_kwargs)
                document = loader.load()

            if not document or not document[0].page_content.strip():
                raise ValueError("No HTML body content found in the document fetched by ChromiumLoader.")
            parsed_content = document[0].page_content

            if  isinstance(self.llm_model, ChatOpenAI) and not self.script_creator or self.force and not self.script_creator and not self.openai_md_enabled:
                parsed_content = convert_to_md(document[0].page_content, input_data[0])


            compressed_document = [
                Document(page_content=parsed_content, metadata={"source": "html file"})
            ]

        state.update(
            {
                self.output[0]: compressed_document,
            }
        )

        return state
