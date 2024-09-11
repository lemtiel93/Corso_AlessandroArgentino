class Prodotto:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        
        if type(descrizione) == str and type(costo_produzione) == int and type(prezzo_vendita) == int:
            self.descrizione = descrizione
            self.costo_produzione = costo_produzione
            self.prezzo_vendita = prezzo_vendita
        else:
            raise ValueError("Errore inserimento dati")
        
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Xbox(Prodotto):
    
    def __init__(self , descrizione , costo_produzione, prezzo_vendita , serie):
        super().__init__(descrizione , costo_produzione , prezzo_vendita)
        self.serie = serie

class Computer(Prodotto):
    
    def __init__(self , descrizione , costo_produzione, prezzo_vendita , processore):
        super().__init__(descrizione , costo_produzione , prezzo_vendita)
        self.processore = processore
    
    def get_processore(self):
        return self.processore

computer = Computer("Mac",20,30,"i7")

print(computer.calcola_profitto())
print(computer.get_processore())
