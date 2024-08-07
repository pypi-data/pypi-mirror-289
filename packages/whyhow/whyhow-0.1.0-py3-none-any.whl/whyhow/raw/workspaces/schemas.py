"""Collection of Pydantic models for the workspace routers."""

from datetime import datetime
from typing import Literal

from pydantic import BaseModel, Field

from whyhow.raw.base import (
    PathParameters,
    QueryParameters,
    RequestBody,
    ResponseBody,
)


# Auxiliary models
class WorkspaceRaw(BaseModel):
    """Workspace model (Just a helper).

    OpenAPI: WorkspaceOut
    """

    id: str = Field(..., alias="_id")
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: str


# GET /workspaces/{workspace_id}
class GetWorkspacePathParameters(PathParameters):
    """Path parameters for the get workspace endpoint."""

    workspace_id: str


class GetWorkspaceResponseBody(ResponseBody):
    """Response body for the get workspace endpoint.

    OpenAPI: WorkspacesResponse
    """

    message: str
    status: str
    count: int = 0
    workspaces: list[WorkspaceRaw]


# GET /workspaces
class GetAllWorkspacesQueryParameters(QueryParameters):
    """Query parameters for the get all workspaces endpoint."""

    skip: int | None
    limit: int | None
    name: str | None
    order: Literal["ascending", "descending"] | None


class GetAllWorkspacesResponseBody(GetWorkspaceResponseBody):
    """Response body for the get all workspaces endpoint.

    OpenAPI: WorkspacesResponse
    """


# POST /workspaces
class CreateWorkspaceRequestBody(RequestBody):
    """Request body for the create workspace endpoint.

    OpenAPI: WorkspaceCreate
    """

    name: str


class CreateWorkspaceResponseBody(GetWorkspaceResponseBody):
    """Response body for the create workspace endpoint.

    OpenAPI: WorkspacesResponse
    """


# PUT /workspaces/{workspace_id}
class UpdateWorkspacePathParameters(PathParameters):
    """Path parameters for the update workspace endpoint."""

    workspace_id: str


class UpdateWorkspaceRequestBody(RequestBody):
    """Request body for the update workspace endpoint.

    OpenAPI: WorkspaceUpdate
    """

    name: str


class UpdateWorkspaceResponseBody(GetWorkspaceResponseBody):
    """Response body for the update workspace endpoint.

    OpenAPI: WorkspacesResponse
    """


# DELETE /workspaces/{workspace_id}
class DeleteWorkspacePathParameters(PathParameters):
    """Path parameters for the delete workspace endpoint."""

    workspace_id: str


class DeleteWorkspaceResponseBody(GetWorkspaceResponseBody):
    """Response body for the delete workspace endpoint.

    OpenAPI: WorkspacesResponse
    """
