from django.contrib import admin

from booking.models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('name', 'service', 'date', 'time_slot')
    search_fields = ['name', 'service', 'date']
    ordering = ['-date']
