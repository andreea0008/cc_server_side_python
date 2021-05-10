from datetime import datetime, timedelta

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

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
    filter_fields = ('city', 'country')


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
    queryset = Event.objects.all().filter()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ['location', 'type_event']
    search_fields = ['title_event', 'description_event', 'description_event']

    def get_queryset(self):
        queryset = Event.objects.all().filter()
        startdate = datetime.today()
        start_data_event_query_params = self.request.query_params.get('start_data_event')
        print(start_data_event_query_params)
        if start_data_event_query_params is not None:
            startdate = datetime.strptime(start_data_event_query_params, "%Y-%m-%dT%H:%M:%SZ")

        enddate = startdate + timedelta(days=365)
        print(startdate, enddate)
        queryset = Event.objects.filter(start_data_event__range=[startdate, enddate])

        return queryset


class MovieEventView(viewsets.ModelViewSet):
    queryset = MovieEvent.objects.all()
    serializer_class = MovieEventSerializer


class CurrencyView(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer


class LanguageMovieView(viewsets.ModelViewSet):
    queryset = LanguageMovie.objects.all()
    serializer_class = LanguageMovieSerializer


class ImageEventView(viewsets.ModelViewSet):
    queryset = ImageEvent.objects.all()
    serializer_class = ImageEventSerializer


class ImagePublicPlaceView(viewsets.ModelViewSet):
    queryset = ImagePublicPlace.objects.all()
    serializer_class = ImagePublicPlaceSerializer


class MovieSessionView(viewsets.ModelViewSet):
    queryset = MovieSession.objects.all()
    serializer_class = MovieSessionSerializer


class CinemaView(viewsets.ModelViewSet):
    queryset = Cinema.objects.all()
    serializer_class = CinemaSerializer
