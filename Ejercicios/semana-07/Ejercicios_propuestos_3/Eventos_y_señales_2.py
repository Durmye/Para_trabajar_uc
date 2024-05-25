import sys
import os # Imagenes
from random import randint
from PyQt6.QtGui import QPixmap, QMouseEvent
from PyQt6.QtWidgets import QApplication, QWidget, QLabel

class Cuadrado_Cambiante(QWidget): 
    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)
        self.gui()
        self.show()

    def gui(self) -> None: 

        # Varibales aleatorias
        x = randint(0, 450)
        y = randint(0, 450)
        
        # QLables = "QEtiquetas" 
        # Esta etiqueta en particular corresponde a una imagen
        self.imagen = QLabel(self)

        #Geometria 
        self.setGeometry(100, 100, 500, 500)
        self.imagen.setGeometry(x, y, 50, 50)
        
        #QPixmap
        ruta = os.path.join("img", "colors", "azul.png")
        imagen = QPixmap(ruta)
        self.imagen.setPixmap(imagen)
        self.imagen.setScaledContents(True)
    
    def mousePressEvent(self, event:QMouseEvent) -> None: 
        x = randint(0, 450)
        y = randint(0, 450)
        dentro_label = self.imagen.underMouse()
        if dentro_label: 
            self.imagen.move(x, y)
        

if __name__ == "__main__": 
    def hook(type, value, traceback) -> None: 
        print(type)
        print(traceback)
    sys.__excepthook__ = hook 

    app = QApplication([])
    epico = Cuadrado_Cambiante()
    sys.exit(app.exec())
    