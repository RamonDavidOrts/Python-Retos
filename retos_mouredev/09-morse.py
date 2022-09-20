import re

morse_dict = {
    "A": ".-",       "B": "-...",     "C": "-.-.",     "*": "----",
    "D": "-..",      "E": ".",        "F": "..--.",    "G": "--.",
    "H": "....",     "I": "..",       "J": ".---",     "K": "-.-",
    "L": ".-..",     "M": "--",       "N": "-.",       "Ñ": "--.--",
    "O": "---",      "P": ".--.",     "Q": "--._",     "R": ".-.",
    "S": "...",      "T": "-",        "U": "..-",      "V": "...-",
    "W": ".--",      "X": "-..-",     "Y": "-.--",     "Z": "--..",
    "0": "-----",    "1": ".----",    "2": "..---",    "3": "...--",
    "4": "....-",    "5": ".....",    "6": "-....",    "7": "--...",
    "8": "---..",    "9": "----.",    ".": ".-.-.-",   ",": "--..--",
    "?": "..--..",   '"': ".-..-.",   "/": "-..-.",    " ": "/"
}

def natural_to_morse(text):
    text = text.upper().replace("CH", "*")
    morse = ""
    for char in text:
        morse += morse_dict[char] + " "
    return morse

def morse_to_natural(morse):
    keys = list(morse_dict.keys())
    values = list(morse_dict.values())
    morse = morse.split()
    text = ""
    for char in morse:
        text += keys[values.index(char)]
    return text.replace("*", "CH")

def encode(text):
    if re.match("[ .-/]", text):
        return morse_to_natural(text)
    return natural_to_morse(text)
    
text = "En un lugar de la Mancha, yo por bien tengo que cosas tan señaladas"
morse = encode(text)
print(morse)
text = encode(morse)
print(text)
