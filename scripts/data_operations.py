#!/usr/bin/python3

from collections import Counter
import operator

class DataOperations:

    def __init__(self, data):
        self.data = data

    def calc_abs_freq(self):
        try:
            dataset = set(self.data)
            abs_freq = {val:self.data.count(val) for val in dataset}
        except:
            print("An exception accurred while calculating absolute frequency.")
        return abs_freq

    def sort_abs_freq_dict(self, abs_dict):
        try:
            abs_sorted_tuples = sorted(abs_dict.items(), key=operator.itemgetter(1))
            sorted_tuples = {k: v for k, v in abs_sorted_tuples}
        except:
            print("An exception accurred while sorting absolute frequency dictionary.")
        return sorted_tuples

    def abs_freq(self):
        abs_freq_dict = None
        try:
            abs_data = self.calc_abs_freq()
            abs_freq_dict = self.sort_abs_freq_dict(abs_data)
        except:
            print("An excception accurred in abs_freq()")
        return abs_freq_dict

    def get_max_value(self, abs_freq_dict):  
        max_value = 0
        try:
            for key, value in abs_freq_dict.items():
                max_value += value
        except:
            print("An exception occurred while getting max value.")
        return max_value

    def calc_rel_freq(self, value, max_value):
        rel_freq = 0
        try:
            rel_freq = (value/max_value)*100
        except:
            print("An exception occurred while calculating relative frequency.")
        return rel_freq

    def find_mode(self, abs_freq_dict):
        #get all keys with max equal values
        mode = []
        try:
            mode = [key for key in abs_freq_dict.keys() if abs_freq_dict[key] == max(abs_freq_dict.values())]
        except:
            print("An exception occurred while finding mode.")
        return mode

    def calc_scope(self, min, max):
        scope = 0
        try: 
            scope = max[1] - min[1]
        except:
            print("An exception occurred while calculating scope.")
        return scope

    def absolute_frequency(self):
        print("Абсолютни честоти:")
        max_val = 0
        abs_freq_dict = dict()
        try:
            abs_freq_dict = self.abs_freq()
            max_val = self.get_max_value(abs_freq_dict)
        except:
            print("An exception occurred in absolute_frequency().")
        return (max_val, abs_freq_dict)

    def relative_frequency(self):
        print("Релативни честоти:")
        rel_freq_dict = dict()
        try:
            abs_freq_dict = self.abs_freq()
            max_value = self.get_max_value(abs_freq_dict)
            for key, value in abs_freq_dict.items():
                rel_freq_dict[key] = self.calc_rel_freq(value, max_value)
        except:
            print("An exception occurred in relative_frequency().")
        return rel_freq_dict

    def mode(self):
        print("Мода:")
        mode_value = 0
        try:
            abs_freq_dict = self.abs_freq()
            mode_value = self.find_mode(abs_freq_dict)
        except:
            print("An exception occurred in mode().")
        return mode_value

    def scope(self):
        print("Размах:")
        scope_value = 0
        try:
            abs_freq_dict = self.abs_freq()
            scope_value = self.calc_scope(list(abs_freq_dict.items())[0], list(abs_freq_dict.items())[-1])
        except:
            print("An exception occurred in scope().")
        return scope_value