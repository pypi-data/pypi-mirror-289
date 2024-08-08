import numpy as np

rng = np.random.default_rng()


def random_image(size: tuple, low=0, high=255, writeable=False) -> np.ndarray:
    img = rng.integers(low, high + 1, size=size, dtype=np.uint8)
    img.setflags(write=writeable)
    return img
