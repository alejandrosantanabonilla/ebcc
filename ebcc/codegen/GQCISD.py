# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 2, 3), ()) * 0.25

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(v.ovov, (0, 1, 2, 3), t1, (2, 1), (0, 3)) * -1.0
    t1new += einsum(v.ovvv, (0, 1, 2, 3), t2, (4, 0, 2, 3), (4, 1)) * -0.5
    t1new += einsum(f.vv, (0, 1), t1, (2, 1), (2, 0))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(v.vvvv, (0, 1, 2, 3), t2, (4, 5, 3, 2), (5, 4, 1, 0)) * -0.5
    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x0 += einsum(v.oovv, (0, 1, 2, 3), t1, (4, 3), (4, 1, 0, 2)) * -1.0
    t1new += einsum(t2, (0, 1, 2, 3), x0, (4, 0, 1, 2), (4, 3)) * -0.5
    x1 = np.zeros((nocc, nvir), dtype=np.float64)
    x1 += einsum(f.ov, (0, 1), (0, 1))
    x1 += einsum(t1, (0, 1), v.oovv, (2, 0, 3, 1), (2, 3))
    t1new += einsum(t2, (0, 1, 2, 3), x1, (0, 2), (1, 3))
    x2 = np.zeros((nocc, nocc), dtype=np.float64)
    x2 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 0, 2, 3), (4, 1)) * -1.0
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(f.oo, (0, 1), (1, 0)) * 2.0
    x3 += einsum(x2, (0, 1), (1, 0))
    t1new += einsum(x3, (0, 1), t1, (0, 2), (1, 2)) * -0.5
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5))
    t2new += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x4, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new += einsum(x4, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x5 = np.zeros((nvir, nvir), dtype=np.float64)
    x5 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 3, 4), (2, 4)) * -1.0
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(x5, (0, 1), t2, (2, 3, 4, 1), (2, 3, 4, 0))
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), v.oovv, (1, 4, 3, 5), (0, 4, 2, 5))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t2, (0, 1, 2, 3), x7, (4, 1, 5, 3), (0, 4, 2, 5))
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x9 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x9, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), f.oo, (4, 1), (4, 0, 2, 3))
    x11 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x11 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(x2, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2))
    x13 += einsum(x11, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x13 += einsum(x12, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    t2new += einsum(x13, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x13, (0, 1, 2, 3), (1, 0, 2, 3))
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(t2, (0, 1, 2, 3), f.vv, (4, 3), (0, 1, 4, 2))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(x14, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x16 += einsum(x15, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x16, (0, 1, 2, 3), (0, 1, 3, 2))
    x17 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x17 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x17 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 5, 2, 3), (1, 0, 5, 4)) * 0.5
    t2new += einsum(x17, (0, 1, 2, 3), t2, (0, 1, 4, 5), (2, 3, 5, 4)) * -0.5

    return {"t1new": t1new, "t2new": t2new}

