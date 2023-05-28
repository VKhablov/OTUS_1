import requests

from src.config import json_placeholder_path


def get_post_by_id(id, path="posts/"):
    response = requests.get(json_placeholder_path + path + str(id))
    return response


def get_all_posts(path="posts/"):
    response = requests.get(json_placeholder_path + path)
    return response


def create_post(body, header=None, path="posts/"):
    response = requests.post(json_placeholder_path + path, headers=header, json=body)
    return response


def update_post(id, body, header=None, path="posts/"):
    response = requests.patch(json_placeholder_path + path + str(id), headers=header, json=body)
    return response


def delete_post(id, path="posts/"):
    response = requests.delete(json_placeholder_path + path + str(id))
    return response
