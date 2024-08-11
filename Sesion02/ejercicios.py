# Sesion 02

# 01 ****** Ejemplo input **********
nombre = input("¿cómo te llamas?")
print("gracias por introducir tu nombre " + nombre)

# 02 ****** Ejemplo concatenación *********
nombre = input("¿cómo te llamas?")
saludo = ("hola como estas " + nombre)
# Imprime el saludo
print (saludo)

# 03 ****** Ejercicio tipo de datos

palabra = input("hola  escribe una palabra")
#numero entero
num_int = input("Escribe un numero entero")
#flotante
num_float = input("escribe un numero flotante")
#Cadena de texto
print("string", palabra)
print("int", num_int)
print("float", num_float)

# 04 ******** Tipos de datos mejorado *********

palabra = input("hola  escribe una palabra")
#numero entero
num_int = int(input("Escribe un numero entero"))
#flotante
num_float = float(input("escribe un numero flotante"))
#Cadena de texto
print(type(palabra))
print(type(num_int))
print(type( num_float))

# 05 ****** Calculadora *****
# Calculadora
nombre = input("¿Cual es tu nombre?")
print("hola " + nombre +  "vamos a hacer una suma")
# Declaramos nuestras variables
num_uno = float(input("porfavor escribe el primer valor"))
num_dos = float(input("porfavor escribe el segundo valor"))
# Primer operación 
resultado = num_uno / num_dos
# Imprimir el resultado de la suma
print(nombre + " el resultado de la suma es:", resultado)
# Haz lo mismo para resta, multiplicación y división.



