"""Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь, 
где ключами являются уникальные слова, а значениями — множества индексов строк, в которых эти слова встречаются."""


def words_index_map(strings: list) -> dict:
    translation = input()
    enumNames = enumerate(translation)
    translation.dict = {}


# Тест
strings = ["hello world", "world of python", "hello again"]
print(words_index_map(strings))
# {'hello': {0, 2}, 'world': {0, 1}, 'of': {1}, 'python': {1}, 'again': {2}}
