import math

class Punto:
    def __init__ (self,x,y):  #metodo costruttore
        self.x = x
        self.y = y
        
    def muovi(self, dx, dy):   #metodo che trasla il punto di un vettore v = (dx, dy)
        return self.x + dx, self.y + dy
    
    def distanza_da_origine(self):  #metodo che calcola la distanza dall'origine
        return math.sqrt(self.x**2 + self.y**2)
    
    def __str__(self):              #metodo stampa
        return f"({self.x},{self.y})"
    

punto1 = Punto(4,3)

print(punto1.muovi(-2,-3))
print(punto1.distanza_da_origine())
print(punto1)

#aggiungo elementi ad una lista
punti = []

punti.append(punto1)
punti.append(Punto(7,-1))
punti.append(Punto(3,-1))

for p in punti:
    print(p)   #printo richiamando il metodo speciale __str__