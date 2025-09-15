from django.shortcuts import render
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer
from . import docs

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer


    @docs.post_list_docs
    def list(self, request, *args, **kwargs):
        """Lists all blog posts"""
        return super().list(request, *args, **kwargs)

    @docs.post_detail_docs
    def retrieve(self, request, *args, **kwargs):
        """Retrieves a blog post"""
        return super().retrieve(request, *args, **kwargs)

    @docs.post_create_docs
    def create(self, request, *args, **kwargs):
        """Creates a blog post"""
        return super().create(request, *args, **kwargs)
