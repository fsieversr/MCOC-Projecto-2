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

tau_star= 0.067

tau_cr= 0.0343326015316

tau_star/tau_cr= 1.9514979061

ustar= 0.08483576191677658



El codigo se mejoro realizando cambios para que las particulas se revisaran por separado en caso de algun choque, tambien se guardaron los archivos en formato texto aparte para disminuir el consumo de memoria ram, para asi disminuir los tiempos de ejecucion y logar resultados lineales.
Tambien se creo un codigo por separado para los graficos, que toma el archivo de salida del primer codigo y lo ejecuta.

Con estos cambios se encontraron los siguientes resultados


