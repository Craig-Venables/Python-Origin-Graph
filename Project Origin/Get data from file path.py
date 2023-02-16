from pathlib import Path
import os

# Folder Path
path = r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\Device's\Repair a device\90,2000"

# Change the directory
os.chdir(path)

# Read text File


def read_text_file(file_path):
	with open(file_path, 'r') as f:
		print(f.read())


# iterate through all file
for file in os.listdir():
	# Check whether file is in text format or not
	if file.endswith(".txt"):
		file_path = f"{path}\{file}"

		# call read text file function
		read_text_file(file_path)
