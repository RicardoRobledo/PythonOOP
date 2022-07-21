'''
Created on 5 may. 2020

@author: RSSpe
'''
class Empleado():
    
    def __init__(self):
        self.__salario = 0
    
    @property 
    def salario(self): #getter
        return self.__salario
    
    @salario.setter
    def salario(self, salario): #setter
        self.__salario = salario
        
    
#En Python se recominda que antes de trabajar con metodos accesores, trabajemos directamente con los atributos o las propiedades
#hasta que haya algo que nos obligue a hacer una modificacion
ingenieroSistemas = Empleado()
ingenieroSistemas.salario = 400
print(ingenieroSistemas.salario)