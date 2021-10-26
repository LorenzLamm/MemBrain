import os
from utils.parameters import ParameterSettings
from scripts.add_labels_and_distances import add_labels_and_distances
from scripts.data_loading import add_datasplit_to_star, MemBrain_datamodule
from scripts.rotator import compute_all_Euler_angles_for_star, Rotator
from scripts.trainer import MemBrainer
from scripts.clustering import MeanShift_clustering
from scripts.normal_voting import normal_voting_for_star
from utils import inspect_segmentations
from scripts import create_initial_stars
from scripts.sample_points_on_seg import sample_points_on_seg

from time import time



def check_mkdir(directory):
    if not os.path.isdir(directory):
        os.makedirs(directory)

def pipeline_structure(main_directory, tomo_dir=None):
    dirs = []
    dirs.append('cluster_centers')
    dirs.append('cluster_centers/plain')
    dirs.append('cluster_centers/with_orientation')
    dirs.append('cluster_centers/classified')
    dirs.append('gt_coords') # add folder for each tomo
    dirs.append('heatmaps')
    dirs.append('initial_stars')
    dirs.append('mics')
    dirs.append('models')
    dirs.append('positions')
    dirs.append('positions/sampled')
    dirs.append('positions/normals_corrected')
    dirs.append('positions/normals_corrected_with_euler')
    dirs.append('rotated_volumes')
    dirs.append('segs')
    dirs.append('subtomogram_averaging')
    dirs.append('temp_files')
    if tomo_dir is not None:
        for tomo_folder in os.listdir(tomo_dir):
            if os.path.isdir(os.path.join(tomo_dir, tomo_folder)):
                dirs.append(os.path.join('gt_coords', tomo_folder, 'as_xml'))
                dirs.append(os.path.join('gt_coords', tomo_folder, 'as_csv'))
                dirs.append(os.path.join('gt_coords', tomo_folder, 'as_vtp'))
    check_mkdir(main_directory)
    for entry in dirs:
        check_mkdir(os.path.join(main_directory, entry))

def main():
    time_zero = time()
    tomo_dir = '/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/test_data/tomograms'
    pixel_spacing_bin1 = 14.08
    unbinned_offset_Z = 0.
    tomo_binning = 4

    print(1, time() - time_zero)
    project_name = 'trythis'
    project_directory = '/Users/lorenz.lamm/PhD_projects/MemBrain_stuff/test_pipeline'
    project_directory = os.path.join(project_directory, project_name)
    pipeline_structure(project_directory)


    out_star = os.path.join(project_directory, 'initial_stars', project_name + '.star')
    out_star2 = os.path.join(project_directory,'initial_stars', project_name + 'with_inner_outer.star')
    gt_out_dir = os.path.join(project_directory, 'gt_coords')


    print(out_star)
    create_initial_stars.create_initial_stars(tomo_dir, out_star, gt_out_dir, binning=tomo_binning, with_dimi=False,
                                              with_denoised=False, pixel_spacing_bin1=pixel_spacing_bin1,
                                              unbinned_offset_Z=unbinned_offset_Z, training=True)
    print(2, time() - time_zero)

    tomograms_folder = 'tomos'
    membranes_folder = 'membranes'
    meshes_folder = 'meshes'
    pipeline_structure(os.path.join(project_directory), tomo_dir)
    training = True
    particle_orientations = True
    particle_orientations_from = 'membranorama' # 'relion'



    inspect_segmentations.fuse_segmentations_together(out_star, os.path.join(project_directory, 'temp_files/'))
    print(3, time() - time_zero)

    inspect_segmentations.inspect_segmentation_before(out_star, out_star2, os.path.join(project_directory, 'temp_files/'))
    print(4, time() - time_zero)

    normals_star = sample_points_on_seg(project_directory, out_star2, os.path.join(project_directory, 'positions', 'sampled'), max_mb_dist=15)
    # normals_star = os.path.join(os.path.join(project_directory, 'positions', 'sampled'), os.path.basename(out_star2))
    print(5, time() - time_zero)


    normals_corrected_star = normal_voting_for_star(normals_star, os.path.join(project_directory, 'positions', 'normals_corrected'), npr=4)
    # normals_corrected_star = os.path.join(os.path.join(project_directory, 'positions', 'normals_corrected'), os.path.basename(normals_star))

    print(6, time() - time_zero)

    out_star_name = compute_all_Euler_angles_for_star(normals_corrected_star, os.path.join(project_directory, 'positions', 'normals_corrected_with_euler'))
    # out_star_name = os.path.join(os.path.join(project_directory, 'positions', 'normals_corrected_with_euler'), os.path.basename(normals_corrected_star))

    print(7, time() - time_zero)

    settings = ParameterSettings(out_star_name)#
    rotator = Rotator(os.path.join(project_directory, 'rotated_volumes'), out_bins=[4], pred_bin=4,
                                       box_ranges=[6], settings=settings, n_pr=1,
                                       store_dir=os.path.join(project_directory, 'rotated_volumes', 'raw'),
                                       store_normals=True, store_angles=True)
    out_star_name = rotator.rotate_all_volumes()
    # out_star_name = os.path.join(os.path.join(project_directory, 'rotated_volumes'), os.path.basename(out_star_name))

    print(8, time() - time_zero)


    prot_tokens = {'PSII': ['PSII', 'PS2'],
                   'PSI': ['PSI_', 'PS1'],
                   'b6f': ['b6f', 'bf6'],
                   'UK': ['UK', 'unknown']}
    psii_particle = '/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/test_data/particles/structures/Chlamy_C2_14A.mrc'
    b6f_particle = '/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/test_data/particles/structures/Cyt b6f_14A_center.mrc'
    uk_particle = 'sphere3'
    prot_shapes = {'PSII': psii_particle, 'b6f': b6f_particle, 'UK': uk_particle}

    add_labels_and_distances(out_star_name, project_directory, prot_tokens=prot_tokens, prot_shapes=prot_shapes,
                             particle_orientations=True, membranorama_xmls=True)
    print(9, time() - time_zero)


    train_tokens = None
    train_tokens = {'Tomo_17': [('S1_', 'M3')],
                    'Tomo_0002_2': [('S1', 'M10')]}

    val_tokens = {'Tomo_17': [('S1_', 'M2')]}
    # val_tokens = None
    # test_tokens = None
    test_tokens = {'Tomo_0002_2': [('S1', 'M7')]}

    add_datasplit_to_star(out_star_name, val_tokens=val_tokens, train_tokens=train_tokens, test_tokens=test_tokens)

    dm = MemBrain_datamodule(out_star_name, 128, part_dists=['PSII'])

    heatmap_out_dir = os.path.join(project_directory, 'heatmaps')
    trainer = MemBrainer(box_range=6, dm=dm, project_dir=project_directory, star_file=out_star_name, ckpt='/Users/lorenz.lamm/PhD_projects/MemBrain_Python3/Backup_15_09_21/l'
                                                  'ightning_logs/version_54/checkpoints/last.ckpt')
    # trainer.train()
    heatmap_star = trainer.predict(heatmap_out_dir, star_file=out_star_name)
    # heatmap_star = os.path.join(project_directory, 'heatmaps', os.path.basename(out_star_name))

    ms = MeanShift_clustering(heatmap_star, os.path.join(project_directory, 'cluster_centers', 'plain'))
    for bandwidth in [15, 23, 28]:
        cluster_star = ms.start_clustering(bandwidth=bandwidth)
        ms.evaluate_clustering(cluster_star, prot_tokens, bandwidth=bandwidth, store_mb_wise=True)
    ms.store_metrics()


if __name__ == '__main__':
    main()


