'''
Created on 5 may. 2020

@author: RSSpe

class FilaBanco():
    usuarios = {}
    
    def siguiente_usuario(self, numero):
        return self.usuarios.obtener(numero)

    def formar_usuario(self, numero, usuario):
        self.usuarios.agregar(numero, usuario)


class Hash():
    datos = {}
    
    def obtener(self, llave):
        self.datos[llave]
        
    def agregar(self, llave, valor):
        self.datos[llave] = valor
        

class Queue:
    datos = []
    
    def obtener(self):
        self.datos[0]
        
    def agregar(self, llave, valor):
        pass
'''

#Clases abstractas

#Tenemos que importar este modulo
from abc import ABC, abstractmethod
from _ast import Try

#Cualquier clase que sea abstracta debe de heredar de ABC y cada metodo debe de tener el decorador "@abstractmethod"
class EstructuraAbstracta(ABC):
    @abstractmethod
    def obtener(self):
        pass
        
    @abstractmethod
    def agregar(self):
        pass
        

class Hash(EstructuraAbstracta):
    #Sobreescribir metodos
    def obtener(self):
        pass
    
    def agregar(self):
        pass

class Queue(EstructuraAbstracta):
    def __init__(self, almacen):
        if not isinstance(almacen, EstructuraAbstracta): #Validando que sea instancia de estructura abstracta
            raise ValueError('Store is not supported')
        self.almacen = almacen
        
h = Hash()