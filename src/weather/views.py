from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema
from .services.weather_api import get_weather
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes
class WeatherAPIView(APIView):

    @extend_schema(
        summary="Получить погоду по городу",
        parameters=[
            OpenApiParameter(
                name="city",
                type=OpenApiTypes.STR,
                required=False,
                location=OpenApiParameter.QUERY,
                description="Название города (например: Bishkek)"
            )
        ],
        responses={
            200: {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "example": "Bishkek"},
                    "temperature": {"type": "number", "example": 22.4},
                    "description": {"type": "string", "example": "ясно"},
                    "icon": {"type": "string", "example": "https://..."},
                }
            },
            404: {
                "type": "object",
                "properties": {
                    "error": {"type": "string", "example": "City not found or API error"}
                }
            }
        }
    )
    def get(self, request):
        city = request.GET.get("city", "Bishkek")
        data = get_weather(city)
        if "error" in data:
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        return Response(data)
from django.shortcuts import render
# Create your views here.
