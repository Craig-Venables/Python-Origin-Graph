#fill this in, give directorys
################################################
# #File Paths
# working_folder = os.path.dirname(os.path.realpath(__file__)) + '\\'
#
# filename = "a2"
# p = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\Devices\Repair a device\90,2000")   #read the path as a string
# working_file = p / filename
#
# #templates_folder= link to origin folder
# #temporary
# ################################################

def upper_axis_limit(array):
    array.sort
    return array[-1]
def lower_axis_limit(array):
    array.sort
    return array[0]

def equations(voltage_data,current_data,area,distance):
    v = voltage_data
    i = current_data
    a = area
    d = distance
    current_density = (d / ((v / i) * a**2)) * (v / d)
    electric_field = v / d
    current_over_voltage = i / v
    voltage_to_the_half = v ^ 1 / 2
    return current_density,electric_field,current_over_voltage,voltage_to_the_half

# val1 = zero_devision_check(voltage,current)
# val3 = zero_devision_check(d,val1**a)
# new_num= val3 * (voltage / d)


# Please add file path for graph templates provided
# Please only replace inside the brackets eg Path(r" Your file path "
# graph_template_folder = Path(
#     r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\OriginGraph\Graph Templates")


def check_folders_and_change_directory(folder_name):
    base_dir = os.getcwd() + '\\data'  # get current working directory as the base directory
    folders = ["retention", "endurance", "iv sweeps", "graphs"]
    # changed_dir = base_dir + '\\' folder_name
    for folder in folders:
        full_path = os.path.join(base_dir, folder)
        if not os.path.exists(full_path):
            os.makedirs(full_path)
    os.chdir(os.path.join(base_dir, folder_name))
    # print(f"Changed directory to {os.getcwd()}")


# checks if directory in second argument exists and further if within that file txt files exist
def measurements_present(working_folder, measurement_type):
    if os.path.exists(working_folder + measurement_type):  # check if folder endurance exists
        if len(os.listdir(working_folder + measurement_type)) == 0:
            return 'folder empty'
        else:
            for fname in os.listdir(working_folder + measurement_type):
                if fname.endswith('.txt'):
                    return 'txt files present'
    else:
        return 'no directory'
