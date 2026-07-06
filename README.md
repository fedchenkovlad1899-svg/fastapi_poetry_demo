# Poetry Demo FastApi

Этот документ позволяtт новому разработчику самостоятельно развернуть проект и начать работу без дополнительной консультации.

---

## Используемые технологии

*    Python 3.13+
*    FastAPI >0.138.1 
*    Uvicorn >0.49.0
*    SQLAlchemy >2.0.51
*    Alembic >1.118.5
*    Poetry >2.x
*    Ruff >0.15.20

---

##  Архитектура проекта

Проект использует классическую структуру для FastAPI-приложений с изоляцией исходного кода в директории `src/`:

```poetry-demo/
├── .venv/                           # Локальное виртуальное окружение Python
├── alembic/                         # Миграции базы данных
│   ├── versions/                    # История миграций
│   └── env.py                       # Окружение Alembic
├── src/                             # Исходный код приложения
│   ├── account/                     # Модуль пользователей
│   │   ├── models/
│   │   ├── repositories/
│   │   ├── router/
│   │   └── schemas/
│   │   └── services/
│   ├── authentication/              # Модуль авторизации
│   │   ├── routers/
│   │   ├── schemas/
│   │   └── services/
│   ├── chat/                        # Websockets
│   ├── core/                        # Конфигурация ядра приложения
│   ├── async_test.py                # Асинхронные тесты 
│   └── main.py                      # Точка входа FastAPI
├── tests/                           # Тесты
├── .env                             # Конфиденциальные настройки
├── .env.example                     # Шаблон настроек 
├── .gitignore                       # Исключения для Git
├── .pre-commit-config.yaml          # pre-commit
├── alembic.ini                      # Конфигурация Alembic
├── poetry.lock                      # Лок-файл зависимостей Poetry
├── pyproject.toml                   # Конфигурация проекта, Poetry и Ruff
└── README.md                        # Документация проекта

```

---

## Настройка окружения

### 1. Переменные среды
В корне проекта необходимо создать файл **`.env`** (добавить в .gitignore). Заполните его конфигурационными данными  (.env.exampple):

### 2. Установка Poetry

```
pip install poetry
```
---

## 3. Работа с Poetry (Развертывание проекта)

1. **Создайте и активируйте чистое окружение:**
   ```
   poetry env use python
   ```

2. **Установите все зависимости из `pyproject.toml`:**
   ```
   poetry install 
   ```
---

## Работа с Alembic (Миграции)

Изменения в моделях базы данных должны фиксироваться через миграции.

*   **Создание новой автоматической миграции**:
   ```
   poetry run alembic revision --autogenerate -m "описание_изменений"
   ```
*   **Применение всех актуальных миграций к базе данных:**
   ```
   poetry run alembic upgrade head
   ```
*   **Откат последней примененной миграции на один шаг назад:**
   ```
   poetry run alembic downgrade -1
   ```

---

##  Основные команды 
### Запуск сервера 
Запуск сервера:
```
poetry run uvicorn src.main:app --reload
```
документация API будет доступна по адресам:
*   FastApi Swagger UI: `http://127.0.0.1:8000/docs`
*   Chat: `http://127.0.0.1:8001/api/chat/`

### Проверка качества кода (Ruff)
 `[tool.ruff]` в `pyproject.toml` .

*   **поиск ошибок и неиспользуемых импортов:**
   ```
   poetry run ruff check
   ```
*   **Автоматическое исправление безопасных ошибок линтера:**
   ```
   poetry run ruff check --fix
   ```

