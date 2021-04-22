import logging

from exline.models import City
from exline.api import ExlineApi


logger = logging.getLogger(__name__)
exline_server = "https://api.exline.systems/"
origin_id = 4
pricing_policy = "im_2021"


def update_or_create_destination(update_info: dict) -> str:
    city_id = update_info.get("id")

    if city_id is not None:

        id_ = update_info.pop("id", None)

        try:
            obj, created = City.objects.update_or_create(
                city_id=city_id,
                defaults=update_info,
            )
            logger.debug(f"update_or_create_destination: City {obj}: created {created}")
            return id_
        except Exception as e:
            logger.debug(f"update_or_create_destination: Error {e}")
            logger.exception(e)


def delete_old_records(valid_id_list):
    all_cities_in_db = City.objects.all().values_list("city_id", flat=True)
    for id_ in all_cities_in_db:
        if id_ not in valid_id_list:
            logger.debug(f"delete_old_records: Deleting {id_}")
            City.objects.get(city_id=id_).delete()


def get_cities(country: str) -> dict:
    client = ExlineApi(
        exline_server=exline_server,
        origin_id=origin_id,
        pricing_policy=pricing_policy,
    )
    destinations = client.destinations(country=country)
    all_ids = []
    for dest in destinations.get("regions"):
        id_ = update_or_create_destination(dest)
        if id_ is not None:
            all_ids.append(id_)

    delete_old_records(all_ids)
