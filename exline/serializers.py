from rest_framework import serializers

from exline.models import City


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        depth = 1
        fields = [
               "city_id",
               "title",
               "cached_path",
            ]
