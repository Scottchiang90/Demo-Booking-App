from django.test import TestCase

from booking.forms import BookingForm
from booking.models import Booking


class BookingFormTests(TestCase):
    def setUp(self):
        self.form_data = {'name': 'Customer 1',
                     'email': 'customer@email.com',
                     'service': 'Colouring',
                     'date': '2020-7-7',
                     'time_slot': '8'}

    def test_valid_timeslot(self):
        form = BookingForm(data=self.form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_timeslot(self):
        Booking.objects.create(**self.form_data)
        form = BookingForm(data=self.form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('time_slot'))
