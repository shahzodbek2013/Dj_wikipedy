from django.db import models
from django.contrib.auth.models import User

class Page(models.Model):
    title = models.CharField(max_length=100)
    context = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f"ID: {self.id} - {self.title}"
    