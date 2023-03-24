import originpro as op
import os
import re
import sys
import Equations as eq
from originpro.graph import GLayer, Axis
#gl.SetData()

def tile_all_windows(x):
    if x == True:
        op.lt_exec('win-s T')

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

# Example graph template
def create_graph_from_template(x_vals,y_vals,graph_template_folder):
    # Cloneable template - Example 3
    wks = op.new_book('w', hidden = True)[0]
    wks.from_list(0,x_vals, 'Voltage')
    wks.from_list(1,y_vals, 'Current')
    tmpl = graph_template_folder / "(Iv)_Multi_Sweep_loop_Template(cloneable).otpu"
    wks.plot_cloneable(tmpl)

def graph_log_iv_merged(voltage_data, current_data,graph_template_folder):
    # Cloneable template - Example 3
    wks = op.new_book('w', hidden = False)[0]
    abs_current = absolute_val(current_data)
    wks.from_list(0, voltage_data, 'Voltage')
    wks.from_list(1, current_data, 'Current')
    wks.from_list(2, abs_current, 'Abs Current')
    tmpl = graph_template_folder / "LOG+IV_loops_merged_template_revisioin_4.0 (cloneable)"
    wks.plot_cloneable(tmpl)

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

def all_graphs_from_template(voltage_data,current_data,area,distance,graph_template_folder):
    wks = op.new_book('w', hidden = False)[0]
    abs_current = absolute_val(current_data)

    # plot first 3 voltage current and abs(current)
    wks.from_list(0, voltage_data, 'Voltage')
    wks.from_list(1, current_data, 'Current')
    wks.from_list(2, abs_current, 'Abs Current')

    # find  positive values for data using functions "rpv"
    voltage_data_positive,current_data_positive = filter_positive_values(voltage_data, current_data)

    # run data through equations for positive values.
    current_density_p = eq.current_density_eq(voltage_data_positive,current_data_positive,area,distance)
    electric_field_p = eq.electric_field_eq(voltage_data_positive,distance)
    current_over_voltage_p = eq.current_over_voltage_eq(voltage_data_positive,current_data_positive)
    voltage_to_the_half_p = eq.voltage_to_the_half_eq(voltage_data_positive)

    # get positive values and plot for positive regions only
    wks.from_list(3, current_density_p, 'Current Density')
    wks.from_list(4, electric_field_p, 'Electric Field')
    wks.from_list(5, current_over_voltage_p, 'Current/Voltage')
    wks.from_list(6, voltage_to_the_half_p, 'Voltage^1/2')

    # find negative values for data using functions "rpv" and "equations"
    voltage_data_negative, current_data_negative = filter_negative_values(voltage_data, current_data)

    # run data through equations for negative values.
    current_density_n = eq.current_density_eq(voltage_data_negative,current_data_negative,area,distance)
    electric_field_n = eq.electric_field_eq(voltage_data_negative,distance)
    current_over_voltage_n = eq.current_over_voltage_eq(voltage_data_negative,current_data_negative)
    voltage_to_the_half_n = eq.voltage_to_the_half_eq(voltage_data_negative)

    # get positive values and plot for positive regions only
    wks.from_list(7, absolute_val(voltage_data_negative), 'abs(Voltage)')
    wks.from_list(8, absolute_val(current_data_negative), 'abs(Current)')
    wks.from_list(9, absolute_val(current_density_n), 'abs(Current Density)')
    wks.from_list(10, absolute_val(electric_field_n), 'abs(Electric Field)')
    wks.from_list(11, absolute_val(current_over_voltage_n), 'abs(Current/Voltage)')
    wks.from_list(12, absolute_val(voltage_to_the_half_n), 'abs(Voltage^1/2)')

    # plots the graph using template provided, must be a clonable template
    tmpl = graph_template_folder / "electron_transport_all(clonable).otpu"
    wks.plot_cloneable(tmpl)


def realtime_monitor(x_vals,y_vals,graph_template_folder):
    wks = op.new_book('w', hidden=True)[0]
    # Load graph template and add plots to both layers
    tmpl = graph_template_folder / "endurance.otpu"
    gr = op.new_graph(template=tmpl)
    op.lt_exec('win -z')  # Maximize the graph window
    gr[0].add_plot(wks, 1, 0, type=230)  # type is template-defined, color is template-defined
    gr[1].add_plot(wks, 1, 0, type=230)  # type is template-defined, color is template-defined

# def change_directory(folders):
#     folders = ["retention", "endurance", "Iv sweeps", "graphs"]
#     for folder in folders:
#         if not os.path.exists(folder):
#             os.makedirs(folder)
#         os.chdir(folder)
#         print(f"Changed directory to {os.getcwd()}")  # prints the current working directory

# def change_directory(folder_name):
#     folders = ["retention", "endurance", "Iv sweeps", "graphs"]
#     for folder in folders:
#         dir_path = folder_name
#         full_path = os.path.join(dir_path, folder)
#         if not os.path.exists(full_path):
#             os.makedirs(full_path)
#         os.chdir(full_path)
#         print(f"Changed directory to {os.getcwd()}")

def check_folders_and_change_directory(folder_name):
    base_dir = os.getcwd() + '\\data'  # get current working directory as the base directory
    folders = ["retention", "endurance", "iv sweeps", "graphs"]
    #changed_dir = base_dir + '\\' folder_name
    for folder in folders:
        full_path = os.path.join(base_dir, folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
    os.chdir(os.path.join(base_dir,folder_name))
    #print(f"Changed directory to {os.getcwd()}")


def measurements_present(working_folder, measurement_type):
    if os.path.exists(working_folder + measurement_type):  # check if folder endurance exists
        if len(os.listdir(working_folder + measurement_type)) == 0:
            return ('folder empty')
        else:
            for fname in os.listdir(working_folder + measurement_type):
                if fname.endswith('.txt'):
                    return ('txt files present')
    else:
        return ('no directory')

def split_iv_sweep(data_file):
    print(f"{data_file}")
    B = filereader(data_file)
    Data = []
    for i, line in enumerate(B):
        C = (line.split('\t'))
        D = []
        for value in C:
            if value != '':
                D.append(float(value))
        Data.append(D)
    C0 = []
    C1 = []
    for value in Data:
        if value != []:
            C0.append(value[0])
            C1.append(value[1])
    return (C0,C1)
def split_endurance_sweep(working_data_folder,filename):
    file_path = working_data_folder + 'data\\endurance\\Endurance 1.8v.txt'
    print(file_path)
    data = []

    # Extract voltage from filename using regular expression
    match = re.search(r"voltage_(\d+)V_", filename)
    if match:
        voltage = int(match.group(1))
        print("Voltage:", voltage)
    else:
        print("Error: could not extract voltage from filename")

    with open(file_path, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            values = line.strip().split()
            values = [float(x) for x in values]  # Ignore the first value of each group
            data.append(values)

    # Separate the columns into individual arrays and remove the titles
    iteration = [row[0] for row in data][1:]
    time_set = [row[1] for row in data][1:]
    current_set = [row[2] for row in data][1:]
    time_reset = [row[3] for row in data][1:]
    current_reset = [row[4] for row in data][1:]

    # Print the results
    print("Iteration:", iteration)
    print("Time (Set):", time_set)
    print("Current (Set):", current_set)
    print("Time (Reset):", time_reset)
    print("Current (Reset):", current_reset)
    return (iteration,time_set,current_set,time_reset,current_reset)

#how to use the above
#endurance_iter, endurance_set_t, endurance_set_i, endurance_reset_t,endurance_reset_i = split_endurance_sweep(working_data_folder,"Endurance 1.8v")

#
def split_retention_sweep(filename):
    iteration = []
    time = []
    current = []
    resistance = []
    # re.search(pattern, string, flags=0)
    # Scan through string looking
    # for the first location where the regular expression pattern
    # produces a match, and return a corresponding match object.
    # Return None if no position in the string matches the pattern;
    # note that this is different from finding a zero-length match at
    # some point in the string.
    # Extract voltage from filename using regular expression
    #match = re.search(r'(?<=v)'\w-, filename)

    match = re.search(r"voltage_(\d+)V_", filename)
    if match:
        voltage = int(match.group(1))
        print("Voltage:", voltage)
    else:
        print("Error: could not extract voltage from filename")

    with open(filename, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            # Split the line into three values and convert them to float
            values = line.strip().split()
            values = [float(x) for x in values[1:]]  # Ignore the first value of each line
            iteration.append(values[0])
            time.append(values[1])
            current.append(values[2])
            resistance.append(voltage / values[2])  # Calculate resistance and add to array

    # Print the results
    print("Iteration:", iteration)
    print("Time:", time)
    print("Current:", current)
    print("Resistance:", resistance)

    return (iteration,time,current,resistance)

def split_endurance_sweep(working_folder,filename):
    file_path = working_folder + 'data\\endurance\\Endurance 1.8v.txt'
    print(file_path)
    data = []

    # Extract voltage from filename using regular expression
    match = re.search(r"voltage_(\d+)V_", filename)
    if match:
        voltage = int(match.group(1))
        print("Voltage:", voltage)
    else:
        print("Error: could not extract voltage from filename")

    with open(file_path, "r") as file:
        next(file)  # Skip the header line
        for line in file:
            # Split the line into two groups of three values and convert them to float
            values = line.strip().split()
            values = [float(x) for x in values[1:]]  # Ignore the first value of each group
            data.append(values)

    # Separate the columns into individual arrays and remove the titles
    iteration = [row[0] for row in data][1:]
    time_set = [row[1] for row in data][1:]
    current_set = [row[2] for row in data][1:]
    time_reset = [row[3] for row in data][1:]
    current_reset = [row[4] for row in data][1:]

    # Print the results
    print("Iteration:", iteration)
    print("Time (Set):", time_set)
    print("Current (Set):", current_set)
    print("Time (Reset):", time_reset)
    print("Current (Reset):", current_reset)
    return (iteration,time_set,current_set,time_reset,current_reset)

def origin_shutdown_exception_hook(exctype, value, traceback):
    '''Ensures Origin gets shut down if an uncaught exception'''
    op.exit()
    sys.__excepthook__(exctype, value, traceback)