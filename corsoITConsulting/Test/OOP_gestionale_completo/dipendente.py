from abc import ABC, abstractmethod

class Dipendente(ABC):
    """
    Classe base astratta che rappresenta un dipendente.
    Questa classe non può essere istanziata direttamente.
    """

    def __init__(self, nome: str, eta: int):
        # Usa nomi consistenti: 'nome' invece di 'targa'
        self._nome = nome
        self._eta = eta
        self.orario_lavoro = 8 * 60  # orario di lavoro in minuti (8 ore)
        self.ora_acesso = None
        self.minuti_accesso = None
        self.accesi_fuori_orario = 0

    @abstractmethod
    def calcola_stipendio(self):
        """
        Metodo astratto: ogni classe derivata deve implementarlo.
        """
        pass


    def ora_minuti(ora: int, minuti: int = None) -> int:
        """
        Metodo statico per convertire ora e minuti in minuti totali.
        """
        if minuti == None:
            minuti = 0
        return ora * 60 + minuti
        
    def login(self, ora: int, minuti: int):
        """
        Metodo comune per simulare il login del dipendente.
        """
        if  self.ora_minuti(8) <= self.ora_minuti(ora, minuti) <= self.ora_minuti(10): #orario di ingresso consentito
            print(f"{self._nome} ha effettuato il login alle: {ora}:{minuti}")
            self.ora_acesso = ora
            self.minuti_accesso = minuti
            
            self.accesi_fuori_orario += 1 # conta accessi fuori orario
        else: # fuori orario
            print(f"{self._nome} ha provato ad effettuare il login fuori orario alle: {ora}:{minuti}")
            
    def logout(self, ora: int, minuti: int):
        """
        Metodo comune per simulare il logou del dipendente.
        """
        if self.ora_minuti(ora, minuti) - self.ora_minuti(self.ora_acesso, self.minuti_accesso) > self.orario_lavoro: #orario di ingresso consentito
            print(f"{self._nome} ha effettuato il logout alle: {ora}:{minuti}")
        else: # fuori orario
            print(f"{self._nome} ha provato ad effettuare il logout alle: {ora}:{minuti}, ma era troppop presto")
            
            


class DipendenteJunior(Dipendente):
    """
    Dipendente di livello junior con stipendio fisso.
    """

    def __init__(self, nome: str, eta: int):
        super().__init__(nome, eta)  # richiama costruttore della classe base
        self._stipendio_base = 2000

    def calcola_stipendio(self):
        return self._stipendio_base


class DipendenteSenior(Dipendente):
    """
    Dipendente senior, guadagna bonus in base agli anni di servizio.
    """

    def __init__(self, nome: str, eta: int, anni_servizio: int = 3):
        super().__init__(nome, eta)
        self._stipendio_base = 2000
        self._anni_servizio = anni_servizio

    def calcola_stipendio(self):
        return self._stipendio_base + 250 * self._anni_servizio


class Dirigente(Dipendente):
    """
    Il dirigente ha le stesse logiche di un senior con stipendio base diverso,
    ma potrai differenziarlo con privilegi extra.
    """

    def __init__(self, nome: str, eta: int, anni_servizio: int = 3):
        super().__init__(nome, eta)
        self._stipendio_base = 3500
        self._anni_servizio = anni_servizio

    def calcola_stipendio(self):
        return self._stipendio_base + 250 * self._anni_servizio
    
    #sovrascittura metodi login e logout
    def login(self, ora: int, minuti: int):
        """Il dirigente non ha orari fissi in cui fare login, in questa azienda può fare come vuole!"""
        print(f"{self._nome} ha effettuato il login alle: {ora}:{minuti}")

            
    def logout(self, ora: int, minuti: int):
        """Il dirigente non ha orari fissi in cui fare logout, in questa azienda può fare come vuole!"""
        print(f"{self._nome} ha effettuato il logout alle: {ora}:{minuti}")
