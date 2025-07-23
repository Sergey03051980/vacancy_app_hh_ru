from api.hh_api import HeadHunterAPI
from models.vacancy import Vacancy
from storage.json_storage import JSONStorage
from utils.filters import filter_vacancies, sort_vacancies


def user_interaction():
    hh_api = HeadHunterAPI()
    storage = JSONStorage()

    search_query = input("Введите поисковый запрос: ")
    vacancies = hh_api.get_vacancies(search_query)
    vacancy_objects = Vacancy.cast_to_object_list(vacancies)

    for vacancy in vacancy_objects:
        storage.add_vacancy(vacancy.to_dict())
        
    top_n = int(input("Введите количество вакансий для вывода: "))
    filter_words = input("Введите ключевые слова для фильтрации: ").split()

    filtered = filter_vacancies(vacancy_objects, filter_words)
    sorted_vacancies = sort_vacancies(filtered)

    print(f"\nТоп {top_n} вакансий:")
    for i, vacancy in enumerate(sorted_vacancies[:top_n], 1):
        print(f"{i}. {vacancy.title} ({vacancy.salary_from}-{vacancy.salary_to})")


if __name__ == "__main__":
    user_interaction()