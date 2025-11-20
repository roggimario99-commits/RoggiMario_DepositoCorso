class MetodoPagamento:
   def effettua_pagamento(self, importo):
       print(f"Effettuato pagamento di {importo}£")
       
       
class CartaDiCredito:
    def __init__(self, carta):
        self._carta = carta
    def effettua_pagamento(self, importo):
       print(f"Effettuato pagamento di {importo}£ con carta {self._carta}.")
       
       
class Paypal:
    def effettua_pagamento(self, importo):
       print(f"Effettuato pagamento di {importo}£ con Paypal.")
       
class BonificoBancario:
    def __init__(self, nome: str, numero: str):
        self._nome = nome
        self._numero = numero
    def effettua_pagamento(self, importo):
       print(f"Effettuato pagamento di {importo}£ con bonifico bancario dal conto {self._numero} intestato a {self._nome}.")
       
       
class GestorePagamenti:
    
    def effettua_pagamento(self, metodoPagamento):
        metodoPagamento.effettua_pagamento()

if __name__ == "__main__":
    
    metodoGen = MetodoPagamento()
    carta = CartaDiCredito("visa")
    paypal = Paypal()
    conto = BonificoBancario("Antonio Antoni", "0000000010")

    metodi = [metodoGen, carta, paypal, conto]

    for m in metodi:
        
        m.effettua_pagamento(100)

