# MCOC-Projecto-2
##Entrega_4

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
Analizando los graficos se logra apreciar como el movimiento de rebote de cada una va en declive a medida que avanza a lo largo del rio. Ademas se logra apreciarque a medida que transcurre el tiempo y la particulas avanzan, estas tienden a mantenerse a una cierta distancia del fondo del rio. Esto ultimo responde al perfil de velocidad de todo flujo de agua, en donde la velocidad del flujo que va pegado a alguno de los bordes es cero, por lo que sumado a un bajo peso de las particulas (debido a un diametro estimado en 0,56 mm) estas tienden a mantenerse ................
 
### Comentarios
Los resultados obtenidos se mantienen dentro de lo esperado de una particula que a medida que pasa el tiempo va adquiriendo velocidad (debido al cauce del rio) y a la vez se va trasladando, donde este ultimo es producido por distintas fuerzas dando como resultado un movimiento de rebote. 
El presente codigo esta pensado para una sola particula, por lo que en un futuro podria ser adaptado para "n" particulas, en donde el movimiento, posicion y aceleracion de cada una de ellas se puedan ver afectados por el choque entre ellas
