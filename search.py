# search.py

from db_utils import connect_db_sakila
from log_utils import log_search
from mysql.connector import Error
from prettytable import PrettyTable

def get_movies():
    """Функция поиска фильмов по параметрам"""
    category = input("Введите название категории (например, 'Comedy','Drama') или Enter для пропуска: ").strip() or None
    year = input("Введите год выпуска фильма или Enter для пропуска: ").strip() or None
    min_length = input("Введите минимальную продолжительность фильма (в минутах) или Enter для пропуска: ").strip()
    max_length = input("Введите максимальную продолжительность фильма (в минутах) или Enter для пропуска: ").strip()
    rating = input("Введите рейтинг (например, 'PG', 'R', 'G') или Enter для пропуска: ").strip() or None
    title = input("Введите название фильма или Enter для пропуска: ").strip() or None

    min_length = int(min_length) if min_length else None
    max_length = int(max_length) if max_length else None

    query = """
        SELECT film.title, film.release_year, film.length, film.rating
        FROM film
        JOIN film_category ON film.film_id = film_category.film_id
        JOIN category ON film_category.category_id = category.category_id
        WHERE 1 = 1
    """
    params = []

    if category:
        query += " AND LOWER(category.name) = LOWER(%s)"
        params.append(category)
    if year:
        query += " AND film.release_year = %s"
        params.append(year)
    if min_length:
        query += " AND film.length >= %s"
        params.append(min_length)
    if max_length:
        query += " AND film.length <= %s"
        params.append(max_length)
    if rating:
        query += " AND film.rating = %s"
        params.append(rating)
    if title:
        query += " AND LOWER(film.title) LIKE LOWER(%s)"
        params.append(f"%{title}%")

    query += " ORDER BY film.title"

    connection = connect_db_sakila()
    if not connection:
        return

    cursor = connection.cursor()
    try:
        cursor.execute(query, tuple(params))
        results = cursor.fetchall()

        if not results:
            print("⚠️ Фильмы по заданным параметрам не найдены.")
        else:
            table = PrettyTable(["Название", "Год", "Длительность", "Рейтинг"])
            for row in results:
                table.add_row(row)
            print(table)
            log_search(category, year, title)

    except Error as e:
        print(f"❌ Ошибка выполнения запроса: {e}")
    finally:
        cursor.close()
        connection.close()
