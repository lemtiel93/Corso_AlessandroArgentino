class Punto:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def muovi(self, dx , dy):
        self.x += dx
        self.y += dy
    
    def distanza_origine(self):
        return self.x , self.y

punto = Punto(3,4)

punto.muovi(1,1)

print(punto.distanza_origine())