from .views import WeatherAPIView, UserCityCreateView
from django.urls import path
from .views import UserCityListView

urlpatterns = [
    path("api/weather/", WeatherAPIView.as_view()),
    path("user/cities/", UserCityListView.as_view(), name="user-cities"),
    path("user/cities/create/", UserCityCreateView.as_view(), name="user-cities-create"),
]

