import importlib.util
import inspect
import re
import subprocess

import pytest

import whyhow.raw as raw_module

SERVER_URL = "http://localhost:8001"


@pytest.fixture(scope="session")
def openapi_schemas(tmp_path_factory):
    path = tmp_path_factory.mktemp("data") / "schemas.py"

    # Generate schema files
    subprocess.run(
        [
            "datamodel-codegen",
            "--input-file-type",
            "json",
            "--output-model-type",
            "pydantic_v2.BaseModel",
            "--url",
            f"{SERVER_URL}/openapi.json",
            "--output",
            str(path),
        ],
        check=True,
    )

    # import dynamically generated module
    spec = importlib.util.spec_from_file_location("schemas", path)

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    schemas = {
        name: cls for name, cls in inspect.getmembers(module, inspect.isclass)
    }

    return schemas


@pytest.mark.openapi
@pytest.mark.parametrize(
    "our_schema",
    [cls for _, cls in inspect.getmembers(raw_module, inspect.isclass)],
)
def test_(our_schema, openapi_schemas):
    # check if the docstring continues OpenAPI link

    pattern = r"OpenAPI:\s*(\w+)"

    # Search the pattern in the docstring
    match = re.search(pattern, our_schema.__doc__)

    # If a match is found, return the captured group (the response name)
    if match:
        openapi_schema_name = match.group(1)
    else:
        pytest.skip("Our schema does not have an OpenAPI link")

    if openapi_schema_name not in openapi_schemas:
        pytest.skip("Linked OpenAPI schema not found")

    openapi_schema = openapi_schemas[openapi_schema_name]
    openapi_dicts = [
        v
        for k, v in openapi_schema.model_json_schema()["$defs"].items()
        if k.startswith("Properties")
    ]

    if len(openapi_dicts) == 0:
        pytest.skip("OpenAPI schema does not have properties")
    elif len(openapi_dicts) > 1:
        # this happens when there is a property called "properties"
        # you take the one with the highest identifier because
        # the parent is always defined after the children

        openapi_dicts = sorted(openapi_dicts, key=lambda x: x["title"])

    openapi_dict = openapi_dicts[0]

    openapi_properties = set(openapi_dict["properties"].keys())
    our_properties = set(our_schema.model_json_schema()["properties"].keys())

    assert openapi_properties == our_properties

    openapi_required = set(openapi_dict.get("required", []))
    our_required = set(our_schema.model_json_schema().get("required", []))

    assert openapi_required == our_required
