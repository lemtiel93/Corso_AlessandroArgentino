from menu import Menu

class Libro:
    def __init__(self,titolo,autore,anno,quantita):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.quantita = quantita
    def descrivi(self):
        print(f"titolo : {self.titolo} autore : {self.autore}")
        
    def set_quantita(self,quantita):
        self.quantita = quantita

class Libreria:
    def __init__(self):
        self.libri =[]
    
    def aggiungi_libro(self,libro):
        self.libri.append(libro)
        
    def visualizza_libri(self):
        for lib in self.libri:
            lib.descrivi()
    
    def cerca_libro(self, titolo):
        for lib in self.libri:
            if lib.titolo == titolo:
                lib.descrivi()
                return lib
            
    def modifica_quantita(self, titolo, nuova_quantita):
        libro = self.cerca_libro(titolo)
        try:
            libro.set_quantita(nuova_quantita)
        except:
            print("Libro non trovato")

libreria = Libreria()

def aggiungi_libro():
    titolo = input("TItolo ")
    autore = input("Autore: ")
    anno = input("Anno ")
    quantita = int(input("Numero : "))
    libro = Libro(titolo, autore, anno, quantita)
    libreria.aggiungi_libro(libro)

menu = Menu("Menu Libreria")
menu.aggiungi_opzione("1", "Aggiungi un libro", aggiungi_libro)
menu.aggiungi_opzione("2", "Visualizza tutti i libri", libreria.visualizza_libri)
menu.aggiungi_opzione("3", "Cerca un libro", libreria.cerca_libro)
menu.aggiungi_opzione("4", "Modifica la quantità di un libro", libreria.modifica_quantita)
menu.aggiungi_opzione("5", "Esci", exit)

while True: 
    menu.visualizza_menu()
    menu.scelta_menu()