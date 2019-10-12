### MCOC-Proyecto-2
Especificaciones Computador
Modelo Computador: Lenovo ideapad 330S

Procesador: i7-8550U 1.80 GHz.

Memoria RAM: 8 GB.

Sistema operativo: Windows 10 64bits.

Rendimiento
Para poder obtener una noción del rendimiento del código, se midió el tiempo que demoró el computador en simular distintos números de partículas. Estos datos se presentan a continuación.

N° Particulas       Tiempo[s]
      2              4.08
      5              31.75 
      10             143.5
      20             1239.9

Comentarios
Se puede observar en el gráfico que a medida que aumentan las particulas, el tiempo aumenta de forma exponencial. Esto se debe a que el código demora mucho en analizar el choque entre las partículas. Este procedimiento sería el cuello de botella, ya que el codigo toma la posición de una partícula en un instante en el tiempo y compara con las posiciones del resto de las partículas para comprobar si se estas se cruzan. Por lo tanto, como se puede observar en el gráfico, mientras más particulas se simulen mayor será el tiempo que demora en correr el código.

Mejoras posibles
Para mejorar el código se podría optimizar los dos ciclos for que sirven para recorrer una partícula con la otra. Para esto se podrían ocupar listas de compresión, esta es una forma de escribir el código en la que python la puede ejecutar más rápido. Se debería analizar esta opción en los ciclos de la modelación de choque para que de esta forma no tome tanto tiempo.
