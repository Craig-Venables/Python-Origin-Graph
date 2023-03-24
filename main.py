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
# Area of device
area = 100E-6
# Distance between electrodes
distance = 100E-9

# tile windows?
pof.tile_all_windows(False)

# fill these in for filepaths (temp)
graph_template_folder = Path(
    r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\OriginGraph\Graph Templates")
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
# noinspection PyTypeChecker
user_data_folder = Path(
    r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder\Top left 001")
user_save_folder = Path(
    r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder\Origin Graphs")

# user_data_folder = simpledialog.askstring(title="Working data folder",
#                                   prompt='please give working data folder path')
#
# user_save_folder = simpledialog.askstring(title="Save Folder",
#                                   prompt='please give save folder path')

# checks if user made input if not breaks
# pof.empty_variable(user_data_folder)
# pof.empty_variable(user_save_folder)

# loops through directory_path splits data and plots into origin using template from folder
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isdir(file_path):
        # skip directories
        continue
    if filename.endswith(''):
        with open(os.path.join(directory_path, filename), 'r') as file:
            x_vals, y_vals = pof.split_iv_sweep(file_path)
            pof.all_graphs_from_template(x_vals, y_vals, area, distance, graph_template_folder)
            # splits data from file and plots within origin
            print(f"{filename}")

# checks if directory in second argument exists and further if within that file txt files exist
# pof.measurements_present(user_data_folder,"iv sweep")

# todo add save location, check if folder "graphs" exist if not create it
# followed by changing directory into graphs folder and save the document there

# Save the project to working folder
# Only save if external Python
# if op.oext:
#     op.save(user_save_folder / 'gt_examples2.opju')
# # Only run if external Python
# if op.oext:
#     op.exit()


print(__file__)

# other code for later

# Full path to folder containing this script
# path_file = 'os.path.realpath(__file__)'
# his_script_path = os.path.dirname(path_file) + '\\'
