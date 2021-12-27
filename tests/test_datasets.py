import sys

sys.path.append('..')


from jtils.datasets.tf import load_celeba64, load_tfds

ds = load_celeba64(data_dir='../data').take(1).cache()
for batch in ds:
    continue
print(batch['image'].numpy().shape, 64**2*3)

ds = load_tfds('mnist', data_dir='../data').take(1).cache()
for batch in ds:
    continue
print(batch['image'].numpy().shape, 28**2)

ds = load_tfds('cifar10', data_dir='../data').take(1).cache()
for batch in ds:
    continue
print(batch['image'].numpy().shape, 32**2*3)