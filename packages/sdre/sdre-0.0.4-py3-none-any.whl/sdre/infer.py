
class _submodules:
    import numpy as np

    from . model import sample
    from . func import P, E, Var
    from . utils import int_tenexp, flatten, identity, neglog, tenexp, int_reciprocal

_s = _submodules


def exp_fit(data):
    x = []
    n_cells = []
    for key, values in data.items():
        x += list(_s.np.ones_like(values)*key)
        n_cells += values

    n_cells = _s.np.array(n_cells)
    x = _s.np.array(x)
    y = _s.np.log2(n_cells.flatten())

    A = _s.np.vstack([x, _s.np.ones(len(x))]).T

    w, b = _s.np.linalg.lstsq(A, y, rcond=None)[0]

    return w, b, x, y


class LikelihoodModel:
    """

    """
    default_params = {'cct': None, 'logshape': None, 'drate': 0, 'n0': None, 't0': 0}
    default_transform = {'cct': _s.identity, 'logshape': _s.int_tenexp, 'drate': _s.identity, 'n0': round, 't0': _s.identity}


    def __init__(self, data, *, params=default_params, 
            # tau leaping kwargs
            cct=None, bshape=None, drate=None, n0=None, t0=None,
            tau=.1, return_full_states=False, n_samples=100, n_threads=1, 
            rel_tau=True, batch=True, percentile=.99, cpp=True,
            #
            transform=default_transform):
        """

        """

        self.rel_tau = rel_tau
        self.tau = tau
        self.cpp = cpp
        self.batch = batch
        self.percentile = percentile

        self.data = data
        self.n_samples = n_samples
        self.n_threads = n_threads
        self.N = 4 * max(_s.flatten(list(data.values())))
        self.T = max(data.keys())
        self.params = dict(LikelihoodModel.default_params, **params)
        self.transform = dict(LikelihoodModel.default_transform, **transform)

        rate, _, _, _ = exp_fit(data)
        self.mean_cct = 1/rate
        self.transform['cct'] = lambda x: x * self.mean_cct

        # construct prior polytope from positivity constraints
        kmap = {}
        n = 0
        for key, value in self.params.items():
            if value is None:
                kmap[key] = n
                n += 1

        self.A, self.b = _s.np.zeros((2*n, n)), _s.np.zeros(2*n)

        for i, key in enumerate(kmap):
            if key == 'cct': # cct \in [mu_cct/2, 2*mu_cct]
                self.A[2*i,  i] = -1
                self.b[2*i]     = - .5

                self.A[2*i+1,i] =  1
                self.b[2*i+1]   =  2
            if key == 'logshape': # logshape \in [0, 5] => max(k) = 10^5
                self.A[2*i,  i] = -1
                self.b[2*i]     =  0

                self.A[2*i+1,i] =  1
                self.b[2*i+1]   =  5
            if key == 'n0': # n0 \in [1, max(Y_0)]
                self.A[2*i,  i] = -1
                self.b[2*i]     = -1

                self.A[2*i+1,i] =  1
                self.b[2*i+1]   =  _s.np.max(data[0])
            if key == 't0': # t0 \in [0, 2*cct] => t0 <= 2*cct => t0 - 2*cct <= 0
                self.A[2*i,  i] = -1
                self.b[2*i]     =  0

                k = kmap['cct']
                self.A[2*i+1,i] =  1
                self.A[2*i+1,k] = -2
                self.b[2*i+1]   =  0 

        self.x0 = [1, 1, _s.np.median(data[0])] + ( [0] if 't0' in kmap else [] )
        self.t, self.n = None, None


    def _map(self, x):
        k = 0
        for key, value in self.params.items():
            T = self.transform[key]
            if value is None:
                k += 1
                yield T(x[k-1])
            else:
                yield value


    def loglikelihood(t, n, data):
        """

        """
        loglikeli = 0
        for _t in data.keys():
            idx = _s.np.max(_s.np.where(t <= _t)) 
            mean, var = n[:,idx].mean(), _s.np.max([n[:,idx].std(), 1])

            for m in data[_t]:
                loglikeli += - .5 * (m - mean)**2 / var - _s.np.log(var)

        return loglikeli


    def sample(self, x):
        cct, bshape, drate, n0, rel_t0 = self._map(x)

        t0 = cct*rel_t0

        t, n =  _s.sample(cct=cct, bshape=bshape, drate=drate, n0=n0, T=self.T+t0, N=self.N,
                n_samples=self.n_samples, n_threads=self.n_threads, cpp=self.cpp,
                rel_tau=self.rel_tau, batch=self.batch, percentile=self.percentile, tau=self.tau)

        idx = _s.np.max(_s.np.where(t < t0)) if t0 > t[0] else 0

        t = t[:-idx] if idx > 0 else t
        return t, n[:,idx:]


    def compute_negative_log_likelihood(self, x):
        """

        """
        self.t, self.n = self.sample(x)

        return -LikelihoodModel.loglikelihood(self.t, self.n, self.data)

    def param_names(self):
        return list(self.params.keys())

