# Test su come funzionano gli if

try: 
    numero = int(input("Inserisci Numero:"))

    if numero > 20:
        print("Numero maggiore di 20")
    elif numero == 20:
        print("Numero uguale a 20")
    else:
        print("Numero minore di 20")
        
except:
    print ("Input errato")