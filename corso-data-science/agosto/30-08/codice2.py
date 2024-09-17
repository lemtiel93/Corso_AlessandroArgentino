while True:
    lista1 = []
    lista2 = []
    
    for i in range(5):
        numero = int(input("Inserisci numero lista 1 "))
        lista1.append(numero)
    for i in range(5):
        numero = int(input("Inserisci numero lista 2 "))
        lista2.append(numero)
    
    for i in range(5):
        print(lista1[i] + lista2[i])
    
    ripetere = input("Vuoi ripetere? (y/n)")
    
    if ripetere == 'n':
        break