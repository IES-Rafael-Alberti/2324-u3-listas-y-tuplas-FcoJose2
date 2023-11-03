from src.Ejercicio7 import Letra, mensajeSalida

def test_Letra():
    assert Letra(["a","b","c","d","e","f","g","h","i","j","k","n","m","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]) == ["b","c","e","f","h","i","k","n","ñ","o","q","r","t","u","w","x","z"]

def test_mensajeSalida():
    assert mensajeSalida(["b","c","e","f","h","i","k","n","ñ","o","q","r","t","u","w","x","z"]) == "Las letras que no son multiplos de 3 son :b,c,e,f,h,i,k,n,ñ,o,q,r,t,u,w,x,z"