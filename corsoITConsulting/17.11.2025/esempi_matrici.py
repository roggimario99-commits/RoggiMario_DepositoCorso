matrice = [       #definisco una matrice
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrice[1])       #print seconda riga
print(matrice[1][2])       #print elemento seconda riga, terza colonna

for riga in matrice:     #print elementi matrice
    for elemento in riga:
        print(elemento)
        
## creazione matrice trasposta (righe scambiate con le colonne) 
       
matriceTrasp = [
    [riga[i] for riga in matrice] 
                
                for i in range(len(matrice))  ] 
print(matriceTrasp)