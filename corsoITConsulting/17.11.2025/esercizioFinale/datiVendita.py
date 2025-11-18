class GestioneVendite:
    def __init__(self, vendite):
        self.vendite = vendite
        self.tot = sum(vendite)
        self.mean = sum(vendite) / len(vendite)
        
    def stats(self):
        
        print(f"Il tot delle vendite è: {self.tot} e la media è {self.mean}.")
        
    def greater_then_mean(self):
        vendite_sopra_media = []
        for val in self.vendite:
            if val > self.mean:
                vendite_sopra_media.append(val)
                
        if len(self.vendite) == 0:
                print("Non ci sono vendite sopra la media! Tutti i valori erano uguali")
        else:
                print("vendite sopra la media: ", vendite_sopra_media)  
                
        return vendite_sopra_media
            
            
        
        
