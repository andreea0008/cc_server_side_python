from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class CountrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Country
        fields = '__all__'


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['social_name']


class PhoneContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneContact
        fields = ['phone']


class HolidayScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaySchedule
        fields = ['day', 'work_time_from', 'work_time_to', 'break_time_from', 'break_time_to']


class WorkingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingSchedule
        fields = ['day', 'work_time_from', 'work_time_to', 'break_time_from', 'break_time_to']


class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventType
        fields = ['type']


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['currency_name']


class ImageEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEvent
        fields = ['image', 'name_event']


class EventSerializer(serializers.ModelSerializer):
    event_type_name = serializers.ReadOnlyField()
    location_address = serializers.ReadOnlyField()
    location_lat = serializers.ReadOnlyField()
    location_lng = serializers.ReadOnlyField()
    lacation_inclusive = serializers.ReadOnlyField()
    name_currency = serializers.ReadOnlyField()

    class Meta:
        model = Event
        fields = '__all__'


class LanguageMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageMovie
        fields = ['language']


class MovieSessionSerializer(serializers.ModelSerializer):
    currency_name = serializers.ReadOnlyField()

    class Meta:
        model = MovieSession
        fields = '__all__'


class CinemaSerializer(serializers.ModelSerializer):
    movie_session = MovieSessionSerializer(many=True, read_only=True, source='cinema')
    language_movie = serializers.ReadOnlyField()

    class Meta:
        model = Cinema
        fields = '__all__'


class MovieEventSerializer(serializers.ModelSerializer):
    cinema = CinemaSerializer(many=True, read_only=True, source='movie_name')
    event_type_name = serializers.ReadOnlyField()
    location_address = serializers.ReadOnlyField()
    location_lat = serializers.ReadOnlyField()
    location_lng = serializers.ReadOnlyField()
    lacation_inclusive = serializers.ReadOnlyField()
    name_currency = serializers.ReadOnlyField()

    class Meta:
        model = MovieEvent
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    phone = PhoneContactSerializer(many=True, read_only=True, source='phones')
    holiday_schedule = HolidayScheduleSerializer(many=True, read_only=True, source='holidays_schedule')
    working_schedule = WorkingScheduleSerializer(many=True, read_only=True, source='working_days_schedule')
    event = EventSerializer(many=True, read_only=True, source='event_location')

    class Meta:
        model = Location
        fields = '__all__'


class SocialInfoSerializer(serializers.ModelSerializer):
    public_place_name = serializers.ReadOnlyField()

    class Meta:
        model = SocialInfo
        fields = ['link', 'name_social', 'public_place_name']


class PublicPlaceSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True, source='locations')
    social_info = SocialInfoSerializer(many=True, read_only=True)
    movie_sessions = MovieSessionSerializer(many=True, read_only=True, source='movie_session')
    public_place_city = serializers.ReadOnlyField()
    public_place_country = serializers.ReadOnlyField()
    public_place_category = serializers.ReadOnlyField()

    class Meta:
        model = PublicPlace
        fields = '__all__'



