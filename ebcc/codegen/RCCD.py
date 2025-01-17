# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t2=None, **kwargs):
    # energy
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    e_cc = 0
    e_cc += einsum(t2, (0, 1, 2, 3), x0, (0, 1, 2, 3), ()) * 2.0

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t2=None, **kwargs):
    # T amplitudes
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(t2, (0, 1, 2, 3), v.vvvv, (4, 3, 2, 5), (0, 1, 5, 4))
    t2new += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    t2new += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 3, 5), (4, 0, 5, 1)) * -1.0
    t2new += einsum(v.oovv, (0, 1, 2, 3), t2, (1, 4, 5, 3), (0, 4, 5, 2)) * -1.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x1 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5)) * -1.0
    x1 += einsum(v.ovov, (0, 1, 2, 3), x0, (4, 0, 1, 5), (4, 2, 5, 3))
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new += einsum(x1, (0, 1, 2, 3), x2, (4, 1, 3, 5), (0, 4, 2, 5))
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x3 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 0, 3, 5), (4, 2, 5, 1))
    t2new += einsum(x3, (0, 1, 2, 3), t2, (1, 4, 3, 5), (0, 4, 2, 5))
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x4 += einsum(t2, (0, 1, 2, 3), v.ovov, (0, 4, 5, 3), (1, 5, 2, 4))
    t2new += einsum(t2, (0, 1, 2, 3), x4, (4, 1, 5, 2), (0, 4, 5, 3))
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * 3.0
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x6 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x7 = np.zeros((nvir, nvir), dtype=np.float64)
    x7 += einsum(f.vv, (0, 1), (1, 0))
    x7 += einsum(t2, (0, 1, 2, 3), x5, (0, 1, 4, 3), (2, 4)) * -0.5
    x7 += einsum(t2, (0, 1, 2, 3), x6, (0, 1, 4, 2), (3, 4)) * 0.5
    t2new += einsum(x7, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x8 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.3333333333333333
    x9 = np.zeros((nvir, nvir), dtype=np.float64)
    x9 += einsum(f.vv, (0, 1), (1, 0))
    x9 += einsum(x6, (0, 1, 2, 3), t2, (0, 1, 4, 3), (4, 2)) * -0.5
    x9 += einsum(t2, (0, 1, 2, 3), x8, (0, 1, 4, 2), (3, 4)) * -1.5
    t2new += einsum(x9, (0, 1), t2, (2, 3, 4, 1), (2, 3, 4, 0))
    x10 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x10 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x10 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 5, 1, 3), (0, 4, 2, 5))
    t2new += einsum(x10, (0, 1, 2, 3), t2, (0, 2, 4, 5), (1, 3, 4, 5))
    x11 = np.zeros((nocc, nocc), dtype=np.float64)
    x11 += einsum(f.oo, (0, 1), (1, 0))
    x11 += einsum(t2, (0, 1, 2, 3), v.ovov, (0, 2, 4, 3), (1, 4))
    x11 += einsum(t2, (0, 1, 2, 3), x6, (1, 4, 2, 3), (0, 4)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x11, (4, 1), (0, 4, 2, 3)) * -1.0
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x12 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum(f.oo, (0, 1), (1, 0)) * 0.5
    x13 += einsum(t2, (0, 1, 2, 3), x12, (1, 4, 2, 3), (0, 4))
    t2new += einsum(t2, (0, 1, 2, 3), x13, (4, 0), (4, 1, 2, 3)) * -2.0
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x14 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    t2new += einsum(t2, (0, 1, 2, 3), x14, (1, 4, 3, 5), (0, 4, 2, 5)) * 2.0

    return {"t2new": t2new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t2=None, l2=None, **kwargs):
    # L amplitudes
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(l2, (0, 1, 2, 3), v.vvvv, (4, 1, 0, 5), (5, 4, 2, 3))
    l2new += einsum(v.ovov, (0, 1, 2, 3), (3, 1, 2, 0))
    l2new += einsum(v.ovov, (0, 1, 2, 3), l2, (4, 3, 2, 5), (4, 1, 5, 0)) * -1.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), t2, (2, 4, 3, 5), (4, 0, 5, 1))
    l2new += einsum(x0, (0, 1, 2, 3), l2, (4, 2, 5, 0), (4, 3, 5, 1))
    x1 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x1, (4, 5, 0, 2), (1, 3, 4, 5))
    x2 = np.zeros((nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 0, 1), (4, 3))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x2, (4, 3), (1, 4, 0, 2)) * -1.0
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 1), (4, 0))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x3, (4, 2), (3, 1, 4, 0)) * -1.0
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x4 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x4 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x5 = np.zeros((nvir, nvir), dtype=np.float64)
    x5 += einsum(x4, (0, 1, 2, 3), l2, (4, 2, 1, 0), (3, 4))
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(v.ovov, (0, 1, 2, 3), x5, (1, 4), (0, 2, 4, 3)) * 0.5
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), l2, (3, 2, 0, 4), (4, 1))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x8 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x9 = np.zeros((nocc, nocc), dtype=np.float64)
    x9 += einsum(l2, (0, 1, 2, 3), x8, (3, 4, 0, 1), (4, 2))
    x10 = np.zeros((nocc, nocc), dtype=np.float64)
    x10 += einsum(x7, (0, 1), (0, 1))
    x10 += einsum(x9, (0, 1), (1, 0)) * -1.0
    x11 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x11 += einsum(x10, (0, 1), v.ovov, (1, 2, 3, 4), (0, 3, 2, 4)) * 0.5
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3))
    x12 += einsum(x11, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(x12, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x12, (0, 1, 2, 3), (2, 3, 1, 0))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 3, 5), (4, 0, 5, 1))
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), l2, (4, 2, 0, 5), (5, 1, 4, 3))
    l2new += einsum(x14, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x14, (0, 1, 2, 3), (3, 2, 1, 0))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 1, 3), (0, 4, 2, 5))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(x15, (0, 1, 2, 3), l2, (4, 2, 5, 0), (5, 1, 4, 3))
    l2new += einsum(x16, (0, 1, 2, 3), (2, 3, 0, 1)) * 3.0
    l2new += einsum(x16, (0, 1, 2, 3), (3, 2, 1, 0))
    x17 = np.zeros((nvir, nvir), dtype=np.float64)
    x17 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 0, 1), (4, 2))
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(v.ovov, (0, 1, 2, 3), x17, (4, 3), (0, 2, 4, 1))
    x19 = np.zeros((nocc, nocc), dtype=np.float64)
    x19 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 0, 4), (4, 1))
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(x19, (0, 1), v.ovov, (2, 3, 1, 4), (0, 2, 3, 4))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(x18, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x21 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    l2new += einsum(x21, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x21, (0, 1, 2, 3), (2, 3, 1, 0)) * -3.0
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 5, 0), (5, 1, 4, 2))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 0, 5), (5, 1, 4, 3))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3))
    x24 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(v.ovov, (0, 1, 2, 3), x24, (4, 0, 5, 1), (4, 2, 5, 3)) * 2.0
    l2new += einsum(x25, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x25, (0, 1, 2, 3), (3, 2, 1, 0)) * -0.5
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x26 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x27 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x28 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x28 += einsum(t2, (0, 1, 2, 3), x26, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x28 += einsum(x27, (0, 1, 2, 3), t2, (4, 0, 3, 5), (4, 1, 5, 2))
    l2new += einsum(l2, (0, 1, 2, 3), x28, (2, 4, 0, 5), (5, 1, 4, 3))
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x29 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x30 += einsum(x29, (0, 1, 2, 3), l2, (4, 3, 5, 0), (5, 1, 4, 2)) * -0.5
    l2new += einsum(v.ovov, (0, 1, 2, 3), x30, (4, 0, 5, 3), (5, 1, 4, 2)) * 2.0
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x31 += einsum(x27, (0, 1, 2, 3), t2, (0, 4, 3, 5), (4, 1, 5, 2)) * -1.0
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x32 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x31, (0, 1, 2, 3), x32, (4, 0, 5, 2), (3, 5, 1, 4))
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x33 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 1, 5), (4, 0, 5, 3))
    l2new += einsum(l2, (0, 1, 2, 3), x33, (2, 4, 1, 5), (0, 5, 4, 3))
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x34 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 0, 5), (1, 4, 2, 5))
    l2new += einsum(x34, (0, 1, 2, 3), l2, (2, 4, 5, 0), (3, 4, 5, 1))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x35 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * 3.0
    x36 = np.zeros((nvir, nvir), dtype=np.float64)
    x36 += einsum(f.vv, (0, 1), (1, 0))
    x36 += einsum(x35, (0, 1, 2, 3), t2, (0, 1, 4, 3), (4, 2)) * -0.5
    x36 += einsum(t2, (0, 1, 2, 3), x27, (0, 1, 4, 2), (3, 4)) * 0.5
    l2new += einsum(x36, (0, 1), l2, (0, 2, 3, 4), (1, 2, 3, 4))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x37 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.3333333333333333
    x38 = np.zeros((nvir, nvir), dtype=np.float64)
    x38 += einsum(f.vv, (0, 1), (1, 0))
    x38 += einsum(t2, (0, 1, 2, 3), x27, (0, 1, 4, 3), (2, 4)) * -0.5
    x38 += einsum(t2, (0, 1, 2, 3), x37, (0, 1, 4, 2), (3, 4)) * -1.5
    l2new += einsum(x38, (0, 1), l2, (2, 0, 3, 4), (2, 1, 3, 4))
    x39 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x39 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x39 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 5, 3), (0, 4, 1, 5))
    l2new += einsum(x39, (0, 1, 2, 3), l2, (4, 5, 0, 2), (4, 5, 1, 3))
    x40 = np.zeros((nocc, nocc), dtype=np.float64)
    x40 += einsum(f.oo, (0, 1), (1, 0))
    x40 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 0, 2), (1, 4))
    x40 += einsum(t2, (0, 1, 2, 3), x27, (1, 4, 2, 3), (0, 4)) * -1.0
    l2new += einsum(x40, (0, 1), l2, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    x41 = np.zeros((nocc, nocc), dtype=np.float64)
    x41 += einsum(f.oo, (0, 1), (1, 0))
    x41 += einsum(t2, (0, 1, 2, 3), x26, (1, 4, 2, 3), (0, 4)) * 2.0
    l2new += einsum(x41, (0, 1), l2, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x42 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    l2new += einsum(x42, (0, 1, 2, 3), l2, (4, 2, 5, 0), (4, 3, 5, 1)) * 2.0

    return {"l2new": l2new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t2=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM1
    rdm1_f_oo = np.zeros((nocc, nocc), dtype=np.float64)
    rdm1_f_oo += einsum(delta.oo, (0, 1), (1, 0)) * 2.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x0 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm1_f_oo += einsum(x0, (0, 1, 2, 3), t2, (4, 0, 3, 2), (4, 1)) * -1.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.3333333333333333
    x1 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm1_f_oo += einsum(t2, (0, 1, 2, 3), x1, (1, 4, 2, 3), (0, 4)) * -3.0
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    rdm1_f_vv = np.zeros((nvir, nvir), dtype=np.float64)
    rdm1_f_vv += einsum(x2, (0, 1, 2, 3), l2, (4, 2, 1, 0), (4, 3))
    rdm1_f_ov = np.zeros((nocc, nvir), dtype=np.float64)
    rdm1_f_vo = np.zeros((nvir, nocc), dtype=np.float64)

    rdm1_f = np.block([[rdm1_f_oo, rdm1_f_ov], [rdm1_f_vo, rdm1_f_vv]])

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t2=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM2
    rdm2_f_oooo = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovv = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvoo = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x1 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x1 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 4, 5), (4, 5, 0, 1)) * 0.5
    rdm2_f_oooo += einsum(x1, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_oooo += einsum(x1, (0, 1, 2, 3), (2, 3, 1, 0))
    rdm2_f_oooo += einsum(x1, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_oooo += einsum(x1, (0, 1, 2, 3), (2, 3, 1, 0))
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(x2, (0, 1, 2, 3), l2, (3, 2, 4, 1), (4, 0))
    x4 = np.zeros((nocc, nocc), dtype=np.float64)
    x4 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 1, 4), (4, 0)) * 0.3333333333333333
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(x3, (0, 1), (0, 1))
    x5 += einsum(x4, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 0, 2)) * -1.5
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 0, 2)) * 1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 0, 1, 2)) * 1.5
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * -1.5
    x6 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1))
    rdm2_f_oooo += einsum(x6, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x6, (0, 1, 2, 3), (3, 2, 1, 0))
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 1, 4), (4, 0))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x8 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_vovo = np.zeros((nvir, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_vovo += einsum(x8, (0, 1, 2, 3), t2, (4, 0, 3, 5), (2, 4, 5, 1)) * -1.0
    x9 = np.zeros((nocc, nocc), dtype=np.float64)
    x9 += einsum(t2, (0, 1, 2, 3), x8, (1, 4, 3, 2), (0, 4))
    x10 = np.zeros((nocc, nocc), dtype=np.float64)
    x10 += einsum(x7, (0, 1), (0, 1))
    x10 += einsum(x9, (0, 1), (1, 0)) * -1.0
    rdm2_f_oooo += einsum(x10, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(x10, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_oooo += einsum(x10, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(x10, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * 0.5
    x11 = np.zeros((nocc, nocc), dtype=np.float64)
    x11 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 1), (4, 0))
    rdm2_f_oooo += einsum(x11, (0, 1), delta.oo, (2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x11, (2, 3), (3, 1, 2, 0)) * -1.5
    rdm2_f_oooo += einsum(x11, (0, 1), delta.oo, (2, 3), (2, 1, 3, 0)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x11, (2, 3), (3, 1, 2, 0)) * -0.5
    x12 = np.zeros((nocc, nocc), dtype=np.float64)
    x12 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 0, 4), (4, 1))
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum(delta.oo, (0, 1), (1, 0))
    x13 += einsum(x12, (0, 1), (0, 1)) * -1.0
    rdm2_f_oooo += einsum(x13, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    x14 = np.zeros((nocc, nocc), dtype=np.float64)
    x14 += einsum(delta.oo, (0, 1), (1, 0)) * -1.0
    x14 += einsum(x12, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(x14, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.0
    x15 = np.zeros((nocc, nocc), dtype=np.float64)
    x15 += einsum(x0, (0, 1, 2, 3), x8, (1, 4, 3, 2), (0, 4))
    x16 = np.zeros((nocc, nocc), dtype=np.float64)
    x16 += einsum(x12, (0, 1), (0, 1)) * 2.0
    x16 += einsum(x15, (0, 1), (1, 0))
    rdm2_f_oooo += einsum(x16, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x16, (2, 3), (1, 3, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x16, (2, 3), (3, 0, 1, 2)) * 0.5
    rdm2_f_oooo += einsum(x16, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * -0.5
    x17 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x17 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 4, 5), (4, 5, 0, 1))
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x18 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(x18, (0, 1, 2, 3), x17, (0, 1, 4, 5), (4, 5, 2, 3)) * -0.25
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x20 += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x20, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x20, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x21 = np.zeros((nocc, nocc), dtype=np.float64)
    x21 += einsum(x2, (0, 1, 2, 3), l2, (3, 2, 4, 1), (4, 0)) * 3.0
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 1, 4), (4, 0))
    x23 = np.zeros((nocc, nocc), dtype=np.float64)
    x23 += einsum(x21, (0, 1), (0, 1))
    x23 += einsum(x22, (0, 1), (0, 1))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(x23, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 0.5
    rdm2_f_oovv += einsum(x24, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x24, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x24, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x25 = np.zeros((nvir, nvir), dtype=np.float64)
    x25 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 0, 1), (4, 2))
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(t2, (0, 1, 2, 3), x25, (2, 4), (0, 1, 4, 3))
    rdm2_f_oovv += einsum(x26, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    rdm2_f_oovv += einsum(x26, (0, 1, 2, 3), (0, 1, 3, 2))
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 5, 1), (5, 0, 4, 2))
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(t2, (0, 1, 2, 3), x27, (1, 4, 3, 5), (0, 4, 2, 5))
    rdm2_f_oovv += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x28, (0, 1, 2, 3), (0, 1, 3, 2)) * -3.0
    rdm2_f_oovv += einsum(x28, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x28, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 1, 5), (5, 0, 4, 2))
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(x29, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x31 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 5, 1), (5, 0, 4, 3))
    rdm2_f_ovov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_ovov += einsum(x32, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x32, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(x31, (0, 1, 2, 3), x32, (1, 4, 2, 5), (0, 4, 3, 5))
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x34 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x34, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x34, (0, 1, 2, 3), (1, 0, 2, 3))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 1, 5), (5, 0, 4, 3))
    rdm2_f_ovvo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_ovvo += einsum(x35, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_voov += einsum(x35, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x36 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm2_f_ovvo += einsum(t2, (0, 1, 2, 3), x36, (1, 4, 5, 2), (0, 5, 3, 4)) * -1.0
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(x36, (0, 1, 2, 3), t2, (4, 1, 5, 2), (0, 4, 3, 5))
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3))
    x38 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x39 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(x38, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x39, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x39, (0, 1, 2, 3), (1, 0, 3, 2))
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(x27, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x41 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(t2, (0, 1, 2, 3), x25, (3, 4), (0, 1, 2, 4))
    rdm2_f_oovv += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x41, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x42 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x42 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x42 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x43 = np.zeros((nvir, nvir), dtype=np.float64)
    x43 += einsum(x42, (0, 1, 2, 3), l2, (2, 4, 1, 0), (3, 4))
    rdm2_f_oovv += einsum(x31, (0, 1, 2, 3), x43, (4, 2), (0, 1, 3, 4)) * 0.5
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x44 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x44 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_ovvo += einsum(l2, (0, 1, 2, 3), x44, (4, 3, 1, 5), (4, 0, 5, 2))
    x45 = np.zeros((nvir, nvir), dtype=np.float64)
    x45 += einsum(x44, (0, 1, 2, 3), l2, (4, 2, 1, 0), (4, 3))
    rdm2_f_oovv += einsum(x0, (0, 1, 2, 3), x45, (2, 4), (0, 1, 4, 3)) * 0.5
    x46 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x46 += einsum(t2, (0, 1, 2, 3), x6, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_oovv += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x46, (0, 1, 2, 3), (1, 0, 3, 2))
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 0, 5), (5, 1, 4, 2))
    rdm2_f_ovov += einsum(x47, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x47, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x48 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum(t2, (0, 1, 2, 3), x47, (1, 4, 2, 5), (0, 4, 5, 3))
    rdm2_f_oovv += einsum(x48, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x48, (0, 1, 2, 3), (1, 0, 3, 2))
    x49 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x49 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3))
    x49 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x50 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x50 += einsum(x49, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x50, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x50, (0, 1, 2, 3), (0, 1, 2, 3))
    x51 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x51 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 5, 1), (5, 0, 4, 3))
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 0, 5), (5, 1, 4, 3))
    rdm2_f_ovov += einsum(x52, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x52, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x52, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x52, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x53 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3))
    x53 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x53 += einsum(x44, (0, 1, 2, 3), l2, (2, 4, 5, 1), (5, 0, 4, 3))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x53, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x54 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3))
    x54 += einsum(x36, (0, 1, 2, 3), t2, (1, 4, 2, 5), (0, 4, 3, 5)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x54, (1, 4, 2, 5), (0, 4, 3, 5))
    x55 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x55 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333333
    x55 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x55 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333333
    x56 = np.zeros((nvir, nvir), dtype=np.float64)
    x56 += einsum(x55, (0, 1, 2, 3), l2, (2, 4, 1, 0), (4, 3)) * 3.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x56, (3, 4), (0, 1, 2, 4)) * -0.5
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x57 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x57 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x58 = np.zeros((nvir, nvir), dtype=np.float64)
    x58 += einsum(l2, (0, 1, 2, 3), x57, (3, 2, 1, 4), (4, 0)) * 3.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x58, (4, 2), (0, 1, 4, 3)) * -0.5
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x58, (2, 3), (1, 3, 0, 2)) * 0.5
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x58, (2, 3), (1, 3, 0, 2)) * 0.5
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x58, (2, 3), (1, 3, 2, 0)) * -0.5
    rdm2_f_voov += einsum(delta.oo, (0, 1), x58, (2, 3), (3, 1, 0, 2)) * -0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x58, (2, 3), (3, 1, 2, 0)) * 0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x58, (2, 3), (3, 1, 2, 0)) * 0.5
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(x16, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 0.5
    rdm2_f_oovv += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x59, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x60 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x60 += einsum(x23, (0, 1), t2, (0, 2, 3, 4), (1, 2, 3, 4)) * 0.5
    rdm2_f_oovv += einsum(x60, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x60, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x61 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x61 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x61 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * 2.0
    rdm2_f_ovvo += einsum(x61, (0, 1, 2, 3), t2, (4, 0, 5, 3), (4, 2, 5, 1))
    x62 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x62 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x62 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x62 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0))
    x63 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x63 += einsum(x31, (0, 1, 2, 3), x61, (1, 4, 5, 3), (4, 0, 5, 2)) * -1.0
    x63 += einsum(x62, (0, 1, 2, 3), t2, (0, 4, 2, 5), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x63, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x64 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x64 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 0, 5), (5, 1, 4, 3))
    rdm2_f_ovvo += einsum(x64, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x64, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x65 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x65 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x65 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x65 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x66 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x66 += einsum(l2, (0, 1, 2, 3), x65, (4, 3, 5, 1), (4, 2, 5, 0))
    rdm2_f_voov += einsum(x66, (0, 1, 2, 3), (3, 0, 1, 2))
    x67 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x67 += einsum(x64, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x67 += einsum(x66, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x67, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5)) * -1.0
    x68 = np.zeros((nvir, nvir), dtype=np.float64)
    x68 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 0, 1), (4, 3))
    x69 = np.zeros((nvir, nvir), dtype=np.float64)
    x69 += einsum(x42, (0, 1, 2, 3), l2, (4, 2, 1, 0), (3, 4))
    rdm2_f_oovv += einsum(x69, (0, 1), x0, (2, 3, 1, 4), (2, 3, 0, 4)) * -0.5
    x70 = np.zeros((nvir, nvir), dtype=np.float64)
    x70 += einsum(x68, (0, 1), (0, 1)) * 2.0
    x70 += einsum(x69, (0, 1), (1, 0))
    rdm2_f_oovv += einsum(x70, (0, 1), t2, (2, 3, 4, 0), (3, 2, 1, 4)) * -0.5
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x70, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x70, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x70, (2, 3), (1, 2, 3, 0)) * -0.5
    rdm2_f_voov += einsum(delta.oo, (0, 1), x70, (2, 3), (2, 1, 0, 3)) * -0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x70, (2, 3), (2, 1, 3, 0)) * 0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x70, (2, 3), (2, 1, 3, 0)) * 0.5
    x71 = np.zeros((nvir, nvir), dtype=np.float64)
    x71 += einsum(x25, (0, 1), (0, 1)) * 2.0
    x71 += einsum(x43, (0, 1), (1, 0)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x71, (2, 4), (1, 0, 3, 4)) * -0.5
    x72 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x72 += einsum(l2, (0, 1, 2, 3), x31, (4, 3, 5, 1), (4, 2, 5, 0))
    x73 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x73 += einsum(x72, (0, 1, 2, 3), t2, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x74 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x74 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x74 += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x74, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x74, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x74, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x75 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x75 += einsum(x68, (0, 1), x0, (2, 3, 0, 4), (2, 3, 1, 4)) * 1.5
    rdm2_f_oovv += einsum(x75, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x75, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x76 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x76 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 1, 5), (5, 0, 4, 3))
    x77 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x77 += einsum(x76, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5))
    x78 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(x64, (0, 1, 2, 3), t2, (0, 4, 2, 5), (1, 4, 3, 5))
    x79 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x79 += einsum(l2, (0, 1, 2, 3), x31, (4, 3, 5, 0), (4, 2, 5, 1))
    x80 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x80 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3))
    x80 += einsum(x79, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x81 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x81 += einsum(x80, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x82 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum(x77, (0, 1, 2, 3), (0, 1, 2, 3))
    x82 += einsum(x78, (0, 1, 2, 3), (0, 1, 2, 3))
    x82 += einsum(x81, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x82, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3))
    x83 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x83 += einsum(x51, (0, 1, 2, 3), t2, (4, 0, 2, 5), (4, 1, 5, 3))
    x84 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x84 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 5, 0), (5, 1, 4, 3))
    x85 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x85 += einsum(x84, (0, 1, 2, 3), t2, (0, 4, 2, 5), (4, 1, 5, 3))
    x86 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum(x76, (0, 1, 2, 3), (0, 1, 2, 3))
    x86 += einsum(x72, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x87 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x87 += einsum(x86, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x88 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x88 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    x88 += einsum(x85, (0, 1, 2, 3), (0, 1, 2, 3))
    x88 += einsum(x87, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x88, (0, 1, 2, 3), (1, 0, 3, 2))
    x89 = np.zeros((nvir, nvir), dtype=np.float64)
    x89 += einsum(x65, (0, 1, 2, 3), l2, (2, 4, 1, 0), (4, 3))
    rdm2_f_oovv += einsum(x31, (0, 1, 2, 3), x89, (2, 4), (0, 1, 3, 4)) * 0.5
    x90 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x90 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x90 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x91 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x91 += einsum(l2, (0, 1, 2, 3), x90, (4, 3, 1, 5), (4, 2, 5, 0))
    rdm2_f_ovov += einsum(x91, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_voov += einsum(x91, (0, 1, 2, 3), (3, 0, 1, 2))
    x92 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x92 += einsum(x31, (0, 1, 2, 3), l2, (4, 2, 1, 5), (0, 5, 3, 4))
    rdm2_f_ovov += einsum(x92, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_voov += einsum(x92, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x93 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x93 += einsum(x8, (0, 1, 2, 3), x31, (4, 0, 3, 5), (4, 1, 5, 2))
    rdm2_f_ovov += einsum(x93, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_vovo += einsum(x93, (0, 1, 2, 3), (3, 0, 2, 1))
    x94 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x94 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x94 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0))
    x94 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x95 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x95 += einsum(x94, (0, 1, 2, 3), t2, (4, 0, 5, 3), (1, 4, 2, 5))
    rdm2_f_ovvo += einsum(x95, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x95, (0, 1, 2, 3), (2, 1, 0, 3))
    x96 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x96 += einsum(x8, (0, 1, 2, 3), x31, (4, 0, 5, 3), (4, 1, 5, 2))
    rdm2_f_ovvo += einsum(x96, (0, 1, 2, 3), (0, 3, 2, 1))
    rdm2_f_voov += einsum(x96, (0, 1, 2, 3), (3, 0, 1, 2))
    x97 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.5
    x97 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm2_f_vovo += einsum(x97, (0, 1, 2, 3), t2, (4, 0, 5, 3), (2, 4, 5, 1)) * -2.0
    x98 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x98 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x98 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x99 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x99 += einsum(x98, (0, 1, 2, 3), l2, (4, 5, 1, 0), (2, 3, 4, 5)) * 0.5
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(x99, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vvvv += einsum(x99, (0, 1, 2, 3), (2, 3, 1, 0))
    rdm2_f_vvvv += einsum(x99, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vvvv += einsum(x99, (0, 1, 2, 3), (2, 3, 1, 0))
    x100 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x100 += einsum(t2, (0, 1, 2, 3), l2, (4, 5, 0, 1), (4, 5, 2, 3))
    rdm2_f_vvvv += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x100, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

