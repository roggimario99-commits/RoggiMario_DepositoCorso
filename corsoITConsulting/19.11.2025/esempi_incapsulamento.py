class Computer:
    def __init__(self):
        self.__processore = "Intel i5"  #attributo privato
        
    def get_processore(self):
        return self.__processore
    
    def set_processore(self, processore):
        self.__processore = processore
        
    def __metodo_privato(self):
        return "Questo è un metodo privato"
    
        
pc = Computer()

print( pc.get_processore())
pc.set_processore("AMD Ryzen")
print( pc.get_processore())

#print(pc.__metodo_privato())  #ERRORE! 
#print(pc.__processore)

print(pc._Computer__metodo_privato())  #Funziona ma non fare mai! Rompe l'incapsulamento
print(pc._Computer__processore)        #Funziona ma non fare mai! Rompe l'incapsulamento

# Variabile globale

numero = 10


def funzione_esterna():

    # Variabile locale nella funzione esterna

    numero = 5

    print("Numero dentro funzione_esterna (locale):", numero)    


    def funzione_interna():

        # Utilizzo nonlocal per modificare la variabile locale della funzione esterna

        
        nonlocal numero

        numero = 3

        print("Numero dentro funzione_interna (nonlocal):", numero)

    
    print("Numero dentro funzione_esterna prima (locale):", numero) 
    funzione_interna()
    print("Numero dentro funzione_esterna dopo (locale):", numero) 

print("Numero nel main (globale):", numero)

funzione_esterna()

print("Numero nel main dopo chiamata (globale non cambiato):", numero)