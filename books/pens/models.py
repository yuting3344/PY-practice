from django.db import models


class Pen(models.Model):
    number = models.CharField(max_length=100)
    length = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
