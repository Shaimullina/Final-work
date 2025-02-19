"""Задача 3: Работа с файлами
Напишите программу, которая читает текстовый файл, удаляет из него все пустые строки и строки, 
состоящие только из пробелов, а затем записывает результат в новый файл."""


def clean_file(input_file: str, output_file: str) -> None:
    with open(input_file) as input_f, open(output_file, "w") as output_f:
        for line in input_f:
            if line.strip():
                output_f.write(line)


# Тест
input_file = "input.txt"
output_file = "output.txt"
clean_file(input_file, output_file)
