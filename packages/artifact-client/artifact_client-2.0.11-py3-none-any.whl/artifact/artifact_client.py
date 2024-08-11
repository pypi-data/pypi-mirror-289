import os
import json
import logging
from typing import List, Optional

from ._client.api import DefaultApi
from ._client.models import Graph, GraphStats, QueryRequest, CreateGraphRequest, IngestDocumentRequest

log = logging.getLogger(__name__)


class ArtifactClient:
    def __init__(self, api_key: Optional[str] = None, base_url: Optional[str] = None):
        api_key = api_key or os.environ.get("ARTIFACT_API_KEY")
        if api_key is None:
            raise RuntimeError(
                "API authorization key required. "
                "Set ARTIFACT_API_KEY environment variable or pass as argument to client."
            )
        base_url = base_url or os.environ.get(
            "ARTIFACT_BASE_URL", "https://xxny160gbe.execute-api.us-east-1.amazonaws.com/Prod"
        )

        from . import ApiClient, Configuration

        config = Configuration()
        if base_url:
            config.host = base_url
        # config.api_key_prefix = {"Authorization": "Bearer"}
        config.api_key = {"Authorization": api_key}

        api = ApiClient(configuration=config)
        self.api_instance = DefaultApi(api_client=api)
        self.api_key = api_key

    @property
    def api(self):
        return self.api_instance.api_client

    @property
    def configuration(self):
        return self.api.configuration

    def format_body(self, body) -> str:
        if isinstance(body, str):
            # assume string is json formatted
            return body
        elif isinstance(body, dict) or isinstance(body, list):
            return json.dumps(body)
        elif isinstance(body, list):
            # allow list of objects
            return json.dumps([b.to_dict() if hasattr(body, "to_dict") else b for b in body])
        elif hasattr(body, "to_dict"):
            # assume body is a request object
            return json.dumps(body.to_dict())
        else:
            raise RuntimeError(f"Unsupported body type: {type(body)}")

    def extract_body(self, resp):
        try:
            return resp.json()
        except Exception:
            raise ValueError(f"Only JSON bodies supported. Received: {resp.text if resp else 'None'}")

    def list_all_graphs(self) -> List[Graph]:
        """Lists all graphs."""
        graphs_data = self.api_instance.list_graphs()
        return [Graph(**g) for g in graphs_data]

    def delete_all_graphs(self):
        """Delete all graphs associated with the organization"""
        response = self.api_instance.delete_all_graphs()
        return response

    def create_graph(self, name: str, index_interval: str = "IMMEDIATE") -> Graph:
        """Create a new graph."""
        return self.api_instance.create_graph(CreateGraphRequest(name=name, index_interval=index_interval))

    def get_graph(self, graph_id: str) -> Graph:
        return self.api_instance.get_graph(graph_id)

    def update_graph(self, graph_id: str, **attrs) -> Graph:
        """Update a graph."""
        return self.api_instance.update_graph(attrs, graph_id)

    def delete_graph(self, graph_id: str):
        """Delete a graph."""
        self.api_instance.delete_graph(graph_id)

    def query_graph(self, graph_id: str, query: str) -> str:
        """Query the graph."""
        return self.api_instance.query_graph(QueryRequest(query=query), graph_id)

    def graph_stats(self, graph_id: str) -> GraphStats:
        """Get graph statistics."""
        return self.api_instance.get_graph_stats(graph_id)

    def ingest_document(self, graph_id: str, document: str) -> None:
        """Ingest a document into the graph."""
        return self.api_instance.ingest_document(IngestDocumentRequest(document=document), graph_id)

    def get_document_meta(self, graph_id: str) -> List[dict]:
        """Get documents metadata."""
        return self.api_instance.get_graph_documents_meta(graph_id=graph_id)
