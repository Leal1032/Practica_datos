from Datos import Datos
from typing import List

class GestionDatos:
    def __init__(self):
        self.datos_list: List[Datos] = []


    @property
    def ListaDatos(self)-> List:
        return self._ListaDatos
    
    @ListaDatos.setter
    def ListaDatos(self,ListaDatos:List):
        self._ListaDatos=ListaDatos

        
    def mostrarDatos(self):
        for datos in self.ListaDatos:
            print("El nombre de la persona es: ",self.Nombre)
            print("El apellido de la persona es: ",self.Apellido)
            print("La edad de la persona es: ",self.Edad)
            print("El correo de la persona es: ",self.Correo)