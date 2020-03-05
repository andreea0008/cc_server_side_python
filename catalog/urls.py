from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('category', views.CategoryView)
router.register('country', views.CountryView)
router.register('city', views.CityView)
router.register('public-place', views.PublicPlaceView)
router.register('working-schedule', views.WorkingScheduleView)
router.register('holiday-schedule', views.HolidayScheduleView)
router.register('social', views.SocialNetworkView)
router.register('phone', views.PhonesView)
router.register('location', views.LocationView)
router.register('comment', views.CommentsView)
router.register('event-category', views.CategoryEventView)
router.register('actor', views.ActorView)
router.register('movie', views.MovieView)
router.register('event', views.EventView)
router.register('event_item', views.EventItemView)
router.register('image_movie', views.EventView)

urlpatterns = [
    path('', include(router.urls)),
]


