class Monitor:

    contadorMonitores = 0

    def __init__(self, marca, tamaño):
        Monitor.contadorMonitores += 1
        self._idMonitor = Monitor.contadorMonitores
        self._marca = marca
        self._tamaño = tamaño

    def __str__(self):
        return f'Monitor [ID: {self._idMonitor}, tamaño: {self._tamaño}, marca: {self._marca}]'

    @property
    def idMonitor(self):
        return self._idMonitor

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

    @property
    def tamaño(self):
        return self._tamaño

    @tamaño.setter
    def tamaño(self, tamaño):
        self._tamaño = tamaño

if __name__ == "__main__":
    monitor1 = Monitor("Philips", 19)
    monitor2 = Monitor("Samsung", 52)

    monitor1.marca = "LG"
    monitor2.tamaño = 27

    print(monitor1)
    print(monitor2)