#2 EJERCICIO
sb=float(input("ingrese el sueldo base:"))
v1=float(input("ingrese la primera venta:"))
v2=float(input("ingrese la segunda venta:"))
v3=float(input("ingrese la tercera venta:"))
tot_vta=v1+v2+v3
com=tot_vta*0.10
total_pago= sb+com
print(f"el pago total es de ${total_pago:.3f}")