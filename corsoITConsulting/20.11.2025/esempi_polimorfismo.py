#overloading simulato

class Stampa:

    def mostra(self, a=None, b=None, c=None):

        if a is not None and b is not None and c is not None:

            print(a + b + c)
        
        elif a is not None and b is not None:

            print(a + b)

        elif a is not None:

            print(a)

        else:

            print("Niente da mostrare")
            
            
s = Stampa()
s.mostra(2,8,4)
s.mostra(3,9)
s.mostra(6)
s.mostra()


#### Esempio di duck typing
### polimorfismo

class Cane:

    def parla(self):

        return "Bau!"


class Gatto:

    def parla(self):

        return "Miao!"


def fai_parlare(animale):

    # Non importa di che tipo sia l'animale,

    print(animale.parla())


cane = Cane()

gatto = Gatto()


fai_parlare(cane)  # Output: Bau!

fai_parlare(gatto)  # Output: Miao!
