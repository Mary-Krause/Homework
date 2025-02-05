# Функция personal_sum
# Эта функция будет принимать коллекцию чисел, перебирать её, суммируя числовые элементы, и считать количество некорректных данных (не числовых типов).
def personal_sum(numbers):
    result = 0
    incorrect_data = 0

    for item in numbers:
        try:
            result += item
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {item}')

    return result, incorrect_data


# Функция calculate_average
# Эта функция будет использовать personal_sum для подсчёта суммы чисел в коллекции, а затем вычислять среднее арифметическое. Также она будет обрабатывать исключения, связанные с пустой коллекцией и некорректным типом данных.
def calculate_average(numbers):
    try:
        if not isinstance(numbers, (list, tuple, set)):
            raise TypeError

        total_sum, incorrect_count = personal_sum(numbers)

        if len(numbers) - incorrect_count == 0:
            return 0

        average = total_sum / (len(numbers) - incorrect_count)
        return average

    except ZeroDivisionError:
        return 0
    except TypeError:
        print('В numbers записан некорректный тип данных')
        return None


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать


