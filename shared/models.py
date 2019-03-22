from uuid import uuid4

from django.db import models


class BaseCompany(models.Model):
    """
    Base abstract (concrete) class for companies.
    Example: Contractor, Consultant, Client
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    short_name = models.CharField(max_length=120)
    long_name = models.CharField(
        max_length=255,
        help_text='Company official full name.'
    )
    address = models.TextField(blank=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.short_name


class Contractor(BaseCompany):
    pass


class Consultant(BaseCompany):
    pass


class Client(BaseCompany):
    pass


class Work(models.Model):
    """
    Major construction works.
    Example: Earthworks, Concrete works, Block work, Electric installation
    """
    title = models.CharField(max_length=120)
    icon = models.CharField(max_length=120, blank=True)
    order = models.IntegerField(unique=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'Work'
        verbose_name_plural = 'Works'
        ordering = ('order', )

    def __str__(self):
        return self.title


class Activity(models.Model):
    """
    Minor construction activities.
    Example: formwork, painting, gypsum, pipe, etc
    """
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.name
