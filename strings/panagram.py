'''Given a string Str. The task is to check if it is Pangram or not. 
A pangram is a sentence containing every letter in the English Alphabet.'''

def panagram(str1: str):
    str1 = str1.lower()
    
    set1 = set(str1)
    
    suma = 0
    for _ in set1:
        suma += 1
    if suma >= 26:
        return True
    return False

res = panagram('The quick brown fox jumps over the dog')
print(res)