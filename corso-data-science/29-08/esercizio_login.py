# Inserisco User e Password che serviranno per il confronto
user_check = "admin"
password_check = "12345"
colore_pref = "Rosso"
animale_pref = "Coccodrillo"

# Chiedo a utente User e Password
user = input("Inserisci Username: ")
password = input("Inserisci Password: ")


if user == user_check and password == password_check:
    # Se user e pass sono corretti do il benvenuto e chiedo se vuole cambiare qualcosa tra user e password
    print(f"Benvenuto {user}")
    change = input("Vuoi Cambiare nome utente o password? y/n ")
    
    # Se user vuole cambiare chiedo se vuole cambiare user o password
    if change == "y":
        change_choice = int(input("Scegli tra user (1) e password (2)"))
        
        # Chiedo a utente a quale domande vuole rispondere per cambiare user
        if change_choice == 1:
            secret_question = int(input("Scegli la domanda preferita: Qual è il tuo colore preferito?(1) e Quale è il tuo animale preferito? (2)"))
            
            # Se utente sceglie colore preferito faccio il check con il colore preferito presente in sistema e chiedo nuovo user
            if secret_question == 1:
                colore_preferito = input("Inserisci Colore Preferito")
                if colore_preferito == colore_pref:
                    user = input("Inserisci nuovo username: ")
                else:
                    print("Risposta errata")
                    
            # Se utente sceglie animale preferito faccio il check e chiedo nuovo user
            else :
                animale_preferito = input("Inserisci Animale preferito")
                if animale_preferito == animale_pref:
                    user = input("Inserisci nuovo username")
                else : 
                    print("Risposta errata")
        
        # Chiedo a utente a quale domande vuole rispondere per cambiare password  
        else:
            secret_question = int(input("Scegli la domanda preferita: Qual è il tuo colore preferito?(1) e Quale è il tuo animale preferito? (2)"))
            
            # Se utente sceglie colore preferito faccio il check con il colore preferito presente in sistema e chiedo nuova pass
            if secret_question == 1:
                colore_preferito = input("Inserisci Colore Preferito")
                if colore_preferito == colore_pref:
                    password = input("Inserisci nuova password: ")
                else:
                    print("Risposta errata")
            # Se utente sceglie animale preferito faccio il check e chiedo nuova pass
            else :
                animale_preferito = input("Inserisci Animale preferito")
                if animale_preferito == animale_pref:
                    password = input("Inserisci nuova password")
                else : 
                    print("Risposta errata")
    else: 
        print("Arrivederci")
                
else:
    print("Utente non loggato")

# Stampa nome utente e password
print(f"User: {user} Password: {password}")