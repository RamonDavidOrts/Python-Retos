def reverse(text):
    new_text = ""
    for i in range(len(text)-1, -1, -1):
        new_text += text[i]
    return new_text

def recursive_reverse(text, reversed_text="", index=None):
    if index == 0:
        return text[0]
    if index == None:
        index = len(text) - 1
    return text[index] + recursive_reverse(text, index - 1)

text = "hocus pocus"
print(reverse(text))
print(recursive_reverse(text))
