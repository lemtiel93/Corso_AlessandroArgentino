import random

def randomizza():
    numero = random.randint(1,100)
    return numero

def confronta_numero(num,num_generato):
    if num < num_generato:
        print("Inserisci numero più alto")
        return False
    elif num > num_generato:
        print("Inserisci numero più basso")
        return False
    else:
        print("bravo")
        return True
        
    
variabile_controllo = False

numero = randomizza()
while variabile_controllo is False:
    try:
        numero_ut = int(input("Inserisci numero: "))
    except:
        print("Inserisci numero valido")
        continue
    
    variabile_controllo = confronta_numero(numero_ut,numero)
    
    
    
    