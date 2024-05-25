#Problema solucionado, explicación en lineas 15-19

class Guerrero:
    def __init__(self, vida,
                 mana, nivel) -> None:
        
        self._vida = vida
        self._mana = mana 
        self._nivel = nivel


    @property
    def vida(self):
        
        #En teoria la primera linea del getter llama al setter asegurandose de que este contenga inicialmente un valor valido.
        #La duda es si se llamarian de manera infita el setter y el getter

        #self.vida = self.vida  -> da error con recursion infinita
        #self.vida = self._vida -> soluciona el error llamando unicamente al setter antes de retornar el valor
        self.vida = self._vida
        return self._vida
    @vida.setter
    def vida(self, p):
        if p > 100: 
            self._vida = 100
        elif p < 0: 
            self._vida = 0
        else: 
            self._vida = p

erreh = Guerrero(120, 200, 1)
print(f"La vida de erreh es de: {erreh.vida}")