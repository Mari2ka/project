# log_utils.py

from db_utils import connect_db_logs
from mysql.connector import Error

def log_search(genre, year, keyword):
    """Логирование поисковых запросов"""
    if genre or year or keyword:
        connection = connect_db_logs()
        if not connection:
            return

        cursor = connection.cursor()
        try:
            insert_query = """
            INSERT INTO Marika_logs (genre, year, keyword, search_time)
            VALUES (%s, %s, %s, NOW())
            """
            cursor.execute(insert_query, (genre, year, keyword))
            connection.commit()
            print("✅ Поисковый запрос успешно сохранён!")
        except Error as e:
            print(f"❌ Ошибка при сохранении запроса: {e}")
        finally:
            cursor.close()
            connection.close()
