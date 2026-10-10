

"""

---------------------------------

Practica 1 - el mayor de dos números ingresados por teclado usando un 

operador ternario


nro_1 = float(input("Ingrese el primer numero: "))
nro_2 = float(input("Ingrese el segundo numero: "))

print("El numero 1 es Mayor" if nro_1 > nro_2 else "El numero 2 es Mayor")

-------------------------------------------------

Practica 2 - Buscar una palabra en una lista ingresada por teclado usando args 
y un operador ternario


def lista_de_palabras(*lista):
    palabra = input("Ingrese la palabra a buscar: ")
    print("La palabra se encuentra en la lista" if palabra in lista else "La palabra no se encuentra en la lista")


lista_de_palabras("Hola", "Mundo", "Python", "Programacion")

-------------------------------------------------

Practica 3 - Determinar si un número es par o impar

nro_buscado = int(input("Ingrese el numero deseado: " ))

print("El numero es Par" if nro_buscado % 2 == 0 else "El numero es Impar")

-------------------------------------------------

Practica 4 - Calcular el promedio de una lista de números usando args 
y un operador ternario

def lista_de_numeros(*lista):

    promedio = sum(lista) / len(lista) if lista else 0
    print(f"El promedio de la lista es: {promedio}")

    
lista_de_numeros(1, 2, 3, 4, 5)

"""




