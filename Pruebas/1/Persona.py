import Arcade

class Persona: 
    def __init__(self, nickname):
        self.nickname = nickname

    def encender_arcade(self, arcade):
        arcade.encendido = True

    def jugar_arcade(self, Arcade, juego): 
