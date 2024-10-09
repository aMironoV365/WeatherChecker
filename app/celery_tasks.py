import asyncio
from celery import Celery
from .models import create_tables
from .config import Config
from .fetch_weather import fetch_weather_data_async

app = Celery('celery_tasks', broker=Config.CELERY_BROKER_URL, backend=Config.CELERY_RESULT_BACKEND)


@app.on_after_configure.connect
def setup_tasks(sender, **kwargs):
    """
    Создает таблицы в базе данных после настройки Celery.

    Эта функция вызывается после конфигурации Celery и использует
    asyncio для асинхронного выполнения функции создания таблиц.
    """
    asyncio.run(create_tables())


@app.task
def fetch_weather_data():
    """
    Запрашиваем данные о погоде и сохраняем их в базу.
    """
    asyncio.run(fetch_weather_data_async())


@app.on_after_configure.connect
def setup_periodic_tasks(sender, **kwargs):
    """
    Настраивает периодические задачи для Celery.

    Добавляет периодическую задачу, которая будет выполняться каждые 5 секунд,
    чтобы запрашивать данные о погоде и сохранять их в базу данных.
    """
    sender.add_periodic_task(5.0, fetch_weather_data.s(), name='fetch weather data every 5 seconds')
