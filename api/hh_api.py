import requests
from typing import Dict, List
from .abstract_api import AbstractAPI


class HeadHunterAPI(AbstractAPI):
    __slots__ = ('_base_url',)

    def __init__(self):
        self._base_url = "https://api.hh.ru/vacancies"

    def _connect(self, params: Dict) -> Dict:
        response = requests.get(self._base_url, params=params)
        response.raise_for_status()
        return response.json()

    def get_vacancies(self, search_query: str) -> List[Dict]:
        params = {
            'text': search_query,
            'per_page': 100,
            'area': 113  # Россия
        }
        data = self._connect(params)
        return data.get('items', [])
