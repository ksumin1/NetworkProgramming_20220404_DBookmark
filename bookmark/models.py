from django.db import models

# Create your models here.
class Bookmark(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()