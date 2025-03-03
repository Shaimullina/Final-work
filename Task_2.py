"""Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь, 
где ключами являются уникальные слова, а значениями — множества индексов строк, в которых эти слова встречаются."""


def words_index_map(strings: list) -> dict:
    for _ in strings:
        enumNames = list(enumerate(strings))
    return enumNames


strings = ["hello world", "world of python", "hello again"]
print(words_index_map(strings))
