import unittest

def suma(num_1, num_2):
    return num_1 + num_2

class CajaNegraTest(unittest.TestCase):
    # Las pruebas desde funciones

    def test_suma_dos_positivos(self):
        num_1 = 10
        num_2 = 5

        resultado = suma(num_1, num_2)
        
        #Esto funciona asi:
        #(valor, valorQuerido) = valor == valorQuerido (Nos devuelve un true o false)
        self.assertEqual(resultado, 15)

        #(valor, valorQuerido) = valor > valorQuerido (Nos devuelve un true o false)
        #self.assertGreater(resultado, 14)

        # (valor, valorQuerido) = valor >= valorQuerido (Nos devuelve un true o false)
        #self.assertGreaterEqual(resultado, 15)

        # (valor, valorQuerido) = valor < valorQuerido (Nos devuelve un true o false)
        #self.assertLess(resultado, 16)

        # (valor, valorQuerido) = valor <= valorQuerido (Nos devuelve un true o false)
        #self.assertLessEqual(resultado, 15)

        
    def test_suma_dos_negativos(self):
        num_1 = -10
        num_2 = -7

        resultado = suma(num_1, num_2)

        self.assertEqual(resultado, -17)

        

if __name__ == '__main__':
    unittest.main()






