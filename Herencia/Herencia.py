'''
Created on 5 may. 2020

@author: RSSpe
'''
class SuperHero:
    def __init__(self, nombre):
        self.nombre = nombre
        
class Persona:
    pass

class Veloz(SuperHero, Persona):
    poder = ""
    
    def __init__(self, nombre, poder):
        super().__init__(nombre)
        self.poder = poder

    def __str__(self):
        return f"Nombre: {self.nombre}\npoder: {self.poder}"

Flash = Veloz("Flash", "Correr rapido")
print(Flash.__str__())