from functools import reduce

import numpy as np


def dcs(channels):
    input_shape = (*channels[0].shape, 3)
    channel_vectors = np.dstack(channels).reshape(-1, 3)
    channel_covariance = np.ma.cov(channel_vectors.T)
    eigenvalues, eigenvectors = np.linalg.eig(channel_covariance)
    # diagonal matrix containing per-band "stretch factors"
    stretch_matrix = np.diag(1 / np.sqrt(eigenvalues))
    # mean values for each channel
    channel_means = np.mean(channel_vectors, axis=0)
    # full transformation matrix:
    # rotates into eigenspace of covariance matrix, applies stretch,
    # rotates back to channelspace, applies sigma scaling
    transformation_matrix = reduce(
        np.dot, [eigenvectors, stretch_matrix, eigenvectors.T]
    )

    # remove mean from each channel, transform, replace mean and add offset
    dcs_vectors = (
        np.dot((channel_vectors - channel_means), transformation_matrix)
        + channel_means
    )
    dcs_array = dcs_vectors.reshape(input_shape)
    # special limiter included ensuite
    for i in range(3):
        c = dcs_array[:, :, i]
        dcs_array[:, :, i] -= c.min()
        dcs_array[:, :, i] *= 1/c.max()
    return dcs_array
