# Chiede a utente una parola, e restituisce solo le vocali, per ogni vocale l'indice delle vocali

frase = input("Inserisci frase: ").lower()

vocali = "aeiou"

vocali_trovate = []
indici = []

# For che cicla su ogni lettera della frase usando un indice
for i  in range(len(frase)):
    if frase[i] in vocali:
        vocali_trovate.append(frase[i])
        indici.append(i)
            
print(vocali_trovate)
print(indici)
