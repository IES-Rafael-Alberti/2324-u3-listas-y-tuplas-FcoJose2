'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.
'''

def listaAsignaturas(notas):
    lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    mensaje = ""
    for i, asignatura in enumerate(lista):
        mensaje += "En " + asignatura + " has sacado " + str(notas[i]) + "\n"
    return mensaje


if __name__ == "__main__":

    #Entrada
    notas = []
    for asignatura in ["Matemáticas", "Física", "Química", "Historia", "Lengua"]:
        nota = input("Introduce tu nota en " + asignatura + ": ")
        notas.append(nota)
    #Proceso
    resultado = listaAsignaturas(nota)

    #Salida
    print(resultado)