import os 
import json

def dimension_puzzle(nombre_archivo: str) -> int: 
    ruta = os.path.join("base_puzzles", nombre_archivo+".txt")
    with open(ruta, "r") as estructura: 
        columnas = estructura.readline().split(";")
        dimension = len(columnas)
    return dimension

def leer_json(nombre_archivo: str) -> dict: 
    with open(nombre_archivo) as datos: 
        return json.load(datos)
    
def leer_base(nombre_archivo: str) -> list:
    ruta = os.path.join("backend", "base_puzzles", nombre_archivo+".txt")
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
    return len(puzzle[0])

def dimension_mapa(lista: list) -> int: 
    return len(lista[0])
