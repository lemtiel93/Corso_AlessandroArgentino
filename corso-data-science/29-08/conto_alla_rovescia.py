while True:
    numero = int(input("Inserisci un numero "))
    
    # Loop per stampare tutti i numeri in maniera decrescente
    for i in range(numero,-1,-1):
        print(i)
    continua = input("Vuoi continuare? y/n")
    
    # Verifica se utente inserisce n per uscire dal ciclo
    if continua == 'n':
        break