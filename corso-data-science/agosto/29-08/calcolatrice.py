operatore = int(input("Quale operatore vuoi usare? addizione (1), sottrazione (2), divisione (3), moltiplicazione (4) "))

x = int(input("Inserisci Primo  Numero "))
y = int(input("Inserisci Secondo Numero " ))

if operatore ==1:
    print (x+y)
elif operatore == 2:
    print(x-y)
elif operatore == 3:
    if y==0:
        print("Errore divisione per zero")
    else:
        print(x/y)
elif operatore ==4:
    print(x*y)
else:
    print("Inserisci numero da 1 a 4")