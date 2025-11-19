class ContoBancario:
    def __init__(self):
        self.__titolare = ""    
        self.__saldo = 0
        
    def deposita(self, importo):
        if importo > 0:
            self.__saldo += importo
            
            return True

        else:
            print("Importo inserito non valido! ")
            return False
            
    def preleva(self, importo):
        if importo < self.__saldo:
            self.__saldo -= importo
            return True
        else:
            print("Importo inserito non è' disponibile nel conto!")
            return False
            
    def visualizza_saldo(self):
        print(f"Il saldo corrente è {self.__saldo}$.")
        
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, titolare):
        if type(titolare) == str and titolare != "":
            self.__titolare = titolare
            return True
        else:
            print("Nome inserito non valido.")
            return False
        
    
    