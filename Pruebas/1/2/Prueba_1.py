class Variable: 
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @valor.setter
    def valor(self, x):
        if x <= 0:
            self._valor = x
        else:
            self._valor = -x

variable_uno = Variable(5)

print(variable_uno.valor)

variable_uno.valor -= 3

print(variable_uno.valor)

variable_uno.valor = -1

print(variable_uno.valor)

variable_uno.valor += 3

print(variable_uno.valor)
