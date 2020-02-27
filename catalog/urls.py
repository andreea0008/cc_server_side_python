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
router.register('address', views.AddressView)

urlpatterns = [
    path('', include(router.urls)),
]


