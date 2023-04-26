import json


class Book:
    title: str
    author: str
    genre: str
    pages: int
    publisher: str

    def __init__(self, title: str, author: str, genre: str, pages: int, publisher: str):
        self.title = title
        self.author = author
        self.genre = genre
        self.pages = pages
        self.publisher = publisher

    def to_json(self):
        json = {
            "title": self.title,
            "author": self.author,
            "pages": self.pages,
            "genre": self.genre
        }
        return json
