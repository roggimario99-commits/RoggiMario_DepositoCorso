#Es. 1
# n = int( input("inserisci un intero") ) #inserisci numero

# # controllo di dove si trova il num rispetto a 10 e -10.
# if n < -10:
#     print("Il numero è strettamnete minore di -10.")
# elif n <= 10:
#     print("Il numero è compreso fra -10 e 10 estremi inclusi.")
# else:
#      print("Il numero è strettamente maggiore di 10.")     
     
# #Es. 2
# #Richiedi input
# contr = input("Inserisci 'i' se vuoi inserire un nuovo nome, 'm' se vuoi modificarlo e 'c' se vuoi cancellarlo. \nComando: ")    

# #definizione variabili
# name = "Mario"
# newName = ""


# if contr == "i":
#         newName = input("inserisci nome: ")
#         print("Inserito il nome ", newName)
# elif contr == "m":
#         name = input("inserisci nome: ")
#         print("Modificato il nome con: ", name)
# elif contr == "c":
#         name = ""
#         print("Nome cancellato!")    
# else:    
#         print("ERRORE! Comando non valido.")
        
#Es.3
credAccesso = ["admin", "12345"] 
credInserite = []
credInserite.append(input("Inserisci nome utente: "))
credInserite.append(input("Inserisci nome password: "))

match credInserite:
    case  [adm , pas]  if [adm , pas] == credAccesso:
        print("Accesso eseguito")
        match input("vuoi cambiare pasword? si o no"):
            case "si":
                credAccesso[0] = input("Inserisci nuova password: ")
                print("Password modificata!")    
            case "no":
                print("manteniamo la password!")  
            case _ :
                print("Comando non valido!")    
        
        match input("devi inserire una domanda segreta:\n1) Colore preferito? \n2) Animale preferito\nVuoi 1 o 2:  "):
            case "1":
                print("Domanda inserita!")    
            case "2":
                print("Domanda inserita!")  
            case _ :
                print("Comando non valido!")  
                         
    case _:
        print("Credenziali ERRATE!")    
    