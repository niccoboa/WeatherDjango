from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import WeatherForecast
from .serializer import WeatherForecastSerializer
from django.shortcuts import render, redirect


# Create your views here.
def homepage(request):
    return render(request, 'index.html')

class WeatherForecastInfo(APIView):
    
    def get_permissions(self):
        if self.request.method in ['POST', 'DELETE']:
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def handle_no_permission(self):
        if self.request.method in ['POST', 'DELETE'] and not self.request.user.is_authenticated:
            message = "Please log in to perform this action."
            return Response({"detail": message}, status=403)
        super().handle_no_permission()


    def get(self, request):
        # extracting attributes
        id = request.query_params.get('id')
        location = request.query_params.get('location')
        date = request.query_params.get('date')
        time = request.query_params.get('time')


        if id:
            return self.getForecastById(id)
        elif location and not date and not time:
            return self.getForecastsByLocation(location)
        elif location and date and not time:
            return self.getForecastsByLocationAndDate(location, date)
        elif location and date and time:
            return self.getForecastsByLocationDateAndTime(location, date, time)
        elif not location and not date and not time:
            return self.getAllForecasts()
        else:
            msg = {"msg": "Invalid parameters provided"}
            return Response(msg, status=status.HTTP_400_BAD_REQUEST)

    def getForecastById(self, id):
        return self.getForecastResponse(WeatherForecast.objects.filter(id=id))

    def getForecastsByLocation(self, location):
        return self.getForecastResponse(WeatherForecast.objects.filter(location=location))

    def getForecastsByLocationAndDate(self, location, date):
        return self.getForecastResponse(WeatherForecast.objects.filter(location=location, date=date))

    def getForecastsByLocationDateAndTime(self, location, date, time):
        return self.getForecastResponse(WeatherForecast.objects.filter(location=location, date=date, time=time))

    def getAllForecasts(self):
        return self.getForecastResponse(WeatherForecast.objects.all())

    def getForecastResponse(self, queryset):
        try:
            obj = queryset
            if not obj:
                raise WeatherForecast.DoesNotExist
            serializer = WeatherForecastSerializer(obj, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except WeatherForecast.DoesNotExist:
            msg = {"msg": "No forecast found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
    
    #def patch(self, request):
    #   example: PATCH > http://127.0.0.1:8000/weather_app/forecasts/?id=5
    #    giving { "description": "Lightning" } 

    #    id = request.query_params.get('id')
    #    
    #    try:
    #        obj = WeatherForecast.objects.get(id=id)
    #    except WeatherForecast.DoesNotExist:
    #        msg = {"msg": f"Forecast with id {id} not found"}
    #        return Response(msg, status=status.HTTP_404_NOT_FOUND)
    #    
    #    serializer = WeatherForecastSerializer(obj, data=request.data, partial=True)
    #
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_200_OK)
    #    
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        # example: DELETE > http://127.0.0.1:8000/weather_app/forecasts/?id=5
        id = request.query_params.get('id')

        try:
            obj = WeatherForecast.objects.get(id=id)
            obj.delete()
            return Response({"msg": "Forecast deleted"}, status=status.HTTP_204_NO_CONTENT)
        except WeatherForecast.DoesNotExist:
            msg = {"msg": "Forecast not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        data = request.data

        if isinstance(data, list):
            serializer = WeatherForecastSerializer(data=data, many=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            serializer = WeatherForecastSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
