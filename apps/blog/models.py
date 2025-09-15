"""
This model sets up and defines the database
"""

from django.db import models

class Post(models.Model):
    """
    Class that handles the class Post
    """
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
