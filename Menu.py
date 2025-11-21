from Datos import Datos #Se importan los datos como nombre, apellido etc..
from Gestion_datos import GestionDatos #Agregamos la funcion de la lista y la consulta

gt = GestionDatos() #Gt va a ser igual a GestionDatos

while True: #Aqui iniciamos e imprimimos el menu 
    print("-----------")
    print("   Menu   ")
    print("1. Agregar")
    print("2. Consultar")
    print("3. Salir")

    opcion = input("Seleccione una opcion: ") #Aqui le estamos pidiendo al usuario que digite una opcion del menu

    if opcion == '1':
        agregar = Datos() #agregar va a ser igual que los datos
        agregar.Nombre = input("Ingrese el nombre: ") #Aqui pedimos que igrese el nombre, el apellido etc
        agregar.Apellido = input("Ingrese el apellido: ")
        agregar.Edad = int(input("Ingrese la edad: "))
        agregar.Cedula = int(input("Ingrese el numero de identificacion: "))
        agregar.Correo = input("Ingrese el correo: ")
        gt.agregar_datos(agregar) #Aqui agregamos los datos obtenidos y lo agregamos a la lista 
        print("Datos agregados correctamente.\n") 

    elif opcion == '2':
        cedula = int(input("Ingrese la cedula a consultar: ")) #Aqui pedimos el numero de documento para consultar la persona
        resultado = gt.consultar_por_cedula(cedula) #Aqui el resulatdo va a hacer igual a los datos de el numero de identidad que consultan

        if resultado:
            print("---- Datos encontrados ----") #Aqui mostranos los datos con el numero de documento que ingresaro el usuario
            print(f"Nombre: {resultado.Nombre}")
            print(f"Apellido: {resultado.Apellido}")
            print(f"Edad: {resultado.Edad}")
            print(f"Correo: {resultado.Correo}")
        else:
            print("No se encontró un registro con esa cédula.") #Si no hay datos con el numero de cedula bota este mensaje

    elif opcion == '3': #Esta opcion es para salir del menu
        print("Salir")
        break

    else:
        print("Opción no válida") #Si no se encuantra la opcion que digito el usuario bota este mensaje
