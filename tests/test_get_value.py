import os, sys

sys.path.append('..')

from jtils.config import get_value, load_config, config_eval, clear_hydra
from jtils.files import get_directory, get_filename


config_path = '../configs/mnist.yaml'

cfg = load_config(config_path)

print(get_value('image_size', cfg['data']) == 28 )
