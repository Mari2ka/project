

import mysql.connector
from mysql.connector import Error
from db_config import SAKILA_DB_CONFIG, LOG_DB_CONFIG

def connect_db_sakila():
    """Подключение к базе данных Sakila"""
    try:
        connection = mysql.connector.connect(**SAKILA_DB_CONFIG)
        return connection
    except Error as e:
        print(f"❌ Ошибка подключения к базе Sakila: {e}")
        return None

def connect_db_logs():
    """Подключение к базе логов"""
    try:
        connection = mysql.connector.connect(**LOG_DB_CONFIG)
        return connection
    except Error as e:
        print(f"❌ Ошибка подключения к базе логов: {e}")
        return None
