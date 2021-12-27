
import tensorflow as tf
import zipfile
import os
from jtils.datasets.tf.tfrecords import open_image, load_from_tfr, load_from_tfr, get_basic_preprocess_fn, create_tfrecord_from_dir
from jtils.gdrive import gdrive_download


def download_celeba64(download_dir='./'):
    # download
    file_list = [['1T_FfvbnT7NwqGYwF9-OB4ZBXaTK0hb4c', 'img_align_celeba.zip']]
    gdrive_download(file_list, download_dir=download_dir)

def image_dir_to_tfr(image_dir, tfr_filepath):

    # convert to tfr
    def process_fn(file_path):
        IMG_HEIGHT = 64 
        IMG_WIDTH =  64
        img = open_image(file_path)
        img = tf.image.central_crop(img, 0.7)
        img = tf.image.convert_image_dtype(img, tf.float32)
        img = tf.image.resize(img, [IMG_HEIGHT, IMG_WIDTH])
        return img.numpy()

    create_tfrecord_from_dir(image_dir, process_fn=process_fn, filename =tfr_filepath)

def load_celeba64(data_dir='./', tfr_filename='celeba.tfr', 
                  shuffle_buffer_size = 10000):

    tfr_filepath = os.path.join(data_dir, tfr_filename)
    if tfr_filename not in os.listdir(data_dir):
        # download
        if "img_align_celeba.zip" not in os.listdir(data_dir):
            print('Download')
            download_celeba64(data_dir)
        
        # extract
        if "img_align_celeba" not in os.listdir(data_dir):
            print('Extract')
            with zipfile.ZipFile(os.path.join(data_dir, "img_align_celeba.zip"), "r") as f:
                f.extractall(data_dir)
        
        # convert to tfr
        if tfr_filename not in os.listdir(data_dir):
            print('Convert to tfr')
            image_dir = os.path.join(data_dir, 'img_align_celeba')
            image_dir_to_tfr(image_dir, tfr_filepath)
    
    ds = load_from_tfr(tfr_filepath)

    record_feature_description = {
        'image': tf.io.FixedLenFeature([], tf.string),
    }
    preprocess_fn= get_basic_preprocess_fn(record_feature_description)

    ds = ds.shuffle(shuffle_buffer_size)
    ds = ds.map(preprocess_fn, num_parallel_calls=tf.data.experimental.AUTOTUNE)
    return ds