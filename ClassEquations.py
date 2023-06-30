import originpro as op
import sys
import os
import re


def absolute_val(column):
    return [abs(x) for x in column]


def filereader(readthisfile):
    with open(readthisfile, "r") as f:  # open the file as read only
        fread = f.readlines()
        fread.pop(0)
        return fread


def empty_variable(var):
    if var == None or var == "":
        sys.exit("Please" " Enter " "Information")


class functions:
    """
    Class for all functions for data manipulation
    """

    # This class represents all the functions used for sorting the data.
    def __init__(self) -> None:
        pass

    voltage_data = []
    current_data = []

    # return positive values of Voltage and corresponding Current
    def filter_positive_values(voltage_data, current_data):
        result_voltage = []
        result_current = []
        for v, c in zip(voltage_data, current_data):
            if v >= 0:
                result_voltage.append(v)
                result_current.append(c)
            else:
                result_voltage.append(0)
                result_current.append(0)
        return result_voltage, result_current

    def filter_negative_values(voltage_data, current_data):
        """ """
        result_voltage = []
        result_current = []
        for v, c in zip(voltage_data, current_data):
            if v <= 0:
                result_voltage.append(v)
                result_current.append(c)
            else:
                result_voltage.append(0)
                result_current.append(0)
        return absolute_val(result_voltage), absolute_val(result_current)

    def weird_division(n, d):
        return n / d if d else 0

    def zero_devision_check(x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 0

    def current_density_eq(v, i, a, d):
        current_density = []
        for voltage, current in zip(v, i):
            if voltage == 0 or current == 0:
                current_density.append(0)
                # for checking for divide by zero error
                continue
            new_num = (d / ((voltage / current) * a ** 2)) * (voltage / d)
            current_density.append(new_num)
        return current_density

    def electric_field_eq(v, d):
        electric_field = []
        for voltage in v:
            if voltage == 0:
                electric_field.append(0)
                continue
            new_num = voltage / d
            electric_field.append(new_num)
        return electric_field

    def current_over_voltage_eq(v, i):
        current_over_voltage = []
        for voltage, current in zip(v, i):
            if voltage == 0 or current == 0:
                current_over_voltage.append(0)
                # for checking for divide by zero error
                continue
            new_num = current / voltage
            current_over_voltage.append(new_num)
        return current_over_voltage

    def voltage_to_the_half_eq(v):
        voltage_to_the_half = []
        for voltage in v:
            new_num = voltage ** 1 / 2
            voltage_to_the_half.append(new_num)
        return voltage_to_the_half
