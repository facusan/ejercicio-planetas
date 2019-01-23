from sistemaSolar import SistemaSolar, Planeta, SentidoOrbita
from dibujador import DibujadorSistemaSolar
from predictor import Predictor

ferengi = Planeta('Ferengi',500,0,1, SentidoOrbita.HORARIO,500)
betasoide = Planeta('Betasoide',2000,0,3, SentidoOrbita.HORARIO,2000)
vulcano = Planeta('Vulcano',1000,0,5, SentidoOrbita.ANTIHORARIO,1000)
planetas = [ferengi,betasoide,vulcano]
sistemaSolar = SistemaSolar(planetas,[0,0])

# TODO Agregar parametros por consola
# --- Para dibujar el sistema solar en un determinado dia ---
sistemaSolar.avanzar_posiciones(5)
dibujadorSistemaSolar = DibujadorSistemaSolar(sistemaSolar)
dibujadorSistemaSolar.dibujar()

# --- Para generar el csv con las predicciones ---
# predictor = Predictor()
# predictor.generar_predicciones(sistemaSolar,3650)

#  --- PERIODOS DE CLIMA ---
# SEQUIA 40
# CONDICIONES OPTIMAS 0
# LLUVIA 101
# LLUVIA INTESA 20
# SIN PRONOSTICO 82

