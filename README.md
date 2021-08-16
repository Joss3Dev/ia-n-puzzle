# ia-n-puzzle
Implementacion del algoritmo de N-Puzzle con Busqueda por Ancho y A*

## Alumnos:
 - Ivan Vera
 - Nelson Ruiz
 - José Luis Benitez

# Instalacion y Uso
Para utilizar se debe contar con python 3.5 para arriba, se debe instalar la libreria ```eel``` mediante:

```pip install eel```

Para ejecutar el programa se debe correr con python el archivo main.py:

````python main.py````

Una vez ejecutado el script main.py se abre una pestaña en el navegador en el puesto 8000 de localhost
en el enlace ````http://localhost:8000/vista.html````

Ahi se solicita ingresar el numero de la N para generar y el algoritmo que se desea utilizar para 
resolver el puzzle y se muestra una tabla inicial con unos valores falsos.

Una vez cargado esos datos se debe esperar a que el algoritmo resuelva el puzzle, cuando lo
resuelve muestra otra tabla debajo de la del estado inicial que muestra la tabla final obtenida.
Tambien se muestra el tiempo transcurrido en milisegundos para la solucion, la cantidad de nodos y
el camino de solucion.

Si el algoritmo tarda mas de 30 segundos para el BFS o mas de 5 minutos para la busqueda A* se muestra una adventencia y se deja de ejecutar.git 