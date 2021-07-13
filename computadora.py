from mouse import Mouse
from teclado import Teclado
from monitor import Monitor

class Computadora(Mouse, Teclado, Monitor):

    contadorComputadoras = 0

    def __init__(self, nombre, monitor, teclado, mouse):
        Computadora.contadorComputadoras += 1
        self._idComputadora = Computadora.contadorComputadoras
        self._nombre = nombre
        self._monitor = monitor
        self._teclado = teclado
        self._mouse = mouse

    def __str__(self):
        return f'''
        Computadora: {self._nombre}
        Id: {self._idComputadora}
        {self._monitor}
        {self._teclado}
        {self._mouse}
        '''

    @property
    def idComputadora(self):
        return self._idComputadora

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def monitor(self):
        return self._monitor

    @monitor.setter
    def monitor(self, monitor):
        self._monitor = monitor

    @property
    def teclado(self):
        return self._teclado

    @teclado.setter
    def teclado(self, teclado):
        self._teclado = teclado

    @property
    def mouse(self):
        return self._mouse

    @mouse.setter
    def mouse(self, mouse):
        self._mouse = mouse

if __name__ == "__main__":
    monitor1 = Monitor("LG", 19)
    monitor2 = Monitor("Samsung", 27)
    teclado1 = Teclado("USB", "Logitech")
    teclado2 = Teclado("USB", "Redragon")
    mouse1 = Mouse("USB", "Logitech")
    mouse2 = Mouse("USB", "Redragon")

    computadora1 = Computadora("Office", monitor1, teclado1, mouse1)
    computadora2 = Computadora("Gamer", monitor2, teclado2, mouse2)

    print(computadora1)
    print(computadora2)