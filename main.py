import originpro as op
import os
import re
import random
import tkinter as tk
from tkinter import simpledialog
import sys
from pathlib import Path
import Python_origin_functions as pof

##################################################################################
# Fill in these Values of depending on device
# Area of device electrode
area = 100E-6
# Distance between electrodes (ie active layer height)
distance = 100E-9

# if save file already exists within folder this breaks!
save_file = False
Pictures = True  # export pictures to folder?
Plot_iv_log_only = False
debugging = False
close_origin = False

###################################################################################
# for debugging so please ignore, this removes the popup prompt for directory_path
# files to ignore when looking through directory add as appropriate
ignore_files = ('.ini', '.opju', '.Wdf', '.exe', '.ogwu', '.jpg', '.png')
# for the executable
application_path = os.path.dirname(sys.executable)
python_file_path = os.path.dirname(os.path.realpath(__file__)) + '\\'
graph_template_folder = python_file_path + 'Template folder' + '\\'

if debugging:
    directory_path = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder")

    # directory_path = r("C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder")
# tile windows?
pof.tile_all_windows(False)
##################################################################################

# Ensures Origin gets shut down if an uncaught exception
if op and op.oext:
    sys.excepthook = pof.origin_shutdown_exception_hook
# Only run if external Python
if op.oext:
    op.set_show(True)

# Input GUI box
ROOT = tk.Tk()
ROOT.withdraw()
if not debugging:
    user_data_folder_temp = simpledialog.askstring(title="Working data folder",
                                                   prompt='please give working data folder path')
    directory_path = rf"{user_data_folder_temp}"
    # checks if user made input if not breaks
    pof.empty_variable(user_data_folder_temp)


# loops through directory_path splits data and plots into origin using template from folder
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isdir(file_path):
        # skip directories ie folders
        continue
    # do something with the file
    if not filename.endswith(ignore_files):
        with open(os.path.join(directory_path, filename), 'r') as file:

            #Splits iv sweep into usable arrays
            x_vals, y_vals = pof.split_iv_sweep(file_path)

            # beings the ploting depending on boolean parameters
            if Pictures == True:
                # Graphs use python for the calculations
                pof.plot_into_workbook_cal(x_vals, y_vals, area, distance, graph_template_folder, filename, Plot_iv_log_only)
                if not Plot_iv_log_only == True:
                    pof.check_if_folder_exists(directory_path, 'Exported Graphs png (Transport)')
                    g = op.find_graph()
                    filename_ext = f"{filename}" + '.png'
                    exported_path = directory_path + '\\Exported Graphs png (Transport)'
                    g.save_fig(str(exported_path) + '\\' + f"{filename_ext}", width=500)
                else:
                    pof.check_if_folder_exists(directory_path, 'Exported Graphs png (iv_log)')
                    g = op.find_graph()
                    filename_ext = f"{filename}" + '.png'
                    exported_path = directory_path + '\\Exported Graphs png (iv_log)'
                    g.save_fig(str(exported_path) + '\\' + f"{filename_ext}", width=500)

            else:
                # uses origin for all the calculations this uses a different graph template
                pof.plot_into_workbook(x_vals, y_vals, graph_template_folder, filename, 'MasterTemplate_v2.ogwu')

            # # splits data from file and plots within origin
            # print(f"{filename}")
            #
            # # save fig dosnt work though
            # g = op.find_graph()
            # filename_ext = f"{filename}" + '.png'
            # g.save_fig(str(directory_path) + '\\' + f"{filename_ext}", width=500)
            # print("this is", directory_path)

# Save the project to data folder
if save_file == True:
    if op.oext:
        op.save(str(directory_path) + "\\" + 'Graphs.opju')
        print("saved file in " f"{directory_path}")

# Only run if external Python
if close_origin == True:
    if op.oext:
        op.exit()

print(__file__)
