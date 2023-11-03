from src.Ejercicio8 import comprobarPalindromo

def test_comprobarPalindromo():
    assert comprobarPalindromo("Ana") == True
    assert comprobarPalindromo("Paco") == False