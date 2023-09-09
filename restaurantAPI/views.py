from datetime import datetime
from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from restaurant.models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED

class MenuListCreateAPIView(generics.ListCreateAPIView):
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
    
class MenuItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get(self, request, *args, **kwargs):
        menu_item = self.queryset.filter(pk=kwargs['pk']).first()
        if not menu_item:
            return Response({'message': 'Menu item not found'}, status=404)
        serializer = MenuSerializer(menu_item)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        menu_item = self.queryset.filter(pk=kwargs['pk']).first()
        if not menu_item:
            return Response({'message': 'Menu item not found'}, status=404)
        serializer = MenuSerializer(menu_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        menu_item = self.queryset.filter(pk=kwargs['pk']).first()
        if not menu_item:
            return Response({'message': 'Menu item not found'}, status=404)
        menu_item.delete()
        return Response(status=204)

    
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

class BookinkItemDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.request.method == 'GET':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]
    
    def get(self, request, *args, **kwargs):
        booking = self.queryset.filter(pk=kwargs['pk']).first()
        if not booking:
            return Response({'message': 'Booking not found'}, status=404)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    def put(self, request, *args, **kwargs):
        booking = self.queryset.filter(pk=kwargs['pk']).first()
        if not booking:
            return Response({'message': 'Booking not found'}, status=404)
        serializer = BookingSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        booking = self.queryset.filter(pk=kwargs['pk']).first()
        if not booking:
            return Response({'message': 'Booking not found'}, status=404)
        booking.delete()
        return Response(status=204)