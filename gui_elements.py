import tkinter as tk
from tkinter import simpledialog

class GUI:
    """
    Class for the gui

    x = | type: int

    """

    # This class represents all the functions used for sorting the data.
    def __init__(self, voltage_data) -> None:
        self.v_data = voltage_data

        # Input GUI box
        ROOT = tk.Tk()
        ROOT.withdraw()
        if not debugging:
            user_data_folder_temp = simpledialog.askstring(title="Working data folder",
                                                           prompt='please give working data folder path')
            directory_path = rf"{user_data_folder_temp}"
            # checks if user made input if not breaks
            pof.empty_variable(user_data_folder_temp)

