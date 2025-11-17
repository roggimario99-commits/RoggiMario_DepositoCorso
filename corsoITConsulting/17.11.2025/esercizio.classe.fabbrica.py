# ---------------------------------------------------------
# CLASSI BASE
# ---------------------------------------------------------
class Prodotto:
    
    def __init__(self, nome, costo_produzione, prezzo_vendita):
        self.nome = nome
        self.costo_produzione = costo_produzione
        self.prezzo_vendita = prezzo_vendita
    
    def calcola_profitto(self):
        return self.prezzo_vendita -self.costo_produzione
    
# ---------------------------------------------------------
# CLASSI PARALLELE
# ---------------------------------------------------------    
class Abbigliamento:
    
    def __init__(self, prodotto, materiale, taglia):
        self.nome = prodotto.nome
        self.costo_produzione = prodotto.costo_produzione
        self.prezzo_vendita = prodotto.prezzo_vendita
        self.materiale = materiale
        self.taglia = taglia
        
        
    def calcola_profitto(self):
        return self.prezzo_vendita -self.costo_produzione
    
class Elettronica:
    
    def __init__(self, prodotto, garanzia = False):
        self.nome = prodotto.nome
        self.costo_produzione = prodotto.costo_produzione
        self.prezzo_vendita = prodotto.prezzo_vendita
        self.garanzia = garanzia
        
    def calcola_profitto(self):
        return self.prezzo_vendita -self.costo_produzione

# ---------------------------------------------------------
# CLASSE FABBRICA
# ---------------------------------------------------------    

class Fabbrica:
    def __init__ (self, inventario = {}): 
        self.inventario = inventario  
        
    def aggiungi_prodotto(self, prodotto, quantita):
        if prodotto in self.inventario:
            self.inventario[prodotto.nome] += quantita
        else:
            self.inventario[prodotto.nome] = quantita
            
        
    def vendi_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.inventario:
            print("prodotto non presente in inventario!")
        else:
            self.inventario[prodotto.nome] -= quantita
            
    def reso_prodotto(self, prodotto, quantita):
        if prodotto.nome not in self.inventario:
            print("prodotto non presente in inventario!")
        else:
            self.inventario[prodotto.nome] += quantita
            
    def stato_inventario(self):
        print("\n--- Inventario Attuale ---")
        for nome, qta in self.inventario.items():
            print(f"{nome}: {qta} pezzi")
        print("---------------------------")        
    

if __name__ == "__main__":
    pantalone = Prodotto("jeans", 15, 35)
    pantalone = Abbigliamento(pantalone, "jeans", 40)
    computer = Prodotto("PC", 150, 350)
    
    print(f"Il profitto sul prodotto {pantalone.nome} è {pantalone.calcola_profitto()}.")
    
    myFabbrica = Fabbrica()
    
    myFabbrica.aggiungi_prodotto(pantalone, 90)
    
    myFabbrica.aggiungi_prodotto(computer, 200)
    
    myFabbrica.vendi_prodotto(pantalone, 10)
    
    print(myFabbrica.inventario)
    
    

        