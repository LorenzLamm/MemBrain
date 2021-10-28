from scripts.MemBrain_model import MemBrain_model
from pytorch_lightning import Trainer
import numpy as np
import os
from pytorch_lightning.callbacks import ModelCheckpoint
from utils import star_utils, data_utils
from utils.parameters import ParameterSettings
from config import *



def store_pred_results_in_h5(data_dict, out_dir, star_file=None):
    if star_file is not None:
        star_dict = star_utils.read_star_file_as_dict(star_file)
        out_dict = {}
    heatmap_paths = []
    unique_tomos = np.unique(data_dict['tomo_token'])
    for unique_tomo in unique_tomos:
        tomo_mask = data_dict['tomo_token'] == unique_tomo
        cur_tomo_dict = data_dict.copy()
        for key in cur_tomo_dict.keys():
            cur_tomo_dict[key] = cur_tomo_dict[key][tomo_mask]
        cur_stack_mbs = np.unique(np.concatenate((np.expand_dims(cur_tomo_dict['stack_token'], axis=1),
                                                  np.expand_dims(cur_tomo_dict['mb_token'], axis=1)), axis=1), axis=0)
        for unique_stack, unique_mb in cur_stack_mbs:
            if star_file is not None:
                cur_idx = star_utils.find_tomo_mb_idx(unique_tomo, unique_mb, star_dict, stack_token=unique_stack)
                star_utils.merge_line_from_star_dict_to_star_dict(cur_idx, star_dict, out_dict)

            out_file = os.path.join(out_dir, unique_tomo + '_' + unique_stack + '_' + unique_mb + '_heatmap.csv')
            heatmap_paths.append(out_file)
            stack_mask = cur_tomo_dict['stack_token'] == unique_stack
            mb_mask = cur_tomo_dict['mb_token'] == unique_mb
            stack_mb_mask = np.logical_and(stack_mask, mb_mask)

            cur_stack_mb_dict = cur_tomo_dict.copy()
            for key in cur_stack_mb_dict:
                cur_stack_mb_dict[key] = cur_stack_mb_dict[key][stack_mb_mask]
            all_data = None
            for key, entry in cur_stack_mb_dict.items():
                if key in ['tomo_token', 'stack_token', 'mb_token']:
                    continue
                if len(entry.shape) == 1:
                    entry = np.expand_dims(entry, 1)
                if all_data is None:
                    all_data = entry
                else:
                    all_data = np.concatenate((all_data, entry), 1)
            header = ['posX', 'posY', 'posZ']
            for entry in TRAINING_PARTICLE_DISTS:
                if not isinstance(entry, list):
                    header.append('labelDist_' + entry)
                else:
                    token = entry[0]
                    for instance in entry[1:]:
                        token += "_" + instance
                    header.append('labelDist_' + token)

            for entry in TRAINING_PARTICLE_DISTS:
                if not isinstance(entry, list):
                    header.append('predDist_' + entry)
                else:
                    token = entry[0]
                    for instance in entry[1:]:
                        token += "_" + instance
                    header.append('predDist_' + token)
            header += ['normalX', 'normalY', 'normalZ', 'anglePhi', 'angleTheta', 'anglePsi']
            print(len(header), all_data.shape)
            data_utils.store_array_in_csv(out_file, all_data, header=header)
            print(out_file)
            data_utils.convert_csv_to_vtp(out_file, out_file[:-3] + 'vtp', hasHeader=True)
    out_star_file = os.path.join(out_dir, os.path.basename(star_file))
    star_utils.write_star_file_from_dict(out_star_file, out_dict)
    star_utils.add_or_change_column_to_star_file(out_star_file, 'heatmapDir', heatmap_paths)
    return out_star_file



class MemBrainer():
    def __init__(self, box_range, dm, project_dir, star_file, part_dists, ckpt=None, max_epochs=100):
        self.box_range = box_range
        self.project_dir = project_dir
        self.star_file = star_file
        self.settings = ParameterSettings(self.star_file)
        self.max_epochs = max_epochs
        if ckpt is not None:
            self.model = MemBrain_model.load_from_checkpoint(ckpt, box_range=self.box_range, part_dists=part_dists)
        else:
            self.model = MemBrain_model(box_range=self.box_range, part_dists=part_dists)
        self.ckpt_dir = os.path.join(self.project_dir, '../lightning_logs')
        self.dm = dm



    def train(self):
        checkpoint_callback = ModelCheckpoint(monitor='Val_Loss', save_last=True)
        trainer = Trainer(max_epochs=self.max_epochs, callbacks=[checkpoint_callback], default_root_dir=self.ckpt_dir)
        trainer.fit(self.model, self.dm)

    def predict(self, out_dir, star_file=None):
        test_dl = self.dm.test_dataloader()
        preds = []
        all_labels = []
        all_positions = []
        all_tomos = []
        all_stacks = []
        all_mbs = []
        all_normals = []
        all_angles = []
        for batch in test_dl:
            vols, labels, positions, tomo_tokens, stack_tokens, mb_tokens, normals, angles = batch
            for entry, all_entries in [(labels, all_labels), (positions, all_positions), (tomo_tokens, all_tomos),
                                       (stack_tokens, all_stacks), (mb_tokens, all_mbs), (normals, all_normals),
                                       (angles, all_angles)]:
                if isinstance(entry, tuple):
                    all_entries.append(np.array(entry))
                else:
                    all_entries.append(entry.detach())
            batch_pred = self.model(vols)
            preds.append(batch_pred.detach())
        data_dict = {
            'tomo_token': np.concatenate(all_tomos),
            'stack_token': np.concatenate(all_stacks),
            'mb_token': np.concatenate(all_mbs),
            'position': np.concatenate(all_positions),
            'label': np.concatenate(all_labels),
            'pred': np.concatenate(preds),
            'normal': np.concatenate(all_normals),
            'angle': np.concatenate(all_angles)
        }
        consider_bin = self.settings.consider_bin
        data_dict['position'] *= consider_bin
        out_star = store_pred_results_in_h5(data_dict, out_dir, star_file=star_file)
        return out_star

