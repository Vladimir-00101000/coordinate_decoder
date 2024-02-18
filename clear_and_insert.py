import mysql.connector

from init import get_config


config = get_config("config.json")

db_connection = mysql.connector.connect(
    host=config.host_id,
    user=config.user_name,
    password=config.password,
    database=config.db_name
)

# clearing the table
with db_connection.cursor() as cursor:
    cursor.execute("""DELETE FROM address""")
    db_connection.commit()

# Filling in the table
with db_connection.cursor() as cursor:
    for x, y in config.value_to_db:
        fill_table = f"INSERT INTO address (point) VALUES (POINT({x}, {y}))"
        cursor.execute(fill_table)
    db_connection.commit()
