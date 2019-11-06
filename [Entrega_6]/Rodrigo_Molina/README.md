### MCOC-Proyecto-2
Especificaciones Computador
Modelo Computador: Lenovo ideapad 330S

Procesador: i7-8550U 1.80 GHz.

Memoria RAM: 8 GB.

Sistema operativo: Windows 10 64bits.

Rendimiento
Para poder obtener una noción del rendimiento del código, se midió el tiempo que demoró el computador en simular distintos números de partículas. Estos datos se presentan a continuación.

 N° Particulas       Tiempo[s]
          2              5.35
          5              8.4 
          10             18.9
          20             39.4
          50             115.9
          80             205.8
          100            294.3
          130            429.0
         
Comentarios
Se logra apreciar que a medida que aumentan las particulas el tiempo de ejecucion del programa aumenta de manera logaritmica, esto es debido a que debe procesar mayor cantidad de choques entre estas, llegando a chocar incluso a veces dos o mas particulas a misma tiempo

Mejoras posibles
Para mejorar el código se podría optimizar los dos ciclos for que sirven para recorrer una partícula con la otra. Para esto se podrían ocupar listas de compresión, esta es una forma de escribir el código en la que python la puede ejecutar más rápido. Se debería analizar esta opción en los ciclos de la modelación de choque para que de esta forma no tome tanto tiempo.

