from rest_framework import serializers
from rest_framework import serializers
from .models import UserCity

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
    icon = serializers.URLField()
    feels_like = serializers.FloatField()
    weather_summary = serializers.CharField(source="description")

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()

class UserCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCity
        fields = ['id', 'city']

class UserCityCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCity
        fields = ['city']