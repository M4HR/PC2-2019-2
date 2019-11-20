def cortarletra(texto, letra):
    cuenta = 0
    for i in texto:
        if i == letra:
            cuenta+=1 
    return cuenta
A = cortarletra("hola mundo", "o")
B = cortarletra("1231133421", "1")

print(A)
print(B)
