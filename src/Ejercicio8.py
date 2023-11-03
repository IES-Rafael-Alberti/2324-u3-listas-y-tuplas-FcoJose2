'''
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un palíndromo.
'''
def comprobarPalindromo(palabra):
    palabra = palabra.lower()
    return palabra == palabra[::-1]

if __name__ == "__main__":

    #Entrada
    palabra = input("Introduce una palabra: ")
    #Proceso
    resultado = comprobarPalindromo(palabra)

    #Salida
    
    if resultado:
        print("Es un palíndromo")
    else:
        print("No es un palíndromo")