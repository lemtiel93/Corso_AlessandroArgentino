import math
class Punto:
    
    def __init__(self,x,y):
        try:
            if type(x == int) and type(y == int):
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
        return math.sqrt(self.x**2 + self.y**2)

punto = Punto(5,4)

if type(punto == Punto):
    punto.muovi(4,1)

if type(punto == Punto):
    print(punto.distanza_origine())