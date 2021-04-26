import json
import sys
from django.db import transaction
from django.core.management.base import BaseCommand

from catalog.models import Location, PublicPlace, SocialInfo, WorkingSchedule, PhoneContact


class Command(BaseCommand):
    help = 'Load datasets of ...'

    @transaction.atomic
    def get_data(self):
        with open('data.txt', mode='r', encoding='utf-8') as json_file:
            data = json.load(json_file)
            for obj in data:
                public_place, _isCreated = PublicPlace.objects.get_or_create(
                    name=obj['name'],
                    city_id=obj['city_id'],
                    country_id=obj['country_id'],
                    category_id=obj['category_id']
                )

                location, _isCreated = Location.objects.get_or_create(
                    public_place=public_place,
                    address=obj['address']
                )
                # social
                if obj['socials']['facebook']:
                    SocialInfo.objects.get_or_create(
                        public_place=public_place,
                        name_social="Facebook",
                        link=obj['socials']['facebook']
                    )

                if obj['socials']['facebook']:
                    SocialInfo.objects.get_or_create(
                        public_place=public_place,
                        name_social="Instagram",
                        link=obj['socials']['instagram']
                    )

                # schedule
                schedule_object = obj['schedule']
                days_names = [('Mon', 'Monday'), ('Tue', 'Tuesday'), ('Wed', 'Wednesday'), ('Thu', 'Thursday'),
                              ('Fri', 'Friday'), ('Sat', 'Saturnday'), ('Sun', 'Sunday')]
                if schedule_object:
                    for day_tuple_item in days_names:
                        day_name_short = day_tuple_item[0]
                        day_name_long = day_tuple_item[1]

                        schedule_in_mon_from_to = schedule_object[day_name_short][0]
                        schedule_in_mon_from = schedule_object[day_name_short][0][0:5]
                        schedule_in_mon_to = schedule_object[day_name_short][0][8:]

                        break_in_mon = schedule_object[day_name_short][1]

                        if 'Без перерви' == break_in_mon:
                            break_from = '00:00'
                            break_to = '00:00'
                        else:
                            break_from = schedule_object[day_name_short][1][0:5]
                            break_to = schedule_object[day_name_short][1][8:]

                        WorkingSchedule.objects.get_or_create(
                            location=location,
                            day=day_name_long,
                            work_time_from=schedule_in_mon_from,
                            work_time_to=schedule_in_mon_to,
                            break_time_from=break_from,
                            break_time_to=break_to
                        )

                # phone
                for phone in obj['phones']:
                    PhoneContact.objects.get_or_create(
                        location=location,
                        phone=phone
                    )

    def handle(self, *args, **options):
        self.get_data()
        self.stdout.write(self.style.SUCCESS('Script successfully finished!'))
