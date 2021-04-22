#!/usr/bin/python3

import pytest
from pathlib import Path
import sys
sys.path.append('..')
import audit_log as al
import scripts.data_operations as do

DATA = ['Hi', 'Hello', 'Hi', 'Hello', 'Hello', 'Ciao', 'Hi', 'Hola', 'Hi', 'Hi', 'Hello', 'Hi', 'Hello', 'Hi', 'Hola', 'Hi', 'Hello', 'Hi', 'Hi', 'Hi']
DATA_2 = ['Hello', 'Hello', 'Hello', 'Hola', 'Hello', 'Hello', 'Ciao', 'Hi', 'Hola', 'Hi', 'Hi', 'Hello', 'Hi', 'Hello', 'Hi', 'Hola', 'Hi', 'Hello', 'Hello', 'Hello', 'Hi']

class TestAuditLog():

    @pytest.mark.parametrize("path", [(Path(__file__).with_name('info_table.xlsx'))])
    def test_read_file(self, path):
        expected = ['File: Лекция 8: Език за заявки SPARQL', 'File: Лекция 1: Въведение в програмиране за семантичен уеб', 'File: Лекция 7: Проектиране на онтология с Protégé', 'File: Лекция 9: Програмиране за семантичен уеб', 'File: Лекция 1: Въведение в програмиране за семантичен уеб']
        actual = al.AuditLog().read_file(path, "File: Лекция")
        assert (len(expected) == len(actual)) and (sorted(expected) == sorted(actual))

    @pytest.mark.parametrize("data, expected", [(do.DataOperations(DATA), 20), (do.DataOperations(DATA_2), 21)])
    def test_get_abs_freq(self, data, expected):
        actual = al.AuditLog().get_abs_freq(data)
        assert actual == expected

    @pytest.mark.parametrize("data, expected", [(do.DataOperations(DATA), 100), (do.DataOperations(DATA_2), 100)])
    def test_get_rel_freq(self, data, expected):
        actual = al.AuditLog().get_rel_freq(data)
        assert actual == 100

    @pytest.mark.parametrize("data, expected", [(do.DataOperations(DATA), ['Hi']), (do.DataOperations(DATA_2), ['Hello'])])
    def test_get_mode(self, data, expected):
        actual = al.AuditLog().get_mode(data)
        assert actual == expected

    @pytest.mark.parametrize("data, expected", [(do.DataOperations(DATA), 10), (do.DataOperations(DATA_2), 9)])
    def test_get_scope(self, data, expected):
        actual = al.AuditLog().get_scope(data)
        assert actual == expected 

if __name__ == '__main__':
    unittest.main()      