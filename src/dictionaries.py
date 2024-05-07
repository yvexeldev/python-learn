person = {
    "name": "Azam",
    "age": 17,
    "country": "Uzbekistan"
}

# for key, value in person.items():
#     print(f"{key} - {value}")

book = {
    "title": "Python",
    "author": "Azam",
    "year": 2022
}

# for key, value in book.items():
#     print(f"{key} - {value}")

fruits_basket = {
    "apple": 5,
    "banana": 3,
    "cherry": 2
}

# for key, value in fruits_basket.items():
#     print(f"Name: {key} - {value}")

# print(book.get("author"))

# for fruit in fruits_basket.keys():
#     print(fruit)

person.update({"city": "Tashkent"})
# print(person)

fruits_basket.update({"apple": 4})
# print(fruits_basket)

book.pop("year")
# print(book)
