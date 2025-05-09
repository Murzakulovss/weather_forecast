from rest_framework import status
from drf_spectacular.utils import extend_schema
from .services.weather_api import get_weather
from drf_spectacular.utils import OpenApiParameter, OpenApiTypes
from .serializers import WeatherSerializer, ErrorSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import UserCity
from .serializers import UserCitySerializer
from .serializers import UserCityCreateSerializer

@method_decorator(cache_page(60 * 10), name='get')
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
            200: WeatherSerializer,
            404: ErrorSerializer,
            429: ErrorSerializer
        }
    )
    def get(self, request):
        city = request.GET.get("city", "Bishkek")
        data = get_weather(city)
        if "error" in data:
            return Response(data, status=status.HTTP_404_NOT_FOUND)
        return Response(WeatherSerializer(data).data)


class UserCityListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        cities = UserCity.objects.filter(user=request.user)
        serializer = UserCitySerializer(cities, many=True)
        return Response(serializer.data)


class UserCityCreateView(APIView):
    permission_classes = [IsAuthenticated]

    @extend_schema(
        request=UserCityCreateSerializer,  # указываем сериализатор для тела запроса
        responses={201: UserCityCreateSerializer}  # указываем сериализатор для успешного ответа
    )
    def post(self, request):
        serializer = UserCityCreateSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
