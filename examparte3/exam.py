def Ingresar_sueldo():
    sueldo = float(input("Ingrese el sueldo del empleado: "))
    if(sueldo > 0):
        return sueldo
    return Ingresar_sueldo()

def Determinar_Cantidad(sueldo):
    if(sueldo >= 50000) and (sueldo <= 100000 ):
        return 1
    else:
        return 0


Sueldo = 0
autoIncrement = 0

cantEmpleados = int(input("Ingrese la cantidad de empleados: "))
for x in range(cantEmpleados):
    Sueldo += Ingresar_sueldo()
    autoIncrement += Determinar_Cantidad(Sueldo)


print("Cantidad de sueldo adecuados: ",autoIncrement)
print("El promedio es: ", Sueldo/cantEmpleados)