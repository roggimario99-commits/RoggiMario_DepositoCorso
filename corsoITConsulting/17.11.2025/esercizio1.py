import math

class Punto:
    def __init__ (self,x,y):
        self.x = x
        self.y = y
        
    def muovi(self, dx, dy):
        return self.x + dx, self.y + dy
    
    def distanza_da_origine(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):
        return f"({self.x},{self.y})"
    

punto1 = Punto(4,3)

print(punto1.muovi(-2,-3))
print(punto1.distanza_da_origine())
print(punto1)

punti = []

punti.append(punto1)
punti.append(Punto(7,-1))
punti.append(Punto(3,-1))

for p in punti:
    print(p)