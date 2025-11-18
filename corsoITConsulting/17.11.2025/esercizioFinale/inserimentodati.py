def inserimento_dati_vendita():
    while True:
        testo = input("Inserisci gli importi di vendita separati da spazio: ")

        # Se l'utente non inserisce niente
        if testo.strip() == "":
            print("Non sono stati inseriti dati. Riprova.")
            continue

        parti = testo.split()
        vendite = []

        try:
            for p in parti:
                numero = int(p)
                vendite.append(numero)
            # se tutto va bene si esce dal while
            break
        except ValueError:
            print("Errore: hai inserito qualcosa che non è un numero.")
            print("Riprova inserendo solo numeri interi, separati da spazi.\n")
    return vendite