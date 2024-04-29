from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    number = models.CharField(max_length=5)
    note = models.TextField(default="")
