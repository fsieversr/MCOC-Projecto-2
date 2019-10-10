# MCOC-Projecto-2


### Integrantes 
* Isidora Ahumada - [isidoraahumada](https://github.com/isidoraahumada)
* Ángel Gabriel Derix - [gabovzla90](https://github.com/gabovzla90)
* Rodrigo Molina - [RodrigoMolina95](https://github.com/RodrigoMolina95)
* Francisca Sievers - [fsieversr](https://github.com/fsieversr)
### Descripción Proyecto
En este proyecto se va a simular el transporte de varias particulas debido a un flujo de agua. Ademas de considerar el movimiento debido a la propia fuerza del rio, tambien se modelara el eventual choque de las particulas entre si y de estas con el suelo
    
### Validación
Para lograr modelar el transporte de sedimentos se contaran con los siguientes supuestos:
* La partícula es esférica por tanto su cd= 0,47.
* La velocidad en el eje X es de 10 m/s.
* La velocidad en el eje Y es de 0,1 m/s.
* El diámetro de la partícula es de 1mm.
* El peso especifico de la partícula es de 2650 kg/m3. 
 
Además se ocupó la ecuación F=ma, donde F es la sumatoria de fuerzas ejercida sobre la partícula. Para este caso, consideramos el peso, la fuerza de drag y la fuerza boyante. De esta forma obtenemos la aceleración de la partícula y además tenemos la velocidad inicial supuesta, a partir de estos datos y el comando odeint de Python, se procede a calcular la posición y velocidad de la partícula a través del tiempo. Estos resultados fueron graficados.  

### Resultados

Tras analizar los gráficos obtenidos, se logra apreciar como en el primero se tiene un movimiento constante en el eje X, mientras que en el eje Y un movimiento de rebote en declive. Esto forma parte de lo esperado en una particula de fondo, en donde debido a distintas fuerzas externas esta se traslada a lo largo del rio y va rebotando con el fondo de este.
En el segundo grafico tenemos tanto la recta azul como naranja, cada una representando la velocidad de la particula tanto en el eje X como en el Y respectivamente. Aunque no se logra apreciar (debido a las condicion de borde del eje Y) ambas velocidades aumentan de manera constante a traves del tiempo, lo que esta dentro de lo esperado debido a que se esta modelando bajo el supuesto de que solo hay velocidad (del agua) en el eje X y que para llevarlo un poco mas a la realidad se establece una velocidad limite (aumque muy baja) en el eje Y
Por ultimo tenemos el tercer gráfico que representa la aceleración de la particula tanto en el eje X como en el Y, donde nuevamente vemos como ambas curvas se comportan de igual manera a través del tiempo pero con distintas condiciones de borde.
 
### Comentarios
Los resultados obtenidos se mantienen dentro de lo esperado de una particula que a medida que pasa el tiempo va adquiriendo velocidad (debido al cauce del rio) y a la vez se va trasladando, donde este ultimo es producido por distintas fuerzas dando como resultado un movimiento de rebote. 
El presente codigo esta pensado para una sola particula, por lo que en un futuro podria ser adaptado para "n" particulas, en donde el movimiento, posicion y aceleracion de cada una de ellas se puedan ver afectados por el choque entre ellas
