'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

def pedirNumeros():
    contador = 0
    numeros = []
    while contador < 9:
        numero = int(input("Introduce el número: "))
        numeros.append(numero)
        contador = contador + 1
    return numeros


def ordenarNumero(numeros):
    numeros.sort()
    return numeros

if __name__ == "__main__":

    #Entrada
    numeros = pedirNumeros()
    #Proceso
    resultado = ordenarNumero(numeros)
    #Salida
    print(resultado)
