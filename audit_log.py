#!/usr/bin/python3

import argparse
import scripts.file_operations as fo
import scripts.data_operations as do

class AuditLog:

    ####################################################
    #    function name: read_file                      #
    #    function parameters: string path,             #
    #                         string str_to_search_for #
    #    function description: read file and return    #
    #            list of read data                     #
    ####################################################
    def read_file(self, path, str_to_search_for):
        lectures = {}
        try:
            file_operations = fo.FileOperations(path)
            sheet = file_operations.load_file()
            if sheet is None:
                raise Exception("sheet is empty.")
            lectures = file_operations.read_data(str_to_search_for, sheet)
            if lectures is None:
                raise Exception("lectures is empty.")
        except Exception as ex:
            print(ex)
            print("An exception occurred in read_file().")
        return lectures

    ####################################################
    #    function name: get_abs_freq                   #
    #    function parameters: list data                #
    #    function description: get absolute frequency  #
    ####################################################
    def get_abs_freq(self, data):
        print("Absolute frequency:")
        (max_value, abs_freq_dict) = (0, None)
        try:
            (max_value, abs_freq_dict) = data.absolute_frequency()
            if max_value is None or max_value < 0:
                raise Exception("max value is not correct.")
            if abs_freq_dict is None:
                raise Exception("absolute frequency dictionary is empty.")
            for key, value in abs_freq_dict.items():
                print(f'{key}: {value}')
            print(f'Max: {max_value}')
        except Exception as ex:
            print(ex)
            print("An exception occurred in get_abs_freq().")    
        return max_value

    ####################################################
    #    function name: get_rel_freq                   #
    #    function parameters: list data                #
    #    function description: get relative frequency  #
    ####################################################
    def get_rel_freq(self, data):
        print("Relative frequency:")
        (max_value, rel_freq_dict) = (0, None)
        try:
            (max_value, rel_freq_dict) = data.relative_frequency()
            if max_value is None or max_value != 100:
                raise Exception("max value is not correct.")
            if rel_freq_dict is None:
                raise Exception("ralative frequency dictionary is empty.")
            for key, value in rel_freq_dict.items():
                print(f'{key}: {value}%')
            print(f'Max: {max_value}%')
        except Exception as ex:
            print(ex)
            print("An exception occurred in get_rel_freq().")    
        return max_value

    ####################################################
    #    function name: get_mode                       #
    #    function parameters: list data                #
    #    function description: get mode                #
    ####################################################
    def get_mode(self, data):
        print("Mode:")
        mode = None
        try:
            mode = data.mode()
            if mode is None:
                raise Exception("mode value is not correct.")
            print(f'M0 = {mode}')
        except Exception as ex:
            print(ex)
            print("An exception occurred in get_mode().")    
        return mode

    ####################################################
    #    function name: get_scope                      #
    #    function parameters: list data                #
    #    function description: get scope               #
    ####################################################
    def get_scope(self, data):
        print("Scope:")
        scope = 0
        try:
            scope = data.scope()
            if scope is None or scope < 0:
                raise Exception("scope value is not correct.")
            print(f'{scope}')
        except Exception as ex:
            print(ex)
            print("An exception occurred in get_mode().")    
        return scope          

    ####################################################
    #    function name: main                           #
    #    function parameters: string path,             #
    #                         string str_to_search_for #
    #    function description: main function which     #
    #        calls all funcs                           #
    ####################################################
    def main(self, args, str_to_search_for):
        try:
            lectures = self.read_file(args.path, str_to_search_for)
            if lectures is None:
                raise Exception("lectures is empty.") 
            data = do.DataOperations(lectures)
            if args.abs is True:
                if self.get_abs_freq(data) is None:
                    raise Exception("get_abs_freq(data) returns None value.")
            if args.rel is True:
                if self.get_rel_freq(data) is None:
                    raise Exception("get_rel_freq(data) returns None value.") 
            if args.mode is True:
                if self.get_mode(data) is None:
                    raise Exception("get_mode(data) returns None value.")
            if args.scope is True:
                if self.get_scope(data) is None:
                    raise Exception("get_scope(data) returns None value.")         
        except Exception as ex:
            print(ex)
            print("An exception occurred in main().")    

if __name__ == "__main__":
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', action='store', type=str, required=True)
        parser.add_argument('-a', '--abs', action='store_true')
        parser.add_argument('-r', '--rel', action='store_true')
        parser.add_argument('-m', '--mode', action='store_true')
        parser.add_argument('-s', '--scope', action='store_true')
        args = parser.parse_args()
        AuditLog().main(args, "File: Лекция")
    except Exception as ex:
        print(ex)