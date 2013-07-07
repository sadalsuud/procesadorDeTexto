# -*- coding: utf-8 -*-


# Clase para el manejo de una lista circular doble enlazada
# @author Daniel Méndez
# @version 0.1

# hereda de la clase list
class ListaCD(list):

    # constructor que sirve como parametrizado y contructor vacio
    def __init__(self, sequence=[]):
        super(ListaCD, self).__init__(sequence)
        self.size = len(sequence)

    # Adiciona un Elemento al Inicio de la Lista
    def addInicio(self, dato):
        self.insert(0, dato)
        self.size += 1

    # Inserta un Elemento al Final de la Lista
    def addFin(self, dato):
        self.append(dato)
        self.size += 1

    # Borra un elemento de la lista dada una posicion
    def remove(self, i):
        self.pop(i)
        self.size -= 1

    # Retorna el Objeto de la posicion i
    def get(self, i):
        return self[i]

    # Borra la lista
    def removeAll(self):
        self.size = 0
        del self[:]

    # Retorna true si la lista esta vacia, false en caso contrario
    def esVacia(self):
        return self.size == 0

    # Busca un elemento de la lista y devuelve su posicion.
    def indexOf(self, dato):
        return self.index(dato)

    def _not_in_range(self, i):
        return i < 0 or i >= len(self)

    def set_index(self, i):
        if self._not_in_range(i):
            raise IndexError, 'Can\'t set index out of range'
        else:
            self.i = i

    def next(self, n=1):
        if self == []:
            raise Exception, 'There are no items'
        if self._not_in_range(self.i):
            self.i = len(self) - 1
        self.i = (self.i + n) % len(self)
        return self[self.i]

    def prev(self, n=1):
        return self.next(-n)


if __name__ == '__main__':
    '''Clase testeada con unittest'''

    import unittest

    class Prueba(unittest.TestCase):
        def setUp(self):
            self.l = ListaCD([1, 2, 3, 15, "www", 'u'])
        """"
        def testArrancaDeCero(self):
            self.assertEqual(self.l.next(), 2)
        def testTomaElPasoComoParametroOpcional(self):
            self.assertEqual(self.l.next(4), "www")
        def testTomaPasoNegativo(self):
            self.assertEqual(self.l.next(-2), "www")
        def testTomaPasoQueDaUnParDeVueltas(self):
            self.assertEqual(self.l.next(8), 3)
        def testSePortaIgualParaAtrasYParaAdelante(self):
            self.assertEqual(self.l.prev(), "u")
        def testIndiceFueraDeRango(self):
            self.assertRaises(IndexError, self.l.set_index, 8)
        def testNoItems(self):
            self.assertRaises(Exception, ListaCD([]).next)
        def testResizeList(self):
            '''el indice queda fuera de rango'''
            self.l.set_index(5)
            self.l.pop()
            self.assertEqual(self.l.prev(), 15)
"""
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
    unittest.main()
