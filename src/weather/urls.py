from django.urls import path
from .views import WeatherAPIView

urlpatterns = [
    path("api/weather/", WeatherAPIView.as_view()),
]
