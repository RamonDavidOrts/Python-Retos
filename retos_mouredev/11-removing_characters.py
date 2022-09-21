def new_sentence(str1, str2):
    out = ""
    for char in str1:
        if char not in str2:
            out += char
    return out

def removing(str1, str2):
    print(new_sentence(str1, str2))
    print(new_sentence(str2, str1))
    
str1 = "el niño de la pelota"
str2 = "es un idealista pertinaz"

removing(str1, str2)
