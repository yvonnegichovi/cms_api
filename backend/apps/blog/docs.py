from drf_spectacular.utils import extend_schema, OpenApiExample, OpenApiResponse
from rest_framework import status
from .serializers import PostSerializer
from .utils.schema import (
    create_success_example,
    get_standard_responses,
    standard_api_schema,
)

post_list_docs = extend_schema(
    summary="List all blog posts",
    description="Returns a list of blog posts ordered by creation date.",
    responses={200: PostSerializer(many=True)},
    tags=["blog"]
)

post_detail_docs = extend_schema(
    summary="Retrieve a single blog post",
    description="Get a specific blog post by its ID.",
    responses={200: PostSerializer},
    tags=["blog"]
)

post_create_docs = extend_schema(
    summary="Create a new blog post",
    description="Creates and returns a new blog post.",
    request=PostSerializer,
    responses={
       201: create_success_example(
            "Successful creation",
            {
                "id": 1,
                "title": "My first Blog post",
                "content": "Pied piper was the first project for Richard Henderson on the Silicon Valley.",
                "created_at": "2025-09-15T11:37:19.452Z",
                "updated_at": "2025-09-15T11:37:19.452Z",
            },
            message="Post created successfully",
            status_code=201,
        ),
        **get_standard_responses("Post"),
    },
    tags=["blog"],
)
