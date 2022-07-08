# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:22:58 2022
See information here: https://vedo.embl.es/#gallery


Open and display multiple files
1) open files
2) change first line

# FROM: https://github.com/brainglobe/morphapi/blob/master/examples/visualise/visualise_swc.py


@author: tchen
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
inputDir = "orig_swc_file"
outputDir = "new_swc_file"
singleFile = "connected_3D_points_0.swc"


#fp = "examples/example_files/example1.swc"
#fp="RGC9.swc"
#fp="c91662.swc"

# Change working directory to the directory where this script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
currentPath = os.getcwd()
print ("current path is: " + currentPath)

#%% Calculate Total Points in a singular SWC file
# loops through the entire SWC file and counts the lines
# Note: make sure that there is only ONE SWC file in the input directory

# Change working directory to the directory where this script is located
# Change working directory to the directory where this script is located
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)
currentPath = os.getcwd()
#print ("current path is: " + currentPath)

modifySWC = True
inputPath = os.path.join (currentPath , inputDir)
outputPath = os.path.join (currentPath , outputDir)

if (modifySWC):
    #print ("Initial files will be read from " + inputPath)
    
    
    # Retrieve file name
    fname = os.path.join(currentPath, inputDir, singleFile)
    #print ("file = ", file)
    file = open(fname, "r")
    replacement = ""
    # using the for loop
    for points,line in enumerate(file):
        pass
print('Total lines in SWC file', points);
totalPoints = points;

#%%     : 
''' This cell creates new swc files and outputs percentages of the origianl (eg 1% - 100%)

# CELL DESCRIPTION:
# This cell modifies one SWC files in an input directory 
# It takes a percentage of the inital points in SWC file 
# and creates a new SWC file
# The script writes the new files into an output directory
# The cell produces 0.1% increments of the original file
# Note: make sure to clear the output folder if the number of outputted frames is different'''

modifySWC = True
inputPath = os.path.join (currentPath , inputDir)
outputPath = os.path.join (currentPath , outputDir)

#1000 snapshots are created
for x in range(1000):
    if (modifySWC):
        #print("User selected to modify the first section of the SWC file into SOMA type")
        #print ("Initial files will be read from " + inputPath)
        #print ("Modified files will be saved in " + outputPath)
        
        # Retrieve file name
        fname = os.path.join(currentPath, inputDir, singleFile)
        #print ("file = ", file)
    
        # Open file
        file = open(fname, "r")
        replacement = ""
        a = (totalPoints*((x+1)/1000))
        a = int(a)
        for i,line in enumerate(file):
            
            if (i < a):
                replacement = replacement + line
            else:
                break
    
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
        percent = (x+1)/10    
        # Define new file name
        newfname = "new_" + str(percent)+"_" + os.path.basename(fname)
        # Create new file handle
        newfile = os.path.join(outputPath, newfname)
        
        fout = open(newfile, "w")
        fout.write(replacement)
        fout.close()
                
        print("done with SWC file " + str(percent) + "% of original")
    
    else:
        print("User slected to NOT modify the SWC files")
#%% LOOP ON MUltiple SWC
'''
# Use to test files
# The cell loads different swc files and takes snap shots for every generated swc file
# The final SWC rendered is the last file read in
# Note: the rendered should be blank
'''

# Instanciate empty plotter object
vp = Plotter(shape=(1, 1), axes=0, resetcam = True)

# Change working directory to the directory where this script is located
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)
currentPath = os.getcwd()
print ("current path is: " + currentPath + '\n')

# determine path for output folder
outputPath = os.path.join (currentPath , outputDir)
print("next path" + outputPath + '\n')

#Loop on all SWC files in outputPath
for dirs, subdirs, files in os.walk(outputPath):
    nbOfFiles = 0
    #Loop on all files
    for file in files:
        if file.startswith('.DS'):
            print('error')
            continue
        
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
            # under the screenshot function: https://vedo.embl.es/autodocs/content/vedo/plotter.html#vedo.plotter.Plotter.screenshot
            vp.screenshot(filename= str(nbOfFiles)+'_screenshot.png', scale=None)
            # clear funciton under plotter: https://vedo.embl.es/autodocs/content/vedo/plotter.html#vedo.plotter.Plotter.clear
            vp.clear()
        # Keep track of the number of neurons imported
        nbOfFiles = nbOfFiles + 1


vp.show(interactive=True)   

#%% Visualization of 1 cells with VEDO with modified camera
'''
Renders SWC at a specific camera angle
'''

fp = "new_connected_3D_points_3_small.swc"
fileName = fp

# Create vedo actors from the .swc file
neuron = Neuron(data_file=fp)
components, neuron = neuron.create_mesh(
    neurite_radius=4,  #
    soma_color="salmon",  # Specify colors [see vedo.colors for more details]
    apical_dendrites_color="blackboard",
    basal_dendrites_color="orangered",
    axon_color="darkseagreen",
    whole_neuron_color= "cornflowerblue" #"blackboard",
)


vp = Plotter(shape=(1, 1), axes=0, resetcam = True)

vp.add(neuron, render= True)
# Shift c while in interactive mode will output the camera position
# Use the python code template
cam_1 = dict(pos=(2460, 9621, 9093),
           focalPoint=(2954, 5932, 2163),
           viewup=(0.09178, -0.8762, 0.4731),
           distance=7866,
           clippingRange=(5480, 1.091e+4))

vp.show(interactive=True, camera= cam_1)
vp.screenshot(filename='test_screenshot.png', scale=None)
vp.close()

# WILL SAVE FILE INTO X3D format (and associated html file)
if (save):
    #vp.write("man_low.obj")
    #vp.export('man_low.x3d', binary=False)
    vp.export('EC_axon.x3d')
else:
    print ("SAVE option is False. Mesh is not saved as X3D file")
    
#%% LOOP ON MUltiple SWC

'''
Initally renders a sample SWC file to set the camera angle (sharecam = True)
After exiting out of vedo render, the snap shots will be created with chosen camera
Note: the file must be rendered before creating snapshots
    Vedo does not have an option to set the camera without rendering first
'''

# Create vedo actors from the .swc file
neuron = Neuron(data_file=fp)
components, neuron = neuron.create_mesh(
    neurite_radius=4,  #
    soma_color="salmon",  # Specify colors [see vedo.colors for more details]
    apical_dendrites_color="blackboard",
    basal_dendrites_color="orangered",
    axon_color="darkseagreen",
    whole_neuron_color= "cornflowerblue" #"blackboard",
)


vp = Plotter(shape=(1, 1), axes=0, resetcam = True, sharecam = True)

vp.add(neuron, render= True)

vp.show(interactive=True, camera= cam_1)
vp.screenshot(filename='test_screenshot.png', scale=None)
vp.clear()

# Instanciate empty plotter object
#vp = Plotter(shape=(1, 1), axes=0, resetcam = True)

# Change working directory to the directory where this script is located
# abspath = os.path.abspath(__file__)
# dname = os.path.dirname(abspath)
# os.chdir(dname)
currentPath = os.getcwd()
print ("current path is: " + currentPath + '\n')

# determine path for output folder
outputPath = os.path.join (currentPath , outputDir)
print("next path" + outputPath + '\n')
count = 0
#Loop on all SWC files in outputPath
for dirs, subdirs, files in os.walk(outputPath):
    nbOfFiles = 0
    #Loop on all files
    for file in files:
        # mac issues with .DS files
        if file.startswith('.DS'):
            print("error with '.DS' file")
            count = count+1
            continue
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
                whole_neuron_color="limegreen",#"blackboard",
            )
            
            vp.add(neuron, render= True, resetcam= False)
            vp.screenshot(filename= file+'_screenshot.png', scale=None)
            vp.clear()
        # Keep track of the number of neurons imported
        nbOfFiles = nbOfFiles + 1
        
#checks if .ds files are present
print('.dsfiles =' + str(count))
#vp.show(interactive=True, camera = cam_1)   

#@todo MUST CHANGE COLOR FOR EACH CELL (use random colors)!


