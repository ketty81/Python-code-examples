__author__ = 'ketty'

import datetime,locale
locale.setlocale(locale.LC_ALL,'Spanish_Spain.1252')

class ConfiguracionPicoPlaca():

    arreglo_dias = {}
    horainicio = datetime.datetime
    horafin = datetime.datetime

    def __init__(self):
        self.arreglo_dias = {
            'lu.':[1,2],
            'ma.':[3,4],
            'mi.':[5,6],
            'ju.':[7,8],
            'vi.':[9,0],
            'sa.':[],
            'do.':[]
        }
        self.horainicio = datetime.datetime.strptime('07:00:00','%H:%M:%S')
        self.horafin = datetime.datetime.strptime('09:00:00','%H:%M:%S')

    def setear_valores_dia(self,dia,valores):
        if not isinstance(valores, list):
            raise ValueError("La funcion recibe un arreglo de valores enteros")
        else:
            for valor in valores:
                try:
                    valor = int(valor)
                except ValueError:
                    raise ValueError("Los valores a asignar deben ser enteros")

        if not self.arreglo_dias.has_key(dia):
            raise ValueError("El dia ingresado no existe en el listado de dias permitidos")
        else:
            self.arreglo_dias[dia] = valores


    def get_arreglo_dias(self):
        return self.arreglo_dias

    def get_arreglo_por_dia(self,dia):
        return self.arreglo_dias[dia]

    def get_horainicio(self):
        return self.horainicio

    def get_horafin(self):
        return self.horafin

    def set_horainicio(self,hora):
        try:
            self.horainicio = datetime.datetime.strptime(hora,'%H:%M:%S')
        except:
            raise ValueError("El formato del horario no es correcto")

    def set_horafin(self,hora):
        try:
            self.horafin = datetime.datetime.strptime(hora,'%H:%M:%S')
        except:
            raise ValueError("El formato del horario no es correcto")




class Vehiculo():
    placa = ''
    def __init__(self,placa):
        try:
            dig = int(placa[-1])
            self.placa = placa
        except:
            raise ValueError("El ultimo digito de la placa no es numerico")

    def digito_placa(self):
        return int(self.placa[-1])

    def puede_circular(self,fecha,horario,configuracion):
        try:
            fecha = datetime.datetime.strptime(fecha,'%d-%m-%Y')
        except:
             raise ValueError("El formato de fecha no es correcto")

        try:
            horario = datetime.datetime.strptime(horario,'%H:%M:%S')
        except:
            raise ValueError("El formato del horario no es correcto")

        diasemana = fecha.strftime('%a')
        valores = configuracion.get_arreglo_por_dia(diasemana)
        horainicio = configuracion.get_horainicio()
        horafin = configuracion.get_horafin()

        if len(valores) and self.digito_placa() in valores and horario >= horainicio and horario <= horafin:
            return False
        else:
            return True

