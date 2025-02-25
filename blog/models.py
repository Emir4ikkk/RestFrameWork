from django.db import models
from django.contrib.auth.models import User

class Publication(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="publications")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
