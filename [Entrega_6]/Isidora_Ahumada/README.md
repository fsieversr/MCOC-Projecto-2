### MCOC-Proyecto-2

### Descripción Proyecto

En este proyecto se implementará un modelo de simulación de transporte de sedimentos de partícula de fondo en base a un método lagrangiano, el cual analiza el comportamiento de cada una de las partículas. Se presentan a continuacion los resultados del código de la entrega 4 y a continuación los resultados con el nuevo código. 

### Computador 

Mi computador es un MacBook Air de 13 pulgadas con un procesador i7 de 2.2GHz. Tiene 8 gb de memoria ram y un ssd de 500 gb. 
Además tiene una tarjeta gráfica Intel HD Graphic 6000 de 1536 mb de memoria. 


### Rendimiento 

El rendimiento del computador se analizó midiendo el tiempo que se demoró en simular el programa para diferentes números de partículas y comparandolos con el rendimiento del nuevo código [Entrega 6]. 
Se muestra el caso integrando todas las partículas con el mismo salto de tiempo y el caso donde se integran todas las particulas juntas[Entrega 4]. Los resultados del tiempo se muestran a continuación: 

    N° Particulas       Tiempo[s]
          2              9.64
          5              67.9
          10             278.2
          20             360.4
 
 Ahora los resultados para las particulas integradas por separado, entre las que chocan y las que no [Entrega 6]:
 
    N° Particulas       Tiempo[s]
          2              6.94
          5              16.33
          10             33.83
          20             71.05   
          50             195.65   
          80             376.02
          100            462.25   
          130            695.5   

Se presenta a continuación el gráfico obtenido para 80 partículas. 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_6]/Isidora_Ahumada/80_particulas.png)


### Comentarios 

Se puede notar que el código funciona para un mayor número de partículas, y con un menor tiempo de simulación en comparación a la entrega anterior. 
Esto ocurre debido a que el código nuevo funciona separando la integración de las partículas que chocan y las que no, en cambio en el código anterior integraba todo tipo de partículas por igual. 
En el gráfico partículas vs tiempo, se puede notar que crece linealmente la curva. Ya no tenemos una curva cuadrática, por lo que se consiguió que el rendimiento del código haya mejorado y sea más rápido que el anterior. 
 
