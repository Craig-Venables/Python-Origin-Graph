import originpro as op
import os
import tkinter as tk
from tkinter import simpledialog
import sys
from pathlib import Path
import graph as g
import data_manipulation as dm
import parameters as p

# todo need to add a check if the folders and files all ready exist, if so skip this directory!!
#  an exception is needed though so i can overwrite the files already

# todo add push buttons to the gui which determine the parameters in parameters

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

def process_directories_with_exceptions(directory_path):
    # List of folder names to skip
    exceptions = ["Exported Graphs png (iv_log)", "Exported Graphs png (Transport)" ,"device_data_calculations" , "powerpoints" , "0) Polymer thickness"]

    # Walk through the directory and its subdirectories
    for root, dirs, _ in os.walk(directory_path):
        # Create a copy of the list of directories to avoid modifying it while iterating
        dirs_copy = dirs.copy()
        for d in dirs_copy:
            dir_path = os.path.join(root, d)
            if d in exceptions:
                # Skip processing the exception directory
                dirs.remove(d)
            else:
                dir_contents = os.listdir(dir_path)
                print(dir_contents)
                if any(os.path.isfile(os.path.join(dir_path, item)) for item in dir_contents):
                    # Perform your desired action on the directory here
                    for plot_types in available_plot_types:
                        g.plot_in_origin(plot_types, p.save_file, dir_path, graph_template_folder)
                    print(dir_path)
                else:
                    # Handle the case where there are no files in the directory
                    print(f"No files found in {dir_path}")
                    continue


if p.perform_action_on_single_directory:
    for plot_types in available_plot_types:
        g.plot_in_origin(plot_types, p.save_file, directory_path, graph_template_folder)
else:
    process_directories_with_exceptions(directory_path)






# gives current file path
print(__file__)

top_direc = ' '
lower_direct = ' '
