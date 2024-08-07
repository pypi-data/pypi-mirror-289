import importlib.util
import inspect
import re
import subprocess
from typing import Any

import pytest

import whyhow.raw as raw_module

SERVER_URL = "http://localhost:8001"


def check_equal(
    prop: str,
    props_1: dict[str, Any],
    defs_1: dict[str, Any],
    props_2: dict[str, Any],
    defs_2: dict[str, Any],
) -> None:
    """Done for each property separately.

    WIP.
    """
    EXCLUDED_FIELDS = {"title", "description", "example"}

    assert prop in props_1
    assert prop in props_2

    fields_1 = {k for k in props_1[prop].keys() if k not in EXCLUDED_FIELDS}
    fields_2 = {k for k in props_2[prop].keys() if k not in EXCLUDED_FIELDS}

    assert fields_1 == fields_2

    for field in fields_1:
        v_1 = props_1[prop][field]
        v_2 = props_2[prop][field]

        if isinstance(v_1, dict):
            if "$ref" in v_1:
                ref_1 = v_1["$ref"].split("/")[-1]
                ref_2 = v_2["$ref"].split("/")[-1]

                def_1 = defs_1[ref_1]
                def_2 = defs_2[ref_2]

                sub_props_1 = def_1["properties"]
                sub_props_2 = def_2["properties"]

                assert set(sub_props_1.keys()) == set(sub_props_2.keys())

                breakpoint()
                for sub_prop in sub_props_1:
                    check_equal(
                        prop=ref_1,
                        props_1=sub_props_1,
                        defs_1=defs_1,
                        props_2=sub_props_2,
                        defs_2=defs_2,
                    )
            else:
                assert v_1 == v_2

    return True


@pytest.fixture(scope="session")
def openapi_schemas(tmp_path_factory):
    path = tmp_path_factory.mktemp("data") / "schemas.py"

    # Generate schema files
    subprocess.run(
        [
            "datamodel-codegen",
            "--enum-field-as-literal",
            "all",
            "--input-file-type",
            "openapi",
            "--reuse-model",
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

    openapi_schema = openapi_schemas[openapi_schema_name].model_json_schema()
    our_schema = our_schema.model_json_schema()

    our_properties = our_schema["properties"].keys()
    openapi_properties = openapi_schema["properties"].keys()
    assert set(our_properties) == set(openapi_properties)

    openapi_required = our_schema.get("required", [])
    our_required = our_schema.get("required", [])
    assert set(openapi_required) == set(our_required)

    # check if the properties are the same recursively
    # for prop in our_properties:
    #     check_equal(
    #         prop=prop,
    #         props_1=our_schema["properties"],
    #         defs_1=our_schema["$defs"],
    #         props_2=openapi_schema["properties"],
    #         defs_2=openapi_schema["$defs"],
    #     )
    #
