from copy import copy
from collections import defaultdict
from functools import reduce
from itertools import product
from typing import Generator

from parametros import RUTA_PELICULAS, RUTA_GENEROS
from utilidades import (
    Pelicula, Genero, obtener_unicos, imprimir_peliculas,
    imprimir_generos, imprimir_peliculas_genero, imprimir_dccmax
)


# ----------------------------------------------------------------------------
# Parte 1: Cargar dataset
# ----------------------------------------------------------------------------

def cargar_peliculas(ruta: str) -> Generator:
    # Completado
    with open(ruta, "r") as peliculas:
        header = peliculas.readline().split(",")
        lista_datos = peliculas.readlines()
        for dato in lista_datos:
            dato = dato.rstrip("\n").split(",")
            dato[0] = int(dato[0])
            dato[3] = int(dato[3])
            dato[4] = float(dato[4])
            yield Pelicula(*dato)


def cargar_generos(ruta: str) -> Generator:
    # Completado
    with open(ruta, "r") as generos: 
        header = generos.readline().split()
        lista_datos = generos.readlines()
        for dato in lista_datos: 
            dato = dato.rstrip("\n").split(",")
            dato[1] = int(dato[1])
            yield Genero(*dato)


# ----------------------------------------------------------------------------
# Parte 2: Consultas sobre generadores
# ----------------------------------------------------------------------------

def obtener_directores(generador_peliculas: Generator) -> set:
    # TODO: Completar
    generador_directores = map(lambda x: x.director, generador_peliculas)
    return obtener_unicos(generador_directores)


def obtener_str_titulos(generador_peliculas: Generator) -> str:
    # TODO: Completar
    # PRIMER ELEMENTO SE ASUME COMO EL RESULTADO DE LAS EJECUCIONES DE LAS FUNCIONES
    titulos = reduce(lambda x, y: x + y.titulo + ", ", 
                     generador_peliculas, "").rstrip(", ")
    return titulos

def filtrar_peliculas(
    generador_peliculas: Generator,
    director: str | None = None,
    rating_min: float | None = None,
    rating_max: float | None = None
) -> filter:
    
    '''
    # Caso 1: Director activado
    # Caso 2: Rating min activado
    # Caso 3: Rating max activado 
    # Caso 4: Director y Rating min activado
    # Caso 5: Director y Rating max activado
    # Caso 6: Rating min y Rating max activado 
    # Caso 7: Todo activado
    # Caso 8: Nada activado
    '''

    # Para organizar casos. 
    if director != None:
        filtrar_director = True
    else: 
        filtrar_director = False

    if rating_min != None: 
        filtrar_rating_min = True
    else: 
        filtrar_rating_min = False

    if rating_max != None: 
        filtrar_rating_max = True
    else: 
        filtrar_rating_max = False

    # Retorma filtro de peliculas en base a director 
    if filtrar_director: 
        filtro_director = filter(lambda x: x.director == director, generador_peliculas)
    # Retorna filtro de peliculas en base a rating min 
    if filtrar_rating_min:
        filtro_rating_min = filter(lambda x: x.rating >= rating_min, generador_peliculas) 
    # Retorna filtro de peliculas en base a rating max
    if filtrar_rating_max: 
        filtro_rating_max = filter(lambda x: x.rating <= rating_max, generador_peliculas)
    
    #Caso 1
    if filtrar_director and not filtrar_rating_min and not filtrar_rating_max: 
        return filtro_director
    #Caso 2
    elif filtrar_rating_min and not filtrar_director and not filtrar_rating_max:
        return filtro_rating_min
    #Caso 3
    elif filtrar_rating_max and not filtrar_director and not filtrar_rating_min:
        return filtro_rating_max
    #Caso 4
    elif filtrar_director and filtrar_rating_min and not filtrar_rating_max:
        filtro_final = filter(lambda pelicula: pelicula.rating >= rating_min, filtro_director)
        return filtro_final
    #Caso 5
    elif filtrar_director and not filtrar_rating_min and filtrar_rating_max:
        filtro_final = filter(lambda pelicula: pelicula.rating <= rating_max, filtro_director)
        return filtro_final
    #Caso 6
    elif not filtrar_director and filtrar_rating_min and filtrar_rating_max:
        filtro_final = filter(lambda pelicula: pelicula.rating <= rating_max, filtro_rating_min)
        return filtro_final
    #Caso 7
    elif filtrar_director and filtrar_rating_min and filtrar_rating_max: 
        filtro_final = filter(lambda pelicula: pelicula.rating >= rating_min, filtro_director)
        filtro_definitivo = filter(lambda pelicula: pelicula.rating <= rating_max, filtro_final)
        return filtro_definitivo
    #Caso 8
    elif not filtrar_director and not filtrar_rating_min and not filtrar_rating_max:
        return None
        
def filtrar_peliculas_por_genero(
    generador_peliculas: Generator,
    generador_generos: Generator,
    genero: str | None = None
) -> Generator:
    # TODO: Completar
    if genero == None: 
        filtro = filter(lambda x: x[0].id_pelicula == x[1].id_pelicula ,product(generador_peliculas, generador_generos))
    else: 
        filtro = filter(lambda x: x[0].id_pelicula == x[1].id_pelicula and x[1].genero == genero, product(generador_peliculas, generador_generos))

    return filtro 

# ----------------------------------------------------------------------------
# Parte 3: Iterables
# ----------------------------------------------------------------------------

class DCCMax:
    def __init__(self, peliculas: list) -> None:
        self.peliculas = peliculas

    def __iter__(self):
        
        return IteradorDCCMax(self.peliculas)


class IteradorDCCMax:
    def __init__(self, iterable_peliculas: list) -> None:
        self.peliculas = copy(iterable_peliculas)

    def __iter__(self):
        
        self.peliculas = sorted(self.peliculas, key = self.orden)
        return self

    def __next__(self) -> tuple:
        if not self.peliculas: 
            # Se levanta la excepción correspondiente
            raise StopIteration()
        else: 
            return self.peliculas.pop(0)
        
    def orden(self, item):
        return (item[3], -item[4])

if __name__ == '__main__':
    print('> Cargar películas:')
    imprimir_peliculas(cargar_peliculas(RUTA_PELICULAS))
    print()

    print('> Cargar géneros')
    imprimir_generos(cargar_generos(RUTA_GENEROS), 5)
    print()

    print('> Obtener directores:')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    print(list(obtener_directores(generador_peliculas)))
    print()

    print('> Obtener string títulos')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    print(obtener_str_titulos(generador_peliculas))
    print()

    print('> Filtrar películas (por director):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(
        generador_peliculas, director='Christopher Nolan'
    ))
    print('\n> Filtrar películas (rating min):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(generador_peliculas, rating_min=9.1))
    print('\n> Filtrar películas (rating max):')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    imprimir_peliculas(filtrar_peliculas(generador_peliculas, rating_max=8.7))
    print()

    print('> Filtrar películas por género')
    generador_peliculas = cargar_peliculas(RUTA_PELICULAS)
    generador_generos = cargar_generos(RUTA_GENEROS)
    imprimir_peliculas_genero(filtrar_peliculas_por_genero(
        generador_peliculas, generador_generos, 'Biography'
    ))
    print()

    print('> DCC Max...')
    imprimir_dccmax(DCCMax(list(cargar_peliculas(RUTA_PELICULAS))))





