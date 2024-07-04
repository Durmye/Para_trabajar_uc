import os



def puntaje(tiempo_restante, n, m, CONSTANTE, tiempo_utilizado) -> float: 
    #Devuelve valor de puntaje aproximado a dos decimales
    puntaje = (tiempo_restante * n * m * CONSTANTE) / tiempo_utilizado
    puntaje = round(puntaje, 2)
    return puntaje

def nombre_alphanum(nombre_usuario) -> bool: 
    pass


### Funciones de puntajes
## Funciones para mostrar puntajes en salon de la fama 

def leer_puntajes() -> list: 
    puntajes = []
    ruta = os.path.join("frontend/puntaje.txt")
    with open(ruta, "r") as ptjs_file: 
        ptjs_list = ptjs_file.readlines()
        for ptj in ptjs_list: 
            ptj_list = ptj.rstrip("\n").split(",")
            puntajes.append(ptj_list)
    return puntajes

def ordenar_puntajes(lista_puntajes) -> list: 
    sorted(lista_puntajes, key = lambda ptj: ptj[1])
    return lista_puntajes

## Funciones para guardar puntajes en el salon de la fama



### Funciones construccion grilla 

def leer_base(nombre_archivo: str) -> list:
    ruta = os.path.join("frontend", "base_puzzles", nombre_archivo+".txt")
    with open(ruta) as base: 
        info = base.readlines()
        puzzle = []
        for line in info: 
            linea = line.rstrip("\n").split(";")
            puzzle.append(linea)
    #Puzzle corresponde a una lista de listas 
    # con la primera lista siendo las columnas
    # y la segunda lista siendo las filas 
    # Las listas "filas" y "columnas" estan separadas
    #   por las "hints". Cada hint NO esta separada, 
    #   es decir, corresponde a un string, ej: "1,1,1"
    return puzzle

def dimension_grilla(lista: list) -> int: 
    return len(lista[0])

def obtener_columnas(lista: list) -> list:
    # Lista[0] corresponde a la lista con las 
    #   hints de las columnas.
    columnas = lista[0]
    for i in range(len(lista[0])): 
        if len(lista[0][i]) > 1:
            columnas[i] = lista[0][i].split(",")
    return columnas


def obtener_filas(lista: list) -> list: 
    # Lista[1] corresponde a la lista con las
    #   hints de las filas.
    filas = lista[1]
    for i in range(len(lista[1])): 
        if len(lista[1][i]) > 1: 
            filas[i] = lista[1][i].split(",")
    return filas 

def obtener_max_columna(columna: list) -> int: 
    max = 0
    for hint_columna in columna:
        len_actual = len(hint_columna)
        if len_actual > max: 
            max = len_actual 
    return max 

def obtener_max_fila(fila: list) -> int: 
    max = 0
    for hint_fila in fila: 
        len_actual = len(hint_fila)
        if len_actual > max: 
            max = len_actual 
    return max 
