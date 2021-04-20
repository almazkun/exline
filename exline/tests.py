from django.test import TestCase

from exline.api import ExlineApi

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


r = {
    "calculations": {
        "standard": {
            "price": 800,
            "fuel_surplus": 0,
            "declared_value_fee": 150,
            "human_range": "21 – 22 апреля",
            "min": 1,
            "max": 2,
            "id": 1133,
        },
        "express": {
            "price": 800,
            "fuel_surplus": 0,
            "declared_value_fee": 150,
            "human_range": "21 – 22 апреля",
            "min": 1,
            "max": 2,
        },
    }
}
