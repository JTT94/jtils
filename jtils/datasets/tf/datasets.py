import tensorflow as tf
import tensorflow_datasets as tfds


def get_read_config(map_parallelization=True):
    dataset_options = tf.data.Options()
    dataset_options.experimental_optimization.map_parallelization = map_parallelization
    read_config = tfds.ReadConfig(options=dataset_options)
    return read_config


def load_tfds(dataset, data_dir, split='train', shuffle_files=True):
    read_config = get_read_config()
    dataset_builder = tfds.builder(dataset, data_dir = data_dir)
    dataset_builder.download_and_prepare(download_dir = data_dir)
    ds = dataset_builder.as_dataset(split=split, shuffle_files=shuffle_files, read_config=read_config)
    return ds