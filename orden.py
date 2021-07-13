class Orden:
    
    contadorOrdenes = 0

    def __init__(self, computadoras):
        Orden.contadorOrdenes += 1
        self._idOrden = Orden.contadorOrdenes
        self._computadoras = computadoras

    def agregarComputadora(self, computadora):
        self._computadoras.append(computadora)

    def __str__(self):
        strComputadoras = ''
        for computadora in self._computadoras:
            strComputadoras += computadora.__str__()

        return f'''
        Orden: {self._idOrden}
        Computadoras: {strComputadoras}
        '''