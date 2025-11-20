from Datos import Datos
from Gestion_datos import GestionDatos
from typing import List
while True:
    print("-----------")
    print("   Menu   ")
    print("1. Agregar")
    print("2. Consultar")
    print("3. Salir")

    opcion = input("Seleccione la opcion: ")

    if opcion == '1':

        agregar = Datos()
        nombre = input("Ingrese el nombre: ")
        listaDatos.append(nombre)
        apellido = input("Ingrese el apellido: ")
        listaDatos.append(apellido)
        edad = int(input("Ingrese la edad: "))
        listaDatos.append(edad)
        correo = input("Ingrese el correo: ")
        listaDatos.append(correo)
        agregar.Nombre = nombre
        agregar.Apellido = apellido
        agregar.Edad = edad
        agregar.Correo = correo
        print("Datos agregados correctamente.")

    elif opcion == '2':
            agregar.mostrarDatos()
    elif opcion == '3':
        print("Salir")
        break
    else:
        print("Opcion no valida")