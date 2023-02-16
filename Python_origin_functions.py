import os


##########################################################
#temporary for testing delete after!!!!!!!
working_folder = os.path.dirname(os.path.realpath(__file__)) + '\\'

#
#######################################################
def filereader(readthisfile):
    with open(readthisfile, "r") as f:    #open the file as read only
        fread = f.readlines()
        fread.pop(0)
        return fread
def split_iv_sweep(working_file):
    B = filereader(working_file)
    Data = []
    for i, line in enumerate(B):
        C = (line.split('\t'))
        D = []
        for value in C:
            if value != '':
                D.append(float(value))
        Data.append(D)
    C0 = []
    C1 = []
    for value in Data:
        if value != []:
            C0.append(value[0])
            C1.append(value[1])
    return (C0,C1)

def measurements_present(working_folder,measurement_type):

    if os.path.exists(working_folder + measurement_type ): # check if folder endurance exists
        if len(os.listdir (working_folder + measurement_type)) == 0:
            return('folder empty')
        else:
            for fname in os.listdir (working_folder + measurement_type):
                if fname.endswith('.txt'):
                    return ('txt files present')
    else:
        return ('no directory')


# def split_endurance_sweep(split_endurance_sweep):
#     return(x)
#
#
# def split_retention_sweep(split_retention_sweep):
#     return(x)
