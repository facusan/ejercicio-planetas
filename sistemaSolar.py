import math
from enum import IntEnum
from enviroment import FECHA_INICIAL

class SentidoOrbita(IntEnum):
    HORARIO = -1
    ANTIHORARIO = 1

class Planeta():
    def __init__(self, nombre, x, y, velocidad, sentidoOrbita,radio):
        self.nombre = nombre
        self.x = x
        self.y = y
        self.radio = radio
        self.velocidad = velocidad
        self.sentidoOrbita = sentidoOrbita
        
    def avanzar_posicion(self, dias):
        self.x = int(self.radio * ( math.cos((math.pi / 180) * dias * self.velocidad * int(self.sentidoOrbita))))
        self.y = int(self.radio * ( math.sin((math.pi / 180) * dias * self.velocidad * int(self.sentidoOrbita))))
        #print(self.nombre + ' (x:' + str(self.x) + ', y:' + str(self.y)+')')
                
class SistemaSolar():
    def __init__(self,planetas,posicion_sol):
        self.planetas = planetas
        self.posicion_sol = posicion_sol

    def avanzar_posiciones(self, dias):
        for planeta in self.planetas:
            planeta.avanzar_posicion(dias)

