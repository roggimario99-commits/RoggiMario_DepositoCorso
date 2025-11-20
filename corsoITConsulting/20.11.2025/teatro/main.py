# =======================
# CLASSE BASE: POSTO
# =======================

class Posto:
    def __init__(self, numero: int, fila: str):
        self._numero = numero
        self._fila = fila
        self._occupato = False

    # ------------ GETTER ------------
    @property
    def numero(self):
        return self._numero

    @property
    def fila(self):
        return self._fila

    @property
    def occupato(self):
        return self._occupato

    # ------------ METODI BASE ------------
    def prenota(self):
        if self._occupato:
            print(f"Il posto {self._fila}{self._numero} è già occupato.")
        else:
            self._occupato = True
            print(f"Posto {self._fila}{self._numero} prenotato con successo.")

    def libera(self):
        if not self._occupato:
            print(f"Il posto {self._fila}{self._numero} non era prenotato.")
        else:
            self._occupato = False
            print(f"Posto {self._fila}{self._numero} ora è libero.")



# ======================================
# CLASSE DERIVATA: POSTO VIP
# ======================================

class PostoVIP(Posto):
    def __init__(self, numero: int, fila: str, servizi_extra: list[str]):
        super().__init__(numero, fila)
        self.servizi_extra = servizi_extra

    def prenota(self):
        if self._occupato:
            print(f"Il posto VIP {self._fila}{self._numero} è già occupato!")
        else:
            self._occupato = True
            print(f"Posto VIP {self._fila}{self._numero} prenotato!")
            print("   Servizi extra attivati:")
            for servizio in self.servizi_extra:
                print(f"   - {servizio}")



# ======================================
# CLASSE DERIVATA: POSTO STANDARD
# ======================================

class PostoStandard(Posto):
    def __init__(self, numero: int, fila: str, costo: float):
        super().__init__(numero, fila)
        self.costo = costo

    def prenota(self):
        if self._occupato:
            print(f"Il posto Standard {self._fila}{self._numero} è già occupato.")
        else:
            self._occupato = True
            print(f"Posto Standard {self._fila}{self._numero} prenotato.")
            print(f"Costo prenotazione: {self.costo:.2f}€")



# =======================
# CLASSE TEATRO
# =======================

class Teatro:
    def __init__(self):
        self._posti = []

    # aggiunge un posto alla lista
    def aggiungi_posto(self, posto: Posto):
        self._posti.append(posto)

    # prenota cercando numero e fila
    def prenota_posto(self, numero: int, fila: str):
        for posto in self._posti:
            if posto.numero == numero and posto.fila == fila:
                posto.prenota()
                return
        print(f"Nessun posto trovato con identificativo {fila}{numero}")

    # stampa solo i posti occupati
    def stampa_posti_occupati(self):
        print("\n=== POSTI OCCUPATI ===")
        trovati = False
        for posto in self._posti:
            if posto.occupato:
                print(f"- {posto.fila}{posto.numero}")
                trovati = True
        if not trovati:
            print("Nessun posto occupato.")



# =======================
# ESEMPIO DI UTILIZZO
# =======================

if __name__ == "__main__":
    teatro = Teatro()


    
    # Creiamo alcuni posti
    p1 = PostoStandard(1, "A", 12.5)
    p2 = PostoStandard(2, "A", 12.5)
    vip1 = PostoVIP(1, "B", ["Accesso Lounge", "Bevanda Inclusa"])
    print()
    
    # Aggiungiamoli al teatro
    teatro.aggiungi_posto(p1)
    teatro.aggiungi_posto(p2)
    teatro.aggiungi_posto(vip1)
    print()
    
    # Prenotazioni
    teatro.prenota_posto(1, "A")
    teatro.prenota_posto(1, "B")
    teatro.prenota_posto(1, "B")  # Tentativo su posto occupato

    teatro.stampa_posti_occupati()