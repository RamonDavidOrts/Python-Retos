def capitalize(text):
    list = text.split()
    list2 = []
    for word in list:
        new_word = word.replace(word[0], word[0].upper(), 1)
        list2.append(new_word)
    return " ".join(list2)

print(capitalize("el hombre que no estuvo allí"))
