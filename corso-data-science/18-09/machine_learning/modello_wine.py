from sklearn.datasets import load_wine
from esercizio_iris2 import ModelloIris
from menu import Menu

wine = ModelloIris(load_wine())
menu = Menu('Menu modello di machine learning')
wine.split_dataset()

menu.aggiungi_opzioni('1','Scala i dati' ,wine.scala_dati)

menu.aggiungi_opzioni('2', 'Valuta il modello', wine.create_evaluate_model)
menu.aggiungi_opzioni('3', 'Genera matrie di confusione', wine.matrice_confusione)

menu.visualizza_menu()
menu.scelta_menu('1')
#menu.scelta_menu('2')
#menu.scelta_menu('3')
#menu.scelta_menu('4')