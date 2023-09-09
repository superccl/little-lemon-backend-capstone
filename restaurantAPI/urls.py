from django.urls import path
from . import views


urlpatterns = [
    path('menu/', views.MenuListCreateAPIView.as_view(), name="menu"),
    path('menu/<int:pk>/', views.MenuItemDetailAPIView.as_view(), name="menu_item"),
    path('bookings/', views.BookingListCreateAPIView.as_view(), name='bookings'),
    path('bookings/<int:pk>/', views.BookinkItemDetailAPIView.as_view(), name='booking'),
]