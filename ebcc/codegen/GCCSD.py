# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(f.ov, (0, 1), t1, (0, 1), ())
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    e_cc += einsum(v.oovv, (0, 1, 2, 3), x0, (0, 1, 2, 3), ()) * 0.25

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t1new += einsum(v.ovov, (0, 1, 2, 3), t1, (2, 1), (0, 3)) * -1.0
    t1new += einsum(f.vv, (0, 1), t1, (2, 1), (2, 0))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum(v.oovv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x1 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x1 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new += einsum(x1, (0, 1, 2, 3), t2, (1, 2, 3, 4), (0, 4)) * -0.5
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x2 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    t1new += einsum(x2, (0, 1, 2, 3), v.ovvv, (0, 4, 2, 3), (1, 4)) * 0.5
    t2new += einsum(x2, (0, 1, 2, 3), v.vvvv, (2, 3, 4, 5), (1, 0, 4, 5)) * -0.5
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum(v.oovv, (0, 1, 2, 3), t1, (1, 3), (0, 2))
    x4 = np.zeros((nocc, nvir), dtype=np.float64)
    x4 += einsum(f.ov, (0, 1), (0, 1))
    x4 += einsum(x3, (0, 1), (0, 1))
    t1new += einsum(x4, (0, 1), t2, (0, 2, 1, 3), (2, 3))
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(t1, (0, 1), v.ooov, (0, 2, 3, 1), (2, 3)) * -1.0
    x6 = np.zeros((nocc, nocc), dtype=np.float64)
    x6 += einsum(f.oo, (0, 1), (1, 0))
    x6 += einsum(t1, (0, 1), f.ov, (2, 1), (2, 0))
    x6 += einsum(x5, (0, 1), (0, 1))
    x6 += einsum(v.oovv, (0, 1, 2, 3), x2, (0, 4, 2, 3), (1, 4)) * 0.5
    t1new += einsum(x6, (0, 1), t1, (0, 2), (1, 2)) * -1.0
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(t2, (0, 1, 2, 3), x8, (4, 1, 5, 3), (4, 0, 2, 5)) * -1.0
    x10 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x10 += einsum(v.ovov, (0, 1, 2, 3), t1, (4, 1), (4, 2, 0, 3))
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 0, 5, 3), (4, 1, 2, 5)) * -1.0
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(t2, (0, 1, 2, 3), x0, (4, 1, 5, 3), (4, 0, 5, 2))
    x13 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 += einsum(x12, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x15 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x15 += einsum(x14, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x15, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x15, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x15, (0, 1, 2, 3), (1, 0, 3, 2))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x17 = np.zeros((nocc, nocc), dtype=np.float64)
    x17 += einsum(x4, (0, 1), t1, (2, 1), (2, 0))
    x18 = np.zeros((nocc, nocc), dtype=np.float64)
    x18 += einsum(f.oo, (0, 1), (1, 0))
    x18 += einsum(x17, (0, 1), (0, 1))
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(t2, (0, 1, 2, 3), x18, (4, 0), (4, 1, 2, 3))
    x20 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x20 += einsum(v.ooov, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(x2, (0, 1, 2, 3), x20, (4, 0, 1, 5), (4, 5, 2, 3)) * 0.5
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 0, 2, 3), (4, 1)) * -1.0
    x23 = np.zeros((nocc, nocc), dtype=np.float64)
    x23 += einsum(x5, (0, 1), (0, 1))
    x23 += einsum(x22, (0, 1), (1, 0)) * 0.5
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(t2, (0, 1, 2, 3), x23, (0, 4), (4, 1, 2, 3))
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(x16, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x25 += einsum(x19, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x25 += einsum(x21, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x25 += einsum(x24, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3))
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(t2, (0, 1, 2, 3), v.oovv, (1, 4, 3, 5), (0, 4, 2, 5))
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(x26, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5))
    x28 = np.zeros((nvir, nvir), dtype=np.float64)
    x28 += einsum(t1, (0, 1), v.ovvv, (0, 2, 1, 3), (2, 3)) * -1.0
    x29 = np.zeros((nvir, nvir), dtype=np.float64)
    x29 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 3, 4), (2, 4)) * -1.0
    x30 = np.zeros((nvir, nvir), dtype=np.float64)
    x30 += einsum(x28, (0, 1), (0, 1))
    x30 += einsum(x29, (0, 1), (0, 1)) * 0.5
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(x30, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum(v.ovvv, (0, 1, 2, 3), x2, (4, 5, 2, 3), (0, 4, 5, 1)) * 0.5
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum(t2, (0, 1, 2, 3), x4, (4, 2), (0, 1, 4, 3))
    x34 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x34 += einsum(x32, (0, 1, 2, 3), (0, 2, 1, 3))
    x34 += einsum(x33, (0, 1, 2, 3), (2, 1, 0, 3))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(x34, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4))
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x36 += einsum(x31, (0, 1, 2, 3), (1, 0, 3, 2))
    x36 += einsum(x35, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x36, (0, 1, 2, 3), (0, 1, 3, 2))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(f.vv, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4))
    x39 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(x37, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x39 += einsum(x38, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x39, (0, 1, 2, 3), (0, 1, 3, 2))
    x40 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x40 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x40 += einsum(v.oovv, (0, 1, 2, 3), x2, (4, 5, 2, 3), (1, 0, 5, 4))
    t2new += einsum(x2, (0, 1, 2, 3), x40, (0, 1, 4, 5), (4, 5, 3, 2)) * -0.25

    return {"t1new": t1new, "t2new": t2new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    # L amplitudes
    l1new = np.zeros((nvir, nocc), dtype=np.float64)
    l1new += einsum(f.ov, (0, 1), (1, 0))
    l1new += einsum(v.ovov, (0, 1, 2, 3), l1, (1, 2), (3, 0)) * -1.0
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(v.oovv, (0, 1, 2, 3), (3, 2, 1, 0))
    l2new += einsum(v.vvvv, (0, 1, 2, 3), l2, (2, 3, 4, 5), (1, 0, 5, 4)) * 0.5
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 0), (2, 4, 1, 5)) * -1.0
    l1new += einsum(x0, (0, 1, 2, 3), v.ovvv, (1, 2, 4, 3), (4, 0)) * -1.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(l2, (0, 1, 2, 3), t1, (4, 1), (2, 3, 4, 0))
    l1new += einsum(x2, (0, 1, 2, 3), x1, (1, 2, 3, 4), (4, 0))
    l1new += einsum(x2, (0, 1, 2, 3), v.ovov, (1, 4, 2, 3), (4, 0)) * -1.0
    l2new += einsum(x2, (0, 1, 2, 3), v.ovvv, (2, 3, 4, 5), (4, 5, 0, 1))
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum(v.oovv, (0, 1, 2, 3), t1, (0, 3), (1, 2)) * -1.0
    x4 = np.zeros((nocc, nocc), dtype=np.float64)
    x4 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    l1new += einsum(x3, (0, 1), x4, (2, 0), (1, 2)) * -1.0
    x5 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x5 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    l1new += einsum(v.ooov, (0, 1, 2, 3), x5, (4, 2, 0, 1), (3, 4)) * -0.25
    x6 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x6 += einsum(x2, (0, 1, 2, 3), t1, (4, 3), (1, 0, 2, 4))
    l1new += einsum(v.ooov, (0, 1, 2, 3), x6, (4, 2, 1, 0), (3, 4)) * 0.5
    x7 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x7 += einsum(v.oovv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x8 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x8 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x8 += einsum(x7, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x9 = np.zeros((nocc, nvir), dtype=np.float64)
    x9 += einsum(f.ov, (0, 1), (0, 1))
    x9 += einsum(x3, (0, 1), (0, 1))
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x10 += einsum(x1, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x11 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x11 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 5, 2, 3), (4, 5, 0, 1))
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x12 += einsum(x7, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    x13 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x13 += einsum(t1, (0, 1), x12, (2, 3, 4, 1), (2, 3, 4, 0)) * 4.0
    x14 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x14 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * 2.0
    x14 += einsum(x11, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x14 += einsum(x13, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x15 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x15 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 5, 2, 3), (4, 1, 0, 5)) * 0.5
    x15 += einsum(t2, (0, 1, 2, 3), x8, (4, 0, 5, 2), (5, 1, 4, 3)) * 2.0
    x15 += einsum(t2, (0, 1, 2, 3), x9, (4, 2), (4, 1, 0, 3))
    x15 += einsum(x10, (0, 1, 2, 3), t1, (4, 2), (1, 0, 4, 3)) * -2.0
    x15 += einsum(x14, (0, 1, 2, 3), t1, (0, 4), (1, 3, 2, 4)) * -0.5
    l1new += einsum(l2, (0, 1, 2, 3), x15, (4, 2, 3, 0), (1, 4)) * -0.5
    x16 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x16 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x16 += einsum(t1, (0, 1), v.vvvv, (2, 1, 3, 4), (0, 2, 4, 3))
    l1new += einsum(l2, (0, 1, 2, 3), x16, (2, 4, 0, 1), (4, 3)) * 0.5
    x17 = np.zeros((nocc, nocc), dtype=np.float64)
    x17 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 1), (3, 4))
    x18 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x18 += einsum(x5, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x18 += einsum(x6, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    l2new += einsum(x18, (0, 1, 2, 3), v.oovv, (2, 3, 4, 5), (5, 4, 1, 0)) * -0.25
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(l1, (0, 1), t2, (2, 3, 4, 0), (1, 3, 2, 4)) * -2.0
    x19 += einsum(t1, (0, 1), x17, (2, 3), (2, 0, 3, 1)) * 2.0
    x19 += einsum(t2, (0, 1, 2, 3), x2, (4, 1, 5, 3), (4, 0, 5, 2)) * -4.0
    x19 += einsum(x18, (0, 1, 2, 3), t1, (0, 4), (1, 3, 2, 4)) * -1.0
    l1new += einsum(v.oovv, (0, 1, 2, 3), x19, (4, 0, 1, 2), (3, 4)) * -0.25
    x20 = np.zeros((nvir, nvir), dtype=np.float64)
    x20 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 0, 4), (1, 4))
    x21 = np.zeros((nvir, nvir), dtype=np.float64)
    x21 += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    x21 += einsum(x20, (0, 1), (0, 1)) * 0.5
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x21, (1, 2), (3, 0)) * -1.0
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum(x4, (0, 1), (0, 1))
    x22 += einsum(x17, (0, 1), (0, 1)) * 0.5
    l1new += einsum(x22, (0, 1), v.ooov, (1, 2, 0, 3), (3, 2)) * -1.0
    x23 = np.zeros((nocc, nvir), dtype=np.float64)
    x23 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x23 += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3)) * -1.0
    x23 += einsum(t2, (0, 1, 2, 3), x2, (0, 1, 4, 2), (4, 3)) * 0.5
    x23 += einsum(t1, (0, 1), x22, (0, 2), (2, 1))
    l1new += einsum(v.oovv, (0, 1, 2, 3), x23, (0, 2), (3, 1)) * -1.0
    x24 = np.zeros((nvir, nvir), dtype=np.float64)
    x24 += einsum(v.ovvv, (0, 1, 2, 3), t1, (0, 3), (1, 2))
    x25 = np.zeros((nvir, nvir), dtype=np.float64)
    x25 += einsum(f.vv, (0, 1), (1, 0))
    x25 += einsum(x24, (0, 1), (0, 1)) * -1.0
    l1new += einsum(l1, (0, 1), x25, (0, 2), (2, 1))
    x26 = np.zeros((nocc, nocc), dtype=np.float64)
    x26 += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 1), (2, 3))
    x27 = np.zeros((nocc, nocc), dtype=np.float64)
    x27 += einsum(v.oovv, (0, 1, 2, 3), t2, (1, 4, 2, 3), (4, 0)) * -1.0
    x28 = np.zeros((nocc, nocc), dtype=np.float64)
    x28 += einsum(f.oo, (0, 1), (1, 0))
    x28 += einsum(x26, (0, 1), (1, 0))
    x28 += einsum(x27, (0, 1), (0, 1)) * 0.5
    x28 += einsum(x9, (0, 1), t1, (2, 1), (2, 0))
    l1new += einsum(x28, (0, 1), l1, (2, 0), (2, 1)) * -1.0
    x29 = np.zeros((nocc, nocc), dtype=np.float64)
    x29 += einsum(x4, (0, 1), (0, 1)) * 2.0
    x29 += einsum(x17, (0, 1), (0, 1))
    l1new += einsum(x29, (0, 1), f.ov, (1, 2), (2, 0)) * -0.5
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(v.ooov, (0, 1, 2, 3), x2, (4, 2, 1, 5), (4, 0, 5, 3))
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(x7, (0, 1, 2, 3), x2, (0, 4, 2, 5), (4, 1, 5, 3)) * -1.0
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 0, 2, 5), (1, 4, 3, 5)) * -1.0
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x33 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3))
    x33 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(x33, (0, 1, 2, 3), l2, (2, 4, 0, 5), (1, 5, 3, 4))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(f.ov, (0, 1), l1, (2, 3), (0, 3, 1, 2))
    x35 += einsum(l1, (0, 1), x3, (2, 3), (1, 2, 0, 3))
    x35 += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3))
    x35 += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x35 += einsum(x34, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x35, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x35, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x35, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new += einsum(x35, (0, 1, 2, 3), (3, 2, 1, 0))
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(f.vv, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(f.ov, (0, 1), x2, (2, 3, 0, 4), (2, 3, 1, 4))
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(x20, (0, 1), v.oovv, (2, 3, 4, 1), (3, 2, 0, 4))
    x39 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(x2, (0, 1, 2, 3), x3, (2, 4), (0, 1, 3, 4))
    x40 = np.zeros((nvir, nvir), dtype=np.float64)
    x40 += einsum(v.oovv, (0, 1, 2, 3), t2, (0, 1, 3, 4), (4, 2)) * -1.0
    x41 = np.zeros((nvir, nvir), dtype=np.float64)
    x41 += einsum(x24, (0, 1), (0, 1))
    x41 += einsum(x40, (0, 1), (0, 1)) * 0.5
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(x41, (0, 1), l2, (0, 2, 3, 4), (3, 4, 1, 2))
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(l1, (0, 1), x8, (1, 2, 3, 4), (2, 3, 4, 0))
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x44 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x44 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x44 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3))
    x44 += einsum(x42, (0, 1, 2, 3), (1, 0, 3, 2))
    x44 += einsum(x43, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x44, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x44, (0, 1, 2, 3), (3, 2, 0, 1))
    x45 = np.zeros((nocc, nocc), dtype=np.float64)
    x45 += einsum(t1, (0, 1), f.ov, (2, 1), (2, 0))
    x46 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x46 += einsum(x45, (0, 1), l2, (2, 3, 4, 1), (0, 4, 2, 3))
    x47 = np.zeros((nocc, nocc), dtype=np.float64)
    x47 += einsum(x3, (0, 1), t1, (2, 1), (2, 0))
    x48 = np.zeros((nocc, nocc), dtype=np.float64)
    x48 += einsum(x26, (0, 1), (0, 1))
    x48 += einsum(x27, (0, 1), (1, 0)) * 0.5
    x48 += einsum(x47, (0, 1), (1, 0))
    x49 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x49 += einsum(l2, (0, 1, 2, 3), x48, (4, 2), (4, 3, 0, 1))
    x50 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x50 += einsum(v.oovv, (0, 1, 2, 3), x22, (4, 0), (4, 1, 2, 3))
    x51 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x51 += einsum(x46, (0, 1, 2, 3), (0, 1, 3, 2))
    x51 += einsum(x49, (0, 1, 2, 3), (1, 0, 3, 2))
    x51 += einsum(x50, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new += einsum(x51, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x51, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(l2, (0, 1, 2, 3), f.oo, (4, 3), (4, 2, 0, 1))
    x53 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(v.ovvv, (0, 1, 2, 3), l1, (1, 4), (4, 0, 2, 3))
    x54 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum(x52, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x54 += einsum(x53, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(x54, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x54, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x55 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x55 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x55 += einsum(x11, (0, 1, 2, 3), (1, 0, 3, 2))
    x55 += einsum(x13, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x55, (2, 3, 4, 5), (1, 0, 4, 5)) * -0.25

    return {"l1new": l1new, "l2new": l2new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM1
    rdm1_f_oo = np.zeros((nocc, nocc), dtype=np.float64)
    rdm1_f_oo += einsum(delta.oo, (0, 1), (1, 0))
    rdm1_f_ov = np.zeros((nocc, nvir), dtype=np.float64)
    rdm1_f_ov += einsum(t1, (0, 1), (0, 1))
    rdm1_f_ov += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3))
    rdm1_f_vo = np.zeros((nvir, nocc), dtype=np.float64)
    rdm1_f_vo += einsum(l1, (0, 1), (0, 1))
    rdm1_f_vv = np.zeros((nvir, nvir), dtype=np.float64)
    rdm1_f_vv += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    rdm1_f_vv += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 0), (1, 4)) * -0.5
    x0 = np.zeros((nocc, nocc), dtype=np.float64)
    x0 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm1_f_oo += einsum(x0, (0, 1), (1, 0)) * -1.0
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 1), (4, 0))
    rdm1_f_oo += einsum(x1, (0, 1), (1, 0)) * -0.5
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(l2, (0, 1, 2, 3), t1, (4, 1), (2, 3, 4, 0))
    rdm1_f_ov += einsum(t2, (0, 1, 2, 3), x2, (0, 1, 4, 3), (4, 2)) * 0.5
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(x0, (0, 1), (0, 1))
    x3 += einsum(x1, (0, 1), (0, 1)) * 0.5
    rdm1_f_ov += einsum(t1, (0, 1), x3, (0, 2), (2, 1)) * -1.0

    rdm1_f = np.block([[rdm1_f_oo, rdm1_f_ov], [rdm1_f_vo, rdm1_f_vv]])

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM2
    rdm2_f_oooo = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo += einsum(l1, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1))
    rdm2_f_ovoo += einsum(l1, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo += einsum(l1, (0, 1), delta.oo, (2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_vooo += einsum(l1, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2))
    rdm2_f_oovv = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_ovov += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_ovvo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_ovvo += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_voov = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_voov += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_vovo = np.zeros((nvir, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_vovo += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vvoo = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 5), (1, 0, 5, 4)) * 0.5
    x0 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x0 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_oooo += einsum(x0, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.5
    x1 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum(l2, (0, 1, 2, 3), t1, (4, 1), (2, 3, 4, 0))
    rdm2_f_ovoo += einsum(x1, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x1, (0, 1, 2, 3), (3, 2, 1, 0))
    x2 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x2 += einsum(t1, (0, 1), x1, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_oooo += einsum(x2, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 1), (4, 0))
    rdm2_f_oooo += einsum(x3, (0, 1), delta.oo, (2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_oooo += einsum(x3, (0, 1), delta.oo, (2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x3, (2, 3), (3, 1, 0, 2)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x3, (2, 3), (3, 1, 2, 0)) * -0.5
    x4 = np.zeros((nocc, nocc), dtype=np.float64)
    x4 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm2_f_oooo += einsum(x4, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_oooo += einsum(x4, (0, 1), delta.oo, (2, 3), (1, 3, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x4, (2, 3), (1, 3, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x4, (2, 3), (3, 1, 2, 0)) * -1.0
    x5 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x5 += einsum(l1, (0, 1), t2, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov += einsum(x5, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo += einsum(x5, (0, 1, 2, 3), (2, 1, 3, 0))
    x6 = np.zeros((nocc, nvir), dtype=np.float64)
    x6 += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3))
    x7 = np.zeros((nocc, nvir), dtype=np.float64)
    x7 += einsum(x1, (0, 1, 2, 3), t2, (0, 1, 4, 3), (2, 4)) * -1.0
    x8 = np.zeros((nocc, nocc), dtype=np.float64)
    x8 += einsum(x4, (0, 1), (0, 1))
    x8 += einsum(x3, (0, 1), (0, 1)) * 0.5
    x9 = np.zeros((nocc, nvir), dtype=np.float64)
    x9 += einsum(t1, (0, 1), x8, (0, 2), (2, 1))
    x10 = np.zeros((nocc, nvir), dtype=np.float64)
    x10 += einsum(x6, (0, 1), (0, 1)) * -1.0
    x10 += einsum(x7, (0, 1), (0, 1)) * 0.5
    x10 += einsum(x9, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(x10, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x10, (2, 3), (2, 0, 1, 3))
    rdm2_f_oovo += einsum(x10, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x10, (2, 3), (2, 0, 3, 1)) * -1.0
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(t2, (0, 1, 2, 3), x1, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(delta.oo, (0, 1), t1, (2, 3), (1, 0, 2, 3))
    x12 += einsum(x11, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x12 += einsum(x8, (0, 1), t1, (2, 3), (2, 0, 1, 3))
    rdm2_f_ooov += einsum(x12, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x12, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x12, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x12, (0, 1, 2, 3), (2, 0, 3, 1))
    x13 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x13 += einsum(x0, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x13 += einsum(x2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x13, (0, 1, 4, 5), (5, 4, 3, 2)) * -0.25
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4)) * 0.5
    rdm2_f_ooov += einsum(x14, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x14, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_oovv += einsum(x14, (0, 1, 2, 3), t1, (0, 4), (2, 1, 3, 4))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(x11, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3))
    x16 += einsum(x10, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x16, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x16, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum(t2, (0, 1, 2, 3), x4, (1, 4), (4, 0, 2, 3))
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(x3, (0, 1), t2, (2, 0, 3, 4), (2, 1, 3, 4))
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(x17, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x19 += einsum(x18, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    rdm2_f_oovv += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x19, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(x5, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    x21 = np.zeros((nvir, nvir), dtype=np.float64)
    x21 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 0), (1, 4)) * -1.0
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(t2, (0, 1, 2, 3), x21, (3, 4), (0, 1, 2, 4))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 0), (2, 4, 1, 5)) * -1.0
    rdm2_f_ovov += einsum(x23, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x23, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x23, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x23, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(t2, (0, 1, 2, 3), x23, (1, 4, 3, 5), (4, 0, 5, 2))
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x25 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x25, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(x1, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    rdm2_f_ovov += einsum(x26, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_ovvo += einsum(x26, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x26, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x26, (0, 1, 2, 3), (2, 1, 3, 0))
    x27 = np.zeros((nvir, nvir), dtype=np.float64)
    x27 += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    x28 = np.zeros((nvir, nvir), dtype=np.float64)
    x28 += einsum(x27, (0, 1), (0, 1)) * 2.0
    x28 += einsum(x21, (0, 1), (0, 1))
    rdm2_f_ovov += einsum(x28, (0, 1), delta.oo, (2, 3), (3, 0, 2, 1)) * 0.5
    rdm2_f_ovvo += einsum(x28, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -0.5
    rdm2_f_voov += einsum(x28, (0, 1), delta.oo, (2, 3), (0, 3, 2, 1)) * -0.5
    rdm2_f_vovo += einsum(x28, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2)) * 0.5
    x29 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x29 += einsum(x1, (0, 1, 2, 3), t2, (0, 1, 4, 5), (2, 3, 4, 5))
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv += einsum(x29, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv += einsum(x29, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x30 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x30 += einsum(x26, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4)) * -1.0
    rdm2_f_ovvv += einsum(x30, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x30, (0, 1, 2, 3), (1, 0, 3, 2))
    x31 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x31 += einsum(t2, (0, 1, 2, 3), l1, (4, 1), (0, 4, 2, 3))
    rdm2_f_ovvv += einsum(x31, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x31, (0, 1, 2, 3), (1, 0, 3, 2))
    x32 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x32 += einsum(t1, (0, 1), x23, (0, 2, 3, 4), (2, 3, 1, 4))
    x33 = np.zeros((nvir, nvir), dtype=np.float64)
    x33 += einsum(x27, (0, 1), (0, 1))
    x33 += einsum(x21, (0, 1), (0, 1)) * 0.5
    x34 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x34 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x34 += einsum(x33, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovvv += einsum(x34, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x34, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x34, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x34, (0, 1, 2, 3), (1, 0, 3, 2))
    x35 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x35 += einsum(l2, (0, 1, 2, 3), t1, (3, 4), (2, 0, 1, 4))
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov += einsum(x35, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo += einsum(x35, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_vvvv += einsum(t1, (0, 1), x35, (0, 2, 3, 4), (2, 3, 1, 4))

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

def make_ip_mom_kets(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta_oo = np.eye(nocc)
    delta_vv = np.eye(nvir)

    ket2_o = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    ket1_o = np.zeros((nocc, nocc), dtype=np.float64)
    ket1_o += einsum("ij->ji", delta_oo)
    ket1_v = np.zeros((nocc, nvir), dtype=np.float64)
    ket1_v += einsum("ia->ia", t1)
    ket2_v = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    ket2_v -= einsum("ijab->jiba", t2)

    ket1 = np.concatenate([ket1_o, ket1_v], axis=1)
    ket2 = np.concatenate([ket2_o, ket2_v], axis=3)

    return ket1, ket2

def make_ea_mom_kets(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta_oo = np.eye(nocc)
    delta_vv = np.eye(nvir)

    ket2_v = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    ket1_o = np.zeros((nvir, nocc), dtype=np.float64)
    ket1_o -= einsum("ia->ai", t1)
    ket1_v = np.zeros((nvir, nvir), dtype=np.float64)
    ket1_v += einsum("ab->ba", delta_vv)
    ket2_o = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    ket2_o += einsum("ijab->baji", t2)

    ket1 = np.concatenate([ket1_o, ket1_v], axis=1)
    ket2 = np.concatenate([ket2_o, ket2_v], axis=3)

    return ket1, ket2

def make_ip_mom_bras(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta_oo = np.eye(nocc)
    delta_vv = np.eye(nvir)

    bra1_o = np.zeros((nocc, nocc), dtype=np.float64)
    bra1_o += einsum("abij,kjab->ki", l2, t2) * -0.5
    bra1_o += einsum("ij->ji", delta_oo)
    bra1_o -= einsum("ai,ja->ji", l1, t1)
    bra1_v = np.zeros((nvir, nocc), dtype=np.float64)
    bra1_v += einsum("ai->ai", l1)
    bra2_o = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    bra2_o -= einsum("ia,bajk->ikjb", t1, l2)
    bra2_o += einsum("ij,ak->jika", delta_oo, l1)
    bra2_o -= einsum("ij,ak->jkia", delta_oo, l1)
    bra2_v = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    bra2_v += einsum("abij->bjia", l2)

    bra1 = np.concatenate([bra1_o, bra1_v], axis=0)
    bra2 = np.concatenate([bra2_o, bra2_v], axis=0)

    return bra1, bra2

def make_ea_mom_bras(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta_oo = np.eye(nocc)
    delta_vv = np.eye(nvir)

    bra1_o = np.zeros((nocc, nvir), dtype=np.float64)
    bra1_o -= einsum("ai->ia", l1)
    bra1_v = np.zeros((nvir, nvir), dtype=np.float64)
    bra1_v += einsum("ab->ba", delta_vv)
    bra1_v -= einsum("ai,ib->ba", l1, t1)
    bra1_v += einsum("abij,ijcb->ca", l2, t2) * -0.5
    bra2_o = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    bra2_o -= einsum("abij->jbai", l2)
    bra2_v = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    bra2_v -= einsum("ia,bcji->acbj", t1, l2)
    bra2_v += einsum("ab,ci->baci", delta_vv, l1)
    bra2_v -= einsum("ab,ci->bcai", delta_vv, l1)

    bra1 = np.concatenate([bra1_o, bra1_v], axis=0)
    bra2 = np.concatenate([bra2_o, bra2_v], axis=0)

    return bra1, bra2

def hbar_matvec_ip(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, r1=None, r2=None, **kwargs):
    x0 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum("i,jiab->jab", r1, v.oovv)
    x47 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x47 += einsum("ia,jba->ijb", t1, x0)
    x48 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x48 += einsum("ija,kjba->ikb", x47, t2)
    x60 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x60 += einsum("ija->ija", x48)
    del x48
    x63 = np.zeros((nocc, nocc, nocc), dtype=np.float64)
    x63 += einsum("ia,jka->kij", t1, x47)
    del x47
    r1new = np.zeros((nocc), dtype=np.float64)
    r1new += einsum("iab,jiab->j", x0, t2) * 0.5
    del x0
    x1 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum("ija->ija", r2)
    x1 += einsum("i,ja->ija", r1, t1) * 2
    x6 = np.zeros((nvir), dtype=np.float64)
    x6 += einsum("ija,jiab->b", x1, v.oovv) * 0.5
    x7 = np.zeros((nvir), dtype=np.float64)
    x7 += einsum("a->a", x6)
    del x6
    x61 = np.zeros((nvir, nvir, nvir), dtype=np.float64)
    x61 += einsum("ija,jibc->acb", x1, v.oovv) * 0.5
    r1new += einsum("ija,jika->k", x1, v.ooov) * 0.5
    del x1
    x2 = np.zeros((nocc, nvir), dtype=np.float64)
    x2 += einsum("ia,jiba->jb", t1, v.oovv)
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum("ia->ia", x2)
    x50 = np.zeros((nocc, nvir), dtype=np.float64)
    x50 += einsum("ia->ia", x2)
    del x2
    x3 += einsum("ia->ia", f.ov)
    x4 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum("ija->ija", r2)
    x4 += einsum("ija->jia", r2) * -1
    x30 = np.zeros((nocc, nocc, nocc), dtype=np.float64)
    x30 += einsum("ija,ikla->klj", x4, v.ooov)
    x31 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x31 += einsum("ia,ijk->kja", t1, x30) * 0.5
    del x30
    x40 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x40 += einsum("ija->ija", x31)
    del x31
    r1new += einsum("ia,ija->j", x3, x4) * -0.5
    del x3
    del x4
    x5 = np.zeros((nvir), dtype=np.float64)
    x5 += einsum("i,ia->a", r1, f.ov)
    x7 += einsum("a->a", x5)
    del x5
    r1new += einsum("a,ia->i", x7, t1) * -1
    r2new = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    r2new += einsum("a,ijab->jib", x7, t2)
    del x7
    x8 = np.zeros((nvir, nvir, nvir), dtype=np.float64)
    x8 += einsum("i,iabc->abc", r1, v.ovvv)
    x9 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum("ia,bca->ibc", t1, x8)
    r2new -= einsum("ia,jba->ijb", t1, x9)
    del x9
    x61 += einsum("abc->acb", x8)
    del x8
    r2new += einsum("abc,ijbc->jia", x61, t2) * -0.5
    del x61
    x10 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x10 += einsum("ia,jkla->ijkl", t1, v.ooov)
    x11 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x11 -= einsum("ija,kjil->kla", r2, x10)
    del x10
    x40 += einsum("ija->ija", x11) * 0.5
    del x11
    x12 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum("ija->ija", r2) * -1
    x12 += einsum("ija->jia", r2)
    x16 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum("ija,jkab->ikb", x12, v.oovv)
    x32 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum("ij,ika->kja", f.oo, x12) * 0.5
    x40 += einsum("ija->jia", x32) * -1
    del x32
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum("ia,jbca->ijbc", t1, v.ovvv)
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum("ijab->jiab", x13) * -1
    del x13
    x14 += einsum("iajb->ijab", v.ovov)
    x15 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum("ija,jkba->ikb", x12, x14) * 0.5
    del x14
    x40 += einsum("ija->ija", x15) * -1
    del x15
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum("ijab->jiba", t2)
    x17 += einsum("ia,jb->ijba", t1, t1) * -1
    x18 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x18 += einsum("ija,jkab->ikb", x16, x17) * -0.5
    del x16
    del x17
    x40 += einsum("ija->ija", x18) * -1
    del x18
    x19 = np.zeros((nvir, nvir), dtype=np.float64)
    x19 += einsum("ia,ib->ab", f.ov, t1)
    x23 = np.zeros((nvir, nvir), dtype=np.float64)
    x23 += einsum("ab->ba", x19)
    del x19
    x20 = np.zeros((nvir, nvir), dtype=np.float64)
    x20 -= einsum("ia,ibac->bc", t1, v.ovvv)
    x23 += einsum("ab->ab", x20)
    x52 = np.zeros((nvir, nvir), dtype=np.float64)
    x52 -= einsum("ab->ab", x20)
    del x20
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum("ijab->jiba", t2)
    x21 += einsum("ia,jb->ijab", t1, t1) * 2
    x22 = np.zeros((nvir, nvir), dtype=np.float64)
    x22 += einsum("ijab,ijac->cb", v.oovv, x21) * 0.5
    x23 += einsum("ab->ab", x22)
    del x22
    x27 = np.zeros((nocc, nocc), dtype=np.float64)
    x27 += einsum("ijab,ikab->kj", v.oovv, x21) * 0.5
    del x21
    x28 = np.zeros((nocc, nocc), dtype=np.float64)
    x28 += einsum("ij->ji", x27)
    del x27
    x23 += einsum("ab->ab", f.vv) * -1
    x24 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x24 += einsum("ab,ijb->ija", x23, r2) * 0.5
    del x23
    x40 += einsum("ija->ija", x24)
    del x24
    x25 = np.zeros((nocc, nocc), dtype=np.float64)
    x25 += einsum("ia,ja->ij", f.ov, t1)
    x28 += einsum("ij->ij", x25)
    del x25
    x26 = np.zeros((nocc, nocc), dtype=np.float64)
    x26 -= einsum("ia,ijka->jk", t1, v.ooov)
    x28 += einsum("ij->ij", x26)
    x29 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x29 += einsum("ij,kia->kja", x28, x12) * 0.5
    del x12
    del x28
    x40 += einsum("ija->ija", x29) * -1
    del x29
    x55 = np.zeros((nocc, nocc), dtype=np.float64)
    x55 += einsum("ij->ij", x26)
    del x26
    x33 = np.zeros((nocc, nvir), dtype=np.float64)
    x33 += einsum("ijab,jcab->ic", t2, v.ovvv)
    x39 = np.zeros((nocc, nvir), dtype=np.float64)
    x39 += einsum("ia->ia", x33)
    del x33
    x34 = np.zeros((nocc, nocc), dtype=np.float64)
    x34 -= einsum("ijab,jkab->ik", t2, v.oovv)
    x35 = np.zeros((nocc, nvir), dtype=np.float64)
    x35 += einsum("ia,ji->ja", t1, x34)
    del x34
    x39 += einsum("ia->ia", x35)
    del x35
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum("ia,jkba->ijkb", t1, v.oovv)
    x37 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x37 += einsum("ijka->ikja", x36) * -1
    x62 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x62 += einsum("ia,jkla->lkij", t1, x36) * -1
    del x36
    x37 += einsum("ijka->kjia", v.ooov)
    x38 = np.zeros((nocc, nvir), dtype=np.float64)
    x38 += einsum("ijab,kija->kb", t2, x37)
    del x37
    x39 += einsum("ia->ia", x38)
    del x38
    x40 += einsum("i,ja->ija", r1, x39) * 0.5
    del x39
    r2new += einsum("ija->ija", x40) * -1
    r2new += einsum("ija->jia", x40)
    del x40
    x41 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum("i,iajb->jab", r1, v.ovov)
    x42 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum("ia,jba->ijb", t1, x41)
    del x41
    x60 -= einsum("ija->ija", x42)
    del x42
    x43 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x43 += einsum("i,jika->jka", r1, v.ooov)
    x44 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x44 -= einsum("ija,kiba->kjb", x43, t2)
    x60 -= einsum("ija->ija", x44)
    del x44
    x45 = np.zeros((nocc, nocc, nocc), dtype=np.float64)
    x45 += einsum("ia,jka->ijk", t1, x43)
    del x43
    x46 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x46 -= einsum("ia,jik->jka", t1, x45)
    del x45
    x60 += einsum("ija->ija", x46)
    del x46
    x49 = np.zeros((nocc, nvir), dtype=np.float64)
    x49 += einsum("ia,ibja->jb", t1, v.ovov)
    x57 = np.zeros((nocc, nvir), dtype=np.float64)
    x57 += einsum("ia->ia", x49)
    del x49
    x50 += einsum("ia->ia", f.ov)
    x51 = np.zeros((nocc, nvir), dtype=np.float64)
    x51 += einsum("ia,ijab->jb", x50, t2)
    x57 -= einsum("ia->ia", x51)
    del x51
    x54 = np.zeros((nocc, nocc), dtype=np.float64)
    x54 += einsum("ia,ja->ji", t1, x50)
    del x50
    x55 += einsum("ij->ij", x54)
    del x54
    x56 = np.zeros((nocc, nvir), dtype=np.float64)
    x56 += einsum("ia,ij->ja", t1, x55)
    del x55
    x57 += einsum("ia->ia", x56)
    del x56
    x52 += einsum("ab->ab", f.vv)
    x53 = np.zeros((nocc, nvir), dtype=np.float64)
    x53 += einsum("ia,ba->ib", t1, x52)
    del x52
    x57 -= einsum("ia->ia", x53)
    del x53
    x60 += einsum("i,ja->ija", r1, x57)
    del x57
    x58 = np.zeros((nocc, nvir), dtype=np.float64)
    x58 += einsum("ij,ia->ja", f.oo, t1)
    x59 = np.zeros((nocc, nvir), dtype=np.float64)
    x59 -= einsum("ia->ia", x58)
    del x58
    x59 += einsum("ai->ia", f.vo)
    x60 += einsum("i,ja->jia", r1, x59)
    del x59
    r2new -= einsum("ija->ija", x60)
    r2new += einsum("ija->jia", x60)
    del x60
    x62 += einsum("ijkl->jilk", v.oooo)
    r2new += einsum("ija,jikl->lka", r2, x62) * 0.5
    del x62
    x63 -= einsum("i,jikl->jlk", r1, v.oooo)
    r2new += einsum("ia,ijk->kja", t1, x63)
    del x63
    r1new -= einsum("i,ij->j", r1, f.oo)
    r2new += einsum("i,iajk->kja", r1, v.ovoo)

    return r1new, r2new

def hbar_matvec_ea(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, r1=None, r2=None, **kwargs):
    r2 = -r2

    x0 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum("a,ijba->ijb", r1, v.oovv)
    x12 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum("ija,kiba->kjb", x0, t2)
    x13 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum("ija->jia", x12)
    del x12
    r1new = np.zeros((nvir), dtype=np.float64)
    r1new += einsum("ija,ijba->b", x0, t2) * 0.5
    del x0
    x1 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum("a,ib->iab", r1, t1) * 2
    x1 += einsum("abi->iab", r2) * -1
    x6 = np.zeros((nocc), dtype=np.float64)
    x6 += einsum("iab,ijba->j", x1, v.oovv) * 0.5
    x7 = np.zeros((nocc), dtype=np.float64)
    x7 += einsum("i->i", x6)
    del x6
    r1new += einsum("iab,icba->c", x1, v.ovvv) * 0.5
    del x1
    x2 = np.zeros((nocc, nvir), dtype=np.float64)
    x2 += einsum("ia,jiba->jb", t1, v.oovv)
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum("ia->ia", x2)
    x18 = np.zeros((nocc, nvir), dtype=np.float64)
    x18 += einsum("ia->ia", x2)
    del x2
    x3 += einsum("ia->ia", f.ov)
    x4 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum("abi->iab", r2)
    x4 += einsum("abi->iba", r2) * -1
    r1new += einsum("ia,iba->b", x3, x4) * -0.5
    del x3
    del x4
    x5 = np.zeros((nocc), dtype=np.float64)
    x5 += einsum("a,ia->i", r1, f.ov)
    x7 += einsum("i->i", x5)
    del x5
    r1new += einsum("i,ia->a", x7, t1) * -1
    r2new = np.zeros((nvir, nvir, nocc), dtype=np.float64)
    r2new += einsum("i,ijab->baj", x7, t2)
    del x7
    x8 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum("a,ibca->ibc", r1, v.ovvv)
    x9 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x9 -= einsum("iab,jicb->jca", x8, t2)
    x27 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x27 -= einsum("iab->iab", x9)
    del x9
    x11 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x11 -= einsum("ia,jba->ijb", t1, x8)
    del x8
    x13 += einsum("ija->jia", x11)
    del x11
    x10 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x10 += einsum("a,ibja->ijb", r1, v.ovov)
    x13 -= einsum("ija->ija", x10)
    del x10
    x14 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum("ia,ijb->jba", t1, x13)
    del x13
    x27 += einsum("iab->iba", x14)
    del x14
    x15 = np.zeros((nocc, nvir), dtype=np.float64)
    x15 += einsum("ia,ibja->jb", t1, v.ovov)
    x24 = np.zeros((nocc, nvir), dtype=np.float64)
    x24 += einsum("ia->ia", x15)
    del x15
    x16 = np.zeros((nvir, nvir), dtype=np.float64)
    x16 -= einsum("ia,ibac->bc", t1, v.ovvv)
    x17 = np.zeros((nocc, nvir), dtype=np.float64)
    x17 += einsum("ia,ba->ib", t1, x16)
    x24 += einsum("ia->ia", x17)
    del x17
    x42 = np.zeros((nvir, nvir), dtype=np.float64)
    x42 += einsum("ab->ab", x16)
    del x16
    x18 += einsum("ia->ia", f.ov)
    x19 = np.zeros((nocc, nvir), dtype=np.float64)
    x19 += einsum("ia,ijab->jb", x18, t2)
    x24 -= einsum("ia->ia", x19)
    del x19
    x21 = np.zeros((nocc, nocc), dtype=np.float64)
    x21 += einsum("ia,ja->ji", t1, x18)
    del x18
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum("ij->ij", x21)
    del x21
    x20 = np.zeros((nocc, nocc), dtype=np.float64)
    x20 -= einsum("ia,ijka->jk", t1, v.ooov)
    x22 += einsum("ij->ij", x20)
    x46 = np.zeros((nocc, nocc), dtype=np.float64)
    x46 += einsum("ij->ij", x20)
    del x20
    x22 += einsum("ij->ij", f.oo)
    x23 = np.zeros((nocc, nvir), dtype=np.float64)
    x23 += einsum("ia,ij->ja", t1, x22)
    del x22
    x24 += einsum("ia->ia", x23)
    del x23
    x27 += einsum("a,ib->iab", r1, x24)
    del x24
    x25 = np.zeros((nocc, nvir), dtype=np.float64)
    x25 += einsum("ab,ib->ia", f.vv, t1)
    x26 = np.zeros((nocc, nvir), dtype=np.float64)
    x26 += einsum("ia->ia", x25)
    del x25
    x26 += einsum("ai->ia", f.vo)
    x27 += einsum("a,ib->iba", r1, x26)
    del x26
    r2new -= einsum("iab->abi", x27)
    r2new += einsum("iab->bai", x27)
    del x27
    x28 = np.zeros((nocc, nocc, nvir), dtype=np.float64)
    x28 += einsum("abi,jcab->ijc", r2, v.ovvv)
    x29 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum("ia,jib->jab", t1, x28)
    del x28
    x54 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum("iab->iab", x29) * 0.5
    del x29
    x30 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum("abi->iab", r2) * -1
    x30 += einsum("abi->iba", r2)
    x37 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum("iab,ijbc->jac", x30, v.oovv)
    x38 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum("iab,ijbc->jac", x37, t2) * -0.5
    del x37
    x54 += einsum("iab->iab", x38) * -1
    del x38
    x48 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum("ab,icb->ica", f.vv, x30) * 0.5
    x54 += einsum("iab->iba", x48) * -1
    del x48
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum("ia,jbca->ijbc", t1, v.ovvv)
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum("ijab->ijab", x31)
    del x31
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum("ia,jkba->ijkb", t1, v.oovv)
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum("ijka->ikja", x32) * -1
    del x32
    x33 += einsum("ijka->kjia", v.ooov)
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum("ia,jikb->jkba", t1, x33)
    x35 += einsum("ijab->ijba", x34)
    del x34
    x52 = np.zeros((nocc, nvir), dtype=np.float64)
    x52 += einsum("ijab,kija->kb", t2, x33)
    del x33
    x53 = np.zeros((nocc, nvir), dtype=np.float64)
    x53 += einsum("ia->ia", x52)
    del x52
    x35 += einsum("iajb->jiab", v.ovov) * -1
    x36 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum("iab,jicb->jac", x30, x35) * 0.5
    del x35
    x54 += einsum("iab->iab", x36)
    del x36
    x39 = np.zeros((nvir, nvir), dtype=np.float64)
    x39 += einsum("ia,ib->ab", f.ov, t1)
    x42 += einsum("ab->ba", x39)
    del x39
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum("ijab->jiba", t2)
    x40 += einsum("ia,jb->ijab", t1, t1) * 2
    x41 = np.zeros((nvir, nvir), dtype=np.float64)
    x41 += einsum("ijab,ijac->cb", v.oovv, x40) * 0.5
    x42 += einsum("ab->ab", x41)
    del x41
    x43 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum("ab,icb->ica", x42, x30) * 0.5
    del x42
    del x30
    x54 += einsum("iab->iab", x43) * -1
    del x43
    x45 = np.zeros((nocc, nocc), dtype=np.float64)
    x45 += einsum("ijab,ikab->kj", v.oovv, x40) * 0.5
    x46 += einsum("ij->ji", x45)
    del x45
    x44 = np.zeros((nocc, nocc), dtype=np.float64)
    x44 += einsum("ia,ja->ij", f.ov, t1)
    x46 += einsum("ij->ij", x44)
    del x44
    x46 += einsum("ij->ij", f.oo)
    x47 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum("ij,abi->jab", x46, r2) * 0.5
    del x46
    x54 += einsum("iab->iab", x47)
    del x47
    x49 = np.zeros((nocc, nvir), dtype=np.float64)
    x49 += einsum("ijab,jcab->ic", t2, v.ovvv)
    x53 += einsum("ia->ia", x49)
    del x49
    x50 = np.zeros((nocc, nocc), dtype=np.float64)
    x50 -= einsum("ijab,jkab->ik", t2, v.oovv)
    x51 = np.zeros((nocc, nvir), dtype=np.float64)
    x51 += einsum("ia,ji->ja", t1, x50)
    del x50
    x53 += einsum("ia->ia", x51)
    del x51
    x54 += einsum("a,ib->iab", r1, x53) * -0.5
    del x53
    r2new += einsum("iab->abi", x54)
    r2new += einsum("iab->bai", x54) * -1
    del x54
    x55 = np.zeros((nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum("abi->iab", r2)
    x55 += einsum("a,ib->iba", r1, t1) * 2
    x56 = np.zeros((nocc, nocc, nocc), dtype=np.float64)
    x56 += einsum("iab,jkab->kji", x55, v.oovv) * -0.5
    r2new += einsum("iab,cdab->dci", x55, v.vvvv) * 0.5
    del x55
    x56 += einsum("a,ijka->jik", r1, v.ooov) * -1
    r2new += einsum("ijk,ijab->bak", x56, x40) * 0.5
    del x40
    del x56
    r1new += einsum("a,ba->b", r1, f.vv)
    r2new += einsum("a,bcia->cbi", r1, v.vvov)

    return r1new, r2new

def make_ee_mom_kets(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta_oo = np.eye(nocc)
    delta_vv = np.eye(nvir)

    ketee1_oo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    ketee1_oo -= einsum("ij,ka->jaki", delta_oo, t1)
    ketee1_ov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    ketee1_ov -= einsum("ia,jb->iajb", t1, t1)
    ketee1_ov += einsum("ijab->jbia", t2)
    ketee1_vo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    ketee1_vo += einsum("ab,ij->jbai", delta_vv, delta_oo)
    ketee1_vv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    ketee1_vv += einsum("ab,ic->ibac", delta_vv, t1)
    ketee2_oo = np.zeros((nocc, nocc, nvir, nvir, nocc, nocc), dtype=np.float64)
    ketee2_oo += einsum("ij,klab->jlbaki", delta_oo, t2)
    ketee2_oo -= einsum("ij,klab->ljbaki", delta_oo, t2)
    ketee2_ov = np.zeros((nocc, nocc, nvir, nvir, nocc, nvir), dtype=np.float64)
    ketee2_ov += einsum("ia,jkbc->ikcbja", t1, t2)
    ketee2_ov -= einsum("ia,jkbc->kicbja", t1, t2)
    ketee2_ov += einsum("ia,jkbc->kjacib", t1, t2)
    ketee2_ov -= einsum("ia,jkbc->kjcaib", t1, t2)
    ketee2_vv = np.zeros((nocc, nocc, nvir, nvir, nvir, nvir), dtype=np.float64)
    ketee2_vv -= einsum("ab,ijcd->jibdac", delta_vv, t2)
    ketee2_vv += einsum("ab,ijcd->jidbac", delta_vv, t2)

    ketee2_vo = np.zeros((nocc, nocc, nvir, nvir, nvir, nocc), dtype=np.float64)

    ketee1 = np.concatenate([np.concatenate([ketee1_oo, ketee1_ov], axis=-1), np.concatenate([ketee1_vo, ketee1_vv], axis=-1)], axis=-2)
    ketee2 = np.concatenate([np.concatenate([ketee2_oo, ketee2_ov], axis=-1), np.concatenate([ketee2_vo, ketee2_vv], axis=-1)], axis=-2)

    return ketee1, ketee2

def make_ee_mom_bras(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    delta_oo = np.eye(nocc)
    delta_vv = np.eye(nvir)

    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum("ia,bajk->jkib", t1, l2)
    x5 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x5 -= einsum("ijka->jika", x0)
    braee1_oo = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    braee1_oo -= einsum("ijka->kjia", x0)
    del x0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum("ijab->jiba", t2)
    x1 -= einsum("ia,jb->ijba", t1, t1)
    braee1_ov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    braee1_ov += einsum("abij,ikac->kcjb", l2, x1)
    del x1
    x2 = np.zeros((nvir, nvir), dtype=np.float64)
    x2 += einsum("ab->ba", delta_vv) * -2
    x2 += einsum("ai,ib->ab", l1, t1) * 2
    x2 += einsum("abij,ijcb->ac", l2, t2)
    braee1_ov += einsum("ij,ab->jbia", delta_oo, x2) * -0.5
    del x2
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum("ai,ja->ij", l1, t1) * 2
    x3 += einsum("abij,kjab->ik", l2, t2)
    braee1_ov += einsum("ab,ij->jbia", delta_vv, x3) * -0.5
    del x3
    x4 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x4 += einsum("ia,bcji->jbca", t1, l2)
    braee1_vv = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    braee1_vv += einsum("iabc->bcia", x4)
    braee2_ov = np.zeros((nocc, nvir, nocc, nocc, nvir, nvir), dtype=np.float64)
    braee2_ov -= einsum("ij,kabc->icjkba", delta_oo, x4)
    braee2_ov += einsum("ij,kabc->ickjba", delta_oo, x4)
    del x4
    x5 += einsum("ij,ak->jkia", delta_oo, l1)
    x5 -= einsum("ij,ak->kjia", delta_oo, l1)
    braee2_ov -= einsum("ab,ijkc->kbjiac", delta_vv, x5)
    braee2_ov += einsum("ab,ijkc->kbjica", delta_vv, x5)
    del x5
    braee1_oo += einsum("ij,ak->jika", delta_oo, l1)
    braee1_oo -= einsum("ij,ak->jkia", delta_oo, l1)
    braee1_ov += einsum("ai,jb->jbia", l1, t1)
    braee1_vo = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    braee1_vo += einsum("abij->bjia", l2)
    braee1_vv += einsum("ab,ci->cbia", delta_vv, l1)
    braee2_oo = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    braee2_oo += einsum("ij,abkl->jilkba", delta_oo, l2)
    braee2_oo -= einsum("ij,abkl->jlikba", delta_oo, l2)
    braee2_oo += einsum("ij,abkl->jlkiba", delta_oo, l2)
    braee2_ov += einsum("ia,bcjk->iakjcb", t1, l2)
    braee2_vv = np.zeros((nvir, nvir, nocc, nocc, nvir, nvir), dtype=np.float64)
    braee2_vv += einsum("ab,cdij->dbjiac", delta_vv, l2)
    braee2_vv -= einsum("ab,cdij->dbjica", delta_vv, l2)

    braee2_vo = np.zeros((nvir, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)

    braee1 = np.concatenate([np.concatenate([braee1_oo, braee1_ov], axis=1), np.concatenate([braee1_vo, braee1_vv], axis=1)], axis=0)
    braee2 = np.concatenate([np.concatenate([braee2_oo, braee2_ov], axis=1), np.concatenate([braee2_vo, braee2_vv], axis=1)], axis=0)

    return braee1, braee2

def hbar_matvec_ee(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, r1=None, r2=None, **kwargs):
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum("ijab->ijab", r2)
    x0 += einsum("ijab->jiab", r2) * -1
    x105 = np.zeros((nocc, nocc), dtype=np.float64)
    x105 += einsum("ijab,ikab->jk", v.oovv, x0)
    x106 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x106 += einsum("ij,ikab->kjab", x105, t2) * 0.25
    del x105
    x107 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum("ijab->jiba", x106)
    del x106
    ree1new = np.zeros((nocc, nvir), dtype=np.float64)
    ree1new += einsum("iabc,ijbc->ja", v.ovvv, x0) * 0.25
    del x0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum("ijab->ijab", r2) * -1
    x1 += einsum("ijab->ijba", r2)
    x87 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x87 += einsum("ab,ijcb->ijac", f.vv, x1) * 0.25
    x94 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x94 += einsum("ijab->ijab", x87) * -1
    del x87
    ree1new += einsum("ijka,jiba->kb", v.ooov, x1) * -0.25
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum("ijab->ijab", r2)
    x2 += einsum("ijab->ijba", r2) * -1
    x2 += einsum("ijab->jiab", r2) * -1
    x2 += einsum("ijab->jiba", r2)
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum("ijab,kiac->jkbc", v.oovv, x2)
    x78 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x78 += einsum("ia,jkab->ikjb", t1, x3) * -1
    x79 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x79 += einsum("ijka->kjia", x78)
    del x78
    ree1new += einsum("ia,ijab->jb", t1, x3) * -0.25
    del x3
    x83 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x83 += einsum("iabc,jibd->jacd", v.ovvv, x2)
    x84 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x84 += einsum("ia,jbac->ijcb", t1, x83) * 0.25
    del x83
    x94 += einsum("ijab->jiab", x84)
    del x84
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum("ijab->ijab", r2) * -1
    x4 += einsum("ijab->ijba", r2)
    x4 += einsum("ijab->jiab", r2)
    x4 += einsum("ijab->jiba", r2) * -1
    x76 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x76 += einsum("ijka,ilba->jklb", v.ooov, x4)
    x79 += einsum("ijka->ikja", x76) * -1
    del x76
    ree1new += einsum("ia,ijba->jb", f.ov, x4) * 0.25
    del x4
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum("ijab,jkbc->ikac", t2, v.oovv)
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 -= einsum("ijab->jiab", x5)
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum("ijab->ijab", x5)
    x48 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum("ijab->ijab", x5)
    x74 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x74 += einsum("ijab->ijab", x5)
    del x5
    x6 += einsum("iajb->ijab", v.ovov)
    x55 = np.zeros((nocc, nvir), dtype=np.float64)
    x55 += einsum("ia,ijba->jb", t1, x6)
    x56 = np.zeros((nocc, nvir), dtype=np.float64)
    x56 += einsum("ia->ia", x55)
    del x55
    ree1new -= einsum("ia,ijba->jb", r1, x6)
    del x6
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 -= einsum("ia,ijka->jk", r1, v.ooov)
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum("ij->ij", x7)
    x58 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x58 -= einsum("ij,kiab->kjab", x7, t2)
    del x7
    x69 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x69 -= einsum("ijab->ijba", x58)
    del x58
    x8 = np.zeros((nocc, nvir), dtype=np.float64)
    x8 += einsum("ia,ijab->jb", r1, v.oovv)
    x9 = np.zeros((nocc, nocc), dtype=np.float64)
    x9 -= einsum("ia,ja->ij", t1, x8)
    x13 += einsum("ij->ji", x9) * -1
    x63 = np.zeros((nocc, nocc), dtype=np.float64)
    x63 -= einsum("ij->ij", x9)
    del x9
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 -= einsum("ia,jkba->jkib", x8, t2)
    del x8
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 -= einsum("ia,jkib->jkab", t1, x26)
    del x26
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum("ijab->ijab", x27)
    del x27
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum("ijab->ijab", r2) * -1
    x10 += einsum("ijab->jiab", r2)
    x13 += einsum("ijab,kiab->jk", v.oovv, x10) * 0.25
    x88 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x88 += einsum("ij,ikab->jkab", f.oo, x10) * 0.25
    x94 += einsum("ijab->ijab", x88) * -1
    del x88
    x11 = np.zeros((nocc, nvir), dtype=np.float64)
    x11 += einsum("ia,ijab->jb", t1, v.oovv)
    x12 = np.zeros((nocc, nvir), dtype=np.float64)
    x12 += einsum("ia->ia", x11)
    x30 = np.zeros((nocc, nvir), dtype=np.float64)
    x30 += einsum("ia->ia", x11)
    x53 = np.zeros((nocc, nocc), dtype=np.float64)
    x53 += einsum("ia,ja->ij", t1, x11)
    del x11
    x54 = np.zeros((nocc, nvir), dtype=np.float64)
    x54 += einsum("ia,ji->ja", t1, x53)
    del x53
    x56 += einsum("ia->ia", x54)
    del x54
    x12 += einsum("ia->ia", f.ov)
    x13 += einsum("ia,ja->ji", r1, x12)
    ree1new += einsum("ia,ij->ja", t1, x13) * -1
    del x13
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum("ia,ja->ij", t1, x12)
    x23 = np.zeros((nocc, nocc), dtype=np.float64)
    x23 += einsum("ij->ji", x22)
    x85 = np.zeros((nocc, nocc), dtype=np.float64)
    x85 += einsum("ij->ji", x22)
    del x22
    x77 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x77 += einsum("ia,jkba->jkib", x12, x1)
    del x1
    del x12
    x79 += einsum("ijka->kija", x77) * -1
    del x77
    x80 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x80 += einsum("ia,ijkb->jkab", t1, x79) * 0.25
    del x79
    x94 += einsum("ijab->ijba", x80)
    del x80
    x14 = np.zeros((nvir, nvir), dtype=np.float64)
    x14 -= einsum("ia,ibac->bc", r1, v.ovvv)
    x16 = np.zeros((nvir, nvir), dtype=np.float64)
    x16 += einsum("ab->ab", x14)
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 -= einsum("ab,ijcb->ijca", x14, t2)
    del x14
    x38 += einsum("ijab->ijab", x25)
    del x25
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum("ijab->ijab", r2)
    x15 += einsum("ijab->ijba", r2) * -1
    x16 += einsum("ijab,jiac->cb", v.oovv, x15) * -0.25
    ree1new += einsum("ia,ba->ib", t1, x16) * -1
    del x16
    x114 = np.zeros((nvir, nvir), dtype=np.float64)
    x114 += einsum("ijab,jiac->bc", v.oovv, x15)
    x115 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x115 += einsum("ab,ijac->ijcb", x114, t2) * -0.25
    del x114
    x120 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x120 += einsum("ijab->jiba", x115)
    del x115
    x17 = np.zeros((nvir, nvir), dtype=np.float64)
    x17 -= einsum("ia,ibac->bc", t1, v.ovvv)
    x19 = np.zeros((nvir, nvir), dtype=np.float64)
    x19 += einsum("ab->ab", x17)
    x52 = np.zeros((nocc, nvir), dtype=np.float64)
    x52 += einsum("ia,ba->ib", t1, x17)
    x56 += einsum("ia->ia", x52)
    del x52
    x81 = np.zeros((nvir, nvir), dtype=np.float64)
    x81 += einsum("ab->ab", x17)
    del x17
    x18 = np.zeros((nvir, nvir), dtype=np.float64)
    x18 -= einsum("ijab,ijbc->ac", t2, v.oovv)
    x19 += einsum("ab->ab", x18) * 0.5
    x81 += einsum("ab->ab", x18) * 0.5
    x82 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum("ab,ijbc->ijca", x81, x15) * 0.25
    del x81
    del x15
    x94 += einsum("ijab->ijab", x82) * -1
    del x82
    x91 = np.zeros((nocc, nvir), dtype=np.float64)
    x91 += einsum("ia,ba->ib", t1, x18)
    del x18
    x93 = np.zeros((nocc, nvir), dtype=np.float64)
    x93 += einsum("ia->ia", x91)
    del x91
    x19 += einsum("ab->ab", f.vv) * -1
    ree1new += einsum("ia,ba->ib", r1, x19) * -1
    del x19
    x20 = np.zeros((nocc, nocc), dtype=np.float64)
    x20 -= einsum("ia,ijka->jk", t1, v.ooov)
    x23 += einsum("ij->ij", x20)
    x85 += einsum("ij->ij", x20)
    x123 = np.zeros((nocc, nocc), dtype=np.float64)
    x123 += einsum("ij->ij", x20)
    del x20
    x21 = np.zeros((nocc, nocc), dtype=np.float64)
    x21 -= einsum("ijab,jkab->ik", t2, v.oovv)
    x23 += einsum("ij->ji", x21) * 0.5
    x85 += einsum("ij->ji", x21) * 0.5
    x86 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum("ij,kiab->kjab", x85, x10) * 0.25
    del x10
    del x85
    x94 += einsum("ijab->ijab", x86) * -1
    del x86
    x92 = np.zeros((nocc, nvir), dtype=np.float64)
    x92 += einsum("ia,ji->ja", t1, x21)
    del x21
    x93 += einsum("ia->ia", x92)
    del x92
    x23 += einsum("ij->ij", f.oo)
    ree1new += einsum("ia,ij->ja", r1, x23) * -1
    del x23
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 -= einsum("ijab,jikl->klab", r2, v.oooo)
    ree2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    ree2new += einsum("ijab->jiab", x24) * -0.25
    ree2new += einsum("ijab->jiba", x24) * 0.25
    del x24
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 -= einsum("ia,jbac->ijbc", t1, v.ovvv)
    x29 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x29 -= einsum("ia,jkba->jikb", t1, x28)
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum("ijka->kjia", x29)
    del x29
    x48 += einsum("ijab->ijab", x28)
    del x28
    x30 += einsum("ia->ia", f.ov)
    x31 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x31 += einsum("ia,jkab->jkib", x30, t2)
    x36 += einsum("ijka->kjia", x31)
    del x31
    x62 = np.zeros((nocc, nocc), dtype=np.float64)
    x62 += einsum("ia,ja->ij", r1, x30)
    del x30
    x63 += einsum("ij->ij", x62)
    del x62
    x64 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x64 += einsum("ij,jkab->kiab", x63, t2)
    del x63
    x69 += einsum("ijab->jiba", x64)
    del x64
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 -= einsum("ia,jkab->ijkb", t1, v.oovv)
    x33 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x33 += einsum("ia,jkla->jilk", t1, x32)
    x34 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x34 -= einsum("ijkl->klji", x33)
    del x33
    x65 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x65 += einsum("ijka->kjia", x32)
    del x32
    x34 += einsum("ijkl->jilk", v.oooo)
    x35 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x35 += einsum("ia,ijkl->jkla", t1, x34)
    del x34
    x36 += einsum("ijka->ikja", x35)
    del x35
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum("ia,ijkb->jkab", r1, x36)
    del x36
    x38 -= einsum("ijab->jiab", x37)
    del x37
    ree2new += einsum("ijab->ijab", x38)
    ree2new -= einsum("ijab->ijba", x38)
    del x38
    x39 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x39 -= einsum("ijab,jcbd->iacd", t2, v.ovvv)
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum("ia,jbca->ijbc", r1, x39)
    del x39
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 -= einsum("ijab->ijab", x40)
    del x40
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 -= einsum("ijab,jklb->ikla", t2, v.ooov)
    x46 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x46 += einsum("ijka->ijka", x41)
    del x41
    x42 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x42 += einsum("ia,jkla->ijkl", t1, v.ooov)
    x43 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x43 -= einsum("ia,jikl->jkla", t1, x42)
    del x42
    x46 -= einsum("ijka->ijka", x43)
    del x43
    x44 -= einsum("iajb->jiab", v.ovov)
    x45 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x45 += einsum("ia,jkba->ijkb", t1, x44)
    del x44
    x46 -= einsum("ijka->ikja", x45)
    del x45
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum("ia,jikb->jkab", r1, x46)
    del x46
    x57 -= einsum("ijab->ijab", x47)
    del x47
    x48 -= einsum("iajb->jiab", v.ovov)
    x49 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x49 += einsum("ia,jkba->ijkb", r1, x48)
    del x48
    x50 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x50 += einsum("ia,jkib->jkab", t1, x49)
    del x49
    x57 += einsum("ijab->ijab", x50)
    del x50
    x51 = np.zeros((nocc, nvir), dtype=np.float64)
    x51 += einsum("ia,jiba->jb", f.ov, t2)
    x56 -= einsum("ia->ia", x51)
    del x51
    x57 += einsum("ia,jb->ijab", r1, x56)
    del x56
    ree2new -= einsum("ijab->ijab", x57)
    ree2new += einsum("ijab->ijba", x57)
    ree2new += einsum("ijab->jiab", x57)
    ree2new -= einsum("ijab->jiba", x57)
    del x57
    x59 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x59 -= einsum("ia,bcad->ibcd", t1, v.vvvv)
    x60 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x60 += einsum("iabc->ibac", x59)
    del x59
    x60 -= einsum("abic->ibac", v.vvov)
    x61 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x61 += einsum("ia,jbca->ijbc", r1, x60)
    del x60
    x69 += einsum("ijab->ijba", x61)
    del x61
    x65 -= einsum("ijka->jika", v.ooov)
    x66 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x66 += einsum("ia,jkla->ijkl", r1, x65)
    del x65
    x67 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x67 -= einsum("ia,jkil->jkla", t1, x66)
    del x66
    x68 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x68 -= einsum("ia,jikb->jkab", t1, x67)
    del x67
    x69 -= einsum("ijab->ijab", x68)
    del x68
    ree2new += einsum("ijab->ijab", x69)
    ree2new -= einsum("ijab->jiab", x69)
    del x69
    x70 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x70 -= einsum("ijab,jikc->kabc", r2, v.ooov)
    x71 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x71 += einsum("ia,jbca->ijbc", t1, x70)
    del x70
    x94 += einsum("ijab->ijab", x71) * 0.25
    del x71
    x72 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x72 += einsum("ijab,kcab->ijkc", r2, v.ovvv)
    x73 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x73 += einsum("ia,jkib->jkab", t1, x72)
    del x72
    x94 += einsum("ijab->ijab", x73) * 0.25
    del x73
    x74 += einsum("iajb->jiab", v.ovov) * -1
    x75 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x75 += einsum("ijab,kjca->ikbc", x2, x74) * 0.25
    del x2
    del x74
    x94 += einsum("ijab->ijab", x75)
    del x75
    x89 = np.zeros((nocc, nvir), dtype=np.float64)
    x89 += einsum("ijab,ijkb->ka", t2, v.ooov)
    x93 += einsum("ia->ia", x89)
    del x89
    x90 = np.zeros((nocc, nvir), dtype=np.float64)
    x90 += einsum("ijab,jcab->ic", t2, v.ovvv)
    x93 += einsum("ia->ia", x90)
    del x90
    x94 += einsum("ia,jb->ijab", r1, x93) * 0.5
    del x93
    ree2new += einsum("ijab->ijab", x94) * -1
    ree2new += einsum("ijab->ijba", x94)
    ree2new += einsum("ijab->jiab", x94)
    ree2new += einsum("ijab->jiba", x94) * -1
    del x94
    x95 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x95 += einsum("ijab,cdab->ijcd", r2, v.vvvv)
    x107 += einsum("ijab->ijba", x95) * -0.25
    del x95
    x96 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x96 += einsum("ijab,klab->ijkl", r2, v.oovv)
    x97 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum("ijab,klij->klab", t2, x96)
    x107 += einsum("ijab->ijba", x97) * -0.125
    del x97
    x98 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x98 -= einsum("ia,jkil->jkla", t1, x96)
    del x96
    x99 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 -= einsum("ia,jkib->jkba", t1, x98)
    del x98
    x107 += einsum("ijab->ijba", x99) * -0.25
    del x99
    x100 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x100 += einsum("ijab,ijkc->kabc", t2, v.ooov)
    x103 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x103 += einsum("iabc->ibac", x100) * -1
    del x100
    x101 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x101 += einsum("ijab,ijcd->abcd", t2, v.oovv)
    x102 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x102 -= einsum("ia,bcad->ibcd", t1, x101)
    del x101
    x103 += einsum("iabc->ibac", x102)
    del x102
    x104 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x104 += einsum("ia,jbca->ijbc", r1, x103) * 0.5
    del x103
    x107 += einsum("ijab->ijba", x104)
    del x104
    ree2new += einsum("ijab->ijab", x107)
    ree2new += einsum("ijab->jiab", x107) * -1
    del x107
    x108 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x108 += einsum("ia,ibjk->jkab", r1, v.ovoo)
    ree2new += einsum("ijab->jiab", x108)
    ree2new -= einsum("ijab->jiba", x108)
    del x108
    x109 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x109 += einsum("ijab,klab->ijkl", t2, v.oovv)
    x110 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum("ijab,klji->lkab", r2, x109)
    x120 += einsum("ijab->ijab", x110) * 0.125
    del x110
    x117 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x117 -= einsum("ia,jkil->jkla", t1, x109)
    del x109
    x118 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x118 += einsum("ijka->ijka", x117) * -1
    del x117
    x111 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x111 -= einsum("ijab,jicd->abcd", r2, v.oovv)
    x112 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x112 -= einsum("ia,bcad->ibcd", t1, x111)
    del x111
    x113 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x113 += einsum("ia,jbca->ijbc", t1, x112)
    del x112
    x120 += einsum("ijab->ijab", x113) * 0.25
    del x113
    x116 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x116 += einsum("ijab,kcab->ijkc", t2, v.ovvv)
    x118 += einsum("ijka->jika", x116) * -1
    del x116
    x119 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x119 += einsum("ia,jkib->jkab", r1, x118) * 0.5
    del x118
    x120 += einsum("ijab->jiab", x119)
    del x119
    ree2new += einsum("ijab->ijab", x120)
    ree2new += einsum("ijab->ijba", x120) * -1
    del x120
    x121 = np.zeros((nocc, nvir), dtype=np.float64)
    x121 += einsum("ab,ib->ia", f.vv, t1)
    x125 = np.zeros((nocc, nvir), dtype=np.float64)
    x125 -= einsum("ia->ia", x121)
    del x121
    x122 = np.zeros((nocc, nocc), dtype=np.float64)
    x122 += einsum("ia,ja->ij", f.ov, t1)
    x123 += einsum("ij->ij", x122)
    del x122
    x123 += einsum("ij->ij", f.oo)
    x124 = np.zeros((nocc, nvir), dtype=np.float64)
    x124 += einsum("ia,ij->ja", t1, x123)
    del x123
    x125 += einsum("ia->ia", x124)
    del x124
    x125 -= einsum("ai->ia", f.vo)
    ree2new -= einsum("ia,jb->ijab", r1, x125)
    ree2new -= einsum("ia,jb->jiba", r1, x125)
    ree2new += einsum("ia,jb->ijba", r1, x125)
    ree2new += einsum("ia,jb->jiab", r1, x125)
    del x125

    return ree1new, ree2new
