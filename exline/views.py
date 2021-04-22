from django.views import View
from django.views.generic import ListView
from django.http import JsonResponse

from rest_framework import viewsets

from exline.models import City
from exline.api import ExlineApi
from exline.serializers import CitySerializer
from exline.utils import get_cities


exline_server = "https://api.exline.systems/"
origin_id = 4
pricing_policy = "im_2021"
# Create your views here.
class CalculateView(View):
    def get(self, *args, **kwargs):
        client = ExlineApi(
            exline_server=exline_server,
            origin_id=origin_id,
            pricing_policy=pricing_policy,
        )
        destination_id = self.request.GET.get("destination_id")
        weight = self.request.GET.get("weight")
        r = client.calculate(destination_id=destination_id, weight=weight)
        return JsonResponse(r)


class CitySearch(View):
    def get(self, *args, **kwargs):
        search = self.request.GET.get("search")
        cities = City.objects.filter(title__icontains=search).order_by("city_id")[:10]
        serializer = CitySerializer(cities, many=True)
        return JsonResponse(serializer.data, safe=False)


class CityListView(viewsets.ModelViewSet):
    queryset = City.objects.all().order_by("city_id")
    serializer_class = CitySerializer


class UpdateCityList(View):
    def get(self, *args, **kwargs):
        get_cities(country="KZ")