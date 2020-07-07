from django.urls import path

from .views import BookingCreateView, SuccessView

urlpatterns = [
    path('', BookingCreateView.as_view()),
    path('success/<int:pk>', SuccessView.as_view(), name='success'),
]
