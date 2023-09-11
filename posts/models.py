from django.db import models

# Create your models here.
class Post(models.Model):
    text = models.TextField
# posts/models.py
from django.db import models
class Post(models.Model):
    text = models.TextField()
def __str__(self):
    return self.text[:50]