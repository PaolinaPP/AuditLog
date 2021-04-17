#!/usr/bin/python3

import argparse
import scripts.file_operations as fo
import scripts.data_operations as do

class AuditLog:

    def read_file(self, path, str_to_search_for):
        lectures = {}
        try:
            file_operations = fo.FileOperations(path)
            sheet = file_operations.load_file()
            lectures = file_operations.read_data(str_to_search_for, sheet)
        except:
            print("An exception occurred in read_file().")
        return lectures

    def get_abs_freq(self, data):
        (max_value, abs_freq_dict) = data.absolute_frequency()
        for key, value in abs_freq_dict.items():
            print(f'{key}: {value}')
        print(f'Общо: {max_value}')

    def get_rel_freq(self, data):
        rel_freq_dict = data.relative_frequency()
        for key, value in rel_freq_dict.items():
            print(f'{key}: {value}%')
        print(f'Общо: 100%')

    def get_mode(self, data):
        mode = data.mode()
        print(f'M0 = {mode}')

    def get_scope(self, data):
        scope = data.scope()
        print(f'{scope}')      

    def main(self, path, str_to_search_for):
        try:
            lectures = self.read_file(path, str_to_search_for)
            data = do.DataOperations(lectures)
            self.get_abs_freq(data)
            self.get_rel_freq(data)
            self.get_mode(data)
            self.get_scope(data)
        except:
            print("An exception occurred in main().")

if __name__ == "__main__":
        parser = argparse.ArgumentParser()
        parser.add_argument('--path', action='store', type=str, required=True)
        args = parser.parse_args()
        AuditLog().main(args.path, "File: Лекция")