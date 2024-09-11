stringa = input("inserisci stringa: ")
dizionario = {}

for char in stringa:
    if char in dizionario:
        dizionario[char] += 1
    else: 
        dizionario[char] = 1

lista_valori =list(dizionario.values())

lista_chiavi = list(dizionario.keys())

dizionario2 = dict(zip(lista_valori,lista_chiavi))

for element in sorted(dizionario2, reverse=True):
    print(f"chiave originaria: {dizionario2[element]}, valore originario: {element}")