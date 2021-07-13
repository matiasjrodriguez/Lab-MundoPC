class DispositivoEntrada:
    def __init__(self, tipoEntrada, marca):
        self._tipoEntrada = tipoEntrada
        self._marca = marca

    def __str__(self):
        return f'Dispositivo Entrada[Tipo entrada: {self._tipoEntrada}, marca: {self._marca}]'

    @property
    def tipoEntrada(self):
        return self._tipoEntrada

    @tipoEntrada.setter
    def tipoEntrada(self, tipoEntrada):
        self._tipoEntrada = tipoEntrada

    @property
    def marca(self):
        return self._marca

    @marca.setter
    def marca(self, marca):
        self._marca = marca

if __name__ == "__main__":
    dispositivo1 = DispositivoEntrada("USB", "Razer")
    dispositivo2 = DispositivoEntrada("Wireless", "Redragon")
    
    dispositivo1.marca = "Logitech"
    dispositivo2.tipoEntrada = "USB"

    print(dispositivo1)
    print(dispositivo2)