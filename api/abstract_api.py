from abc import ABC, abstractmethod
from typing import Dict, List


class AbstractAPI(ABC):
    @abstractmethod
    def get_vacancies(self, search_query: str) -> List[Dict]:
        """Получить вакансии по поисковому запросу"""
        pass
