"""Collection of Pydantic models for the the graphs router."""

from typing import Literal

from whyhow.raw.autogen import (
    ChunkFilters,
    CreateGraphBody,
    CypherResponse,
    DetailedGraphsResponse,
    GraphsDetailedTripleResponse,
    GraphsResponse,
    GraphUpdate,
    Name,
    Query,
    QueryGraphRequest,
)
from whyhow.raw.base import (
    PathParameters,
    QueryParameters,
    RequestBody,
    ResponseBody,
)


# Auxiliar models
class GraphNameRaw(Name):
    """Graph name model.

    OpenAPI: Name
    """


class GraphQueryRaw(Query):
    """Graph query model.

    OpenAPI: Query
    """


class GraphChunkFiltersRaw(ChunkFilters):
    """Graph chunk filters model.

    OpenAPI: ChunkFilters
    """


# GET /graphs/{graph_id}
class GetGraphPathParameters(PathParameters):
    """Path parameters for the get graph endpoint."""

    graph_id: str


class GetGraphResponseBody(ResponseBody, DetailedGraphsResponse):
    """Graph workspace model.

    OpenAPI: DetailedGraphsResponse
    """


# GET /graphs
class GetAllGraphsQueryParameters(QueryParameters):
    """Query parameters for the get all graphs endpoint."""

    skip: int | None = None
    limit: int | None = None
    name: str | None = None
    workspace_id: str | None = None
    workspace_name: str | None = None
    schema_id: str | None = None
    schema_name: str | None = None
    order: Literal["ascending", "descending"] | None = None


class GetAllGraphsResponseBody(ResponseBody, DetailedGraphsResponse):
    """Graph workspace model.

    OpenAPI: DetailedGraphsResponse
    """


# POST /graphs
class CreateGraphRequestBody(RequestBody, CreateGraphBody):
    """Create graph request body.

    OpenAPI: CreateGraphBody
    """


class CreateGraphResponseBody(ResponseBody, GraphsResponse):
    """Graph workspace model.

    OpenAPI: GraphsResponse
    """


# PUT /graphs/{graph_id}
class UpdateGraphPathParameters(PathParameters):
    """Path parameters for the update graph endpoint."""

    graph_id: str


class UpdateGraphRequestBody(RequestBody, GraphUpdate):
    """Update graph request body.

    OpenAPI: GraphUpdate
    """


class UpdateGraphResponseBody(ResponseBody, GraphsResponse):
    """Update graph response body.

    OpenAPI: GraphsResponse
    """


# GET /graphs/{graph_id}/export/cypher
class ExportGraphCypherPathParameters(PathParameters):
    """Path parameters for the export cypher endpoint."""

    graph_id: str


class ExportGraphCypherResponseBody(ResponseBody, CypherResponse):
    """Extract cypher response body.

    OpenAPI: CypherResponse
    """


# POST /graphs/{graph_id}/query
class QueryGraphPathParameters(PathParameters):
    """Path parameters for the query graph endpoint."""

    graph_id: str


class QueryGraphRequestBody(RequestBody, QueryGraphRequest):
    """Query graph request body.

    OpenAPI: QueryGraphRequest
    """


class QueryGraphResponseBody(ResponseBody, DetailedGraphsResponse):
    """Query graph response body.

    OpenAPI: DetailedGraphsResponse
    """


# GET /graphs/{graph_id}/triples
class GetGraphTriplesPathParameters(PathParameters):
    """Path parameters for the get graph triples endpoint."""

    graph_id: str


class GetGraphTriplesQueryParameters(QueryParameters):
    """Query parameters for the get graph triples endpoint."""

    skip: int | None = None
    limit: int | None = None
    order: Literal["ascending", "descending"] | None = None


class GetGraphTriplesResponseBody(ResponseBody, GraphsDetailedTripleResponse):
    """Graph triples response body.

    OpenAPI: GraphsDetailedTripleResponse
    """
