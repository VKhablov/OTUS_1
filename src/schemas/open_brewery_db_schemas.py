ob_db_breweries_with_limit = {
    "type": "array",
    "items": {
        "type": "object"
    }
}

ob_db_brewery_by_id = {
    "type": "object"
}

ob_db_random_breweries = {
    "type": "array",
    "items": {
        "type": "object"
    }
}

ob_db_search_breweries_with_autocomplete = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "id": {"type": "string"},
            "name": {"type": "string"}
        }
    }
}

ob_db_metadata = {
    "type": "object",
    "properties": {
        "total": {"type": "string"},
        "page": {"type": "string"},
        "per_page": {"type": "string"}
    }
}
