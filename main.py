### 1. К уже реализованному классу «Автомобиль» добавьте возможность упаковки и распаковки данных
# с использованием json и pickle.

# import pickle
# import json
#
# class Auto:
#     def __init__(self, model, year, manufacturer, color, price):
#         self.model = model
#         self.year = year
#         self.manufacturer = manufacturer
#         self.color = color
#         self.price = price
#
#     def info(self):
#         print(f'автомобиль {self.model}')
#
#     def save_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def load_pickle(filename):
#         try:
#             with open(filename, 'rb') as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print('Указан неверный путь к файлу!')
#
#     def save_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def load_json(filename):
#         with open(filename, 'r') as f:
#             auto_dict = json.load(f)
#             return Auto(**auto_dict)
#
#     def __str__(self):
#         return f'Модель: {self.model}\n' \
#                f'Год: {self.year}\n' \
#                f'Производитель: {self.manufacturer}\n' \
#                f'Цвет: {self.color}\n' \
#                f'Цена: {self.price}'
#
#
# a = Auto('KIA', '2022', 'Корея', 'зеленый', '1 890 000')
# print(a)
# a.save_pickle('auto.txt')
# new_auto = Auto.load_pickle('auto.txt')
# print(new_auto)
# new_auto.info()
#
# b =Auto('Lada', '2023', 'Россия', 'белый', '1 090 000')
# b.save_json('auto.json')
# new_b = Auto.load_json('auto.json')
# print(new_b)
# new_b.info()


### 2. К уже реализованному классу «Книга» добавьте возможность упаковки и распаковки данных
# с использованием json и pickle.

# import pickle
# import json
#
# class Book:
#     def __init__(self, name, year, genre, author, price):
#         self.name = name
#         self.year = year
#         self.genre = genre
#         self.author = author
#         self.price = price
#
#     def info(self):
#         print(f'Книга {self.name} о ...')
#
#     def save_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def load_pickle(filename):
#         try:
#             with open(filename, 'rb') as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print('Указан неверный путь к файлу!')
#
#     def save_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def load_json(filename):
#         with open(filename, 'r') as f:
#             book_dict = json.load(f)
#             return Book(**book_dict)
#
#     def __str__(self):
#         return f'Название: {self.name}\n' \
#                f'Год: {self.year}\n' \
#                f'Жанр: {self.genre}\n' \
#                f'Автор: {self.author}\n' \
#                f'Цена: {self.price}'
#
#
# a = Book('Сказка о рыбаке и рыбке', '1833', 'сказка', 'А.С.Пушкин', '200 руб.')
# print(a)
# a.save_pickle('book.txt')
# new_a = Book.load_pickle('book.txt')
# print(new_a)
# new_a.info()
#
# b =Book('Турецкий гамбит', '1998', 'детектив', 'Б.Акунин', '600 руб.')
# b.save_json('book.json')
# new_b = Book.load_json('book.json')
# print(new_b)
# new_b.info()


### 3. К уже реализованному классу «Стадион» добавьте возможность упаковки и распаковки данных
# с использованием json и pickle.

# import pickle
# import json
#
# class Stadium:
#     def __init__(self, name, year, country, city, capacity):
#         self.name = name
#         self.year = year
#         self.country = country
#         self.city = city
#         self.capacity = capacity
#
#     def info(self):
#         print(f'Стадион {self.name} может поместить {self.capacity} человек.')
#
#     def save_pickle(self, filename):
#         with open(filename, 'wb') as f:
#             pickle.dump(self, f)
#
#     @staticmethod
#     def load_pickle(filename):
#         try:
#             with open(filename, 'rb') as f:
#                 return pickle.load(f)
#         except FileNotFoundError:
#             print('Указан неверный путь к файлу!')
#
#     def save_json(self, filename):
#         with open(filename, 'w') as f:
#             json.dump(self.__dict__, f)
#
#     @staticmethod
#     def load_json(filename):
#         with open(filename, 'r') as f:
#             stadium_dict = json.load(f)
#             return Stadium(**stadium_dict)
#
#     def __str__(self):
#         return f'Название: {self.name}\n' \
#                f'Дата открытия: {self.year}\n' \
#                f'Страна: {self.country}\n' \
#                f'Город: {self.city}\n' \
#                f'Вместимость: {self.capacity}'
#
#
# a = Stadium('Торпедо', '1933', 'Россия', 'Москва', '65 000 человек')
# print(a)
# a.save_pickle('stadium.txt')
# new_a = Stadium.load_pickle('stadium.txt')
# print(new_a)
# new_a.info()
#
# b =Stadium('Динамо', '1928', 'Россия', 'Москва', '70 000 человек')
# b.save_json('stadium.json')
# new_b = Stadium.load_json('stadium.json')
# print(new_b)
# new_b.info()