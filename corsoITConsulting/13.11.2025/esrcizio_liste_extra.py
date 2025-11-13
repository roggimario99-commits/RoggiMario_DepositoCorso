print("Inserisci tre numeri (a1 ,a2 ,a3) e due operazioni fra addizione (+), sottrazione (-)")
a = [0,0,0] #lista con valori
op = ["",""]

a[0] = float(input("a1 = "))
op[0] = input("operazione: ") 
a[1] = float(input("a2 = "))
op[1] = input("operazione: ") 
a[2] = float(input("a3 = "))

match op:
    case ["+","+"]:
        res = a[0] + a[1] + a[2]
        print(a[0], " ", op[0], " ", a[1] , op[1], " ", a[2] ," = ", res)
        
    case ["+","-"]:
        res = a[0] + a[1] - a[2]
        print(a[0], " ", op[0], " ", a[1] , op[1], " ", a[2] ," = ", res)    
    
    case ["-","+"]:
        res = a[0] - a[1] + a[2]
        print(a[0], " ", op[0], " ", a[1] , op[1], " ", a[2] ," = ", res) 
        
    case ["-","-"]:
        res = a[0] - a[1] - a[2]
        print(a[0], " ", op[0], " ", a[1] , op[1], " ", a[2] ," = ", res) 
        
    case _ :
        
        print("Operazioni non valide!")         
         
         
         
        