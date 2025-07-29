import pytest
import os
import json
from storage.json_storage import JSONStorage
# from models.vacancy import Vacancy


@pytest.fixture
def temp_storage(tmp_path):
    test_file = tmp_path / 'test_vacancies.json'
    storage = JSONStorage(file_path=str(test_file))
    yield storage
    if os.path.exists(test_file):
        os.remove(test_file)


def test_add_vacancy(temp_storage):
    test_vacancy = {'title': 'Test', 'url': 'http://test.com'}
    temp_storage.add_vacancy(test_vacancy)

    with open(temp_storage._file_path, 'r') as f:
        data = json.load(f)

    assert len(data) == 1
    assert data[0]['title'] == 'Test'


def test_no_duplicates(temp_storage):
    vacancy = {'title': 'Duplicate', 'url': 'http://test.com'}
    temp_storage.add_vacancy(vacancy)
    temp_storage.add_vacancy(vacancy)

    with open(temp_storage._file_path, 'r') as f:
        data = json.load(f)

    assert len(data) == 1


def test_delete_vacancy(temp_storage):
    vacancy = {'title': 'To Delete', 'url': 'http://delete.com'}
    temp_storage.add_vacancy(vacancy)
    temp_storage.delete_vacancy(vacancy)

    with open(temp_storage._file_path, 'r') as f:
        data = json.load(f)

    assert len(data) == 0


def test_get_vacancies(temp_storage):
    vacancies = [
        {'title': 'Python', 'url': 'http://python.com', 'salary': 100000},
        {'title': 'Java', 'url': 'http://java.com', 'salary': 90000}
    ]
    for v in vacancies:
        temp_storage.add_vacancy(v)

    result = temp_storage.get_vacancies({'title': 'Python'})
    assert len(result) == 1
    assert result[0]['title'] == 'Python'
    assert result[0]['url'] == 'http://python.com'
