# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t1, (0, 1), f.ov, (0, 1), ()) * 2.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x1 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    e_cc += einsum(x0, (0, 1, 2, 3), x1, (0, 1, 2, 3), ()) * 2.0

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(f.vv, (0, 1), t1, (2, 1), (2, 0))
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 0, 5, 1), (2, 4, 3, 5))
    t2new += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    t2new += einsum(v.ooov, (0, 1, 2, 3), t1, (1, 4), (2, 0, 3, 4)) * -1.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x1 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t1new += einsum(x0, (0, 1, 2, 3), x1, (4, 0, 1, 3, 5, 2), (4, 5)) * 0.25
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x2 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.3333333333333333
    t1new += einsum(x2, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 2), (4, 5)) * 1.5
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x3 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    x4 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x4 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x4 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2))
    t1new += einsum(x4, (0, 1, 2, 3), x3, (4, 0, 1, 2), (4, 3)) * 2.0
    x5 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x5 += einsum(v.ovov, (0, 1, 2, 3), t1, (4, 3), (4, 0, 2, 1))
    x6 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x6 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x6 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x6 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    x6 += einsum(x5, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    t1new += einsum(t2, (0, 1, 2, 3), x6, (4, 1, 0, 3), (4, 2)) * -1.5
    x7 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x7 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x7 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x7 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x7 += einsum(x5, (0, 1, 2, 3), (0, 2, 1, 3))
    t1new += einsum(t2, (0, 1, 2, 3), x7, (4, 1, 0, 2), (4, 3)) * -0.5
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x8 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x9 = np.zeros((nocc, nvir), dtype=np.float64)
    x9 += einsum(x8, (0, 1, 2, 3), t1, (0, 2), (1, 3)) * 2.0
    x10 = np.zeros((nocc, nvir), dtype=np.float64)
    x10 += einsum(f.ov, (0, 1), (0, 1))
    x10 += einsum(x9, (0, 1), (0, 1))
    x11 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x11 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x11 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t1new += einsum(x11, (0, 1, 2, 3), x10, (1, 3), (0, 2))
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x12 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    t1new += einsum(t1, (0, 1), x12, (0, 2, 1, 3), (2, 3)) * 2.0
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum(t1, (0, 1), f.ov, (2, 1), (2, 0))
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x14 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x15 = np.zeros((nocc, nocc), dtype=np.float64)
    x15 += einsum(x3, (0, 1, 2, 3), x14, (1, 4, 2, 3), (0, 4)) * 2.0
    x16 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x16 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    x17 = np.zeros((nocc, nocc), dtype=np.float64)
    x17 += einsum(x16, (0, 1, 2, 3), t1, (2, 3), (0, 1)) * 2.0
    x18 = np.zeros((nocc, nocc), dtype=np.float64)
    x18 += einsum(f.oo, (0, 1), (1, 0))
    x18 += einsum(x13, (0, 1), (0, 1))
    x18 += einsum(x15, (0, 1), (1, 0))
    x18 += einsum(x17, (0, 1), (1, 0))
    t1new += einsum(x18, (0, 1), t1, (0, 2), (1, 2)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x18, (0, 4), (4, 1, 2, 3)) * -1.0
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(t2, (0, 1, 2, 3), v.ovov, (1, 2, 4, 5), (0, 4, 3, 5))
    t2new += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x20 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x20 += einsum(v.vvvv, (0, 1, 2, 3), t1, (4, 1), (4, 2, 3, 0))
    t2new += einsum(x20, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(t2, (0, 1, 2, 3), x21, (4, 1, 2, 5), (4, 0, 3, 5))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(x5, (0, 1, 2, 3), t3, (4, 2, 1, 5, 6, 3), (0, 4, 5, 6))
    x24 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x24 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2))
    x24 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(t3, (0, 1, 2, 3, 4, 5), x24, (2, 5, 3, 6), (0, 1, 4, 6)) * 0.5
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x26 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(t3, (0, 1, 2, 3, 4, 5), x26, (0, 6, 2, 5), (1, 6, 3, 4)) * 0.5
    x28 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x28 += einsum(v.oovv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x29 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x29 += einsum(t3, (0, 1, 2, 3, 4, 5), v.ovov, (2, 5, 6, 4), (0, 1, 6, 3))
    x30 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x30 += einsum(v.ooov, (0, 1, 2, 3), x3, (4, 2, 3, 5), (0, 1, 4, 5))
    x31 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x31 += einsum(x28, (0, 1, 2, 3), (0, 2, 1, 3))
    x31 += einsum(x29, (0, 1, 2, 3), (0, 2, 1, 3))
    x31 += einsum(x30, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(t1, (0, 1), x31, (2, 0, 3, 4), (2, 3, 1, 4))
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x33 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3))
    x33 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x33 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x33 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x33 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x33, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x33, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(t3, (0, 1, 2, 3, 4, 5), v.ooov, (6, 1, 2, 5), (0, 6, 3, 4))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 0, 6, 3, 1), (4, 5, 6, 2))
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x36 += einsum(x5, (0, 1, 2, 3), (0, 2, 1, 3))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(t3, (0, 1, 2, 3, 4, 5), x36, (6, 0, 2, 5), (1, 6, 3, 4)) * 0.5
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(t3, (0, 1, 2, 3, 4, 5), x10, (2, 5), (0, 1, 3, 4))
    x39 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x39 += einsum(t2, (0, 1, 2, 3), x5, (4, 1, 5, 2), (4, 0, 5, 3))
    x40 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x40 += einsum(t3, (0, 1, 2, 3, 4, 5), x0, (2, 6, 3, 5), (0, 1, 6, 4)) * 0.5
    x41 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x41 += einsum(x21, (0, 1, 2, 3), (1, 0, 2, 3))
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(x41, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x43 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x43 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x43 += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x43 += einsum(x42, (0, 1, 2, 3), (0, 2, 1, 3))
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(t1, (0, 1), x43, (2, 3, 0, 4), (2, 3, 1, 4))
    x45 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x45 += einsum(x34, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x45 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3))
    x45 += einsum(x37, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x45 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x45 += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x45, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x45, (0, 1, 2, 3), (1, 0, 3, 2))
    x46 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x46 += einsum(x21, (0, 1, 2, 3), t2, (4, 1, 5, 2), (0, 4, 5, 3))
    t2new += einsum(x46, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x46, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x47 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x47 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 2, 5, 3), (4, 0, 1, 5))
    x48 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum(t1, (0, 1), x47, (2, 3, 0, 4), (2, 3, 1, 4))
    t2new += einsum(x48, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    t2new += einsum(x48, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x49 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x49 += einsum(t2, (0, 1, 2, 3), x19, (4, 1, 5, 3), (0, 4, 2, 5))
    t2new += einsum(x49, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    t2new += einsum(x49, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x50 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x50 += einsum(t2, (0, 1, 2, 3), x5, (4, 1, 5, 3), (4, 0, 5, 2))
    x51 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x51 += einsum(t1, (0, 1), x50, (2, 3, 0, 4), (2, 3, 1, 4))
    t2new += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x51, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x53 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x54 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x54 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x55 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum(v.ovov, (0, 1, 2, 3), x3, (4, 0, 3, 5), (4, 2, 5, 1))
    x56 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x56 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * 2.0
    x56 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x56 += einsum(x52, (0, 1, 2, 3), (1, 0, 2, 3))
    x56 += einsum(x53, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x56 += einsum(x8, (0, 1, 2, 3), x54, (0, 4, 2, 5), (4, 1, 5, 3)) * 2.0
    x56 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(t2, (0, 1, 2, 3), x56, (4, 1, 5, 3), (0, 4, 2, 5))
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x57 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x58 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x58 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x58 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x58 += einsum(x3, (0, 1, 2, 3), x57, (1, 4, 2, 5), (0, 4, 3, 5)) * -1.0
    x58 += einsum(t1, (0, 1), x24, (2, 3, 1, 4), (0, 2, 4, 3)) * -1.0
    x58 += einsum(t1, (0, 1), x26, (0, 2, 3, 4), (2, 3, 1, 4)) * -1.0
    t2new += einsum(x58, (0, 1, 2, 3), t2, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x59 += einsum(x52, (0, 1, 2, 3), (1, 0, 2, 3))
    x59 += einsum(x53, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x59, (0, 1, 2, 3), t2, (1, 4, 5, 3), (0, 4, 5, 2))
    x60 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x60 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x60 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    x61 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x61 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x61 += einsum(x53, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x61 += einsum(t1, (0, 1), x60, (2, 0, 3, 4), (2, 3, 1, 4))
    t2new += einsum(x61, (0, 1, 2, 3), t2, (4, 1, 3, 5), (4, 0, 2, 5))
    x62 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x62 += einsum(t1, (0, 1), v.ovvv, (0, 2, 3, 4), (1, 2, 3, 4))
    x63 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x63 += einsum(v.vvvv, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x63 += einsum(x62, (0, 1, 2, 3), (1, 0, 3, 2))
    x63 += einsum(x62, (0, 1, 2, 3), (3, 2, 0, 1))
    t2new += einsum(t2, (0, 1, 2, 3), x63, (3, 4, 5, 2), (0, 1, 5, 4)) * -1.0
    x64 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x64 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 5, 2), (0, 1, 5, 4))
    x65 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x65 += einsum(x5, (0, 1, 2, 3), t1, (4, 3), (0, 4, 2, 1))
    x66 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x66 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x67 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x67 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x67 += einsum(x64, (0, 1, 2, 3), (3, 1, 0, 2))
    x67 += einsum(x65, (0, 1, 2, 3), (3, 1, 0, 2))
    x67 += einsum(x66, (0, 1, 2, 3), (3, 0, 2, 1))
    x67 += einsum(x66, (0, 1, 2, 3), (2, 1, 0, 3))
    t2new += einsum(t2, (0, 1, 2, 3), x67, (1, 4, 5, 0), (5, 4, 2, 3))
    x68 = np.zeros((nvir, nvir), dtype=np.float64)
    x68 += einsum(f.ov, (0, 1), t1, (0, 2), (1, 2))
    x69 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x69 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    x69 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x69 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x70 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x70 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 4.0
    x70 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x70 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x71 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x71 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x71 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x72 = np.zeros((nvir, nvir), dtype=np.float64)
    x72 += einsum(x71, (0, 1, 2, 3), t1, (0, 1), (2, 3)) * 0.5
    x73 = np.zeros((nvir, nvir), dtype=np.float64)
    x73 += einsum(f.vv, (0, 1), (1, 0)) * -0.5
    x73 += einsum(x68, (0, 1), (0, 1)) * 0.5
    x73 += einsum(x69, (0, 1, 2, 3), v.ovov, (0, 4, 1, 2), (4, 3)) * -0.25
    x73 += einsum(x70, (0, 1, 2, 3), v.ovov, (0, 2, 1, 4), (4, 3)) * 0.25
    x73 += einsum(x72, (0, 1), (1, 0)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x73, (3, 4), (0, 1, 2, 4)) * -2.0
    x74 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x74 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 0.6666666666666666
    x74 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x74 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x75 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x75 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 4.0
    x75 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x75 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x76 = np.zeros((nvir, nvir), dtype=np.float64)
    x76 += einsum(f.vv, (0, 1), (1, 0)) * -0.5
    x76 += einsum(x68, (0, 1), (0, 1)) * 0.5
    x76 += einsum(x74, (0, 1, 2, 3), v.ovov, (0, 4, 1, 2), (4, 3)) * -0.75
    x76 += einsum(x75, (0, 1, 2, 3), v.ovov, (0, 2, 1, 4), (4, 3)) * 0.25
    x76 += einsum(x72, (0, 1), (1, 0)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x76, (2, 4), (0, 1, 4, 3)) * -2.0
    x77 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x77 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    x77 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x77 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x78 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x78 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    x79 = np.zeros((nocc, nocc), dtype=np.float64)
    x79 += einsum(f.oo, (0, 1), (1, 0))
    x79 += einsum(x13, (0, 1), (0, 1))
    x79 += einsum(v.ovov, (0, 1, 2, 3), x77, (0, 4, 3, 1), (2, 4)) * -1.0
    x79 += einsum(x17, (0, 1), (1, 0))
    x79 += einsum(v.ovov, (0, 1, 2, 3), x78, (4, 0, 3, 1), (2, 4))
    t2new += einsum(t2, (0, 1, 2, 3), x79, (1, 4), (0, 4, 2, 3)) * -1.0
    x80 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x80 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x80 += einsum(x64, (0, 1, 2, 3), (3, 1, 0, 2))
    x80 += einsum(x65, (0, 1, 2, 3), (3, 1, 0, 2))
    x81 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x81 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x81 += einsum(t1, (0, 1), x80, (0, 2, 3, 4), (3, 2, 4, 1))
    t2new += einsum(t1, (0, 1), x81, (2, 3, 0, 4), (2, 3, 1, 4))
    x82 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x82 += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x82, (0, 1, 2, 3), t2, (4, 1, 3, 5), (0, 4, 2, 5))
    x83 = np.zeros((nocc, nocc), dtype=np.float64)
    x83 += einsum(f.oo, (0, 1), (1, 0))
    x83 += einsum(x13, (0, 1), (0, 1))
    t3new = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    t3new += einsum(t3, (0, 1, 2, 3, 4, 5), x83, (1, 6), (0, 6, 2, 3, 4, 5)) * -1.0
    x84 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x84 += einsum(t3, (0, 1, 2, 3, 4, 5), x83, (2, 6), (0, 1, 6, 3, 4, 5))
    t3new += einsum(x84, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x84, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x85 = np.zeros((nvir, nvir), dtype=np.float64)
    x85 += einsum(f.vv, (0, 1), (1, 0))
    x85 += einsum(x68, (0, 1), (0, 1)) * -1.0
    t3new += einsum(x85, (0, 1), t3, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x86 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x86 += einsum(t3, (0, 1, 2, 3, 4, 5), x85, (5, 6), (0, 1, 2, 3, 4, 6))
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x87 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x87 += einsum(t2, (0, 1, 2, 3), f.ov, (4, 3), (4, 0, 1, 2))
    x88 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x88 += einsum(x87, (0, 1, 2, 3), t2, (4, 0, 5, 6), (1, 4, 2, 3, 5, 6))
    x89 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x89 += einsum(t1, (0, 1), x65, (2, 3, 0, 4), (3, 2, 4, 1))
    x90 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x90 += einsum(x89, (0, 1, 2, 3), t2, (2, 4, 5, 6), (1, 0, 4, 3, 5, 6))
    x91 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x91 += einsum(x88, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x91 += einsum(x90, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x92 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x92 += einsum(t2, (0, 1, 2, 3), f.ov, (4, 2), (4, 0, 1, 3))
    x93 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x93 += einsum(x92, (0, 1, 2, 3), t2, (4, 0, 5, 6), (1, 4, 2, 5, 3, 6))
    x94 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x94 += einsum(x21, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x95 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x95 += einsum(t2, (0, 1, 2, 3), x94, (4, 5, 0, 6), (4, 5, 1, 2, 3, 6))
    x96 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x96 += einsum(x93, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x96 += einsum(x95, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x96, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x96, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x96, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x96, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x97 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x97 += einsum(t2, (0, 1, 2, 3), x87, (0, 4, 5, 6), (4, 5, 1, 6, 2, 3))
    x98 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x98 += einsum(x92, (0, 1, 2, 3), t2, (0, 4, 5, 6), (1, 2, 4, 5, 3, 6))
    x99 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x99 += einsum(x97, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x99 += einsum(x98, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x99, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x99, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    x100 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x100 += einsum(t2, (0, 1, 2, 3), x28, (4, 5, 1, 6), (4, 0, 5, 2, 3, 6))
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x100, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x101 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x101 += einsum(t2, (0, 1, 2, 3), x5, (4, 5, 1, 6), (4, 0, 5, 2, 3, 6))
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x101, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x102 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x103 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x103 += einsum(x102, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x104 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x104 += einsum(t2, (0, 1, 2, 3), x103, (4, 5, 0, 6), (1, 4, 5, 2, 3, 6))
    t3new += einsum(x104, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x104, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x104, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x104, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    x105 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x105 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 5, 6, 3), (0, 1, 5, 4, 2, 6))
    x106 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x106 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 5, 3, 6), (4, 5, 1, 0, 2, 6))
    x107 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum(x106, (0, 1, 2, 3, 4, 5), t1, (4, 6), (0, 1, 2, 3, 6, 5))
    x108 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x108 += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x108 += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x109 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x109 += einsum(t1, (0, 1), x108, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x110 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 5, 3, 6), (4, 5, 1, 0, 6, 2))
    x111 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x111 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 5, 6, 3), (4, 5, 1, 0, 2, 6))
    x112 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x112 += einsum(x111, (0, 1, 2, 3, 4, 5), t1, (4, 6), (0, 1, 2, 3, 6, 5))
    x113 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x113 += einsum(x110, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x113 += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x114 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x114 += einsum(t1, (0, 1), x113, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x114, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x114, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    x115 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x115 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 5, 6), (0, 1, 5, 4, 2, 6))
    x116 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x116 += einsum(t1, (0, 1), x115, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x116, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x116, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x116, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x116, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x116, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x116, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x117 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x117 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 5, 1, 6), (4, 5, 2, 0, 6, 3))
    x118 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x118 += einsum(x117, (0, 1, 2, 3, 4, 5), t1, (3, 6), (0, 1, 2, 6, 4, 5))
    t3new += einsum(x118, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x118, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x118, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x118, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x118, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x118, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x119 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x119 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    t3new += einsum(x119, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x119, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x119, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x119, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x119, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x119, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x120 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x120 += einsum(v.ovvv, (0, 1, 2, 3), t2, (4, 5, 3, 6), (4, 5, 0, 6, 1, 2))
    t3new += einsum(x120, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x120, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x120, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x120, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x120, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x120, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x121 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x121 += einsum(t1, (0, 1), x66, (2, 3, 4, 0), (2, 4, 3, 1))
    x122 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x122 += einsum(t2, (0, 1, 2, 3), x121, (4, 1, 5, 6), (4, 0, 5, 6, 2, 3))
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x123 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x123 += einsum(x66, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x123 += einsum(x66, (0, 1, 2, 3), (0, 2, 3, 1))
    x124 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x124 += einsum(t1, (0, 1), x123, (2, 3, 4, 0), (2, 3, 4, 1))
    x125 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x125 += einsum(x124, (0, 1, 2, 3), t2, (2, 4, 5, 6), (4, 0, 1, 5, 6, 3)) * -1.0
    t3new += einsum(x125, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    t3new += einsum(x125, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x125, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x125, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    x126 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x126 += einsum(t1, (0, 1), x66, (2, 3, 0, 4), (2, 3, 4, 1))
    x127 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x127 += einsum(t2, (0, 1, 2, 3), x126, (4, 5, 1, 6), (4, 0, 5, 6, 2, 3))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    x128 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x128 += einsum(t1, (0, 1), v.oooo, (2, 0, 3, 4), (3, 4, 2, 1))
    x129 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x129 += einsum(t2, (0, 1, 2, 3), x128, (4, 1, 5, 6), (0, 5, 4, 6, 2, 3))
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x129, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x130 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x130 += einsum(t2, (0, 1, 2, 3), x128, (4, 0, 5, 6), (1, 5, 4, 6, 2, 3))
    t3new += einsum(x130, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x130, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x130, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x130, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3))
    x131 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x131 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 1, 5, 6), (0, 4, 5, 2, 3, 6))
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x131, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x132 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x132 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 0, 5, 6), (1, 4, 5, 2, 3, 6))
    t3new += einsum(x132, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x132, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    t3new += einsum(x132, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new += einsum(x132, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3)) * -1.0
    x133 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x133 += einsum(x20, (0, 1, 2, 3), t2, (4, 5, 6, 2), (0, 4, 5, 6, 3, 1))
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x134 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x134 += einsum(t2, (0, 1, 2, 3), x20, (4, 5, 2, 6), (4, 0, 1, 3, 6, 5))
    t3new += einsum(x134, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x134, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x134, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x134, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    t3new += einsum(x134, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x134, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))
    x135 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x135 += einsum(x89, (0, 1, 2, 3), t2, (4, 2, 5, 6), (1, 0, 4, 3, 5, 6))
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x135, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x136 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x136 += einsum(t2, (0, 1, 2, 3), x53, (4, 5, 6, 2), (4, 0, 1, 5, 3, 6))
    x137 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x137 += einsum(t2, (0, 1, 2, 3), x5, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x138 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x138 += einsum(x137, (0, 1, 2, 3, 4, 5), t1, (4, 6), (0, 1, 2, 3, 6, 5))
    x139 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x139 += einsum(x136, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x139 += einsum(x138, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x140 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x140 += einsum(t1, (0, 1), x139, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    x141 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x141 += einsum(x53, (0, 1, 2, 3), t2, (4, 5, 6, 3), (0, 4, 5, 1, 6, 2))
    x142 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x142 += einsum(t2, (0, 1, 2, 3), x5, (4, 5, 6, 2), (4, 0, 1, 6, 5, 3))
    x143 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x143 += einsum(x142, (0, 1, 2, 3, 4, 5), t1, (4, 6), (0, 1, 2, 3, 6, 5))
    x144 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x144 += einsum(x141, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x144 += einsum(x143, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x145 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x145 += einsum(t1, (0, 1), x144, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x145, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x145, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x145, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x145, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x145, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x145, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x146 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x146 += einsum(t2, (0, 1, 2, 3), x94, (4, 5, 1, 6), (4, 5, 0, 2, 3, 6))
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x146, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x147 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x147 += einsum(t2, (0, 1, 2, 3), x21, (4, 5, 2, 6), (4, 0, 1, 5, 3, 6))
    x148 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x148 += einsum(t1, (0, 1), x147, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x149 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x149 += einsum(x21, (0, 1, 2, 3), t2, (4, 5, 6, 2), (0, 4, 5, 1, 6, 3))
    x150 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x150 += einsum(t1, (0, 1), x149, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x150, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x150, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x150, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x150, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x150, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x150, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))

    return {"t1new": t1new, "t2new": t2new, "t3new": t3new}

