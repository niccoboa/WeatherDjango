from django.urls import path
from . import views
from .views import WeatherForecastInfo

urlpatterns = [
    # API endpoints
    path('forecasts/', WeatherForecastInfo.as_view(), name='forecasts'),
    path('', views.homepage),
    path('home/', views.homepage),
]


