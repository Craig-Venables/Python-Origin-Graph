import originpro as op
import os
import tkinter as tk
from tkinter import simpledialog
import sys
from pathlib import Path
import graph as g
import data_manipulation as dm
import parameters as p


# for the executable
application_path = os.path.dirname(sys.executable)
python_file_path = os.path.dirname(os.path.realpath(__file__)) + '\\'
graph_template_folder = python_file_path + 'Template folder' + '\\'

# for debugging so please ignore, this removes the popup prompt for directory_path
if p.debugging:
    directory_path = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder")

# tile windows?
g.plot.tile_all_windows(False)

# Input GUI box
ROOT = tk.Tk()
ROOT.withdraw()
if not p.debugging:
    user_data_folder_temp = simpledialog.askstring(title="Working data folder",
                                                   prompt='please give working data folder path')
    directory_path = rf"{user_data_folder_temp}"
    # checks if user made input if not breaks
    dm.functions.empty_variable(user_data_folder_temp)

available_plot_types = ['iv_log', 'transport']

# Loop through plot_in_origin using the various plot types defined earlier
for plot_types in available_plot_types:
    g.plot_in_origin(plot_types, p.save_file, directory_path,graph_template_folder)

# loops through directory given called directory path

# gives current file path
print(__file__)
