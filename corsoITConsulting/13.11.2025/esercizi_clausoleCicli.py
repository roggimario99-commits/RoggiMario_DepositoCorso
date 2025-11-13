#Esercizio 1
while(True):
    act = input("Vuoi inserire un numero o una stringa? (n/s): ")
    match act:
        case "n":
            num = int(input("Inserisci il numero:"))
            if num % 2 == 0:
                print("Pari!")
            else:
                print("dispari!")
                
        case "s":
            str = input("Inserisci la stringa:")
            if len(str) % 2 == 0:
                print("Pari!")
            else:
                print("dispari!")
        case _:
            print("ERRORE! Risposta non valida.") 
        
    rep = input("Vuoi ripetere? (si/no): ")
    if rep == "no":
        break
    elif rep == "si":
        continue
    else:
        print("ERRORE! Risposta non valida.")