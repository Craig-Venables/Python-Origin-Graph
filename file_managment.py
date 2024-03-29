import os



class directory():
    """
    Class for all functions for data manipulation

    filepath = Filepath of current file used | type: str
    filename = filename of current file used  | type: str
    foldername = foldername used| type: str
    """

    # This class represents all functions for directory management.
    def __init__(self, filepath="", filename="", foldername="", directory_path="") -> None:
        self.filepath = filepath
        self.filename = filename
        self.fol_name = foldername
        self.d_path = directory_path


    def filereader(self):
        with open(self.filepath, "r") as f:  # open the file as read only
            fread = f.readlines()
            fread.pop(0)
            return fread

    def check_if_folder_exists(self):
        if not os.path.exists(str(self.d_path) + '\\' + f"{self.fol_name}"):
            os.makedirs(str(self.d_path) + '\\' + f"{self.fol_name}")
            return f"{self.fol_name}", "exists"
        return 'already exists'
