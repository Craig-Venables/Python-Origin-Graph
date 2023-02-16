import originpro as op
import os
import random
import sys
from pathlib import Path
import Python_origin_functions as pof

################################################
#File Paths
working_folder = os.path.dirname(os.path.realpath(__file__)) + '\\'

filename = "a2"
p = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\Devices\Repair a device\90,2000")   #read the path as a string
working_file = p / filename
################################################
def origin_shutdown_exception_hook(exctype, value, traceback):
    '''Ensures Origin gets shut down if an uncaught exception'''
    op.exit()
    sys.__excepthook__(exctype, value, traceback)
if op and op.oext:
    sys.excepthook = origin_shutdown_exception_hook
# Only run if external Python
if op.oext:
    op.set_show(True)

pof.measurements_present(working_folder,"endurance")
#checks if directory and txt files are present using second argument

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