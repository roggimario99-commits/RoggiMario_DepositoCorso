from classi_astr_concrete import *
from gestore_flotta import GestoreFlotta

c = Camion(targa="AB123CD", peso_massimo=10000, carico_attuale= 10000, numero_assi=4)
f = Furgone(targa="EF456GH", peso_massimo=3000, carico_attuale= 1500, alimentazione="elettrico")
m = Motocarro(targa="IJ789KL", peso_massimo=2000, carico_attuale= 500, anni_servizio=5)

veicoli = [c, f, m]

gestore = GestoreFlotta()

for veicolo in veicoli:
    gestore.aggiungi_veicolo(veicolo)
    
print(f"Costo Totale Manutenzione Flotta: {gestore.costo_totale_manutenzione()}")
    
gestore.stampa_veicoli()

print("Rimuovo il furgone EF456GH dalla flotta.")

gestore.rimuovi_veicolo("EF456GH")

print(f"Costo Totale Manutenzione Flotta: {gestore.costo_totale_manutenzione()}")
    
gestore.stampa_veicoli()



        
        


