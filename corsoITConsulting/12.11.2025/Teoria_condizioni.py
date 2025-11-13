#### CONDIZIONI


n = int(input("Inserisci un intero: ")) #richiedo un intero all'utente

#Le seguenti cond. printano se il numero è neg, pos o nullo.

if n > 0:                              #if (eseguo il com se è vera la cond)
    print("Il numero è positivo.")
elif n == 0:                           #elif (eseguo il com se sono false le cond. precedenti ma vera la cond di ora)
    print("Il numero è nullo.") 
else:                                  #else (eseguo il com se sono false tutte le cond. precedenti)
    print("Il numero è negativo.")       
    
# match    

#Richiedi input
contr = input("Inserisci 'i' se vuoi inserire un nuovo nome, 'm' se vuoi modificarlo e 'c' se vuoi cancellarlo. \nComando: ")    

#definizione variabili
name = "Mario"
newName = ""

match contr:
   case "i":
        newName = input("inserisci nome: ")
        print("Inserito il nome ", newName)
   case "m":
        name = input("inserisci nome: ")
        print("Modificato il nome con: ", name)
   case "c":
        name = ""
        print("Nome cancellato!")    
   case _:   
        print("ERRORE! Comando non valido.")