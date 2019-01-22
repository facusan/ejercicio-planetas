from sistemaSolar import SistemaSolar, Planeta, SentidoOrbita
from dibujador import DibujadorSistemaSolar
from predictor import Predictor

import unittest

class PredictorTest(unittest.TestCase):

    def test_CalcularAreaDeTriaguloEquilatero(self):
        predictor = Predictor()
        area = predictor.calcular_area_triangulo(0,0,1,0,0.5,1)
        self.assertEqual(0.5, area)
    
    def test_CalcularAreaDeTriaguloIsoceles(self):
        predictor = Predictor()
        area = predictor.calcular_area_triangulo(1,1,5,1,3,2)
        self.assertEqual(2, area)
    
    def test_DesplazarPlanetaSengunVelocidadAngulaDiariaYSentidoHorario(self):
        planeta = Planeta('Ferengi',500,0,1, SentidoOrbita.HORARIO,500)
        planeta.avanzar_posicion(90)
        self.assertEqual(0,planeta.x)
        self.assertEqual(-500,planeta.y)
    
    def test_DesplazarPlanetaSengunVelocidadAngulaDiariaYSentidoAntiHorario(self):
        planeta = Planeta('Ferengi',500,0,1, SentidoOrbita.ANTIHORARIO,500)
        planeta.avanzar_posicion(45)
        self.assertEqual(353,planeta.x)
        self.assertEqual(353,planeta.y)
    
    def test_ComprobarQueUnPuntoPertenceAUnaRecta(self):
        predictor = Predictor()
        pertenceALaRecta = predictor.punto_dentro_de_recta([(-1,0),(1,2)],(2,3))
        self.assertEqual(True,pertenceALaRecta)

    def test_ComprobarQueUnPuntoPertenceAUnaRectaQueContieneCero(self):
        predictor = Predictor()
        pertenceALaRecta = predictor.punto_dentro_de_recta([(0,0),(50,0)],(40,0))
        self.assertEqual(True,pertenceALaRecta)
    
    def test_ComprobarQueUnPuntoNoPertenceAUnaRectaQueContieneCero(self):
        predictor = Predictor()
        pertenceALaRecta = predictor.punto_dentro_de_recta([(0,0),(50,0)],(40,40))
        self.assertEqual(True,pertenceALaRecta)
    
    def test_ComprobarQueUnPuntoEstaDentroDeUnTriangulo(self):
        predictor = Predictor()
        pertenceAlTriangulo = predictor.punto_dentro_de_triangulo([(-1,-1),(1,-1),(0,1)],(0,0))
        self.assertEqual(True, pertenceAlTriangulo)
    
    def test_ComprobarQueUnPuntoNoEstaDentroDeUnTriangulo(self):
        predictor = Predictor()
        pertenceAlTriangulo = predictor.punto_dentro_de_triangulo([(-1,-1),(1,-1),(0,1)],(5,5))
        self.assertEqual(False, pertenceAlTriangulo)
    
    def test_ComprobarQueUnPuntoDelBordeEstaDentroDeUnTriangulo(self):
        predictor = Predictor()
        pertenceAlTriangulo = predictor.punto_dentro_de_triangulo([(-1,-1),(1,-1),(0,1)],(0,2))
        self.assertEqual(False, pertenceAlTriangulo)

if __name__ == '__main__':
    unittest.main()
