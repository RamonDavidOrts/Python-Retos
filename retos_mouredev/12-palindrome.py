import re
from unicodedata import normalize

def is_palindrome(text):
    text = re.sub(
        r"([^n\u0300-\u036f]|n(?!\u0303(?![\u0300-\u036f])))[\u0300-\u036f]+", r"\1", 
        normalize( "NFD", text), 0, re.I)
    text = normalize("NFC", text).lower()
    chars = " ,.;:"
    for char in chars:
        text = text.replace(char, "")
    out = text[::-1]
    if out == text:
        return True
    return False
    
print(is_palindrome("Este niño es un demonio"))
print(is_palindrome("A mamá, Roma le aviva el amor a papá, y a papá, Roma le aviva el amor a mamá"))
