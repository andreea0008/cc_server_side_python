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


class PhoneContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneContact
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    phone = PhoneContactSerializer(many=True, read_only=True)

    class Meta:
        model = Location
        fields = '__all__'


class PublicPlaceSerializer(serializers.ModelSerializer):
    location = LocationSerializer(many=True, read_only=True, source='locations')

    class Meta:
        model = PublicPlace
        fields = '__all__'


class WorkingScheduleNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingSchedule
        fields = [
            'id', 'day', 'work_time_from', 'work_time_to', 'break_time_from', 'break_time_to'
        ]


class HolidayScheduleNestedSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaySchedule
        fields = [
            'id', 'date', 'work_time_from', 'work_time_to', 'break_time_from', 'break_time_to'
        ]


class WorkingScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkingSchedule
        fields = '__all__'


class HolidayScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HolidaySchedule
        fields = '__all__'



