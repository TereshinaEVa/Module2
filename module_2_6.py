def single_root_words(root_word, *other_words):
    some_words = []
    for i in other_words:
        word_ = i.lower()
        word2 = root_word.lower()
        if word_.count(word2) > 0 or word2.count(word_) > 0:
            some_words.append(i)
    return some_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')

print(result1)
print(result2)
