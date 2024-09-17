# Ciclo finchè utente non inserisce un numero di parole
while True:
    try: 
        numero_parole = int(input("Inserisci numero parole: "))
    except:
        continue

    parole = []
    for parola in range(numero_parole):
        parola = input("Inserisci parola: ")
        parole.append(parola)
        
    print(parole)
    ripetere = input("Vuoi ripetere? y/n ")
    if ripetere == "n": 
        break