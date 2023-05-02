import json

from src.data.Book import Book


class Friend:
    id: int
    name: str


class User:
    _id: str
    index: int
    guid: str
    isActive: bool
    balance: str
    picture: str
    age: int
    eyeColor: str
    name: str
    gender: str
    company: str
    email: str
    phone: str
    address: str
    about: str
    registered: str
    latitude: float
    longitude: float
    tag: list[str]
    friends: list[Friend]
    greeting: str
    favoriteFruit: str
    books: list[Book]

    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            self.__setattr__(k, v)
        self.books = []

    def to_json(self):
        books = []
        for book in self.books:
            books.append(book.to_json())
        json = {
            "name": self.name,
            "gender": self.gender,
            "address": self.address,
            "age": self.age,
            "books": books
        }
        return json
