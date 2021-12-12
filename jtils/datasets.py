import tensorflow as tf
import tensorflow_datasets as tfds

def get_read_config(map_parallelization=True, 
                private_threadpool_size=48,
                max_intra_op_parallelism=1):
    dataset_options = tf.data.Options()
    dataset_options.experimental_optimization.map_parallelization = map_parallelization
    dataset_options.experimental_threading.private_threadpool_size = private_threadpool_size
    dataset_options.experimental_threading.max_intra_op_parallelism = max_intra_op_parallelism
    read_config = tfds.ReadConfig(options=dataset_options)
    return read_config

def load_mnist(data_dir, split='train', shuffle_files=True):
    read_config = get_read_config()
    dataset_builder = tfds.builder('mnist', data_dir = data_dir)
    dataset_builder.download_and_prepare(download_dir = data_dir)
    ds = dataset_builder.as_dataset(split=split, shuffle_files=shuffle_files, read_config=read_config)
    return ds


def load_from_tfr(tfrecords_path):
    ds = tf.data.TFRecordDataset(tfrecords_path)
    return ds