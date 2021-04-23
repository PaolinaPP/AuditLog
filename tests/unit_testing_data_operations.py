#!/usr/bin/python3

import unittest
import sys
sys.path.append('..')
import scripts.data_operations as do

class TestDataOperations(unittest.TestCase):

    c_data = ['Hi', 'Hello', 'Hi', 'Hello', 'Hello', 'Ciao', 'Hi', 'Hola', 'Hi', 'Hi', 'Hello', 'Hi', 'Hello', 'Hi', 'Hola', 'Hi', 'Hello', 'Hi', 'Hi', 'Hi']
    c_do_obj = do.DataOperations(c_data)

    def test_calc_abs_freq(self):
        expected = {'Hi': 11, 'Hello': 6, 'Ciao': 1, 'Hola': 2}
        actual = TestDataOperations.c_do_obj.calc_abs_freq()
        self.assertDictEqual(expected, actual)    

    def test_sort_abs_freq_dict(self):
        d = {'Hello': 6, 'Hi': 11, 'Hola': 2, 'Ciao': 1}
        expected = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual =  TestDataOperations.c_do_obj.sort_abs_freq_dict(d)
        self.assertDictEqual(expected, actual)  

    def test_abs_freq(self):
        expected = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.abs_freq()
        self.assertDictEqual(expected, actual)

    def test_get_max_value(self):
        d = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.get_max_value(d)
        self.assertEqual(20, actual) 

    def test_calc_rel_freq(self):
        actual = TestDataOperations.c_do_obj.calc_rel_freq(5, 20)
        self.assertEqual(25, actual)

    def test_find_mode(self):
        d = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.find_mode(d)
        self.assertEqual(['Hi'], actual)  

    def test_calc_scope(self):
        actual = TestDataOperations.c_do_obj.calc_scope(('Hi', 20), ('Hola', 100))
        self.assertEqual(80, actual) 

    def test_absolute_frequency(self):
        expected = (20, {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11})
        actual = TestDataOperations.c_do_obj.absolute_frequency()
        self.assertEqual(expected, actual)  

    def test_relative_frequency(self):
        expected = (100, {'Ciao': 5.0, 'Hola': 10.0, 'Hello': 30.0, 'Hi': 55.00000000000001})
        actual = TestDataOperations.c_do_obj.relative_frequency()
        self.assertEqual(expected, actual)   

    def test_mode(self):
        actual = TestDataOperations.c_do_obj.mode()
        self.assertEqual(['Hi'], actual)

    def test_scope(self):
        actual = TestDataOperations.c_do_obj.scope()
        self.assertEqual(10, actual)

if __name__ == '__main__':
    unittest.main()