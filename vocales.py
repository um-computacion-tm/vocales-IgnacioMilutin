import unittest

def contar_vocales(palabra):
    vocales = ("a", "e", "i", "o", "u")
    resultado = {}
    palabra=palabra.lower()
    for letra in palabra:
        if letra in vocales:
            if letra in resultado.keys():
                resultado[letra] += 1
            else:
                resultado[letra] = 1
    return resultado


#def vocal_counter(word: str) -> dict:
#    vocales={}
#    for letter in word:
#        if letter in ('a','e','i','o','u'):
#            vocales[letter]=1+vocales.get(letter,0)
#        return vocales
    


class TestCont(unittest.TestCase):
    def test_sin_vocales(self):
        palabra="tryhgf"
        resultado=contar_vocales(palabra)
        self.assertEqual(resultado,{})
    
    def test_con_o(self):
        palabra="tryhgfo"
        resultado=contar_vocales(palabra)
        self.assertEqual(resultado,{"o":1})
    
    def test_con_doble_o(self):
        palabra="tryhgfoo"
        resultado=contar_vocales(palabra)
        self.assertEqual(resultado,{'o':2})
    
    def test_con_todas_las_vocales(self):
        palabra="aaeuuuioo"
        resultado=contar_vocales(palabra)
        self.assertEqual(resultado,{'a':2,'e':1,'u':3,'i':1,'o':2})
    
    def test_con_mayusculas(self):
        palabra="HOla, como ESTAS"
        resultado=contar_vocales(palabra)
        self.assertEqual(resultado,{'o':3,'a':2,'e':1})

if __name__ == '__main__':
    unittest.main()