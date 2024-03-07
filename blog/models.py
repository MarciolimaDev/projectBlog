from django.db import models
from django.utils import dates
from datetime import datetime

# Create your models here.
class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    subTitle = models.CharField(max_length=255)
    description = models.TextField()
    dateAt = models.DateTimeField(default=datetime.now())