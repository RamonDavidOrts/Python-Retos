def reverse(text):
    new_text = ""
    for i in range(len(text)-1, -1, -1):
        new_text += text[i]
    return new_text

def recursive_reverse(text, reversed_text="", index=None):
    if index is None:
        index = len(text) - 1        
    reversed_text += text[index]
    if index > 0:
        index = index - 1
        reversed_text = recursive_reverse(text, reversed_text, index)
    return reversed_text

text = "hocus pocus"
print(reverse(text))
print(recursive_reverse(text))
