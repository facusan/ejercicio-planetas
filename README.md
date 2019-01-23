# Ejercio de planetas
En una galaxia lejana, existen tres civilizaciones. Vulcanos, Ferengis y Betasoides. Cada
civilización vive en paz en su respectivo planeta.
Dominan la predicción del clima mediante un complejo sistema informático.
A continuación el diagrama del sistema solar.

## Premisas:
- El planeta Ferengi se desplaza con una velocidad angular de 1 grados/día en sentido
horario. Su distancia con respecto al sol es de 500Km.
- El planeta Betasoide se desplaza con una velocidad angular de 3 grados/día en sentido
horario. Su distancia con respecto al sol es de 2000Km.
- El planeta Vulcano se desplaza con una velocidad angular de 5 grados/día en sentido
antihorario,
su distancia con respecto al sol es de 1000Km.
- Todas las órbitas son circulares.
Cuando los tres planetas están alineados entre sí y a su vez alineados con respecto al sol, el
sistema solar experimenta un período de sequía.

Cuando los tres planetas no están alineados, forman entre sí un triángulo. Es sabido que en el
momento en el que el sol se encuentra dentro del triángulo, el sistema solar experimenta un
período de lluvia, teniendo éste, un pico de intensidad cuando el perímetro del triángulo está en
su máximo.

Las condiciones óptimas de presión y temperatura se dan cuando los tres planetas están
alineados entre sí pero no están alineados con el sol.

Realizar un programa informático para poder predecir en los próximos 10 años:
1. ¿Cuántos períodos de sequía habrá?
    <br />**Habran 40 periodos de sequía.**
2. ¿Cuántos períodos de lluvia habrá y qué día será el pico máximo de lluvia?
   <br /> **Habran 81 periodos de lluvia y 20 de lluvia intensa (282,438,462,618,642,798,1002,1182,1338,1362,1722,2058,2082,2238,2418,2442,2622,2778,2802,2982)**
3. ¿Cuántos períodos de condiciones óptimas de presión y temperatura habrá?
   <br /> **No habran periodos con condiciones optimas de presion y temperatura.**

**Bonus:**
Para poder utilizar el sistema como un servicio a las otras civilizaciones, los Vulcanos requieren
tener una base de datos con las condiciones meteorológicas de todos los días y brindar una API
REST de consulta sobre las condiciones de un día en particular.
1. Generar un modelo de datos con las condiciones de todos los días hasta 10 años en adelante
utilizando un job para calcularlas.
<br />
**Las predicciones para los próximos 10 años se encuentran en el archivo 'predicciones_clima.csv' con formato DIA,CLIMA**
2. Generar una API REST la cual devuelve en formato JSON la condición climática del día
consultado.
<br />
**La implementacion de la API REST se encuentra en el archivo 'main.py'**
3. Hostear el modelo de datos y la API REST en un cloud computing libre (como APP Engine o
Cloudfoudry) y enviar la URL para consulta: 
<br />
**Se realizo deploy del servidor en Google Cloud Engine, con la URL: [https://planetas-mercado-libre.appspot.com](https://planetas-mercado-libre.appspot.com)**
```
Ej: GET → http://….../clima?dia=566 → Respuesta: {“dia”:566, “clima”:”lluvia”}
```
## Comandos para ejecutar las aplicaciones
Para levantar el servidor se debe ejecutar por consola
```
python main.py
```
Para correr los test se debe ejecutar
```
python unittest.py
```
## Supuestos y aclaraciones
- No hay predicción para cuando no se cumple con las premisas del enunciado.
- Si el sol se encuentra en el borde de un triangulo se considera como que esta dentro.
- El area máxima se considera que es **1435791.5**, que fue obtenida después de ejecutar las predicciones para los 10 años.
- En el archivo
- No suelo programar en Python
