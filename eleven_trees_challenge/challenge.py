from typing import List
import datetime
from enum import Enum


class DiasSemana(Enum):
    Lunes = 1
    Martes = 2
    Miercoles = 3
    Jueves = 4
    Viernes = 5
    Sabado = 6
    Domingo = 7


class Staff:
    pass


class Persona:
    nombre: str
    dias_puntuales: List[str]
    dias_mes: List[int]

    def __init__(self, nombre: str, dias_puntuales: List[str], dias_mes: List[int]):
        self.nombre = nombre
        self.dias_puntuales = dias_puntuales
        self.dias_mes = dias_mes

    def esta_disponible(self, fecha: datetime.date):
        dia_puntual = fecha.isoweekday()
        dia_mes = fecha.day
        return (
            dia_mes in self.dias_mes
            or DiasSemana(dia_puntual).name in self.dias_puntuales
        )


class Equipo:
    pass


class Sucursal:
    pass


def main():
    print(f"Hello world!")
