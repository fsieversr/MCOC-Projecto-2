# MCOC-Proyecto-2

### Especificaciones Computador
Modelo Computador: HP Pavillion 5JREP0C.
Procesador: i3-3217U 1.80 GHz.
Memoria RAM: 4 GB.
Sistema operativo: Windows 10 64bits.

### Rendimiento
Para poder obtener una noción del rendimiento del código, se midió el tiempo que demoró el computador en simular distintos números de partículas. Estos datos se presentaran a continuación.

 
    N° Particulas       Tiempo[s]
          2              19,6
          5              122,6 
          10             606,6
          20
         
         
### Comentarios
Se puede observar en el gráfico que a medida que aumentan las particulas, el tiempo aumenta de forma exponencial. Esto se debe a que el código demora mucho en analizar el choque entre las partículas. Este procedimiento sería el cuello de botella, ya que el codigo toma la posición de una partícula en un instante en el tiempo y compara con las posiciones del resto de las partículas para comprobar si se estas se cruzan. Por lo tanto, como se puede observar en el gráfico, mientras más particulas se simulen mayor será el tiempo que demora en correr el código.

### Mejoras posibles


          
