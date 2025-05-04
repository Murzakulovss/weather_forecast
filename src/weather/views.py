from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .services.weather_api import get_weather

class WeatherAPIView(APIView):
    def get(self, request):
        city = request.GET.get("city", "Bishkek")
        data = get_weather(city)
        if "error" in data:
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        return Response(data)
from django.shortcuts import render
# Create your views here.
