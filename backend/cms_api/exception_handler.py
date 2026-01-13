from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status as drf_status
from apps.blog.utils import standard_response

def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        status_messages = {
            400: "Bad request",
            401: "Unauthorized",
            402: "Payment required",
            403: "Forbidden",
            404: "Resource not found",
            500: "Internal server error",
        }

        message = status_messages.get(response.status_code, "Unexpected error")

        response.data = standard_response(
            data=None,
            message=message,
            status="error",
            errors=response.data,
        )
    else:
        response = Response(
            standard_response(
                data=None,
                message="Internal server error",
                status="error",
                errors={"detail": str(exc)},
            ),
            status=drf_status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

    return response
