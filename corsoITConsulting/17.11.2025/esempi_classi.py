class Automobile:
    numero_di_ruote = 4
    
    def __init__(self, marca, modello):
        self.marca = marca
        self.modello = modello
        
    def __str__(self):
        return f"L'auto è una: {self.marca} {self.modello}"
        
    def stampa_info(self):
        print("L'auto è una", self.marca, self.modello)
        
auto1 = Automobile("Citroen", "C1")   
auto2 = Automobile("Fiat","500")
  
auto1.stampa_info()   
auto2.stampa_info()   

print(auto1)
print(auto2)
