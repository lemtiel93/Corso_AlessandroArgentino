
lista = [1,4,42,3,4,4,4,4,4,3]

tupla = (1, 2, 3)

set2 = { 3, 4, 5}

set2.add(7)
set2.add(5)
print(set(lista))
print(list(set(lista)))

dizionario = {1:{"nome" : "Pape",
              "cognome": "rino"},
              2:{"nome" : "giovanni",
                 "cognome" : "verdi"}}

print(dizionario[2]['nome'])