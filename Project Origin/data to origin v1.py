import os
import originpro as op
from pathlib import Path
op.set_show()

filename = "a2"
p = Path(r"C:\Users\ppxcv1\OneDrive - The University of Nottingham\Documents\Phd\2) Data\Device's\Repair a device\90,2000")   #read the path as a string
q = p / filename


#read the file and open in origin

def filereader(readthisfile):
    with open(readthisfile, "r") as f:    #open the file as read only
        fread = f.read()
        fread=fread[15:]  #removes first line (jankey as hell)
        print(fread)
        return fread


#from old code.
A = filereader(q)
B = A.split('\n')  #belive splits numbers up
# split the data into 3 arrays
Data = []
for i in range(len(B)):
    C = (B[i].split('\t'))
    D = []
    for j in range(len(C)):
        if C[j] != '':
            D.append(float(C[j]))
    Data.append(D)
C0 = []
C1 = []
C2 = []
print (C0)
for i in range(len(Data)):
    if Data[i] != []:
        C0.append(Data[i][0])
        C1.append(Data[i][1])
        #C2.append(Data[i][2])  # remove for non looped data


x_vals = C0
y_vals = C1

wks = op.new_sheet('w')

wks.from_list(0, x_vals, 'X Values')
wks.from_list(1, y_vals, 'Y Values')

gp = op.new_graph()
gl = gp[0]
gl.add_plot(wks, 1, 0)
gl.rescale()

fpath = op.path('u') + 'simple.png'
gp.save_fig(fpath)
print(f'{gl} is exported as {fpath}')
print(op.path('u'))
#op.exit()

