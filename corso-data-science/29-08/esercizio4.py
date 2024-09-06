contatore_elementi = 0
numeri = []
# Ciclo While per inizializzare lista numeri
while True:
    numero = input("Inserisci un numero o premi s per stoppare: ")
    if numero.lower() == "s":
        break
    # Se utente ha inserito un numero lo aggiunge correttamente alla lista sennò va avanti
    try:
        numero = numeri.append(int(numero))
        # Incremento per contare quanti elementi corretti ci sono
        contatore_elementi +=1
    except ValueError:
        continue
# Controllo se lista è vuota
if not numeri:
    print("Lista Vuota")
else:
    # Inizializzo num max al primo elemento della lista
    num_max = numeri[0]
    for num in numeri:
        
        # Questo if registra se num é maggiore di num max e lo aggiorna nel caso
        if num_max < num:
            num_max = num
            
    print("Numero massimo",num_max)
    print("Numero elementi",contatore_elementi)
        
    
   