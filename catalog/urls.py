from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.conf import  settings
from django.conf.urls.static import static


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
router.register('event_type', views.EventTypeView)
router.register('event', views.EventView)
router.register('movie_event', views.MovieEventView)
router.register('currency', views.CurrencyView)
router.register('language_movie', views.LanguageMovieView)
router.register('movie_session', views.MovieSessionView)
router.register('image_event', views.ImageEventView)
router.register('cinema', views.CinemaView)
router.register('image_public_place', views.ImagePublicPlaceView)
router.register('client_message', views.ClientMessageView)
router.register('session_events', views.EventSessionView)
urlpatterns = [
    path('', include(router.urls)),
]



