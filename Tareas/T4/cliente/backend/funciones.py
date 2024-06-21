import os 

def dimension_puzzle(nombre_archivo: str) -> int: 
    ruta = os.path.join("base_puzzles", nombre_archivo+".txt")
    with open(ruta, "r") as estructura: 
        columnas = estructura.readline().split(";")
        dimension = len(columnas)
    return dimension

