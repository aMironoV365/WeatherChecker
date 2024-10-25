from api import weather_request
from models import WeatherData, async_session
from datetime import datetime


async def fetch_weather_data_async():
    """
    Асинхронно запрашивает данные о погоде и сохраняет их в базу данных.

    Эта функция делает асинхронный запрос к API для получения
    актуальных данных о погоде и сохраняет их в базе данных.
    """
    weather_data = await weather_request()

    async with async_session() as session:
        current_weather = weather_data["current"]

        weather = WeatherData(
            temperature=current_weather["temperature_2m"],
            wind_direction=current_weather["wind_direction_10m"],
            wind_speed=current_weather["wind_speed_10m"],
            surface_pressure=current_weather["surface_pressure"],
            precipitation=current_weather["precipitation"],
            relative_humidity=current_weather["relative_humidity_2m"],
            timestamp=datetime.utcnow()
        )

        session.add(weather)
        await session.commit()
