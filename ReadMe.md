# Python-Origin-Graph:

This is a simple script to run through a given directory of text files and plot the corresponding graphs; <br />
Iv, Log Iv, Space Charge Limited Current, Poole-Frenkel, Schottky

Please fill in at the top of "main" the area and distance which relates to your device as so including
the path to the graph templates folder;


Area of device electrode <br />
area = 100E-6 <br />
Distance between electrodes (ie active layer height) <br />
distance = 100E-9 <br />

There is currently no exception for python to skip files that arnt txt files, so please make sure that there are only 
txt files and folders within the filepath specified. Due to this is if you set "save file" True you cannot run the
program a second time without deleting/moving the origin file. This will be changed later. 

### Graph Templates:

Please use the template provided as python places the data within the file in specific places however if you want to
edit the file you can do so however make sure you re-save as a cloanable template otherwise this wont work.
(note: for the graph to have the name of the work sheet this needs to be configured within the template)


### Future plans:

If you have any ideas of what to add please let me know, currently this is the next on my list
- Allow the program to skip files that arnt .txt
- Plot all graphs in one master file to see how the IV sweeps change over time. 
- Incorporate the use of endurance and retention graphs
    -automatically and determine which file its reading ie endurance/retention/Iv sweep and plot accordingly
- make the whole program run as an .exe for ease of use. 
<br />
<br />
Cheers, Craig


