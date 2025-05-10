from .views import WeatherAPIView, UserCityCreateView, UserCityUpdateView, UserCityDeleteView
from django.urls import path
from .views import UserCityListView

urlpatterns = [
    path("api/weather/", WeatherAPIView.as_view()),
    path("user/cities/", UserCityListView.as_view(), name="user-cities"),
    path("user/cities/create/", UserCityCreateView.as_view(), name="user-cities-create"),
    path("user/cities/<int:pk>/", UserCityUpdateView.as_view(), name="user-city-update"),
    path("user/cities/<int:pk>/delete/", UserCityDeleteView.as_view(), name="user-city-delete"),
]

