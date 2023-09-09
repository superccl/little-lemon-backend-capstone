from datetime import datetime
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from restaurant.models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

class MenuItemListCreateAPIView(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def post(self, request, *args, **kwargs):
        # add permission to allow staff only
        serializer = MenuSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)
    
class BookingListCreateAPIView(generics.ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get(self, request, *args, **kwargs):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.filter(reservation_date=date)
        else:
            bookings = self.queryset.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    
    def post(self, request, *args, **kwargs):
        # add permission to allow staff only
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, HTTP_201_CREATED)
