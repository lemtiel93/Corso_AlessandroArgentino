import menu
import random
import numpy as np

def crea_matrice():
    dim1 = int(input("Inserisci numero righe "))
    dim2 = int(input("Inserisci numero colonne "))
    
    matrice = np.random.randint(0,10, size = (dim1, dim2))
    return  matrice

def trasposta():
    matrice = crea_matrice()
    print( matrice.T)

def somma():
    matrice = crea_matrice()
    print(np.sum(matrice))

def moltiplicazione():
    dim1 = int(input("Inserisci numero righe "))
    dim2 = int(input("Inserisci numero colonne "))
    matrice1 = np.random.randint(0,10, size = (dim1, dim2))
    matrice2 = np.random.randint(0,10, size = (dim1, dim2))
    
    print (matrice1 * matrice2)

def media_elementi():
    matrice = crea_matrice()
    print (np.mean(matrice))

def determinante():
    matrice = crea_matrice()
    print (np.linalg.det(matrice))
    
def sottomatrice():
    matrice = crea_matrice()
    print(matrice[1:-1,1:-1])

menuogg = menu.Menu("Menù Matrici")
menuogg.aggiungi_opzioni("1","stampa sotto matrice centrale",sottomatrice)
menuogg.aggiungi_opzioni("2","Crea matrice e fa trasposta",trasposta)
menuogg.aggiungi_opzioni("3","Somma tutti gli elementi della matrice creata",somma)
menuogg.aggiungi_opzioni("4","Genera 2 matrici e le moltiplica",moltiplicazione)
menuogg.aggiungi_opzioni("5","Fa media elementi matrice",media_elementi)
menuogg.aggiungi_opzioni("6","Calcola determinante",determinante)

menuogg.visualizza_menu()
menuogg.scelta_menu()