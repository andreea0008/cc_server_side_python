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


class SocialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Social
        fields = ['name_social_network', 'link_social_network']


class PhonesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phones
        fields = '__all__'


class LocationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CategoryEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoryEvent
        fields = ['categoryName']


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    actor = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'


class ImageEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageEvent
        fields = ['image']


class EventItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventItem
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(many=True, read_only=True)
    images = ImageEventSerializer(many=True, read_only=True, source='image_event')

    class Meta:
        model = Event
        fields = '__all__'


class PublicPlaceSerializer(serializers.ModelSerializer):
    working_days_schedule = WorkingScheduleNestedSerializer(many=True, read_only=True)
    holidays_schedule = HolidayScheduleNestedSerializer(many=True, read_only=True)
    social = SocialSerializer(many=True, read_only=True)
    phones = PhonesSerializer(many=True, read_only=True)
    location = LocationsSerializer(many=True, read_only=True, source='locations')
    event = EventSerializer(many=True, read_only=True)

    class Meta:
        model = PublicPlace
        fields = '__all__'
