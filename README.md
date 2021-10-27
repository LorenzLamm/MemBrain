# MemBrain
### Automated detection of membrane-bound proteins

MemBrain is a pipeline for the automated detection of membrane-bound proteins in cryo-electron tomograms. It utilizes 
the geometry of a pre-segmented membrane to reduce the complexity of the detection task. As a result, MemBrain only requires a small amount of 
annotated data (even one single annotated membrane can be enough!) and can generalize well to unseen tomograms and membranes.

### Workflow
#### Inputs
MemBrain takes as an input the 3D segmentation of a membrane, together with the respective tomogram (both in .mrc or .rec format). 

For re-training MemBrain, .csv files or .xml files containing particle positions are required. It is optimized for particle positions outputs 
generated by Membranorama in .xml format. For also taking into account the particle shapes (e.g. elliptic), one will also require low-resolution particle models 
(the ones mapped onto the Membranorama densities), as well as the mesh files corresponding to the membrane segmentations (again, the ones used in Membranorama).
#### Point and normal sampling
As a
