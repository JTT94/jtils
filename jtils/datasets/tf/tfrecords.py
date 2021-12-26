
import tensorflow as tf
import PIL
from tqdm import tqdm
import os


def load_from_tfr(tfrecords_path):
    ds = tf.data.TFRecordDataset(tfrecords_path)
    return ds

def keys_to_record_description(keys):
    if isinstance(keys, str):
        keys = [keys]
    
    return  {
                k : tf.io.FixedLenFeature([], tf.string) for k in keys
            }

def parse_tfr(example_proto, record_feature_description):
    # Parse the input tf.Example proto using the dictionary above.
    bytes_loaded = tf.io.parse_single_example(example_proto, record_feature_description)
    out = {}
    for k,v in bytes_loaded.items():
        out[k] = tf.io.decode_raw(v, out_type=tf.float32)
    return out

def get_basic_preprocess_fn(record_feature_description):
    def preprocess_fn(d):
        return parse_tfr(d, record_feature_description)
    return preprocess_fn
    
def _bytes_feature(value):
    return tf.train.Feature(bytes_list=tf.train.BytesList(value=[value.tobytes()]))


def serialize_record(item):
    """
    Creates a tf.Example message ready to be written to a file.
    """

    feature = {k: _bytes_feature(v) for k, v in item.items()}
            
    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()


def open_image(file_path):
    img = PIL.Image.open(file_path)
    img = tf.keras.preprocessing.image.img_to_array(img)
    return img

    
#function to create tfrecord
def create_tfrecord_from_dir(file_dir, process_fn, filename ='celeba.tfr'):

    with tf.io.TFRecordWriter(filename) as writer:

        for image in tqdm(os.listdir(file_dir)):
            file_path = os.path.join(file_dir,image)
            img = process_fn(file_path)
                            
            example = serialize_record({'image': img})
            writer.write(example)


