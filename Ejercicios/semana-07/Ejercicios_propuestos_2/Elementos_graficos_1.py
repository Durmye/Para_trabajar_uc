import sys  # necesario para: 1. Debuggeo, 2. Mantener programa
from PyQt6.QtWidgets import QWidget, QApplication

class MiVentana(QWidget): 
    def __init__(self, x, y, ancho, alto, titulo) -> None:
        super().__init__()

        self.setGeometry(x, y, ancho, alto)
        self.setWindowTitle(titulo) 

if __name__ == "__main__": 
    def hook(type, value, traceback) -> None: 
        print(type)
        print(traceback)
    sys.__excepthook__ = hook

    pp = QApplication([])a

    #Antes de instanciar solicita variables

    x = int(input("Ingrese posicion x de inicio: "))
    y = int(input("Ingrese posicion y de inicio: "))
    ancho = int(input("Ingrese ancho de la ventana: "))
    largo = int(input("Ingrese largo de la ventana: "))
    string = str(input("Ingrese el titulo de la ventana: "))
    parametros = [x, y, ancho, largo, string]

    ventana = MiVentana(*parametros)
    ventana.show()
    sys.exit(app.exec())