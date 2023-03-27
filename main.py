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

# tile windows?
pof.tile_all_windows(False)

# Please add file path for graph templates provided
graph_template_folder = Path(
    r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\OriginGraph\Graph Templates")

###################################################################################
# for debugging use this it removes the popup prompt for directory_path
save_file = False
# if save file already exists this breaks!
debugging = False
close_origin = False
if debugging:
    directory_path = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder")

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
    if filename.endswith(''):
        with open(os.path.join(directory_path, filename), 'r') as file:
            x_vals, y_vals = pof.split_iv_sweep(file_path)
            pof.all_graphs_from_template(x_vals, y_vals, area, distance, graph_template_folder,filename)
            # splits data from file and plots within origin
            print(f"{filename}")

# Save the project to data folder
if not debugging and save_file == True:
    if op.oext:
        op.save(user_data_folder_temp + "\\" + 'graphs_all_within_document.opju')
        print("saved file in " f"{user_data_folder_temp}")

# Only run if external Python
if close_origin == True:
    if op.oext:
        op.exit()

print(__file__)
