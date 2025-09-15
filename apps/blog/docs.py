from drf_spectacular.utils import extend_schema, OpenApiParameter
from .serializers import PostSerializer

post_list_docs = extend_schema(
    summary="List all blog posts",
    description="Returns a list of blog posts ordered by creation date.",
    responses={200: PostSerializer(many=True)},
    tags=["Blog"]
)

post_detail_docs = extend_schema(
    summary="Retrieve a single blog post",
    description="Get a specific blog post by its ID.",
    responses={200: PostSerializer},
    tags=["Blog"]
)

post_create_docs = extend_schema(
    summary="Create a new blog post",
    description="Creates and returns a new blog post.",
    request=PostSerializer,
    responses={201: PostSerializer},
    tags=["Blog"]
)
