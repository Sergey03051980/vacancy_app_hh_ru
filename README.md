#курсовая_работа
# 🚀 Vacancy Parser - Парсер вакансий с HH.ru

![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)
![Poetry](https://img.shields.io/badge/Poetry-1.2+-yellow?logo=poetry)
![Coverage](https://img.shields.io/badge/Coverage-85%25-green)

Проект для сбора и анализа вакансий с платформы HeadHunter (HH.ru) с возможностью:
- Поиска по ключевым словам
- Фильтрации и сортировки
- Сохранения в JSON
- Анализа зарплатных предложений

## 📦 Структура проекта
vacancy_app/
├── src/ # Исходный код
│ ├── api/ # Модуль работы с API
│ ├── models/ # Модели данных
│ ├── storage/ # Хранение данных
│ ├── utils/ # Вспомогательные утилиты
│ └── main.py # Точка входа
├── tests/ # Тесты
├── pyproject.toml # Конфигурация Poetry
└── requirements.txt # Зависимости

text

## 🛠 Установка

1. Клонируйте репозиторий:
```bash
git clone https://github.com/yourname/vacancy-parser.git
cd vacancy-parser
Установите зависимости:

bash
poetry install
# Или
pip install -r requirements.txt
🚀 Использование
bash
poetry run python src/main.py
# Или
python src/main.py
Пример работы:

text
Введите поисковый запрос: Python Developer
Введите количество вакансий для вывода: 10
Введите ключевые слова для фильтрации: Django Flask

Топ 10 вакансий по зарплате:
1. Senior Python Developer (200000-250000 руб.)
2. Python Backend Developer (180000-220000 руб.)
...
🔧 Технологии
Python 3.8+ - Базовый язык

Requests - Работа с API

Pydantic/Dataclasses - Валидация данных

Poetry - Управление зависимостями

Pytest - Тестирование

📊 Возможности
✔️ Парсинг вакансий с HH.ru
✔️ Фильтрация по ключевым словам
✔️ Сортировка по зарплате
✔️ Сохранение в JSON
✔️ Консольный интерфейс

🧪 Тестирование
bash
pytest tests/ -v
# С покрытием:
pytest --cov=src --cov-report=html tests/
Отчет о покрытии: htmlcov/index.html

📝 Лицензия
MIT License. См. файл LICENSE.

<div align="center"> <sub>Разработано с ❤️ для курсового проекта</sub> </div> ```
Ключевые особенности:
Профессиональное оформление с иконками и badges

Полная структура проекта с описанием

Четкие инструкции по установке и запуску

Пример работы программы

Список технологий и возможностей

Инструкции по тестированию

