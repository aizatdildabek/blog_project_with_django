from django.db import models
from django.db.models import Q, CheckConstraint
from django.contrib.auth.models import User 

# Create your models here.

class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')

    def __str__(self) -> str:
        return f"{self.content} ({self.pk})"

    # class Meta:
    #     constraints = [
    #         CheckConstraint(
    #             check=Q(content__startswith="Hello"),
    #             name="content_starts_with_hello"
    #         )
    #     ]


class Comment(models.Model):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()    
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.content}"


class Category(models.Model):

    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.name}"