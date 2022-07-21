'''
Created on 5 may. 2020

@author: RSSpe
'''
class Curso():
    pass

CursoDePython = Curso()

#-----------------------------------

class User():
    nombre = ""
    
    #Metodos constructor
    def __init__(self, nombre):
        self.nombre = nombre
        pass
    
    def saluda(self):
        print("Hola " + self.nombre + " bienvenido al Curso de Python")
    

Ricardo = User("Ricardo")
print(Ricardo.nombre)
Ricardo.saluda()










