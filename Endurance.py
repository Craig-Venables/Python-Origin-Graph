import tkinter as tk
from tkinter import simpledialog

###############
# this is an experimental section this porbs wont work #
# voltage is needed too calculate rssistance from the data # get from file name?
# check if the file used is an enduramce file#


# 1. determine if its endurance or retention
# 2. read file and find voltage within the title or ask the user



# use the file read thing witin the iile to read the first line, if the file has specifics then
# the  di the specific thing'


#these will not be fully correct, look for soecific words in soecific orders
# the  split them into the correct arrays
Retention = ('Iteration #	Time (s)	Current (Set)')
r_ittereration = []
r_time = []
r_current_s = []

endurance = ('Iteration #	Time (s)	Current (Set)	Time (s)	Current (Reset)')
e_itteration = []
e_time_s = []
e_current_s = []
e_time_r = []
e_current_r = []


def ask_user_for_voltage(filename):
    #here find volthae within filename

    #n add a if this thing breaks ask the user(bellow)
    if True
        # Input GUI box
        ROOT = tk.Tk()
        ROOT.withdraw()
        uservoltage = simpledialog.askstring(title="voltage of filer",
                                                        prompt='please give voltage used within the file')
    return uservoltage