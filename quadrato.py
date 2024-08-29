# Inizializzo lista numeri
numeri = []

# Ciclo per inserire numeri
while True:
    numero = input("Inserisci un numero o premi s per stoppare: ")
    # Rompo il ciclo se inserisco s da tastiera
    if numero == 's':
        break
    
    # Inserisco nella lista direttamente il quadrato del numero inserito
    numero = numeri.append(int(numero)**2)
    
print(numeri)
   