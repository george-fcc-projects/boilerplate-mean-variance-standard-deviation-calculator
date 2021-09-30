import numpy as np


def calculate(list):
    if len(list) < 9:
        raise ValueError('List must contain nine numbers.')

    calculations = {}
    numpyArray = np.array(list).reshape([3, 3])
    calculations['mean'] = [np.mean(numpyArray, axis=0).tolist(), np.mean(numpyArray, axis=1).tolist(),
                            np.mean(numpyArray)]
    calculations['variance'] = [np.var(numpyArray, axis=0).tolist(), np.var(numpyArray, axis=1).tolist(),
                                np.var(numpyArray)]
    calculations['standard deviation'] = [np.std(numpyArray, axis=0).tolist(), np.std(numpyArray, axis=1).tolist(),
                                          np.std(numpyArray)]
    calculations['max'] = [np.max(numpyArray, axis=0).tolist(), np.max(numpyArray, axis=1).tolist(), np.max(numpyArray)]
    calculations['min'] = [np.min(numpyArray, axis=0).tolist(), np.min(numpyArray, axis=1).tolist(), np.min(numpyArray)]
    calculations['sum'] = [np.sum(numpyArray, axis=0).tolist(), np.sum(numpyArray, axis=1).tolist(), np.sum(numpyArray)]

    return calculations
