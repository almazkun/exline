from rest_framework.response import Response
from rest_framework.views import APIView

from exline.models import City
from exline.api import ExlineApi
from exline.serializers import CitySerializer
from exline.utils import get_cities


exline_server = "https://api.exline.systems/"
origin_id = 4
pricing_policy = "im_2021"
# Create your views here.
class CalculateView(APIView):
    def get(self, *args, **kwargs):
        client = ExlineApi(
            exline_server=exline_server,
            origin_id=origin_id,
            pricing_policy=pricing_policy,
        )
        destination_id = self.request.GET.get("destination_id")
        weight = self.request.GET.get("weight")
        r = client.calculate(destination_id=destination_id, weight=weight)
        return Response(r)


class CitySearch(APIView):
    def get(self, *args, **kwargs):
        search = self.request.GET.get("search")
        cities = City.objects.filter(title__icontains=search).order_by("city_id")[:10]
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class CityListView(APIView):
    def get(self, *args, **kwargs):
        cities = City.objects.all().order_by("city_id")
        serializer = CitySerializer(cities, many=True)
        return Response(serializer.data)


class UpdateCityList(APIView):
    def get(self, *args, **kwargs):
        get_cities(country="KZ")
        return Response({"status":"ok"})