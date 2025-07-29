import pytest
from models.vacancy import Vacancy


@pytest.fixture
def sample_vacancy_data():
    return {
        'title': 'Python Developer',
        'url': 'https://hh.ru/vacancy/123',
        'salary_from': 100000,
        'salary_to': 150000,
        'description': 'Требуется опыт работы с Python'
    }


def test_vacancy_creation(sample_vacancy_data):
    vacancy = Vacancy(**sample_vacancy_data)
    assert vacancy.title == 'Python Developer'
    assert vacancy.salary_from == 100000
    assert vacancy.url.startswith('https://')


def test_vacancy_comparison():
    v1 = Vacancy('Junior', 'http://url1.com', 50000, None, 'desc1')
    v2 = Vacancy('Senior', 'http://url2.com', 150000, None, 'desc2')
    assert v1 < v2
    assert not v2 < v1


def test_vacancy_validation():
    # Проверка корректного URL
    Vacancy('Valid', 'http://valid.com', 100000, None, 'desc')
    Vacancy('Valid', 'https://valid.com', 100000, None, 'desc')

    # Проверка некорректных случаев
    with pytest.raises(ValueError):
        Vacancy('', 'http://invalid.com', 100000, None, 'desc')
    with pytest.raises(ValueError):
        Vacancy('Invalid URL', 'invalid_url', 100000, None, 'desc')


def test_cast_to_object_list():
    api_data = [{
        'name': 'Dev',
        'alternate_url': 'https://hh.ru/vacancy/456',
        'salary': {'from': 120000, 'to': 180000},
        'snippet': {'requirement': 'Python 3+'}
    }]
    vacancies = Vacancy.cast_to_object_list(api_data)
    assert len(vacancies) == 1
    assert vacancies[0].title == 'Dev'


def test_to_dict(sample_vacancy_data):
    vacancy = Vacancy(**sample_vacancy_data)
    data = vacancy.to_dict()
    assert data['title'] == sample_vacancy_data['title']
    assert isinstance(data, dict)
