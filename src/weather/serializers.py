from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
    icon = serializers.URLField()
    feels_like = serializers.FloatField()
    weather_summary = serializers.CharField(source="description")

class ErrorSerializer(serializers.Serializer):
    error = serializers.CharField()
