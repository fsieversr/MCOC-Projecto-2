# MCOC-Proyecto-2

### Especificaciones Computador
 
Modelo Computador: HP Pavillion 5JREP0C.
 
Procesador: i3-3217U 1.80 GHz.
 
Memoria RAM: 4 GB.
 
Sistema operativo: Windows 10 64bits. 

### Rendimiento
 
Para poder obtener una noción del rendimiento del código, se midió el tiempo que demoró el computador en simular distintos números de partículas, se muestra el caso integrando todas las partículas con el mismo salto de tiempo y el caso donde se integran separadas. Estos datos se presentan a continuación.

 
    N° Particulas       Tiempo[s]
          2              19,6
          5              122,6 
          10             606,6
          20             3538,1
          
Separando los integrados los resultados son los siguientes.      

    N° Particulas       Tiempo[s]
          2              22,5
          5              39,1 
          10             72,3
          20             146,7
          50             422,7
          80             685,1
          100            1000,4
          130            1287,8
          
![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/Francisca_Sievers/grafico_rendimiento2.png)         
         
### Comentarios
 
Con la mejora del tiempo se observa en este gráfico una crecida lineal en cuanto al número de partículas y el tiempo que corre el código. Esto debe a la separación de los integradores para las partículas que chocan, ya que toma pasos de tiempos menores que si no chocaran. En el caso de que no choquen se integra con un intervalo de tiempo mayor, porque la trayectoria no varía en gran medida. 
 
Además de lo mencionado anteriormente, el código funciona con mayor cantidad de partículas debido a que se guarda el archivo directamente como texto en el disco, de esta forma no se ve limitado por la cantidad de RAM del computador.
  
 En la imagen se puede observar también una interrupción en la recta pasando de 80 a 100 partículas, esto se explica porque al momento de correr el código estaban ocurriendo más procesos en el computador que en los casos anteriores.
