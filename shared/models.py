from uuid import uuid4

from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class Company(models.Model):
    """
    Example: Contractor, Consultant, Client
    """
    CLIENT = 'CLIENT'
    CONTRACTOR = 'CONTRACTOR'
    CONSULTANT = 'CONSULTANT'
    SUBCONTRACTOR = 'SUBCONTRACTOR'

    type_choices = (
        (CLIENT, 'Client'),
        (CONTRACTOR, 'Contractor'),
        (CONSULTANT, 'Consultant'),
        (SUBCONTRACTOR, 'Sub-contractor')
    )

    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    short_name = models.CharField(max_length=120)
    long_name = models.CharField(
        max_length=255,
        help_text='Company official full name.'
    )
    address = models.TextField(blank=True)
    type = models.CharField(max_length=15, choices=type_choices)
    owner = models.ForeignKey(
        User,
        blank=True, null=True,
        on_delete=models.SET_NULL
    )

    class Meta:
        default_related_name = 'companies'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.short_name


class Activity(models.Model):
    """
    Minor construction activities.
    Example: formwork, painting, gypsum, pipe, etc
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=60)

    class Meta:
        verbose_name = 'Activity'
        verbose_name_plural = 'Activities'

    def __str__(self):
        return self.name


class Work(models.Model):
    """
    Major construction works.
    Example: Earthworks, Concrete works, Block work, Electric installation
    """
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
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
