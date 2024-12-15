def print_params(a=1, b='строка', c=True):
    print(a, b, c)


# 1.Функция с параметрами по умолчанию:
print("    1.Функция с параметрами по умолчанию:")
print_params()
print_params(5)
print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
print("    2.Распаковка параметров")
values_list = [2, False, 'Monday']
values_dict = {'a': True, 'b': 7, 'c': 'Tuesday'}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
print("    3.Распаковка + отдельные параметры:")
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
