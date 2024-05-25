#!/usr/bin/python 
# -*- coding: utf-8 -*- 
import os
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREN = '\033[92m'
    OKYEOW = '\033[93m'
    OKREDS = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def is_number(n):
    try:
        float(n)   # Intentamos transformar la variable a float, si no funciona devolverá error
    except ValueError:
        return False
    return True

def valid_number(msg):
    valido = False
    # Repetimos la solicitud hasta que se ingrese un número
    while (not valido):
        ingreso = input(msg)
        # Si es que se ingresa un número y es mayor a 0 entonces se valida
        if (is_number(ingreso) and (float(ingreso)>0)):
            valido = True
            # Si es un número decimal, se redondea al número entero más cercano
            numero = round(float(ingreso),0)
            # Lo transformamos a entero en caso de de haber sido aproximado
            numero = int(numero)
            return numero
    return None

def final_msg():
    print(input("Presione Cualquier tecla para continuar..."))
    os.system('cls')
    return True

"""
Esta definición busca por números primos, fue adaptada de la original del libro
para ser más eficiente, en vez de buscar todos los números entre el 2 y el entregado
solo buscamos hasta la mitad de los divisores, si a la mitad del número no hay
en la segunda mitad tampoco.
"""
def prime_search(numero):

    creo_que_es_primo = True
    for divisor in range(2, int(round(numero/2,0))):
        if (numero % divisor == 0): 
            creo_que_es_primo = False
            break
    return creo_que_es_primo
    
opcion = ""
primos = []
os.system('cls')
while (opcion != "3"):
    numero = 0
    limite = 0
    primos.clear()
    print("\n" + bcolors.UNDERLINE + "Escoge una opción" + bcolors.ENDC )
    print("1) Listar Números Primos.")
    print("2) Chequear Número Primo.")
    print("3) Salir.")
    opcion = input(bcolors.OKYEOW + "\nIngresa la tarea a realizar (1-3) y pulsa el retorno de carro: " + bcolors.ENDC)
    if opcion == "1":
        limite = valid_number("Hasta que número: ")
        inicio = time.time()
        primos.append(1)
        for numero in range(2, limite+1):
            creo_que_es_primo = prime_search(numero)
            if creo_que_es_primo:
                primos.append(numero)
        print("\n" + bcolors.HEADER + f"Hay {len(primos)} números primos entre el 0 y {limite}: {primos}" + bcolors.ENDC)
        fin = time.time()
        print(fin - inicio)
        final_msg()
    elif opcion == "2":
        aux = ""
        numero = valid_number("Ingrese un número entero positivo mayor a 0: ")
        if (numero > 1):
            inicio = time.time()
            creo_que_es_primo = prime_search(numero)
            fin = time.time()
            print(fin-inicio)
        else: 
            creo_que_es_primo = True

        if not creo_que_es_primo:
            aux = " no"
        print(f"\n" + bcolors.HEADER + "El número {0}{1} es primo." .format (numero, aux) + bcolors.ENDC)
        final_msg()

    elif opcion != "3":
        if opcion == "":
            opcion = "intro"
        print(bcolors.OKREDS + "Solo hay tres opciones: 1, 2 ó 3. Tú has tecleado " + opcion + bcolors.ENDC)
        final_msg()


"""
Marzal Varó, A. García Sevilla, P. y Gracia Luengo, I. (2016). 
Introducción a la programación con Python 3: 
( ed.). Castelló de la Plana, Spain: D - 
Universitat Jaume I. Servei de Comunicació i Publicacions. 
Recuperado de https://elibro.net/es/ereader/ipp/51760?page=141.
Edición: Pablo Rodríguez R.
"""