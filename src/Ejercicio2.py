'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.
'''

def listaAsignaturas():
    lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    mensaje = ""
    for asignatura in lista:
        mensaje += "Yo estudio " + asignatura + "\n"
    return mensaje
    

if __name__ == "__main__":

    #Entrada

    #Proceso
    resultado = listaAsignaturas()

    #Salida
    print(resultado)
