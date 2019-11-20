nombre =[]
sexo = []
edad = []
datos = [nombre, sexo, edad] 
print("***Registro al curso de Natacion***")
print("Solo se acepta un maximo de 5 personas")
num = 0
hom = 0
muj = 0
while len(nombre) < 5:
     num += 1
     print(f"Numero de Inscripcion: {num}")
     n = input("Ingrese Nombre: ")
     nombre.append(n)
     while True:
         e = int(input("Ingrese edad (Entre 5 y 17): "))
         if e >= 5 and e <= 17:
             edad.append(e)
             break
     while True:
         s = input("Ingrese Sexo (Hombre/Mujer): ")
         if s == "hombre" or s == "Hombre" or s == "Mujer" or s=="mujer":
             sexo.append(s)
             break
     if s == "hombre" or s == "Hombre":
         hom +=1
     elif s == "mujer" or s == "Mujer":
         muj += 1 
     op = input("Desea seguir ingresando inscripciones (S/N): ")
     if op == "n" or op =="N":
         break
if (len(nombre)>0):
    # Imprimir Inscritos
    print("***Inscritos***")
    for i in range(len(nombre)):
        print(
                f"{i+1} Nombre: {datos[0][i]}  Sexo: {datos[1][i]} Edad: {datos[2][i]}"
        )
    # Cantidad de hombre y mujeres
    print(
        "Hombres: "+ str(hom)+
        " Mujeres: "+ str(muj)
    )
    # Promedio de edad
    suma = 0
    promediocon = 0
    for i in range(len(edad)):
        suma = suma + edad[i]
        promediocon += 1
    print(
        f"El Promedio de edades es: {suma/promediocon}"
    )



