""" age = int(input("Qual'è la tua età? "))
if age < 18:
    print("Mi spiace, non puoi vedere questo film!")
else:
    print("Puoi vedere il film!")   """  
    
    
print("Inserisci due numeri (a e b) ed un oprerazione fra +, -, * e /.")
a = float(input("a = "))
operazione = input("operazione: ") 
b = float(input("b = "))

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
        if b != 0:
            res = a / b
            print(a, " ", operazione, " ", b , " = ", res)  
        else: 
            print("Non è possibile dividere per zero!")      
        
    case _ :
        
        print("Operazione non riconosciuta!")    
    