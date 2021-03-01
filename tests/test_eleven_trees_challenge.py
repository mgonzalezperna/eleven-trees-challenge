from eleven_trees_challenge import challenge as ch
import pytest
import datetime


def test_persona_no_esta_disponible():
    fecha = datetime.date.today()
    persona = ch.Persona("Pilar", ["Martes"], [2, 4, 7, 25])
    assert not persona.esta_disponible(fecha)


def test_persona_esta_disponible_por_dia_puntual():
    fecha = datetime.date.today()
    nombre_fecha = ch.DiasSemana(fecha.isoweekday()).name
    persona = ch.Persona("Pilar", [nombre_fecha], [])
    assert persona.esta_disponible(fecha)


def test_persona_esta_disponible_por_dia_mes():
    fecha = datetime.date.today()
    persona = ch.Persona("Pilar", [], [fecha.day])
    assert persona.esta_disponible(fecha)
