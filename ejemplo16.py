#16 ejercicio
exaMat=float(input("ingrese la nota del examen de matematicas:"))
tarMat1=float(input("ingrese la nota de la primera tarea:"))
tarMat2=float(input("ingrese la nota de la segunda tarea:"))
tarMat3=float(input("ingrese la nota de la tercera tarea:"))
Pmatem=0.90*exaMat+0.10*(tarMat1+tarMat2+tarMat3)/3
print(f"el porcentaje de la nota de matematicas es:{Pmatem:.2f}")

exaFis=float(input("ingrese la nota del examen de fisica:"))
tarFis1=float(input("ingrese la nota de la primera tarea de fisica:"))
tarFis2=float(input("ingrese la nota de la segunda tarea de fisica"))
promFis=0.80*exaFis+0.20*(tarFis1+tarFis2)/2
print(f"el promrdio de fisica es:{promFis:.2f}")

exaQuim=float(input("ingrese la nota del examen de quimica:"))
tarQui1=float(input("ingrese la nota de la primera tarea de quimica:"))
tarQui2=float(input("iingrse la nota de la segunda tarea de quimica"))
tarQui3=float(input("ingrese la nota de la tercera tarea de quimica:"))
promQui=0.85*exaQuim+0.15*(tarQui1+tarQui2+tarQui3)/3
print(f"el porcentaje de quimica es:{promQui:.2f}")

promGen=(Pmatem+promFis+promQui)/3
print(f"el promedio general de las tres materias es:{promGen:.2f} ")