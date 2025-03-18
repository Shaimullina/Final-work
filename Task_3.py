"""Задача 3: Работа с файлами
Напишите программу, которая читает текстовый файл, удаляет из него все пустые строки и строки,
состоящие только из пробелов, а затем записывает результат в новый файл."""


def clean_file(input_file: str, output_file: str) -> None:
    try:
        with open("input", "w") as input_f:
            for line in input_f:
                clean_line = line.strip()
        with open("input", "r") as input_f, open("output.txt", "a") as output_f:
            for line in input_f:
                output_f.write(line)
    except FileNotFoundError:
        print(f"Файл '{input_file}' не найден!")
