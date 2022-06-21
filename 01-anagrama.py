def isAnagram(wordOne, wordTwo):
    if wordOne.lower() == wordTwo.lower(): 
        return False
    return sorted(wordOne.lower()) == sorted(wordTwo.lower())
    

print(isAnagram("Voltaire", "areitvol"))