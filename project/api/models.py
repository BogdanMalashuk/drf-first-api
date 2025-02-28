from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    author = models.CharField(max_length=255, verbose_name="author")
    year = models.PositiveIntegerField(verbose_name="year")
