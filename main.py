import originpro as op
import os
import tkinter as tk
from tkinter import simpledialog
import sys
from pathlib import Path
import graph as cg
import data_manipulation as ce
import parameters as p


##################################################################################
# save file?
save_file = True
# export pictures to folder?
Pictures = True
# plot where python does calculations
Plot_iv_log_only = True
# if debugging set True
debugging = False
# Close origin after completion
close_origin = False

###################################################################################
# for debugging so please ignore, this removes the popup prompt for directory_path

# for the executable
application_path = os.path.dirname(sys.executable)
python_file_path = os.path.dirname(os.path.realpath(__file__)) + '\\'
graph_template_folder = python_file_path + 'Template folder' + '\\'

if debugging:
    directory_path = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Desktop\Origin Test Folder")

# tile windows?
cg.plot.tile_all_windows(False)

# Only run if external Python, Opens instance of origin
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
    ce.functions.empty_variable(user_data_folder_temp)

# todo create the main loops as a function adding in the op.oext: function to open multiple instances /
#  of origin graph: try however and find a limit so it dosnot open too many!


# loops through directory given called directory path


# loops through directory_path splits data and plots into origin using template from folder
for filename in os.listdir(directory_path):
    file_path = os.path.join(directory_path, filename)
    if os.path.isdir(file_path):
        # skip directories ie folders
        continue

    # do something with the file
    if not filename.endswith(p.ignore_files):
        with open(os.path.join(directory_path, filename), 'r') as file:

            # Splits iv sweep into usable arrays

            voltage_data, current_data = ce.split_iv_sweep(file_path)

            # beings the plotting depending on boolean parameters
            if Pictures == True:

                # Graphs use python for the calculations
                pg = cg.plot(voltage_data, current_data, directory_path, filename, graph_template_folder)
                pg.plot_origin_using_python()

                if Plot_iv_log_only:

                    pg.plot_iv_log_and_save()

                else:
                    # plots transport where python does all the calculations
                    pg.plot_transport_and_save()
            else:
                # plots transport graphs where origin calculates the columns
                # used for own template
                pg.plot_into_workbook()


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
