class Pantalone:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        
        if type(descrizione) == str and type(costo_produzione) == int and type(prezzo_vendita) == int:
            self.descrizione = descrizione
            self.costo_produzione = costo_produzione
            self.prezzo_vendita = prezzo_vendita
        else:
            raise ValueError("Errore inserimento dati")
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Maglietta:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        
        if type(descrizione) == str and type(costo_produzione) == int and type(prezzo_vendita) == int:
            self.descrizione = descrizione
            self.costo_produzione = costo_produzione
            self.prezzo_vendita = prezzo_vendita
        else:
            raise ValueError("Errore inserimento dati")
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Computer:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        
        if type(descrizione) == str and type(costo_produzione) == int and type(prezzo_vendita) == int:
            self.descrizione = descrizione
            self.costo_produzione = costo_produzione
            self.prezzo_vendita = prezzo_vendita
        else:
            raise ValueError("Errore inserimento dati")
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Xbox:
    def __init__(self, descrizione, costo_produzione, prezzo_vendita):
        
        if type(descrizione) == str and type(costo_produzione) == int and type(prezzo_vendita) == int:
            self.descrizione = descrizione
            self.costo_produzione = costo_produzione
            self.prezzo_vendita = prezzo_vendita
        else:
            raise ValueError("Errore inserimento dati")
    
    def calcola_profitto(self):
        return self.prezzo_vendita - self.costo_produzione

class Abbigliamento:
    
    def __init__(self,indumento,materiale):
        if type(indumento) == Pantalone or type(indumento) == Maglietta:
            self.indumento = indumento
            self.materiale = materiale

class Elettronica:
    
    def __init__(self,elettro,materiale):
        if type(elettro) == Computer or type(elettro) == Xbox:
            self.elettro = elettro
            self.materiale = materiale

class Fabbrica:
    
    def __init__(self):
        self.oggetti = {}
    
    # Questo prende il numero di prodotti da aggiungere
    def aggiungi_prodotto(self,prodotto, num):
        
        if prodotto.descrizione in self.oggetti:
            self.oggetti[prodotto.descrizione] += num
        else:
            self.oggetti[prodotto.descrizione] = num
    
    def vendi_prodotto(self,prodotto):
        
        if prodotto.descrizione in self.oggetti and self.oggetti[prodotto.descrizione]>0:
            self.oggetti[prodotto.descrizione] -= 1
            print(prodotto.calcola_profitto())
        else: 
            print("Prodotto non presente")
    
    def resi_prodotto(self, prodotto):
        if prodotto.descrizione in self.oggetti:
            self.oggetti[prodotto.descrizione] += 1
        else:
            self.oggetti[prodotto.descrizione] = 1

pantalone = Pantalone("Pantalone", 30, 50)
maglietta = Maglietta("Maglietta", 15, 25)
computer = Computer("Computer", 500, 800)
xbox = Xbox("Console di gioco", 300, 500)

fabbrica = Fabbrica()

    
fabbrica.aggiungi_prodotto(pantalone, 5)
fabbrica.aggiungi_prodotto(maglietta, 10)
fabbrica.aggiungi_prodotto(computer, 2)
fabbrica.aggiungi_prodotto(xbox, 3)

fabbrica.vendi_prodotto(xbox)
fabbrica.vendi_prodotto(xbox)
fabbrica.vendi_prodotto(xbox)
fabbrica.vendi_prodotto(xbox)
