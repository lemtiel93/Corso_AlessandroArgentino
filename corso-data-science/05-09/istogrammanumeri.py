# Chiedere lista di numeri, fornisce in output un istogramma su quei numeri

lista_numeri = []
while True:
    try:
        numero = int(input("Inserisci Numero o premi altro per finire: "))
        if numero >= 0: lista_numeri.append(numero)
    except:
        break
    
for num in lista_numeri: print(num * '*')
    
    
