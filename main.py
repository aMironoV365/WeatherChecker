import asyncio
from app.export_excel import export_to_excel

if __name__ == "__main__":
    """
    Точка входа для выполнения скрипта экспорта данных о погоде в Excel файл.

    Этот скрипт выполняет следующие шаги:
    1. Запускает асинхронную функцию `export_to_excel()`, 
       которая извлекает последние данные о погоде из базы данных 
       и экспортирует их в Excel файл.
    """
    asyncio.run(export_to_excel())
