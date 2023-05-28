import pytest

from src.helpers.dog_api_helper import get_all_breeds, get_random_breed, get_dog_by_breed, get_dog_by_breed_with_limit
from jsonschema import validate

from src.schemas.dog_api_schemas import dog_api_list_all_breeds, dog_api_random_breed, dog_api_dog_by_breed, \
    dog_api_dog_by_breed_with_limit, dog_api_all_sub_breeds


class TestDogApi:
    def test_list_all_breeds(self):
        response = get_all_breeds().json()
        assert response.status_code == 200

        list_of_breeds = response.json()
        validate(list_of_breeds, dog_api_list_all_breeds)

        assert list_of_breeds.get('status') == 'success'

    def test_random_breed(self):
        response = get_random_breed().json()
        assert response.status_code == 200

        list_of_breeds = response.json()
        validate(list_of_breeds, dog_api_random_breed)

        assert list_of_breeds.get('status') == 'success'

    @pytest.mark.parametrize("breed", ["hound", "akita"])
    def test_get_dog_breed(self, breed):
        response = get_dog_by_breed(breed).json()
        assert response.status_code == 200

        list_of_breeds = response.json()
        validate(list_of_breeds, dog_api_dog_by_breed)

        assert list_of_breeds.get('status') == 'success'

    @pytest.mark.parametrize("breed", ["hound", "akita"])
    @pytest.mark.parametrize("limit", [5, 7, 1])
    def test_get_dog_breed_with_limit(self, breed, limit):
        response = get_dog_by_breed_with_limit(breed, limit)
        assert response.status_code == 200

        list_of_breeds = response.json()
        validate(list_of_breeds, dog_api_dog_by_breed_with_limit)

        assert list_of_breeds.get('status') == 'success'
        assert len(list_of_breeds.get('message')) == limit

    @pytest.mark.parametrize("breed", ["hound", "akita"])
    def test_get_all_sub_breeds(self, breed):
        response = get_dog_by_breed(breed).json()
        assert response.status_code == 200

        list_of_breeds = response.json()
        validate(list_of_breeds, dog_api_all_sub_breeds)

        assert list_of_breeds.get('status') == 'success'
