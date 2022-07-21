'''
Created on 5 may. 2020

@author: RSSpe
'''
class SuperHero:
    def __init__(self, nombre):
        #Protegido: poner un "_" antes del nombre
        self._nombre = nombre
        
class Persona:
    pass

class Veloz(SuperHero, Persona):
    __poder = ""
    
    def __init__(self, nombre, poder):
        super().__init__(nombre)
        #Privado: poner doble "__" antes del nombre
        self.__poder = poder

    def __str__(self):
        return f"Nombre: {self._nombre}\npoder: {self.__poder}"

Flash = Veloz("Flash", "Correr rapido")
print(Flash.__str__())

#Forma de acceder a atributos privados
print(Flash._Veloz__poder)