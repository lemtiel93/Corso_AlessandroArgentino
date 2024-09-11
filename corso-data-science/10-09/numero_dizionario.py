
while True:
    try: 
        numero = int(input("Inserisci un numero intero positivo: "))
        if numero > 0:
            break
        else:
            print("hai inserito un numero negativo")
            continue
    except ValueError:
        print("Non hai inserito un numero intero")
        continue

dizionario = {'quadrato': numero ** 2, 
              'pari o dispari': 'pari' if numero % 2 == 0 else 'dispari',
              'cifre': len(str(numero))}

print(dizionario)