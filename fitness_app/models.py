from django.db import models
from django.utils.translation import gettext as _

from fitness_app.mixins import NameMixin


class Program(NameMixin):
    """
    Program model
    """

    description = models.CharField(verbose_name=_('description'), max_length=500)
    place = models.CharField(verbose_name=_('place'), max_length=255)
    teacher = models.CharField(verbose_name=_('teacher'), max_length=255)
    start_time = models.TimeField(verbose_name=_('start time'))
    end_time = models.TimeField(verbose_name=_('end time'))
    weekDay = models.PositiveSmallIntegerField(verbose_name=_('week day'))
    appointment_id = models.UUIDField(verbose_name=_('appointment id'))
    service_id = models.UUIDField(verbose_name=_('service id'))
    pay = models.BooleanField(verbose_name=_('pay'), default=False)
    appointment = models.BooleanField(verbose_name=_('appointment'), default=False)
    color = models.CharField(verbose_name=_('color'), max_length=7)
    availability = models.SmallIntegerField(verbose_name=_('availability'))
    teacher_v2 = models.ForeignKey('Teacher', verbose_name=_('teacher v2'), on_delete=models.CASCADE,
                                   related_name='programs')

    class Meta:
        verbose_name = _('Program')
        verbose_name_plural = _('Programs')


class Teacher(NameMixin):
    """
    Teacher model
    """

    short_name = models.CharField(verbose_name=_('short name'), max_length=50)
    position = models.CharField(verbose_name=_('position'), max_length=255)
    imageUrl = models.URLField(verbose_name=_('image url'))

    class Meta:
        verbose_name = _('Teacher')
        verbose_name_plural = _('Teachers')
