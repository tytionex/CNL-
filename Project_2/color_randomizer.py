# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:22:58 2022
See information here: https://vedo.embl.es/#gallery


Open and display multiple files
1) open files
2) change first line

# FROM: https://github.com/brainglobe/morphapi/blob/master/examples/visualise/visualise_swc.py


@author: jmbouteiller
"""
#%% INITIALIZATION OF PATH 







from vedo import Plotter

from morphapi.morphology.morphology import Neuron

import os

"""
    This example shows how to use vedo to visualise a 3d reconstruction of a neuron.
    However, the reccomended way to visualise neurons is with brainrender:
    https://github.com/BrancoLab/BrainRender
"""

save= False
inputDir = "color_original"
outputDir = "color_modified"


#fp = "examples/example_files/example1.swc"
#fp="RGC9.swc"
#fp="c91662.swc"

# Change working directory to the directory where this script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
currentPath = os.getcwd()
print ("current path is: " + currentPath)

#%%     : 
''' This cell converts the first section of the morphology (line 1) from axon 
to soma so that the neuron becomes a valid neuron and may be displayed   
(the rendered will throw an error if there is no soma)

#   CELL DESCRIPTION:
#   This cell modifies all SWC files in an input directory to specify that the 
#   section located in the first line of the file is converted into a soma (not an axon) 
#   (Basically replaces '2' (axon) with a '1' (soma))
#   And writes new files into an output directory
#   Note: This step is time consuming and only needs to be done once! '''

modifySWC = False
inputPath = os.path.join (currentPath , inputDir)
outputPath = os.path.join (currentPath , outputDir)

if (modifySWC):
    print("User selected to modify the first section of the SWC file into SOMA type")
    print ("Initial files will be read from " + inputPath)
    print ("Modified files will be saved in " + outputPath)
    
    
    #Loop on all SWC files 
    for dirs, subdirs, files in os.walk(inputPath):
        #Loop on all files
        for file in files:
            # Retrieve file name
            fname = os.path.join(currentPath, inputDir, file)
            print ("file = ", file)
    
            # Open file
            file = open(fname, "r")
            replacement = ""
            # using the for loop
            for i,line in enumerate(file):
                
                if (i==0):
                    line = line.strip()
                    # Changing character '1' at position 2
                    changes = line[:2] + '1' + line[3:]
                    
                    #changes = line.replace("1 2 ", "1 1 ", 1)
                    replacement = replacement + changes + "\n"
                else:
                    replacement = replacement + line
    
            file.close()
            # opening the new file in write mode
            
            #Make directory if it does NOT exist
            # Check whether the specified path exists or not
            isExist = os.path.exists(outputPath)
            #If it does NOT exist, create it:
            if not isExist:
                print("Directory for modified SWC does NOT exist...")
                # Create a new directory because it does not exist 
                #os.makedirs(outputPath)
                os.mkdir(outputPath)
                print("The new directory is created!")
                
            
            # Define new file name
            newfname = "new_"+ os.path.basename(fname)
            # Create new file handle
            newfile = os.path.join(outputPath, newfname)
            
            fout = open(newfile, "w")
            fout.write(replacement)
            fout.close()
            
        print("done with all files")

else:
    print("User slected to NOT modify the SWC files")

#%% Color randomizer
'''
Randomized colors for different axons (an array of predetermined color outputs)

This is where the colors are from:
https://matplotlib.org/stable/gallery/color/named_colors.html

#   The colors pulled from matplotlib 
#   In "numberOfAxon", you can change the number of Axons that are rendered
#   The cell creates an array of random numbers that will be referenced in the next cell
#   The random function is called so that no duplicate numbers are generated
'''
from random import randint
import random

numberOfAxons = 5
color = ["aliceblue",
    "antiquewhite",
    "aqua",
    "aquamarine",
    "azure",
    "beige",
    "bisque",
    "blanchedalmond",
    "blue",
    "blueviolet",
    "brown",
    "burlywood",
    "cadetblue",
    "chartreuse",
    "chocolate",
    "coral",
    "cornflowerblue",
    "cornsilk",
    "crimson",
    "cyan",
    "darkblue",
    "darkcyan",
    "darkgoldenrod",
    "darkgray",
    "darkgreen",
    "darkkhaki",
    "darkmagenta",
    "darkolivegreen",
    "darkorange",
    "darkorchid",
    "darkred",
    "darksalmon",
    "darkseagreen",
    "darkslateblue",
    "darkslategray",
    "darkturquoise",
    "darkviolet",
    "deeppink",
    "deepskyblue",
    "dimgray",
    "dodgerblue",
    "firebrick",
    "floralwhite",
    "forestgreen",
    "fuchsia",
    "gainsboro",
    "ghostwhite",
    "gold",
    "goldenrod",
    "gray",
    "green",
    "greenyellow",
    "honeydew",
    "hotpink",
    "indianred",
    "indigo",
    "ivory",
    "khaki",
    "lavender",
    "lavenderblush",
    "lawngreen",
    "lemonchiffon",
    "lightblue",
    "lightcoral",
    "lightcyan",
    "lightgray",
    "lightgreen",
    "lightpink",
    "lightsalmon",
    "lightseagreen",
    "lightskyblue",
    "lightsteelblue",
    "lightyellow",
    "lime",
    "limegreen",
    "linen",
    "magenta",
    "maroon",
    "mediumaquamarine",
    "mediumblue",
    "mediumorchid",
    "mediumpurple",
    "mediumseagreen",
    "mediumslateblue",
    "mediumspringgreen",
    "mediumturquoise",
    "mediumvioletred",
    "midnightblue",
    "mintcream",
    "mistyrose",
    "moccasin",
    "navajowhite",
    "navy",
    "oldlace",
    "olive",
    "olivedrab",
    "orange",
    "orangered",
    "orchid",
    "palegoldenrod",
    "palegreen",
    "paleturquoise",
    "palevioletred",
    "papayawhip",
    "peachpuff",
    "peru",
    "pink",
    "plum",
    "powderblue",
    "purple",
    "rebeccapurple",
    "red",
    "rosybrown",
    "royalblue",
    "saddlebrown",
    "salmon",
    "sandybrown",
    "seagreen",
    "seashell",
    "sienna",
    "silver",
    "skyblue",
    "slateblue",
    "slategray",
    "snow",
    "blackboard",
    "springgreen",
    "steelblue",
    "tan",
    "teal",
    "thistle",
    "tomato",
    "turquoise",
    "violet",
    "wheat",
    "white",
    "whitesmoke",
    "yellow",
    "yellowgreen"]
#randomColor = randint(0, 28)
#print(randomColor)
indexList = random.sample(range(138), numberOfAxons+1)
print(indexList)
#%% LOOP ON MUltiple SWC

'''
This renders multiple swc files into one. The axons will each have a different
color. 

#

#Note: Line 317 is for mac users. There is a problem with generating .DS files
when reading in the swc files. This line skips any .DS files that happend to 
appear accidentally. 

'''

from vedo import Plotter
from morphapi.morphology.morphology import Neuron
import os


# Instanciate empty plotter object
vp = Plotter(shape=(1, 1), axes=0, resetcam = True)

# Change working directory to the directory where this script is located
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)
currentPath = os.getcwd()
print ("current path is: " + currentPath)

# determine path for output folder
outputPath = os.path.join (currentPath , outputDir)
nbOfFiles = 0

#Loop on all SWC files in outputPath
for dirs, subdirs, files in os.walk(outputPath):
    nbOfFiles = 0
    #Loop on all files
    for file in files:
        if file.startswith('.DS'):
            continue
        if (nbOfFiles < numberOfAxons):
            # Retrieve file name
            fname = os.path.join(outputPath, file)
            print ("file = ", file)
            print ("fname = ", fname)
    
            neuron = Neuron(data_file= fname)
            components, neuron = neuron.create_mesh(
                neurite_radius=3,  #
                soma_color="salmon",  #@todo Specify different colors for different cells [see vedo.colors for more details]
                apical_dendrites_color="blackboard",
                basal_dendrites_color="orangered",
                axon_color="darkseagreen",
                whole_neuron_color=indexList[nbOfFiles],
            )
            vp.add(neuron, render= True, resetcam=True)
        # Keep track of the number of neurons imported
        nbOfFiles = nbOfFiles + 1
vp.show(interactive=True)   
#vp.screenshot(filename='example_screenshot.png', scale=None)

