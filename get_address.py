import mysql.connector
import requests

from init import get_config


config = get_config("config.json")

db_connection = mysql.connector.connect(
    host=config.host_id,
    user=config.user_name,
    password=config.password,
    database=config.db_name
)

# We read the coordinates and get the result of the request URL
with db_connection.cursor() as cursor:
    cursor.execute("""SELECT ST_X(Point), ST_Y(Point)
                        FROM address
                       WHERE country IS NULL;
                    """)
    for latitude, longitude in cursor.fetchall():
        url = (f'https://www.mapquestapi.com/geocoding/v1/reverse?key'
               f'={config.api_key}&location={latitude}%2C{longitude}&outFormat'
               f'=json&thumbMaps=false')
        response = requests.get(url)

        # Checking the success of the request
        if response.status_code == 200:
            data = response.json()
            # Extracting the address from the API response
            try:
                country = data['results'][0]['locations'][0]['adminArea1']
                city = data['results'][0]['locations'][0]['adminArea5']
            except IndexError:
                print('Incorrect coordinate format...')

            # We record the results in the database
            data_recording = (f"UPDATE address SET country = '{country}',"
                              f" city = '{city}' "
                              f"WHERE ST_X(Point) = {latitude}")
            cursor.execute(data_recording)
            db_connection.commit()
        else:
            print(f'Ошибка при выполнении запроса: {response.status_code}')
