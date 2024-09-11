def palindromo(stringa):
    new_stringa = ''
    for char in stringa:
        if char.isalpha():
            new_stringa += char.lower()
    
    for i in range(len(new_stringa) // 2):
        if new_stringa[i] != new_stringa [len(new_stringa) - i - 1]:
            return False
    return True 
        
frase = input("Inserisci frase ")

print(palindromo(frase))
        


