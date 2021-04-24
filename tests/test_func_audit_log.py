#!/usr/bin/python3

import pytest
from pathlib import Path
import os
import sys
from subprocess import Popen, PIPE

os.environ['PYTHONIOENCODING'] = 'UTF-8'

PYTHON_FILE = os.path.join(str(os.path.dirname(os.path.dirname(__file__))), 'audit_log.py')

class TestFuncAuditLog:

    @pytest.mark.parametrize("xlsx_path", [(Path(__file__).with_name('info_table_func.xlsx'))])
    def test_func_abs_freq(self, xlsx_path):
        p = Popen(['python', str(PYTHON_FILE),'--path', str(xlsx_path), '-a'],bufsize=0, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        output,err = p.communicate()
        expected = open(os.path.join(os.path.dirname(__file__), 'expected_func_tests', 'test_func_abs_freq.txt'), "rb").read()
        assert expected.decode('UTF-8').replace("\r","") == output

    @pytest.mark.parametrize("xlsx_path", [(Path(__file__).with_name('info_table_func.xlsx'))])
    def test_func_rel_freq(self, xlsx_path):
        p = Popen(['python', str(PYTHON_FILE),'--path', str(xlsx_path), '-r'],bufsize=0, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        output,err = p.communicate()
        expected = open(os.path.join(os.path.dirname(__file__), 'expected_func_tests', 'test_func_rel_freq.txt'), "rb").read()
        assert expected.decode('UTF-8').replace("\r","") == output

    @pytest.mark.parametrize("xlsx_path", [(Path(__file__).with_name('info_table_func.xlsx'))])
    def test_func_mode(self, xlsx_path):
        p = Popen(['python', str(PYTHON_FILE),'--path', str(xlsx_path), '-m'],bufsize=0, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        output,err = p.communicate()
        expected = open(os.path.join(os.path.dirname(__file__), 'expected_func_tests', 'test_func_mode.txt'), "rb").read()
        assert expected.decode('UTF-8').replace("\r","") == output 

    @pytest.mark.parametrize("xlsx_path", [(Path(__file__).with_name('info_table_func.xlsx'))])
    def test_func_scope(self, xlsx_path):
        p = Popen(['python', str(PYTHON_FILE),'--path', str(xlsx_path), '-s'],bufsize=0, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        output,err = p.communicate()
        expected = open(os.path.join(os.path.dirname(__file__), 'expected_func_tests', 'test_func_scope.txt'), "rb").read()
        assert expected.decode('UTF-8').replace("\r","") == output       

    @pytest.mark.parametrize("xlsx_path", [(Path(__file__).with_name('info_table_func.xlsx'))])
    def test_func_abs_rel_freq(self, xlsx_path):
        p = Popen(['python', str(PYTHON_FILE),'--path', str(xlsx_path), '-a', '-r'],bufsize=0, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        output,err = p.communicate()
        expected = open(os.path.join(os.path.dirname(__file__), 'expected_func_tests', 'test_func_abs_rel_freq.txt'), "rb").read()
        assert expected.decode('UTF-8').replace("\r","") == output

    @pytest.mark.parametrize("xlsx_path", [(Path(__file__).with_name('info_table_func.xlsx'))])
    def test_func_mode_scope(self, xlsx_path):
        p = Popen(['python', str(PYTHON_FILE),'--path', str(xlsx_path), '-m','-s'],bufsize=0, stdout=PIPE, stderr=PIPE, encoding='UTF-8')
        output,err = p.communicate()
        expected = open(os.path.join(os.path.dirname(__file__), 'expected_func_tests', 'test_func_mode_scope.txt'), "rb").read()
        assert expected.decode('UTF-8').replace("\r","") == output    