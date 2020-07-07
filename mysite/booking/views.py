from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from booking.forms import BookingForm
from booking.models import Booking


class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    success_url = '/success/'

    def get_success_url(self):
        return reverse_lazy('success', kwargs={'pk': self.object.pk})


class SuccessView(DetailView):
    template_name = "booking/thanks.html"
    queryset = Booking.objects.all()
