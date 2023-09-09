from datetime import datetime
from django.shortcuts import render

# Create your views here.
from restaurant.models import Menu, Booking
from .serializers import MenuSerializer, BookingSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_404_NOT_FOUND

class MenuViewSet(ViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        queryset = self.queryset.all()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        menu_item = self.queryset.filter(pk=pk).first()
        if not menu_item:
            return Response({'message': 'Menu item not found'}, status=HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(menu_item)
        return Response(serializer.data)

    def update(self, request, pk=None):
        menu_item = self.queryset.filter(pk=pk).first()
        if not menu_item:
            return Response({'message': 'Menu item not found'}, status=HTTP_404_NOT_FOUND)
        serializer = self.serializer_class(menu_item, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        menu_item = self.queryset.filter(pk=pk).first()
        if not menu_item:
            return Response({'message': 'Menu item not found'}, status=HTTP_404_NOT_FOUND)
        menu_item.delete()
        return Response(status=HTTP_204_NO_CONTENT)

    
class BookingViewSet(ViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

    def get_permissions(self):
        if self.action == 'list' or self.action == 'retrieve':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permission_classes]

    def list(self, request):
        date = request.GET.get('date')
        if date:
            bookings = Booking.objects.filter(reservation_date=date)
        else:
            bookings = self.queryset.all()
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        booking = self.queryset.filter(pk=pk).first()
        if not booking:
            return Response({'message': 'Booking not found'}, status=HTTP_404_NOT_FOUND)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def update(self, request, pk=None):
        booking = self.queryset.filter(pk=pk).first()
        if not booking:
            return Response({'message': 'Booking not found'}, status=HTTP_404_NOT_FOUND)
        serializer = BookingSerializer(booking, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        booking = self.queryset.filter(pk=pk).first()
        if not booking:
            return Response({'message': 'Booking not found'}, status=HTTP_404_NOT_FOUND)
        booking.delete()
        return Response(status=HTTP_204_NO_CONTENT)