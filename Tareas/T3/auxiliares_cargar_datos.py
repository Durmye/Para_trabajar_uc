from utilidades import Animales, Candidatos, Distritos, \
                       Locales, Votos, Ponderador

def instanciar_animal(tipo_generator: str, atributos: str): 
    info = atributos.split(",") 
    id_animal = int(info[0])
    nombre = info[1]
    especie = info[2]
    id_comuna = int(info[3])
    peso_kg = float(info[4])
    edad = int(info[5])
    fecha_nacimiento = info[6]
    return Animales(id_animal, nombre, especie, id_comuna, peso_kg, edad, fecha_nacimiento)

def instanciar_candidato(tipo_generator: str, atributos: str):
    info = atributos.split(",")
    id_candidato = int(info[0])
    nombre = info[1]
    id_distrito_postulacion = int(info[2])
    especie = info[3]
    return Candidatos(id_candidato, nombre, id_distrito_postulacion, especie)

def instanciar_distrito(tipo_genrator: str, atributos: str): 
    info = atributos.split(",")
    id_distrito = int(info[0])
    nombre = info[1]
    id_comuna = int(info[2])
    provincia = info[3]
    region = info[4]
    return Distritos(id_distrito, nombre, id_comuna, provincia, region)

def instanciar_locales(tipo_generator: str, atributos: str): 
    indice_lista = atributos.find("[")

    atributos_1 = atributos[:indice_lista].rstrip(",").split(",")
    id_local = int(atributos_1[0])
    nombre_local = atributos_1[1]
    id_comuna = int(atributos_1[2])

    id_votantes = atributos[indice_lista+1:].rstrip("]").split(",")
    for i in range(len(id_votantes)):
        if len(id_votantes[i]) > 0:
            id_votantes[i] = int(id_votantes[i])

    return Locales(id_local, nombre_local, id_comuna, id_votantes)

def instanciar_ponderaciones(tipo_generator: str, atributos: str): 
    info = atributos.split(",")
    especie = info[0]
    ponderador = float(info[1])

    return Ponderador(especie, ponderador)

def instanciar_voto(tipo_generator: str, atributos: str): 
    info = atributos.split(",")
    idvoto = int(info[0])
    votante = int(info[1])
    idlocal = int(info[2])
    idcandidato = int(info[3])

    return Votos(idvoto, votante, idlocal, idcandidato)