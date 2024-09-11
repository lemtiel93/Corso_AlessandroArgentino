import libro

class Biblioteca:
    
    def __init__(self):
        self.lista_libri = []
    
    def aggiungi_libro(self, libros):
        if type(libros == libro.Libro):
            self.lista_libri.append(libros)
    
    def stampa_libri(self):
        for lib in self.lista_libri:
            lib.descrizione()

biblioteca = Biblioteca()
libro1 = libro.Libro("prova","prova", 2)
libro2 = libro.Libro("prova2","prova2", 5)

biblioteca.aggiungi_libro(libro1)
biblioteca.aggiungi_libro(libro2)
biblioteca.aggiungi_libro(libro.Libro("prova3", "prova4", 5))

biblioteca.stampa_libri()            