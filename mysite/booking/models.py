from django.db import models
from django.db.models import DO_NOTHING

from booking import SERVICE_CHOICES, TIME_SLOT_CHOICES, POSITION_CHOICES


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    preferred_stylist = models.ForeignKey('Employee', on_delete=DO_NOTHING, null=True, blank=True)
    date = models.DateField()
    time_slot = models.CharField(max_length=2, choices=TIME_SLOT_CHOICES)

    def __str__(self):
        return '{} {}'.format(self.name, self.date)


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=2, choices=POSITION_CHOICES)

    def __str__(self):
        return '{1} {0}'.format(self.name, self.get_position_display())
