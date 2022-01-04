import numpy as np
from sklearn import datasets


# checker/pinwheel/8gaussians can be found at 
# https://github.com/rtqichen/ffjord/blob/994864ad0517db3549717c25170f9b71e96788b1/lib/toy_data.py#L8

def load_twodim(num_samples, dataset):

    if dataset == 'mixture':
        sample = np.random.randn(num_samples, 2)
        p = sample.shape[0]//2
        sample[:p,0] = sample[:p,0]  - 7.
        sample[p:,0] = sample[p:,0] + 7.

    if dataset == 'scurve':
        X, y  = datasets.make_s_curve(n_samples=num_samples, noise=0.0, random_state=None)
        init_sample = X[:,[0,2]]
        scaling_factor = 7
        sample = (init_sample - init_sample.mean()) / init_sample.std() * scaling_factor

    if dataset == 'swiss':
        X, y  = datasets.make_swiss_roll(n_samples=num_samples, noise=0.0, random_state=None)
        init_sample = X[:,[0,2]]
        scaling_factor = 7
        sample = (init_sample - init_sample.mean()) / init_sample.std() * scaling_factor        

    if dataset == 'moon':
        X, y  = datasets.make_moons(n_samples=num_samples, noise=0.0, random_state=None)
        scaling_factor = 7.
        init_sample = X
        sample = (init_sample - init_sample.mean()) / init_sample.std() * scaling_factor

    if dataset == 'circle':
        X, y  = datasets.make_circles(n_samples=num_samples, noise=0.0, random_state=None, factor=.5)
        sample = X * 10

    if dataset == 'checker':
        x1 = np.random.rand(num_samples) * 4 - 2
        x2_ = np.random.rand(num_samples) - np.random.randint(0, 2, num_samples) * 2
        x2 = x2_ + (np.floor(x1) % 2)
        sample = np.concatenate([x1[:, None], x2[:, None]], 1) * 7.5

    if dataset == 'pinwheel':
        radial_std = 0.3
        tangential_std = 0.1
        num_classes = 5
        num_per_class = num_samples // 5
        rate = 0.25
        rads = np.linspace(0, 2 * np.pi, num_classes, endpoint=False)

        features = np.random.randn(num_classes*num_per_class, 2) \
            * np.array([radial_std, tangential_std])
        features[:, 0] += 1.
        labels = np.repeat(np.arange(num_classes), num_per_class)

        angles = rads[labels] + rate * np.exp(features[:, 0])
        rotations = np.stack([np.cos(angles), -np.sin(angles), np.sin(angles), np.cos(angles)])
        rotations = np.reshape(rotations.T, (-1, 2, 2))    
        sample = 7.5 * np.random.permutation(np.einsum("ti,tij->tj", features, rotations))

    if dataset == '8gaussians':
        scale = 4.
        centers = [(1, 0), (-1, 0), (0, 1), (0, -1), (1. / np.sqrt(2), 1. / np.sqrt(2)),
                   (1. / np.sqrt(2), -1. / np.sqrt(2)), (-1. / np.sqrt(2),
                                                         1. / np.sqrt(2)), (-1. / np.sqrt(2), -1. / np.sqrt(2))]
        centers = [(scale * x, scale * y) for x, y in centers]

        sample = []
        for _ in range(num_samples):
            point = np.random.randn(2) * 0.5
            idx = np.random.randint(8)
            center = centers[idx]
            point[0] += center[0]
            point[1] += center[1]
            sample.append(point)
        sample = np.array(sample, dtype="float32")
        sample *= 3

    return sample