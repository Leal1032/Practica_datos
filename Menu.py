from Datos import Datos #Se importan los datos como nombre, apellido etc..
from Gestion_datos import GestionDatos #Agregamos la funcion de la lista y la consulta

gt = GestionDatos() #Gt va a ser igual a GestionDatos

while True: #Aqui iniciamos e imprimimos el menu 
    print("-----------")
    print("   Menu   ")
    print("1. Agregar")
    print("2. Modificar")
    print("3. consultar por cédula")
    print("4. Eliminar")
    print("5. Salir")

    opcion = input("Seleccione una opcion: ") #Aqui le estamos pidiendo al usuario que digite una opcion del menu

    if opcion == '1':
        agregar = Datos() #agregar va a ser igual que los datos
        agregar.Nombre = input("Ingrese el nombre: ") #Aqui pedimos que igrese el nombre, el apellido etc
        agregar.Apellido = input("Ingrese el apellido: ")
        agregar.Edad = int(input("Ingrese la edad: "))
        while True: #este while es para que no se repita el numero de cedula
            agregar.Cedula = int(input("Ingrese la cedula: "))
            if gt.consultar_por_cedula(agregar.Cedula) is None:
                break
            else:
                print("La cédula ya está registrada. Por favor, ingrese una cédula diferente.")
                continue
        agregar.Correo = input("Ingrese el correo: ")
        gt.agregar_datos(agregar) #Aqui agregamos los datos obtenidos y lo agregamos a la lista 
        print("Datos agregados correctamente.") 
        print("-----------")
    
    if opcion == '2':
        modificar = Datos()
        modificar.Cedula = int(input("Ingrese la cedula a modificar: ")) #Aqui pedimos el numero de documento para modificar la persona
        modificar.Nombre = input("Ingrese el nuevo nombre: ") #Aqui pedimos que igrese el nuevo nombre, el apellido etc
        modificar.Apellido = input("Ingrese el nuevo apellido: ")
        modificar.Edad = int(input("Ingrese la nueva edad: "))
        modificar.Correo = input("Ingrese el nuevo correo: ")
        gt.modificar_datos(modificar) #Aqui el exito va a ser igual a modificar los datos obtenidos
        returned = gt.modificar_datos(modificar)
        if not returned:
            print("No se encontró un registro con esa cédula.")
        else:
            print("Datos modificados correctamente.")
      
    elif opcion == '3':
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

    if opcion == '4':
        eliminar = int(input("Ingrese la cedula a eliminar: ")) #Aqui pedimos el numero de documento para eliminar la persona
        resultado = gt.consultar_por_cedula(eliminar) #Aqui el resulatdo
        if resultado:
            gt.datos_list.remove(resultado) #Si el resultado es verdadero elimina los datos de la lista
            print("Datos eliminados correctamente.")
        else:
            print("No se encontró un registro con esa cédula.") #Si no hay datos con el numero de cedula bota este mensaje

    elif opcion == '5':
        print("Saliendo del programa...") #Si el usuario digita 5 sale del programa
        break
