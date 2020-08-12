#15 ejercicio
prim_pers=float(input("ingrese la inversion de la primera persona:"))
seg_pers=float(input("ingrese la inversion de la segunda persona:"))
terc_pers=float(input("ingrese la inversion de la tercera persona:"))
cant_tot=prim_pers+seg_pers+terc_pers
porc_pri_pers=prim_pers*100/cant_tot
porc_seg_pers=seg_pers*100/cant_tot
porc_terc_pers=terc_pers*100/cant_tot
print(f"el porcentaje que invierte la primera persona es:{porc_pri_pers:.2f}%")
print(f"el porcentaje que invierte la segunda persona es:{porc_seg_pers:.2f}%")
print(f"el porcentaje que invierte la tercera persona es:{porc_terc_pers:.2f}%")