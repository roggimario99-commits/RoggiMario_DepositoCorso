#Liste
myList = [1, 2 , "pizza" ,3, 4, 99.99, 5, True]
print(myList[0])
print(myList[-2])
print(myList[1:6])

#metodi liste
numeri = [0,1,2,3,4,5,6]
print(len(numeri))
numeri.append(1)
print(numeri)
numeri.insert(3,"margherita")
print(numeri)
numeri.remove("margherita")
print(numeri)
numeri.sort(1)
print(numeri)