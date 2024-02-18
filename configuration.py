class Configuration:
    """Конфигурационный файл"""
    def __init__(self, config):
        self.api_key = config.get("API_KEY")
        self.host_id = config.get("HOST_ID")
        self.user_name = config.get("USER_NAME")
        self.password = config.get("PASSWORD")
        self.db_name = config.get("DB_NAME")
        self.value_to_db = config.get("VALUE_TO_DB", [])
