import requests
from src.config import dog_api_path


def get_all_breeds(path="breeds/list/all"):
    response = requests.get(dog_api_path + path)
    return response


def get_random_breed(path="breeds/image/random"):
    response = requests.get(dog_api_path + path)
    return response


def get_dog_by_breed(breed, path="breed/{breed}/images"):
    response = requests.get(dog_api_path + path.format(breed=breed))
    return response


def get_dog_by_breed_with_limit(breed, limit, path="breed/{breed}/images/random/{limit}"):
    response = requests.get(dog_api_path + path.format(breed=breed, limit=limit))
    return response


def get_all_sub_breeds(breed, path="breed/{breed}/list"):
    response = requests.get(dog_api_path + path.format(breed=breed))
    return response
