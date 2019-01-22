import matplotlib.pyplot as plt
from sistemaSolar import SistemaSolar
import numpy as np
import base64
from io import BytesIO

class DibujadorSistemaSolar():
    def __init__(self, sistema_solar):
        self.sistema_solar = sistema_solar
    def dibujar_orbitas(self,X,Y):
        for planeta in self.sistema_solar.planetas:
            planetaOrbita = X**2 + Y**2 - planeta.radio**2
            plt.contour(X,Y,planetaOrbita,[0])
    def dibujar_planetas(self):
        for planeta in self.sistema_solar.planetas:
            plt.scatter(planeta.x, planeta.y, s=500)
    def dibujar_poligono(self):
        posiciones = list(map(lambda p: [p.x,p.y], self.sistema_solar.planetas))
        poligono = plt.Polygon(posiciones, color='grey')
        plt.gca().add_patch(poligono)
        
    def dibujar(self):
        x = np.linspace(-2000.0, 2000.0, 100) #TODO Hacerlo variable segun el mayor radio
        y = np.linspace(-2000.0, 2000.0, 100)
        X, Y = np.meshgrid(x,y)        
        fig, ax = plt.subplots(1,1)
        ax.grid(True)
        ax.autoscale(True)
        self.dibujar_orbitas(X,Y)
        self.dibujar_planetas()
        self.dibujar_poligono()
        plt.gca().set_aspect('equal')
        plt.show()
        #plt.savefig('sistemaSolar.png')
    
    def dibujarEnBytes(self):
        x = np.linspace(-2000.0, 2000.0, 100) #TODO Hacerlo variable segun el mayor radio
        y = np.linspace(-2000.0, 2000.0, 100)
        X, Y = np.meshgrid(x,y)        
        fig, ax = plt.subplots(1,1)
        ax.grid(True)
        ax.autoscale(True)
        self.dibujar_orbitas(X,Y)
        self.dibujar_planetas()
        self.dibujar_poligono()
        plt.gca().set_aspect('equal')
        
        figfile = BytesIO()
        plt.savefig(figfile, format='png')
        figfile.seek(0)
        figdata_png = base64.b64encode(figfile.getvalue())
        return figdata_png  