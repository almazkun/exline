import requests
import logging

import urllib

logger = logging.getLogger(__name__)


class ExlineApi:
    def __init__(
        self,
        exline_server: str,
        origin_id: int,
        pricing_policy: str,
    ) -> None:
        self.server = exline_server
        self.origin_id = origin_id
        self.pricing_policy = pricing_policy

    def _make_call(self, endpoint: str, params: dict) -> dict:
        """API caller

        Args:
            endpoint (str): API endpoint
            params (dict): query parems

        Returns:
            dict: API response
        """

        url = f"{self.server}{endpoint}"

        logger.debug(f"ExlineApi._make_call: Making API call to: {url}")

        r = requests.get(url, params=params)

        if r.ok:
            return r.json()

        r.raise_for_status()

    @property
    def _params(self):
        return {
            "origin_id": self.origin_id,
            "pricing_policy": self.pricing_policy,
        }

    def calculate(self, destination_id: int, weight: float) -> dict:
        endpoint = "public/v1/calculate"
        params = self._params
        params.update(
            {
                "destination_id": destination_id,
                "weight": weight,
            }
        )

        return self._make_call(endpoint=endpoint, params=params)
