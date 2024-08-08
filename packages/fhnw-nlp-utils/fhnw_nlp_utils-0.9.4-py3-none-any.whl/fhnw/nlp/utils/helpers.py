
def indices_to_one_hot(indices, num_labels, dtype=int):
    """Converts a list of indices array to a one-hot encoded matrix

    Parameters
    ----------
    indices: list
        The list containing array of indices
    num_labels: int
        The total number of labels
    dtype: type
        The type of the one-hot encoded elements (e.g. int, np.float32) 
        
    Returns
    -------
    ndarray
        The one-hot encoded matrix
    """
    # https://stackoverflow.com/questions/29034928/pandas-convert-a-column-of-list-to-dummies
    # https://stackoverflow.com/questions/56123419/how-to-cover-a-label-list-under-the-multi-label-classification-context-into-one
    import pandas as pd
    import numpy as np
    import torch

    one_hot = pd.Series(indices)
    # ensure we consider all possible labels (indices might only contain [0,2,5] but we have 10 in total)
    # add a temporal rows with all possible labels
    one_hot[len(one_hot)] = [i for i in range(num_labels)]
    one_hot = one_hot.explode()   
    one_hot = pd.crosstab(one_hot.index, one_hot)
    # remove temporal num_classes row
    one_hot = one_hot.head(-1)
    #one_hot = one_hot.to_numpy()
    one_hot = one_hot.to_numpy(dtype=dtype)
    
    return one_hot
