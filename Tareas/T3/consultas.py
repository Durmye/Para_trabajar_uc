from typing import Generator

# ----------------------------------------------------------------------
# COMPLETAR
# ----------------------------------------------------------------------

import os 
from utilidades import Animales, Candidatos, Distritos, \
                       Locales, Votos, Ponderador 

import auxiliares_cargar_datos as aux_1
import auxiliares_generador1 as gen_1
import auxiliares_generador2 as gen_2
# CARGA DE DATOS

def cargar_datos(tipo_generator: str, tamano: str):
    ruta = os.path.join("data", tamano, tipo_generator+".csv")
    with open(ruta, "r", encoding = "latin-1") as info: 
        atributos = info.readline()
        datos = info.readlines()
       
    for dato in datos: 
        dato = dato.rstrip("\n")

        #Entrega 
        if tipo_generator == "animales":
            yield aux_1.instanciar_animal(tipo_generator, dato)
        elif tipo_generator == "candidatos": 
            yield aux_1.instanciar_candidato(tipo_generator, dato)
        elif tipo_generator == "distritos": 
            yield aux_1.instanciar_distrito(tipo_generator, dato)
        elif tipo_generator == "locales":
            yield aux_1.instanciar_locales(tipo_generator, dato)
        elif tipo_generator == "ponderadores": 
            yield aux_1.instanciar_ponderaciones(tipo_generator, dato)
        elif tipo_generator == "votos":
            yield aux_1.instanciar_voto(tipo_generator, dato)

# 1 GENERADOR

def animales_segun_edad(generador_animales: Generator,
                        comparador: str, edad: int) -> Generator:
    return gen_1.animales_segun_edad(generador_animales, 
                                    comparador,
                                    edad)


def animales_que_votaron_por(generador_votos: Generator,
                            id_candidato: int) -> Generator:    
    return gen_1.animales_que_votaron_por(generador_votos, 
                                          id_candidato)


def cantidad_votos_candidato(generador_votos: Generator,
                            id_candidato: int) -> int:
    return gen_1.cantidad_votos_candidato(generador_votos, 
                                          id_candidato)


def ciudades_distritos(generador_distritos: Generator) -> Generator:
    return gen_1.ciudades_distritos(generador_distritos)


def especies_postulantes(generador_candidatos: Generator,
                        postulantes: int) ->Generator:
    return gen_1.especies_postulantes(generador_candidatos, postulantes)


def pares_candidatos(generador_candidatos: Generator) -> Generator:
    return gen_1.pares_candidatos(generador_candidatos)

def votos_alcalde_en_local(generador_votos: Generator, candidato: int,
                            local: int) -> Generator:
    return gen_1.votos_alcalde_en_local(generador_votos, candidato, local)


def locales_mas_votos_comuna(generador_locales: Generator,
                            cantidad_minima_votantes: int, id_comuna: int) -> Generator:
    return gen_1.locales_mas_votos_comuna(generador_locales, cantidad_minima_votantes, id_comuna)


def votos_candidato_mas_votado(generador_votos: Generator) -> Generator:
    return gen_1.votos_candidato_mas_votado(generador_votos)


# 2 GENERADORES


def animales_segun_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator, comparador: str,
    edad: int) -> Generator:
    
    return gen_2.animales_segun_edad_humana(generador_animales,
                                            generador_ponderadores,
                                            comparador, 
                                            edad)


def animal_mas_viejo_edad_humana(generador_animales: Generator,
    generador_ponderadores: Generator) -> Generator:
    return gen_2.animal_mas_viejo_edad_humana(generador_animales,
                                              generador_ponderadores,
                                              )

def votos_por_especie(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    return gen_2.votos_por_especie(generador_candidatos,
                                   generador_votos
                                   )


def hallar_region(generador_distritos: Generator,
    generador_locales: Generator, id_animal: int) -> str:
    return gen_2.hallar_region(generador_distritos, 
                               generador_locales, 
                               id_animal)


def max_locales_distrito(generador_distritos: Generator,
    generador_locales: Generator) -> Generator:
    return gen_2.max_locales_distrito(generador_distritos, generador_locales)


def votaron_por_si_mismos(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def ganadores_por_distrito(generador_candidatos: Generator,
    generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


# 3 o MAS GENERADORES

def mismo_mes_candidato(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator,
    id_candidato: str) -> Generator:
    # COMPLETAR
    pass


def edad_promedio_humana_voto_comuna(generador_animales: Generator,
    generador_ponderadores: Generator, generador_votos: Generator,
    id_candidato: int, id_comuna:int ) -> float:
    # COMPLETAR
    pass


def votos_interespecie(generador_animales: Generator,
    generador_votos: Generator, generador_candidatos: Generator,
    misma_especie: bool = False,) -> Generator:
    # COMPLETAR
    pass


def porcentaje_apoyo_especie(generador_animales: Generator,
    generador_candidatos: Generator, generador_votos: Generator) -> Generator:
    # COMPLETAR
    pass


def votos_validos(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores) -> int:
    # COMPLETAR
    pass


def cantidad_votos_especie_entre_edades(generador_animales: Generator,
    generador_votos: Generator, generador_ponderador: Generator,
    especie: str, edad_minima: int, edad_maxima: int) -> str:
    # COMPLETAR
    pass


def distrito_mas_votos_especie_bisiesto(generador_animales: Generator,
    generador_votos: Generator, generador_distritos: Generator,
    especie: str) -> str:
    # COMPLETAR 
    pass


def votos_validos_local(generador_animales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator,
    id_local: int) -> Generator:
    # COMPLETAR
    pass


def votantes_validos_por_distritos(generador_animales: Generator,
    generador_distritos: Generator, generador_locales: Generator,
    generador_votos: Generator, generador_ponderadores: Generator) -> Generator:
    # COMPLETAR
    pass