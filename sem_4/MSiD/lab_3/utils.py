import numpy as np
from scipy.ndimage.filters import convolve


def hog(image):
    nwin_x = 5
    nwin_y = 5
    B = 7
    (L, C) = np.shape(image)
    H = np.zeros(shape=(nwin_x * nwin_y * B, 1))
    m = np.sqrt(L / 2.0)
    if C is 1:
        raise NotImplementedError
    step_x = np.floor(C / (nwin_x + 1))
    step_y = np.floor(L / (nwin_y + 1))
    cont = 0
    hx = np.array([[1, 0, -1]])
    hy = np.array([[-1], [0], [1]])
    grad_xr = convolve(image, hx, mode='constant', cval=0.0)
    grad_yu = convolve(image, hy, mode='constant', cval=0.0)
    angles = np.arctan2(grad_yu, grad_xr)
    magnit = np.sqrt((grad_yu ** 2 + grad_xr ** 2))
    for n in range(nwin_y):
        for m in range(nwin_x):
            cont += 1
            angles2 = angles[int(n * step_y):int((n + 2) * step_y),
                      int(m * step_x):int((m + 2) * step_x)]
            magnit2 = magnit[int(n * step_y):int((n + 2) * step_y),
                      int(m * step_x):int((m + 2) * step_x)]
            v_angles = angles2.ravel()
            v_magnit = magnit2.ravel()
            bin = 0
            H2 = np.zeros(shape=(B, 1))

            for ang_lim in np.arange(start=-np.pi + 2 * np.pi / B,
                                     stop=np.pi + 2 * np.pi / B,
                                     step=2 * np.pi / B):
                check = v_angles < ang_lim
                v_angles = (v_angles * (~check)) + (check) * 100
                H2[bin] += np.sum(v_magnit * check)
                bin += 1

            H2 = H2 / (np.linalg.norm(H2) + 0.01)
            H[(cont - 1) * B:cont * B] = H2
    return H
