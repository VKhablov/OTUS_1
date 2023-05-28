import pytest
from jsonschema.validators import validate

from src.helpers.open_brewery_db_helper import get_breweries_with_limit, get_brewery_by_id, get_random_brewery, \
    get_brewery_with_autocomplete_search, get_metadata
from src.schemas.open_brewery_db_schemas import ob_db_breweries_with_limit, ob_db_brewery_by_id, ob_db_random_breweries, \
    ob_db_search_breweries_with_autocomplete, ob_db_metadata


class TestOpenBreweryDB:

    @pytest.mark.parametrize("limit", [1, 5, 10])
    def test_get_breweries_with_limit(self, limit):
        response = get_breweries_with_limit(limit)
        assert response.status_code == 200

        list_of_breweries = response.json()
        validate(list_of_breweries, ob_db_breweries_with_limit)

        assert len(list_of_breweries) == limit

    def test_get_brewery_by_id(self):
        response = get_breweries_with_limit(1).json()[0]
        brewery_id = response.get("id")
        brewery_name = response.get("name")

        response = get_brewery_by_id(brewery_id)
        assert response.status_code == 200

        brewery = response.json()
        validate(brewery, ob_db_brewery_by_id)

        assert brewery.get('name') == brewery_name

    def test_get_random_brewery(self):
        response = get_random_brewery()
        assert response.status_code == 200

        breweries = response.json()
        validate(breweries, ob_db_random_breweries)

        assert len(breweries) == 1

    @pytest.mark.parametrize("query", ["dog", "brew"])
    def test_get_brewery_with_autocomplete_search(self, query):
        response = get_brewery_with_autocomplete_search(query)
        assert response.status_code == 200

        breweries = response.json()
        validate(breweries, ob_db_search_breweries_with_autocomplete)

    def test_get_metadata(self):
        response = get_metadata()
        assert response.status_code == 200

        metadata = response.json()
        validate(metadata, ob_db_metadata)
