# Esercizio con if annidati e input

'''nome = input("Inserisci Nome:")
if nome == "Pippo":
    eta = int(input("Inserisci eta:"))
    if eta == 25:
        cognome = input("Inserisci Cognome:")
        if cognome == "Paperino":
            print("Ti chiami Pippo Paperino e hai 25 anni")
        else:
            print("Non sei Paperino")
    else:
        print("Non hai 25 anni")
else:
    print("Non ti chiami Pippo")'''
    
# Esercizio 2

'''parola = input("Inserisci una parola")
scelta =int(input("Scegli se concatenare (1), sostituisci (2) o eliminare la parola(3)"))

if scelta == 1:
    parola2 = input("Aggiungi parola")
    parola = parola + parola2
    print (parola)
elif scelta == 2:
    nuova_parola =input("Sostituisci:")
    parola = nuova_parola
    print (parola)
elif scelta == 3:
    del parola
    print("Parola eliminata")
else: 
    print("errore")'''

# Esercizio 3

nome = "Mario"
password = "Rossi"
id = 0
utenti = [("Mario", "Rossi", id)]

nome_in = input("Inserisci Nome: ")
password_in = input("Inserisci Password: ")

if nome_in != "Mario":  
    id += 1 
    # Registra direttamente nuovo utente se username non coincide 
    utenti.append((nome_in, password_in, id))
elif nome_in =="Mario" and password_in != "Rossi": # Verifica se password è errata e in caso chiede di modificarla
    print("Password Errata")
    password_in = input("Immetti nuova password: ")
    utenti.remove(("Mario","Rossi", id))
    utenti.append((nome_in, password_in, id))
else:
    print("Sei già registrato")

print("Lista degli utenti:", utenti)
    
  




