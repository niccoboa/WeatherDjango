from rest_framework import serializers
from .models import WeatherForecast



class WeatherForecastSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherForecast
        exclude = ['id']        # i don't care about the id