from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    parent = models.ForeignKey(
        'self',
        related_name='children',
        on_delete=models.CASCADE,
        default=None,
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('name',)
