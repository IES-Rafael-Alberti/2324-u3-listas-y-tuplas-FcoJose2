from src.Ejercicio4 import ordenarNumero, pedirNumeros
import pytest

def test_ordenarNumero():
    assert ordenarNumero([32,34,246,2,45,11,23,4]) == [2, 4, 11, 23, 32, 34, 45, 246]

def test_pedirNumeros(monkeypatch):
    input_values = [32,34,246,2,45,11,23,4,65]
    def mock_input(s):
        return input_values.pop(0)
    monkeypatch.setattr("builtins.input",mock_input)
    assert pedirNumeros() == [32,34,246,2,45,11,23,4,65]
