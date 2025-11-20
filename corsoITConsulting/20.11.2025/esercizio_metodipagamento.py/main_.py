from metodo_pagamento import *
import random

allPaymentMethods = {}

while True:
    print("\n### Registrazione nuovo utente ###")
    nome = input("Iserisci nome:")
    while True:
        
        print("### menu ###")
        print("1. Metodo generico")
        print("2. Paypal")
        print("3. Conto")
        print("4. Esci")
        
        metScelto = input("Che metodo vuoi?")
        
        match metScelto:
            case "1":
                allPaymentMethods[nome] = MetodoPagamento()
                print("metodo inserito!")
                
            case "2":
                allPaymentMethods[nome] = Paypal()    
                print("metodo inserito!")
                
            case "3":
                numero = input("Inserisci numero conto: ")
                allPaymentMethods[nome] = BonificoBancario(nome, numero)
                print("metodo inserito!")
                
            case "4":
                break
            case _:
                print("Scelta non valida!")
                
        while True:
            resp = input("Vuoi inserire nuovo metodo di pagamento: ").strip().lower()
            if resp in ("si", "no"):   #ripete se la risposta non è valida
                break
            print("Risposta non valida. Scrivi 'si' o 'no'.")

        if resp == "no":
            break      
                
    while True:
        scelta = input("Vuoi inserire un nuovo utente? (si/no): ").strip().lower()
        if scelta in ("si", "no"):   #ripete se la risposta non è valida
            break
        print("Risposta non valida. Scrivi 'si' o 'no'.")

    if scelta == "no":
        break            
    
    
for k, v in allPaymentMethods.items():
    
    print(f"Utente: {k}")
    if len(v) == 1:
        (v).effettua_pagamento(100)
    else:   
        random.choice(v).effettua_pagamento(100)