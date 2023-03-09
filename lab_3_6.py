# Копылов Кирилл, Брюзгин Виктор ФБИ-02
# Раздел III. Работа со списками. Операции над списками в Python (по вариантам)

# Задание 3.6
# 1. Считать из параметров командной строки одномерный массив, состоящий из N целочисленных элементов.;
# 2. Найти максимальный элемент;
# 3. Вывести количество меньших чисел, чем максимальный элемент;
# 4. Вывести сумму чисел больших 5.

# Импорт библиотеки "argparse" для разбора параметров (аргументов) командной строки
import argparse

# Создание парсера argparse
parser = argparse.ArgumentParser()

# Добавление аргумента
parser.add_argument("numbers", nargs="+", type=int)

# Получение аргументов
arguments = parser.parse_args()

# Получение массива чисел
numbers = arguments.numbers

# Максимальное число
maximum_number = numbers[0]
for num in numbers:
    if num > maximum_number:
        maximum_number = num

# Количество чисел меньших максимального числа
less_than_max = 0
for num in numbers:
    if num < maximum_number:
        less_than_max += 1

# Сумма чисел больших 5
greater_than_5_sum = 0
for num in numbers:
    if num > 5:
        greater_than_5_sum += num

# Вывод результатов
print("Максимальный элемент:", maximum_number)
print("Количество меньших чисел, чем максимальный элемент:", less_than_max)
print("Сумма чисел больших 5:", greater_than_5_sum)