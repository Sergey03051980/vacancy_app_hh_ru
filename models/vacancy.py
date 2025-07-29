from dataclasses import dataclass
from typing import Optional, List, Dict


@dataclass
class Vacancy:
    __slots__ = ('title', 'url', 'salary_from', 'salary_to', 'description')

    title: str
    url: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    description: str

    def __post_init__(self):
        self._validate_data()

    def _validate_data(self):
        if not self.title:
            raise ValueError("Название вакансии обязательно")
        if not (self.url.startswith('http://') or self.url.startswith('https://')):
            raise ValueError("URL должен начинаться с http:// или https://")

    def __lt__(self, other):
        if self.salary_from is None:
            return True
        if other.salary_from is None:
            return False
        return self.salary_from < other.salary_from

    @classmethod
    def cast_to_object_list(cls, data: List[Dict]) -> List['Vacancy']:
        vacancies = []
        for item in data:
            salary = item.get('salary', {})
            vacancies.append(cls(
                title=item.get('name', ''),
                url=item.get('alternate_url', ''),
                salary_from=salary.get('from'),
                salary_to=salary.get('to'),
                description=item.get('snippet', {}).get('requirement', '')
            ))
        return vacancies
