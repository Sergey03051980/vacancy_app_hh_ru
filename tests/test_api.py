import pytest
from api.hh_api import HeadHunterAPI
from unittest.mock import patch, MagicMock


def test_hh_api_get_vacancies():
    api = HeadHunterAPI()
    vacancies = api.get_vacancies("Python")
    assert isinstance(vacancies, list)
    assert len(vacancies)


@patch('requests.get')
def test_get_vacancies(mock_get):
    mock_response = MagicMock()
    mock_response.json.return_value = {'items': [{'name': 'Python Dev'}]}
    mock_response.raise_for_status.return_value = None
    mock_get.return_value = mock_response

    api = HeadHunterAPI()
    result = api.get_vacancies('Python')

    assert len(result) == 1
    assert result[0]['name'] == 'Python Dev'
    mock_get.assert_called_once()


def test_connection_error():
    api = HeadHunterAPI()
    with patch('requests.get', side_effect=Exception("Connection error")):
        with pytest.raises(Exception):
            api.get_vacancies('Python')