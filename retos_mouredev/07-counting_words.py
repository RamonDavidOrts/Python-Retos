special_chars = "¿?¡!.,;\"'()-_"

def counting_words(text):
    text = text.lower()
    for char in special_chars:
        text = text.replace(char, "")
    list = text.split()
    dict = {}
    for word in list:
        if word in dict:
            dict[word] += 1
        else:
            dict[word] = 1
    return dict

text = "El niño comía queso y guindillas, ¡¿El niño?!, ¿Guindillas? y queso (que es peor)"
print(counting_words(text))
