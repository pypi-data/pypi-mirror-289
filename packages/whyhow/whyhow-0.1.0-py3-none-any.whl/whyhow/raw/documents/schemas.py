"""Collection of Pydantic models for the the documents router."""

from datetime import datetime
from typing import Any, Literal

from pydantic import BaseModel, Field

from whyhow.raw.base import (
    PathParameters,
    QueryParameters,
    RequestBody,
    ResponseBody,
)

DOCUMENT_STATUS = Literal["uploaded", "processing", "processed", "failed"]
ALLOWED_FORMAT = Literal["csv", "json", "pdf", "txt"]


# Auxiliary models
class DocumentWorkspaceRaw(BaseModel):
    """Model for the workspace details.

    OpenAPI: WorkspaceDetails
    """

    id: str = Field(..., alias="_id")
    name: str


class DocumentMetadataRaw(BaseModel):
    """Model for the document metadata.

    OpenAPI: DocumentMetadata
    """

    size: int
    format: ALLOWED_FORMAT
    filename: str


class DocumentProcessingDetailsRaw(BaseModel):
    """Model for the document processing details.

    OpenAPI: DocumentProcessingDetails
    """

    start_time: datetime | None
    end_time: datetime | None
    error_details: str | None


class DocumentRaw(BaseModel):
    """Model for the document details.

    OpenAPI: DocumentOutWithWorkspaceDetails
    """

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime
    created_by: str
    workspaces: list[DocumentWorkspaceRaw]
    status: DOCUMENT_STATUS
    metadata: DocumentMetadataRaw
    processing_details: DocumentProcessingDetailsRaw | None
    tags: dict[str, str]
    user_metadata: dict[str, Any]


class DocumentSlimRaw(BaseModel):
    """Model for the document details.

    It only includes the workspace ID.

    OpenAPI: DocumentOut
    """

    id: str = Field(..., alias="_id")
    created_at: datetime
    updated_at: datetime
    created_by: str
    workspaces: list[str]
    status: DOCUMENT_STATUS
    metadata: DocumentMetadataRaw
    processing_details: DocumentProcessingDetailsRaw | None
    tags: dict[str, str]
    user_metadata: dict[str, Any]


# GET /documents/{}
class GetDocumentPathParameters(PathParameters):
    """Path parameters for GET /documents/{document_id}."""

    document_id: str


class GetDocumentResponseBody(ResponseBody):
    """Response body for GET /documents/{document_id}.

    OpenAPI: DocumentsResponseWithWorkspaceDetails
    """

    message: str
    status: str
    count: int
    documents: list[DocumentRaw]


# GET /documents
class GetAllDocumentsQueryParameters(QueryParameters):
    """Query parameters for GET /documents."""

    skip: int | None = None
    limit: int | None = None
    filename: str | None = None
    workspace_id: str | None = None
    workspace_name: str | None = None
    order: Literal["ascending", "descending"] | None = None


class GetAllDocumentsResponseBody(ResponseBody):
    """Response body for GET /documents.

    OpenAPI: DocumentsResponseWithWorkspaceDetails
    """

    message: str
    status: str
    count: int
    documents: list[DocumentRaw]


# POST /documents/generate_presigned
class GeneratePresignedDocumentRequestBody(RequestBody):
    """Request body for POST /documents/generate_presigned.

    OpenAPI: GeneratePresignedRequest
    """

    filename: str
    workspace_id: str


class GeneratePresignedDocumentResponseBody(ResponseBody):
    """Response body for POST /documents/generate_presigned.

    OpenAPI: GeneratePresignedResponse
    """

    url: str
    fields: dict[str, str]


# POST /documents/{document_id}/upload
class ProcessDocumentPathParameters(PathParameters):
    """Path parameters for POST /documents/{document_id}/upload."""

    document_id: str


class ProcessDocumentResponseBody(ResponseBody):
    """Response body for POST /documents/{document_id}/upload.

    OpenAPI: DocumentsResponseWithWorkspaceDetails
    """

    message: str
    status: str
    count: int = 0
    documents: list[DocumentRaw]


# DELETE /documents/{document_id}
class DeleteDocumentPathParameters(PathParameters):
    """Path parameters for DELETE /documents/{document_id}."""

    document_id: str


class DeleteDocumentResponseBody(ResponseBody):
    """Response body for DELETE /documents/{document_id}.

    OpenAPI: DocumentsResponse
    """

    message: str
    status: str
    count: int = 0
    documents: list[DocumentSlimRaw] | None = None
