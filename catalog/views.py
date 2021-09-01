from datetime import datetime, timedelta

import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import *
from rest_framework.views import APIView
from dateutil import parser

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
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['location', 'type_event']
    search_fields = ['title_event', 'description_event', 'description_event']
    ordering_fields = ['rating']
    ordering = ['rating']

    def get_queryset(self):
        queryset = Event.objects.all()
        startdate = datetime.today()
        start_data_event_query_params = self.request.query_params.get('start_data_event')
        date_event_query_params = self.request.query_params.get('date')

        enddate = startdate + timedelta(days=30)
        if date_event_query_params:
            dt = datetime.strptime(date_event_query_params, '%Y-%m-%dT%H:%M:%S')
            date = dt.date()
            time = dt.time()

            if startdate < dt:
                startdate = dt

            queryset = Event.objects.filter(sessions_event__date__range=[startdate, enddate])

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


class EventSessionView(viewsets.ModelViewSet):
    queryset = EventSession.objects.all()
    serializer_class = EventSessionSerializer


class ClientMessageView(viewsets.ModelViewSet):
    queryset = ClientMessage.objects.all()
    serializer_class = ClientMessageSerializer



