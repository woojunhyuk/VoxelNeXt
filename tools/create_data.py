import argparse
from pathlib import Path
from pcdet.config import cfg, cfg_from_yaml_file
from pcdet.datasets.kitti.kitti_dataset import create_kitti_infos


def parse_config():
    parser = argparse.ArgumentParser(description='KITTI Dataset Preparation')
    parser.add_argument('--cfg_file', type=str, default='cfgs/dataset_configs/kitti_dataset.yaml',
                        help='config file with dataset settings')
    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = parse_config()

    cfg_from_yaml_file(args.cfg_file, cfg)

    dataset_cfg = cfg.DATA_CONFIG
    class_names = cfg.CLASS_NAMES
    data_path = Path(dataset_cfg.DATA_PATH)
    save_path = data_path 

    create_kitti_infos(
        dataset_cfg=dataset_cfg,
        class_names=class_names,
        data_path=data_path,
        save_path=save_path
    )

