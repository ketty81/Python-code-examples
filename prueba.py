__author__ = 'ketty'
from configurations.models import *


fecha = raw_input('Fecha formato dd-mm-aaaa:')
placa = raw_input('Placa de Vehiculo:')
horario = raw_input('Horario formato hh:mm:ss:')

configuracion = ConfiguracionPicoPlaca()
try:
    vehiculo = Vehiculo(placa)
except Exception as error:
    print(error)
    exit()

try:
    if vehiculo.puede_circular(fecha,horario,configuracion):
        print "Puede Circular"
    else:
        print("No puede circular")
except Exception as error:
    print(error)


