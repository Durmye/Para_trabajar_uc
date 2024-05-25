from abc import ABC, abstractmethod
import random


class Vehiculo(ABC):
    identificador = 0
    
    def __init__(self, rendimiento: int, marca: str, energia = 120, *args, **kargs):
        self.rendimiento = rendimiento 
        self.marca = marca
        self.energia = energia
        self.identificador = Vehiculo.identificador
        Vehiculo.identificador += 1

        

    @abstractmethod
    def recorrer(self, kilometros):
        pass
    
    @property
    def autonomia(self):
        autonomia = self._energia * self.rendimiento
        return autonomia
    
    @property
    def energia(self):
        return self._energia 
    
    @energia.setter
    def energia(self, dato):
        if dato < 0: 
            self._energia = 0
        else:
            self._energia = dato


class AutoBencina(Vehiculo):
    
    def __init__(self,bencina_favorita: int, *args, **kargs):
        super().__init__(*args, **kargs)
        self.bencina_favorita = bencina_favorita

    def recorrer(self, kilometros):
        
        if self.autonomia <= kilometros: 
            msg = f"Anduve por {str(self.autonomia)}Km y gaste {str(self.energia)}L de bencina"
            self.energia = 0
            return msg
        else: 
            gasto = int(kilometros/self.rendimiento)
            self.energia -= gasto
            return f"Anduve por {str(kilometros)}Km y gaste {str(gasto)}L de bencina"


class AutoElectrico(Vehiculo):
    
    def __init__(self, vida_util_bateria = 0, *args, **kargs):
        super().__init__(*args, **kargs)
        self.vida_util_bateria = vida_util_bateria

    def recorrer(self, kilometros):
        if self.autonomia <= kilometros:
            msg = "Anduve por " + str(self.autonomia) + "Km y gaste " + str(self.energia) + "W de energia electrica"
            self.energia = 0
            return msg 
        else: 
            gasto = int(kilometros/self.rendimiento) 
            self.energia -= gasto
            msg = "Anduve por " + str(kilometros) + "Km y gaste " + str(gasto) + "W de energia electrica"
            return msg


class Camioneta(AutoBencina):

    def __init__(self, capacidad_maleta: int, *args, **kargs):
        super().__init__(*args, **kargs)
        self.capacidad_maleta = capacidad_maleta


class Telsa(AutoElectrico):
    
    def __init__(self, vida_util_bateria: int, *args, **kargs):
        super().__init__(vida_util_bateria, *args, **kargs)
        
    def recorrer(self, kilometros):
        return super().recorrer(kilometros) + " de forma inteligente"


class FaitHibrido(AutoBencina, AutoElectrico):
    vida_util_bateria = 5   

    def __init__(self, bencina_favorita: int, *args, **kargs):
        super().__init__(bencina_favorita, *args, **kargs)
        self.vida_util_bateria = FaitHibrido.vida_util_bateria

    def recorrer(self, kilometros):
        return AutoElectrico.recorrer(self, kilometros/2) + " " + AutoBencina.recorrer(self, kilometros/2)  

    
