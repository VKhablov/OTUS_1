dog_api_list_all_breeds = {
    "type": "object",
    "properties": {
        "message": {"type": "object"},
        "status": {"type": "string"}
    }
}

dog_api_random_breed = {
    "type": "object",
    "properties": {
        "message": {"type": "string"},
        "status": {"type": "string"}
    }
}

dog_api_dog_by_breed = {
    "type": "object",
    "properties": {
        "message": {"type": "array"},
        "status": {"type": "string"}
    }
}

dog_api_dog_by_breed_with_limit = {
    "type": "object",
    "properties": {
        "message": {"type": "array"},
        "status": {"type": "string"}
    }
}

dog_api_all_sub_breeds = {
    "type": "object",
    "properties": {
        "message": {"type": "array"},
        "status": {"type": "string"}
    }
}
