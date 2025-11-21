class ContoBancario:
    def __init__(self):
        self.__titolare = ""    
        self.__saldo = 0
        
    def get_titolare(self):
        return self.__titolare
    
    def set_titolare(self, titolare):
        if type(titolare) == str and titolare != "":
            self.__titolare = titolare
            return True
        else:
            print("Nome inserito non valido.")
            return False
        
    
    