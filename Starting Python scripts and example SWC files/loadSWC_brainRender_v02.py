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

from morphapi.morphology.morphology import Neuronpsp

import os

"""
    This example shows how to use vedo to visualise a 3d reconstruction of a neuron.
    However, the reccomended way to visualise neurons is with brainrender:
    https://github.com/BrancoLab/BrainRender
"""

save= False
inputDir = "Axons_Tianyuan"
outputDir = "Axons_Tianyuan_modified"


#fp = "examples/example_files/example1.swc"
#fp="RGC9.swc"
#fp="c91662.swc"

# Change working directory to the directory where this script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
currentPath = os.getcwd()
print ("current path is: " + currentPath)

#%% Modification of SWC file: 
''' This cell converts the first section of the morphology (line 1) from axon 
to soma so that the neuron becomes a valid neuron and may be displayed   
(the rendered will throw an error if there is no soma)

# CELL DESCRIPTION:
# This cell modifies all SWC files in an input directory to specify that the 
# section located in the first line of the file is converted into a soma (not an axon) 
# (Basically replaces '2' (axon) with a '1' (soma))
# And writes new files into an output directory
# Note: This step is time consuming and only needs to be done once! '''

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

#%% Visualization of 2 cells with VEDO 
'''
This is an attempt at loading two cells in the renderer. 
Once functional, we will be able to generalize the principles in this script 
to multiple cells
'''

fp = "connected_3D_points_0_small.swc"
fileName = fp


# Create vedo actors from the .swc file
neuron = Neuron(data_file=fp)
components, neuron = neuron.create_mesh(
    neurite_radius=4,  #
    soma_color="salmon",  # Specify colors [see vedo.colors for more details]
    apical_dendrites_color="blackboard",
    basal_dendrites_color="orangered",
    axon_color="darkseagreen",
    whole_neuron_color="darkseagreen",#"blackboard",
)

# components stores an actor for each neuronal component (dendrites, soma...)
# neuron is a single actor for the entire neuron

fp2="new_connected_3D_points_3_small.swc"
#fp2="example3.swc"
# Create vedo actors from the .swc file
neuron2 = Neuron(data_file=fp2)
components2, neuron2 = neuron2.create_mesh(
    neurite_radius=2,  #
    soma_color="salmon",  # Specify colors [see vedo.colors for more details]
    apical_dendrites_color="blackboard",
    basal_dendrites_color="darkseagreen",
    axon_color="orangered",
    #whole_neuron_color="blackboard",
    whole_neuron_color="orangered",   #Note: One can display the neuron as a single object, or as its elements (with each element having a different color)
    
)


# Show neuron as individual components or entire neuron
#vp = Plotter(shape=(1, 2), axes=1)
#Info on the plotter can be found here: https://vedo.embl.es/autodocs/content/vedo/plotter.html
vp = Plotter(shape=(1, 1), axes=0, resetcam = True)
#vp.show(*list(components.values()), at=0, interactive=False)
#vp.show(neuron, at=1, interactive=True)
vp.add(neuron, render= True)
#INITIAL CODE:
# vp = Plotter(shape=(1, 2), axes=0, resetcam = True)
# vp.show(*list(components.values()), at=0, interactive=False)
# vp.show(neuron, at=1, interactive=True)

#vp.add(*list(components2.values()))

#vp.show(*list(components2.values()), at=0, interactive=True)
#vp.show(neuron2, at=0, interactive=True)
vp.add(neuron2, render= True, resetcam=True)

vp.show(interactive=True)

# WILL SAVE FILE INTO X3D format (and associated html file)
if (save):
    #vp.write("man_low.obj")
    #vp.export('man_low.x3d', binary=False)
    vp.export('EC_axon.x3d')
else:
    print ("SAVE option is False. Mesh is not saved as X3D file")
    
#%% LOOP ON MUltiple SWC

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


#Loop on all SWC files in outputPath
for dirs, subdirs, files in os.walk(outputPath):
    nbOfFiles = 0
    #Loop on all files
    for file in files:
        # Keep track of the number of neurons imported
        nbOfFiles = nbOfFiles + 1
        if (nbOfFiles < 3):
            
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
                whole_neuron_color="darkseagreen",#"blackboard",
            )
            vp.add(neuron, render= True, resetcam=True)


vp.show(interactive=True)

#@todo MUST CHANGE COLOR FOR EACH CELL (use random colors)!

