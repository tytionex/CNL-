# -*- coding: utf-8 -*-
"""
Created on Tue May 24 13:22:58 2022
See information here: https://vedo.embl.es/#gallery

@author: jmbouteiller
"""

# from brainrender.actors import Volume
# import numpy as np
# #vol = Volume(np.load('data.npy')) #  this will work
# #vol = Volume(np.load('RGC9.swc')) #  this will work
# vol = Volume('RGC9.swc')  # this will work too :)

# # FROM VOLUME TO SURFACE
# from vedo import Volume
# from brainrender import Scene

# #vol = Volume(mydata)
# mesh = vol.isosurface()

# scene = Scene()
# scene.add(mesh)




# FROM: https://github.com/brainglobe/morphapi/blob/master/examples/visualise/visualise_swc.py



from vedo import Plotter

from morphapi.morphology.morphology import Neuron

"""
    This example shows how to use vedo to visualise a 3d reconstruction of a neuron.
    However, the reccomended way to visualise neurons is with brainrender:
    https://github.com/BrancoLab/BrainRender
"""

#fp = "examples/example_files/example1.swc"
#fp="RGC9.swc"
#fp="c91662.swc"
fp = "connected_3D_points_1_modified.swc"

# Create vedo actors from the .swc file
neuron = Neuron(data_file=fp)
components, neuron = neuron.create_mesh(
    neurite_radius=3,  #
    soma_color="salmon",  # Specify colors [see vedo.colors for more details]
    apical_dendrites_color="blackboard",
    basal_dendrites_color="orangered",
    axon_color="darkseagreen",
    #whole_neuron_color="blackboard",
)

# components stores an actor for each neuronal component (dendrites, soma...)
# neuron is a single actor for the entire neuron


# Show neuron as individual components or entire neuron
#vp = Plotter(shape=(1, 2), axes=1)
#Infor on the lotter can be found here: https://vedo.embl.es/autodocs/content/vedo/plotter.html
vp = Plotter(shape=(1, 2), axes=0, resetcam = True)
vp.show(*list(components.values()), at=0, interactive=False)
vp.show(neuron, at=1, interactive=True)

# SAVE 
#vp.write("man_low.obj")
#vp.export('man_low.x3d', binary=False)
vp.export('EC_axon.x3d')