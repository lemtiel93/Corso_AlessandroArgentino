from menu import Menu
from sistema_matrici import Matrice



while True:
    menu = Menu("Menu della matrice")
    dim1 = int(input("Inserisci righe matrice: "))
    dim2 = int(input("Inserisci colonne matrice: "))
    
    matrice = Matrice(dim1 , dim2)
    
    if isinstance(matrice, Matrice):
        menu.aggiungi_opzioni("1","Trasposta",matrice.trasposta)
        menu.aggiungi_opzioni("2","Somma", matrice.somma)
        menu.aggiungi_opzioni("3","Moltiplicazione", matrice.moltiplicazione)
        menu.aggiungi_opzioni("4","Media elementi", matrice.media_elementi)
        menu.aggiungi_opzioni("5","Determinante",matrice.determinante)
        
        menu.visualizza_menu()
        
        scelta = input("Inserisci scelta o 's' per terminare ")
        if scelta == 's':
            break
        print(menu.scelta_menu(scelta))
