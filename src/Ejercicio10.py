'''
Escribir un programa que almacene en una lista los siguientes precios: 50, 75, 46, 22, 80, 65, 8 y muestre por pantalla el menor y el mayor de los precios.
'''

def mayor(numeros):
    return "El numero mayor es " + str(max(numeros))
def menor(numeros):
    return "El numero menor es " + str(min(numeros))

if __name__ == "__main__":

    #Entrada
    numeros = [50,75,46,22,80,65,8]
    #Proceso
    resultadoMa = mayor(numeros)
    resultadoMe = menor(numeros)

    #Salida
    
    print(resultadoMa)
    print(resultadoMe)