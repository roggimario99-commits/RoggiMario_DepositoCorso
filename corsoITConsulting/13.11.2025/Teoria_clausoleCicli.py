# ""break"" blocca il ciclo (rompe il loop)
# ""continue"" salta un giro (non rompe il loop)

numeri = [0,1,2,3,4,5,6,7]
for n in numeri:
    print(n)
    if n == 3:
        continue   #salta la terza iterazione (dopo il continue)
    if n == 5:
        break      #il ciclo si rompe all'inizio della sesta iterazione
    
    print(n)
    
# ""pass"" è un place holder!! non fa nulla

prova = 8787

if prova == 8787:
    print("Work in progress!!")
    pass      #non fa nulla, ma così non da errore
     
print({*range(6)})