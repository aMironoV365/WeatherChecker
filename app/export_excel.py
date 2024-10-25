import os
import openpyxl
from sqlalchemy import select
from models import WeatherData, async_session
from config import Config
import aiofiles


async def export_to_excel():
    """
    Асинхронно экспортируем данные из базы данных в Excel файл.

    Эта функция выполняет следующие шаги:
    1. Подключается к базе данных и извлекает последние 10 записей
       о погоде из таблицы WeatherData, упорядоченных по времени.
    2. Создаёт новый Excel файл и добавляет заголовки столбцов.
    3. Записывает данные о погоде в файл.
    4. Сохраняет файл в указанной директории экспорта.
    """
    async with async_session() as session:
        stmt = select(WeatherData).order_by(WeatherData.timestamp.desc()).limit(10)
        result = await session.execute(stmt)
        weather_data = result.scalars().all()

        workbook = openpyxl.Workbook()
        sheet = workbook.active
        sheet.title = "Weather Data"

        sheet.append(["Timestamp", "Temperature (°C)", "Wind Direction", "Wind Speed (m/s)",
                      "Surface Pressure (hPa)", "Precipitation (mm)", "Relative Humidity (%)"])

        for data in weather_data:
            sheet.append([
                data.timestamp,
                data.temperature,
                data.wind_direction,
                data.wind_speed,
                data.surface_pressure,
                data.precipitation,
                data.relative_humidity
            ])

        export_dir = Config.EXPORT_DIR
        os.makedirs(export_dir, exist_ok=True)

        export_file = os.path.join(export_dir, "weather_data.xlsx")

        async with aiofiles.open(export_file, 'wb') as f:
            temp_file = f"{export_file}.tmp"
            workbook.save(temp_file)

            async with aiofiles.open(temp_file, 'rb') as temp_f:
                content = await temp_f.read()
                await f.write(content)

            os.remove(temp_file)

        print(f"Экспортировано в файл: {export_file}")
