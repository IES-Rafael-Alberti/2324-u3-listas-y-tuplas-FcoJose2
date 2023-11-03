'''
Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre por pantalla la lista resultante.
'''


def Letra(abecedario):
    del abecedario[::3]
    return abecedario

def mensajeSalida(letras):
    resultado = ",".join(letras)
    return "Las letras que no son multiplos de 3 son :" + resultado


if __name__ == "__main__":

    #Entrada
    abecedario = ["a","b","c","d","e","f","g","h","i","j","k","n","m","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
    #Proceso
    letras = Letra(abecedario)
    resultado = mensajeSalida(letras)
    #Salida
    print(resultado)
