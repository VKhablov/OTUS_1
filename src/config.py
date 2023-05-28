from dotenv import dotenv_values

config = dotenv_values(".env")

dog_api_path = config.get("DOG_API_PATH")
ob_db_path = config.get("OPEN_BREWERY_DB_PATH")
json_placeholder_path = config.get("JSON_PLACEHOLDER_PATH")

