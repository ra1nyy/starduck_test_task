### 1. Установка зависимостей

```bash
python3 -m pip install pipenv
pipenv install
```

### 2. Запуск приложения

> Выполняется из корневой директории проекта

```bash
uvicorn server:app --port 3000 --reload
```

### 3. Основные файлы
- [db_wrapper.py](db_wrapper.py) - слой репозитория для доступа к сущности RecordEntity + ORM обертка для PostgreSQL
- [service.py](service.py) - слой сервиса с логикой отсечки спортсменов
- [server.py](server.py) - FastAPI сервер с 2умя эндпоинтами
- [config.py](config.py) - конфигурация приложения (строка подключения к БД)
- [client.py](client.py) - aiohttp клиент для прогонки функционала
- [seed.py](seed.py) - сидинг данными
- [migrations](migrations) - Alembic миграции
