
from django.urls import path
from .views import RegisterView, LoginView, BusListCreateView, UserBookingView, BusDetailView, BookingView


urlpatterns = [
    path('buses/', BusListCreateView.as_view(), name='bus-list'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('user/<int:user_id>/bookings/', UserBookingView.as_view(), name='user-bookings'),
    path('booking/', BookingView.as_view(), name='booking'),
]