# geospace_project

Este proyecto consiste en evaluar el amplazamiento de una empresa atendiendo a diferentes parámetros:
    ·Estar cerca de empresas que hayan levantadao más de $1M
    ·Estar cerca de empresas de diseño
    ·Estar cerca de starbucks
    ·Que haya colegios cerca.
    ·Que haya estadios de baloncesto
    ·Que haya aeropuertos
    ·Que haya rest. veganos.
    ·Que haya bares cerca.
    
Hemos usado la base de datos de empresas en mongo db como munto de partida. Elegimos las empresas que tengan cerca empresas de diseño.

Nos quedamos con las 20 mejores que cumplan estos atendiendo a las distancia entre ellas.

Posteriormente consultamos todos los parámetros en FS y calculamos para cada oficina un valor al ponderar cada elemento de la suma de resultados por la inversa del cuadrado de la distancia.

Como no sabemos de todos los parámetros si hay alguno que el cliente le de más o menos valor damos la posibilidad de ponderar la suma final a gusto del cliente.

El resultado lo damos en 3 mapas localizando todos los servicios y localizándolos atravez de FS.

Además proporcionamos un mapa de kepler dnd se puede observar la puntuación final de los 20 candidatos y los parámetros de los 3 finalistas.

Los diferentes puntos del proceso se almacenan en archivos .json en la capeta "json" y los mapas finales en la capeta "maps"

Para ejecutar el proyecto hay un jupyter NB de proceso que llamado geospace.ipynb que genera todos los json y hace todas las llamadas a la api. Se ha utilizado un NB para poder separar en celda la parte de la llamada a api de la evaluación final sin tener que crear funciones separadas.

Para ejecutar la visualización está el archivo Visual.ipynb. que hace uso del archivo /json/top3.json para generar los mapas.

LIBRERÍAS
Pandas
cartoframes.viz
Folium
Sys
Keplergl (no utilizada porque no fucionaba. dejadas esas líineas en comentarios)
json
geopandas
bson.json_util
math
functools
requests
dotenv
os
time
operator



