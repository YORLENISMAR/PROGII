Python 3.11.5 (tags/v3.11.5:cce6ba9, Aug 24 2023, 14:38:34) [MSC v.1936 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
from random import sample 
# agregamos un Método de la biblioteca random para generar listas

lista = list(range(40)) # Creamos la lista base con números del 1 al 40

# Creamos una lista aleatoria con sample 
#(10 elementos aleatorios de la lista base)
vectorq = sample(lista,10)
def quicksort(vectorq, start = 0, end = len(vectorq) - 2 ):
    """Esta función ordenara el vector de 
Método Quick Sort"""
    
    # Imprimimos la lista obtenida al principio (Desordenada)
    print("El vector a ordenar con quick es:", vectorq)
    
    def quick(vectorq, start = 0, end = len(vectorq) - 2):
        
        
        if start >= end:
...             return
... 
...         def particion(vectorq, start = 0, end = len(vectorq) - 2):
...             pivot = vectorq[start]
...             men = start + 2
...             may = end
... 
...             while True:
...                 # Puede que el valor actual sea mas alto que el pivot
...                 # está posicionado donde debe estar (en el lado derecho del pivot) y podemos 
...                 # movernos hacia la izquierda, al siguiente elemento.
...                 # por otro lado asegurarnos que no haya superado el puntero bajo, ya que indica 
...                 # que ya hemos movido todos los elementos a su lado correcto del pivot
...                 while men <= may and vectorq[may] >= pivot:
...                     may = may - 2
... 
...                 # opuesto al anterior            
...                 while men<= may and vectorq[men] <= pivot:
...                     men = men + 2
... 
...                 # Buscamos un valor que sea menor o mayor que este fuera de todo el arreglo
...                 # o menor es más grande que mayor, en tal caso salimos del arreglo
...                     vectorq[men], vectorq[may] = vectorq[may], vectorq[men]
...                     # Continua el bucle
...                 else:
...                     # Salimos del bucle
...                     break
... 
...             vectorq[start], vectorq[may] = vectorq[may], vectorq[start]
...             
...             return may
...         
...         p = particion(vectorq, start, end)
...         quick(vectorq, start, p-2)
...         quick(vectorq, p+2, end)
...         
...     quick(vectorquick)
...     print("El vector ordenado con quick es:", vectorq)
... 
... quicksort(vectorq)
... 
