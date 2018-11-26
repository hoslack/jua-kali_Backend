from django.db import models
from django.contrib.postgres.fields import ArrayField
from ..authentication.models import User


class Product(models.Model):

    name = models.TextField(max_length=255)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    producer = models.ForeignKey(User, on_delete=models.CASCADE,
                                 db_column='producer')
    product_type = models.TextField(max_length=255)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    images = ArrayField(
        models.CharField(max_length=1000, blank=True),
        size=20,
        null=True,
        blank=True)
    verified = models.BooleanField(default=False)
    category = models.CharField(max_length=50)
    sub_category = models.CharField(max_length=50)

    class Meta:
        """Order by time created, the most recently created is at the top."""

        ordering = ('createdAt',)
