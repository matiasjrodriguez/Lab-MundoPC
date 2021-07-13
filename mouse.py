from dispositivo_entrada import DispositivoEntrada

class Mouse(DispositivoEntrada):

    contadorMouse = 0

    def __init__(self, tipoEntrada, marca):
        Mouse.contadorMouse += 1
        self._idMouse = Mouse.contadorMouse
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Mouse [ID: {self._idMouse}, tipo entrada: {self._tipoEntrada}, marca: {self._marca}]'

    @property
    def idMouse(self):
        return self._idMouse


if __name__ == "__main__":
    mouse1 = Mouse("USB", "Razer")
    mouse2 = Mouse("Wireless", "Redragon")

    mouse1.marca = "Logitech"
    mouse2.tipoEntrada = "USB"

    print(mouse1)
    print(mouse2)