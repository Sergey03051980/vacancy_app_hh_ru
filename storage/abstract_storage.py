from abc import ABC, abstractmethod
from typing import List, Dict


class AbstractStorage(ABC):
    @abstractmethod
    def add_vacancy(self, vacancy: Dict) -> None:
        pass

    @abstractmethod
    def get_vacancies(self, criteria: Dict) -> List[Dict]:
        pass

    @abstractmethod
    def delete_vacancy(self, vacancy: Dict) -> None:
        pass
