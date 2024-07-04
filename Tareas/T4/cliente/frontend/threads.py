from PyQt6.QtWidgets import QLabel
from PyQt6.QtCore import QThread, pyqtSignal, QTimer, QUrl
from PyQt6.QtGui import QPixmap
from PyQt6.QtMultimedia import QSoundEffect
from frontend.constantes import TIEMPO_DURACION, TIEMPO_APARICION, TIEMPO_TRANSICION
from os.path import join 
from time import sleep
from random import randint




class ThreadMovimiento(QThread):

    def __init__(self, direccion: str, pepa: QLabel, intervalo_x: int, intervalo_y: int) -> None:
        super().__init__()
        self.direccion = direccion
        self.pepa = pepa
        self.intervalo_x = intervalo_x
        self.intervalo_y = intervalo_y 

        if self.intervalo_x % 4 != 0: 
            self.resto_x = self.intervalo_x % 4
        else: 
            self.resto_x = 0
        
        if self.intervalo_y % 4 != 0: 
            self.resto_y = self.intervalo_y % 4
        else: 
            self.resto_y = 0

    def run(self) -> None: 

        if self.direccion == "w": 
            sprite_0 = QPixmap("frontend/sprites/pepa/up_0.png")
            sprite_1 = QPixmap("frontend/sprites/pepa/up_1.png")
            sprite_2 = QPixmap("frontend/sprites/pepa/up_2.png")
            sprite_3 = QPixmap("frontend/sprites/pepa/up_3.png")
            mov_x = 0
            mov_y = - int(self.intervalo_y/4)
            resto_x = 0
            resto_y = - self.resto_y 

        elif self.direccion == "s": 
            sprite_0 = QPixmap("frontend/sprites/pepa/down_0.png")
            sprite_1 = QPixmap("frontend/sprites/pepa/down_1.png")
            sprite_2 = QPixmap("frontend/sprites/pepa/down_2.png")
            sprite_3 = QPixmap("frontend/sprites/pepa/down_3.png")
            mov_x = 0
            mov_y = int(self.intervalo_y/4)
            resto_x = 0
            resto_y = self.resto_y 

        elif self.direccion == "a": 
            sprite_0 = QPixmap("frontend/sprites/pepa/left_0.png")
            sprite_1 = QPixmap("frontend/sprites/pepa/left_1.png")
            sprite_2 = QPixmap("frontend/sprites/pepa/left_2.png")
            sprite_3 = QPixmap("frontend/sprites/pepa/left_3.png")
            mov_x = - int(self.intervalo_x/4)
            mov_y = 0
            resto_x = - self.resto_x
            resto_y = 0

        elif self.direccion == "d": 
            sprite_0 = QPixmap("frontend/sprites/pepa/right_0.png")
            sprite_1 = QPixmap("frontend/sprites/pepa/right_1.png")
            sprite_2 = QPixmap("frontend/sprites/pepa/right_2.png")
            sprite_3 = QPixmap("frontend/sprites/pepa/right_3.png")
            mov_x = int(self.intervalo_x/4)
            mov_y = 0
            resto_x = self.resto_x
            resto_y = 0

        self.pepa.move(self.pepa.x() + mov_x, self.pepa.y() + mov_y)
        self.pepa.setPixmap(sprite_1)
        sleep(0.15)

        self.pepa.move(self.pepa.x() + mov_x, self.pepa.y() + mov_y)
        self.pepa.setPixmap(sprite_2)
        sleep(0.15)

        self.pepa.move(self.pepa.x() + mov_x, self.pepa.y() + mov_y)
        self.pepa.setPixmap(sprite_3)
        sleep(0.15)
        
        self.pepa.move(self.pepa.x() + mov_x + resto_x, self.pepa.y() + mov_y + resto_y)
        self.pepa.setPixmap(sprite_0)      


class ThreadInteraccion(QThread): 
    def __init__(self, casilla: QLabel, senal_cambio_casilla: pyqtSignal) -> None:
        super().__init__()
        self.casilla = casilla

    def run(self) -> None: 
        self.media_player = QSoundEffect(self)
        if self.casilla.pixmap().isNull(): 
            
            #Musica 
            path_musica = QUrl.fromLocalFile(join("frontend", "sonidos", "poop.wav"))
            self.media_player.setSource(path_musica)
            self.media_player.play()
            
            # Accion
            poop_pixmap = QPixmap("frontend/sprites/poop.png")
            self.casilla.setPixmap(poop_pixmap)
            sleep(TIEMPO_TRANSICION)
            lechuga_pixmap = QPixmap("frontend/sprites/lechuga.png")
            self.casilla.setPixmap(lechuga_pixmap)

        else:

            #Musica 
            path_musica = QUrl.fromLocalFile(join("frontend", "sonidos", "comer.wav"))
            self.media_player.setSource(path_musica)
            self.media_player.play()

            #Accion
            self.casilla.clear()

class ThreadSandia(QThread): 
    def __init__(self, dimension: int, sandia: QLabel) -> None:
        super().__init__()
        self.sandia = sandia
        self.dimension = dimension

    def run(self): 
        self.timer_sandia = QTimer()
        self.timer_sandia.setInterval(TIEMPO_APARICION * 1000)
        self.timer_sandia.timeout.connect(self.funcion_timer)
        self.timer_sandia.start()
        print(self.timer_sandia.isActive())

    # Timer se encarga de hacer aparecer y desaparecer sandias en funcion de las constantes de tiempo. 
    def funcion_timer(self) -> None:
        
        self.sandia.raise_()
        print("alo? mostrar")
        self.timer_sandia.sleep(TIEMPO_DURACION)
        print("Alo esconder? ")
        self.sandia.hide()
        self.mover_sandia(self.sandia)

    def mover_sandia(self, sandia: None | QLabel) -> None:
        sandia_x = randint(0, self.dimension) 
        sandia_y = randint(0, self.dimension)
        sandia.move(sandia_x, sandia_y)

class TimerTiempo(QTimer): 
    def __init__(self): 
        super().__init__()

    