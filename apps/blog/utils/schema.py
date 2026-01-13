"""
Common API schema components for standardized documentation.

Reusable OpenAPI schema components for consistent docs
across all endpoints, following the standard response format.
"""

import uuid
from drf_spectacular.utils import OpenApiExample, OpenApiResponse, extend_schema
from rest_framework import status


def create_error_example(name, message, errors, status_code=400, request_id=None):
    """Factory for standardized error examples."""
    if request_id is None:
        request_id = f"err{str(uuid.uuid4())[:8]}"

    return OpenApiExample(
        name,
        value={
            "status": "error",
            "message": message,
            "data": None,
            "errors": errors,
            "request_id": request_id,
        },
        response_only=True,
        status_codes=[str(status_code)],
    )


def create_success_example(name, data, message="Operation successful", status_code=200, request_id=None):
    """Factory for standardized success examples."""
    if request_id is None:
        request_id = f"succ{str(uuid.uuid4())[:8]}"

    return OpenApiExample(
        name,
        value={
            "status": "success",
            "message": message,
            "data": data,
            "errors": None,
            "request_id": request_id,
        },
        response_only=True,
        status_codes=[str(status_code)],
    )


# --- Reusable error examples ---
validation_error_example = create_error_example(
    "Validation Error",
    "Validation failed",
    {"title": ["This field is required."]},
    status.HTTP_400_BAD_REQUEST,
)

authentication_error_example = create_error_example(
    "Authentication Error",
    "Authentication failed",
    {"detail": ["Authentication credentials were not provided."]},
    status.HTTP_401_UNAUTHORIZED,
)

permission_error_example = create_error_example(
    "Permission Denied",
    "Access denied",
    {"detail": ["You do not have permission to perform this action."]},
    status.HTTP_403_FORBIDDEN,
)

not_found_error_example = create_error_example(
    "Not Found",
    "Resource not found",
    {"detail": ["The requested resource was not found."]},
    status.HTTP_404_NOT_FOUND,
)

server_error_example = create_error_example(
    "Server Error",
    "An unexpected error occurred",
    {"detail": ["Internal server error occurred."]},
    status.HTTP_500_INTERNAL_SERVER_ERROR,
)


def get_standard_responses(resource_name="Resource"):
    """Return standard responses for common errors."""
    return {
        status.HTTP_400_BAD_REQUEST: validation_error_example,
        status.HTTP_401_UNAUTHORIZED: authentication_error_example,
        status.HTTP_403_FORBIDDEN: permission_error_example,
        status.HTTP_404_NOT_FOUND: not_found_error_example,
        status.HTTP_500_INTERNAL_SERVER_ERROR: server_error_example,
    }


def standard_api_schema(**schema_args):
    """
    Map OpenApiExample -> OpenApiResponse for Swagger display.
    """
    responses = {}
    if "responses" in schema_args:
        for status_code, example in schema_args["responses"].items():
            if isinstance(example, OpenApiExample):
                responses[status_code] = OpenApiResponse(
                    response=dict, examples=[example]
                )
            else:
                responses[status_code] = example
        schema_args["responses"] = responses
    return extend_schema(**schema_args)
