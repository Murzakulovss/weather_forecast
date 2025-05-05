from rest_framework import serializers

class WeatherSerializer(serializers.Serializer):
    city = serializers.CharField()
    temperature = serializers.FloatField()
    description = serializers.CharField()
    icon = serializers.URLField()
