def obtener_coordenadas(red, estaciones, inicio, destino):

    #Recorre lista estaciones hasta encontrar la estacion = inicio y guarda su indice. 
    fila = int()
    columna = int()
    for indice in range(len(red)):
        if estaciones[indice] == inicio: 
            fila = indice
      
    #Recorre lista estaciones hasta encontrar la estacion = destino y guarda su indice. 
    for indice in range(len(red)):
        if estaciones[indice] == destino: 
           columna = indice
    return [fila, columna]

def imprimir_opciones():
    print("")
    print("")
    print("Opcion 1: Mostrar red")
    print("Opcion 2: Encontrar ciclo mas corto")
    print("Opcion 3: Asegurar ruta")
    print("Opcion 4: Salir del programa")
    print("")


