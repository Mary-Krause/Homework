first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# Список длин строк из first_strings, если длина >= 5
first_result = [len(word) for word in first_strings if len(word) >= 5]

# Список кортежей слов одинаковой длины из обоих списков
second_result = [(word1, word2) for word1 in first_strings for word2 in second_strings if len(word1) == len(word2)]

# Словарь строк с четной длиной из объединенных списков
third_result = {word: len(word) for word in first_strings + second_strings if len(word) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
