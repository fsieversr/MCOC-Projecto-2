# MCOC-Projecto-2: Entrega 4

### Integrantes 
* Isidora Ahumada - [isidoraahumada](https://github.com/isidoraahumada)
* Ángel Gabriel Derix - [gabovzla90](https://github.com/gabovzla90)
* Rodrigo Molina - [RodrigoMolina95](https://github.com/RodrigoMolina95)
* Francisca Sievers - [fsieversr](https://github.com/fsieversr)
### Descripción Proyecto
En este proyecto se va a simular el transporte de varias particulas debido a un flujo de agua. Ademas de considerar el movimiento debido a la propia fuerza del rio, tambien se modelara el eventual choque de las particulas entre si y de estas con el suelo.
 
Para lograr modelar el transporte de sedimentos se contaran con los siguientes supuestos:
* La partícula es esférica por tanto su Cd= 0,47.
* Las partículas inician en posiciones aleatorias del río.
* Las velocidades iniciales de las partículas son aleatorias.
* Se asume un fluido con perfil de velocidad logarítmico.
* El diámetro de la partícula es de 0.56 mm.
* El peso especifico de la partícula es de 2650 kg/m3. 
 
Además se ocupó la ecuación F=ma, donde F es la sumatoria de fuerzas ejercida sobre la partícula. Para este caso, consideramos el peso, la fuerza de drag (arrastre) y la fuerzade lift (fuerza de levante). De esta forma obtenemos la aceleración de la partícula y además tenemos la velocidad inicial supuesta, a partir de estos datos y el comando odeint de Python, se procede a calcular la posición y velocidad de la partícula a través del tiempo. Además de esto se considera una constante k de resorte asociada al choque en el suelo y entre partículas. Estos resultados fueron graficados y de acuerdo a ellos se establecio si el codigo era el correcto o no  

### Validación
Para validar los resultados, se tomaron como base los gráficos entregados para 2, 5, 10 y 20 partículas. El código se modeló con las mismas condiciones iniciales entregadas en ambos casos y los mismos parámetros. Se observa que los gráficos resultan similares en cuanto a la forma de la trayectoria de las particulas, sin embargo en el código simulado las partículas llegan a puntos más altos que en los graficos de validación, esto debe ser por el choque contra el suelo ejerce una fuerza mayor en la modelación. 

### Resultados

Gráfico para 2 partículas 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/2_particulas.png)

Gráfico para 5 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/5_particulas.png)

Gráfico para 10 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/10_particulas.png)

Gráfico para 20 partículas 
![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/20_particulas.png)




Analizando los graficos vemos como en cada uno de ellos se mantiene un rebote constante a traves del tiempo y la distancia de cada una de las particulas.  

 
### Comentarios
Los resultados obtenidos se mantienen dentro de lo esperado de una particula que a medida que pasa el tiempo va adquiriendo velocidad (debido al cauce del rio) y a la vez se va trasladando, donde este ultimo es producido el choque de las partículas con el fondo, lo que ejerce una fuerza en dirección contraria, el resultado de esto es un movimiento de rebote.  Si bien en ciertos momento pierden energia, estas la vuelven a adquirir nuevamente debido al rebote con el fondo y el choque entre ellas.
Los choque entre particulas no se alcanzan a apreciar a simple vista debido el pequeño diametro de estas.
Cabe mencionar además, que las particulas dificilmente quedarán estáticas en el fondo del lecho debido al perfil de velocidad del flujo, si bien en el fondo del rio la velocidad es cero (debido al principio de Bernoulli), los puntos donde esta variable no se hace nula evitan que las particulas caigan a esta zona. 

