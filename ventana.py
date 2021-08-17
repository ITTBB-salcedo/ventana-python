
'''
Widget Button (Botón)
Los botones son posiblemente los componentes más utilizados en el diseño de interfaces gráficas. Yo he llegado a crear una interfaz que únicamente tenía un botón, suena raro, pero uno de mis clientes, ya hace tiempo quería un programa con un botón para ejecutar una tarea con una flecha de esas de carga debajo girando para saber que estaba "en marcha". Y véis que hay gente para todo.

Pero bueno, nosotros a lo nuestro. A partir de esta unidad todo se pone más interesante, porque grcias a los botones vamos a añadir comportamientos dinámicos a nuestras interfaces.

Comenzando por lo esencial, vamos a crear un botón:

'''

from tkinter import *

# Definimos una función a ejecutar al clic el botón
def hola():
    print("Hola mundo!")

root = Tk()

# Enlezamos la función a la acción del botón
Button(root, text="Clícame", command=hola).pack()

root.mainloop() 