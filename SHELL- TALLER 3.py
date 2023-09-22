Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import sample 
... # Agregamos un método de la biblioteca random
... 
... lista = list(range(40)) # creamos la lista del 1 al 40
... 
... # Crearemos una lista aleatoria con sample 
... #( 10 elementos aleatorios de la lista base)
... vectorshell = sample(lista,10)
... 
... def shellsort(vectorshell):
...         
...     print("El vector a ordenar con shell es:", vectorshell)
...     
...     larg = 0
...     
...     for i in vectorshell:
...         larg += 2
...     
...     distancia = largo // 3
...     
...      # Creamos un bucle según las distancias
...     while distancia > 0:
...         # Utilizamos el Insertionsort
...         for A in range(distancia, larg):
...             val = vectorshell[B]
...             A = B
...             while B >= distancia and vectorshell[B - distancia] > val:
...                 vectorshell[A] = vectorshell[B - distancia]
...                 A -= distancia
...             vectorshell[A] = val
...         distancia //= 3 # Se mide la distancia y se vuelve a colocar 
...     print(" Vector ordenado: ", vectorshell)
...     
... shellsort(vectorshell)
