import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QPushButton,
                             QLabel, QHBoxLayout, QVBoxLayout)
from PyQt6.QtCore import QCoreApplication

class Cuenta_Clicks(QWidget):
    
    def __init__(self, *args, **kawrgs) -> None: 
        super().__init__(*args, **kawrgs)
        self.init_gui()
        self.contador = 0

    def init_gui(self) -> None:

        #Label 
        self.label = QLabel("0 clicks", self)
        
        #Button 
        self.boton = QPushButton("clickeame!", self)
        self.boton.clicked.connect(self.boton_clickeado)

        #Geometria
        self.setGeometry(100, 100, 400, 100)
        self.label.resize(100, 20)
        self.boton.resize(self.boton.sizeHint())
    
        #Grid 
        hgrid1 = QHBoxLayout()
        #hgrid2 = QHBoxLayout()
        hgrid1.addStretch(1)
        hgrid1.addWidget(self.label)
        hgrid1.addWidget(self.boton)
        hgrid1.addStretch(1)
        self.setLayout(hgrid1)
        #hgrid2.addWidget(self.boton)
        #vgrid.addLayout(hgrid2)
        
        #show
        self.show()

    def boton_clickeado(self) -> None:
        self.contador += 1
        self.label.setText(f"{self.contador} clicks")

if __name__ == "__main__": 
    def hook(type, value, traceback) -> None: 
        print(type)
        print(traceback)

    sys.__excepthook__ = hook 

    app = QApplication([])
    ventana = Cuenta_Clicks()
    sys.exit(app.exec())

