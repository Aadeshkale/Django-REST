from django.db import models


class Emp(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=100)
    address = models.CharField(max_length=60)

