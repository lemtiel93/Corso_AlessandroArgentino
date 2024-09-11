class Libro:
    
    def __init__(self, titolo, autore, pagine):
        try:
            if type(titolo== str) and type (autore == str) and type(pagine == int):
                self.titolo = titolo
                self.autore = autore
                self.pagine = pagine
        except: 
            print("errore")
            
    def descrizione(self):
        print(f"Titolo :{self.titolo} Autore: {self.autore} Pagine: {self.pagine}")
        
libro = Libro("Il visconte dimezzato", "Italo Calvino", 5)

libro.descrizione()