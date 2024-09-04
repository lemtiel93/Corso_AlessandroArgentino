# Chiedo in input lista di 10 numeri
numeri = []
for i in range (10):
        numero = int(input("Inserisci numero: "))
        numeri.append(numero)

# Inizializzo variabili di controllo per max e min
num_min = numeri[0]
num_max = numeri[0]
num_medio = 0

# Trovo max e min
for num in numeri:
    if num < num_min:
        num_min = num
    elif num > num_max:
        num_max = num

num_ordinati = []

# Elimino ogni volta il minimo e lo appendo ad una lista ordinata
while numeri: 
    num_min2 = numeri[0]
    for num in numeri:
        if num < num_min2:
            num_min2 = num
    numeri.remove(num_min2)
    num_ordinati.append(num_min2)
        
print(f"Numero min: {num_min} numero max: {num_max} mediana: {(num_ordinati[4] + num_ordinati[5]) / 2 }")
print(num_ordinati)