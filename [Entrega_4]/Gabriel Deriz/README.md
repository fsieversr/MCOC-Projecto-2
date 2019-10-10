### MCOC-Proyecto-2
Datos del problema

#masa de una partícula#

g = 9.81 *_m/_s**2 #gravedad#

d = 1*_mm #diámetro# 

rho_agua = 1000.*_kg/(_m**3)

rho_partícula = 2650.*_kg/(_m**3)

dt = 0.001*_s  #paso de tiempo#

tmax = 0.7*_s #tiempo máximo de simulación#

ti = 0.*_s  #tiempo actual#

N.º de partículas Tiempo de ejecución(segundos)
1   0,41
3   1,35
5   3,54
8   12,08
12  35,99
15  47,46
18  106,46
20  251,37
23  287,01
25  457,17

El problema principal radica en que al haber un choque el dt de las partículas se hace muy pequeño para todas las partículas, por tanto ocupa mas memoria y esto tiempo, ademas que al graficar mas choques y partículas aumenta de forma exponencial el tiempo de ejecución.

Una buena forma de mejorar el código es que el dt disminuya solamente en las partículas que choquen, pero para esto hay que trabajar cada partícula como independiente.
