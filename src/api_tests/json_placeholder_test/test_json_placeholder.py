import pytest
from jsonschema.validators import validate

from src.helpers.json_placeholder_helper import get_all_posts, get_post_by_id, create_post, update_post, delete_post
from src.schemas.json_placeholder_schema import json_placeholder_all_posts, json_placeholder_post_by_id, \
    json_placeholder_create_post, json_placeholder_update_post


class TestJsonPlaceholder:
    def test_list_all_posts(self):
        response = get_all_posts()
        assert response.status_code == 200

        list_of_posts = response.json()
        validate(list_of_posts, json_placeholder_all_posts)

    @pytest.mark.parametrize('post_id', [1, 25, 100])
    def test_post_by_id(self, post_id):
        response = get_post_by_id(post_id)
        assert response.status_code == 200

        list_of_posts = response.json()
        validate(list_of_posts, json_placeholder_post_by_id)

    def test_create_post(self):
        body = {
            'title': 'foo',
            'body': 'bar',
            'userId': 1,
        }
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
        }
        response = create_post(body, headers)
        assert response.status_code == 201

        created_post = response.json()
        validate(created_post, json_placeholder_create_post)

    @pytest.mark.usefixtures("url_check")
    @pytest.mark.parametrize("param_name, param_value", [
        ('title', 'foo'),
        ('body', 'bar'),
        ('userId', 100)
    ])
    def test_update_post(self, param_name, param_value):
        body = {
            param_name: param_value
        }
        headers = {
            'Content-type': 'application/json; charset=UTF-8',
        }
        response = update_post(5, body, headers)
        assert response.status_code == 200

        updated_post = response.json()
        validate(updated_post, json_placeholder_update_post)

    def test_delete_post(self):
        response = delete_post(1)
        assert response.status_code == 200

