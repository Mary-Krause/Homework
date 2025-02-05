def add_everything_up(a, b):
    try:
        # Пытаемся сложить a и b
        return a + b
    except TypeError:
        # Если возникает ошибка TypeError, возвращаем строковое представление a и b
        return str(a) + str(b)


# Примеры использования функции
print(add_everything_up(123.456, 'строка'))  # Вывод: 123.456строка
print(add_everything_up('яблоко', 4215))  # Вывод: яблоко4215
print(add_everything_up(123.456, 7))  # Вывод: 130.456

# Если вы хотите поэкспериментировать, можно добавить дополнительные проверки или обработку других исключений. Например, можно добавить проверку на тип аргументов перед выполнением сложения:

# def add_everything_up(a, b):
#     if isinstance(a, (int, float)) and isinstance(b, (int, float)):
#         return a + b
#     elif isinstance(a, str) and isinstance(b, str):
#         return a + b
#     else:
#         return str(a) + str(b)
