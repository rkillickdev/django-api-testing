from django.db import models

# Create your models here.


class Place(models.Model):
    api_id = models.CharField(max_length=200, unique=True, null=False)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.api_id