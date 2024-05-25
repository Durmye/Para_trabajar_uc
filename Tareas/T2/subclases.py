from clases import Combatiente, Item
from random import randint
from parametros import CANSANCIO, PROB_CAB, RED_CAB, ATQ_CAB, \
    PROB_MAG, RED_MAG, ATQ_MAG, PROB_PAL, AUM_PAL, PROB_CAR, \
    AUM_CAR, PROB_MDB, DEF_MDB


class Guerrero(Combatiente):
    def __init__(self, nombre: str, 
                 vida: int, 
                 poder: int, defensa: int, 
                 agilidad: int, resistencia: int) -> None:
        
        super().__init__(nombre, vida, poder, defensa, agilidad, resistencia)
        self.tipo = "Guerrero"

    def atacar(self, oponente): 
        #Formula ataque 
        ataque = round(self.ataque - oponente.defensa)
            
        #Chequea que sea >= 1
        if ataque < 1: 
           ataque = 1
            
        #Cambio en los atributos propios y del enemigo. 
        oponente.vida -= ataque 
        self.agilidad -= round(self.agilidad * CANSANCIO)

    def evolucionar(self, item: Item): 
        if item.nombre == "Armadura": 
            evolucion = Paladin(self.nombre, self.vida,
                                         self.poder, self.defensa,
                                         self.agilidad, self.resistencia)
            return [True, evolucion]
        elif item.nombre == "Pergamino":
            evolucion = Mago_Batalla(self.nombre, self.vida,
                                self.poder, self.defensa,
                                self.agilidad, self.resistencia)
            return [True, evolucion]
        else: 
            return [False]


class Mago(Combatiente):
    def __init__(self, nombre: str, 
                 vida: int, 
                 poder: int, defensa: int, 
                 agilidad: int, resistencia: int) -> None:
        
        super().__init__(nombre, vida, poder, defensa, agilidad, resistencia)
        self.tipo = "Mago" 
     
    def atacar(self, oponente): 

        #Dependiendo de la probabilidad activa o no un poder
        # Y resta vida del oponente
        if randint(0, 100) <= PROB_MAG:
            ataque = round(self.ataque * (ATQ_MAG / 100) - oponente.defensa * ((100 - RED_MAG)/100))
            if ataque < 1:
                ataque = 1
            oponente.vida -= ataque
        else: 
            ataque = round(self.ataque - oponente.defensa)
            if ataque < 1: 
                ataque = 1
            oponente.vida -= ataque 

        #En cualquier caso el Mago se fatiga 
        self.resistencia -= round(self.resistencia * CANSANCIO)
        self.agilidad -= round(self.agilidad * CANSANCIO)


    def evolucionar(self, item: Item): 
        if item.nombre == "Armadura": 
            evolucion = Caballero_Arcano(self.nombre, self.vida,
                                         self.poder, self.defensa,
                                         self.agilidad, self.resistencia)
            return [True, evolucion]
        elif item.nombre == "Lanza":
            evolucion = Mago_Batalla(self.nombre, self.vida,
                                self.poder, self.defensa,
                                self.agilidad, self.resistencia)
            return [True, evolucion]
        else: 
            return [False]


class Caballero(Combatiente):
    def __init__(self, nombre: str, 
                 vida: int, 
                 poder: int, defensa: int, 
                 agilidad: int, resistencia: int) -> None:

        super().__init__(nombre, vida, poder, defensa, agilidad, resistencia)
        self.tipo = "Caballero"

    def atacar(self, oponente): 

        #Dependiendo de la probabilidad activa o no poder
        # Y resta vida del oponente
        if randint(0, 100) <= PROB_CAB: 
            oponente.poder -= round(oponente.poder * RED_CAB)
            ataque = round(self.ataque * (ATQ_CAB/100) - oponente.defensa)
            if ataque < 1: 
                ataque = 1
            oponente.vida -= ataque
        else: 
            ataque = round(self.ataque - oponente.defensa)
            if ataque < 1:
                ataque = 1
            oponente.vida -= ataque
            
        #En cualquier caso Caballero se fatiga 
        self.resistencia -= round(self.resistencia * CANSANCIO)

    def evolucionar(self, item: Item): 
        if item.nombre == "Pergamino": 
            evolucion = Caballero_Arcano(self.nombre, self.vida,
                                         self.poder, self.defensa,
                                         self.agilidad, self.resistencia)
            return [True, evolucion]
        elif item.nombre == "Lanza":
            evolucion = Paladin(self.nombre, self.vida,
                                self.poder, self.defensa,
                                self.agilidad, self.resistencia)
            return [True, evolucion]
        else: 
            return [False]


class Paladin(Guerrero, Caballero):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Paladin"

    def atacar(self, oponente): 
        #En caso de que se active poder, ataca como caballero
        if randint(0, 100) <= PROB_PAL: 
            ataque = round(self.ataque * (ATQ_CAB/100) - oponente.defensa )
            if ataque < 1: 
                ataque = 1
            oponente.vida -= ataque
        else: 
            ataque = round(self.ataque - oponente.defensa)
            if ataque < 1:
                ataque = 1
            oponente.vida -= ataque
            
        #En cualquier Paladin aumenta resistencia
        self.resistencia += round(self.resistencia * AUM_PAL)


class Caballero_Arcano(Mago, Caballero):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Caballero Arcano"


    def atacar(self, oponente): 
        #Ataque caballero 
        if randint(0, 100) <= PROB_CAR:
            ataque = round(self.ataque * (ATQ_CAB/100) - oponente.defensa)
            if ataque < 1: 
                ataque = 1
            oponente.vida -= ataque
        #ataque mago 
        else: 
            ataque = round(self.ataque * (ATQ_MAG / 100) - oponente.defensa * ((100 - RED_MAG)/100))
            if ataque < 1:
                ataque = 1
            oponente.vida -= ataque

        #En cualquier caso se fatiga
        self.resistecia = round(self.resistencia * CANSANCIO)
        #En cualquier caso aumenta su agilidad y poder 
        self.agilidad = round(self.agilidad * AUM_CAR)
        self.poder = round(self.poder * AUM_CAR)


class Mago_Batalla(Guerrero, Mago):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.tipo = "Mago de Batalla"
        
    def ataque(self, oponente): 
        if randint(0, 100) <= PROB_MDB: 
            ataque = round(self.ataque * (ATQ_MAG / 100) - oponente.defensa * ((100 - RED_MAG)/100))
            if ataque < 1:
                ataque = 1
            oponente.vida -= ataque
        else: 
            ataque = round(self.ataque - oponente.defensa)
            if ataque < 1: 
                ataque = 1
            oponente.vida -= ataque 

        #En cualquier caso se fatiga 
        self.agilidad -= round(self.agilidad * CANSANCIO)

        #En cualquier caso su defensa aumenta   
        self.defensa += round(self.defensa * DEF_MDB)