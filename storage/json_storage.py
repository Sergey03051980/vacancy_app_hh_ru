import json
import os
from typing import List, Dict
from .abstract_storage import AbstractStorage


class JSONStorage(AbstractStorage):
    __slots__ = ('_file_path',)

    def __init__(self, file_path: str = 'vacancies.json'):
        self._file_path = file_path
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                json.dump([], f)

    def _read_file(self) -> List[Dict]:
        with open(self._file_path, 'r') as f:
            return json.load(f)

    def _write_file(self, data: List[Dict]) -> None:
        with open(self._file_path, 'w') as f:
            json.dump(data, f, indent=2)

    def add_vacancy(self, vacancy: Dict) -> None:
        data = self._read_file()
        if vacancy not in data:
            data.append(vacancy)
            self._write_file(data)

    def get_vacancies(self, criteria: Dict) -> List[Dict]:
        data = self._read_file()
        return [v for v in data if all(v.get(k) == criteria[k] for k in criteria)]


    def delete_vacancy(self, vacancy: Dict) -> None:
        data = self._read_file()
        data = [v for v in data if v != vacancy]
        self._write_file(data)
