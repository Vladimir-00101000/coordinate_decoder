# Coordinate Decoder
This is my first mini-project to decode geographical coordinates into addresses using a third-party API.

The project uses a MYSQL database into which using a script "clear_and_insert.py " geographical coordinates are
recorded from the file "config.json". Next, the script "get_address.py " it takes these coordinates from the database,
uses a third-party API to get the address at these coordinates and writes it to the appropriate field in the database.