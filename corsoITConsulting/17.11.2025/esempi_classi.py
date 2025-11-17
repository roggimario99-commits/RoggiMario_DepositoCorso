########################
### Classe Automobile ##
########################

class Automobile:
    numero_di_ruote = 4
    
    def __init__(self, marca, modello):  #metodo costruttore
        self.marca = marca
        self.modello = modello
        
    def __str__(self):                   #metodo speciale o subordinato (serve a stampare quello che vuoi tu e non l'indirizzo di memoria)
        return f"L'auto è una: {self.marca} {self.modello}"
        
    def stampa_info(self):
        print("L'auto è una", self.marca, self.modello)
        
auto1 = Automobile("Citroen", "C1")   
auto2 = Automobile("Fiat","500")

print("### Classe Automobile ###")
auto1.stampa_info()   
auto2.stampa_info()   

print(auto1)
print(auto2)

########################
### Metodo statico ### 
########################

class Calcolatrice:  #dichiarazione classe Calcolatrice
    @staticmethod
    def somma(a,b):  #metodo statico somma (non prende in input istanze della classe - non c'è self!)
        return a + b

print("### Metodo Statico ###")    
print(Calcolatrice.somma(2,3))
calcolo1 = Calcolatrice()
print(calcolo1.somma(2,3))

########################
### Metodo di Classe ### 
########################

class Contatore:
    num_istanze = 0
    def __init__(self):
        Contatore.num_istanze += 1
        
    @classmethod
    def mostra_num_istanze(cls):
        print(f"sono state create {cls.num_istanze} istanze.")

print("### Metodo di classe ###")     
Contatore.mostra_num_istanze()
c1 = Contatore()      

Contatore.mostra_num_istanze()
c2 = Contatore()       

Contatore.mostra_num_istanze()
c3 = Contatore()     

Contatore.mostra_num_istanze()