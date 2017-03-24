import numpy as np


def pad(img, max_size, bg_value):
    """Pad image to match given size.

    Args:
        img (~numpy.ndarray): An array to be transformed. This is in
            CHW format.
        max_size (tuple of two ints): the size of output image after
            padding (max_W, max_H).
        bg_value (scalar): value of the padded regions

    Returns:
        ~numpy.ndarray: a padded array in CHW format.

    """
    x_slices, y_slices = _get_pad_slices(img, max_size=max_size)
    out = bg_value * np.ones((img.shape[0],) + max_size, dtype=img.dtype)
    out[:, y_slices, x_slices] = img
    return out


def _get_pad_slices(img, max_size):
    """Get slices needed for padding.

    Args:
        img (~numpy.ndarray): this image is in format CHW.
        max_size (tuple of two ints): (max_W, max_H).
    """
    _, H, W = img.shape

    if W < max_size[0]:
        diff_x = max_size[0] - W
        margin_x = diff_x / 2
        if diff_x % 2 == 0:
            x_slices = slice(int(margin_x), int(max_size[0] - margin_x))
        else:
            x_slices = slice(int(margin_x), int(max_size[0] - margin_x - 1))
    else:
        x_slices = slice(0, int(max_size[0]))

    if H < max_size[1]:
        diff_y = max_size[1] - H
        margin_y = diff_y / 2
        if diff_y % 2 == 0:
            y_slices = slice(int(margin_y), int(max_size[1] - margin_y))
        else:
            y_slices = slice(int(margin_y), int(max_size[1] - margin_y - 1))
    else:
        y_slices = slice(0, int(max_size[1]))
    return x_slices, y_slices
