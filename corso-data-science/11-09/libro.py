class Libro:
    
    def __init__(self, titolo, autore, pagine):
        
        if type(titolo == str):
            self.titolo = titolo
        else: 
            print("Il titolo deve essere una stringa")
        if type(autore == str):
            self.autore = autore
        else:
            print("Autore deve essere una stringa")
        if type (pagine == int):
            self.pagine = pagine
        else:
            print("Pagine deve essere numero")
        
    def descrizione(self):
        print(f"Titolo: {self.titolo} Autore: {self.autore} Pagine: {self.pagine}")
        
libro = Libro("Il visconte dimezzato", 54, "5")

if type(libro == Libro):
    libro.descrizione()
else: 
    print("Errore di tipo")