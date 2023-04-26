import json
import csv

from src.User import User
from src.data.Book import Book

if __name__ == "__main__":
    f_users = open('C:\\Users\\tumak\\PycharmProjects\\vadim_test\\src\\data\\users.json')
    users_data = json.load(f_users)
    f_users.close()
    users = []
    for user in users_data:
        users.append(User(**user))

    f_books = open("C:\\Users\\tumak\\PycharmProjects\\vadim_test\\src\\data\\books.csv")
    books_data = list(csv.reader(f_books, delimiter=',', quotechar='"'))
    f_books.close()
    books = []
    for book in books_data[1:]:
        books.append(Book(*book))

    for i in range(len(books)):
        users[i % len(users)].books.append(books[i])

    json_list = []
    for user in users:
        json_list.append(user.to_json())
    json_string = json.dumps(json_list)

    outfile = open('result.json', 'w')
    outfile.write(json_string)
    outfile.close()
