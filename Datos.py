from typing import List
class Datos:
    def __init__(self):
        pass

    @property
    def Nombre(self)-> str:
        return self._Nombre
    
    @Nombre.setter
    def Nombre(self, Nombre: str):
        self._Nombre = Nombre
    
    @property
    def Apellido(self)-> str:
        return self._Apellido
    
    @Apellido.setter
    def Apellido(self, Apellido: str):
        self._Apellido = Apellido
    
    @property
    def Edad(self)-> int:
        return self._Edad 
    
    @Edad.setter
    def Edad(self, edad: int):
        self._Edad = edad
    

    @property
    def Correo(self)-> str:
        return self._correo
    
    @Correo.setter
    def Correo(self, correo: str):
        self._correo = correo

