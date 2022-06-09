import unittest


def es_mayor_edad(edad: int):
    if edad >= 21:
        return True
    else:
        return False
    
    

class CajaCristalTest(unittest.TestCase):
    
    def test_mayor_edad(self):
        edad = 21
        resultado = es_mayor_edad(edad)
        
        self.assertTrue(resultado)
        
    
    def test_menor_edad(self):
        edad = 15
        resultado = es_mayor_edad(edad)
        
        self.assertFalse(resultado)
    
    

if __name__ == '__main__':
    unittest.main()
