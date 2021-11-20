from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=100, blank=True, default='')
    body = models.FileField(blank=True, default='')
    url = models.CharField(max_length=100, blank=True, default='')
