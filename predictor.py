import csv
import matplotlib.path as mpltPath
from enviroment import FECHA_INICIAL, AREA_MAXIMA
from datetime import timedelta
from enum import Enum

class Clima(Enum):
    SEQUIA = 'SEQUIA'
    CONDICIONES_OPTIMAS = 'CONDICIONESOPTIMAS'
    LLUVIA_INTESA = 'LLUVIA INTESA'
    LLUVIA = 'LLUVIA'
    SIN_PRONOSTICO = 'SIN PRONOSTICO'

class Predictor:
    def punto_dentro_de_triangulo(self, posiciones_planetas, punto):
        #posiciones = list(map(lambda p: (p.x,p.y), self.planetas))
        path = mpltPath.Path(posiciones_planetas)
        inside = path.contains_points([punto])
        return inside[0]
    
    def predecir_clima_str(self, area, sol_dentro_recta, sol_dentro_triangulo):
        if area == 0 and sol_dentro_recta:
            return str(Clima.SEQUIA)
        if area == 0 and sol_dentro_recta == False:
            return str(Clima.CONDICIONES_OPTIMAS)
        if area == AREA_MAXIMA and sol_dentro_triangulo:
            return str(Clima.LLUVIA_INTESA)
        if area != 0 and sol_dentro_triangulo:
            return str(Clima.LLUVIA)
        return str(Clima.SIN_PRONOSTICO)

    #puntos_recta contiene las posiciones de los planetas
    def punto_dentro_de_recta(self, puntos_recta, punto):
        x1 = puntos_recta[0][0]
        x2 = puntos_recta[1][0]
        y1 = puntos_recta[0][1]
        y2 = puntos_recta[1][1]
        punto_x = punto[0]
        punto_y = punto[1]
        
        if((x2-x1 == 0 and x2 == punto_x)or(y2-y1 == 0 and y2== punto_y)): #Para evitar la division por 0
            return True
        inside = ((punto_x - x1 )/(x2 - x1 ))== ((punto_y -y1)/(y2- y1)) #Ecuacion de una recta por dos puntos
        return inside
    
    def calcular_area_triangulo(self,x1, y1, x2, y2, x3, y3):
        return abs(0.5*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2)))

    def calcular_area(self, posiciones):
        return self.calcular_area_triangulo(posiciones[0][0],posiciones[0][1],posiciones[1][0],posiciones[1][1],posiciones[2][0],posiciones[2][1])

    def predecir_clima(self,listaPlanetas,posicion_sol):
        area = self.calcular_area(listaPlanetas)
        dentroDeTriangulo = self.punto_dentro_de_triangulo(listaPlanetas, posicion_sol)
        dentroDeRecta = self.punto_dentro_de_recta(listaPlanetas, posicion_sol)
        clima = self.predecir_clima_str(area,dentroDeRecta,dentroDeTriangulo)
        return area, dentroDeTriangulo, dentroDeRecta, clima

    def generar_predicciones(self,sistemaSolar, ndias):
        periodos = { str(Clima.SEQUIA) : 0, str(Clima.CONDICIONES_OPTIMAS): 0 , str(Clima.LLUVIA): 0, str(Clima.LLUVIA_INTESA): 0 , str(Clima.SIN_PRONOSTICO): 0 }
        with open('planetas.csv', 'w', newline='') as writeFile:
            writer = csv.writer(writeFile, delimiter=';')
            dia = 1
            clima_anterior = ''
            while dia <= ndias:
                estado_sistema = []
                sistemaSolar.avanzar_posiciones(dia)
                listaPlanetas = list(map(lambda p: (p.x,p.y), sistemaSolar.planetas))
                area, dentroDeTriangulo, dentroDeRecta, clima = self.predecir_clima(listaPlanetas,sistemaSolar.posicion_sol)

                estado_sistema.append(dia)
                estado_sistema.append(str(area))
                estado_sistema.append(str(dentroDeTriangulo))
                estado_sistema.append(str(dentroDeRecta))
                estado_sistema.append(clima)

                if clima_anterior != clima:
                    periodos[clima] = int(periodos[clima]) + 1
                writer.writerow(estado_sistema)                  
                clima_anterior = clima
                dia = dia + 1
        writeFile.close()
        print(' --- PERIODOS DE CLIMA ---')
        for clima, cantidad_periodos in periodos.items():
            print(clima, cantidad_periodos)