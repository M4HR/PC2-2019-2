import random
lin = ""
while True:
    n = int(input("Ingrese tamaño de la matriz: "))
    res = 0
    if n < 2 or n > 5:
        while True:
            n = int(input("Ingrese un valor entre 2 y 5: "))
            
            if n > 1 and n < 6:
                res = 1
                break
    if res == 1:
        break
    if n > 1 and n < 6:
        break
matriz = []
for i in range(n):
    ai = []
    matriz.append(ai)

datos = n * n
#print(matriz)
for i in range(n): 
    for j in range(n):
        matriz[i].append(random.randint(0,100)




for i in range(n)
    for j in range(n)
        a =  matriz[i][j]
        lin = lin + " " + str(a)
    lin = lin\n    
print(matriz)
