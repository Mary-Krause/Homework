def single_root_words(root_word, *other_words):
    same_words = []
    list_words_up = []
    for i in other_words:
        word_lower = i.lower()
        if root_word.lower() in word_lower or word_lower in root_word.lower():
            same_words.append(i)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
