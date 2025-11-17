studente = {"nome" : "Alice", "età": 20, "sesso": "Femmina"} #dizionario

print(studente["età"])

studente["città"] = "Roma"
print(studente)


### metodi ###

print(studente.keys())     #keys
print(studente.values())   #values
print(studente.items())    #tuple di key e value

print(studente.get("nome"))   #prende il value associato ad una key e non da errore se non esiste
print(studente.get("ciao"))

### for su dizionario

myDict = {"1" : "", "2": "", "3": ""}

myDict["1"] = 99
myDict["2"] = "stringa"
myDict["3"] = True
    
for k, v in myDict.items():
    print(f"{k}: {v}")