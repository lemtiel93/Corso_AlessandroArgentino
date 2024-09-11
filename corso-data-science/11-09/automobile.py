class Automobile: # dichiaro la classe
    numero_di_ruote = 4 # attributo di classe
    
    def __init__(self, marca, modello): # metodo costruttore
        self.marca = marca # attributo di istanza
        self.modello = modello # attributo di istanza
        
    def stampa_info(self): # metodo di istanza
        print("L'automobile è una" , self.marca, self.modello)

automobile = Automobile("audi" , "a3")

automobile.stampa_info()
