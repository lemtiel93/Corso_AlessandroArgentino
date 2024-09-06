def sequenza_fibonacci (n):
    sequenza = [0,1]
    if n == 0 :
        return sequenza[0]
    elif n == 1:
        return sequenza
    else:
        for i in range (2, n+1):
            sequenza.append(sequenza [i - 2] + sequenza [i - 1])
    return sequenza
    
while True:
    try: 
        num = int(input("Inserisci fino a dove vuoi fare la sequenza di fibonacci: "))
        if num < 0:
            print("Inserisci numero positivo")
            continue
        print(sequenza_fibonacci(num))
        break
    except:
        print("Inserisci un numero valido")
            
            
    