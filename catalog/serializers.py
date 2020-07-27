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


class LocationSerializer(serializers.ModelSerializer):
    phone = PhoneContactSerializer(many=True, read_only=True, source='phones')
    holiday_schedule = HolidayScheduleSerializer(many=True, read_only=True, source='holidays_schedule')
    working_schedule = WorkingScheduleSerializer(many=True, read_only=True, source='working_days_schedule')

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
    public_place_city = serializers.ReadOnlyField()
    public_place_country = serializers.ReadOnlyField()
    public_place_category = serializers.ReadOnlyField()
    
    class Meta:
        model = PublicPlace
        fields = '__all__'
