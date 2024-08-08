
class _submodules:
    import numpy as np

_s = _submodules

def flatten(l): # https://stackoverflow.com/questions/952914/how-do-i-make-a-flat-list-out-of-a-list-of-lists
    """
        Flattens a list of lists.
        
        Parameters
        ----------
        l: list
            A list containing lists, which are to be flattened.

        Returns
        -------
        list
            A flattened list containing all the elements from all the lists initially passed.
    """
    return [item for sublist in l for item in sublist]


def identity(x):
    return x

def tenexp(x):
    return 10**x

def int_tenexp(x):
    return int(10**x)

def neglog(x):
    return -_s.np.log10(x)

def int_reciprocal(x):
    return int(1/x)
    #return -_s.np.log10(x)

