
while True:
    numero = input("Inserisci un numero o premi s per stoppare: ")
    if numero == "s":
        break
    numero = int(numero)
    if numero % 2 == 0:
        print("Numero Pari")
    else:
        print("Numero Dispari")