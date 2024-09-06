# Decoratore che controlla se stringa inserita è uguale in lunghezza a stringa compressa
def decoratore(funzione):
    def wrapper(stringa):
        stringa_compressa = funzione(stringa)
        if len(stringa_compressa) == len (stringa):
            return stringa
        else:
            return stringa_compressa
    return wrapper 

# Funzione per comprimere stringa
@decoratore
def comprimi_stringa(stringa):
    new_stringa = ''
    count = 1
    
    # Itero stringa partendo da 1 e confronto con valore precedente
    for i in range(1, len(stringa)):
        if stringa[i - 1] == stringa[i]:
            count +=1
        else:
            new_stringa += stringa[i - 1] + str(count)
            count = 1
    
    # Aggiungo ultimo carattere che il for non stampa
    new_stringa += stringa[-1] + str(count)
    return new_stringa


# Funzione per chiedere in input stringa e controllarne se il valore è di soli caratteri alfabetici
def inserisci_stringa():
    while True:
        stringa = input("Inserisci stringa di soli caratteri ")
        if stringa.isalpha():
            return stringa
        else:
            continue

# Test della funzione       
print(comprimi_stringa(inserisci_stringa()))

