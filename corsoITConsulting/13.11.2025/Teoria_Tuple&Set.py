### Tuple
myTuple = (8989, "ciao!", 0.9, "c", True) #def con parentesi tonde
print(myTuple[3])
print(myTuple)

punto = 3, 4
x, y = punto
print(x,y)

## Insiemi
set1 = set([1,2,3])
set2 = {1,2,3,3,4,8,9,8}
print(set1,set2)

#operazioni insiemi
setA = {1,2,3,4,5,6}
setB = {4,5,6,7,8,9,0}
print("\n\n",setA,setB)
print(setA.union(setB))        #unione
print(setA.intersection(setB)) #intersezione
print(setA.difference(setB))   #differenza
print(setA.symmetric_difference(setB))  #differenza simmetrica (unione - intersezione)

#metodi
setA.add(10)
print(setA)
setA.remove(2)
print(setA)
setA.discard(2)
print(setA)

print(len(setA))

setB=setA.copy()

setB.add(11)
print(setA,setB)