"""Collection of Pydantic models for the the chunks router."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from whyhow.raw.base import PathParameters, QueryParameters, ResponseBody


# Auxiliary models
class ChunkWorkspaceRaw(BaseModel):
    """Chunk workspace model.

    OpenAPI: WorkspaceDetails
    """

    id: str = Field(..., alias="_id")
    name: str


class ChunkDocumentDetailRaw(BaseModel):
    """Chunk document details model.

    OpenAPI: DocumentDetail
    """

    id: str = Field(..., alias="_id")
    filename: str


class ChunkMetadataRaw(BaseModel):
    """Chunk metadata model.

    OpenAPI: ChunkMetadata
    """

    language: str
    length: int | None = None
    size: int | None = None
    data_source_type: str | None = None
    index: int | None = None
    page: int | None = None
    start: int | None = None
    end: int | None = None


class ChunkRaw(BaseModel):
    """Chunk model (Just a helper).

    OpenAPI: ChunksOutWithWorkspaceDetails
    """

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime
    created_by: str
    workspaces: list[ChunkWorkspaceRaw]
    document: ChunkDocumentDetailRaw | None = None
    data_type: str
    content: str
    embedding: list[float] | None = None
    metadata: ChunkMetadataRaw
    tags: dict[str, Any] | list[Any]
    user_metadata: dict[str, Any]


# GET /chunks/{chunk_id}
class GetChunkPathParameters(PathParameters):
    """Path parameters for the get chunk endpoint."""

    chunk_id: str


class GetChunkQueryParameters(QueryParameters):
    """Query parameters for the get chunk endpoint."""

    include_embeddings: bool | None = None


class GetChunkResponseBody(ResponseBody):
    """Response body for the get chunk endpoint.

    OpenAPI: ChunksResponseWithWorkspaceDetails
    """

    message: str
    status: str
    count: int = 0
    chunks: list[ChunkRaw]


# GET /chunks
class GetAllChunksQueryParameters(QueryParameters):
    """Query parameters for the get all chunks endpoint."""

    skip: int | None = None
    limit: int | None = None
    data_type: str | None = None
    workspace_id: str | None = None
    workspace_name: str | None = None
    worskpace_id: str | None = None
    document_id: str | None = None
    document_filename: str | None = None
    include_embeddings: bool | None = None
    order: Literal["ascending", "descending"] | None = None


class GetAllChunksResponseBody(ResponseBody):
    """Response body for the get all chunks endpoint.

    OpenAPI: ChunksResponseWithWorkspaceDetails
    """

    message: str
    status: str
    count: int
    chunks: list[ChunkRaw]
