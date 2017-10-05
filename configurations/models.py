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

    def setear_valores(self,dia,valores):
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
        self.horainicio = hora

    def set_horainicio(self,hora):
        self.horainicio = hora



class Vehiculo():
    placa = ''
    def __init__(self,placa):
        self.placa = placa

    def digito_placa(self):
        return int(self.placa[-1])


    def puede_circular(self,fecha,horario,configuracion):
        diasemana = fecha.strftime('%a')
        valores = configuracion.get_arreglo_por_dia(diasemana)
        horainicio = configuracion.get_horainicio()
        horafin = configuracion.get_horafin()

        if len(valores) and self.digito_placa() in valores and horario >= horainicio and horario <= horafin:
            return False
        else:
            return True

