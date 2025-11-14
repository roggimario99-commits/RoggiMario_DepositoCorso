import random
 #gioco numero
def indovinaNum():
    numVinc = random.randint(1,100)  #genero u intero fra 1 e 100
    guess = 0
    while guess != numVinc:
        
        while True:
           guess = int(input("Inserisci un intero fra 1 e 100: "))  #prendo la guess dell'utente e ripeto finchè non è nell'intervallo corretto
           if 0 < guess <= 100:
               break
           
        if guess < numVinc:         #do informazioni all'utente
            print("Troppo basso!")
        elif guess > numVinc:
            print("Troppo alto!")
        else:
            print("Hai vinto!")
 
 
 #fibbonacci   
def fibobonacci(N, a = 1, b = 1):  
    n_in_seq = [a,b] #definisco una lista con i primi due valori della sequenza

    while n_in_seq[-1] + n_in_seq[-2] < N:
        n_in_seq.append(n_in_seq[-1] + n_in_seq[-2]) #aggiungo il numero alla sequenza come somma dei due precedenti                                    #aumento il contatore

        
    print(f"Sequenza di fibbonacci per num minori di {N}:")
    for n in n_in_seq:
        print(n, end = " ")                         #printo la sequenza
        
    return n_in_seq                                 #returno la sequenza
        


memory = []       
while(True):
    N = int(input("Inserisci un intero : "))
    
    memory.append( fibobonacci(N) )
    
    rep = input("\nVuoi ripetere? (si/no): ")
    if rep == "no":
        break
    elif rep == "si":
        continue
    else:
        print("ERRORE! Risposta non valida.")
        
        
print(memory)        



#struttura ripetizione base
""" while(True):
    pass
        
    rep = input("Vuoi ripetere? (si/no): ")
    if rep == "no":
        break
    elif rep == "si":
        continue
    else:
        print("ERRORE! Risposta non valida.") """