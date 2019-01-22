from sistemaSolar import SistemaSolar, Planeta, SentidoOrbita
from dibujador import DibujadorSistemaSolar
from predictor import Predictor

ferengi = Planeta('Ferengi',500,0,1, SentidoOrbita.HORARIO,500)
betasoide = Planeta('Betasoide',2000,0,3, SentidoOrbita.HORARIO,2000)
vulcano = Planeta('Vulcano',1000,0,5, SentidoOrbita.ANTIHORARIO,1000)
planetas = [ferengi,betasoide,vulcano]
sistemaSolar = SistemaSolar(planetas,[0,0])
predictor = Predictor()
#sistemaSolar.avanzar_posiciones('02/04/2019')# Fecha sol dentro triangulo
#sistemaSolar.avanzar_posiciones('02/08/2019')
#sistemaSolar.avanzar_posiciones('21/03/2027') # Fecha area max
sistemaSolar.avanzar_posiciones(5)

listaPlanetas = list(map(lambda p: (p.x,p.y), sistemaSolar.planetas))

area = predictor.calcular_area(listaPlanetas)
dentroDeTriangulo = predictor.punto_dentro_de_triangulo(listaPlanetas, sistemaSolar.posicion_sol)
dentroDeRecta = predictor.punto_dentro_de_recta(listaPlanetas, sistemaSolar.posicion_sol)
print('Area = ' +str(area))
print('Dentro de triangulo = ' + str(dentroDeTriangulo))
print('Dentro de recta = ' +str(dentroDeRecta))
dibujadorSistemaSolar = DibujadorSistemaSolar(sistemaSolar)
#dibujadorSistemaSolar.dibujar()

predictor.generar_predicciones(sistemaSolar,365)