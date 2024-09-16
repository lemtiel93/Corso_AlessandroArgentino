import menu

def funzione1():
    print("Ciao")

def funzione2():
    print("Salve")
    
def funzione3():
    print("Arrivederci")
    
menuogg = menu.Menu("Menù di prova")

menuogg.aggiungi_opzioni("1","Stampa Ciao",funzione1)

menuogg.aggiungi_opzioni("2","Stampa Salve",funzione2)

menuogg.aggiungi_opzioni("3","Stampa Arrivederci",funzione3)

menuogg.visualizza_menu()

menuogg.scelta_menu()