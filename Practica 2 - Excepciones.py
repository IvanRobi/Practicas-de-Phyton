
#Practica 2 - Excepciones

resultado = 0

"""
------Primera Consigna -------

Escribe un programa que intente dividir dos numeros.
Si el segundo numero es cero captura la excepcion ZeroDivisionError 
y muestra un mensaje de error al usuario

--------------------------------

try:
    num1= float(input("Ingrese un primer numero: "))
    num2= float(input("Ingrese un segundo numero: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("No se puede dividir por cero.")

print(f"El resultado de la division es: {resultado:.2f}")

"""

"""
------ Segunda Consigna -------

Escribe un programa que intente sumar un numero y una cadena. 
Si se produce un error de tipo, captura la excepcion TypeError y 
muestra un mensaje de error al usuario

-------------------------------- 

def division(num1,num2):
    return num1 / num2

try:
    resultado = division(6,"Hola")
except TypeError:
    print("Por favor, ingrese numeros validos.")
except ZeroDivisionError:
    print("No se puede dividir por cero.")

print(f"El resultado de la division es: {resultado}")

------ Tercera Consigna -------

Escribe un programa que intente acceder a una clave que no existe en un 
diccionario. Si se produce una excepcion KeyError captura la excepcion 
y muestra un mensaje

---------------------------------

persona_diccionario = {"nombre": "Juan", "Edad": 40, "Sexo": "Masculino", "Profesion": "Docente"}

clave = input("Ingrese una Clave: ")

try:
    valor_buscado = persona_diccionario [clave]
except KeyError:
    print("La clave no existe en el diccionario.")
else :
    print(f"El valor de la clave {clave} es: {valor_buscado}")

print("-----Fin del Programa-----")

------ Cuarta Consigna -------

Escribe un programa que intente abrir un archivo que no existe.
si se produce una excepcion FileNotFoundError, captura la excepcion y muestra
un mensaje de error al usuario. Sin embargo, tambien intenta crear el archivo 
si no existe

---------------------------------

practica_excepciones = "practica_excepciones.txt"

try:
    # Abrimos el archivo en modo lectura ('r')
    with open(practica_excepciones, "r") as archivo:
        contenido = archivo.read()
        print("El archivo se abrió correctamente.")

except FileNotFoundError:
    # Si el archivo no existe, se ejecuta este bloque
    print(f"Error: El archivo '{practica_excepciones}' no existe.")
    print("Intentando crear el archivo...")
    
    # Se crea el archivo en modo escritura ('w')
    with open(practica_excepciones, "w") as archivo:
        # Texto que se escribira en el archivo recien creado
        archivo.write("El programa ha creado este archivo porque no existia previamente.") 
        
    print(f"¡Archivo '{practica_excepciones}' creado con éxito!")


------ Cuarta Consigna -------

Escribe un programa que intente dividir dos numeros. Si el segundo numero es
cero captura la excepcion ZeroDivisionError. Si el primer numero es un numero 
no valido, captura la excepcion Value Error. En cualquier caso muestra un
mensaje de error al usuario

------------------------------

def division(num1,num2):
    return num1 / num2

try:
    num1= float(input("Ingrese un primer numero: "))
    num2= float(input("Ingrese un segundo numero: "))
    resultado = division(num1,num2)

except ValueError:
    print("Error: Por Favor, Ingrese un Valor Numerico Valido.")

except ZeroDivisionError:
    print("Error: No se puede dividir por cero.")

else:
    print(f"El resultado de la division es: {resultado:.2f}")

finally:
    print("Muchas Gracias por utilizar el programa de division.\n")
    print("\n")
    print("--------- Fin del Programa ---------")


-------------------------------- 

""" 
