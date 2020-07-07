from crispy_forms.helper import FormHelper
from django.forms import ModelForm, DateField, DateInput

from booking import TIME_SLOT_CHOICES
from booking.models import Booking


class BookingForm(ModelForm):
    date = DateField(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Booking
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()

        # check if time slot has been booked that day
        booking_date = cleaned_data.get('date')
        booking_time = cleaned_data.get('time_slot')
        if Booking.objects.filter(date=booking_date, time_slot=booking_time).exists():
            msg = "This time slot on {} at {} is not available.".format(booking_date,  dict(TIME_SLOT_CHOICES).get(booking_time))
            self.add_error('time_slot', msg)
