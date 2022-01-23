
import matplotlib.pyplot as plt
import numpy as np

def plot_img(img, **kwargs):
    img = img/ 255. if img.max() > 1. else img
    shape = img.shape

    if len(shape) == 1:
        d = np.sqrt(shape[0])
        if int(d) == d:
            img = img.reshape(d,d)
        d = np.sqrt(shape[0]/3)
        if int(d) == d:
            d = int(d)
            img = img.reshape(d,d,3)
        shape = img.shape

    if len(shape) == 3:
        if shape[0] < shape[2]:
            img = np.moveaxis(img, 2, 0)


    plt.imshow(img, **kwargs)


def plot_2d(x, *args, **kwargs):
    plt.plot(x[:,0], x[:,1], *args, **kwargs)