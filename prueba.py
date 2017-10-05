__author__ = 'ketty'
from configurations.models import *


fecha = raw_input('Fecha formato dd-mm-aaaa:')
placa = raw_input('Placa de Vehiculo:')
horario = raw_input('Horario formato hh:mm:ss:')

errores = []
try:
    fecha = datetime.datetime.strptime(fecha,'%d-%m-%Y')
except:
    errores.append("El formato de fecha no es correcto")

try:
    horario = datetime.datetime.strptime(horario,'%H:%M:%S')
except:
    errores.append("El formato del horario no es correcto")

try:
    dig = int(placa[-1])
except:
    errores.append("El ultimo digito de la placa no es numerico")


if len(errores):
    print(','.join(errores))
else:
    configuracion = ConfiguracionPicoPlaca()
    vehiculo = Vehiculo(placa)
    if vehiculo.puede_circular(fecha,horario,configuracion):
        print "Puede Circular"
    else:
        print("No puede circular")

