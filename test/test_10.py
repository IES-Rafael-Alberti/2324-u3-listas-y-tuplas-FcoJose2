from src.Ejercicio10  import menor , mayor

def test_menor():
    assert menor([50,75,46,22,80,65,8]) == "El numero menor es 8"

def test_mayor():
    assert mayor([50,75,46,22,80,65,8]) == "El numero mayor es 80"