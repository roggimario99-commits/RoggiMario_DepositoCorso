
# Definizione di un messaggio (puoi cambiare i valori per testare)
messaggio = {
    "tipo": "login",
    "utente": "mario",
    "password": "12345"
}

# Pattern matching
match messaggio:
    case {"tipo": "login", "utente": u, "password": p}:
        print(f"Login di {u}")
    case {"tipo": "logout", "utente": u}:
        print(f"Logout di {u}")
    case _:
        print("Messaggio sconosciuto")