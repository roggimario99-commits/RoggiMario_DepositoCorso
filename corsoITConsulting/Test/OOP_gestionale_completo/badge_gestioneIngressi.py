from dipendente import *

class Badge:
    def __init__(self, id_badge: str, owner: Dipendente):
        self.id_badge = id_badge
        self.owner = owner
        self.attivo = True
        
class GestoreAccessi:
    def __init__(self):
        self.log_accessi = []
        
    def controllo_badge(self, badge: Badge):
        if badge.owner.accesi_fuori_orario > 6:
            badge.attivo = False
            print(f"Badge {badge.id_badge} disattivato per troppi accessi fuori orario.")

    def registra_ingresso(self, badge: Badge):
        if not badge.attivo:
            print("Accesso negato: badge disattivato")
            return
        
        badge.owner.login()
        self.log_accessi.append((badge.id_badge, badge.owner._nome))