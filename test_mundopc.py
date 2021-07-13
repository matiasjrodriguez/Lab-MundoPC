from monitor import Monitor
from teclado import Teclado
from mouse import Mouse
from computadora import Computadora
from orden import Orden

monitor1 = Monitor("LG", 19)
monitor2 = Monitor("Samsung", 27)
teclado1 = Teclado("USB", "Logitech")
teclado2 = Teclado("USB", "Redragon")
mouse1 = Mouse("USB", "Logitech")
mouse2 = Mouse("USB", "Redragon")

computadora1 = Computadora("Office", monitor1, teclado1, mouse1)
computadora2 = Computadora("Gamer", monitor2, teclado2, mouse2)

computadoras1 = [computadora1, computadora2]
computadoras2 = [computadora1]

orden1 = Orden(computadoras1)
orden2 = Orden(computadoras2)
print(orden1)
print(orden2)