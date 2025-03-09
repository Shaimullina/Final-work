"""Задача 2: Словари и множества
Напишите функцию, которая принимает список строк и возвращает словарь,где ключами являются уникальные слова,
а значениями — множества индексов строк, в которых эти слова встречаются."""


def words_index_map(strings: list) -> dict:
    dict_words = {j: 1 for i in strings for j in i.lower().split()}
    for i in dict_words:
        new_list = []
        for j in range(len(strings)):
            if i in strings[j].lower():
                new_list.append(j)
        new_list = set(new_list)
        dict_words[i] = new_list
    return dict_words


strings = ["hello world", "world of python", "hello again"]
print(words_index_map(strings))
