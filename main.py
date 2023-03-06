import originpro as op
import os
import re
import random
import tkinter as tk
from tkinter import simpledialog
import sys
from pathlib import Path
import Python_origin_functions as pof

#fill this in, give directorys
################################################
#File Paths
working_folder = os.path.dirname(os.path.realpath(__file__)) + '\\'

filename = "a2"
p = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\Devices\Repair a device\90,2000")   #read the path as a string
working_file = p / filename

#templates_folder= link to origin folder
#temporary
# ################################################
def origin_shutdown_exception_hook(exctype, value, traceback):
    '''Ensures Origin gets shut down if an uncaught exception'''
    op.exit()
    sys.__excepthook__(exctype, value, traceback)
if op and op.oext:
    sys.excepthook = origin_shutdown_exception_hook
# Only run if external Python
if op.oext:
    op.set_show(True)


#file paths need sorting here they are layed out
#def make_folder():

# ask user for working folder
# input GUI box
ROOT = tk.Tk()
ROOT.withdraw()
# noinspection PyTypeChecker
user_specif_folder = simpledialog.askstring(title="Working folder",
                                  prompt='please give working folder path'
#check if user made input if not it breaks the sys
pof.empty_variable(user_specif_folder)

#todo Specify folder for task further loop through only text files
#todo specify templates folder and each template as a specific path for easy calling
#todo using os.path.abspath(folder_name) to specifies the origin graph templates  





pof.measurements_present(working_folder,"endurance")
#checks if directory in second argument exists and further if within that file txt files exist

C0,C1 = pof.split_iv_sweep(working_file)

#data from file too list
x_vals = C0
y_vals = C1

#path_file = 'os.path.realpath(__file__)'
# Full path to folder containing this script
#working_folder = os.path.dirname(path_file) + '\\'


# Cloneable template - Example 3
wks = op.new_book('w', hidden = True)[0]
wks.from_list(0,x_vals, 'X Values')
wks.from_list(1,y_vals, 'Y Values')
tmpl = working_folder + 'Graph Templates\\(Iv)_Multi_Sweep_loop_Template(cloneable).otpu'
wks.plot_cloneable(tmpl)

# Tile all windows
op.lt_exec('win-s T')

# Save the project to working folder
# Only save if external Python
if op.oext:
    op.save(working_folder + 'gt_examples2.opju')
# Only run if external Python
if op.oext:
    op.exit()

print ("working folder =" + working_folder)

print (__file__)