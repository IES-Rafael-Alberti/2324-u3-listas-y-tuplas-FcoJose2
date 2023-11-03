from src.Ejercicio3 import listaAsignaturas

def test_listaAsignaturas():
    assert listaAsignaturas([1,2,3,4,5]) == "En Matemáticas has sacado 1\nEn Física has sacado 2\nEn Química has sacado 3\nEn Historia has sacado 4\nEn Lengua has sacado 5\n"