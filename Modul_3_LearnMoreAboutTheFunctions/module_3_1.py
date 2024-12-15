# Переменная для подсчета количества вызовов
calls = 0

# Функция для подсчета вызовов
def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    count = 0
    for i in string:
        count += 1
    max_size = string.upper()
    min_size = string.lower()
    string = (count, max_size, min_size)
    return string


def is_contains(string, list_to_search):
    count_calls()
    strung_up = string.upper()
    list_to_search_up = []
    flag = False
    for j in list_to_search:
        list_to_search.append(j.upper())
    for i in list_to_search_up:
        if i == strung_up:
            flag = True
    return flag


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'urban', 'urBN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
