alfabeto = "abcdefghijklmnopqrstuvwxyz"


def inserisci_stringa():
    stringa = input("Inserisci frase ").lower()
    return stringa
    
def cripta_decripta(stringa,cripta):
    if cripta =="cripta":
        num = 3
    else:
        num = -3
    stringa_criptata =''
    for char in stringa:
        if char.isalpha():
            if char in alfabeto:
                i = (alfabeto.index(char) % 26) + num
                stringa_criptata += alfabeto[i]
        else:
            stringa_criptata += char
    return stringa_criptata

stringa1 = inserisci_stringa()
stringa2 = (cripta_decripta(stringa1,"cripta"))
stringa3 = (cripta_decripta(stringa2,"dcripta"))

print(stringa2 ,stringa3)