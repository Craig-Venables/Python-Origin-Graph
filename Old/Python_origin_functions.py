import originpro as op
import sys
from Old import Equations as eq


# gl.SetData()

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
def graph_log_iv_merged(voltage_data, current_data, graph_template_folder):
    # Cloneable template - Example 3
    wks = op.new_book('w', hidden=False)[0]
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

def plot_into_workbook(voltage_data, current_data, graph_template_folder,filename,template_name):
    # give the file path of the temple.ogwu
    working_file = graph_template_folder + template_name
    wks = op.load_book(working_file)[0]  # from user file folder

    # Put array into workbook
    wks.from_list(0, voltage_data, 'Voltage')
    wks.from_list(1, current_data, 'Current')

    # fixes name issue, sets names as it's broken in templates, *reportedly fixed now
    wksn = op.find_book()  # Changes workbook name
    wksn.lname = f"{filename}"
    wks.plot_cloneable(graph_template_folder + 'Electron_all_using_otgw.otpu')
    gp = op.find_graph() # changes graph name
    gp.lname = wksn.lname # longname
    #gp.name = wks.name # short name



def plot_into_workbook_cal(voltage_data, current_data, area, distance, graph_template_folder, filename, iv_graphs_yes):
    # This works only for my use case, please ignore

    wks = op.new_book('w', lname=f"{filename}", hidden=False)[0]
    abs_current = absolute_val(current_data)

    # plot first 3 voltage current and abs(current)
    wks.from_list(0, voltage_data, 'Voltage', units='V')
    wks.from_list(1, current_data, 'Current', units='A')
    wks.from_list(2, abs_current, 'Abs Current')

    # find  positive values for data using functions "rpv"
    voltage_data_positive, current_data_positive = filter_positive_values(voltage_data, current_data)

    # run data through equations for positive values.
    current_density_p = eq.current_density_eq(voltage_data_positive, current_data_positive, area, distance)
    electric_field_p = eq.electric_field_eq(voltage_data_positive, distance)
    current_over_voltage_p = eq.current_over_voltage_eq(voltage_data_positive, current_data_positive)
    voltage_to_the_half_p = eq.voltage_to_the_half_eq(voltage_data_positive)

    # get positive values and plot for positive regions only
    wks.from_list(3, current_density_p, 'Current Density', units='A/cm^2')
    wks.from_list(4, electric_field_p, 'Electric Field' , units='V/cm')
    wks.from_list(5, current_over_voltage_p, 'Current/Voltage', units='A/V')
    wks.from_list(6, voltage_to_the_half_p, 'Voltage^1/2', units='V^1/2')

    # find negative values for data using functions "rpv" and "equations"
    voltage_data_negative, current_data_negative = filter_negative_values(voltage_data, current_data)

    # run data through equations for negative values.
    current_density_n = eq.current_density_eq(voltage_data_negative, current_data_negative, area, distance)
    electric_field_n = eq.electric_field_eq(voltage_data_negative, distance)
    current_over_voltage_n = eq.current_over_voltage_eq(voltage_data_negative, current_data_negative)
    voltage_to_the_half_n = eq.voltage_to_the_half_eq(voltage_data_negative)

    # get positive values and plot for positive regions only
    wks.from_list(7, absolute_val(voltage_data_negative), 'abs(Voltage)', units='V')
    wks.from_list(8, absolute_val(current_data_negative), 'abs(Current)', units='A')
    wks.from_list(9, absolute_val(current_density_n), 'abs(Current Density)', units='A/cm^2')
    wks.from_list(10, absolute_val(electric_field_n), 'abs(Electric Field)', units='V/cm')
    wks.from_list(11, absolute_val(current_over_voltage_n), 'abs(Current/Voltage)', units='A/v')
    wks.from_list(12, absolute_val(voltage_to_the_half_n), 'abs(Voltage^1/2)', units='V^1/2')

    # plots the graph using template provided, must be a clonable template
    electron_transport = graph_template_folder + 'Electron_transport_Final.otpu'
    iv_log = graph_template_folder + 'LOG+IV_v3.otpu'

    if not iv_graphs_yes == True:
        wks.plot_cloneable(electron_transport)
    else:
        wks.plot_cloneable(iv_log)

    # Fix short and long names of files
    wks.lname= f"{filename}"
    gp = op.find_graph()
    gp.lname = wks.lname
    gp.name = wks.name

def plot_transport_and_save(directory_path,filename):
    check_if_folder_exists(directory_path, 'Exported Graphs png (Transport)')
    g = op.find_graph()
    filename_ext = f"{filename}" + '.png'
    exported_path = directory_path + '\\Exported Graphs png (Transport)'
    g.save_fig(str(exported_path) + '\\' + f"{filename_ext}")
    print("image saved")

def plot_iv_log_and_save(directory_path,filename):
    check_if_folder_exists(directory_path, 'Exported Graphs png (iv_log)')
    g = op.find_graph()
    filename_ext = f"{filename}" + '.png'
    exported_path = directory_path + '\\Exported Graphs png (iv_log)'
    g.save_fig(str(exported_path) + '\\' + f"{filename_ext}")
    # , width=500
    print ("image saved")


def origin_shutdown_exception_hook(exctype, value, traceback):
    '''Ensures Origin gets shut down if an uncaught exception'''
    op.exit()
    sys.__excepthook__(exctype, value, traceback)

#
# def process_data_folders(parent_folder):
#     # Check if the parent folder exists and is a directory
#     if not os.path.exists(parent_folder) or not os.path.isdir(parent_folder):
#         print("Invalid parent folder path.")
#         return
#
#     # Iterate over subdirectories in the parent folder
#     for folder_name in os.listdir(parent_folder):
#         folder_path = os.path.join(parent_folder, folder_name)
#
#         # Check if the current item is a subdirectory
#         if os.path.isdir(folder_path):
#             # Process the current data folder
#             process_data_folder(folder_path)
#
# def process_data_folder(folder_path):
#     # Implement your graph plotting code here for the specified folder
#     # You can use the 'folder_path' parameter to access the current data folder
#
#     # Example: Print the path of the folder being processed
#     print(f"Processing folder: {folder_path}")
#
#     # Your graph plotting code goes here
#
# # Example usage
# parent_folder = "/path/to/parent/folder"  # Replace with the path to your parent folder
# process_data_folders(parent_folder)
#


