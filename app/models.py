from sqlalchemy.orm import Mapped, mapped_column, declarative_base, sessionmaker
from datetime import datetime
from sqlalchemy import DateTime
from .config import Config
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine

Base = declarative_base()

engine = create_async_engine(Config.SQLALCHEMY_DATABASE_URI)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_tables():
    """
    Создаёт таблицы в базе данных на основе определённых моделей.

    Эта функция устанавливает асинхронное соединение с базой данных
    и выполняет команду создания всех таблиц, описанных в моделях,
    унаследованных от `Base`.
    """
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


class WeatherData(Base):
    """
    Модель данных о погоде.

    Эта модель представляет таблицу `weather_data`, которая хранит
    информацию о текущих метеорологических условиях.

    Атрибуты:
        id (int): Уникальный идентификатор записи.
        temperature (float): Температура в градусах Цельсия.
        wind_direction (float): Направление ветра в градусах.
        wind_speed (float): Скорость ветра в метрах в секунду.
        surface_pressure (float): Атмосферное давление на уровне поверхности в гПа.
        precipitation (float): Количество осадков в миллиметрах.
        relative_humidity (float): Относительная влажность в процентах.
        timestamp (datetime): Дата и время записи в формате UTC.
    """
    __tablename__ = 'weather_data'

    id: Mapped[int] = mapped_column(primary_key=True)
    temperature: Mapped[float] = mapped_column()
    wind_direction: Mapped[float] = mapped_column()
    wind_speed: Mapped[float] = mapped_column()
    surface_pressure: Mapped[float] = mapped_column()
    precipitation: Mapped[float] = mapped_column()
    relative_humidity: Mapped[float] = mapped_column()
    timestamp: Mapped[datetime] = mapped_column(DateTime)
