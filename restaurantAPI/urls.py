from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.MenuItemListCreateAPIView.as_view(), name="menu"),
    path('bookings/', views.BookingListCreateAPIView.as_view(), name='bookings'),
]