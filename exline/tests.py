import json

from django.urls import reverse
from django.test import TestCase, Client

from exline.models import City
from exline.api import ExlineApi
from exline.utils import get_cities

# Create your tests here.
class TestExlineApi(TestCase):
    def setUp(self):
        self.client = ExlineApi(
            exline_server="https://api.exline.systems/",
            origin_id=4,
            pricing_policy="im_2021",
        )

    def test_calculate(self):
        obj = self.client.calculate(destination_id=4, weight=2.0)
        calc = obj.get("calculations")
        standard = calc.get("standard")
        express = calc.get("express")

        self.assertTrue(calc)
        self.assertTrue(standard)
        self.assertTrue(express)

        self.assertTrue(standard["price"])
        self.assertTrue(express["price"])

        self.assertTrue(standard["min"])
        self.assertTrue(express["min"])

        self.assertTrue(standard["max"])
        self.assertTrue(express["max"])

    def test_destinations(self):
        obj = self.client.destinations(country="KZ")

        self.assertTrue(obj.get("regions"))
        self.assertTrue(obj.get("meta"))


class TestUtils(TestCase):
    def setUp(self):
        self.client = ExlineApi(
            exline_server="https://api.exline.systems/",
            origin_id=4,
            pricing_policy="im_2021",
        )

    def test_get_cities(self):
        obj = self.client.destinations(country="KZ")
        count = obj.get("meta").get("total")

        City.objects.create(
            city_id=999999999,
            title="Some",
            cached_path="Some",
            zone="some",
            origin=False,
            destination=False,
            cached_parent="some",
        )

        get_cities(country="KZ")
        self.assertTrue(City.objects.all().count() == count)


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()

        City.objects.create(
            city_id=999999999,
            title="Some",
            cached_path="Some",
            zone="some",
            origin=False,
            destination=False,
            cached_parent="some",
        )

        City.objects.create(
            city_id=121331,
            title="Other",
            cached_path="Some",
            zone="some",
            origin=False,
            destination=False,
            cached_parent="some",
        )
        
        City.objects.create(
            city_id=123,
            title="absent",
            cached_path="Some",
            zone="some",
            origin=False,
            destination=False,
            cached_parent="some",
        )

    def test_search(self):
        r = self.client.get("/e/search/?search=o")
        self.assertTrue(len(r.json()) == 2)
