class Config:
    """
    Класс конфигурации для приложения.

    Этот класс содержит все настройки, необходимые для
    корректной работы приложения, включая параметры для
    подключения к базе данных и конфигурацию Celery.

    Атрибуты:
        SQLALCHEMY_DATABASE_URI (str): URI для подключения к базе данных
            с использованием ai SQLite.
        CELERY_BROKER_URL (str): URL для подключения к брокеру сообщений Redis.
        CELERY_RESULT_BACKEND (str): URL для хранения результатов задач Celery в Redis.
        EXPORT_DIR (str): Путь к директории для экспорта данных.
    """
    SQLALCHEMY_DATABASE_URI = 'sqlite+aiosqlite:///weather.db'
    CELERY_BROKER_URL = 'redis://localhost:6379/0'
    CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
    EXPORT_DIR = './exports'
