"""Collection of Pydantic models for the schemas router."""

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
class SchemaWorkspaceRaw(BaseModel):
    """Schema workspace model.

    OpenAPI: WorkspaceDetails
    """

    id: str = Field(..., alias="_id")
    name: str


class SchemaEntityFieldRaw(BaseModel):
    """Entity field model.

    OpenAPI: EntityField
    """

    name: str
    properties: list[str]


class SchemaEntityRaw(BaseModel):
    """Schema entity model.

    OpenAPI: SchemaEntity
    """

    name: str
    description: str
    fields: list[SchemaEntityFieldRaw]


class SchemaRelationRaw(BaseModel):
    """Schema relation model.

    OpenAPI: SchemaRelation
    """

    name: str
    description: str


class SchemaTriplePatternRaw(BaseModel):
    """Schema triple pattern model.

    OpenAPI: SchemaTriplePattern
    """

    head: SchemaEntityRaw
    relation: SchemaRelationRaw
    tail: SchemaEntityRaw
    description: str


class SchemaTriplePatternSlimRaw(BaseModel):
    """Schema triple pattern model.

    Note that instead of storing the whole entity and relation data, this one
    only stores the names.

    OpenAPI: TriplePattern
    """

    head: str
    relation: str
    tail: str
    description: str


class SchemaRaw(BaseModel):
    """Schema model (Just a helper).

    This one stores the whole workspace data.

    OpenAPI: SchemaOutWithWorkspaceDetails
    """

    id: str = Field(..., alias="_id")
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    entities: list[SchemaEntityRaw]
    relations: list[SchemaRelationRaw]
    patterns: list[SchemaTriplePatternRaw]
    workspace: SchemaWorkspaceRaw


class SchemaSlimRaw(BaseModel):
    """Schema model (Just a helper).

    This one only stores the ID of the workspace.

    OpenAPI: SchemaOut
    """

    id: str = Field(..., alias="_id")
    name: str
    created_at: datetime
    updated_at: datetime
    created_by: str
    entities: list[SchemaEntityRaw]
    relations: list[SchemaRelationRaw]
    patterns: list[SchemaTriplePatternRaw]
    workspace_id: str


class SchemaGeneratedRaw(BaseModel):
    """Generated schema model.

    OpenAPI: GeneratedSchema
    """

    entities: list[SchemaEntityRaw]
    relations: list[SchemaRelationRaw]
    patterns: list[SchemaTriplePatternSlimRaw]


class SchemaGenerationError(BaseModel):
    """Error model for schema generation.

    OpenAPI: ErrorDetails
    """

    message: str
    created_at: datetime
    error: str


# GET /schemas/{schema_id}
class GetSchemaResponseBody(ResponseBody):
    """Response model for the GET /schemas/{schema_id} endpoint.

    OpenAPI: SchemasResponseWithWorkspaceDetails
    """

    message: str
    status: str
    count: int
    schemas: list[SchemaRaw]


class GetSchemaPathParameters(PathParameters):
    """Path parameters for the GET /schemas/{schema_id} endpoint."""

    schema_id: str


# GET /schemas
class GetAllSchemasResponseBody(GetSchemaResponseBody):
    """Response model for the GET /schemas endpoint.

    OpenAPI: SchemasResponseWithWorkspaceDetails
    """


class GetAllSchemasQueryParameters(QueryParameters):
    """Query parameters for the GET /schemas endpoint."""

    skip: int | None = None
    limit: int | None = None
    name: str | None = None
    workspace_id: str | None = None
    workspace_name: str | None = None
    order: Literal["ascending", "descending"] | None = None


# POST /schemas
class CreateSchemaRequestBody(RequestBody):
    """Request model for the POST /schemas endpoint.

    OpenAPI: SchemaCreate
    """

    name: str = Field(..., min_length=1)
    workspace: str
    entities: list[SchemaEntityRaw]
    relations: list[SchemaRelationRaw]
    patterns: list[SchemaTriplePatternSlimRaw]  # Attention


class CreateSchemaResponseBody(ResponseBody):
    """Response model for the POST /schemas endpoint.

    OpenAPI: SchemasResponse
    """

    message: str
    status: str
    count: int = 0
    schemas: list[SchemaSlimRaw]


# DELETE /schemas/{schema_id}
class DeleteSchemaPathParameters(PathParameters):
    """Path parameters for the DELETE /schemas/{schema_id} endpoint."""

    schema_id: str


class DeleteSchemaResponseBody(ResponseBody):
    """Response model for the DELETE /schemas/{schema_id} endpoint.

    OpenAPI: SchemasResponse
    """

    message: str
    status: str
    count: int = 0
    schemas: list[SchemaSlimRaw]


# POST /schemas/generate
class GenerateSchemaRequestBody(RequestBody):
    """Request model for the POST /schemas/generate endpoint.

    OpenAPI: GenerateSchemaBody
    """

    workspace: str
    questions: list[str]


class GenerateSchemaResponseBody(ResponseBody):
    """Response model for the POST /schemas/generate endpoint.

    OpenAPI: GeneratedSchemaResponse
    """

    message: str
    status: str
    questions: list[str]
    count: int
    errors: list[SchemaGenerationError]
    generated_schema: SchemaGeneratedRaw
