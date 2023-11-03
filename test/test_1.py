from src.Ejercicio1 import listaAsignaturas

def test_listaAsignaturas():
    assert listaAsignaturas() == ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']