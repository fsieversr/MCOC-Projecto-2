# MCOC-Projecto-2: Entrega 6

### Integrantes 
* Isidora Ahumada - [isidoraahumada](https://github.com/isidoraahumada)
* Ángel Gabriel Derix - [gabovzla90](https://github.com/gabovzla90)
* Rodrigo Molina - [RodrigoMolina95](https://github.com/RodrigoMolina95)
* Francisca Sievers - [fsieversr](https://github.com/fsieversr)

### Descripción Entrega
El objetivo de esta entrega fue mejorar el desempeño del código. Para esto se siguieron las recomendaciones del profesor, las cuáles eran básicamente separar la integración de todas las partículas y guardar los resultados directamente en el disco para no verse limitado por la memoria RAM del computador.
 
En el caso de la integración se separa las partículas que chocan y las que no chocan, de esta forma el código integra con distintos pasos de tiempo. Cuando no chocan las partículas se toma un dt mayor, ya que la trayectoria de la partícula no varía de gran forma. En cuanto a las partículas que si chocan se toman intervalos de tiempo menores, debido a que el recorrido de la partícula sufre muchos cambios con el choque.
 
La recomendación de guardar un archivo txt directamente en el disco hace posible que el código funcione para muchas más partículas que anteriormente. 
 
### Validación
Para validar los resultados, se midió el tiempo que necesitaba el código para entregar los resultados en relación a la cantidad de partículas que se eligieran. Al ser este rendimiento lineal en vez de exponencial, el resultado se considera correcto. La mejora también se ve reflejada en que el código funciona con una gran cantidad de partículas. 

### Resultados

Gráfico para 2 partículas 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/2_particulas.png)

Gráfico para 5 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/5_particulas.png)

Gráfico para 10 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/10_particulas.png)

Gráfico para 20 partículas 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/20_particulas.png)

Gráfico para 50 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/50_particulas.png)

Gráfico para 80 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/80_particulas.png)

Gráfico para 100 partículas 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/100_particulas.png)

Gráfico para 130 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/130_particulas.png)

Analizando los graficos vemos como en cada uno de ellos se mantiene un rebote constante a traves del tiempo y la distancia de cada una de las particulas.  

 
### Comentarios
Los resultados obtenidos se mantienen dentro de lo esperado de una particula que a medida que pasa el tiempo va adquiriendo velocidad (debido al cauce del rio) y a la vez se va trasladando, donde este ultimo es producido el choque de las partículas con el fondo, lo que ejerce una fuerza en dirección contraria, el resultado de esto es un movimiento de rebote.  Si bien en ciertos momento pierden energia, estas la vuelven a adquirir nuevamente debido al rebote con el fondo y el choque entre ellas.
Los choque entre particulas no se alcanzan a apreciar a simple vista debido el pequeño diametro de estas.
Cabe mencionar además, que las particulas dificilmente quedarán estáticas en el fondo del lecho debido al perfil de velocidad del flujo, si bien en el fondo del rio la velocidad es cero (debido al principio de Bernoulli), los puntos donde esta variable no se hace nula evitan que las particulas caigan a esta zona. 

