from api.hh_api import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_storage import JSONStorage
# from utils.filters import filter_vacancies, sort_vacancies


def user_interaction():
    hh_api = HeadHunterAPI()
    storage = JSONStorage()

    search_query = input("Введите поисковый запрос: ")
    vacancies = hh_api.get_vacancies(search_query)
    vacancy_objects = Vacancy.cast_to_object_list(vacancies)

    for vacancy in vacancy_objects:
        storage.add_vacancy({
            'title': vacancy.title,
            'url': vacancy.url,
            'salary_from': vacancy.salary_from,
            'salary_to': vacancy.salary_to,
            'description': vacancy.description
        })


if __name__ == "__main__":
    user_interaction()
