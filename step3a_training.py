import os
import argparse
from scripts.data_loading import MemBrain_datamodule
from scripts.trainer import MemBrainer
from config import *

import numpy as np
parser = argparse.ArgumentParser()
parser.add_argument("--ckpt", type=str, default=None, help="Path to model checkpoint. Can be used to continue training")
args = parser.parse_args()

def main():
    #TODO: add choice for max distance during training ( not up to 30 or so)
    project_directory = os.path.join(PROJECT_DIRECTORY, PROJECT_NAME)
    out_star_name = os.path.join(os.path.join(project_directory, 'rotated_volumes'),
                                 PROJECT_NAME + '_with_inner_outer.star')
    dm = MemBrain_datamodule(out_star_name, BATCH_SIZE, part_dists=TRAINING_PARTICLE_DISTS, max_dist=MAX_PARTICLE_DISTANCE)
    trainer = MemBrainer(box_range=BOX_RANGE, dm=dm, project_dir=project_directory, star_file=out_star_name, part_dists=TRAINING_PARTICLE_DISTS,
                         ckpt=args.ckpt, max_epochs=MAX_EPOCHS)
    trainer.train()


if __name__ == '__main__':
    main()