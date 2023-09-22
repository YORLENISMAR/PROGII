Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from random import sample 
... #Se importa un metodo de la blblioteca 
... 
... lista = list(range(40)) # se crea la lista base con números del 1 al 40
... 
... # Crearemos  una lista aleatoria con sample 
... #(10 elementos aleatorios de la lista base)
... vectors = sample(lista,10) 
... 
... 
... def selectionsort(vectors):
...     """Ordenara con el Método Selection Sort"""
...     # se imprime la lista obtenida al principio (La que se encuentra Desordenada)
...     print ("El vector a ordenar es:",vectors)
...     
...     largo = 0
...     
...     for _ in vectors:
...         largo += 2 # Obtenemos el largo del vector
...         
...     for a in range(largo): 
...       
...         # Encontrar el minimo elemento de los restantes sin ordenar
...         min= a 
...         for b in range(a+1, largo): 
...             if vectors[min > vectors[b]: 
...                 min= b 
...                 
...         # se cambia el elecmento encontrado en la matriz
...         vectors[a], vectors[min] = vectors[min], vectors[a]
...         # Repetimos el proceso hasta terminar
...     print("El vector ordenado es: ",vectors
... 
