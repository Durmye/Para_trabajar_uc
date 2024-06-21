from PyQt6.QtWidgets import QLabel, QPushButton, QApplication, QWidget
from PyQt6.QtCore import QObject, pyqtSignal, Qt, QThread
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QPixmap, QGuiApplication, QColor
import funciones as aux
import sys
import os
import constantes as c
import time

class ThreadMovimiento(QThread):

    def __init__(self, direccion: str, pepa: QLabel, intervalo_x: int, intervalo_y: int, senal_thread) -> None:
        super().__init__()
        self.direccion = direccion
        self.pepa = pepa
        self.intervalo_x = intervalo_x
        self.intervalo_y = intervalo_y 
        self.senal_thread = senal_thread

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
            sprite_0 = QPixmap("sprites/pepa/up_0.png")
            sprite_1 = QPixmap("sprites/pepa/up_1.png")
            sprite_2 = QPixmap("sprites/pepa/up_2.png")
            sprite_3 = QPixmap("sprites/pepa/up_3.png")
            mov_x = 0
            mov_y = - int(self.intervalo_y/4)
            resto_x = 0
            resto_y = - self.resto_y 

        elif self.direccion == "s": 
            sprite_0 = QPixmap("sprites/pepa/down_0.png")
            sprite_1 = QPixmap("sprites/pepa/down_1.png")
            sprite_2 = QPixmap("sprites/pepa/down_2.png")
            sprite_3 = QPixmap("sprites/pepa/down_3.png")
            mov_x = 0
            mov_y = int(self.intervalo_y/4)
            resto_x = 0
            resto_y = self.resto_y 

        elif self.direccion == "a": 
            sprite_0 = QPixmap("sprites/pepa/left_0.png")
            sprite_1 = QPixmap("sprites/pepa/left_1.png")
            sprite_2 = QPixmap("sprites/pepa/left_2.png")
            sprite_3 = QPixmap("sprites/pepa/left_3.png")
            mov_x = - int(self.intervalo_x/4)
            mov_y = 0
            resto_x = - self.resto_x
            resto_y = 0

        elif self.direccion == "d": 
            sprite_0 = QPixmap("sprites/pepa/right_0.png")
            sprite_1 = QPixmap("sprites/pepa/right_1.png")
            sprite_2 = QPixmap("sprites/pepa/right_2.png")
            sprite_3 = QPixmap("sprites/pepa/right_3.png")
            mov_x = int(self.intervalo_x/4)
            mov_y = 0
            resto_x = self.resto_x
            resto_y = 0

        self.pepa.move(self.pepa.x() + mov_x, self.pepa.y() + mov_y)
        self.pepa.setPixmap(sprite_1)
        time.sleep(0.15)

        self.pepa.move(self.pepa.x() + mov_x, self.pepa.y() + mov_y)
        self.pepa.setPixmap(sprite_2)
        time.sleep(0.15)

        self.pepa.move(self.pepa.x() + mov_x, self.pepa.y() + mov_y)
        self.pepa.setPixmap(sprite_3)
        time.sleep(0.15)
        
        self.pepa.move(self.pepa.x() + mov_x + resto_x, self.pepa.y() + mov_y + resto_y)
        self.pepa.setPixmap(sprite_0)      

        self.senal_thread.emit(self.direccion)

class VentanaJuego(QWidget): 

    senal_cerrar_ventana = pyqtSignal()
    senal_verificar = pyqtSignal()
    senal_movimiento_pepa = pyqtSignal(str)

    def __init__(self) -> None: 
        
        #Atribuos de la clase
        super().__init__()
        self.pausa = False
        self.posicion_pepa = [0, 0]
        self.thread_movimiento = None

        #Agregar geometria de la ventana utilizando resolucion adapatable 
        r_s = QGuiApplication.primaryScreen().geometry()
        ancho = int(r_s.width()/2)
        largo = int(r_s.height()/2)
        self.setGeometry(100, 100, ancho, largo)
        ## Elementos de la ventana

        self.setWindowTitle("Puzzle")

        #Puzzle 
        
        puzzle = aux.leer_base("novato_1")

        dimension = aux.dimension_grilla(puzzle)
        columnas = aux.obtener_columnas(puzzle)
        filas = aux.obtener_filas(puzzle)
        max_hint_columna = aux.obtener_max_columna(columnas)
        max_hint_fila = aux.obtener_max_fila(filas)

        intervalo_x = int((ancho-100)/(dimension + max_hint_fila))
        intervalo_y = int((largo)/(dimension + max_hint_columna))

        self.dimension = dimension
        self.intervalo_x = intervalo_x
        self.intervalo_y = intervalo_y
        self.casillas = []
        self.puzzle = []

        print(intervalo_x, intervalo_y)

        #print(f"puzzle: {puzzle}")
        #print(f"dimension: {dimension}")
        #print(f"columnas: {columnas}")
        #print(f"filas: {filas}")
        #print(f"max_hint_columna: {max_hint_columna}")
        #print(f"max_hint_filas: {max_hint_fila}")

        posiciones = [(i, j) for i in range(dimension + max_hint_columna)
                      for j in range(dimension + max_hint_fila)]
        
        for posicion in posiciones:
            print(posicion[0], posicion[1])
            # Revisa que no inicie informacion dentro de cuadrado superior izquierdo
            if posicion[1] < max_hint_fila and posicion[0] < max_hint_columna: 
                pass
            # Revisa inicio de hints de columnas
            elif posicion[1] >= max_hint_fila and posicion[0] < max_hint_columna: 
                # Revisa que no se exceda indice max de la lista 
                if len(columnas[posicion[1] - max_hint_fila]) > posicion[0]: 
                    hint = QLabel(columnas[posicion[1] - max_hint_fila][posicion[0]], self)
                    hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    hint.setGeometry(posicion[1]*intervalo_x, posicion[0]*intervalo_y, intervalo_x, intervalo_y)
                    self.puzzle.append(hint)
            # Revisa inicio de hints de filas 
            elif posicion[1] < max_hint_fila and posicion[0] >= max_hint_columna:
                #Revisa que no se exceda indice max de la lista 
                if len(filas[posicion[0] - max_hint_columna]) > posicion[1]: 
                    hint = QLabel(filas[posicion[0] - max_hint_columna][posicion[1]], self)
                    hint.setAlignment(Qt.AlignmentFlag.AlignCenter)
                    hint.setGeometry(posicion[1]*intervalo_x, posicion[0]*intervalo_y, intervalo_x, intervalo_y)
                    self.puzzle.append(hint)
            # Revisa inicio del mapa.
            elif posicion[1] >= max_hint_fila and posicion[0] >= max_hint_columna: 
                casilla = QLabel(self)
                casilla.setGeometry(posicion[1]*intervalo_x, posicion[0]*intervalo_y, intervalo_x, intervalo_y)
                casilla.setAlignment(Qt.AlignmentFlag.AlignCenter)
                casilla_pixmap = QPixmap("sprites/lechuga.png")
                casilla.setPixmap(casilla_pixmap)
                self.casillas.append(casilla)
                self.puzzle.append(casilla)

        # Pepa
        self.pepa = QLabel(self)
        self.pepa.setGeometry(max_hint_fila*intervalo_x, max_hint_columna*intervalo_y, intervalo_x, intervalo_y)
        self.pepa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pepa_pixmap = QPixmap("sprites/pepa/down_0.png")
        self.pepa.setPixmap(pepa_pixmap)
        
        # Botones 

        largo_botones = int(largo/4)

        self.boton_verificar = QPushButton("Verificar", self)
        self.boton_verificar.setGeometry(ancho-100, largo_botones, 100, largo_botones)
        self.boton_verificar.clicked.connect(self.verificar)

        self.boton_pausa = QPushButton("Pausa", self)
        self.boton_pausa.setGeometry(ancho-100, largo_botones*2, 100, largo_botones)
        self.boton_pausa.clicked.connect(self.pausar)

        self.boton_salir = QPushButton("Salir", self)
        self.boton_salir.setGeometry(ancho-100, largo_botones*3, 100, largo_botones)
        self.boton_salir.clicked.connect(self.salir)

        # Tiempo restante
        self.tiempo_restante = QLabel(f"{c.TIEMPO_DURACION}", self)
        self.tiempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tiempo_restante.setGeometry(ancho-100, 0, 100, largo_botones)

        self.show()
    
    def keyPressEvent(self, event:QKeyEvent) -> None: 

        #Instancia Thread
        if self.thread_movimiento is None or not self.thread_movimiento.isRunning() \
        and event.text() in "wasd" and not self.pausa:
            self.thread_movimiento = ThreadMovimiento(direccion = event.text(),
                                                      pepa = self.pepa,
                                                      intervalo_x = self.intervalo_x,
                                                      intervalo_y = self.intervalo_y,
                                                      senal_thread= self.senal_movimiento_pepa)

            #Moverse hacia arriba, revisa que no salga del mapa
            if event.text() == "w" and self.posicion_pepa[1] != 0:
                self.thread_movimiento.start()
                self.posicion_pepa[1] = self.posicion_pepa[1] - 1
                print(self.posicion_pepa)

            #Moverse hacia abajo, revisa que no salga del mapa
            elif event.text() == "s" and self.posicion_pepa[1] != self.dimension - 1: 
                self.thread_movimiento.start()
                self.posicion_pepa[1] = self.posicion_pepa[1] + 1
                print(self.posicion_pepa)

            #Moverse hacia la izquierda, revisa que no salga del mapa
            elif event.text() == "a" and self.posicion_pepa[0] != 0:
                self.thread_movimiento.start()
                self.posicion_pepa[0] = self.posicion_pepa[0] - 1
                print(self.posicion_pepa)

            #Moverse hacia la derecha, revisa que no salga del mapa 
            elif event.text() == "d" and self.posicion_pepa[0] != self.dimension - 1: 
                self.thread_movimiento.start()
                self.posicion_pepa[0] = self.posicion_pepa[0] + 1
                print(self.posicion_pepa)

        #Interactuar con la casilla en la que se esta.
        elif event.text() == "g" and not self.pausa: 
            pass


    def mousePressEvent(self, event:QMouseEvent):
        pass


    def salir(self): 
        sys.exit(app.exec())
        #self.senal_cerrar_ventana.emit()

    def pausar(self):
        if not self.pausa: 
            self.pausa = True
            for elemento in self.puzzle: 
                elemento.hide()
            self.pepa.hide()
        else: 
            self.pausa = False
            for elemento in self.puzzle:
                elemento.show()
            self.pepa.show()

    def verificar(self): 
        self.senal_verificar.emit()
    


    '''
    Pepa:
        Movimiento de pepa dado por: WASD
        Interaccion con casillas dado por: G
        Interaccion con sandias dado por: click
    CheatCodes: 
        I + N + F = tiempo infinito, setea puntaje a PUNTAJE_INF
        M + U + T + E = Desactiva el uso de todos los sonidos durante
                        la partida acutal 
    
    '''

if __name__ == "__main__":
    def hook(type_, value, traceback): 
        print(type_)
        print(traceback)
    sys.__excepthook__ = hook

    app = QApplication([])
    juego = VentanaJuego()
    sys.exit(app.exec())