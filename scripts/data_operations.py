#!/usr/bin/python3

from collections import Counter
import operator

PERSENTAGE = 100

class DataOperations:

    def __init__(self, data):
        self.data = data

    ####################################################
    #    function name: calc_abs_freq                  #
    #    function parameters: None                     #
    #    function description: calculate data frequency#
    ####################################################
    def calc_abs_freq(self):
        try:
            dataset = set(self.data)
            abs_freq = {val:self.data.count(val) for val in dataset}
        except:
            print("An exception accurred while calculating absolute frequency.")
        return abs_freq

    ####################################################
    #    function name: sort_abs_freq_dict             #
    #    function parameters: dict abs_dict            #
    #    function description: sort dictionary         #
    ####################################################
    def sort_abs_freq_dict(self, abs_dict):
        try:
            abs_sorted_tuples = sorted(abs_dict.items(), key=operator.itemgetter(1))
            sorted_tuples = {k: v for k, v in abs_sorted_tuples}
        except:
            print("An exception accurred while sorting absolute frequency dictionary.")
        return sorted_tuples

    ####################################################
    #    function name: abs_freq                       #
    #    function parameters: None                     #
    #    function description: calculate and sort      #
    #        data absolute frequency                   #
    ####################################################
    def abs_freq(self):
        abs_freq_dict = None
        try:
            abs_data = self.calc_abs_freq()
            if abs_data is None:
                raise Exception("abs_data is empty.")
            abs_freq_dict = self.sort_abs_freq_dict(abs_data)
            if abs_freq_dict is None:
                raise Exception("abs_freq_dict is empty.")
        except:
            print("An excception accurred in abs_freq()")
        return abs_freq_dict

    ####################################################
    #    function name: get_max_value                  #
    #    function parameters: dict abs_freq_dict       #
    #    function description: summarize all dict      #
    #                           values                 #
    ####################################################
    def get_max_value(self, abs_freq_dict):  
        max_value = 0
        try:
            for key, value in abs_freq_dict.items():
                max_value += value
        except:
            print("An exception occurred while getting max value.")
        return max_value

    ####################################################
    #    function name: calc_rel_freq                  #
    #    function parameters: int value, int max_value #
    #    function description: calculate relative      #
    #                          frequency               #
    ####################################################
    def calc_rel_freq(self, value, max_value):
        rel_freq = 0
        try:
            rel_freq = (value/max_value)*PERSENTAGE
        except:
            print("An exception occurred while calculating relative frequency.")
        return rel_freq

    ####################################################
    #    function name: find_mode                      #
    #    function parameters: dict abs_freq_dict       #
    #    function description: get all keys with max   #
    #                          equal values            #
    ####################################################
    def find_mode(self, abs_freq_dict):
        mode = []
        try:
            mode = [key for key in abs_freq_dict.keys() if abs_freq_dict[key] == max(abs_freq_dict.values())]
        except:
            print("An exception occurred while finding mode.")
        return mode

    ####################################################
    #    function name: calc_scope                     #
    #    function parameters: list min, list max       #
    #    function description: sub min from max        #
    #                         absolute frequencies     #
    ####################################################
    def calc_scope(self, min, max):
        scope = 0
        try: 
            scope = max[1] - min[1]
        except:
            print("An exception occurred while calculating scope.")
        return scope

    ####################################################
    #    function name: absolute_frequency             #
    #    function parameters: None                     #
    #    function description: get absolute frequency  #
    #                         and max value            #
    ####################################################
    def absolute_frequency(self):
        max_val = 0
        abs_freq_dict = dict()
        try:
            abs_freq_dict = self.abs_freq()
            if abs_freq_dict is None:
                raise Exception("abs_freq_dict is empty.")
            max_val = self.get_max_value(abs_freq_dict)
            if max_val is None or max_val < 0:
                raise Exception("max_val is not correct.")
        except:
            print("An exception occurred in absolute_frequency().")
        return (max_val, abs_freq_dict)

    ####################################################
    #    function name: relative_frequency             #
    #    function parameters: None                     #
    #    function description: get relative frequency  #
    #                      and max value which is 100  #
    ####################################################
    def relative_frequency(self):
        rel_freq_dict = dict()
        try:
            abs_freq_dict = self.abs_freq()
            if abs_freq_dict is None:
                raise Exception("abs_freq_dict is empty.")
            max_value = self.get_max_value(abs_freq_dict)
            if max_value is None or max_value < 0:
               raise Exception("max_val is not correct.")
            for key, value in abs_freq_dict.items():
                rel_freq_dict[key] = self.calc_rel_freq(value, max_value)
            if rel_freq_dict is None:
                raise Exception("rel_freq_dict is empty.")    
        except:
            print("An exception occurred in relative_frequency().")
        return (PERSENTAGE, rel_freq_dict)

    ####################################################
    #    function name: mode                           #
    #    function parameters: None                     #
    #    function description: calculate absolute      #
    #              frequency and mode value            #
    ####################################################
    def mode(self):
        mode_value = 0
        try:
            abs_freq_dict = self.abs_freq()
            if abs_freq_dict is None:
                raise Exception("abs_freq_dict is empty.")
            mode_value = self.find_mode(abs_freq_dict)
            if mode_value is None:
                raise Exception("mode value is not correct.")
        except:
            print("An exception occurred in mode().")
        return mode_value

    ####################################################
    #    function name: scope                          #
    #    function parameters: None                     #
    #    function description: calculate absolute      #
    #              frequency and scope value           #
    ####################################################
    def scope(self):
        scope_value = 0
        try:
            abs_freq_dict = self.abs_freq()
            if abs_freq_dict is None:
                raise Exception("abs_freq_dict is empty.")
            scope_value = self.calc_scope(list(abs_freq_dict.items())[0], list(abs_freq_dict.items())[-1])
            if scope_value is None or scope_value < 0:
                raise Exception("scope value is not correct.")
        except:
            print("An exception occurred in scope().")
        return scope_value