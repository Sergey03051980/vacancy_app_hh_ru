from typing import List
from models.vacancy import Vacancy


def filter_vacancies(vacancies: List[Vacancy], filter_words: List[str]) -> List[Vacancy]:
    """Фильтрация вакансий по ключевым словам"""
    if not filter_words:
        return vacancies

    filtered = []
    for vacancy in vacancies:
        description = vacancy.description.lower()
        if any(word.lower() in description for word in filter_words):
            filtered.append(vacancy)
    return filtered


def sort_vacancies(vacancies: List[Vacancy]) -> List[Vacancy]:
    """Сортировка вакансий по зарплате (от высокой к низкой)"""
    return sorted(vacancies, key=lambda x: x.salary_from or 0, reverse=True)
