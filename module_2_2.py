first = int(input("Введите первое число: "))
second = int(input("Введите второе число: "))
third = int(input("Введите третье число: "))
print(f'Вы ввели следующие числа: {first}, {second}, {third}')
if first == second == third:
    print(f'Количество повторяющихся значений: {3}')
elif first == second or first == third or second == third:
    print(f'Количество повторяющихся значений: {2}')
else:
    print("Повторяющиеся значения отсутствуют")