### MCOC-Proyecto-2
Datos del problema

#masa de una partícula#

g = 9.81 *_m/_s**2 #gravedad#

d = 15*_mm #diámetro# 

rho_agua = 1000.*_kg/(_m**3)

rho_partícula = 2650.*_kg/(_m**3)

dt = 0.001*_s  #paso de tiempo#

tmax = 2*_s #tiempo máximo de simulación#

ti = 0.*_s  #tiempo actual#

N.º de partículas vs Tiempo de ejecución(segundos)

1__	1,23

2__37,05

5__	100,62

10__	319,38

20__	1371,51


El problema principal radica en que al haber un choque el dt de las partículas se hace muy pequeño para todas las partículas, por tanto ocupa mas memoria y esto tiempo, ademas que al graficar mas choques y partículas aumenta de forma exponencial el tiempo de ejecución.

Una buena forma de mejorar el código es que el dt disminuya solamente en las partículas que choquen, pero para esto hay que trabajar cada partícula como independiente.
