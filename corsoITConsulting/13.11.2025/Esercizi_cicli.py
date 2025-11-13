""" n = int(input("Inserisci numero: "))
for i in range(n):
    print(n-i) 
    
for i in range(n, -1, -1):
        print(i)  
         
#primi N numeri pari
pari = [] #Lista che conterra i pari
N = 5     #Num massimo, controlleremo tutti i val minori di N

for i in range(2,N,2):
    pari.append(i)   #Salvo il valore
    print(i, "è pari!")         #Printo il valore 

print(pari)          #Printo la lista""" 


#primi N numeri primi
primi = [] #Lista che conterra i primi
N = 10    #Num massimo, controlleremo tutti i val minori di N

def is_prime(num):
    if num <=1:
        return False
    
    if num == 2:
        return True
    
    for j in range(2,int(num**0.5) + 1):
         if num % j == 0:
            return False
            break
        
    return True

for i in range(N):
       if is_prime(i):
         primi.append(i)   #Salvo il valore
         print(i, "è primo!")         #Printo il valore 

print(primi)          #Printo la lista  
    
