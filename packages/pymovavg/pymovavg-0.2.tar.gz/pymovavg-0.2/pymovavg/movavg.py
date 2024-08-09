# pymovavg/movavg.py

import numpy as np
from collections import deque

def movavg(_signal, window_size=5, mode='mean'):
    if not _signal or window_size <= 0:
        raise ValueError("Signal cannot be empty and window size must be positive.")
    
    result = []
    window = deque(maxlen=window_size)
    
    if mode == 'mean':
        agg_func = np.mean
    elif mode == 'median':
        agg_func = np.median
    else:
        raise ValueError("Mode should be 'mean' or 'median'.")
    
    for value in _signal:
        window.append(value)
        result.append(agg_func(window))
    
    return result

