
class _submodules:
    import numpy as np

_s = _submodules


class F:
    """
        CADLAG representation of a step process defined by jump points `t` and 
        corresponding values `n`, s.t. :math`f(t_i) == n_i` and `f(t) == n_i` if 
        :math:`t \in [t_i, t_i+1)`.
        For :math:`t < t_0`, we define `f(t) := n_0`.
    """

    def __init__(self, t, n):
        """
            Construct the CADLAG representation from jump points and corresponding values.
            Note that we require `len(t) == len(n)` for `t`, `n` flattened.

            Parameters
            ----------
            t : list or numpy.array
                Jump points of the function.
                
            n : list or numpy.array
                Values at the jump points of the function.
        """
        t = _s.np.array(t).flatten()
        n = _s.np.array(n).flatten()
        assert len(t) == len(n)

        idx = _s.np.argsort(t)
        self.t = t[idx]
        self.n = n[idx]

    def __call__(self, t):
        """
            Evaluate `f(t)`.

            Parameters
            ----------
            t : float or list
                Query point(s).

            Returns
            -------
            float or numpy.array
                Value at the query point(s).
        """
        tflat = _s.np.array(t).flatten()
        a = _s.np.zeros_like(tflat)
        b = (len(self.n) - 1) * _s.np.ones_like(tflat)

        i = self.t.searchsorted(tflat, side='right') - 1
        i = _s.np.max([a, i], axis=0)
        i = _s.np.min([i, b], axis=0)

        i = i.astype(int)

        return self.n[i] if len(i) > 1 else self.n[i][0]


class P:
    """
        Empirical estimate of the conditional probability of the value of a step process given
        the time.
    """
    def __init__(self, t, ns):
        """
            Construct the estimator from samples of the step process. 
            For every valid index `i`,
            `(ts[i], ns[i])` is a trajectory of a step process defined by jump points and corresponding
            values.
            Note that, we require `len(ts) == len(ns)` and `len(ts[i]) == len(ns[i])` for every valid `i`.

            Parameters:
            -----------
            ts : list
                List of lists of jump points from the trajectory of a step process.

            ns : list or numpy.array
                List of lists of values from the trajectory of a step process.
        """
        #assert len(ts) == len(ns)
        #self.fs = [F(t, n) for t, n in zip(ts, ns)]
        self.fs = [F(t, n) for n in ns]


    def __call__(self, t):
        """
            Estimate the conditional probability of the value of a step process at time `t`.

            Parameters:
            -----------
            t : float
                Time point for which we evaluate the conditional probability.

            Returns
            -------
            n : numpy.array 
                Values with non-zero probability.

            P : numpy.array
                Probabilities corresponding to `n`.
        """
        p = {}
        
        for f in self.fs:
            n = f(t)
            p[n] = 1 if n not in p else p[n] + 1

        n, p = list(p.keys()), list(p.values())
        n, p = _s.np.array(n), _s.np.array(p).astype(float)
        idx = _s.np.argsort(n)
        n = n[idx]
        p = p[idx]

        p /= float(len(self.fs))

        assert len(n) == len(p) 
        return n, p


def E(n, p, h=lambda x: x):
    """
        Compute the expectation of a discrete random variable
        .. math::

            \mathbb{E}_p[h(n)] = \sum_{-\infty}^{\infty} h(n) p(n)

        Note that we require `len(n) == len(p)`

        Parameters
        ----------
        n : list or numpy.array
            Values with non-zero probability

        p : list or numpy.array
            Probabilities corresponding to `n`.

        h : callable, optional
            Function h, for which we compute the expectation. By default this is the identity.
    """
    return (h(n) * p).sum()


def Var(n, p):
    """
        Compute the variance of a discrete random variable
        .. math::

            \mathrm{Var}_p[h(n)] = \sum_{-\infty}^{\infty} h(n)^2 p(n) - \mathbb{E}_p[h(n)]

        Note that we require `len(n) == len(p)`

        Parameters
        ----------
        n : list or numpy.array
            Values with non-zero probability

        p : list or numpy.array
            Probabilities corresponding to `n`.
    """
    return E(n, p, h=lambda x: x**2) - E(n, p)**2

