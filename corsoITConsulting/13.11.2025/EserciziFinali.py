#Es.1 
sum = 0  #inizializzo la var sum a 0
while True:
  num = int(input("Inserisci il numero: ")) #numero in input
  sum += num    #sommo il nuovo numero a sum
  if num == 0:   #quando l'utente inserisce 0 interrompo il ciclo
      break
  
print(f"La somma è {sum}")  #printo la somma

#Es.2
str = input("Inserisci una parola:") #parola in input
for l in str:
    print(l)  #printo la lettera
    
#Es.3
#prendo in input Nmax e step dall'utente
Nmax = int(input("Inserisci il numero massimo: "))   
step = int(input("Inserisci lo step: "))  

for n in range(0,Nmax,step):
    print(n)       #printo il numero