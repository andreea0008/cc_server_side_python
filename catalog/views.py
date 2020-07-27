import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.generics import ListAPIView

from .serializers import *


class CategoryView(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CountryView(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer


class CityView(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class SocialView(viewsets.ModelViewSet):
    queryset = Social.objects.all()
    serializer_class = SocialSerializer


class PublicPlaceView(viewsets.ModelViewSet):
    queryset = PublicPlace.objects.all()
    serializer_class = PublicPlaceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('city', 'country',)


class LocationView(viewsets.ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('public_place', 'inclusive')


class PhoneContactView(viewsets.ModelViewSet):
    queryset = PhoneContact.objects.all()
    serializer_class = PhoneContactSerializer


class WorkingScheduleView(viewsets.ModelViewSet):
    queryset = WorkingSchedule.objects.all()
    serializer_class = WorkingScheduleSerializer


class HolidayScheduleView(viewsets.ModelViewSet):
    queryset = HolidaySchedule.objects.all()
    serializer_class = HolidayScheduleSerializer


class SocialInfoView(viewsets.ModelViewSet):
    queryset = SocialInfo.objects.all()
    serializer_class = SocialInfoSerializer


class EventTypeView(viewsets.ModelViewSet):
    queryset = EventType.objects.all()
    serializer_class = EventTypeSerializer


class EventView(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


class MovieEventView(viewsets.ModelViewSet):
    queryset = MovieEvent.objects.all()
    serializer_class = MovieEventSerializer


class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class LanguageMovieView(viewsets.ModelViewSet):
    queryset = LanguageMovie.objects.all()
    serializer_class = LanguageMovieSerializer
