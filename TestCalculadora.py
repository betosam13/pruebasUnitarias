import unittest


class TestCalculadora(unittest.TestCase):

    def setUp(self):
        self.cal = Calculadora()

    def test_sumar_2_mas_2(self):
        resultado = self.cal.suma(2, 2)

        self.assertEqual(4, resultado)

    def test_sumar_3_mas_3(self):
        resultado = self.cal.suma(3, 3)

        self.assertEqual(6, resultado)


class Calculadora():

    def suma(self, numero1, numero2):
        return numero1 + numero2

if __name__ == '__main__':
    unittest. main()