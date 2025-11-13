# tipo int

x = 10; y = -10

print(x,y)

#tipo float

x = 0.5; y=-10/3

print(x,y)



#stringhe
s = "Python"

print(s[0])  #chiamo elementi
print(s[-1])

print(s + " course!") #prova composizione

#metodi stringhe

s = "Prova metodi!"

print(len(s)) #len() restituisce la lunghezza di una str
print(s.upper()) #metodo che converte in upper case
print(s.lower()) #metodo che converte in lower case
print(s.split("a")) #divide la sringa in una lista di stringhe usando come separatore il parametro
print(s.replace("metodi","riuscita")) # sostituisco una parte di stringa con un'altra

#caratteri (char)
c = "a"
print(c)

###Boleani
b1 = True; b2 = False #defenisco due var booleane 
print(b1,b2)

#prova operatori logici
x = 5; y = 10; z = 7 #prova operatori logici
print(x < y and y > z) # and (congiunzione)
print(x < y or y > z) # or   (disgiunzione)
print(not(x < y))     # not  (negazione)
print(not(x < y) and y > z) #cond più complessa

#operatori di confronto

print(x == y)
print(x == x)
print(x <= y and y != z)