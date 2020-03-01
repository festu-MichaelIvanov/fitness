import uuid

from django.db import models
from django.utils.translation import gettext as _


class NameMixin(models.Model):
    """
    Name mixin
    """

    name = models.CharField(verbose_name=_('name'), max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True
