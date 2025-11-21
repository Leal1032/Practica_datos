from Datos import Datos
from typing import List
#Aqui creamos una clase hija para la lista y la consulta
class GestionDatos:
    def __init__(self):
        self.datos_list: List[Datos] = []

    def agregar_datos(self, datos: Datos):
        self.datos_list.append(datos)

    def consultar_por_cedula(self, cedula: int):
        for datos in self.datos_list:
            if datos.Cedula == cedula:
                return datos
        return None
