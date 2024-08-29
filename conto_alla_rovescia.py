while True:
    numero = int(input("Inserisci un numero "))
    for i in range(numero,-1,-1):
        print(i)
    continua = input("Vuoi continuare? y/n")
    if continua == 'n':
        break