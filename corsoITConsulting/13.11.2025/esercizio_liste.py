#check sull'età
age = int(input("Qual'è la tua età? ")) #prendo in input un età
if age < 18:  #controllo se l'utente e maggiorene e in base a questo printo un mes appropriato
    print("Mi spiace, non puoi vedere questo film!")
else:
    print("Puoi vedere il film!")  
    
#Implemento una calcolatrice    
print("Inserisci due numeri (a e b) ed un oprerazione fra +, -, * e /.") #chiedo all'utente che operazione vuole
#prendo tutte le var in input
a = float(input("a = "))
operazione = input("operazione: ") 
b = float(input("b = "))

#In base all'operazione printo il risultato corretto
match operazione:
    case "+":
        res = a + b
        print(a, " ", operazione, " ", b , " = ", res)
        
    case "-":
        res = a - b
        print(a, " ", operazione, " ", b , " = ", res)  
        
    case "*":
        res = a * b
        print(a, " ", operazione, " ", b , " = ", res)      
        
    case "/":
        if b != 0:  #controllo che il denominatore non sia nullo
            res = a / b
            print(a, " ", operazione, " ", b , " = ", res)  
        else: 
            print("Non è possibile dividere per zero!")  #mess errore    
        
    case _ :
        
        print("Operazione non riconosciuta!")    #mess errore
    