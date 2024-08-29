
# Inizializzo contatore per uscire dal ciclo while se arrivo a 5 numeri primi
contatore_numeri_primi_trovati = 0

while True:
    # Chiedo in input un numero
    numero = int(input("Inserisci un numero "))
    contatore = 0
    
    # Ciclo for che usa il range al contrario
    for i in range(numero,0,-1):
        
        # Conto quante volte un numero è divisibile per un numero al suo interno
        if numero%i == 0:
            contatore +=1
            
    # Verifico contatore per vedere se numero è primo
    if contatore == 2:
        print("Numero Primo ")
        contatore_numeri_primi_trovati +=1
    else:
        print("numero non primo")
        
    # Rompo il ciclo finchè non trovo 5 numeri primi
    if contatore_numeri_primi_trovati == 5:
        break