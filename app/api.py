import aiohttp


async def weather_request() -> dict:
    """
    Асинхронно запрашиваем данные о погоде из API.

    Эта функция выполняет HTTP-запрос к API Open-Meteo для получения
    текущих данных о погоде на основе заданных параметров.

    Возвращает:
        dict: Словарь с данными о погоде, полученными из API, включая
              такие параметры, как температура, влажность, скорость ветра
              и атмосферное давление.

    Исключения:
        - Raises `aiohttp.ClientError`: Если запрос не удался или
          если ответ от сервера не является успешным (статус код
          2xx). Исключение будет вызвано методом `raise_for_status()`.

    Примечания:
        - Параметры `latitude` и `longitude` определяют местоположение,
          для которого запрашиваются данные о погоде.
        - Временная зона установлена на "Europe/Moscow".
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": 55.68,
        "longitude": 37.35,
        "timezone": "Europe/Moscow",
        "current": ["relative_humidity_2m", "temperature_2m", "precipitation",
                    "surface_pressure", "wind_speed_10m", "wind_direction_10m"]
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params) as response:
            response.raise_for_status()
            return await response.json()
