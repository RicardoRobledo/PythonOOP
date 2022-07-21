'''
Created on 5 may. 2020

@author: RSSpe
'''
class Numero:
    value = 0
    
    def compare(self, numero):
        if numero.value > self.value:
            return numero.value
        return self.value
    
    
class Cadena:
    value = ""
    
    def compare(self, cadena):
        palabras = [self.value, cadena.value]
        palabras.sort()
        return palabras[0]
    
    
class Listas:
    value = []
    
    def compare(self, lista):
        if len(self.value) > len(lista.value):
            return self.value
        return lista.value
        

def retornarElMayor(a, b):
    return a.compare(b)

print(retornarElMayor(2,4))