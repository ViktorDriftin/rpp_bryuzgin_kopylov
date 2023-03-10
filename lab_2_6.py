# Копылов Кирилл, Брюзгин Виктор ФБИ-02
# Раздел II. Работа со строками в Python (по вариантам).

# Задание 2.6
# 1. Считать с клавиатуры произвольную строку;
# 2. В строке удалить все буквы "а";
# 3. Вывести количество удаленных символов;
# 4. Вывести в консоль полученную строку.

# 1. Считываем строку с клавиатуры
input_str = input("Введите произвольную строку с клавиатуры: ")

# 2. Удаляем все буквы "а" из строки и считаем их количество
output_str = input_str.replace('a', '')
removed_chars = input_str.count('a')

# 3. Выводим количество удаленных символов
print("Количество удалённых символов 'a':", removed_chars)

# 4. Выводим полученную строку
print("Полученная строка: ", output_str)