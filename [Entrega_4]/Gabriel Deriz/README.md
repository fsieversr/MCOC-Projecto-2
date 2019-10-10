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

N.º de partículas vs Tiempo de ejecución(segundos)

1     __  0,41 seg

3     __  1,35 seg

5     __  3,54 seg

8      __ 12,08 seg

12    __  35,99 seg

15    __  47,46 seg

18   __   106,46 seg

20   __   251,37 seg

23   __   287,01 seg

25    __  457,17 seg


El problema principal radica en que al haber un choque el dt de las partículas se hace muy pequeño para todas las partículas, por tanto ocupa mas memoria y esto tiempo, ademas que al graficar mas choques y partículas aumenta de forma exponencial el tiempo de ejecución.

Una buena forma de mejorar el código es que el dt disminuya solamente en las partículas que choquen, pero para esto hay que trabajar cada partícula como independiente.
