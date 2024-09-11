class Punto:
    
    def __init__(self,x,y):
        try:
            if isinstance(x, int) and isinstance(y, int):
                self.x = x
                self.y = y
        except:
            print("Inserisci valori interi")
            
        
    def muovi(self, dx , dy):
        try:
            if type (dx == int) and type(dy == int):
                self.x += dx
                self.y += dy
        except:
            print("Inserisci valori interi")
       
    
    def distanza_origine(self):
        return self.x , self.y

punto = Punto(5,4)

punto.muovi("a",1)

print(punto.distanza_origine())