from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializers import *
from rest_framework import views


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class ItemBaseView(viewsets.ModelViewSet):
    queryset = ItemBase.objects.all()
    serializer_class = ItemBaseSerializer


class CafeView(viewsets.ModelViewSet):
    queryset = Cafe.objects.all()
    serializer_class = CafeSerializer


class WorkingScheduleView(viewsets.ModelViewSet):
    queryset = WorkingSchedule.objects.all()
    serializer_class = WorkingScheduleSerializer


class HolidayScheduleView(viewsets.ModelViewSet):
    queryset = HolidaySchedule.objects.all()
    serializer_class = HolidayScheduleSerializer