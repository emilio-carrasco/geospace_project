# Story

## Punto de partida
Decidimos acotar nuestra búsqueda a las empresas de la BD proporcionada que cumplan con el requisito. Ser vecinos de una empresa del tipo que queremos tener cerca parece un buen criterio de búsqueda.

Para ello buscamos aquellas que tuvisen más empresas similares cerca. Así, a cada empresa le otorgamos una puntuación igual a la suma de la inversa de la distancia al cuaddrado. De esta manera si tenemos una empresa muy cerca este valor será mucho más alto que si tenemos otra más lejos. 

Antes de hacer esto nos aseguramos de que no fueramos a valorar dos empresaas que estuvieran realmente juntas y nos quedamos solo con unas.

A estas empresas también les asignamos un número en función de cuánto de lejos hubiera empresas de diseño.

Teníamos dos valores entre 0 y 100 para todas las compañías  en función de cuánto de bien posicionadas están con  las compañias 1M y las empresas de diseño. 

No podemos dedicarnos a buscar en la api con todas las empresas candidateas así que filtramos.

Entemos que para el cliente es ma´s importante la primera de las caracterísiticas así que filtramos quedádonos con las 20 mejores pero ponderando un poco mejnos el diseño.

Con esta 20 empresas comenzamos a obtener valores de manera muy similar a lo anterior pero con los resultados de las búsquedas en FS. Almacenábamos esto en un campo nueco.

Finalmente tendríamos una lista de diccionarios tal que así:
[
  {
    "name": "Phreesia",
    "office_numb": 1,
    "latitud": 40.739794,
    "longitud": -73.985878,
    "companies": 70.62,
    "design": 99.01,
    "starbucks": 99.94,
    "colegio": 97.7,
    "aeropuerto": 2.3,
    "bar": 84.99,
    "restaurante_vegano": 90.49,
    "estadio_de_baloncesto": 85.87,
    "peluqueria_perros": 59.0
    
Como entedemos que el cliente puede valorar unos criterios más que otros, antes de realizar la suma final podemos ponderar cada uno de estos campos al gusto. 

obtendremos finalmente un único número que nos permite ordenan las empresas contempladas en función de nuestros criterios. De todos estos nos quedamos solo con los 3 mejores para que sea el cliente el que decida y le imprimimos los 3 mapas de las zonas además de obtener un mapa del mundo donde poder observar:

. Puntuación final de las 20 empresas analizadas al detalle.
· Puntuación desglosada por campos de las 3 mejores empresa.

:)
