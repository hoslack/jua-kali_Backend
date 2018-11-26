from django.db import models
from ..authentication.models import User
from ..products.models import Product


class Order(models.Model):

    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE,
                              db_column='owner')
    product = models.ForeignKey(Product, on_delete=models.CASCADE,
                                db_column='product')
    quantity = models.IntegerField()
    confirmed = models.BooleanField(default=False)
    delivered = models.BooleanField(default=False)

    class Meta:
        """Order by time created, the most recently created is at the top."""

        ordering = ('createdAt',)
