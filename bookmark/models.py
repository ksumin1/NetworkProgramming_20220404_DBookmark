from django.db import models

# Create your models here.
class Bookmark(models.Model):
    name = models.CharField(max_length=10)
    url = models.URLField()

    def __str__(self):
        return f'{self.name} : {self.url}'