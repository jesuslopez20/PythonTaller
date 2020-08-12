#4 EJERCICIO

c1=float(input("ingrese la primera calificacion:"))
c2=float(input("infrese la segunda calificacion:"))
c3=float(input("ingrese la tercera calificacion:"))
ef=float(input("ingrese la calificacion del examen final:"))
tf=float(input("ingrese calificacion del trabajo final:"))
promedio=(c1+c2+c3)/3
ppar=promedio*0.55
pef=ef*0.30
ptf=tf*0.15
cf=ppar+pef+ptf
print(f"la calificacion final es:{cf:.2f}")

