
class _submodules:
    import numpy as np
    import sdre_cpp as cpp

_s = _submodules


def _sample(cct=1, bshape=1, drate=None, t0=0, n0=1, *, T=10, N=None, tau=.1,
        return_full_states=False, n_threads=1, 
        rel_tau=False, batch=False, percentile=.99):
    x = [_s.np.zeros(n0)]
    n = [n0]

    for i in range(int(_s.np.ceil(T/tau))):
        n_steps = _s.np.random.poisson(1/cct/bshape*tau, len(x[-1]))
        y = (x[-1] + n_steps)
        new = len(_s.np.where(y >= bshape)[0])
        y = y % bshape
        y = _s.np.hstack([y, _s.np.zeros(new)])
        x.append(y)
        n.append(len(y))

        if N is not None and n[-1] > N:
            break

    return (t, x) if return_full_states else (t, n)


def sample(cct, bshape=1, drate=None, t0=0, n0=1, *, T=10, N=None, tau=.1,
        return_full_states=False, n_samples=10, n_threads=1, 
        rel_tau=False, batch=False, percentile=.99, cpp=True):
    if rel_tau: 
        t = _s.np.arange(0, T, tau*cct)
    else:
        t = _s.np.arange(0, T, tau)

    if cpp:
        n = _s.cpp.sample(cct=cct, shape=int(bshape), n0=n0, T=T, tau=tau, n_threads=n_threads,
            rel_tau=rel_tau, batch=batch, percentile=percentile, n_samples=n_samples)
    else:
        tau = tau * cct if rel_tau else tau
        n = []
        for _ in range(n_samples):
            n.append(_sample_tauleaping(cct, bshape, 0, n0, T=T, N=N, tau=tau, return_full_states=return_full_states))
        n = np.array(n)

    return t, n

