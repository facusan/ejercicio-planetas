from flask import Flask , abort
from flask import jsonify
from flask import request
from flask import render_template

from sistemaSolar import SistemaSolar, Planeta, SentidoOrbita
from predictor import Predictor
from dibujador import DibujadorSistemaSolar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/clima')
def clima():
    ferengi = Planeta('Ferengi',500,0,1, SentidoOrbita.HORARIO,500)
    betasoide = Planeta('Betasoide',2000,0,3, SentidoOrbita.HORARIO,2000)
    vulcano = Planeta('Vulcano',1000,0,5, SentidoOrbita.ANTIHORARIO,1000)
    planetas = [ferengi,betasoide,vulcano]
    sistemaSolar = SistemaSolar(planetas,[0,0])
    
    dia = request.args.get('dia')
    sistemaSolar.avanzar_posiciones(int(dia))
    predictor_clima = Predictor()
    listaPlanetas = list(map(lambda p: (p.x,p.y), sistemaSolar.planetas))
    clima = predictor_clima.predecir_clima(listaPlanetas, sistemaSolar.posicion_sol)
    return jsonify(dia = dia, clima = clima)

@app.route('/imagen')
def imagen():
    ferengi = Planeta('Ferengi',500,0,1, SentidoOrbita.HORARIO,500)
    betasoide = Planeta('Betasoide',2000,0,3, SentidoOrbita.HORARIO,2000)
    vulcano = Planeta('Vulcano',1000,0,5, SentidoOrbita.ANTIHORARIO,1000)
    planetas = [ferengi,betasoide,vulcano]
    sistemaSolar = SistemaSolar(planetas,[0,0])

    dia = request.args.get('dia')
    sistemaSolar.avanzar_posiciones(int(dia))
    dibujador = DibujadorSistemaSolar(sistemaSolar)
    return dibujador.dibujarEnBytes().decode('utf8')

if __name__ == '__main__':
    app.run()