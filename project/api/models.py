from django.db import models
from rest_framework.reverse import reverse


class Book(models.Model):
    title = models.CharField(max_length=255, verbose_name="title")
    author = models.CharField(max_length=255, verbose_name="author")
    year = models.PositiveIntegerField(verbose_name="year")


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('Died', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'
