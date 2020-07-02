from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('country', views.CountryView)
router.register('city', views.CityView)
router.register('public_place', views.PublicPlaceView)
router.register('location', views.LocationView)
router.register('category', views.CategoryView)
router.register('working-schedule', views.WorkingScheduleView)
router.register('holiday-schedule', views.HolidayScheduleView)
router.register('phone_contacts', views.PhoneContactView)
router.register('socials', views.SocialView)
router.register('social_info', views.SocialInfoView)

urlpatterns = [
    path('', include(router.urls)),
]


