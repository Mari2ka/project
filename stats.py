




from db_utils import connect_db_logs
from mysql.connector import Error
from prettytable import PrettyTable

def get_popular_searches():
    """Получение популярных поисковых запросов"""
    connection = connect_db_logs()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        query = """
        SELECT keyword, genre, year, COUNT(*) AS count 
        FROM Marika_logs 
        GROUP BY keyword, genre, year 
        ORDER BY count DESC 
        LIMIT 5
        """

        cursor.execute(query)
        results = cursor.fetchall()

        if not results:
            print("⚠️ Нет популярных запросов.")
        else:
            table = PrettyTable(["Ключевое слово", "Категория", "Год", "Количество запросов"])
            for row in results:
                table.add_row(row)

            print(table)

    except Error as e:
        print(f"❌ Ошибка выполнения запроса: {e}")
    finally:
        cursor.close()
        connection.close()
