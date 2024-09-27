class Menu:
    # Assegna titolo a menu, e crea dizionario con opzioni
    def __init__(self, titolo):
        self.titolo = titolo
        self.opzioni = {}
        
    def aggiungi_opzioni(self, chiave , descrizione ,funzione):
        self.opzioni[chiave] = {"descrizione" : descrizione,
                                "funzione" : funzione}
    
    def visualizza_menu(self):
        print(self.titolo)
        for opz in self.opzioni:
            print(opz + ":" , self.opzioni[opz]['descrizione'])
    
    def scelta_menu(self, chiave):
            
            self.chiave = chiave
            if self.chiave not in self.opzioni:
                return ("Inserisci Opzione valida")
            else:
                return self.opzioni[self.chiave]['funzione']()
            
        
        