from django.urls import path

from exline.views import CalculateView, CityListView, CitySearch, UpdateCityList


urlpatterns = [
    path("calculate/", CalculateView.as_view(), name="calculate_view"),
    path("cities/", CityListView.as_view(), name="cities"),
    path("search/", CitySearch.as_view(), name="search"),
    path("update/", UpdateCityList.as_view(), name="update"),
]
