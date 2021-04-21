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

    @unittest.expectedFailure
    def test_calc_abs_freq_fail(self):
        expected = {'Hi': 11, 'Hello': 7, 'Ciao': 1, 'Hola': 2}
        actual = TestDataOperations.c_do_obj.calc_abs_freq()
        self.assertDictEqual(expected, actual)     

    def test_sort_abs_freq_dict(self):
        d = {'Hello': 6, 'Hi': 11, 'Hola': 2, 'Ciao': 1}
        expected = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual =  TestDataOperations.c_do_obj.sort_abs_freq_dict(d)
        self.assertDictEqual(expected, actual)

    @unittest.expectedFailure
    def test_sort_abs_freq_dict_fail(self):
        d = {'Hello': 5, 'Hi': 11, 'Hola': 2, 'Ciao': 1}
        expected = {'Hi': 11, 'Ciao': 1, 'Hola': 2, 'Hello': 6}
        actual =  TestDataOperations.c_do_obj.sort_abs_freq_dict(d)
        self.assertDictEqual(expected, actual)    

    def test_abs_freq(self):
        expected = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.abs_freq()
        self.assertDictEqual(expected, actual)

    @unittest.expectedFailure
    def test_abs_freq_fail(self):
        expected = {'Hola': 3, 'Ciao': 1, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.abs_freq()
        self.assertDictEqual(expected, actual)    

    def test_get_max_value(self):
        d = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.get_max_value(d)
        self.assertEqual(20, actual)

    @unittest.expectedFailure
    def test_get_max_value_fail(self):
        d = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.get_max_value(d)
        self.assertEqual(19, actual)    

    def test_calc_rel_freq(self):
        actual = TestDataOperations.c_do_obj.calc_rel_freq(5, 20)
        self.assertEqual(25, actual)

    @unittest.expectedFailure
    def test_calc_rel_freq_fail(self):
        actual = TestDataOperations.c_do_obj.calc_rel_freq(6, 20)
        self.assertEqual(25, actual)

    def test_find_mode(self):
        d = {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.find_mode(d)
        self.assertEqual(['Hi'], actual)

    @unittest.expectedFailure
    def test_find_mode_fail(self):
        d = {'Ciao': 1, 'Hola': 12, 'Hello': 6, 'Hi': 11}
        actual = TestDataOperations.c_do_obj.find_mode(d)
        self.assertEqual(['Hi'], actual)    

    def test_calc_scope(self):
        actual = TestDataOperations.c_do_obj.calc_scope(('Hi', 20), ('Hola', 100))
        self.assertEqual(80, actual)

    @unittest.expectedFailure
    def test_calc_scope_fail(self):
        actual = TestDataOperations.c_do_obj.calc_scope(('Hi', 20), ('Hola', 100))
        self.assertEqual(70, actual)    

    def test_absolute_frequency(self):
        expected = (20, {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11})
        actual = TestDataOperations.c_do_obj.absolute_frequency()
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_absolute_frequency_fail(self):
        expected = (30, {'Ciao': 1, 'Hola': 2, 'Hello': 6, 'Hi': 11})
        actual = TestDataOperations.c_do_obj.absolute_frequency()
        self.assertEqual(expected, actual)    

    def test_relative_frequency(self):
        expected = (100, {'Ciao': 5.0, 'Hola': 10.0, 'Hello': 30.0, 'Hi': 55.00000000000001})
        actual = TestDataOperations.c_do_obj.relative_frequency()
        self.assertEqual(expected, actual)

    @unittest.expectedFailure
    def test_relative_frequency_test(self):
        expected = (100, {'Ciao': 8.0, 'Hola': 10.0, 'Hello': 30.0, 'Hi': 55.00000000000001})
        actual = TestDataOperations.c_do_obj.relative_frequency()
        self.assertEqual(expected, actual)    

    def test_mode(self):
        actual = TestDataOperations.c_do_obj.mode()
        self.assertEqual(['Hi'], actual)

    @unittest.expectedFailure
    def test_mode_fail(self):
        actual = TestDataOperations.c_do_obj.mode()
        self.assertEqual(['Hello'], actual)

    def test_scope(self):
        actual = TestDataOperations.c_do_obj.scope()
        self.assertEqual(10, actual)

    @unittest.expectedFailure
    def test_scope_fail(self):
        actual = TestDataOperations.c_do_obj.scope()
        self.assertEqual(15, actual)    

if __name__ == '__main__':
    unittest.main()