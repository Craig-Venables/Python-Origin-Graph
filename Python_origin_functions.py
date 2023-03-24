import originpro as op
import os
import re
import sys
from originpro.graph import GLayer,Axis
#gl.SetData()

def tile_all_windows(x):
    if x== True:
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

def upper_axis_limit(array):
    array.sort
    return array[-1]
def lower_axis_limit(array):
    array.sort
    return array[0]



def create_graph_from_template(x_vals,y_vals,graph_template_folder):
    # Cloneable template - Example 3
    wks = op.new_book('w', hidden = True)[0]
    wks.from_list(0,x_vals, 'Voltage')
    wks.from_list(1,y_vals, 'Current')
    tmpl = graph_template_folder / "(Iv)_Multi_Sweep_loop_Template(cloneable).otpu"
    wks.plot_cloneable(tmpl)

def create_graph_from_template_iv_log_merged(voltage_data, current_data,graph_template_folder):
    # Cloneable template - Example 3
    wks = op.new_book('w', hidden = False)[0]
    abs_current = absolute_val(current_data)
    wks.from_list(0, voltage_data, 'Voltage')
    wks.from_list(1, current_data, 'Current')
    wks.from_list(2, abs_current, 'Abs Current')
    tmpl = graph_template_folder / "LOG+IV_loops_merged_template_revisioin_4.0 (cloneable)"
    wks.plot_cloneable(tmpl)
    # gl = GLayer
    # gl.rescale('x')
    #rescale graphs in template set too auto

    #todo get rescale to work"AttributeError: 'list' object has no attribute 'obj'"


def create_multi_graph_from_template(x_vals,y_vals,graph_template_folder):
    # Cloneable template - Example 3
    wks = op.new_book('w', hidden = True)[0]
    wks.from_list(0,x_vals, 'X Values')
    wks.from_list(1,y_vals, 'Y Values')
    tmpl = graph_template_folder / "(Iv)_Multi_Sweep_loop_Template(cloneable).otpu"
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

    return (x)

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

#print (working_folder)
#split_endurance_sweep( working_folder,"Endurance 1.8v")

def origin_shutdown_exception_hook(exctype, value, traceback):
    '''Ensures Origin gets shut down if an uncaught exception'''
    op.exit()
    sys.__excepthook__(exctype, value, traceback)