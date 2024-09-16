class Menu:
    # Assegna titolo a menu, e crea dizionario con opzioni
    def __init__(self, titolo):
        self.titolo = titolo
        self.opzioni = {}
        
    # Non accetta 's' come chiava perchè sarà condizione di uscita
    def aggiungi_opzioni(self, chiave , descrizione ,funzione):
        if chiave.lower() == 's':
            print("Chiave s non valida")
            return
        self.opzioni[chiave] = {"descrizione" : descrizione,
                                "funzione" : funzione}
    
    def visualizza_menu(self):
        print(self.titolo)
        for opz in self.opzioni:
            print(opz + ":" , self.opzioni[opz]['descrizione'])
    
    def scelta_menu(self):
        while True:
            self.scelta = input("Fai scelta o chiudi con 's': ")
            if self.scelta.lower() == 's':
                break
            elif self.scelta not in self.opzioni:
                print("Inserisci Opzione valida")
            else:
                self.opzioni[self.scelta]['funzione']()
            
        
        