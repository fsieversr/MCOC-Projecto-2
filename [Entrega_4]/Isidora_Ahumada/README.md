### MCOC-Proyecto-2

### Descripción Proyecto

En este proyecto se implementará un modelo de simulación de transporte de sedimentos de partícula de fondo en base a un método lagrangiano, el cual analiza el comportamiento de cada una de las partículas.

### Computador 

Mi computador es un MacBook Air de 13 pulgadas con un procesador i7 de 2.2GHz. Tiene 8 gb de memoria ram y un ssd de 500 gb. 
Además tiene una tarjeta gráfica Intel HD Graphic 6000 de 1536 mb de memoria. 

El rendimiento del computador se analizó midiendo el tiempo que se demoró en simular el programa para 2, 5, 10 y 20 particulas. Los resultados del tiempo se muestran a continuación: 

 
    N° Particulas       Tiempo[s]
          2              9.64
          5              67.9
          10             278.2
          20             
          
### Resultados

Gráfico para 2 partículas 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/Isidora_Ahumada/2_particulas.png)

Gráfico para 5 partículas

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/Isidora_Ahumada/5_particulas.png)

Gráfico para 10 partículas 

![al text](https://github.com/fsieversr/MCOC-Proyecto-2/blob/master/[Entrega_4]/Isidora_Ahumada/10_particulas.png)




### Comentarios 

El programa se resume en que mientras más particulas tenga que modelar, más tiempo se demora en obtener el gráfico de la posición. El tiempo aumenta exponencialmente, debido a que el código tarda mucho en analizar los choques de la partículas, por lo que una mejora podría ser que las particulas luego de chocar, tomen caminos distintos. Para 20 partículas el programa tarda más de 1 hora en realizar la simulación, por lo que se podría decir que ahi inicia el cuello de botella. 

