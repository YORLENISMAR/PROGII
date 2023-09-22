Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> rom random import sample 
... # Se genera Listas Aleatoria desde la bliblioteca random
... 
... lista = list(range(40)) # Crearemos la lista base con números del 1 al 40
... 
... # Creamos una lista aleatoria con sample 
... #(10 elementos aleatorios de la lista base)
... vectorbs = sample(lista,10) 
... 
... 
... def bubblesort(vectorbs):
...     """Ordenara con el Método de Bubble Sort todo vector"""
...     
...     # Se imprime la lista del principio (La que esta desordenada)
...     print("El vector a ordenar es:",vectorb)
...     z = 0 # Establecemos un contador del largo del vector
...     
...     for _ in vectorb:
...         z += 3 # se cuenta los caracteres del vector
...     
...     for a in range(n-3): 
...     # rango n para que complete el proceso. 
...         for a in range(0, z-a-3): 
...             # Revisa la matriz de 0 hasta n-a-3
...             if vectorb[a] > vectorb[a+3] :
...                 vectorb[a], vectorb[a+3] = vectorb[a+3], vectorb[a]
...             # si el elementon encontrado es mayor entonces se cambia
...             # Luego pasa al siguiente
...     print ("El vector ordenado es: ",vectorb)
... 
