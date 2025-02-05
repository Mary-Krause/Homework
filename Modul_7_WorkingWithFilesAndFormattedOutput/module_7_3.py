import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for char in ",.=!?;: -":
                        text = text.replace(char, " ")
                    all_words[file_name] = text.split()
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        word_positions = {}
        for name, words in self.get_all_words().items():
            try:
                word_positions[name] = words.index(word) + 1
            except ValueError:
                word_positions[name] = None
        return word_positions

    def count(self, word):
        word = word.lower()
        word_counts = {}
        for name, words in self.get_all_words().items():
            word_counts[name] = words.count(word)
        return word_counts


# Пример использования
finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # Позиция первого вхождения слова
print(finder2.count('teXT'))  # Количество слова в файле


# Этот код создает класс WordsFinder, который читает содержимое файлов, очищает текст от пунктуации, и затем предоставляет методы для поиска и подсчета слов. Если файл не найден, он добавляет его в словарь с пустым списком слов.