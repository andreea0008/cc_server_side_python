from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register('category', views.CategoryView)
router.register('country', views.CountryView)
router.register('city', views.CityView)
router.register('cafe', views.CafeView)

urlpatterns = [
    path('', include(router.urls)),
]


