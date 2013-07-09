# -*- coding: utf-8 -*-


# Clase para el manejo de una lista circular doble enlazada
# @author Daniel Méndez
# @version 0.3

# hereda de la clase list
class ListaCD(list):

    # constructor que sirve como parametrizado y contructor vacio
    def __init__(self, sequence=[]):
        super(ListaCD, self).__init__(sequence)
        self.pos = 0

    # Adiciona un Elemento al Inicio de la Lista
    def addInicio(self, dato):
        self.insert(0, dato)
        self.pos = 0

    # Inserta un Elemento al Final de la Lista
    def addFin(self, dato):
        self.append(dato)
        self.pos = len(self) - 1

    # Borra un elemento de la lista dada una posicion
    def remove(self, i):
        self.pop(i)
        if i == 0 and self.size == 1:
            self.pos = 0
        else:
            self.pos = i -1

    # Retorna el Objeto de la posicion i
    def get(self, i):
        self.pos = i % len(self)
        return self[self.pos]
        
    # Modifica el dato en la posición i
    def set(self, i, dato):
        self.pos = i % len(self)
        self[self.pos] = dato

    # Borra la lista
    def removeAll(self):
        self.size = 0
        del self[:]
        self.pos = 0

    # Retorna true si la lista esta vacia, false en caso contrario
    def esVacia(self):
        return self == []

    # Busca un elemento de la lista y devuelve su posicion.
    def indexOf(self, dato):
        return self.index(dato)
       
    # Me da el dato de la posición siguiente e a la actual
    def getSig(self, n=1):
        self.pos = (self.pos + n) % len(self)
        return self[self.pos]
        
    # Me da el dato y se para en el anterior
    def getAnt(self):
        i = self.pos
        self.pos -= 1
        return self.getSig(i)



if __name__ == '__main__':
    '''Clase testeada con unittest'''

    import unittest

    class Prueba(unittest.TestCase):
        def setUp(self):
            self.l = ListaCD([1, 2, 3, 15, "www", 'u'])
             
        def testAddInicio(self):
            aux = [1, 2, 3, 15, "www", 'u']
            self.l.addInicio(3)
            self.assertEqual(self.l, [3] + aux)

        def testAddFin(self):
            aux = [1, 2, 3, 15, "www", 'u']
            self.l.addFin(14)
            self.assertEqual(self.l, aux + [14])

        def testRemove(self):
            aux = [1, 2, 15, "www", 'u']
            self.l.remove(2)
            self.assertEqual(self.l, aux)
        
        def testGet(self):
            self.assertEqual(self.l.get(4), "www")
            self.assertEqual(self.l.get(8), 3)
            
        def testSet(self):
            self.l.set(4, "http")
            self.assertEqual(self.l.get(4), "http")

        def testRemoveAll(self):
            self.l.removeAll()
            self.assertEqual(self.l.size, 0)

        def testEsVacia(self):
            self.l.removeAll()
            self.assertEqual(self.l.esVacia(), True)

        def testIndexOf(self):
            self.assertEqual(self.l.indexOf("www"), 4)

        def testListaVacia(self):
            self.otra = ListaCD([])
            self.assertEqual(self.otra.esVacia(), True)
        
        def testGetNext(self):
            self.assertEqual(self.l.get(5), 'u')
            self.assertEqual(self.l.getSig(), 1)
        
        def testGetAnt(self):
            self.assertEqual(self.l.get(0), 1)
            self.assertEqual(self.l.getAnt(), 'u')
    
    unittest.main()
