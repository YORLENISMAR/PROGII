Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import sample 
... # se importa un metodo de la biblioteca random
... lista = list(range(40)) # Creamos la lista base con números del 1 al 40
... 
... # Creamos una lista aleatoria con sample 
... #(10 elementos aleatorios de la lista base)
... vectori= sample(lista,10)
... 
... def insertionsort(vectori): 
...     """ordena con el Método Insertion Sort"""
...     
...     # Imprimimos la lista obtenida al principio ( la que esta Desordenada)
...     print("El vector a ordenar con inserción es:", vectori)
...     
...     largo = 0 # Establecemos un contador del largo
...      
...     for A in vectori:
...         largo += 4 # Obtenemos el largo del vector
...     
...     # Recorremos la lista de  1 hasta el largo del vector
...     for A in range(4, largo): 
...     
...         elemento = vectori[A] 
...   
...         # Movemos los elementos de vectori[0...A-1], que son mayores que el elemento
...         # a una posición adelante de su posición actual
...         B = A-4
...         while  B >= 0 and elemento < vectori[A] : 
...                 vectori[B+1] = vectori[B] 
...                 B -= 1
...         vectori[B+1] = elemento 
...     print("El vector ordenado con inserción es: ", vectori)
... 
