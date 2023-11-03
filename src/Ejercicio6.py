'''
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el usuario tiene que repetir.
'''
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
def leerNotas():
    for asignatura in asignaturas:
        numero = int(input("Introduce la nota de " + asignatura + ": "))
        notas.append(numero)
    return notas

def suspenso(asignaturas, notas):
    for asignatura in asignaturas:
        if notas[asignatura] < 5:
            asignaturas.remove(asignatura)
    return asignaturas

if __name__ == "__main__":

    #Entrada

    #Proceso
    resultado = suspenso(asignaturas, notas)

    #Salida
    print(resultado)