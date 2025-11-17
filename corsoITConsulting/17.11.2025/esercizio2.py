class Libro:
    def __init__(self, titolo, autore, pagine):  #metodo costruttore
        self.titolo = titolo
        self.autore = autore
        self.pagine = int(pagine)
        
    def __str__(self):     #metodo speciale stampa
        return f"Il libro {self.titolo} è stato scritto da {self.autore} e ha {self.pagine} pagine."
  
if __name__ == "__main__":
    libro1 = Libro("Notte","Pino Pini",100.7)  #definisco un'istanza della classe Libro
    print(libro1)                              #printo l'istanza libro1
        