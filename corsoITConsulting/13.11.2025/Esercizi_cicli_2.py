""" #
num = int(input("Inserisci un numero: "))
if num % 2:
        print("E' pari!")
else:
        print("E' dispari!")
 
#conto alla rovescia con possibilità di ripetere a scelta dell'utente  
contr = True        
while(contr):
    num = int(input("Inserisci un numero: "))
    for n in range(num, -1, -1): 
        print(n) 
        
    ripet = input("Vuoi ripetere? (s/n): ")  #chiedo all'utente se vuole ripetere
    if ripet == "n":
        contr = False """
          
         
#prendo in input una lista e printo i quadrati
numeri = []
len = int(input("Dimmi quanti numeri vuoi inserire: ")   )          
for i in range(len):
    numeri.append( float(input("Inserisci valore: ")) )

numeri.sort()   
 
for n in numeri:
    print(n**2)    
    
#massimo con ciclo for
max=numeri[0]
for n in numeri:
    if n > max:  #controllo se il nuovo elemento è maggiore del max precedente
        max = n   
print("max = ", max)        
numeri = []
numeri_copia =numeri.copy()


#len della lista
len = 0
while numeri_copia != []:
    numeri_copia.pop()
    len += 1
print("len = ", len)    