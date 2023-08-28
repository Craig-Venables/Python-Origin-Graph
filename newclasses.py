# import sys
#
#
# def absolute_val(col):
#     return [abs(x) for x in col]
#
#
# class data:
#     """
#     Class for all functions for data manipulation file reading and equations
#
#     filepath = Filepath of file used | type: str
#     distance = Distance between electrodes default 100E-9 | type: int
#     area = Area between electrodes default 100E-6 | type: int
#
#     """
#
#     # This class represents all the functions used for sorting the data.
#     def __init__(self, filepath="", distance=100E-9, area=100E-6) -> None:
#         # give just file path to the class, and it should do everything inside this class
#         self.distance = distance
#         self.area = area
#         self.filepath = filepath
#
#         # create empty array for appending later
#         self.v_data = []
#         self.c_data = []
#
#         # read file and split data appending v/c data in this class
#
#         self.split_iv_sweep()
#
#         # Values calculated within this class for use later, should run upon creating an instance of this class
#         # calculate all the ps and negative values used later
#         self.v_data_ps, self.c_data_ps = data.filter_positive_values()
#         self.v_data_ng, self.c_data_ng = data.filter_negative_values()
#
#         # Calculate the required values for plotting later
#
#         current_density_ps = self.current_density_eq(self.v_data_ps, self.c_data_ps)
#         current_density_ng = self.current_density_eq(self.v_data_ng, self.c_data_ng)
#         electric_field_ps = self.electric_field_eq(self.v_data_ps)
#         electric_field_ng = self.electric_field_eq(self.v_data_ng)
#         current_over_voltage_ps = self.current_over_voltage_eq(self.v_data_ps, self.c_data_ps)
#         current_over_voltage_ng = self.current_over_voltage_eq(self.v_data_ng, self.c_data_ng)
#         voltage_to_the_half_ps = self.voltage_to_the_half_eq(self.v_data_ps)
#         voltage_to_the_half_ng = self.voltage_to_the_half_eq(self.v_data_ng)
#
#     # Reading the file given in the class and splitting into needed array
#
#     def filereader(self):
#         with open(self.filepath, "r") as f:  # open the file as read only
#             fread = f.readlines()
#             fread.pop(0)
#             return fread
#
#     def split_iv_sweep(self):
#         # print(f"{filepath}")
#         B = self.filereader()
#         # B = fm.directory(self.filepath).filereader()
#         Data = []
#         for i, line in enumerate(B):
#             C = (line.split('\t'))
#             D = []
#             for value in C:
#                 if value != '':
#                     D.append(float(value))
#             Data.append(D)
#         v_data_array = []
#         c_data_array = []
#         for value in Data:
#             if value:
#                 v_data_array.append(value[0])
#                 c_data_array.append(value[1])
#         # Returns array if v_data and c_data
#         self.v_data.append(v_data_array)
#         self.c_data.append(c_data_array)
#         # return v_data_array, c_data_array
#
#     # calculating the positive and negative values for a given array of voltage and current data
#     def filter_positive_values(self):
#         ''' Takes the data given too it within the class (current and voltage arrays)
#         and returns only the positive values in place of zeros if they are negative '''
#         result_voltage_ps = []
#         result_current_ps = []
#         for v, c in zip(self.v_data, self.c_data):
#             if v >= 0:
#                 result_voltage_ps.append(v)
#                 result_current_ps.append(c)
#             else:
#                 result_voltage_ps.append(0)
#                 result_current_ps.append(0)
#         return result_voltage_ps, result_current_ps
#
#     def filter_negative_values(self):
#         ''' Takes the data given too it within the class (current and voltage arrays)
#         and returns only the negative values in place of zeros if they are positive
#         takes arrays '''
#         result_voltage_ng = []
#         result_current_ng = []
#         for v, c in zip(self.v_data, self.c_data):
#             if v <= 0:
#                 result_voltage_ng.append(v)
#                 result_current_ng.append(c)
#             else:
#                 result_voltage_ng.append(0)
#                 result_current_ng.append(0)
#         return absolute_val(result_voltage_ng), absolute_val(result_current_ng)
#
#     # equations for all data within this class
#     def current_density_eq(self, v_data, c_data):
#         current_density = []
#         for voltage, current in zip(v_data, c_data):
#             if voltage == 0 or current == 0:
#                 current_density.append(0)
#                 # for checking for divide by zero error
#                 continue
#             new_num = (self.distance / ((voltage / current) * self.area ** 2)) * (voltage / self.distance)
#             current_density.append(new_num)
#         return current_density
#
#     def electric_field_eq(self, v_data):
#         electric_field = []
#         for voltage in v_data:
#             if voltage == 0:
#                 electric_field.append(0)
#                 continue
#             new_num = voltage / self.distance
#             electric_field.append(new_num)
#         return electric_field
#
#     def current_over_voltage_eq(self, v_data, c_data):
#         # v_data & c_data cant be refered to as self as this needs
#         # positive or negative values only
#         current_over_voltage = []
#         for voltage, current in zip(v_data, c_data):
#             if voltage == 0 or current == 0:
#                 current_over_voltage.append(0)
#                 # for checking for divide by zero error
#                 continue
#             new_num = current / voltage
#             current_over_voltage.append(new_num)
#         return current_over_voltage
#
#     def voltage_to_the_half_eq(self, v_data):
#         voltage_to_the_half = []
#         for voltage in v_data:
#             new_num = voltage ** 1 / 2
#             voltage_to_the_half.append(new_num)
#         return voltage_to_the_half
