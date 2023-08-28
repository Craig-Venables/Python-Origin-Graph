import sys
import file_managment as fm


def absolute_val(column):
    return [abs(x) for x in column]

def split_iv_sweep(filepath):
    # print(f"{filepath}")
    B = fm.directory(filepath).filereader()
    Data = []
    for i, line in enumerate(B):
        C = (line.split('\t'))
        D = []
        for value in C:
            if value != '':
                D.append(float(value))
        Data.append(D)
    v_data_array = []
    c_data_array = []
    for value in Data:
        if value:
            v_data_array.append(value[0])
            c_data_array.append(value[1])
    # Returns array if v_data and c_data
    return v_data_array, c_data_array





# graph1 = functions(voltage_data,current_data)
# with graph 1 being an instance of functions with data
# graph1.filter_positive_values

class functions:
    """
    Class for all functions for data manipulation

    voltage_data = Voltage data | type: int
    current_data = Current data | type: int
    distance = Distance between electrodes default 100E-9 | type: int
    area = Area between electrodes default 100E-6 | type: int
    filepath = Filepath of file used | type: str
    """

    # This class represents all the functions used for sorting the data.
    def __init__(self, voltage_data, current_data, filepath="", distance=100E-9, area=100E-6) -> None:
        self.v_data = voltage_data
        self.c_data = current_data
        self.distance = distance
        self.area = area
        self.filepath = filepath

        # Values calculated within this class for use later, should run upon creating an instance of this class


        self.v_data_ps, self.c_data_ps = self.filter_positive_values()
        self.v_data_ng, self.c_data_ng = self.filter_negative_values()



        self.direct = fm.directory()
        self.direct.filepath = self.filepath

    # return positive values of Voltage and corresponding Current
    def filter_positive_values(self):
        ''' Takes the data given too it within the class (current and voltage arrays)
        and returns only the positive values in place of zeros if they are negative '''
        result_voltage = []
        result_current = []
        for v, c in zip(self.v_data, self.c_data):
            if v >= 0:
                result_voltage.append(v)
                result_current.append(c)
            else:
                result_voltage.append(0)
                result_current.append(0)
        return result_voltage, result_current

    def filter_negative_values(self):
        ''' Takes the data given too it within the class (current and voltage arrays)
        and returns only the negative values in place of zeros if they are positive
        takes arrays '''
        result_voltage = []
        result_current = []
        for v, c in zip(self.v_data, self.c_data):
            if v <= 0:
                result_voltage.append(v)
                result_current.append(c)
            else:
                result_voltage.append(0)
                result_current.append(0)
        return absolute_val(result_voltage), absolute_val(result_current)

    def weird_division(self, n):
        return n / self.distance if self.distance else 0

    def zero_devision_check(self, x, y):
        try:
            return x / y
        except ZeroDivisionError:
            return 0


    def empty_variable(var):
        if var is None or var == "":
            sys.exit("Please" " Enter " "Information")

    # class equations():
    #     """
    #     Subclass for all equations used within Class for all functions for data manipulation
    #
    #     voltage_data = Voltage data | type: int
    #     current_data = Current data | type: int
    #     distance = Distance between electrodes default 100E-9 | type: int
    #     area = Area between electrodes default 100E-6 | type: int
    #     filepath = Filepath of file used
    #     """
    #
    #     # This class represents all the functions used for sorting the data.
    #     def __init__(self, voltage_data, current_data, distance=100E-9, area=100E-6, filepath) -> None:
    #         self.v_data = voltage_data
    #         self.c_data = current_data
    #         self.distance = distance
    #         self.area = area
    #         self.filepath = filepath

    # Below are the equations used

    def current_density_eq(self, v_data, c_data):
        current_density = []
        for voltage, current in zip(v_data, c_data):
            if voltage == 0 or current == 0:
                current_density.append(0)
                # for checking for divide by zero error
                continue
            new_num = (self.distance / ((voltage / current) * self.area ** 2)) * (voltage / self.distance)
            current_density.append(new_num)
        return current_density

    def electric_field_eq(self, v_data):
        electric_field = []
        for voltage in v_data:
            if voltage == 0:
                electric_field.append(0)
                continue
            new_num = voltage / self.distance
            electric_field.append(new_num)
        return electric_field

    def current_over_voltage_eq(self, v_data, c_data):
        # v_data & c_data cant be refered to as self as this needs
        # positive or negative values only
        current_over_voltage = []
        for voltage, current in zip(v_data, c_data):
            if voltage == 0 or current == 0:
                current_over_voltage.append(0)
                # for checking for divide by zero error
                continue
            new_num = current / voltage
            current_over_voltage.append(new_num)
        return current_over_voltage

    def voltage_to_the_half_eq(self, v_data):
        voltage_to_the_half = []
        for voltage in v_data:
            new_num = voltage ** 1 / 2
            voltage_to_the_half.append(new_num)
        return voltage_to_the_half
