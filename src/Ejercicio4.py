'''
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor a mayor.
'''

def loteria():
    lista = []
    for i in range(5):
        numero = input("Introduce los numeros ganadores: ")
        lista.append(numero)
    return lista


if __name__ == "__main__":

    #Entrada
    #Proceso
    resultado = loteria()
    resultado.sort()

    #Salida
    for numero in resultado:
        print(numero)