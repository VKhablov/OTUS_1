import requests

from src.config import ob_db_path


def get_breweries_with_limit(per_page):
    response = requests.get(ob_db_path, params={"per_page": per_page})
    return response


def get_brewery_by_id(id):
    response = requests.get(ob_db_path + id)
    return response


def get_random_brewery(path="random"):
    response = requests.get(ob_db_path + path)
    return response


def get_brewery_with_autocomplete_search(query, path="autocomplete"):
    response = requests.get(ob_db_path + path, params={"query": query})
    return response


def get_metadata(path="meta"):
    response = requests.get(ob_db_path + path)
    return response
