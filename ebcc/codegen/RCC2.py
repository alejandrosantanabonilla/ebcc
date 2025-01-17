# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    e_cc = 0
    e_cc += einsum(x0, (0, 1, 2, 3), t2, (0, 1, 2, 3), ()) * 2.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x1 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x2 = np.zeros((nocc, nvir), dtype=np.float64)
    x2 += einsum(f.ov, (0, 1), (0, 1))
    x2 += einsum(t1, (0, 1), x1, (0, 2, 3, 1), (2, 3))
    e_cc += einsum(x2, (0, 1), t1, (0, 1), ()) * 2.0

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t1new += einsum(t1, (0, 1), f.vv, (2, 1), (0, 2))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(f.vv, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    t2new += einsum(t2, (0, 1, 2, 3), f.vv, (4, 3), (0, 1, 2, 4))
    t2new += einsum(f.oo, (0, 1), t2, (1, 2, 3, 4), (0, 2, 3, 4)) * -1.0
    t2new += einsum(f.oo, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4)) * -1.0
    t2new += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 4), (3, 2, 4, 1)) * -1.0
    t2new += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x0 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    x1 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x1 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x1 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2))
    t1new += einsum(x0, (0, 1, 2, 3), x1, (1, 2, 3, 4), (0, 4)) * 2.0
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(t1, (0, 1), v.ovov, (2, 1, 3, 4), (0, 3, 2, 4))
    x3 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x3 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x3 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.3333333333333333
    x3 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x3 += einsum(x2, (0, 1, 2, 3), (0, 2, 1, 3))
    t1new += einsum(t2, (0, 1, 2, 3), x3, (4, 0, 1, 3), (4, 2)) * -1.5
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x4 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x4 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3))
    x4 += einsum(x2, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new += einsum(x4, (0, 1, 2, 3), t2, (1, 2, 3, 4), (0, 4)) * -0.5
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x6 = np.zeros((nocc, nvir), dtype=np.float64)
    x6 += einsum(f.ov, (0, 1), (0, 1)) * 0.5
    x6 += einsum(t1, (0, 1), x5, (0, 2, 3, 1), (2, 3))
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x7 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    t1new += einsum(x6, (0, 1), x7, (2, 0, 1, 3), (2, 3)) * 2.0
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x8 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    t1new += einsum(x8, (0, 1, 2, 3), t1, (0, 2), (1, 3)) * 2.0
    x9 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x9 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x9 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x10 = np.zeros((nocc, nocc), dtype=np.float64)
    x10 += einsum(f.oo, (0, 1), (1, 0))
    x10 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x10 += einsum(x5, (0, 1, 2, 3), x0, (4, 0, 2, 3), (1, 4)) * 2.0
    x10 += einsum(x9, (0, 1, 2, 3), t1, (0, 3), (2, 1)) * 2.0
    t1new += einsum(x10, (0, 1), t1, (0, 2), (1, 2)) * -1.0
    x11 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x11 += einsum(v.vvvv, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    t2new += einsum(x11, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x13 += einsum(x12, (0, 1, 2, 3), (1, 0, 2, 3))
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(t1, (0, 1), x13, (2, 3, 1, 4), (2, 3, 0, 4))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(t1, (0, 1), x14, (0, 2, 3, 4), (3, 2, 4, 1))
    t2new += einsum(x15, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x15, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x16 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(v.oovv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x17 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x17 += einsum(v.ooov, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x18 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x18 += einsum(x17, (0, 1, 2, 3), t1, (3, 4), (0, 2, 1, 4))
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(x16, (0, 1, 2, 3), (0, 2, 1, 3))
    x19 += einsum(x18, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(t1, (0, 1), x19, (2, 0, 3, 4), (2, 3, 4, 1))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x21 += einsum(x20, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x21, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x21, (0, 1, 2, 3), (1, 0, 2, 3))
    x22 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x22 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x22 += einsum(x2, (0, 1, 2, 3), t1, (4, 3), (1, 4, 0, 2))
    x23 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x23 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x23 += einsum(t1, (0, 1), x22, (0, 2, 3, 4), (3, 2, 4, 1))
    t2new += einsum(t1, (0, 1), x23, (2, 3, 0, 4), (2, 3, 1, 4))

    return {"t1new": t1new, "t2new": t2new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    # L amplitudes
    l1new = np.zeros((nvir, nocc), dtype=np.float64)
    l1new += einsum(f.ov, (0, 1), (1, 0))
    l1new += einsum(l1, (0, 1), v.oovv, (2, 1, 3, 0), (3, 2)) * -1.0
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(l2, (0, 1, 2, 3), v.ovov, (4, 5, 3, 1), (5, 0, 4, 2))
    l2new += einsum(v.ovov, (0, 1, 2, 3), (3, 1, 2, 0))
    l2new += einsum(l2, (0, 1, 2, 3), v.vvvv, (4, 1, 5, 0), (5, 4, 2, 3))
    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), f.ov, (4, 2), (4, 0, 1, 3))
    x1 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), f.ov, (4, 3), (4, 0, 1, 2))
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 2, 3, 5), (0, 1, 4, 5))
    x3 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x3 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 5, 3, 1), (4, 5, 2, 0))
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(x3, (0, 1, 2, 3), t1, (3, 4), (0, 1, 2, 4))
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x6 = np.zeros((nocc, nvir), dtype=np.float64)
    x6 += einsum(t1, (0, 1), x5, (0, 2, 3, 1), (2, 3))
    x7 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), x6, (4, 2), (0, 1, 4, 3)) * 1.5
    x8 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x8 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.75
    x8 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.75
    x8 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x9 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x9 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 3, 2, 5), (0, 1, 4, 5))
    x10 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x10 += einsum(t1, (0, 1), x3, (2, 3, 0, 4), (2, 3, 4, 1))
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(x6, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4)) * 0.5
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x12 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.25
    x12 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 1), (4, 0, 2, 3))
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), t1, (4, 3), (0, 4, 1, 2))
    x15 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(v.ovov, (0, 1, 2, 3), t1, (4, 3), (4, 0, 2, 1))
    x16 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x16 += einsum(x15, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x17 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x17 += einsum(x16, (0, 1, 2, 3), t1, (3, 4), (0, 1, 2, 4))
    x18 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x18 += einsum(x14, (0, 1, 2, 3), (0, 1, 2, 3))
    x18 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x19 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3))
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x20 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x20 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x21 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.6666666666666666
    x21 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.3333333333333333
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x22 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    x23 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x23 += einsum(v.ooov, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    l2new += einsum(l2, (0, 1, 2, 3), x23, (3, 4, 2, 5), (0, 1, 4, 5))
    x24 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x24 += einsum(v.oooo, (0, 1, 2, 3), (1, 3, 2, 0)) * 2.0
    x24 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x24 += einsum(x23, (0, 1, 2, 3), (2, 0, 3, 1)) * 2.0
    x24 += einsum(x23, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x25 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x25 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x25 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.5
    x25 += einsum(x0, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.75
    x25 += einsum(x0, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.25
    x25 += einsum(x1, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    x25 += einsum(x1, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.25
    x25 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(x8, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x25 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x25 += einsum(x12, (0, 1, 2, 3), (1, 0, 2, 3))
    x25 += einsum(x18, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(x18, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x25 += einsum(x20, (0, 1, 2, 3), x19, (4, 5, 1, 3), (4, 0, 5, 2)) * -0.5
    x25 += einsum(x21, (0, 1, 2, 3), x19, (4, 1, 5, 3), (4, 0, 5, 2)) * 1.5
    x25 += einsum(x22, (0, 1, 2, 3), t1, (4, 2), (4, 1, 0, 3))
    x25 += einsum(x24, (0, 1, 2, 3), t1, (0, 4), (1, 3, 2, 4)) * -0.5
    l1new += einsum(x25, (0, 1, 2, 3), l2, (4, 3, 0, 1), (4, 2)) * -2.0
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x26 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x27 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * 3.0
    x28 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x28 += einsum(x27, (0, 1, 2, 3), x26, (0, 4, 2, 5), (4, 1, 5, 3)) * 4.0
    x28 += einsum(l2, (0, 1, 2, 3), x20, (3, 4, 1, 5), (2, 4, 0, 5)) * 2.0
    l1new += einsum(x28, (0, 1, 2, 3), v.ovvv, (1, 3, 2, 4), (4, 0)) * 0.5
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x29 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x30 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x30 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    l2new += einsum(x30, (0, 1, 2, 3), v.ovvv, (2, 4, 5, 3), (4, 5, 0, 1)) * -1.0
    l2new += einsum(x15, (0, 1, 2, 3), x30, (4, 0, 1, 5), (3, 5, 4, 2))
    l2new += einsum(x30, (0, 1, 2, 3), v.ooov, (1, 4, 2, 5), (5, 3, 0, 4))
    x31 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x31 += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x31 += einsum(x30, (0, 1, 2, 3), (1, 0, 2, 3))
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    x32 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 5, 1), (5, 0, 4, 3))
    x32 += einsum(x26, (0, 1, 2, 3), x29, (1, 4, 2, 5), (0, 4, 3, 5)) * -1.0
    x32 += einsum(x31, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3)) * 2.0
    l1new += einsum(x32, (0, 1, 2, 3), v.ovvv, (1, 4, 3, 2), (4, 0)) * -1.0
    x33 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x33 += einsum(t1, (0, 1), x26, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    l1new += einsum(x33, (0, 1, 2, 3), v.vvvv, (2, 4, 1, 3), (4, 0)) * -0.5
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.3333333333333333
    x34 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x35 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x35 += einsum(x34, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4)) * 3.0
    l1new += einsum(x35, (0, 1, 2, 3), v.vvvv, (2, 3, 4, 1), (4, 0)) * 0.5
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new += einsum(x36, (0, 1, 2, 3), v.ovvv, (2, 4, 5, 3), (5, 4, 0, 1)) * -1.0
    l2new += einsum(x15, (0, 1, 2, 3), x36, (4, 0, 1, 5), (5, 3, 4, 2))
    l2new += einsum(x15, (0, 1, 2, 3), x36, (0, 4, 1, 5), (5, 3, 2, 4))
    l2new += einsum(x36, (0, 1, 2, 3), v.ooov, (1, 4, 2, 5), (3, 5, 0, 4))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x36, (0, 4, 2, 5), (5, 3, 1, 4))
    x37 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x37 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x37 += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x37 += einsum(x30, (0, 1, 2, 3), (1, 0, 2, 3))
    l1new += einsum(v.oovv, (0, 1, 2, 3), x37, (4, 0, 1, 2), (3, 4)) * -1.0
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0))
    x38 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x38 += einsum(t1, (0, 1), x37, (2, 0, 3, 4), (2, 3, 4, 1)) * 2.0
    l1new += einsum(x38, (0, 1, 2, 3), v.ovvv, (1, 3, 2, 4), (4, 0)) * -0.5
    x39 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x39 += einsum(x30, (0, 1, 2, 3), t1, (4, 3), (0, 1, 2, 4))
    l2new += einsum(x39, (0, 1, 2, 3), v.ovov, (2, 4, 3, 5), (4, 5, 0, 1))
    x40 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x40 += einsum(x39, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 += einsum(x39, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4))
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x42 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3))
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x43 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x44 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x44 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1))
    x45 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x45 += einsum(t2, (0, 1, 2, 3), l2, (3, 2, 4, 5), (4, 5, 0, 1))
    x46 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x46 += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.0
    x46 += einsum(x44, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x46 += einsum(x45, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x46 += einsum(x45, (0, 1, 2, 3), (1, 0, 2, 3))
    x47 = np.zeros((nocc, nocc), dtype=np.float64)
    x47 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    x48 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x48 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x49 = np.zeros((nocc, nocc), dtype=np.float64)
    x49 += einsum(x29, (0, 1, 2, 3), x48, (0, 4, 2, 3), (1, 4)) * 0.5
    x50 = np.zeros((nocc, nocc), dtype=np.float64)
    x50 += einsum(x47, (0, 1), (0, 1))
    x50 += einsum(x49, (0, 1), (1, 0)) * -1.0
    x51 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x51 += einsum(x30, (0, 1, 2, 3), (0, 2, 1, 3)) * 8.0
    x51 += einsum(x30, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    x51 += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x51 += einsum(x40, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x51 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x51 += einsum(x41, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.0
    x51 += einsum(x27, (0, 1, 2, 3), x42, (4, 0, 5, 2), (4, 5, 1, 3)) * 8.0
    x51 += einsum(x30, (0, 1, 2, 3), x20, (1, 4, 3, 5), (0, 2, 4, 5)) * 4.0
    x51 += einsum(x43, (0, 1, 2, 3), l1, (2, 4), (4, 0, 1, 3)) * 6.0
    x51 += einsum(t1, (0, 1), x46, (2, 0, 3, 4), (2, 3, 4, 1)) * -1.0
    x51 += einsum(x50, (0, 1), t1, (2, 3), (0, 1, 2, 3)) * 8.0
    l1new += einsum(x51, (0, 1, 2, 3), v.ovov, (2, 3, 1, 4), (4, 0)) * -0.25
    x52 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x52 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x52 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x53 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x53 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x54 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x54 += einsum(x53, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1))
    x55 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x55 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3))
    x55 += einsum(x54, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x56 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x56 += einsum(x30, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 2, 4, 5)) * 4.0
    x56 += einsum(t2, (0, 1, 2, 3), x36, (4, 1, 5, 2), (4, 5, 0, 3)) * 4.0
    x56 += einsum(x52, (0, 1, 2, 3), x29, (1, 4, 3, 5), (0, 2, 4, 5)) * -4.0
    x56 += einsum(x53, (0, 1, 2, 3), l1, (2, 4), (4, 0, 1, 3)) * -2.0
    x56 += einsum(x55, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    x56 += einsum(x50, (0, 1), t1, (2, 3), (0, 1, 2, 3)) * 4.0
    l1new += einsum(x56, (0, 1, 2, 3), v.ovov, (2, 4, 1, 3), (4, 0)) * 0.25
    x57 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x57 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x57 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    x57 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x57 += einsum(x15, (0, 1, 2, 3), (0, 2, 1, 3))
    x58 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x58 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x58 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    x58 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x58 += einsum(x15, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x59 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x60 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x60 += einsum(x23, (0, 1, 2, 3), (0, 2, 1, 3))
    x60 += einsum(x23, (0, 1, 2, 3), (0, 3, 2, 1)) * -0.5
    x61 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x61 += einsum(t2, (0, 1, 2, 3), x57, (4, 5, 1, 3), (4, 0, 5, 2)) * 2.0
    x61 += einsum(t2, (0, 1, 2, 3), x58, (4, 5, 1, 2), (4, 0, 5, 3))
    x61 += einsum(x59, (0, 1, 2, 3), t1, (4, 2), (4, 1, 0, 3)) * -1.0
    x61 += einsum(x60, (0, 1, 2, 3), t1, (3, 4), (0, 2, 1, 4)) * 2.0
    l1new += einsum(l2, (0, 1, 2, 3), x61, (3, 2, 4, 1), (0, 4))
    x62 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x62 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x62 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x62 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x63 = np.zeros((nvir, nvir), dtype=np.float64)
    x63 += einsum(t1, (0, 1), l1, (2, 0), (2, 1))
    x63 += einsum(x62, (0, 1, 2, 3), l2, (3, 4, 0, 1), (4, 2)) * -0.5
    x64 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x64 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2))
    x64 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2)) * -0.5
    l1new += einsum(x64, (0, 1, 2, 3), x63, (3, 2), (1, 0)) * 2.0
    x65 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x65 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x65 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x65 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x66 = np.zeros((nocc, nocc), dtype=np.float64)
    x66 += einsum(t1, (0, 1), l1, (1, 2), (2, 0))
    l1new += einsum(x6, (0, 1), x66, (2, 0), (1, 2)) * -2.0
    x67 = np.zeros((nocc, nocc), dtype=np.float64)
    x67 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 0), (4, 1))
    x68 = np.zeros((nocc, nocc), dtype=np.float64)
    x68 += einsum(x48, (0, 1, 2, 3), t2, (0, 4, 3, 2), (4, 1))
    x69 = np.zeros((nocc, nocc), dtype=np.float64)
    x69 += einsum(x66, (0, 1), (0, 1)) * 2.0
    x69 += einsum(x67, (0, 1), (0, 1)) * -1.0
    x69 += einsum(x68, (0, 1), (1, 0))
    x70 = np.zeros((nocc, nvir), dtype=np.float64)
    x70 += einsum(t1, (0, 1), (0, 1))
    x70 += einsum(l1, (0, 1), t2, (1, 2, 3, 0), (2, 3)) * -1.0
    x70 += einsum(x36, (0, 1, 2, 3), x65, (1, 0, 4, 3), (2, 4)) * 0.5
    x70 += einsum(x69, (0, 1), t1, (0, 2), (1, 2)) * -0.5
    x71 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x71 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * 2.0
    x71 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    l1new += einsum(x71, (0, 1, 2, 3), x70, (0, 3), (2, 1))
    x72 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x72 += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.0
    x72 += einsum(x44, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x72 += einsum(x45, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x72 += einsum(x45, (0, 1, 2, 3), (1, 0, 2, 3))
    x72 += einsum(x39, (0, 1, 2, 3), (0, 2, 3, 1)) * -2.0
    x72 += einsum(x39, (0, 1, 2, 3), (0, 3, 2, 1)) * 6.0
    x72 += einsum(x39, (0, 1, 2, 3), (1, 2, 3, 0)) * 2.0
    x72 += einsum(x39, (0, 1, 2, 3), (1, 3, 2, 0)) * -2.0
    l1new += einsum(x72, (0, 1, 2, 3), v.ooov, (3, 1, 2, 4), (4, 0)) * 0.25
    x73 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x73 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x73 += einsum(x54, (0, 1, 2, 3), (1, 0, 2, 3))
    l1new += einsum(v.ooov, (0, 1, 2, 3), x73, (4, 1, 0, 2), (3, 4)) * -0.25
    x74 = np.zeros((nocc, nvir), dtype=np.float64)
    x74 += einsum(t2, (0, 1, 2, 3), x30, (0, 1, 4, 3), (4, 2))
    x75 = np.zeros((nocc, nvir), dtype=np.float64)
    x75 += einsum(x36, (0, 1, 2, 3), t2, (0, 1, 3, 4), (2, 4))
    x76 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x76 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x76 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x77 = np.zeros((nocc, nocc), dtype=np.float64)
    x77 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 0, 4), (4, 1))
    x78 = np.zeros((nocc, nocc), dtype=np.float64)
    x78 += einsum(x47, (0, 1), (0, 1))
    x78 += einsum(x77, (0, 1), (0, 1)) * 0.5
    l1new += einsum(v.ooov, (0, 1, 2, 3), x78, (0, 2), (3, 1))
    x79 = np.zeros((nocc, nvir), dtype=np.float64)
    x79 += einsum(x74, (0, 1), (0, 1)) * 2.0
    x79 += einsum(x75, (0, 1), (0, 1))
    x79 += einsum(l1, (0, 1), x76, (2, 1, 3, 0), (2, 3)) * -2.0
    x79 += einsum(x78, (0, 1), t1, (0, 2), (1, 2)) * 2.0
    l1new += einsum(x79, (0, 1), v.ovov, (0, 2, 3, 1), (2, 3)) * 0.5
    x80 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x80 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x80 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x81 = np.zeros((nocc, nocc), dtype=np.float64)
    x81 += einsum(x47, (0, 1), (0, 1))
    x81 += einsum(x77, (0, 1), (0, 1)) * 2.0
    l1new += einsum(x81, (0, 1), v.ooov, (1, 0, 2, 3), (3, 2)) * -1.0
    x82 = np.zeros((nocc, nvir), dtype=np.float64)
    x82 += einsum(l1, (0, 1), (1, 0)) * -1.0
    x82 += einsum(x74, (0, 1), (0, 1)) * 0.5
    x82 += einsum(x75, (0, 1), (0, 1))
    x82 += einsum(x80, (0, 1, 2, 3), l1, (3, 1), (0, 2)) * -0.5
    x82 += einsum(x81, (0, 1), t1, (0, 2), (1, 2)) * 0.5
    l1new += einsum(v.ovov, (0, 1, 2, 3), x82, (0, 1), (3, 2)) * -2.0
    x83 = np.zeros((nvir, nvir), dtype=np.float64)
    x83 += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 0, 1), (4, 2))
    x84 = np.zeros((nvir, nvir), dtype=np.float64)
    x84 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 0, 1), (4, 3))
    x85 = np.zeros((nvir, nvir), dtype=np.float64)
    x85 += einsum(x83, (0, 1), (0, 1))
    x85 += einsum(x84, (0, 1), (0, 1)) * 2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x85, (3, 2), (1, 0))
    x86 = np.zeros((nvir, nvir), dtype=np.float64)
    x86 += einsum(x83, (0, 1), (0, 1))
    x86 += einsum(x84, (0, 1), (0, 1)) * 0.5
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x86, (2, 1), (3, 0)) * -1.0
    x87 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x87 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x87 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    l1new += einsum(x69, (0, 1), x87, (1, 0, 2, 3), (3, 2)) * -0.5
    x88 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x88 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x88 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2))
    x89 = np.zeros((nvir, nvir), dtype=np.float64)
    x89 += einsum(f.vv, (0, 1), (1, 0)) * 0.5
    x89 += einsum(x88, (0, 1, 2, 3), t1, (0, 2), (3, 1))
    l1new += einsum(x89, (0, 1), l1, (0, 2), (1, 2)) * 2.0
    x90 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x90 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x90 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x91 = np.zeros((nocc, nocc), dtype=np.float64)
    x91 += einsum(x90, (0, 1, 2, 3), t1, (0, 3), (1, 2)) * 2.0
    x92 = np.zeros((nocc, nvir), dtype=np.float64)
    x92 += einsum(t1, (0, 1), x5, (0, 2, 3, 1), (2, 3)) * 2.0
    l2new += einsum(x92, (0, 1), x30, (2, 3, 0, 4), (1, 4, 2, 3)) * -1.0
    l2new += einsum(x36, (0, 1, 2, 3), x92, (2, 4), (3, 4, 0, 1)) * -1.0
    x93 = np.zeros((nocc, nvir), dtype=np.float64)
    x93 += einsum(f.ov, (0, 1), (0, 1))
    x93 += einsum(x92, (0, 1), (0, 1))
    x94 = np.zeros((nocc, nocc), dtype=np.float64)
    x94 += einsum(f.oo, (0, 1), (1, 0))
    x94 += einsum(x5, (0, 1, 2, 3), t2, (4, 0, 2, 3), (4, 1)) * 2.0
    x94 += einsum(x91, (0, 1), (0, 1))
    x94 += einsum(x93, (0, 1), t1, (2, 1), (2, 0))
    l1new += einsum(x94, (0, 1), l1, (2, 0), (2, 1)) * -1.0
    x95 = np.zeros((nocc, nocc), dtype=np.float64)
    x95 += einsum(x66, (0, 1), (0, 1)) * 2.0
    x95 += einsum(x47, (0, 1), (0, 1)) * 2.0
    x95 += einsum(x48, (0, 1, 2, 3), x29, (0, 4, 2, 3), (1, 4)) * -1.0
    l1new += einsum(f.ov, (0, 1), x95, (2, 0), (1, 2)) * -0.5
    x96 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x96 += einsum(x36, (0, 1, 2, 3), v.ooov, (1, 2, 4, 5), (0, 4, 3, 5))
    x97 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x98 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x98 += einsum(l2, (0, 1, 2, 3), x97, (3, 4, 5, 1), (2, 4, 0, 5))
    x99 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 += einsum(x15, (0, 1, 2, 3), x36, (4, 0, 2, 5), (4, 1, 5, 3))
    x100 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x100 += einsum(x96, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x100 += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x100 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    l2new += einsum(x100, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x100, (0, 1, 2, 3), (3, 2, 1, 0)) * -0.5
    x101 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x101 += einsum(v.ooov, (0, 1, 2, 3), l1, (4, 1), (0, 2, 4, 3))
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(x36, (0, 1, 2, 3), v.ooov, (0, 2, 4, 5), (1, 4, 3, 5))
    x103 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x103 += einsum(x15, (0, 1, 2, 3), x36, (0, 4, 2, 5), (4, 1, 5, 3))
    x104 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x104 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x104 += einsum(x97, (0, 1, 2, 3), (0, 1, 2, 3))
    x105 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x105 += einsum(x104, (0, 1, 2, 3), l2, (4, 3, 0, 5), (5, 1, 4, 2))
    x106 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x106 += einsum(l1, (0, 1), f.ov, (2, 3), (2, 1, 3, 0))
    x106 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x106 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3))
    x106 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3))
    x106 += einsum(x105, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x106 += einsum(x6, (0, 1), l1, (2, 3), (3, 0, 2, 1)) * 2.0
    l2new += einsum(x106, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x106, (0, 1, 2, 3), (3, 2, 1, 0))
    x107 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum(v.ovvv, (0, 1, 2, 3), l1, (3, 4), (4, 0, 1, 2))
    x108 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x108 += einsum(x15, (0, 1, 2, 3), l1, (4, 0), (1, 2, 4, 3))
    x109 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x109 += einsum(x66, (0, 1), v.ovov, (2, 3, 1, 4), (0, 2, 3, 4))
    x110 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum(x107, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x110 += einsum(x108, (0, 1, 2, 3), (0, 1, 2, 3))
    x110 += einsum(x109, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new += einsum(x110, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x110, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x111 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x111 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2))
    x111 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x112 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x112 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x112 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x112 += einsum(x111, (0, 1, 2, 3), t1, (4, 1), (4, 0, 3, 2)) * -1.0
    l2new += einsum(x112, (0, 1, 2, 3), l2, (3, 4, 0, 5), (2, 4, 1, 5))
    x113 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x113 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x113 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -2.0
    x113 += einsum(x13, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(x113, (0, 1, 2, 3), l2, (4, 2, 5, 0), (4, 3, 5, 1)) * -1.0
    x114 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x114 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x114 += einsum(x13, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(l2, (0, 1, 2, 3), x114, (2, 4, 1, 5), (0, 5, 4, 3)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x114, (3, 4, 0, 5), (5, 1, 2, 4)) * -1.0
    x115 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x115 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x115 += einsum(x15, (0, 1, 2, 3), (2, 0, 1, 3))
    x116 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x116 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x116 += einsum(x115, (0, 1, 2, 3), t1, (4, 3), (1, 0, 2, 4))
    l2new += einsum(l2, (0, 1, 2, 3), x116, (3, 4, 5, 2), (0, 1, 5, 4))
    x117 = np.zeros((nvir, nvir), dtype=np.float64)
    x117 += einsum(x88, (0, 1, 2, 3), t1, (0, 2), (1, 3)) * 2.0
    x118 = np.zeros((nvir, nvir), dtype=np.float64)
    x118 += einsum(f.vv, (0, 1), (1, 0))
    x118 += einsum(x117, (0, 1), (0, 1))
    l2new += einsum(x118, (0, 1), l2, (2, 1, 3, 4), (2, 0, 3, 4))
    l2new += einsum(x118, (0, 1), l2, (1, 2, 3, 4), (0, 2, 3, 4))
    x119 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x119 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x119 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    l2new += einsum(x30, (0, 1, 2, 3), x119, (0, 2, 4, 5), (5, 3, 4, 1)) * -1.0
    x120 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x120 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x120 += einsum(x15, (0, 1, 2, 3), (0, 2, 1, 3))
    l2new += einsum(x120, (0, 1, 2, 3), x30, (0, 4, 1, 5), (3, 5, 2, 4)) * -1.0
    x121 = np.zeros((nocc, nocc), dtype=np.float64)
    x121 += einsum(f.oo, (0, 1), (1, 0)) * 0.5
    x121 += einsum(x90, (0, 1, 2, 3), t1, (0, 3), (1, 2))
    x121 += einsum(x6, (0, 1), t1, (2, 1), (2, 0))
    l2new += einsum(l2, (0, 1, 2, 3), x121, (2, 4), (0, 1, 4, 3)) * -2.0
    x122 = np.zeros((nocc, nocc), dtype=np.float64)
    x122 += einsum(f.oo, (0, 1), (1, 0))
    x122 += einsum(x91, (0, 1), (0, 1))
    x122 += einsum(x6, (0, 1), t1, (2, 1), (2, 0)) * 2.0
    l2new += einsum(l2, (0, 1, 2, 3), x122, (3, 4), (0, 1, 2, 4)) * -1.0

    return {"l1new": l1new, "l2new": l2new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM1
    rdm1_f_oo = np.zeros((nocc, nocc), dtype=np.float64)
    rdm1_f_oo += einsum(delta.oo, (0, 1), (1, 0)) * 2.0
    rdm1_f_ov = np.zeros((nocc, nvir), dtype=np.float64)
    rdm1_f_ov += einsum(t1, (0, 1), (0, 1)) * 2.0
    rdm1_f_vo = np.zeros((nvir, nocc), dtype=np.float64)
    rdm1_f_vo += einsum(l1, (0, 1), (0, 1)) * 2.0
    rdm1_f_vv = np.zeros((nvir, nvir), dtype=np.float64)
    rdm1_f_vv += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 0, 1), (4, 2)) * 3.0
    rdm1_f_vv += einsum(t1, (0, 1), l1, (2, 0), (2, 1)) * 2.0
    x0 = np.zeros((nocc, nocc), dtype=np.float64)
    x0 += einsum(t1, (0, 1), l1, (1, 2), (2, 0))
    rdm1_f_oo += einsum(x0, (0, 1), (1, 0)) * -2.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x1 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm1_f_oo += einsum(x1, (0, 1, 2, 3), t2, (4, 0, 3, 2), (4, 1)) * -1.0
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.3333333333333333
    x2 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm1_f_oo += einsum(x2, (0, 1, 2, 3), t2, (4, 0, 2, 3), (4, 1)) * -3.0
    x3 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x3 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    rdm1_f_ov += einsum(t2, (0, 1, 2, 3), x3, (0, 1, 4, 3), (4, 2)) * -2.0
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x5 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x5 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x5 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm1_f_ov += einsum(x5, (0, 1, 2, 3), x4, (1, 0, 4, 3), (4, 2))
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x6 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm1_f_ov += einsum(l1, (0, 1), x6, (2, 1, 0, 3), (2, 3)) * 4.0
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x7 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x8 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x9 = np.zeros((nocc, nocc), dtype=np.float64)
    x9 += einsum(x0, (0, 1), (0, 1))
    x9 += einsum(l2, (0, 1, 2, 3), x7, (4, 3, 1, 0), (2, 4)) * 1.5
    x9 += einsum(l2, (0, 1, 2, 3), x8, (4, 2, 1, 0), (3, 4)) * 0.5
    rdm1_f_ov += einsum(x9, (0, 1), t1, (0, 2), (1, 2)) * -2.0
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x10 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x10 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm1_f_vv += einsum(x10, (0, 1, 2, 3), l2, (4, 3, 1, 0), (4, 2)) * -1.0

    rdm1_f = np.block([[rdm1_f_oo, rdm1_f_ov], [rdm1_f_vo, rdm1_f_vv]])

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM2
    rdm2_f_oooo = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(l1, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(l1, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vooo += einsum(l1, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    rdm2_f_vooo += einsum(l1, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    rdm2_f_vooo += einsum(l1, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vooo += einsum(l1, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    rdm2_f_oovv = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_ovov += einsum(t1, (0, 1), l1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_ovov += einsum(t1, (0, 1), l1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_ovvo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_ovvo += einsum(t1, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvo += einsum(t1, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvo += einsum(t1, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvo += einsum(t1, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_voov = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_voov += einsum(t1, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_voov += einsum(t1, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_voov += einsum(t1, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_voov += einsum(t1, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_vovo = np.zeros((nvir, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_vovo += einsum(t1, (0, 1), l1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vovo += einsum(t1, (0, 1), l1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vvoo = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 4, 1), (4, 0))
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(l2, (0, 1, 2, 3), x2, (4, 2, 1, 0), (3, 4)) * 0.3333333333333333
    x4 = np.zeros((nocc, nocc), dtype=np.float64)
    x4 += einsum(x1, (0, 1), (0, 1))
    x4 += einsum(x3, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(x4, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x4, (2, 3), (1, 3, 2, 0)) * 1.5
    rdm2_f_oooo += einsum(x4, (0, 1), delta.oo, (2, 3), (1, 2, 3, 0)) * 1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x4, (2, 3), (3, 0, 2, 1)) * -1.5
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(t1, (0, 1), l1, (1, 2), (2, 0))
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 3, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 3, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 1, 2, 0)) * -1.0
    x6 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x6 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_ovoo += einsum(x6, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_ovoo += einsum(x6, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_ovoo += einsum(x6, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_ovoo += einsum(x6, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_ovoo += einsum(x6, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x6, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x6, (0, 1, 2, 3), (3, 2, 1, 0))
    rdm2_f_vooo += einsum(x6, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x6, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x6, (0, 1, 2, 3), (3, 2, 1, 0))
    x7 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x7 += einsum(t1, (0, 1), x6, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_oooo += einsum(x7, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x7, (0, 1, 2, 3), (3, 2, 1, 0))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x8 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x9 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x9 += einsum(x8, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1)) * 0.5
    x10 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x10 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x10 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oooo += einsum(x10, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x10, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_oooo += einsum(x10, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x10, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x11 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x11 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1))
    rdm2_f_oooo += einsum(x11, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x11, (0, 1, 2, 3), (3, 2, 1, 0))
    x12 = np.zeros((nocc, nocc), dtype=np.float64)
    x12 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 0, 1), (3, 4))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x13 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm2_f_vovo += einsum(x13, (0, 1, 2, 3), t2, (4, 1, 3, 5), (2, 4, 5, 0)) * -1.0
    x14 = np.zeros((nocc, nocc), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), t2, (4, 1, 3, 2), (0, 4))
    x15 = np.zeros((nocc, nocc), dtype=np.float64)
    x15 += einsum(x12, (0, 1), (0, 1))
    x15 += einsum(x14, (0, 1), (0, 1)) * -1.0
    rdm2_f_oooo += einsum(x15, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x15, (2, 3), (3, 0, 2, 1)) * 0.5
    rdm2_f_oooo += einsum(x15, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x15, (2, 3), (3, 0, 2, 1)) * 0.5
    x16 = np.zeros((nocc, nocc), dtype=np.float64)
    x16 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    rdm2_f_oooo += einsum(x16, (0, 1), delta.oo, (2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x16, (2, 3), (3, 1, 2, 0)) * -1.5
    rdm2_f_oooo += einsum(x16, (0, 1), delta.oo, (2, 3), (2, 1, 3, 0)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x16, (2, 3), (3, 1, 2, 0)) * -0.5
    x17 = np.zeros((nocc, nocc), dtype=np.float64)
    x17 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 0, 4), (4, 1))
    x18 = np.zeros((nocc, nocc), dtype=np.float64)
    x18 += einsum(delta.oo, (0, 1), (1, 0))
    x18 += einsum(x17, (0, 1), (0, 1)) * -1.0
    rdm2_f_oooo += einsum(x18, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    x19 = np.zeros((nocc, nocc), dtype=np.float64)
    x19 += einsum(delta.oo, (0, 1), (1, 0)) * -1.0
    x19 += einsum(x17, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x19, (2, 3), (3, 1, 2, 0)) * -1.0
    x20 = np.zeros((nocc, nocc), dtype=np.float64)
    x20 += einsum(x13, (0, 1, 2, 3), x2, (4, 1, 3, 2), (4, 0))
    x21 = np.zeros((nocc, nocc), dtype=np.float64)
    x21 += einsum(x17, (0, 1), (0, 1)) * 2.0
    x21 += einsum(x20, (0, 1), (1, 0))
    rdm2_f_oooo += einsum(x21, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (1, 3, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(x21, (0, 1), delta.oo, (2, 3), (1, 2, 3, 0)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 2, 1)) * -0.5
    x22 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x22 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo += einsum(x8, (0, 1, 2, 3), x22, (4, 1, 5, 2), (0, 5, 3, 4)) * -1.0
    rdm2_f_ovoo += einsum(x22, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x22, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x23 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x23 += einsum(x22, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 2, 4, 5))
    x24 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x24 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x24 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov += einsum(x24, (0, 1, 2, 3), t2, (0, 4, 3, 5), (2, 4, 1, 5))
    x25 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x25 += einsum(x8, (0, 1, 2, 3), x24, (4, 1, 5, 3), (0, 4, 5, 2))
    x26 = np.zeros((nocc, nocc), dtype=np.float64)
    x26 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 4, 1), (4, 0)) * 1.5
    x27 = np.zeros((nocc, nocc), dtype=np.float64)
    x27 += einsum(l2, (0, 1, 2, 3), x2, (4, 2, 1, 0), (3, 4)) * 0.5
    x28 = np.zeros((nocc, nocc), dtype=np.float64)
    x28 += einsum(x5, (0, 1), (0, 1))
    x28 += einsum(x26, (0, 1), (0, 1))
    x28 += einsum(x27, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(x28, (0, 1), t1, (2, 3), (1, 2, 0, 3)) * -1.0
    x29 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x29 += einsum(delta.oo, (0, 1), t1, (2, 3), (1, 0, 2, 3))
    x29 += einsum(x23, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x29 += einsum(x25, (0, 1, 2, 3), (2, 1, 0, 3))
    x29 += einsum(x28, (0, 1), t1, (2, 3), (2, 0, 1, 3))
    rdm2_f_ooov += einsum(x29, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x29, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x29, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x29, (0, 1, 2, 3), (2, 0, 3, 1))
    x30 = np.zeros((nocc, nvir), dtype=np.float64)
    x30 += einsum(t2, (0, 1, 2, 3), x22, (0, 1, 4, 3), (4, 2))
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x31 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x31 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x31 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x32 = np.zeros((nocc, nvir), dtype=np.float64)
    x32 += einsum(x31, (0, 1, 2, 3), x6, (0, 1, 4, 3), (4, 2)) * 0.5
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x33 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x34 = np.zeros((nocc, nvir), dtype=np.float64)
    x34 += einsum(x33, (0, 1, 2, 3), l1, (2, 1), (0, 3))
    x35 = np.zeros((nocc, nvir), dtype=np.float64)
    x35 += einsum(x28, (0, 1), t1, (0, 2), (1, 2))
    x36 = np.zeros((nocc, nvir), dtype=np.float64)
    x36 += einsum(x30, (0, 1), (0, 1))
    x36 += einsum(x32, (0, 1), (0, 1)) * -1.0
    x36 += einsum(x34, (0, 1), (0, 1)) * -1.0
    x36 += einsum(x35, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(x36, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_ooov += einsum(x36, (0, 1), delta.oo, (2, 3), (0, 2, 3, 1))
    rdm2_f_oovo += einsum(x36, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2))
    rdm2_f_oovo += einsum(x36, (0, 1), delta.oo, (2, 3), (0, 2, 1, 3)) * -1.0
    x37 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x37 += einsum(x8, (0, 1, 2, 3), l2, (2, 3, 4, 5), (4, 5, 0, 1))
    x38 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x38 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x38 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x39 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x39 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x39 += einsum(x38, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x40 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x40 += einsum(x39, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4)) * 0.5
    rdm2_f_ooov += einsum(x40, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x40, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 += einsum(x2, (0, 1, 2, 3), l1, (2, 4), (4, 0, 1, 3))
    rdm2_f_ooov += einsum(x41, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x41, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(t2, (0, 1, 2, 3), x6, (4, 1, 5, 2), (4, 5, 0, 3))
    rdm2_f_ooov += einsum(x42, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x42, (0, 1, 2, 3), (1, 2, 3, 0))
    x43 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x43 += einsum(l1, (0, 1), t2, (2, 3, 0, 4), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x43, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x43, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x44 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x44 += einsum(x2, (0, 1, 2, 3), x22, (4, 1, 5, 3), (0, 4, 5, 2))
    rdm2_f_ooov += einsum(x44, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x45 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x45 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x45 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x45 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.3333333333333333
    x45 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333333
    x46 = np.zeros((nocc, nvir), dtype=np.float64)
    x46 += einsum(x45, (0, 1, 2, 3), x6, (0, 1, 4, 3), (4, 2)) * 1.5
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x47 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x47 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_ovvo += einsum(x47, (0, 1, 2, 3), l2, (4, 2, 5, 1), (0, 4, 3, 5))
    x48 = np.zeros((nocc, nvir), dtype=np.float64)
    x48 += einsum(x47, (0, 1, 2, 3), l1, (2, 1), (0, 3))
    x49 = np.zeros((nocc, nocc), dtype=np.float64)
    x49 += einsum(x13, (0, 1, 2, 3), x2, (4, 1, 3, 2), (4, 0)) * 0.5
    x50 = np.zeros((nocc, nocc), dtype=np.float64)
    x50 += einsum(x5, (0, 1), (0, 1))
    x50 += einsum(x17, (0, 1), (0, 1))
    x50 += einsum(x49, (0, 1), (1, 0))
    rdm2_f_ooov += einsum(x50, (0, 1), t1, (2, 3), (1, 2, 0, 3)) * -1.0
    x51 = np.zeros((nocc, nvir), dtype=np.float64)
    x51 += einsum(x50, (0, 1), t1, (0, 2), (1, 2))
    x52 = np.zeros((nocc, nvir), dtype=np.float64)
    x52 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x52 += einsum(x46, (0, 1), (0, 1))
    x52 += einsum(x48, (0, 1), (0, 1)) * -1.0
    x52 += einsum(x51, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(x52, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_oovo += einsum(x52, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2)) * -1.0
    x53 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x53 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x53 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x54 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x54 += einsum(x53, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    rdm2_f_ooov += einsum(x54, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x54, (0, 1, 2, 3), (2, 1, 3, 0))
    x55 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x55 += einsum(t2, (0, 1, 2, 3), x6, (1, 4, 5, 2), (4, 5, 0, 3))
    rdm2_f_ooov += einsum(x55, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x55, (0, 1, 2, 3), (2, 1, 3, 0))
    x56 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x56 += einsum(x22, (0, 1, 2, 3), t2, (0, 4, 5, 3), (1, 2, 4, 5))
    rdm2_f_ooov += einsum(x56, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x56, (0, 1, 2, 3), (1, 2, 3, 0))
    x57 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x57 += einsum(t2, (0, 1, 2, 3), l1, (3, 4), (4, 0, 1, 2))
    rdm2_f_ooov += einsum(x57, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x57, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x58 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x58 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x58 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x59 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x59 += einsum(x58, (0, 1, 2, 3), t2, (4, 0, 5, 3), (1, 2, 4, 5))
    rdm2_f_ooov += einsum(x59, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x59, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x60 = np.zeros((nocc, nvir), dtype=np.float64)
    x60 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x60 += einsum(x30, (0, 1), (0, 1))
    x60 += einsum(x32, (0, 1), (0, 1)) * -1.0
    x60 += einsum(x34, (0, 1), (0, 1)) * -1.0
    x60 += einsum(x35, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(x60, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_oovo += einsum(x60, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2)) * -1.0
    x61 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x61 += einsum(x53, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x61, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x61, (0, 1, 2, 3), (1, 2, 3, 0))
    x62 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x62 += einsum(t2, (0, 1, 2, 3), x6, (0, 4, 5, 2), (4, 5, 1, 3))
    x63 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x63 += einsum(delta.oo, (0, 1), t1, (2, 3), (1, 0, 2, 3))
    x63 += einsum(x62, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x63 += einsum(x25, (0, 1, 2, 3), (2, 1, 0, 3))
    x63 += einsum(x50, (0, 1), t1, (2, 3), (2, 0, 1, 3))
    rdm2_f_ooov += einsum(x63, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x63, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x63, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x63, (0, 1, 2, 3), (2, 0, 3, 1))
    x64 = np.zeros((nocc, nvir), dtype=np.float64)
    x64 += einsum(x46, (0, 1), (0, 1))
    x64 += einsum(x48, (0, 1), (0, 1)) * -1.0
    x64 += einsum(x51, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(x64, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_ooov += einsum(x64, (0, 1), delta.oo, (2, 3), (0, 2, 3, 1))
    rdm2_f_oovo += einsum(x64, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2))
    rdm2_f_oovo += einsum(x64, (0, 1), delta.oo, (2, 3), (0, 2, 1, 3)) * -1.0
    x65 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x65 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x65 += einsum(x38, (0, 1, 2, 3), (1, 0, 2, 3))
    x66 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x66 += einsum(x65, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4)) * 0.5
    rdm2_f_oovo += einsum(x66, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x66, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x67 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x67 += einsum(l1, (0, 1), x8, (2, 3, 0, 4), (1, 2, 3, 4))
    rdm2_f_oovo += einsum(x67, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x67, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x68 = np.zeros((nocc, nocc), dtype=np.float64)
    x68 += einsum(x5, (0, 1), (0, 1)) * 2.0
    x68 += einsum(x17, (0, 1), (0, 1)) * 2.0
    x68 += einsum(x20, (0, 1), (1, 0))
    rdm2_f_oovo += einsum(x68, (0, 1), t1, (2, 3), (2, 1, 3, 0)) * -0.5
    x69 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x69 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    x69 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovo += einsum(t2, (0, 1, 2, 3), x69, (0, 4, 5, 2), (1, 5, 3, 4)) * -1.0
    x70 = np.zeros((nocc, nocc), dtype=np.float64)
    x70 += einsum(x0, (0, 1, 2, 3), l2, (3, 2, 4, 1), (4, 0)) * 3.0
    x71 = np.zeros((nocc, nocc), dtype=np.float64)
    x71 += einsum(l2, (0, 1, 2, 3), x2, (4, 2, 1, 0), (3, 4))
    x72 = np.zeros((nocc, nocc), dtype=np.float64)
    x72 += einsum(x5, (0, 1), (0, 1)) * 2.0
    x72 += einsum(x70, (0, 1), (0, 1))
    x72 += einsum(x71, (0, 1), (0, 1))
    rdm2_f_oovo += einsum(x72, (0, 1), t1, (2, 3), (2, 1, 3, 0)) * -0.5
    x73 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x73 += einsum(t2, (0, 1, 2, 3), x5, (1, 4), (4, 0, 2, 3))
    x74 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x74 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x74 += einsum(x25, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x75 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x75 += einsum(t1, (0, 1), x74, (0, 2, 3, 4), (2, 3, 1, 4))
    x76 = np.zeros((nocc, nocc), dtype=np.float64)
    x76 += einsum(x70, (0, 1), (0, 1))
    x76 += einsum(x71, (0, 1), (0, 1))
    x77 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x77 += einsum(x76, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 0.5
    x78 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x78 += einsum(x75, (0, 1, 2, 3), (0, 1, 2, 3))
    x78 += einsum(x77, (0, 1, 2, 3), (1, 0, 2, 3))
    x78 += einsum(x36, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x78, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x78, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x78, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x78, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x79 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x79 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x79 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x80 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x80 += einsum(x38, (0, 1, 2, 3), x79, (0, 1, 4, 5), (2, 3, 4, 5)) * 0.25
    x81 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x81 += einsum(x10, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    x82 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x82 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x82 += einsum(x81, (0, 1, 2, 3), (0, 1, 2, 3))
    x83 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x83 += einsum(x82, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    x84 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x84 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x84 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x84 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x84, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x84, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x85 = np.zeros((nvir, nvir), dtype=np.float64)
    x85 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x86 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum(x85, (0, 1), t2, (2, 3, 0, 4), (2, 3, 1, 4))
    rdm2_f_oovv += einsum(x86, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    rdm2_f_oovv += einsum(x86, (0, 1, 2, 3), (0, 1, 3, 2))
    x87 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x87 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    x88 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x88 += einsum(t2, (0, 1, 2, 3), x87, (1, 4, 3, 5), (0, 4, 2, 5))
    rdm2_f_oovv += einsum(x88, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -3.0
    rdm2_f_oovv += einsum(x88, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x88, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x89 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x89 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 5, 1), (3, 4, 0, 5))
    x90 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x90 += einsum(t2, (0, 1, 2, 3), x89, (1, 4, 3, 5), (4, 0, 5, 2))
    x91 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x91 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 5, 1), (5, 0, 4, 3))
    rdm2_f_ovov += einsum(x91, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x91, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x92 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x92 += einsum(x2, (0, 1, 2, 3), x91, (1, 4, 3, 5), (4, 0, 5, 2))
    x93 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x93 += einsum(x90, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x93 += einsum(x92, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x93, (0, 1, 2, 3), (1, 0, 2, 3))
    x94 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x94 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 1, 5), (5, 0, 4, 3))
    rdm2_f_ovvo += einsum(x94, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x94, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x95 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x95 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x95 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_ovvo += einsum(x95, (0, 1, 2, 3), t2, (4, 1, 3, 5), (4, 2, 5, 0)) * -1.0
    x96 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x96 += einsum(x95, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x97 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x97 += einsum(x96, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x98 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x98 += einsum(x97, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x98, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x98, (0, 1, 2, 3), (1, 0, 3, 2))
    x99 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 += einsum(t2, (0, 1, 2, 3), x87, (1, 4, 2, 5), (4, 0, 5, 3))
    rdm2_f_oovv += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    rdm2_f_oovv += einsum(x99, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x99, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    rdm2_f_oovv += einsum(x99, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x100 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x100 += einsum(x85, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1))
    rdm2_f_oovv += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x100, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    x101 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x101 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x101 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x101 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x101 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x102 = np.zeros((nvir, nvir), dtype=np.float64)
    x102 += einsum(x101, (0, 1, 2, 3), l2, (3, 4, 1, 0), (4, 2))
    rdm2_f_oovv += einsum(x2, (0, 1, 2, 3), x102, (3, 4), (0, 1, 2, 4)) * 0.5
    x103 = np.zeros((nvir, nvir), dtype=np.float64)
    x103 += einsum(x47, (0, 1, 2, 3), l2, (4, 2, 1, 0), (4, 3))
    rdm2_f_oovv += einsum(x8, (0, 1, 2, 3), x103, (3, 4), (0, 1, 4, 2)) * 0.5
    x104 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x104 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 5, 1), (3, 4, 0, 5))
    rdm2_f_ovov += einsum(x104, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x104, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x105 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x105 += einsum(x104, (0, 1, 2, 3), t2, (4, 0, 2, 5), (4, 1, 3, 5))
    rdm2_f_oovv += einsum(x105, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x105, (0, 1, 2, 3), (1, 0, 3, 2))
    x106 = np.zeros((nocc, nvir), dtype=np.float64)
    x106 += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3))
    rdm2_f_oovv += einsum(x106, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x106, (2, 3), (2, 0, 3, 1)) * 2.0
    rdm2_f_oovv += einsum(x106, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x106, (2, 3), (2, 0, 3, 1))
    x107 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum(x87, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x108 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x108 += einsum(x107, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x109 = np.zeros((nocc, nvir), dtype=np.float64)
    x109 += einsum(t2, (0, 1, 2, 3), l1, (2, 1), (0, 3))
    x110 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x110 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x110 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x111 = np.zeros((nocc, nvir), dtype=np.float64)
    x111 += einsum(x6, (0, 1, 2, 3), x110, (0, 1, 4, 3), (2, 4)) * 0.5
    x112 = np.zeros((nocc, nvir), dtype=np.float64)
    x112 += einsum(x15, (0, 1), t1, (0, 2), (1, 2)) * 0.5
    x113 = np.zeros((nocc, nvir), dtype=np.float64)
    x113 += einsum(x109, (0, 1), (0, 1)) * -1.0
    x113 += einsum(x111, (0, 1), (0, 1))
    x113 += einsum(x112, (0, 1), (0, 1))
    rdm2_f_oovv += einsum(x113, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x113, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x114 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x114 += einsum(x108, (0, 1, 2, 3), (1, 0, 3, 2))
    x114 += einsum(x113, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x114, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x114, (0, 1, 2, 3), (1, 0, 3, 2))
    x115 = np.zeros((nocc, nvir), dtype=np.float64)
    x115 += einsum(x16, (0, 1), t1, (0, 2), (1, 2))
    rdm2_f_oovv += einsum(x115, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(x115, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * -1.5
    rdm2_f_oovv += einsum(x115, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -1.5
    rdm2_f_oovv += einsum(x115, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * -0.5
    x116 = np.zeros((nocc, nvir), dtype=np.float64)
    x116 += einsum(x6, (0, 1, 2, 3), t2, (0, 1, 3, 4), (2, 4))
    rdm2_f_oovv += einsum(x116, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -1.5
    rdm2_f_oovv += einsum(t1, (0, 1), x116, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(x116, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(t1, (0, 1), x116, (2, 3), (2, 0, 3, 1)) * -1.5
    x117 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x117 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 5, 1), (5, 0, 4, 3))
    x118 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x118 += einsum(t2, (0, 1, 2, 3), l2, (2, 4, 0, 5), (5, 1, 4, 3))
    rdm2_f_ovov += einsum(x118, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x118, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x118, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x118, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x119 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x119 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3))
    x119 += einsum(x118, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x119 += einsum(l2, (0, 1, 2, 3), x110, (3, 4, 0, 5), (2, 4, 1, 5))
    rdm2_f_oovv += einsum(x119, (0, 1, 2, 3), t2, (4, 0, 5, 2), (4, 1, 5, 3)) * -1.0
    x120 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x120 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3))
    x120 += einsum(t2, (0, 1, 2, 3), x95, (0, 4, 2, 5), (4, 1, 5, 3)) * -1.0
    rdm2_f_oovv += einsum(x120, (0, 1, 2, 3), t2, (4, 0, 2, 5), (4, 1, 5, 3))
    x121 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x121 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x121 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x121 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x121 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x122 = np.zeros((nvir, nvir), dtype=np.float64)
    x122 += einsum(x121, (0, 1, 2, 3), l2, (3, 4, 1, 0), (4, 2)) * 3.0
    rdm2_f_oovv += einsum(x122, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1)) * -0.5
    x123 = np.zeros((nvir, nvir), dtype=np.float64)
    x123 += einsum(x85, (0, 1), (0, 1)) * 3.0
    x123 += einsum(x103, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(x123, (0, 1), t2, (2, 3, 0, 4), (2, 3, 1, 4)) * -0.5
    x124 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x124 += einsum(x53, (0, 1, 2, 3), t2, (0, 1, 4, 5), (2, 3, 4, 5))
    rdm2_f_oovv += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x124, (0, 1, 2, 3), (1, 0, 3, 2))
    x125 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x125 += einsum(t2, (0, 1, 2, 3), x69, (4, 0, 5, 2), (4, 5, 1, 3))
    x126 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x126 += einsum(x43, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x126 += einsum(x42, (0, 1, 2, 3), (0, 2, 1, 3))
    x126 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3))
    x126 += einsum(x44, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x126 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3))
    x127 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x127 += einsum(x126, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_oovv += einsum(x127, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x127, (0, 1, 2, 3), (1, 0, 3, 2))
    x128 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x128 += einsum(t2, (0, 1, 2, 3), x50, (1, 4), (4, 0, 2, 3))
    rdm2_f_oovv += einsum(x128, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x128, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x129 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x129 += einsum(t2, (0, 1, 2, 3), x28, (0, 4), (4, 1, 2, 3))
    rdm2_f_oovv += einsum(x129, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x129, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x130 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x130 += einsum(x57, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x130 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3))
    x130 += einsum(x55, (0, 1, 2, 3), (0, 2, 1, 3))
    x130 += einsum(x59, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x131 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x131 += einsum(x130, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_oovv += einsum(x131, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x131, (0, 1, 2, 3), (1, 0, 2, 3))
    x132 = np.zeros((nocc, nvir), dtype=np.float64)
    x132 += einsum(t2, (0, 1, 2, 3), l1, (2, 0), (1, 3))
    x133 = np.zeros((nocc, nocc), dtype=np.float64)
    x133 += einsum(x5, (0, 1), (0, 1))
    x133 += einsum(x17, (0, 1), (0, 1))
    x134 = np.zeros((nocc, nvir), dtype=np.float64)
    x134 += einsum(x133, (0, 1), t1, (0, 2), (1, 2))
    x135 = np.zeros((nocc, nvir), dtype=np.float64)
    x135 += einsum(t1, (0, 1), (0, 1))
    x135 += einsum(x132, (0, 1), (0, 1))
    x135 += einsum(x134, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(x135, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x135, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x136 = np.zeros((nocc, nvir), dtype=np.float64)
    x136 += einsum(x5, (0, 1), t1, (0, 2), (1, 2))
    x137 = np.zeros((nocc, nvir), dtype=np.float64)
    x137 += einsum(x136, (0, 1), (0, 1))
    x137 += einsum(x30, (0, 1), (0, 1))
    rdm2_f_oovv += einsum(x137, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_oovv += einsum(x137, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -1.0
    x138 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x138 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * 2.0
    x138 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_ovvo += einsum(x138, (0, 1, 2, 3), t2, (4, 1, 5, 3), (4, 2, 5, 0))
    x139 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x139 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x139 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x139 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0))
    x140 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x140 += einsum(x8, (0, 1, 2, 3), x138, (4, 1, 5, 3), (4, 0, 5, 2)) * -1.0
    x140 += einsum(x139, (0, 1, 2, 3), t2, (1, 4, 3, 5), (0, 4, 2, 5))
    rdm2_f_oovv += einsum(x140, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x141 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x141 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 0, 5), (5, 1, 4, 3))
    rdm2_f_ovvo += einsum(x141, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x141, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x142 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x142 += einsum(l2, (0, 1, 2, 3), x110, (3, 4, 1, 5), (2, 4, 0, 5))
    rdm2_f_voov += einsum(x142, (0, 1, 2, 3), (2, 1, 0, 3))
    x143 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x143 += einsum(x141, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x143 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x143, (1, 4, 2, 5), (4, 0, 5, 3)) * -1.0
    x144 = np.zeros((nvir, nvir), dtype=np.float64)
    x144 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 0, 4), (1, 4))
    x145 = np.zeros((nvir, nvir), dtype=np.float64)
    x145 += einsum(x85, (0, 1), (0, 1))
    x145 += einsum(x144, (0, 1), (0, 1)) * 2.0
    x145 += einsum(x103, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x145, (3, 4), (1, 0, 4, 2)) * -0.5
    x146 = np.zeros((nvir, nvir), dtype=np.float64)
    x146 += einsum(x85, (0, 1), (0, 1)) * 2.0
    x146 += einsum(x102, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x146, (2, 4), (1, 0, 3, 4)) * -0.5
    x147 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x147 += einsum(l2, (0, 1, 2, 3), x8, (4, 3, 5, 1), (2, 4, 0, 5))
    x148 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x148 += einsum(x147, (0, 1, 2, 3), t2, (0, 4, 2, 5), (1, 4, 3, 5)) * -1.0
    x149 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x149 += einsum(x21, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 0.5
    x150 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x150 += einsum(x24, (0, 1, 2, 3), x2, (4, 1, 5, 3), (4, 0, 2, 5))
    x151 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x151 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3))
    x151 += einsum(x150, (0, 1, 2, 3), (1, 2, 0, 3))
    x152 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x152 += einsum(t1, (0, 1), x151, (0, 2, 3, 4), (2, 3, 1, 4))
    x153 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x153 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x153 += einsum(x148, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x153 += einsum(x149, (0, 1, 2, 3), (1, 0, 2, 3))
    x153 += einsum(x152, (0, 1, 2, 3), (0, 1, 2, 3))
    x153 += einsum(x64, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x153, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x153, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x153, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x154 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x154 += einsum(x8, (0, 1, 2, 3), x144, (3, 4), (0, 1, 2, 4)) * 1.5
    rdm2_f_oovv += einsum(x154, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x154, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.6666666666666666
    x155 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x155 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 1, 5), (5, 0, 4, 3))
    x156 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x156 += einsum(x155, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5))
    x157 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x157 += einsum(t2, (0, 1, 2, 3), x141, (0, 4, 2, 5), (4, 1, 5, 3))
    x158 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x158 += einsum(l2, (0, 1, 2, 3), x8, (4, 3, 5, 0), (2, 4, 1, 5))
    x159 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x159 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x159 += einsum(x158, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x160 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x160 += einsum(x159, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x161 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x161 += einsum(x156, (0, 1, 2, 3), (0, 1, 2, 3))
    x161 += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3))
    x161 += einsum(x160, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x161, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x161, (0, 1, 2, 3), (1, 0, 2, 3))
    x162 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x162 += einsum(x117, (0, 1, 2, 3), t2, (4, 0, 2, 5), (4, 1, 5, 3))
    x163 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x163 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 5, 0), (5, 1, 4, 3))
    x164 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x164 += einsum(x163, (0, 1, 2, 3), t2, (0, 4, 2, 5), (4, 1, 5, 3))
    x165 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x165 += einsum(x155, (0, 1, 2, 3), (0, 1, 2, 3))
    x165 += einsum(x147, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x166 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x166 += einsum(t2, (0, 1, 2, 3), x165, (1, 4, 3, 5), (4, 0, 5, 2))
    x167 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x167 += einsum(x162, (0, 1, 2, 3), (0, 1, 2, 3))
    x167 += einsum(x164, (0, 1, 2, 3), (0, 1, 2, 3))
    x167 += einsum(x166, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x167, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x167, (0, 1, 2, 3), (1, 0, 3, 2))
    x168 = np.zeros((nvir, nvir), dtype=np.float64)
    x168 += einsum(x85, (0, 1), (0, 1))
    x168 += einsum(x103, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(x168, (0, 1), x8, (2, 3, 4, 0), (2, 3, 1, 4)) * -0.5
    x169 = np.zeros((nvir, nvir), dtype=np.float64)
    x169 += einsum(x47, (0, 1, 2, 3), l2, (3, 4, 1, 0), (4, 2))
    rdm2_f_oovv += einsum(x169, (0, 1), x2, (2, 3, 4, 0), (2, 3, 4, 1)) * 0.5
    x170 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x170 += einsum(l2, (0, 1, 2, 3), x33, (4, 3, 1, 5), (2, 4, 0, 5))
    rdm2_f_ovov += einsum(x170, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_voov += einsum(x170, (0, 1, 2, 3), (2, 1, 0, 3))
    x171 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x171 += einsum(l2, (0, 1, 2, 3), x8, (4, 2, 1, 5), (3, 4, 0, 5))
    rdm2_f_ovov += einsum(x171, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_voov += einsum(x171, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x172 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x172 += einsum(t1, (0, 1), x69, (0, 2, 3, 4), (2, 3, 1, 4))
    rdm2_f_ovov += einsum(x172, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_ovov += einsum(x172, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_vovo += einsum(x172, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_vovo += einsum(x172, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    x173 = np.zeros((nvir, nvir), dtype=np.float64)
    x173 += einsum(t1, (0, 1), l1, (2, 0), (2, 1))
    x174 = np.zeros((nvir, nvir), dtype=np.float64)
    x174 += einsum(x47, (0, 1, 2, 3), l2, (4, 2, 1, 0), (4, 3)) * 0.5
    x175 = np.zeros((nvir, nvir), dtype=np.float64)
    x175 += einsum(x173, (0, 1), (0, 1))
    x175 += einsum(x85, (0, 1), (0, 1)) * 1.5
    x175 += einsum(x174, (0, 1), (0, 1)) * -1.0
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x175, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x175, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x175, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(delta.oo, (0, 1), x175, (2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x175, (2, 3), (2, 1, 3, 0))
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x175, (2, 3), (2, 1, 3, 0))
    x176 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x176 += einsum(t1, (0, 1), x22, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovov += einsum(x176, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x176, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x177 = np.zeros((nvir, nvir), dtype=np.float64)
    x177 += einsum(x173, (0, 1), (0, 1))
    x177 += einsum(x85, (0, 1), (0, 1)) * 0.5
    x177 += einsum(x144, (0, 1), (0, 1))
    x177 += einsum(x174, (0, 1), (0, 1)) * -1.0
    rdm2_f_ovov += einsum(x177, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1))
    rdm2_f_ovov += einsum(x177, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1))
    rdm2_f_ovvo += einsum(x177, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_voov += einsum(x177, (0, 1), delta.oo, (2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_vovo += einsum(x177, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    rdm2_f_vovo += einsum(x177, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    x178 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x178 += einsum(t1, (0, 1), x6, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovov += einsum(x178, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x178, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x179 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x179 += einsum(x13, (0, 1, 2, 3), x8, (4, 1, 3, 5), (4, 0, 5, 2))
    rdm2_f_ovov += einsum(x179, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_vovo += einsum(x179, (0, 1, 2, 3), (3, 0, 2, 1))
    x180 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x180 += einsum(x24, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_ovvo += einsum(x180, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    rdm2_f_ovvo += einsum(x180, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    rdm2_f_voov += einsum(x180, (0, 1, 2, 3), (3, 1, 0, 2)) * -1.0
    rdm2_f_voov += einsum(x180, (0, 1, 2, 3), (3, 1, 0, 2)) * -1.0
    x181 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x181 += einsum(t1, (0, 1), x22, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovvo += einsum(x181, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x181, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x182 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x182 += einsum(x139, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5))
    rdm2_f_ovvo += einsum(x182, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x182, (0, 1, 2, 3), (2, 1, 0, 3))
    x183 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x183 += einsum(t1, (0, 1), x6, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovvo += einsum(x183, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x183, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x184 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x184 += einsum(x13, (0, 1, 2, 3), x2, (4, 1, 3, 5), (4, 0, 5, 2))
    rdm2_f_ovvo += einsum(x184, (0, 1, 2, 3), (0, 3, 2, 1))
    rdm2_f_voov += einsum(x184, (0, 1, 2, 3), (3, 0, 1, 2))
    x185 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x185 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x185 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.5
    rdm2_f_vovo += einsum(x185, (0, 1, 2, 3), t2, (4, 1, 5, 3), (2, 4, 5, 0)) * -2.0
    x186 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x186 += einsum(t2, (0, 1, 2, 3), l1, (4, 1), (0, 4, 2, 3))
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv += einsum(x186, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv += einsum(x186, (0, 1, 2, 3), (1, 0, 3, 2))
    x187 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x187 += einsum(x6, (0, 1, 2, 3), x79, (0, 1, 4, 5), (2, 4, 5, 3)) * 0.5
    x188 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x188 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x188 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x189 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x189 += einsum(l2, (0, 1, 2, 3), x188, (4, 3, 5, 1), (2, 4, 0, 5))
    x190 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x190 += einsum(x2, (0, 1, 2, 3), l2, (4, 3, 1, 5), (5, 0, 4, 2))
    x191 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x191 += einsum(x183, (0, 1, 2, 3), (0, 1, 2, 3))
    x191 += einsum(x189, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x191 += einsum(x190, (0, 1, 2, 3), (0, 1, 2, 3))
    x192 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x192 += einsum(x191, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    x193 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x193 += einsum(x186, (0, 1, 2, 3), (0, 1, 2, 3))
    x193 += einsum(x187, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x193 += einsum(x192, (0, 1, 2, 3), (0, 2, 1, 3))
    x193 += einsum(t1, (0, 1), x175, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvv += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x193, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x193, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x193, (0, 1, 2, 3), (1, 0, 3, 2))
    x194 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x194 += einsum(t2, (0, 1, 2, 3), x22, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_ovvv += einsum(x194, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x194, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x195 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x195 += einsum(x91, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_ovvv += einsum(x195, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x195, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x196 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x196 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x196 += einsum(x181, (0, 1, 2, 3), (0, 1, 2, 3))
    x196 += einsum(x182, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x197 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x197 += einsum(x196, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    rdm2_f_ovvv += einsum(x197, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x197, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x198 = np.zeros((nvir, nvir), dtype=np.float64)
    x198 += einsum(x173, (0, 1), (0, 1)) * 2.0
    x198 += einsum(x85, (0, 1), (0, 1))
    x198 += einsum(x144, (0, 1), (0, 1)) * 2.0
    x198 += einsum(x103, (0, 1), (0, 1)) * -1.0
    rdm2_f_ovvv += einsum(t1, (0, 1), x198, (2, 3), (0, 2, 1, 3)) * 0.5
    rdm2_f_vovv += einsum(x198, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.5
    x199 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x199 += einsum(x6, (0, 1, 2, 3), t2, (0, 1, 4, 5), (2, 3, 4, 5))
    rdm2_f_ovvv += einsum(x199, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x199, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x200 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x200 += einsum(x104, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_ovvv += einsum(x200, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x200, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x201 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x201 += einsum(t2, (0, 1, 2, 3), l1, (4, 0), (1, 4, 2, 3))
    rdm2_f_ovvv += einsum(x201, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_vovv += einsum(x201, (0, 1, 2, 3), (1, 0, 2, 3))
    x202 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x202 += einsum(x141, (0, 1, 2, 3), (0, 1, 2, 3))
    x202 += einsum(x183, (0, 1, 2, 3), (0, 1, 2, 3))
    x202 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x203 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x203 += einsum(t1, (0, 1), x202, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_ovvv += einsum(x203, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x203, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x204 = np.zeros((nvir, nvir), dtype=np.float64)
    x204 += einsum(x173, (0, 1), (0, 1)) * 2.0
    x204 += einsum(x85, (0, 1), (0, 1)) * 3.0
    x204 += einsum(x103, (0, 1), (0, 1)) * -1.0
    rdm2_f_ovvv += einsum(t1, (0, 1), x204, (2, 3), (0, 2, 1, 3)) * 0.5
    rdm2_f_vovv += einsum(x204, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.5
    x205 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x205 += einsum(x8, (0, 1, 2, 3), x95, (1, 4, 5, 3), (0, 4, 2, 5))
    x206 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x206 += einsum(x118, (0, 1, 2, 3), (0, 1, 2, 3))
    x206 += einsum(x183, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x206 += einsum(x205, (0, 1, 2, 3), (1, 0, 3, 2))
    x207 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x207 += einsum(x206, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    x208 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x208 += einsum(x186, (0, 1, 2, 3), (0, 1, 2, 3))
    x208 += einsum(x187, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x208 += einsum(x207, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x208 += einsum(x177, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovvv += einsum(x208, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x208, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x208, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x208, (0, 1, 2, 3), (1, 0, 3, 2))
    x209 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x209 += einsum(x95, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov += einsum(x209, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vvov += einsum(x209, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x210 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x210 += einsum(t1, (0, 1), l2, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_vvov += einsum(x210, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo += einsum(x210, (0, 1, 2, 3), (2, 1, 3, 0))
    x211 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x211 += einsum(l2, (0, 1, 2, 3), t1, (2, 4), (3, 0, 1, 4))
    rdm2_f_vvov += einsum(x211, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vvvo += einsum(x211, (0, 1, 2, 3), (1, 2, 3, 0))
    x212 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x212 += einsum(x13, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    rdm2_f_vvvo += einsum(x212, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vvvo += einsum(x212, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x213 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x213 += einsum(x210, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x213, (0, 1, 2, 3), (1, 0, 3, 2))
    x214 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x214 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x214 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x215 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x215 += einsum(x214, (0, 1, 2, 3), l2, (4, 5, 1, 0), (4, 5, 2, 3)) * 0.5
    x216 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x216 += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3))
    x216 += einsum(x215, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vvvv += einsum(x216, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x216, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vvvv += einsum(x216, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x216, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x217 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x217 += einsum(t2, (0, 1, 2, 3), l2, (4, 5, 0, 1), (4, 5, 2, 3))
    rdm2_f_vvvv += einsum(x217, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x217, (0, 1, 2, 3), (1, 0, 3, 2))

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

