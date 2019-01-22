from sistemaSolar import SistemaSolar, Planeta, SentidoOrbita
from dibujador import DibujadorSistemaSolar

ferengi = Planeta('Ferengi',500,0,1, SentidoOrbita.HORARIO,500)
betasoide = Planeta('Betasoide',2000,0,3, SentidoOrbita.HORARIO,2000)
vulcano = Planeta('Vulcano',1000,0,5, SentidoOrbita.ANTIHORARIO,1000)
planetas = [ferengi,betasoide,vulcano]
sistemaSolar = SistemaSolar(planetas,[0,0])

sistemaSolar.avanzar_posiciones(5)
dibujadorSistemaSolar = DibujadorSistemaSolar(sistemaSolar)

dibujadorSistemaSolar.dibujar()
#predictor.generar_predicciones(sistemaSolar,365)