class Ristorante:
    
    def __init__(self, nome , tipo_cucina):
        if type(nome) == str and type(tipo_cucina) == str:
            self.nome = nome
            self.tipo_cucina = tipo_cucina
            self.aperto = False
            self.menu = {}
        else:
            print("inserisci dati validi")
            
    def descrivi_ristorante(self):
        print(f"Sono il ristorante {self.nome} e con cucina {self.tipo_cucina} ")
    
    def stato_apertura(self):
        if self.aperto == True:
            print("Aperto")
        else:
            print("Chiuso")
    
    def apri_ristorante(self):
        if self.aperto == False:
            self.aperto = True
            print("Ristorante ora aperto")
        else: 
            print("Già aperto")
    
    def chiudi_ristorante(self):
        if self.aperto == True:
            self.aperto = False
            print("Ristorante ora chiuso")
        else: 
            print("Già chiuso")
    
    def aggiungi_al_menu(self, piatto , prezzo):
        if type(piatto) == str and (type(prezzo)== float or type(prezzo)==int):
            self.menu[piatto] = prezzo
        
        
    def togli_dal_menu(self, piatto):
        if type(piatto)== str and piatto in self.menu:
            del self.menu[piatto]
        
    def stampa_menu(self):
        print(self.menu)

ristorante = Ristorante("Spaccanapoli","Pizzeria")

ristorante.descrivi_ristorante()
ristorante.stato_apertura()
ristorante.apri_ristorante()
ristorante.aggiungi_al_menu("Diavola",10)
ristorante.aggiungi_al_menu("Indiana", 8)
ristorante.aggiungi_al_menu("Margherita", 100)
ristorante.togli_dal_menu("Margherita")

ristorante.stampa_menu()