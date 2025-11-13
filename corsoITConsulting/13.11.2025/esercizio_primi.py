#funzione numero primo
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

while(True):
        print("Inserisci un intervallo di interi positivi!")
        a = int(input("Inserisci l'inizio dell'intervallo: "))
        b = int(input("Inserisci la fine dell'intervallo: "))

        if a > b:
            a, b = b, a

        prime = []
        not_a_prime = []
        for i in range(a, b + 1):
                if is_prime(i):
                    prime.append(i)   #Salvo il valore
                    print(i)         #Printo il valore se è primo
                else:
                    not_a_prime.append(i)
                    
        print(f"Numeri primi: {prime}")
        print(f"Numeri non primi: {not_a_prime}")

        rep = input("Vuoi ripetere? (si/no): ")
        if rep == "no":
            break
        if rep == "si":
            continue
        else:
            print("Errore! Risposta non valida.")
              