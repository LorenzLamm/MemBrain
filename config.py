
PROJECT_NAME = 'trythis'
PROJECT_DIRECTORY = '/Users/lorenz.lamm/PhD_projects/MemBrain_stuff/test_pipeline'
TOMO_DIR = '/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/test_data/tomograms'
PIXEL_SPACING_BIN1 = 14.08
UNBINNED_OFFSET_Z = 0.
TOMO_BINNING = 4
LP_CUTOFF = None
N_PR_NORMALVOTING = 4
N_PR_ROTATION = 4




PROT_TOKENS = {'PSII': ['PSII', 'PS2'],
                   'PSI': ['PSI_', 'PS1'],
                   'b6f': ['b6f', 'bf6'],
                   'UK': ['UK', 'unknown']}
# PSII_PARTICLE = '/fs/pool/pool-engel/Lorenz/4Lorenz/structures/Chlamy_C2_14A.mrc'
PSII_PARTICLE = '/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/test_data/particles/structures/Chlamy_C2_14A.mrc'
# B6F_PARTICLE = '/fs/pool/pool-engel/Lorenz/4Lorenz/structures/Cyt b6f_14A_center.mrc'
B6F_PARTICLE = '/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/test_data/particles/structures/Cyt_b6f_14A_center.mrc'
UK_PARTICLE = 'sphere12'
PROT_SHAPES = {'PSII': PSII_PARTICLE, 'b6f': B6F_PARTICLE, 'UK': UK_PARTICLE}


# TRAIN_TOKENS = None
TRAIN_TOKENS = {'Tomo_0002_2': [('S1', 'M7')]}
#
VAL_TOKENS = {'Tomo_0002_2': [('S1', 'M10')]}
# VAL_TOKENS = None
# TEST_TOKENS = None
TEST_TOKENS = {'Tomo_17': [('S1_', 'M2')]}


BOX_RANGE = 6

## Training settings
BATCH_SIZE = 512
MAX_EPOCHS = 1
TRAINING_PARTICLE_DISTS = [['PSII', 'UK'], 'b6f']
MAX_PARTICLE_DISTANCE = 7. # all distances above this value will be capped


## Clustering settings
CLUSTER_BANDWIDTHS = [15, 23, 28]


## Expert settings
MAX_DIST_FROM_MEMBRANE = 15     # maximum distance for points sampled from membrane segmentation. Higher value increases
                                # robustness of normals, but increases computing efforts.
