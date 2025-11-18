from datiVendita import GestioneVendite
from inserimentodati import inserimento_dati_vendita


vendite = inserimento_dati_vendita() #prendo in input i dati di vendita
print("serie storica dati vendite:", vendite, "\n")

gestione = GestioneVendite(vendite) #creo una classe per la gestione dei dati di vendita


gestione.stats()  #calcolo e printo somma e media

gestione.greater_then_mean() #faccio una lista con i valori mmaggiori della media e la stampo
