#10 ejercicio
edad=int(input("Ingrese su edad: "))
sexo=input("Ingrese si su sexo es Masculino o Femenino (M o F): ")

if sexo == 'F':
    num_pulsos= (220-edad)/10
    print(f"El numero de pulsaciones es de: {num_pulsos}")
else:
    num_pulsos= (210-edad)/10
    print(f"El numero de pulsaciones que tiene es de: {num_pulsos}/seg")


