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
        fields = "__all__"


class ItemBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemBase
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


class CafeSerializer(serializers.ModelSerializer):
    working_days_schedule = WorkingScheduleNestedSerializer(many=True, read_only=True)
    holidays_schedule = HolidayScheduleNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Cafe
        fields = '__all__'
