from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):

    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)
    """field will be updated whenever models are created"""
    updated = models.DateTimeField(auto_now=True)
    """field will be updated whenever models are saved"""

    class Meta:
        abstract = True
