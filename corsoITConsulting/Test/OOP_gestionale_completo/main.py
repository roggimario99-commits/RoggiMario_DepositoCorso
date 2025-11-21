from dipendente import DipendenteJunior, DipendenteSenior, Dirigente
from badge_gestioneIngressi import Badge, GestoreAccessi

def main(): ## creato con aiuto chat gtp per poter testare tutto
    # ------------------------------------------------------------
    # CREAZIONE DIPENDENTI
    # ------------------------------------------------------------
    d1 = DipendenteJunior("Marco", 25)
    d2 = DipendenteSenior("Luisa", 40, anni_servizio=5)
    d3 = Dirigente("Gianni", 55, anni_servizio=10)

    # ------------------------------------------------------------
    # CREAZIONE BADGE
    # ------------------------------------------------------------
    b1 = Badge("B001", d1)
    b2 = Badge("B002", d2)
    b3 = Badge("B003", d3)

    badges = {
        "B001": b1,
        "B002": b2,
        "B003": b3
    }

    # ------------------------------------------------------------
    # GESTORE ACCESSI
    # ------------------------------------------------------------
    gestore = GestoreAccessi()

    # ------------------------------------------------------------
    # MENU SEMPLICE
    # ------------------------------------------------------------
    while True:
        print("\n=== MENU GESTIONALE ACCESSI ===")
        print("1) Mostra dipendenti")
        print("2) Login con badge")
        print("3) Logout con badge")
        print("4) Controlla badge")
        print("0) Esci")

        scelta = input("Scelta: ")

        if scelta == "1":
            print("\n--- DIPENDENTI ---")
            for b in badges.values():
                print(f"{b.id_badge} -> {b.owner._nome}, attivo: {b.attivo}")

        elif scelta == "2":
            id_badge = input("Inserisci ID badge: ")
            if id_badge not in badges:
                print("Badge inesistente")
                continue

            ora = int(input("Ora login: "))
            minuti = int(input("Minuti login: "))
            
            # login dipendente
            badges[id_badge].owner.login(ora, minuti)
            gestore.controllo_badge(badges[id_badge])
            gestore.log_accessi.append((id_badge, f"login {ora}:{minuti}"))

        elif scelta == "3":
            id_badge = input("Inserisci ID badge: ")
            if id_badge not in badges:
                print("Badge inesistente")
                continue

            ora = int(input("Ora logout: "))
            minuti = int(input("Minuti logout: "))

            badges[id_badge].owner.logout(ora, minuti)
            gestore.log_accessi.append((id_badge, f"logout {ora}:{minuti}"))

        elif scelta == "4":
            id_badge = input("Badge da controllare: ")
            if id_badge not in badges:
                print("Badge inesistente")
                continue

            gestore.controllo_badge(badges[id_badge])


        elif scelta == "0":
            print("Chiusura programma...")
            break

        else:
            print("Scelta non valida.")


if __name__ == "__main__":
    main()