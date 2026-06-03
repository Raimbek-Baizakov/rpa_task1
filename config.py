"""
Единый конфигурационный файл
"""

# Конфигурация базы данных
DB_CONFIG = {
    "pg_host": "localhost",
    "pg_port": 5432,
    "pg_db": "bot_results",
    "pg_user": "postgres",
    "pg_password": "1106",  # реальный пароль
}

# Конфигурация бота
BOT_CONFIG = {
    "first_name": "Ivan",
    "last_name": "Ivanov",
    "password": "SecureP@ss123",
    "birth_day": 15,
    "birth_month": 6,
    "birth_year": 1995,
    "gender": "male",
    "headless": False,
    "chromedriver_path": "",
    "page_timeout": 30,
}

# Список телефонов для пакетного запуска
PHONES = [
    "+77871687300",
    "+77871687301",
    "+77871687302",
    "+77871687303",
    "+77871687304",
    "+77871687305",
    "+77871687306",
    "+77871687307",
    "+77871687308",
    "+77871687309",
]