from PyQt6.QtWidgets import QLabel, QPushButton, QApplication, QWidget
from PyQt6.QtCore import QObject, pyqtSignal, Qt, QThread, QTimer, QMutex, QUrl
from PyQt6.QtGui import QKeyEvent, QMouseEvent, QPixmap, QGuiApplication
from PyQt6.QtMultimedia import QSoundEffect
from frontend.threads import ThreadMovimiento, ThreadInteraccion, ThreadSandia
import frontend.funciones as aux
import frontend.constantes as c
from os.path import join
from random import randint
import sys

class Sandia(QLabel):
    
    senal_click_sandia = pyqtSignal()

    def __init__(self) -> QLabel:
        super().__init__()
    
    def mousePressEvent(self, event: QMouseEvent | None) -> None:
        if event.button() == Qt.MouseButton.LeftButton:
            self.senal_click_sandia.emit(self.id)

class VentanaJuego(QWidget): 

    senal_cerrar_ventana = pyqtSignal()
    senal_verificar = pyqtSignal()
    senal_movimiento_pepa = pyqtSignal(int, int)
    senal_interaccion_casilla = pyqtSignal(int, int)

    def __init__(self, nombre_puzzle) -> None: 
        
        #Atribuos de la clase
        super().__init__()
        self.pausa = False
        self.tiempo_terminado = False
        self.posicion_pepa = [0, 0]
        self.thread_movimiento = None
        self.thread_interaccion = None

        #Agregar geometria de la ventana utilizando resolucion adapatable 
        r_s = QGuiApplication.primaryScreen().geometry()
        ancho = int(r_s.width()/2)
        largo = int(r_s.height()/2)
        self.setGeometry(100, 100, ancho, largo)
        ## Elementos de la ventana

        self.setWindowTitle("Puzzle")

        #Puzzle 
        puzzle = aux.leer_base(nombre_puzzle)

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
            #print(posicion[0], posicion[1])
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
                casilla_pixmap = QPixmap("frontend/sprites/lechuga.png")
                casilla.setPixmap(casilla_pixmap)
                self.casillas.append(casilla)
                self.puzzle.append(casilla)

        # Pepa
        self.pepa = QLabel(self)
        self.pepa.setGeometry(max_hint_fila*intervalo_x, max_hint_columna*intervalo_y, intervalo_x, intervalo_y)
        self.pepa.setAlignment(Qt.AlignmentFlag.AlignCenter)
        pepa_pixmap = QPixmap("frontend/sprites/pepa/down_0.png")
        self.pepa.setPixmap(pepa_pixmap)

        # Sandia
        self.sandia = self.instanciar_sandia(self.dimension, self.casillas, self.intervalo_x, self.intervalo_y)
        
        
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
        self.tiempo_restante = QLabel(f"{c.TIEMPO_JUEGO}", self)
        self.tiempo_restante.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tiempo_restante.setGeometry(ancho-100, 0, 100, largo_botones)

        self.timer_tiempo_restante = QTimer(self)
        self.timer_tiempo_restante.timeout.connect(self.actualizar_tiempo)
        self.timer_tiempo_restante.setInterval(1000)
        self.timer_tiempo_restante.start()

        # Musica 
        self.media_player = QSoundEffect(self)
        path_musica = QUrl.fromLocalFile(join("frontend", "sonidos", "musica_1.wav"))
        self.media_player.setSource(path_musica)
        self.media_player.play()
    
    ## Funcion pepa. Movimiento e interactuar con mapa 
    def keyPressEvent(self, event:QKeyEvent) -> None: 

        #Instancia Thread
        if self.thread_movimiento is None or not self.thread_movimiento.isRunning() \
        and event.text() in "wasd" and not self.pausa:
            self.thread_movimiento = ThreadMovimiento(direccion = event.text(),
                                                      pepa = self.pepa,
                                                      intervalo_x = self.intervalo_x,
                                                      intervalo_y = self.intervalo_y,
                                                      )

            #Moverse hacia arriba, revisa que no salga del mapa
            if event.text() == "w" and self.posicion_pepa[1] != 0:
                self.thread_movimiento.start()
                self.posicion_pepa[1] = self.posicion_pepa[1] - 1
                print(self.posicion_pepa)
                self.senal_movimiento_pepa.emit(self.posicion_pepa[0], self.posicion_pepa[1])

            #Moverse hacia abajo, revisa que no salga del mapa
            elif event.text() == "s" and self.posicion_pepa[1] != self.dimension - 1: 
                self.thread_movimiento.start()
                self.posicion_pepa[1] = self.posicion_pepa[1] + 1
                print(self.posicion_pepa)
                self.senal_movimiento_pepa.emit(self.posicion_pepa[0], self.posicion_pepa[1])

            #Moverse hacia la izquierda, revisa que no salga del mapa
            elif event.text() == "a" and self.posicion_pepa[0] != 0:
                self.thread_movimiento.start()
                self.posicion_pepa[0] = self.posicion_pepa[0] - 1
                print(self.posicion_pepa)
                self.senal_movimiento_pepa.emit(self.posicion_pepa[0], self.posicion_pepa[1])

            #Moverse hacia la derecha, revisa que no salga del mapa 
            elif event.text() == "d" and self.posicion_pepa[0] != self.dimension - 1: 
                self.thread_movimiento.start()
                self.posicion_pepa[0] = self.posicion_pepa[0] + 1
                print(self.posicion_pepa)
                self.senal_movimiento_pepa.emit(self.posicion_pepa[0], self.posicion_pepa[1])

        #Interactuar con la casilla en la que se esta.
        elif event.text() == "g" and not self.pausa: 
            casilla = self.casillas[(self.posicion_pepa[1] * self.dimension) + self.posicion_pepa[0]]
            if self.pepa.x() == casilla.x() and self.pepa.y() == casilla.y(): 
                if self.thread_interaccion is None or not self.thread_movimiento.isRunning():
                    self.thread_interaccion = ThreadInteraccion(casilla,
                                                                self.senal_interaccion_casilla)
                    self.thread_interaccion.start()
                    self.senal_interaccion_casilla.emit(self.posicion_pepa[0], self.posicion_pepa[1])

    ## Funcion sandia.
    def instanciar_sandia(self, dimension: int, casillas: list, intervalo_x: int, intervalo_y: int) -> QLabel:
        #Retorna una instancia de sandia en una posicion aleatoria
        sandia_x = randint(0, dimension - 1) 
        sandia_y = randint(0, dimension - 1)

        casilla_aparicion = casillas[(sandia_x * dimension) + sandia_y]
        origen_x = casilla_aparicion.x()
        origen_y = casilla_aparicion.y()

        sandia = Sandia()
        sandia.senal_click_sandia.connect(self.sandia_clickeada)
        sandia.setGeometry(origen_x, origen_y, intervalo_x, intervalo_y)
        sandia.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sandia_pixmap = QPixmap("sprites/sandia.png")
        sandia.setPixmap(sandia_pixmap)
        return sandia

    def sandia_clickeada(self):
        self.sandia.hide()
        self.mover_sandia()
        self.tiempo_restante.setText(f"{int(int(self.tiempo_restante.text()) + {c.TIEMPO_ADICIONAL})}")

    def mover_sandia(self) -> None:
        sandia_x = randint(0, self.dimension - 1) 
        sandia_y = randint(0, self.dimension - 1)
        self.sandia.move(sandia_x, sandia_y)

    ## Funciones Botones
    def salir(self): 
        self.media_player.stop()
        self.senal_cerrar_ventana.emit()
        #self.senal_cerrar_ventana.emit()

    def pausar(self):
        if not self.pausa: 
            self.pausa = True
            for elemento in self.puzzle: 
                elemento.hide()
            self.pepa.hide()
            self.timer_tiempo_restante.stop()
            self.media_player.stop()
        else: 
            self.pausa = False
            for elemento in self.puzzle:
                elemento.show()
            self.pepa.show()
            self.timer_tiempo_restante.start()
            self.media_player.play()

    def verificar(self): 
        self.senal_verificar.emit()

    ## Funcion timepo
    def actualizar_tiempo(self): 
        tiempo_actual = int(self.tiempo_restante.text()) - 1
        self.tiempo_restante.setText(str(tiempo_actual))


