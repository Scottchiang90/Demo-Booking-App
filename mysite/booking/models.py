from django.db import models

from booking import SERVICE_CHOICES, TIME_SLOT_CHOICES


class Booking(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    date = models.DateField()
    time_slot = models.CharField(max_length=2, choices=TIME_SLOT_CHOICES)
