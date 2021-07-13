from dispositivo_entrada import DispositivoEntrada

class Teclado(DispositivoEntrada):

    contadorTeclado = 0

    def __init__(self, tipoEntrada, marca):
        Teclado.contadorTeclado += 1
        self._idTeclado = Teclado.contadorTeclado
        super().__init__(tipoEntrada, marca)

    def __str__(self):
        return f'Teclado [ID: {self._idTeclado}, tipo entrada: {self._tipoEntrada}, marca: {self._marca}]'

    @property
    def idTeclado(self):
        return self._idTeclado


if __name__ == "__main__":
    teclado1 = Teclado("USB", "Razer")
    teclado2 = Teclado("Wireless", "Redragon")

    teclado1.marca = "Logitech"
    teclado2.tipoEntrada = "USB"

    print(teclado1)
    print(teclado2)