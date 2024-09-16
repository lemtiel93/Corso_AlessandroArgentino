import numpy as np

class Matrice:
    # Costruttore per matrice con numeri casuali da 1 a 10, e righe/colonne specificate da utente
    def __init__(self, dim1, dim2):
        if  (type(dim1) == int and dim1 > 0) and (type(dim2) == int and dim2 > 0):
            self.dim1 = dim1
            self.dim2 = dim2
            self.matrice = np.random.randint(0,10, size = (self.dim1, self.dim2))
        else:
            raise Exception("Hai sbagliato ad inserire i valori")
            
    def trasposta(self):
        return self.matrice.T

    def somma(self):
        
        return np.sum(self.matrice)

    def moltiplicazione(self):
        
        self.matrice2 = np.random.randint(0,10, size = (self.dim1, self.dim2))
        
        
        return (self.matrice * self.matrice2)

    def media_elementi(self):
        return (np.mean(self.matrice))

    def determinante(self):
        if self.dim1 == self.dim2:
            return np.round(np.linalg.det(self.matrice))
        else:
            return "Impossibile calcolare determinante"
        
    def sottomatrice(self):
        if self.dim1 > 2 and self.dim2 > 2:
            return (self.matrice[1:-1,1:-1])
        else:
            return "Impossibile stampare sottomatrice"
    
    def get_matrice(self):
        return self.matrice
    



