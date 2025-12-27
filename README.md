# Diplom_2
## Автотесты API сервиса Stellar Burgers

Набор интеграционных API‑тестов на `pytest` для публичного демо‑сервиса [Stellar Burgers](https://stellarburgers.education-services.ru). Проверяются сценарии регистрации, авторизации, обновления профиля и работы с заказами через REST API.

### Стек
- Python, `pytest`
- `requests` для HTTP‑клиента
- `faker` для генерации тестовых данных
- `allure-pytest` для отчетов

### Быстрый старт
```bash
python -m venv .venv
source .venv/bin/activate    # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Запуск тестов
- Обычный прогон:  
  ```bash
  pytest -v
  ```
- С сохранением шагов для Allure:  
  ```bash
  pytest -v --alluredir=allure-results
  ```
  При установленном Allure CLI отчет можно открыть:  
  ```bash
  allure serve allure-results
  ```

### Структура проекта
- `api/` — thin-клиенты для эндпоинтов (пользователь, заказ, ингредиенты).
- `tests/` — сами проверки `pytest` с маркерами Allure.
- `conftest.py` — фикстуры: создание/очистка пользователя, список ингредиентов, подготовка заказа.
- `data.py` — тестовые данные и ожидаемые ответы API.
- `helper.py` — фабрики тел запросов и утилиты для модификации данных.
- `urls.py` — базовый URL и маршруты API (при необходимости можно поменять `BASE_URL`).

### Полезно знать
- Тесты создают временных пользователей и удаляют их в фикстуре `cleanup_user`.
- Для негативных сценариев используются ожидаемые ответы, зашитые в `data.py`.
- По умолчанию все запросы идут на `https://stellarburgers.education-services.ru`; чтобы переключиться на другой стенд, обновите `Urls.BASE_URL`.
