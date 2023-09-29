print("Программа преобразует все идущие подряд пробелы в один.")
# Ввод строки
input_string = input("Введите строку: ")

# Замена повторяющихся пробелов на один пробел
output_string = ' '.join(input_string.split())

# Вывод измененной строки
print(output_string)