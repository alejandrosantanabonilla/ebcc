# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(f.ov, (0, 1), t1, (0, 1), ()) * 2.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x0 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x1 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    e_cc += einsum(x0, (0, 1, 2, 3), x1, (0, 1, 3, 2), ()) * 2.0

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t1new += einsum(f.vv, (0, 1), t1, (2, 1), (2, 0))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x0 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 6.0
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -2.0
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    t1new += einsum(v.ovov, (0, 1, 2, 3), x0, (4, 2, 0, 5, 3, 1), (4, 5)) * 0.25
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x1 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x2 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x2 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x2 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    t1new += einsum(x1, (0, 1, 2, 3), x2, (1, 3, 2, 4), (0, 4)) * 2.0
    x3 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x3 += einsum(t1, (0, 1), v.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x4 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x4 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    x4 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    t1new += einsum(t2, (0, 1, 2, 3), x4, (4, 1, 0, 3), (4, 2)) * -1.5
    x5 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x5 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x5 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x5 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x5 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3))
    t1new += einsum(t2, (0, 1, 2, 3), x5, (4, 1, 0, 2), (4, 3)) * -0.5
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x6 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x7 = np.zeros((nocc, nvir), dtype=np.float64)
    x7 += einsum(t1, (0, 1), x6, (0, 2, 3, 1), (2, 3))
    x8 = np.zeros((nocc, nvir), dtype=np.float64)
    x8 += einsum(f.ov, (0, 1), (0, 1)) * 0.5
    x8 += einsum(x7, (0, 1), (0, 1))
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x9 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t1new += einsum(x8, (0, 1), x9, (2, 0, 3, 1), (2, 3)) * 2.0
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x10 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    t1new += einsum(t1, (0, 1), x10, (0, 2, 1, 3), (2, 3)) * 2.0
    x11 = np.zeros((nocc, nocc), dtype=np.float64)
    x11 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -0.5
    x12 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum(x1, (0, 1, 2, 3), x12, (1, 4, 3, 2), (0, 4)) * 2.0
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x14 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x15 = np.zeros((nocc, nocc), dtype=np.float64)
    x15 += einsum(t1, (0, 1), x14, (2, 3, 0, 1), (2, 3)) * 2.0
    x16 = np.zeros((nocc, nocc), dtype=np.float64)
    x16 += einsum(f.oo, (0, 1), (0, 1))
    x16 += einsum(x11, (0, 1), (0, 1))
    x16 += einsum(x13, (0, 1), (1, 0))
    x16 += einsum(x15, (0, 1), (1, 0))
    t1new += einsum(t1, (0, 1), x16, (0, 2), (2, 1)) * -1.0
    t2new += einsum(x16, (0, 1), t2, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    t2new += einsum(x17, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x18 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x18 += einsum(t1, (0, 1), v.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    t2new += einsum(t1, (0, 1), x18, (2, 3, 1, 4), (0, 2, 3, 4))
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 1, 3), (0, 4, 2, 5))
    t2new += einsum(x19, (0, 1, 2, 3), (1, 0, 3, 2))
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 1, 2), (0, 4, 3, 5))
    t2new += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 1, 2, 5, 6, 3), (4, 0, 5, 6))
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 0, 6, 3, 1), (4, 5, 6, 2))
    x23 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x23 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x23 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(x23, (0, 1, 2, 3), t3, (1, 4, 2, 5, 6, 3), (4, 0, 5, 6)) * 0.5
    x25 = np.zeros((nocc, nvir), dtype=np.float64)
    x25 += einsum(t1, (0, 1), x6, (0, 2, 3, 1), (2, 3)) * 2.0
    x26 = np.zeros((nocc, nvir), dtype=np.float64)
    x26 += einsum(f.ov, (0, 1), (0, 1))
    x26 += einsum(x25, (0, 1), (0, 1))
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(x26, (0, 1), t3, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5))
    x28 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x28 += einsum(t2, (0, 1, 2, 3), x3, (4, 1, 5, 2), (4, 0, 5, 3))
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x29 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x30 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x30 += einsum(x29, (0, 1, 2, 3), t3, (4, 5, 0, 2, 6, 3), (4, 5, 1, 6)) * 0.5
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x32 += einsum(x31, (0, 1, 2, 3), (1, 0, 2, 3))
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum(t1, (0, 1), x32, (2, 3, 1, 4), (0, 2, 3, 4))
    x34 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x34 += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x34 += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x34 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(t1, (0, 1), x34, (2, 3, 0, 4), (2, 3, 1, 4))
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x36 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3))
    x36 += einsum(x24, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x36 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3))
    x36 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x36, (0, 1, 2, 3), (1, 0, 3, 2))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(t2, (0, 1, 2, 3), x31, (4, 1, 2, 5), (4, 0, 3, 5))
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(x3, (0, 1, 2, 3), t3, (4, 2, 1, 5, 6, 3), (0, 4, 5, 6))
    x39 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x39 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x39 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(x39, (0, 1, 2, 3), t3, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3)) * 0.5
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x41 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(x41, (0, 1, 2, 3), t3, (2, 4, 0, 5, 6, 3), (4, 1, 5, 6)) * 0.5
    x43 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x43 += einsum(t1, (0, 1), v.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x44 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x44 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 2, 6, 1, 3), (4, 5, 0, 6))
    x45 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x45 += einsum(v.ooov, (0, 1, 2, 3), x1, (4, 2, 3, 5), (0, 1, 4, 5))
    x46 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x46 += einsum(x43, (0, 1, 2, 3), (0, 2, 1, 3))
    x46 += einsum(x44, (0, 1, 2, 3), (0, 2, 1, 3))
    x46 += einsum(x45, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(t1, (0, 1), x46, (2, 0, 3, 4), (2, 3, 1, 4))
    x48 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x48 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3))
    x48 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x48 += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x48 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x48 += einsum(x47, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x48, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x48, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x49 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x49 += einsum(t2, (0, 1, 2, 3), x20, (4, 1, 5, 3), (0, 4, 2, 5))
    t2new += einsum(x49, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    t2new += einsum(x49, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x50 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x50 += einsum(t2, (0, 1, 2, 3), x3, (4, 1, 5, 3), (4, 0, 5, 2))
    x51 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x51 += einsum(t1, (0, 1), x50, (2, 3, 0, 4), (2, 3, 1, 4))
    t2new += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x51, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t2, (0, 1, 2, 3), x31, (4, 1, 3, 5), (4, 0, 2, 5))
    t2new += einsum(x52, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x52, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x53 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x53 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x54 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum(t1, (0, 1), x53, (2, 3, 0, 4), (2, 3, 1, 4))
    t2new += einsum(x54, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    t2new += einsum(x54, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x55 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum(t2, (0, 1, 2, 3), x6, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x56 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x56 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x56 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x56 += einsum(x1, (0, 1, 2, 3), x29, (1, 4, 5, 2), (0, 4, 3, 5))
    x56 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3))
    x56 += einsum(t1, (0, 1), x39, (2, 3, 1, 4), (0, 2, 4, 3)) * -1.0
    x56 += einsum(t1, (0, 1), x41, (0, 2, 3, 4), (2, 3, 1, 4)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x56, (4, 0, 5, 2), (4, 1, 5, 3))
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x58 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x58 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x59 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x59 += einsum(x57, (0, 1, 2, 3), (1, 0, 2, 3))
    x59 += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3))
    x59 += einsum(v.ovov, (0, 1, 2, 3), x1, (4, 2, 1, 5), (4, 0, 5, 3))
    t2new += einsum(t2, (0, 1, 2, 3), x59, (4, 1, 5, 3), (0, 4, 2, 5))
    x60 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x60 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x60 += einsum(x57, (0, 1, 2, 3), (1, 0, 2, 3))
    x60 += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x60 += einsum(v.ovov, (0, 1, 2, 3), x1, (2, 4, 5, 1), (4, 0, 5, 3))
    t2new += einsum(t2, (0, 1, 2, 3), x60, (4, 1, 5, 2), (0, 4, 5, 3))
    x61 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x61 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x61 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    x62 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x62 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x62 += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x62 += einsum(t1, (0, 1), x61, (2, 0, 3, 4), (2, 3, 1, 4))
    t2new += einsum(t2, (0, 1, 2, 3), x62, (4, 0, 5, 3), (4, 1, 2, 5))
    x63 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x63 += einsum(t1, (0, 1), v.ovvv, (0, 2, 3, 4), (1, 2, 3, 4))
    x64 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x64 += einsum(v.vvvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x64 += einsum(x63, (0, 1, 2, 3), (1, 0, 3, 2))
    x64 += einsum(x63, (0, 1, 2, 3), (3, 2, 1, 0))
    t2new += einsum(t2, (0, 1, 2, 3), x64, (2, 4, 3, 5), (0, 1, 4, 5)) * -1.0
    x65 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x65 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x66 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x66 += einsum(t1, (0, 1), x3, (2, 3, 4, 1), (2, 0, 4, 3))
    x67 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x67 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x68 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x68 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x68 += einsum(x65, (0, 1, 2, 3), (2, 0, 3, 1))
    x68 += einsum(x66, (0, 1, 2, 3), (3, 1, 2, 0))
    x68 += einsum(x67, (0, 1, 2, 3), (3, 0, 2, 1))
    x68 += einsum(x67, (0, 1, 2, 3), (2, 1, 3, 0))
    t2new += einsum(t2, (0, 1, 2, 3), x68, (0, 4, 1, 5), (4, 5, 2, 3))
    x69 = np.zeros((nvir, nvir), dtype=np.float64)
    x69 += einsum(f.ov, (0, 1), t1, (0, 2), (1, 2))
    x70 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x70 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 4.0
    x70 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x70 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x71 = np.zeros((nvir, nvir), dtype=np.float64)
    x71 += einsum(v.ovov, (0, 1, 2, 3), x70, (0, 2, 1, 4), (4, 3))
    x72 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x72 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    x72 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -3.0
    x72 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x73 = np.zeros((nvir, nvir), dtype=np.float64)
    x73 += einsum(v.ovov, (0, 1, 2, 3), x72, (0, 2, 3, 4), (4, 1))
    x74 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x74 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x74 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x75 = np.zeros((nvir, nvir), dtype=np.float64)
    x75 += einsum(t1, (0, 1), x74, (0, 2, 1, 3), (2, 3)) * 2.0
    x76 = np.zeros((nvir, nvir), dtype=np.float64)
    x76 += einsum(f.vv, (0, 1), (0, 1)) * -2.0
    x76 += einsum(x69, (0, 1), (0, 1)) * 2.0
    x76 += einsum(x71, (0, 1), (1, 0))
    x76 += einsum(x73, (0, 1), (1, 0)) * -1.0
    x76 += einsum(x75, (0, 1), (0, 1)) * -1.0
    t2new += einsum(x76, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1)) * -0.5
    t3new = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    t3new += einsum(x76, (0, 1), t3, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * -0.5
    x77 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x77 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 1.3333333333333333
    x77 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x77 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x78 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    x78 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x78 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x79 = np.zeros((nvir, nvir), dtype=np.float64)
    x79 += einsum(f.vv, (0, 1), (0, 1)) * -2.0
    x79 += einsum(x69, (0, 1), (0, 1)) * 2.0
    x79 += einsum(v.ovov, (0, 1, 2, 3), x77, (0, 2, 1, 4), (3, 4)) * 3.0
    x79 += einsum(v.ovov, (0, 1, 2, 3), x78, (0, 2, 3, 4), (1, 4)) * -1.0
    x79 += einsum(x75, (0, 1), (0, 1)) * -1.0
    t2new += einsum(x79, (0, 1), t2, (2, 3, 0, 4), (2, 3, 1, 4)) * -0.5
    x80 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x80 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    x80 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x80 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x81 = np.zeros((nocc, nocc), dtype=np.float64)
    x81 += einsum(v.ovov, (0, 1, 2, 3), x80, (2, 4, 3, 1), (4, 0))
    x82 = np.zeros((nocc, nocc), dtype=np.float64)
    x82 += einsum(v.ovov, (0, 1, 2, 3), x1, (4, 2, 3, 1), (4, 0))
    x83 = np.zeros((nocc, nocc), dtype=np.float64)
    x83 += einsum(f.oo, (0, 1), (0, 1))
    x83 += einsum(x11, (0, 1), (0, 1))
    x83 += einsum(x81, (0, 1), (1, 0))
    x83 += einsum(x15, (0, 1), (1, 0))
    x83 += einsum(x82, (0, 1), (1, 0)) * -1.0
    t2new += einsum(x83, (0, 1), t2, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    t3new += einsum(x83, (0, 1), t3, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -1.0
    x84 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x84 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x84 += einsum(v.ovov, (0, 1, 2, 3), x1, (4, 5, 3, 1), (0, 5, 4, 2))
    x85 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x85 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x85 += einsum(t1, (0, 1), x84, (0, 2, 3, 4), (3, 2, 4, 1))
    t2new += einsum(t1, (0, 1), x85, (2, 3, 0, 4), (2, 3, 1, 4))
    x86 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x86 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(t2, (0, 1, 2, 3), x86, (4, 1, 5, 2), (4, 0, 5, 3))
    x87 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x87 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 0, 5), (1, 4, 3, 5))
    t3new += einsum(x87, (0, 1, 2, 3), t3, (4, 5, 1, 6, 3, 7), (4, 0, 5, 6, 2, 7)) * 1.00000000000001
    x88 = np.zeros((nvir, nvir), dtype=np.float64)
    x88 += einsum(v.ovov, (0, 1, 2, 3), x77, (0, 2, 1, 4), (4, 3)) * 1.5
    x89 = np.zeros((nvir, nvir), dtype=np.float64)
    x89 += einsum(v.ovov, (0, 1, 2, 3), x78, (0, 2, 3, 4), (4, 1)) * 0.5
    x90 = np.zeros((nvir, nvir), dtype=np.float64)
    x90 += einsum(f.vv, (0, 1), (0, 1)) * -1.0
    x90 += einsum(x69, (0, 1), (0, 1))
    x90 += einsum(x88, (0, 1), (1, 0))
    x90 += einsum(x89, (0, 1), (1, 0)) * -1.0
    x91 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x91 += einsum(x90, (0, 1), t3, (2, 3, 4, 5, 6, 0), (2, 3, 4, 5, 6, 1))
    x92 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x92 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 6, 1, 7, 3), (4, 5, 6, 0, 2, 7))
    x93 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x93 += einsum(x92, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x93 += einsum(x92, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x94 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x94 += einsum(t2, (0, 1, 2, 3), x93, (4, 5, 6, 1, 0, 7), (4, 5, 6, 2, 3, 7)) * 0.25
    x95 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x95 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 3, 1), (4, 5, 6, 0, 7, 2))
    x96 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x96 += einsum(t1, (0, 1), x92, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x97 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(x95, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x97 += einsum(x96, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.5
    x98 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x98 += einsum(t1, (0, 1), x97, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x99 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x99 += einsum(x91, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x99 += einsum(x94, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x99 += einsum(x98, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x99, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x99, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    x100 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x100 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 6, 2), (0, 1, 4, 6, 3, 5))
    x101 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x101 += einsum(t1, (0, 1), x100, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x102 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x103 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x103 += einsum(x102, (0, 1, 2, 3), t3, (0, 4, 1, 5, 6, 3), (4, 5, 6, 2))
    x104 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x104 += einsum(t2, (0, 1, 2, 3), x103, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6)) * -0.5
    x105 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x105 += einsum(x101, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x105 += einsum(x104, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x106 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x106 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x107 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x107 += einsum(t2, (0, 1, 2, 3), x106, (4, 5, 6, 2), (0, 1, 4, 3, 5, 6))
    t3new += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 0.5
    t3new += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -0.5
    t3new += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x107, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -0.5
    t3new += einsum(x107, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * 0.5
    x108 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x108 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 0, 2, 5, 6, 1), (4, 5, 6, 3))
    x109 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x109 += einsum(t2, (0, 1, 2, 3), x108, (4, 5, 6, 2), (0, 1, 4, 3, 5, 6))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.5
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * 0.5
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * 0.5
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -0.5
    x110 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x110 += einsum(t2, (0, 1, 2, 3), v.ovvv, (0, 4, 5, 3), (1, 2, 4, 5))
    x111 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x111 += einsum(t2, (0, 1, 2, 3), x110, (4, 5, 2, 6), (0, 1, 4, 5, 3, 6))
    x112 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x112 += einsum(t2, (0, 1, 2, 3), x103, (4, 5, 6, 2), (0, 1, 4, 3, 5, 6)) * -0.5
    x113 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x113 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 1, 0, 5), (4, 2, 3, 5))
    x114 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x114 += einsum(x113, (0, 1, 2, 3), (0, 1, 2, 3))
    x114 += einsum(x110, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x115 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x115 += einsum(t2, (0, 1, 2, 3), x114, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    x116 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x116 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 1, 5, 6, 7, 3), (4, 5, 0, 2, 6, 7))
    x117 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x117 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x117 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x118 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x118 += einsum(t2, (0, 1, 2, 3), x29, (0, 4, 5, 2), (1, 4, 3, 5))
    x119 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x119 += einsum(x117, (0, 1, 2, 3), x118, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6)) * -1.0
    x120 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x120 += einsum(x116, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x120 += einsum(x119, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x121 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x121 += einsum(t1, (0, 1), x120, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x122 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x122 += einsum(x111, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x122 += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x122 += einsum(x115, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x122 += einsum(x121, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x122, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    x123 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x123 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5))
    x124 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x124 += einsum(x123, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (0, 4, 5, 2, 6, 7))
    x125 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x125 += einsum(x29, (0, 1, 2, 3), t3, (4, 5, 0, 2, 6, 3), (4, 5, 1, 6))
    x126 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x126 += einsum(t2, (0, 1, 2, 3), x125, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6)) * -0.5
    x127 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x127 += einsum(x124, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 1.00000000000001
    x127 += einsum(x126, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x127, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x128 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x128 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 5, 1, 6, 3, 7), (4, 5, 0, 2, 6, 7))
    x129 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x129 += einsum(t1, (0, 1), x128, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x130 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x130 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -0.3333333333333333
    x130 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x131 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x131 += einsum(x130, (0, 1, 2, 3), t3, (4, 1, 0, 5, 3, 6), (4, 5, 6, 2))
    x132 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x132 += einsum(t2, (0, 1, 2, 3), x131, (4, 5, 6, 2), (0, 1, 4, 3, 5, 6)) * 1.5
    x133 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x133 += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x133 += einsum(x132, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x133, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    x134 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x134 += einsum(x58, (0, 1, 2, 3), t3, (4, 1, 5, 6, 7, 3), (0, 4, 5, 6, 7, 2))
    x135 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x135 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 2, 5, 6, 3, 1), (4, 5, 0, 6))
    x136 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x136 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x136 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.5
    x137 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x137 += einsum(x29, (0, 1, 2, 3), x136, (4, 5, 0, 6, 2, 3), (1, 4, 5, 6))
    x138 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x138 += einsum(x135, (0, 1, 2, 3), (0, 1, 2, 3))
    x138 += einsum(x137, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x139 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x139 += einsum(t2, (0, 1, 2, 3), x138, (4, 5, 0, 6), (1, 4, 5, 2, 3, 6))
    x140 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x140 += einsum(x134, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x140 += einsum(x139, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x140, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    x141 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x141 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x141 += einsum(x106, (0, 1, 2, 3), (0, 1, 2, 3))
    x142 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x142 += einsum(t2, (0, 1, 2, 3), x141, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    t3new += einsum(x142, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x142, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new += einsum(x142, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x142, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x142, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    t3new += einsum(x142, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    x143 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x143 += einsum(t2, (0, 1, 2, 3), x44, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6))
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    t3new += einsum(x143, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    x144 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x144 += einsum(v.oooo, (0, 1, 2, 3), t3, (4, 1, 3, 5, 6, 7), (4, 0, 2, 5, 6, 7))
    x145 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x145 += einsum(x65, (0, 1, 2, 3), t3, (4, 3, 2, 5, 6, 7), (0, 1, 4, 5, 6, 7))
    x146 = np.zeros((nocc, nocc), dtype=np.float64)
    x146 += einsum(t1, (0, 1), x14, (2, 3, 0, 1), (2, 3))
    x147 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x147 += einsum(x146, (0, 1), t3, (2, 3, 1, 4, 5, 6), (2, 3, 0, 4, 5, 6)) * 2.0
    x148 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x148 += einsum(x144, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x148 += einsum(x145, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x148 += einsum(x147, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x148, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x149 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x149 += einsum(x67, (0, 1, 2, 3), t3, (4, 2, 3, 5, 6, 7), (0, 4, 1, 5, 6, 7))
    x150 = np.zeros((nocc, nocc), dtype=np.float64)
    x150 += einsum(f.oo, (0, 1), (0, 1))
    x150 += einsum(x11, (0, 1), (0, 1))
    x150 += einsum(x13, (0, 1), (1, 0))
    x151 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x151 += einsum(x150, (0, 1), t3, (2, 3, 0, 4, 5, 6), (2, 3, 1, 4, 5, 6))
    x152 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x152 += einsum(x149, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x152 += einsum(x151, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new += einsum(x152, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x152, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    x153 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x153 += einsum(v.vvvv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 1, 3), (4, 5, 6, 7, 0, 2))
    x154 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x154 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 6, 7, 1, 3), (4, 5, 6, 0, 2, 7))
    x155 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x155 += einsum(t2, (0, 1, 2, 3), x154, (4, 5, 6, 1, 0, 7), (4, 5, 6, 2, 3, 7))
    x156 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x156 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x156 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x157 = np.zeros((nvir, nvir), dtype=np.float64)
    x157 += einsum(t1, (0, 1), x156, (0, 2, 1, 3), (2, 3))
    x158 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x158 += einsum(x157, (0, 1), t3, (2, 3, 4, 5, 6, 0), (2, 3, 4, 5, 6, 1)) * 2.0
    x159 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x159 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x159 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x160 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x160 += einsum(x159, (0, 1, 2, 3), t3, (4, 5, 6, 2, 7, 1), (4, 5, 6, 0, 7, 3))
    x161 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x161 += einsum(t1, (0, 1), x160, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6)) * -0.5
    x162 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x162 += einsum(x153, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x162 += einsum(x155, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x162 += einsum(x158, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x162 += einsum(x161, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x162, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x162, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    x163 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x163 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 4, 5, 3), (0, 2, 4, 5))
    x164 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x164 += einsum(t2, (0, 1, 2, 3), x163, (4, 5, 3, 6), (0, 4, 1, 2, 5, 6))
    x165 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x165 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x166 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x166 += einsum(t2, (0, 1, 2, 3), x165, (4, 5, 1, 6), (4, 0, 5, 2, 3, 6))
    x167 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x167 += einsum(t2, (0, 1, 2, 3), x3, (4, 1, 0, 5), (4, 2, 3, 5))
    x168 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x168 += einsum(t2, (0, 1, 2, 3), x167, (4, 5, 6, 3), (4, 0, 1, 2, 5, 6))
    x169 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x169 += einsum(t2, (0, 1, 2, 3), x3, (4, 5, 0, 3), (4, 1, 5, 2))
    x170 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x170 += einsum(t2, (0, 1, 2, 3), x169, (4, 5, 1, 6), (4, 0, 5, 2, 6, 3))
    x171 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x171 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x171 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.99999999999999
    x172 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x172 += einsum(v.ovov, (0, 1, 2, 3), x171, (4, 2, 1, 5), (4, 0, 5, 3)) * 1.00000000000001
    x173 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x173 += einsum(x172, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 6, 7, 2))
    x174 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x174 += einsum(x8, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4)) * 2.0
    x175 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x175 += einsum(x67, (0, 1, 2, 3), (0, 2, 1, 3))
    x175 += einsum(x65, (0, 1, 2, 3), (0, 1, 3, 2))
    x176 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x176 += einsum(t1, (0, 1), x175, (2, 3, 4, 0), (2, 3, 4, 1))
    x177 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x177 += einsum(x174, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x177 += einsum(x176, (0, 1, 2, 3), (0, 2, 1, 3))
    x178 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x178 += einsum(t2, (0, 1, 2, 3), x177, (4, 1, 5, 6), (0, 4, 5, 2, 3, 6))
    x179 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x179 += einsum(t2, (0, 1, 2, 3), v.oooo, (4, 5, 6, 1), (0, 4, 5, 6, 2, 3))
    x180 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x180 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 1, 5), (0, 4, 3, 5))
    x181 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x181 += einsum(t2, (0, 1, 2, 3), x180, (4, 5, 6, 3), (0, 4, 1, 5, 2, 6))
    x182 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x182 += einsum(t2, (0, 1, 2, 3), x123, (4, 5, 6, 2), (0, 4, 1, 5, 6, 3))
    x183 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x183 += einsum(x179, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 4, 5))
    x183 += einsum(x181, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x183 += einsum(x182, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x184 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x184 += einsum(t1, (0, 1), x183, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x185 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x185 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x185 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x186 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x186 += einsum(t2, (0, 1, 2, 3), x185, (1, 4, 5, 3), (0, 4, 5, 2))
    x187 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x187 += einsum(t2, (0, 1, 2, 3), x186, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6)) * 2.0
    x188 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x188 += einsum(x164, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x188 += einsum(x166, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x188 += einsum(x168, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x188 += einsum(x170, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x188 += einsum(x173, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    x188 += einsum(x178, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.0
    x188 += einsum(x184, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x188 += einsum(x187, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x188, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x188, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x188, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x188, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x189 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x189 += einsum(v.ovov, (0, 1, 2, 3), x171, (4, 2, 3, 5), (4, 0, 5, 1))
    x190 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x190 += einsum(x189, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 6, 7, 2)) * 1.00000000000001
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x190, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    x191 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x191 += einsum(x19, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (0, 4, 5, 2, 6, 7))
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * 1.00000000000001
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.00000000000001
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * 2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -2.00000000000002
    t3new += einsum(x191, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * 2.00000000000002
    x192 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x192 += einsum(v.ovov, (0, 1, 2, 3), x171, (4, 2, 1, 5), (4, 0, 5, 3))
    x193 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x193 += einsum(x192, (0, 1, 2, 3), t3, (4, 5, 1, 6, 3, 7), (4, 5, 0, 6, 7, 2)) * 1.00000000000001
    t3new += einsum(x193, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x193, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x194 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x194 += einsum(t2, (0, 1, 2, 3), x3, (4, 0, 1, 5), (4, 2, 3, 5))
    x195 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x195 += einsum(t2, (0, 1, 2, 3), x194, (4, 5, 6, 3), (4, 0, 1, 2, 5, 6))
    x196 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x196 += einsum(v.ovov, (0, 1, 2, 3), x171, (2, 4, 5, 1), (4, 0, 5, 3))
    x197 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x197 += einsum(x196, (0, 1, 2, 3), t3, (4, 1, 5, 6, 7, 3), (4, 5, 0, 6, 7, 2)) * 1.00000000000001
    x198 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x198 += einsum(x195, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x198 += einsum(x197, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new += einsum(x198, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x198, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    x199 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x199 += einsum(x118, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 6, 7, 2)) * -1.00000000000001
    t3new += einsum(x199, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x199, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    x200 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x200 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 1, 2), (0, 4, 5, 3))
    x201 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x201 += einsum(t2, (0, 1, 2, 3), x200, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6))
    x202 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x202 += einsum(x58, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (0, 4, 5, 6, 7, 2))
    x203 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x203 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 4, 5, 2), (0, 3, 4, 5))
    x204 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x204 += einsum(t2, (0, 1, 2, 3), x203, (4, 5, 3, 6), (0, 4, 1, 2, 5, 6))
    x205 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x205 += einsum(t2, (0, 1, 2, 3), x167, (4, 5, 6, 2), (4, 0, 1, 5, 3, 6))
    x206 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x206 += einsum(t1, (0, 1), x180, (2, 0, 3, 4), (2, 1, 3, 4))
    x207 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x207 += einsum(x163, (0, 1, 2, 3), (0, 1, 2, 3))
    x207 += einsum(x206, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x208 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x208 += einsum(t2, (0, 1, 2, 3), x207, (4, 5, 2, 6), (0, 1, 4, 3, 5, 6))
    x209 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x209 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 3, 5, 2), (0, 1, 4, 5))
    x210 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x210 += einsum(x43, (0, 1, 2, 3), (0, 2, 1, 3))
    x210 += einsum(x209, (0, 1, 2, 3), (0, 1, 2, 3))
    x211 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x211 += einsum(t2, (0, 1, 2, 3), x210, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6))
    x212 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x212 += einsum(x201, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x212 += einsum(x202, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x212 += einsum(x204, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x212 += einsum(x205, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.5
    x212 += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x212 += einsum(x211, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x212, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x212, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x212, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x212, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x213 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x213 += einsum(t2, (0, 1, 2, 3), x194, (4, 5, 6, 2), (4, 0, 1, 5, 3, 6))
    t3new += einsum(x213, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.5
    t3new += einsum(x213, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * 0.5
    t3new += einsum(x213, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x213, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x213, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * 0.5
    t3new += einsum(x213, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -0.5
    x214 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x214 += einsum(t1, (0, 1), x67, (2, 3, 0, 4), (2, 3, 4, 1))
    x215 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x215 += einsum(t2, (0, 1, 2, 3), x214, (4, 5, 1, 6), (4, 0, 5, 6, 2, 3))
    x216 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x216 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x216 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3))
    x217 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x217 += einsum(t2, (0, 1, 2, 3), x216, (4, 5, 1, 3), (0, 4, 5, 2))
    x218 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x218 += einsum(t2, (0, 1, 2, 3), x217, (4, 5, 1, 6), (0, 5, 4, 2, 3, 6)) * 2.0
    x219 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x219 += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x219 += einsum(x218, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x219, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x219, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x219, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x219, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    x220 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x220 += einsum(t1, (0, 1), x31, (2, 3, 1, 4), (0, 2, 3, 4))
    x221 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x221 += einsum(t2, (0, 1, 2, 3), x220, (4, 5, 1, 6), (4, 5, 0, 2, 3, 6))
    x222 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x222 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x222 += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3))
    x223 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x223 += einsum(t2, (0, 1, 2, 3), x222, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6))
    x224 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x224 += einsum(x221, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x224 += einsum(x223, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x224, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x224, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x224, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x224, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    x225 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x225 += einsum(x67, (0, 1, 2, 3), t3, (4, 3, 2, 5, 6, 7), (0, 4, 1, 5, 6, 7))
    x226 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x226 += einsum(x66, (0, 1, 2, 3), t3, (4, 3, 2, 5, 6, 7), (1, 0, 4, 5, 6, 7))
    x227 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x227 += einsum(x225, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x227 += einsum(x226, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x227, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    x228 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x228 += einsum(t2, (0, 1, 2, 3), x20, (4, 5, 6, 2), (0, 4, 1, 5, 3, 6))
    x229 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x229 += einsum(t1, (0, 1), x228, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x229, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x229, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x229, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x229, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x229, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x229, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x230 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x230 += einsum(t2, (0, 1, 2, 3), x19, (4, 5, 6, 3), (0, 4, 1, 5, 2, 6))
    x231 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x231 += einsum(t1, (0, 1), x230, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x231, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x231, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x231, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -2.0
    t3new += einsum(x231, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * 2.0
    t3new += einsum(x231, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * 2.0
    t3new += einsum(x231, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -2.0
    x232 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x232 += einsum(v.vvvv, (0, 1, 2, 3), t3, (4, 5, 6, 1, 7, 3), (4, 5, 6, 7, 0, 2))
    x233 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x233 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 1, 3), (4, 5, 6, 0, 7, 2))
    x234 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x234 += einsum(t1, (0, 1), x154, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x235 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x235 += einsum(x233, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x235 += einsum(x234, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x236 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x236 += einsum(t1, (0, 1), x235, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x237 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x237 += einsum(x232, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.5
    x237 += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x237, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x237, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x238 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x238 += einsum(t2, (0, 1, 2, 3), x203, (4, 5, 2, 6), (0, 4, 1, 3, 5, 6))
    x239 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x239 += einsum(t2, (0, 1, 2, 3), x123, (4, 5, 6, 3), (0, 4, 1, 5, 2, 6))
    x240 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x240 += einsum(t1, (0, 1), x239, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x241 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x241 += einsum(x238, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x241 += einsum(x240, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x241, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x241, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x241, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new += einsum(x241, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    x242 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x242 += einsum(t2, (0, 1, 2, 3), x20, (4, 5, 6, 3), (0, 4, 1, 5, 2, 6))
    x243 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x243 += einsum(t1, (0, 1), x242, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x243, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x243, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new += einsum(x243, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x243, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x243, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x243, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))
    x244 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x244 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 0, 5), (1, 4, 2, 5))
    x245 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x245 += einsum(t2, (0, 1, 2, 3), x244, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6))
    x246 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x246 += einsum(t2, (0, 1, 2, 3), x244, (4, 5, 6, 2), (0, 1, 4, 5, 6, 3))
    x247 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x247 += einsum(x245, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x247 += einsum(x246, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x248 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x248 += einsum(t1, (0, 1), x247, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x248, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x248, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    x249 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x249 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 3, 4, 5), (0, 2, 4, 5))
    x250 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x250 += einsum(t2, (0, 1, 2, 3), x249, (4, 5, 6, 3), (0, 4, 1, 2, 5, 6))
    x251 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x251 += einsum(t2, (0, 1, 2, 3), x19, (4, 5, 6, 2), (0, 4, 1, 5, 6, 3))
    x252 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x252 += einsum(t1, (0, 1), x251, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x253 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x253 += einsum(x250, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x253 += einsum(x252, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x253, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x253, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x253, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 2.0
    t3new += einsum(x253, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -2.0
    t3new += einsum(x253, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -2.0
    t3new += einsum(x253, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * 2.0
    x254 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x254 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 0, 1, 5), (4, 2, 3, 5))
    x255 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x255 += einsum(t2, (0, 1, 2, 3), x254, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    x256 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x256 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 0, 5, 3), (1, 4, 5, 2))
    x257 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x257 += einsum(t2, (0, 1, 2, 3), x256, (4, 5, 1, 6), (0, 4, 5, 2, 6, 3))
    x258 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x258 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 2, 6, 7))
    x259 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x259 += einsum(t2, (0, 1, 2, 3), x66, (4, 5, 1, 6), (5, 4, 0, 6, 2, 3))
    x260 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x260 += einsum(x258, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x260 += einsum(x259, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x261 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x261 += einsum(t1, (0, 1), x260, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x262 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x262 += einsum(x255, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x262 += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x262 += einsum(x261, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x262, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x262, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x262, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x262, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x263 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x263 += einsum(t2, (0, 1, 2, 3), x58, (4, 5, 6, 2), (4, 0, 1, 5, 3, 6))
    x264 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x264 += einsum(t2, (0, 1, 2, 3), x3, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x265 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x265 += einsum(t1, (0, 1), x264, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x266 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x266 += einsum(x263, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x266 += einsum(x265, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x267 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x267 += einsum(t1, (0, 1), x266, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x267, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x267, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x267, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    t3new += einsum(x267, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x267, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x267, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    x268 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x268 += einsum(t2, (0, 1, 2, 3), x58, (4, 5, 6, 3), (4, 0, 1, 5, 2, 6))
    x269 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x269 += einsum(t2, (0, 1, 2, 3), x3, (4, 5, 6, 2), (4, 0, 1, 6, 5, 3))
    x270 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x270 += einsum(t1, (0, 1), x269, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x271 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x271 += einsum(x268, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x271 += einsum(x270, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x272 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x272 += einsum(t1, (0, 1), x271, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x272, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x272, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x272, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x272, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x272, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x272, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x273 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x273 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 5, 6, 2), (0, 1, 4, 3, 5, 6))
    t3new += einsum(x273, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x273, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x273, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x273, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x273, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x273, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x274 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x274 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 5, 1, 6, 3, 7), (4, 5, 0, 6, 7, 2))
    t3new += einsum(x274, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x274, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    x275 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x275 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 1, 5, 6), (0, 4, 5, 2, 3, 6))
    x276 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x276 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 6, 7, 2))
    x277 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x277 += einsum(t2, (0, 1, 2, 3), x254, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6))
    x278 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x278 += einsum(x275, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x278 += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x278 += einsum(x277, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.5
    t3new += einsum(x278, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x278, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x278, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x278, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x279 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x279 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 1, 5, 6, 7, 3), (4, 5, 0, 6, 7, 2))
    x280 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x280 += einsum(t2, (0, 1, 2, 3), x39, (0, 4, 2, 5), (1, 3, 4, 5))
    x281 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x281 += einsum(x117, (0, 1, 2, 3), x280, (4, 5, 2, 6), (0, 1, 4, 3, 5, 6)) * -1.0
    x282 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x282 += einsum(t2, (0, 1, 2, 3), x159, (4, 3, 2, 5), (0, 1, 4, 5))
    x283 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x283 += einsum(t2, (0, 1, 2, 3), x282, (4, 5, 0, 6), (1, 4, 5, 2, 3, 6)) * -1.0
    x284 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x284 += einsum(x279, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x284 += einsum(x281, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x284 += einsum(x283, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x284, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x284, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    x285 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x285 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 2, 6, 7, 3), (4, 5, 0, 6, 7, 1))
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x285, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    x286 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x286 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6))
    x287 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x287 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 6, 2), (0, 1, 4, 5, 6, 3))
    x288 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x288 += einsum(t1, (0, 1), x287, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x289 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x289 += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x289 += einsum(x288, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x290 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x290 += einsum(t1, (0, 1), x289, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x290, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x290, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x290, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x290, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x290, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x290, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x291 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x291 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6))
    x292 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x292 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x293 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x293 += einsum(t1, (0, 1), x292, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x294 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x294 += einsum(x291, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x294 += einsum(x293, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x295 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x295 += einsum(t1, (0, 1), x294, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x295, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x295, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x295, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x295, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x295, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x295, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    x296 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x296 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 6, 3), (0, 1, 4, 6, 2, 5))
    x297 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x297 += einsum(t1, (0, 1), x296, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x297, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x297, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x297, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x297, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x297, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x297, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x298 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x298 += einsum(t2, (0, 1, 2, 3), x113, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6))
    t3new += einsum(x298, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.5
    t3new += einsum(x298, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -0.5
    t3new += einsum(x298, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x298, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x298, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -0.5
    t3new += einsum(x298, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * 0.5
    x299 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x299 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 5, 2, 6, 7, 3), (4, 5, 0, 1, 6, 7))
    x300 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x300 += einsum(t1, (0, 1), x299, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x300, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x301 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x301 += einsum(t2, (0, 1, 2, 3), x18, (4, 5, 3, 6), (4, 0, 1, 2, 6, 5))
    t3new += einsum(x301, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x301, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x301, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x301, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x301, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x301, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x302 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x302 += einsum(t2, (0, 1, 2, 3), x18, (4, 5, 2, 6), (4, 0, 1, 3, 6, 5))
    t3new += einsum(x302, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x302, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x302, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x302, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    t3new += einsum(x302, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x302, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))
    x303 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x303 += einsum(x58, (0, 1, 2, 3), t3, (4, 5, 1, 6, 3, 7), (0, 4, 5, 6, 7, 2))
    t3new += einsum(x303, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x303, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -1.0
    x304 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x304 += einsum(x31, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 2), (0, 4, 5, 6, 7, 3))
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x304, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x305 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x305 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 2, 4, 5), (0, 3, 4, 5))
    x306 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x306 += einsum(t2, (0, 1, 2, 3), x305, (4, 5, 6, 3), (0, 4, 1, 2, 5, 6))
    t3new += einsum(x306, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x306, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x306, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x306, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x306, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x306, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x307 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x307 += einsum(t2, (0, 1, 2, 3), x305, (4, 5, 6, 2), (0, 4, 1, 3, 5, 6))
    t3new += einsum(x307, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x307, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x307, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x307, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x307, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x307, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))
    x308 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x308 += einsum(t2, (0, 1, 2, 3), x249, (4, 5, 6, 2), (0, 4, 1, 5, 3, 6))
    t3new += einsum(x308, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x308, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x308, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -2.0
    t3new += einsum(x308, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * 2.0
    t3new += einsum(x308, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * 2.0
    t3new += einsum(x308, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -2.0
    x309 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x309 += einsum(t2, (0, 1, 2, 3), x31, (4, 5, 2, 6), (4, 0, 1, 5, 3, 6))
    x310 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x310 += einsum(t1, (0, 1), x309, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x310, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x310, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x310, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x310, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x310, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x310, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x311 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x311 += einsum(t2, (0, 1, 2, 3), x31, (4, 5, 3, 6), (4, 0, 1, 5, 2, 6))
    x312 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x312 += einsum(t1, (0, 1), x311, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x312, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x312, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x312, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x312, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x312, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x312, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))
    x313 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x313 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * -0.99999999999999
    x313 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x313 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x313 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x314 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x314 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x314 += einsum(x17, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x314 += einsum(x31, (0, 1, 2, 3), (1, 0, 2, 3))
    x314 += einsum(v.ovov, (0, 1, 2, 3), x313, (2, 4, 5, 3), (0, 4, 1, 5)) * 1.00000000000001
    x315 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x315 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x315 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x314, (0, 1, 2, 3), x315, (4, 5, 0, 6, 2, 7), (4, 1, 5, 6, 3, 7)) * -1.0
    x316 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x316 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.99999999999999
    x316 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x316 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x317 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x317 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.99999999999999
    x317 += einsum(x57, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.99999999999999
    x317 += einsum(x58, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.99999999999999
    x317 += einsum(v.ovov, (0, 1, 2, 3), x316, (2, 4, 5, 1), (0, 4, 3, 5)) * -1.0
    t3new += einsum(x317, (0, 1, 2, 3), t3, (4, 0, 5, 6, 2, 7), (4, 1, 5, 6, 3, 7)) * -1.00000000000001
    x318 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x318 += einsum(v.oooo, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x318 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x318 += einsum(x67, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x318 += einsum(x67, (0, 1, 2, 3), (3, 0, 2, 1))
    x318 += einsum(x67, (0, 1, 2, 3), (2, 1, 3, 0))
    x318 += einsum(x67, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x318 += einsum(x65, (0, 1, 2, 3), (2, 0, 3, 1))
    x318 += einsum(x65, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x318 += einsum(x66, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x318 += einsum(x66, (0, 1, 2, 3), (3, 1, 2, 0))
    t3new += einsum(x318, (0, 1, 2, 3), t3, (2, 4, 0, 5, 6, 7), (1, 4, 3, 5, 6, 7)) * -0.5
    x319 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x319 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x319 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x319 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x319 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x320 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x320 += einsum(x319, (0, 1, 2, 3), x61, (4, 0, 5, 3), (4, 5, 1, 2))
    x321 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x321 += einsum(t2, (0, 1, 2, 3), x61, (4, 5, 0, 2), (1, 4, 5, 3))
    x322 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x322 += einsum(t2, (0, 1, 2, 3), x61, (4, 5, 1, 2), (0, 4, 5, 3))
    x323 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x323 += einsum(x8, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4)) * 2.0
    x324 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x324 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x324 += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2))
    x325 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x325 += einsum(t1, (0, 1), x324, (2, 3, 1, 4), (0, 2, 3, 4))
    x326 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x326 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x326 += einsum(x67, (0, 1, 2, 3), (2, 1, 0, 3))
    x326 += einsum(x65, (0, 1, 2, 3), (3, 1, 0, 2))
    x327 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x327 += einsum(t1, (0, 1), x326, (0, 2, 3, 4), (2, 3, 4, 1))
    x328 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x328 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x328 += einsum(x3, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x328 += einsum(x320, (0, 1, 2, 3), (2, 1, 0, 3))
    x328 += einsum(x321, (0, 1, 2, 3), (0, 2, 1, 3))
    x328 += einsum(x322, (0, 1, 2, 3), (1, 2, 0, 3))
    x328 += einsum(x323, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x328 += einsum(x325, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x328 += einsum(x327, (0, 1, 2, 3), (0, 2, 1, 3))
    t3new += einsum(x117, (0, 1, 2, 3), x328, (4, 1, 5, 6), (0, 4, 5, 3, 6, 2)) * -1.0
    x329 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x329 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x329 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    t3new += einsum(x328, (0, 1, 2, 3), x329, (4, 1, 5, 6), (2, 0, 4, 6, 3, 5)) * -1.0
    x330 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x330 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x330 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x331 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x331 += einsum(v.ooov, (0, 1, 2, 3), x330, (4, 2, 5, 3), (0, 1, 4, 5)) * 2.0
    x332 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x332 += einsum(x43, (0, 1, 2, 3), (0, 2, 1, 3))
    x332 += einsum(x331, (0, 1, 2, 3), (2, 1, 0, 3))
    x333 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x333 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x333 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x333 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x334 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x334 += einsum(v.ooov, (0, 1, 2, 3), x333, (1, 4, 5, 3), (0, 2, 4, 5))
    x335 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x335 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.5
    x335 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x335 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x336 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x336 += einsum(x3, (0, 1, 2, 3), x335, (1, 4, 5, 3), (0, 2, 4, 5)) * 2.0
    x337 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x337 += einsum(x117, (0, 1, 2, 3), x3, (4, 5, 1, 2), (4, 5, 0, 3))
    x338 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x338 += einsum(x334, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x338 += einsum(x336, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x338 += einsum(x337, (0, 1, 2, 3), (0, 2, 1, 3))
    x338 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3))
    x339 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x339 += einsum(t1, (0, 1), x67, (2, 3, 4, 0), (2, 4, 3, 1))
    x340 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x340 += einsum(x8, (0, 1), x329, (2, 3, 4, 1), (0, 2, 3, 4)) * 2.0
    x341 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x341 += einsum(v.oooo, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x341 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x341 += einsum(x65, (0, 1, 2, 3), (2, 0, 3, 1))
    x341 += einsum(x65, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x342 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x342 += einsum(t1, (0, 1), x341, (0, 2, 3, 4), (2, 3, 4, 1))
    x343 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x343 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x343 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x343 += einsum(x332, (0, 1, 2, 3), (0, 1, 2, 3))
    x343 += einsum(x332, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x343 += einsum(x338, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x343 += einsum(x338, (0, 1, 2, 3), (1, 0, 2, 3))
    x343 += einsum(x339, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x343 += einsum(x339, (0, 1, 2, 3), (1, 0, 2, 3))
    x343 += einsum(x340, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x343 += einsum(x342, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x344 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x344 += einsum(t2, (0, 1, 2, 3), x343, (4, 5, 0, 6), (1, 4, 5, 2, 3, 6))
    t3new += einsum(x344, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x344, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0

    return {"t1new": t1new, "t2new": t2new, "t3new": t3new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    # L amplitudes
    l1new = np.zeros((nvir, nocc), dtype=np.float64)
    l1new += einsum(f.ov, (0, 1), (1, 0))
    l1new += einsum(l1, (0, 1), v.oovv, (2, 1, 3, 0), (3, 2)) * -1.0
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(v.ovov, (0, 1, 2, 3), (1, 3, 0, 2))
    l2new += einsum(l2, (0, 1, 2, 3), v.vvvv, (4, 0, 5, 1), (4, 5, 2, 3))
    l2new += einsum(v.ooov, (0, 1, 2, 3), l3, (4, 5, 3, 2, 6, 1), (4, 5, 0, 6)) * 0.5
    l2new += einsum(v.ooov, (0, 1, 2, 3), l3, (4, 5, 3, 1, 6, 2), (4, 5, 0, 6)) * -0.5
    l2new += einsum(l2, (0, 1, 2, 3), v.ovov, (4, 5, 3, 1), (5, 0, 4, 2))
    l2new += einsum(l2, (0, 1, 2, 3), v.ovov, (4, 5, 2, 1), (5, 0, 4, 3)) * -1.0
    l3new = np.zeros((nvir, nvir, nvir, nocc, nocc, nocc), dtype=np.float64)
    l3new += einsum(l1, (0, 1), v.ovov, (2, 3, 4, 5), (0, 3, 5, 1, 2, 4))
    l3new += einsum(l1, (0, 1), v.ovov, (2, 3, 4, 5), (5, 3, 0, 1, 2, 4)) * -1.0
    l3new += einsum(l1, (0, 1), v.ovov, (2, 3, 4, 5), (5, 0, 3, 2, 1, 4)) * -1.0
    l3new += einsum(l1, (0, 1), v.ovov, (2, 3, 4, 5), (3, 0, 5, 2, 1, 4))
    l3new += einsum(l1, (0, 1), v.ovov, (2, 3, 4, 5), (0, 5, 3, 2, 4, 1)) * -1.0
    l3new += einsum(l1, (0, 1), v.ovov, (2, 3, 4, 5), (3, 5, 0, 2, 4, 1))
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x1 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), x0, (4, 5, 2, 6), (4, 0, 1, 5, 3, 6))
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x1, (3, 4, 5, 6, 0, 2), (1, 6))
    x2 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(f.ov, (0, 1), t3, (2, 3, 4, 5, 1, 6), (0, 2, 3, 4, 5, 6))
    x3 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(f.ov, (0, 1), t3, (2, 3, 4, 1, 5, 6), (0, 2, 3, 4, 5, 6))
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x4 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x5 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(t2, (0, 1, 2, 3), x4, (4, 5, 3, 6), (0, 1, 4, 5, 2, 6))
    x6 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), x4, (4, 5, 2, 6), (0, 1, 4, 5, 3, 6))
    x7 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x8 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x8 += einsum(x7, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x8 += einsum(x7, (0, 1, 2, 3, 4, 5), (0, 1, 3, 4, 2, 5))
    x9 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(t1, (0, 1), x8, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x10 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 6, 2), (0, 1, 4, 5, 6, 3))
    x11 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(x10, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x11 += einsum(x10, (0, 1, 2, 3, 4, 5), (0, 1, 3, 4, 2, 5))
    x12 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(t1, (0, 1), x11, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x13 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x13 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x14 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), t3, (4, 5, 6, 2, 7, 1), (4, 5, 6, 0, 7, 3)) * 0.16666666666666
    x15 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(x13, (0, 1, 2, 3), t3, (4, 5, 6, 2, 1, 7), (4, 5, 6, 0, 7, 3)) * 0.33333333333332
    x16 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 6, 1, 7, 3), (4, 5, 6, 0, 2, 7))
    x17 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x17 += einsum(x16, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x17 += einsum(x16, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x18 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(t1, (0, 1), x17, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * 0.16666666666666
    x19 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 6, 1, 3, 7), (4, 5, 6, 0, 2, 7))
    x20 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x20 += einsum(x19, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x20 += einsum(x19, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x21 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(t1, (0, 1), x20, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * 0.33333333333332
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x22 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(t2, (0, 1, 2, 3), x22, (1, 4, 5, 3), (0, 4, 2, 5))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x24 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(t2, (0, 1, 2, 3), x24, (1, 4, 5, 2), (0, 4, 3, 5)) * 0.5
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x26 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    x27 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), x26, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6))
    x28 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(t2, (0, 1, 2, 3), x23, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6))
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(t2, (0, 1, 2, 3), x24, (1, 4, 5, 2), (0, 4, 3, 5))
    x30 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(t2, (0, 1, 2, 3), x29, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6)) * -0.5
    x31 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(x2, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * 0.16666666666666
    x31 += einsum(x2, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -0.16666666666666
    x31 += einsum(x2, (0, 1, 2, 3, 4, 5), (3, 1, 0, 2, 4, 5)) * 0.16666666666666
    x31 += einsum(x3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -0.16666666666666
    x31 += einsum(x3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * 0.16666666666666
    x31 += einsum(x3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * 1.16666666666662
    x31 += einsum(x3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -0.16666666666666
    x31 += einsum(x3, (0, 1, 2, 3, 4, 5), (3, 1, 0, 2, 4, 5)) * -0.16666666666666
    x31 += einsum(x3, (0, 1, 2, 3, 4, 5), (3, 1, 0, 2, 5, 4)) * 0.16666666666666
    x31 += einsum(x5, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x31 += einsum(x5, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x31 += einsum(x6, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x31 += einsum(x6, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -3.0
    x31 += einsum(x9, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x31 += einsum(x9, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4))
    x31 += einsum(x12, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x31 += einsum(x12, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * -3.0
    x31 += einsum(x14, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x31 += einsum(x14, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -4.0
    x31 += einsum(x14, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 4, 5))
    x31 += einsum(x15, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x31 += einsum(x15, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x31 += einsum(x15, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 4, 5)) * -1.0
    x31 += einsum(x18, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x31 += einsum(x18, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * 4.0
    x31 += einsum(x18, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 5, 4)) * -1.0
    x31 += einsum(x21, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x31 += einsum(x21, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * -1.0
    x31 += einsum(x21, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 5, 4))
    x31 += einsum(x27, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x31 += einsum(x27, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x31 += einsum(x28, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x31 += einsum(x28, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * 3.0
    x31 += einsum(x30, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x31 += einsum(x30, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -3.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x31, (4, 3, 6, 5, 1, 2), (0, 6)) * -0.5
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum(t1, (0, 1), v.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x34 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x34 += einsum(t2, (0, 1, 2, 3), x33, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x35 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(v.ooov, (0, 1, 2, 3), t3, (1, 4, 5, 6, 3, 7), (4, 5, 0, 2, 6, 7))
    x36 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x36 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x36 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    x37 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(v.ooov, (0, 1, 2, 3), x36, (4, 2, 5, 6, 3, 7), (0, 1, 4, 5, 6, 7)) * 0.25
    x38 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(x35, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 0.25
    x38 += einsum(x37, (0, 1, 2, 3, 4, 5), (2, 3, 1, 0, 4, 5)) * -1.0
    x39 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(v.ooov, (0, 1, 2, 3), t3, (1, 4, 5, 3, 6, 7), (4, 5, 0, 2, 6, 7))
    x40 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(v.ooov, (0, 1, 2, 3), t3, (2, 4, 5, 3, 6, 7), (4, 5, 0, 1, 6, 7))
    x41 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(x33, (0, 1, 2, 3), t3, (2, 4, 5, 6, 3, 7), (0, 4, 5, 1, 6, 7))
    x42 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(x33, (0, 1, 2, 3), x36, (4, 1, 5, 6, 3, 7), (0, 2, 4, 5, 6, 7)) * 0.25
    x43 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(x41, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.25
    x43 += einsum(x42, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 4, 5)) * -1.0
    x44 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(x33, (0, 1, 2, 3), t3, (2, 4, 5, 3, 6, 7), (0, 4, 5, 1, 6, 7))
    x45 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x45 += einsum(x33, (0, 1, 2, 3), t3, (1, 4, 5, 3, 6, 7), (0, 4, 5, 2, 6, 7))
    x46 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x46 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 1, 2), (0, 4, 3, 5))
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x47 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x48 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x48 += einsum(t2, (0, 1, 2, 3), x47, (1, 4, 3, 5), (0, 4, 2, 5))
    x49 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x49 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3))
    x49 += einsum(x48, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x50 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x50 += einsum(t2, (0, 1, 2, 3), x49, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6)) * 0.25
    x51 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x51 += einsum(t2, (0, 1, 2, 3), x29, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6)) * -0.25
    x52 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x52 += einsum(x51, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x53 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(t2, (0, 1, 2, 3), x23, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6)) * 0.5
    x54 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 1, 5), (0, 4, 3, 5))
    x55 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum(t2, (0, 1, 2, 3), x54, (4, 5, 6, 3), (0, 4, 1, 5, 2, 6))
    x56 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x56 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    l2new += einsum(l2, (0, 1, 2, 3), x56, (3, 4, 2, 5), (0, 1, 4, 5))
    x57 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x57 += einsum(t1, (0, 1), x33, (2, 3, 4, 1), (0, 2, 3, 4))
    x58 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x58 += einsum(x56, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.0
    x58 += einsum(x56, (0, 1, 2, 3), (0, 2, 3, 1)) * 2.0
    x58 += einsum(x57, (0, 1, 2, 3), (0, 1, 2, 3))
    x58 += einsum(x57, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x59 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x60 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x60 += einsum(t2, (0, 1, 2, 3), x32, (4, 5, 6, 3), (4, 1, 5, 0, 2, 6))
    x60 += einsum(t1, (0, 1), x34, (2, 3, 4, 5, 0, 6), (2, 4, 5, 3, 6, 1)) * -1.0
    x60 += einsum(x38, (0, 1, 2, 3, 4, 5), (3, 0, 2, 1, 5, 4))
    x60 += einsum(x38, (0, 1, 2, 3, 4, 5), (3, 1, 2, 0, 5, 4)) * -1.0
    x60 += einsum(x39, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 4, 5)) * 0.25
    x60 += einsum(x39, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 5, 4)) * -1.25
    x60 += einsum(x39, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 4, 5)) * -0.25
    x60 += einsum(x39, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 5, 4)) * 0.25
    x60 += einsum(x40, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 4, 5)) * -0.25
    x60 += einsum(x40, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 5, 4)) * 1.25
    x60 += einsum(x40, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 4, 5)) * 1.25
    x60 += einsum(x40, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 5, 4)) * -0.25
    x60 += einsum(x43, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x60 += einsum(x43, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 5, 4)) * -1.0
    x60 += einsum(x44, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 0.25
    x60 += einsum(x44, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.25
    x60 += einsum(x44, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 4, 5)) * -0.25
    x60 += einsum(x44, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 5, 4)) * 0.25
    x60 += einsum(x45, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -0.25
    x60 += einsum(x45, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 1.25
    x60 += einsum(x45, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 4, 5)) * 1.25
    x60 += einsum(x45, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 5, 4)) * -0.25
    x60 += einsum(x52, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x60 += einsum(x52, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 4, 5))
    x60 += einsum(x53, (0, 1, 2, 3, 4, 5), (2, 0, 3, 1, 4, 5)) * -1.0
    x60 += einsum(x53, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 4, 5))
    x60 += einsum(x55, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * 0.25
    x60 += einsum(x55, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 4, 5)) * -0.75
    x60 += einsum(x58, (0, 1, 2, 3), x59, (4, 3, 5, 6), (0, 4, 2, 1, 6, 5)) * -0.25
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x60, (3, 4, 6, 5, 2, 1), (0, 6)) * -1.0
    x61 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x61 += einsum(t2, (0, 1, 2, 3), x56, (4, 5, 1, 6), (4, 0, 5, 6, 2, 3))
    x62 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x62 += einsum(t2, (0, 1, 2, 3), x56, (4, 5, 6, 1), (4, 0, 5, 6, 2, 3))
    x63 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x63 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x63 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3))
    x64 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x64 += einsum(x63, (0, 1, 2, 3), t3, (1, 4, 5, 3, 6, 7), (4, 5, 0, 2, 6, 7)) * 0.5
    x65 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x65 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x65 += einsum(x33, (0, 1, 2, 3), (2, 0, 1, 3))
    x66 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x66 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x66 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * -0.5
    x67 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x67 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x67 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    x68 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x68 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x68 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x69 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x69 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.75
    x69 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x69 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x70 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x70 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x70 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x70 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x71 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x71 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x71 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2))
    x71 += einsum(v.ovov, (0, 1, 2, 3), x69, (4, 2, 3, 5), (4, 0, 5, 1)) * 2.0
    x71 += einsum(v.ovov, (0, 1, 2, 3), x70, (4, 2, 1, 5), (4, 0, 5, 3)) * -0.5
    x72 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x72 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x72 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3))
    x73 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x73 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x73 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x74 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x74 += einsum(x72, (0, 1, 2, 3), x73, (4, 5, 6, 3), (0, 1, 2, 4, 5, 6))
    x75 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x75 += einsum(x40, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * 0.5
    x75 += einsum(x40, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * -0.5
    x75 += einsum(x39, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.5
    x75 += einsum(x39, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * 0.5
    x75 += einsum(x61, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x75 += einsum(x61, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -1.0
    x75 += einsum(x62, (0, 1, 2, 3, 4, 5), (1, 3, 0, 2, 4, 5)) * -3.0
    x75 += einsum(x62, (0, 1, 2, 3, 4, 5), (1, 3, 0, 2, 5, 4))
    x75 += einsum(x64, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x75 += einsum(x64, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    x75 += einsum(x65, (0, 1, 2, 3), x66, (4, 0, 5, 3, 6, 7), (4, 5, 1, 2, 7, 6))
    x75 += einsum(x65, (0, 1, 2, 3), x67, (4, 2, 5, 6, 3, 7), (4, 5, 1, 0, 7, 6)) * 0.5
    x75 += einsum(x68, (0, 1, 2, 3), x71, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6)) * -1.0
    x75 += einsum(t1, (0, 1), x74, (2, 3, 0, 4, 5, 6), (4, 5, 2, 3, 6, 1))
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x75, (3, 5, 4, 6, 2, 1), (0, 6)) * 0.5
    x76 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x76 += einsum(t2, (0, 1, 2, 3), v.oooo, (4, 5, 6, 1), (0, 4, 5, 6, 2, 3))
    x77 = np.zeros((nocc, nvir), dtype=np.float64)
    x77 += einsum(t1, (0, 1), x22, (0, 2, 3, 1), (2, 3))
    x78 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(x77, (0, 1), t3, (2, 3, 4, 5, 1, 6), (2, 3, 4, 0, 5, 6)) * 0.16666666666666
    x79 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x79 += einsum(x77, (0, 1), t3, (2, 3, 4, 1, 5, 6), (2, 3, 4, 0, 5, 6)) * 0.16666666666666
    x80 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x80 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x81 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x81 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x81 += einsum(x80, (0, 1, 2, 3), (0, 1, 3, 2))
    x82 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum(t2, (0, 1, 2, 3), x81, (4, 5, 6, 1), (0, 4, 5, 6, 2, 3)) * 0.25
    x83 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x83 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x83 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x84 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x84 += einsum(v.oooo, (0, 1, 2, 3), (0, 2, 1, 3))
    x84 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x84 += einsum(x80, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x84 += einsum(x80, (0, 1, 2, 3), (3, 0, 1, 2))
    x85 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x85 += einsum(x7, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x85 += einsum(x19, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.49999999999997996
    x86 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 6, 1, 3, 7), (4, 5, 0, 6, 7, 2)) * 0.49999999999997996
    x86 += einsum(x76, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * 0.25
    x86 += einsum(x76, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -0.25
    x86 += einsum(x76, (0, 1, 2, 3, 4, 5), (3, 0, 2, 1, 4, 5)) * -0.25
    x86 += einsum(x76, (0, 1, 2, 3, 4, 5), (3, 0, 2, 1, 5, 4)) * 0.25
    x86 += einsum(x78, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x86 += einsum(x78, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 5, 4))
    x86 += einsum(x78, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4))
    x86 += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x86 += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 6.999999999999999
    x86 += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 4, 5))
    x86 += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 5, 4)) * -1.0
    x86 += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x86 += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * -1.0
    x86 += einsum(x82, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x86 += einsum(x82, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4))
    x86 += einsum(t2, (0, 1, 2, 3), x83, (4, 5, 6, 3), (0, 1, 5, 4, 2, 6)) * -1.0
    x86 += einsum(t2, (0, 1, 2, 3), x84, (0, 4, 5, 6), (4, 1, 6, 5, 2, 3)) * -0.5
    x86 += einsum(t1, (0, 1), x85, (2, 3, 4, 5, 0, 6), (2, 3, 5, 4, 6, 1))
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x86, (3, 4, 6, 5, 2, 1), (0, 6)) * -1.0
    x87 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x87 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x87 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x88 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x88 += einsum(t1, (0, 1), x87, (2, 3, 1, 4), (0, 2, 3, 4))
    x89 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x89 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x89 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x89 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x89 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    x89 += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x90 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x90 += einsum(v.ooov, (0, 1, 2, 3), x73, (4, 5, 6, 3), (0, 1, 2, 4, 5, 6))
    x91 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x91 += einsum(x33, (0, 1, 2, 3), x68, (4, 5, 3, 6), (0, 1, 2, 4, 5, 6))
    x92 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x92 += einsum(x90, (0, 1, 2, 3, 4, 5), (3, 4, 1, 0, 2, 5)) * -1.0
    x92 += einsum(x90, (0, 1, 2, 3, 4, 5), (3, 4, 1, 2, 0, 5))
    x92 += einsum(x91, (0, 1, 2, 3, 4, 5), (3, 4, 0, 2, 1, 5)) * -1.0
    x92 += einsum(x91, (0, 1, 2, 3, 4, 5), (3, 4, 0, 1, 2, 5))
    x93 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x93 += einsum(x68, (0, 1, 2, 3), x89, (4, 5, 6, 2), (0, 1, 5, 4, 3, 6))
    x93 += einsum(t1, (0, 1), x92, (2, 3, 4, 5, 0, 6), (2, 3, 5, 4, 6, 1)) * -1.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x93, (3, 5, 6, 4, 1, 2), (0, 6)) * 0.5
    x94 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x94 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x94 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x95 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x95 += einsum(t1, (0, 1), x94, (2, 1, 3, 4), (0, 2, 3, 4))
    x96 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x96 += einsum(t2, (0, 1, 2, 3), x95, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6)) * -1.0
    x97 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(t2, (0, 1, 2, 3), x95, (4, 5, 6, 2), (0, 1, 4, 5, 3, 6)) * -3.0
    x98 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x98 += einsum(x34, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x98 += einsum(x34, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x99 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 += einsum(t1, (0, 1), x98, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x100 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x100 += einsum(t2, (0, 1, 2, 3), x33, (4, 5, 6, 2), (4, 0, 1, 6, 5, 3))
    x101 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x101 += einsum(x100, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x101 += einsum(x100, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x102 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(t1, (0, 1), x101, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * 3.0
    x103 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x103 += einsum(x96, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x103 += einsum(x96, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x103 += einsum(x97, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x103 += einsum(x97, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -0.3333333333333333
    x103 += einsum(x99, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    x103 += einsum(x99, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    x103 += einsum(x102, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    x103 += einsum(x102, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * 0.3333333333333333
    x103 += einsum(t2, (0, 1, 2, 3), x26, (4, 5, 6, 2), (0, 4, 1, 5, 3, 6)) * 2.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x103, (5, 3, 4, 6, 1, 2), (0, 6)) * 0.5
    x104 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x104 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x104 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x104 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3))
    x104 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x105 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x105 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x105 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3))
    x106 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x106 += einsum(x40, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x106 += einsum(x40, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4))
    x106 += einsum(x61, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 4, 5)) * -2.0
    x106 += einsum(x61, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 5, 4)) * 2.0
    x106 += einsum(x45, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 4, 5)) * -1.0
    x106 += einsum(x45, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 5, 4))
    x106 += einsum(x104, (0, 1, 2, 3), t3, (4, 2, 5, 6, 3, 7), (4, 5, 1, 0, 6, 7)) * -1.0
    x106 += einsum(x105, (0, 1, 2, 3), t3, (2, 4, 5, 6, 3, 7), (5, 4, 1, 0, 6, 7))
    x106 += einsum(x54, (0, 1, 2, 3), x68, (4, 5, 3, 6), (4, 5, 1, 0, 2, 6)) * -1.0
    x106 += einsum(t1, (0, 1), x74, (2, 0, 3, 4, 5, 6), (4, 5, 3, 2, 1, 6)) * -2.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x106, (3, 5, 6, 4, 0, 2), (1, 6)) * -0.25
    x107 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum(t2, (0, 1, 2, 3), x80, (4, 5, 1, 6), (4, 0, 5, 6, 2, 3))
    x108 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x108 += einsum(t2, (0, 1, 2, 3), x80, (4, 5, 6, 1), (4, 0, 5, 6, 2, 3))
    x109 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x109 += einsum(x76, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -2.0
    x109 += einsum(x76, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * 2.0
    x109 += einsum(x76, (0, 1, 2, 3, 4, 5), (3, 0, 2, 1, 4, 5)) * 6.0
    x109 += einsum(x76, (0, 1, 2, 3, 4, 5), (3, 0, 2, 1, 5, 4)) * -2.0
    x109 += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x109 += einsum(x107, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x109 += einsum(x107, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x109 += einsum(x107, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    x109 += einsum(x108, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x109 += einsum(x108, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x109 += einsum(x108, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * 5.0
    x109 += einsum(x108, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x109, (4, 3, 5, 6, 2, 1), (0, 6)) * -0.25
    x110 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 0, 5), (1, 4, 3, 5))
    x111 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x111 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x111 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x111 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x112 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x112 += einsum(x110, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x112 += einsum(v.ovov, (0, 1, 2, 3), x111, (4, 2, 3, 5), (4, 0, 5, 1))
    x113 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x113 += einsum(t1, (0, 1), x100, (2, 3, 4, 0, 5, 6), (3, 4, 2, 5, 1, 6)) * 2.0
    x113 += einsum(x65, (0, 1, 2, 3), t3, (0, 4, 5, 6, 3, 7), (4, 5, 1, 2, 6, 7))
    x113 += einsum(t2, (0, 1, 2, 3), x112, (4, 5, 6, 2), (0, 1, 4, 5, 6, 3)) * -1.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x113, (4, 5, 3, 6, 0, 2), (1, 6)) * 0.5
    x114 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x114 += einsum(t2, (0, 1, 2, 3), x57, (4, 5, 1, 6), (5, 4, 0, 6, 2, 3))
    x115 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x115 += einsum(x61, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 3.0
    x115 += einsum(x61, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x115 += einsum(x62, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x115 += einsum(x62, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x115 += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 4, 5)) * 3.0
    x115 += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 2, 3, 1, 5, 4)) * -1.0
    x115 += einsum(x114, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 4, 5)) * -1.0
    x115 += einsum(x114, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 5, 4))
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x115, (3, 5, 6, 4, 2, 1), (0, 6)) * 0.5
    x116 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x116 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x116 += einsum(x32, (0, 1, 2, 3), (0, 1, 3, 2))
    x116 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x117 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x117 += einsum(x116, (0, 1, 2, 3), x68, (4, 5, 3, 6), (4, 5, 1, 0, 6, 2)) * -1.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x117, (3, 5, 6, 4, 0, 2), (1, 6)) * -0.5
    x118 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x118 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x118 += einsum(x110, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x118 += einsum(v.ovov, (0, 1, 2, 3), x111, (4, 2, 3, 5), (4, 0, 5, 1)) * 0.5
    x119 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x119 += einsum(x2, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.24999999999999
    x119 += einsum(t2, (0, 1, 2, 3), x118, (4, 5, 6, 2), (5, 1, 0, 4, 3, 6))
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x119, (6, 3, 4, 5, 0, 2), (1, 6)) * -1.0
    x120 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x120 += einsum(x10, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x120 += einsum(x19, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -0.4999999999999799
    x121 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x121 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 6, 3, 1, 7), (5, 4, 6, 0, 2, 7))
    x121 += einsum(x77, (0, 1), t3, (2, 3, 4, 5, 1, 6), (3, 2, 4, 0, 5, 6)) * 1.0000000000000002
    x121 += einsum(t1, (0, 1), x120, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 1, 6)) * 2.0000000000000804
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x121, (4, 3, 5, 6, 0, 2), (1, 6)) * -0.49999999999997996
    x122 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x122 += einsum(x62, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x122 += einsum(x62, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x122 += einsum(x114, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 4, 5)) * -1.0
    x122 += einsum(x114, (0, 1, 2, 3, 4, 5), (1, 2, 3, 0, 5, 4))
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x122, (3, 5, 6, 4, 2, 0), (1, 6)) * -0.5
    x123 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x123 += einsum(x76, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x123 += einsum(x76, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 5, 4)) * -1.0
    x123 += einsum(x108, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x123 += einsum(x108, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x123, (4, 3, 5, 6, 2, 0), (1, 6)) * -0.5
    x124 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x124 += einsum(v.vvvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x124 += einsum(v.vvvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x125 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x125 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 5, 6, 1, 0), (6, 4, 5, 2))
    x126 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x126 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x126 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x126 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x127 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x127 += einsum(t1, (0, 1), l2, (2, 3, 0, 4), (4, 3, 2, 1))
    x127 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3))
    x127 += einsum(x126, (0, 1, 2, 3), l3, (2, 4, 5, 6, 0, 1), (6, 4, 5, 3)) * -0.5
    l1new += einsum(x124, (0, 1, 2, 3), x127, (4, 0, 2, 3), (1, 4)) * -0.5
    x128 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x128 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 0, 7, 2), (3, 6, 1, 7))
    x129 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x129 += einsum(t1, (0, 1), l3, (1, 2, 3, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x130 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x130 += einsum(t2, (0, 1, 2, 3), x129, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x130, (4, 2, 5, 1), (3, 5, 4, 0))
    x131 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x131 += einsum(t2, (0, 1, 2, 3), x129, (4, 1, 0, 5, 3, 6), (4, 5, 6, 2))
    x132 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x132 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.2
    x132 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x132 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 0.2
    x132 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.2
    x132 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.2
    x132 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -0.2
    x133 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x133 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x133 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x133 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x133 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * 2.0
    x134 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x134 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x134 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x134 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x134 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x135 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x135 += einsum(t1, (0, 1), l3, (2, 1, 3, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    l3new += einsum(x33, (0, 1, 2, 3), x135, (4, 0, 5, 1, 6, 7), (6, 3, 7, 4, 2, 5))
    x136 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x136 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x136 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x137 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x137 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 5, 1, 6), (5, 6, 0, 4))
    x138 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x138 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 1), (5, 6, 0, 4))
    x139 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x139 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    x140 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x140 += einsum(x68, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 0), (5, 6, 1, 4)) * 0.25
    x141 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x141 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x141 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0))
    x142 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x142 += einsum(x137, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x142 += einsum(x138, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x142 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3))
    x142 += einsum(x139, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x142 += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x142 += einsum(x140, (0, 1, 2, 3), (1, 0, 2, 3))
    x142 += einsum(x73, (0, 1, 2, 3), x141, (4, 5, 0, 2, 6, 3), (4, 5, 1, 6)) * -0.25
    x143 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x143 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    x143 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 5), (2, 4, 1, 5))
    x143 += einsum(x128, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x143 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7)) * 0.25
    x143 += einsum(x130, (0, 1, 2, 3), (0, 1, 3, 2))
    x143 += einsum(x131, (0, 1, 2, 3), (0, 1, 3, 2))
    x143 += einsum(l3, (0, 1, 2, 3, 4, 5), x132, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 1.25
    x143 += einsum(l3, (0, 1, 2, 3, 4, 5), x133, (6, 5, 3, 7, 2, 1), (4, 6, 0, 7)) * 0.25
    x143 += einsum(x134, (0, 1, 2, 3), x135, (4, 0, 1, 5, 2, 6), (4, 5, 3, 6)) * -0.5
    x143 += einsum(x73, (0, 1, 2, 3), x135, (0, 4, 1, 5, 2, 6), (4, 5, 3, 6)) * -1.0
    x143 += einsum(x136, (0, 1, 2, 3), x68, (1, 4, 2, 5), (0, 4, 3, 5)) * -1.0
    x143 += einsum(t1, (0, 1), x142, (2, 0, 3, 4), (2, 3, 1, 4)) * 2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x143, (4, 0, 2, 3), (1, 4)) * -1.0
    x144 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x144 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 1, 5, 6), (5, 6, 0, 4))
    x145 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x145 += einsum(l2, (0, 1, 2, 3), t3, (4, 3, 5, 0, 1, 6), (2, 4, 5, 6))
    x146 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x146 += einsum(t1, (0, 1), x139, (2, 3, 4, 1), (2, 3, 4, 0))
    x147 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x147 += einsum(t1, (0, 1), x146, (2, 0, 3, 4), (2, 3, 4, 1))
    x148 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x148 += einsum(t1, (0, 1), x146, (0, 2, 3, 4), (2, 3, 4, 1))
    x149 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x149 += einsum(t1, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    l2new += einsum(x54, (0, 1, 2, 3), x149, (4, 5, 0, 1, 6, 2), (6, 3, 4, 5))
    l3new += einsum(v.ooov, (0, 1, 2, 3), x149, (4, 1, 5, 0, 6, 7), (6, 3, 7, 4, 2, 5))
    x150 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x150 += einsum(t1, (0, 1), x149, (2, 3, 4, 5, 1, 6), (2, 3, 4, 0, 5, 6))
    x151 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x151 += einsum(t2, (0, 1, 2, 3), x150, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    x152 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x152 += einsum(t1, (0, 1), x129, (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 0, 6))
    x153 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x153 += einsum(x111, (0, 1, 2, 3), x152, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    x154 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x154 += einsum(x148, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x154 += einsum(x151, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x154 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3))
    x155 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x155 += einsum(t2, (0, 1, 2, 3), x152, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    x156 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x156 += einsum(x68, (0, 1, 2, 3), x152, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    x157 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.2
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.2
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -0.2
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * 0.2
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * -0.2
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    x157 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -0.2
    x158 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x158 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x158 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2))
    x159 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x159 += einsum(t1, (0, 1), x158, (2, 3, 4, 5, 1, 6), (2, 3, 4, 0, 5, 6)) * -1.0
    x160 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x160 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x160 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x161 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x161 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x161 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1))
    x161 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    x161 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x162 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x162 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x162 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x163 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x163 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x163 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 3.0
    x163 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x164 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x164 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x164 += einsum(x126, (0, 1, 2, 3), l3, (2, 4, 5, 6, 0, 1), (6, 4, 5, 3)) * -1.0
    x165 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x165 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 5, 1, 6), (5, 6, 0, 4))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x165, (4, 1, 0, 5), (5, 3, 4, 2)) * -1.0
    x166 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x166 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new += einsum(x166, (0, 1, 2, 3), x33, (1, 2, 4, 5), (3, 5, 0, 4))
    x167 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x167 += einsum(x73, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 0), (5, 6, 1, 4)) * 0.3333333333333333
    x168 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x168 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.6666666666666665
    x168 += einsum(x167, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x169 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x169 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -3.0
    x169 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    x169 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * 3.0
    x169 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * 3.0
    x170 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x170 += einsum(x137, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x170 += einsum(x165, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x170 += einsum(x168, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x170 += einsum(x168, (0, 1, 2, 3), (1, 0, 2, 3))
    x170 += einsum(x73, (0, 1, 2, 3), x169, (4, 0, 5, 3, 2, 6), (4, 5, 1, 6)) * 0.3333333333333333
    x171 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x171 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x171 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x172 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x172 += einsum(x73, (0, 1, 2, 3), l3, (2, 4, 3, 5, 6, 0), (5, 6, 1, 4)) * 0.5
    x173 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x173 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x173 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * 3.0
    x174 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x174 += einsum(x139, (0, 1, 2, 3), (1, 0, 2, 3))
    x174 += einsum(x172, (0, 1, 2, 3), (1, 0, 2, 3))
    x174 += einsum(t2, (0, 1, 2, 3), x173, (4, 5, 1, 6, 2, 3), (4, 5, 0, 6)) * 0.25
    x175 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x175 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x175 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x175 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x176 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x176 += einsum(t2, (0, 1, 2, 3), l3, (2, 4, 5, 6, 1, 0), (6, 4, 5, 3))
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x176, (4, 5, 3, 1), (2, 5, 4, 0))
    x177 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x177 += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3))
    x177 += einsum(x68, (0, 1, 2, 3), l3, (3, 4, 5, 0, 6, 1), (6, 4, 5, 2)) * -5.0
    x178 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x178 += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3))
    x178 += einsum(x68, (0, 1, 2, 3), l3, (3, 4, 5, 0, 6, 1), (6, 4, 5, 2)) * -0.1111111111111111
    x179 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x179 += einsum(l2, (0, 1, 2, 3), x73, (4, 5, 0, 1), (2, 3, 4, 5)) * 0.5
    x180 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x180 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    x181 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x181 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 0), (5, 6, 1, 4))
    x182 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x182 += einsum(t1, (0, 1), x181, (2, 3, 4, 1), (2, 3, 0, 4))
    x183 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x183 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x183 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x184 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x184 += einsum(l3, (0, 1, 2, 3, 4, 5), x183, (6, 7, 5, 1, 0, 2), (3, 4, 6, 7)) * 0.16666666666666
    x185 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x185 += einsum(x182, (0, 1, 2, 3), (0, 1, 2, 3))
    x185 += einsum(x184, (0, 1, 2, 3), (0, 1, 2, 3))
    x186 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x186 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 0), (5, 6, 1, 4))
    x187 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x187 += einsum(t1, (0, 1), x186, (2, 3, 4, 1), (2, 3, 0, 4))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x187, (4, 5, 0, 2), (1, 3, 4, 5))
    x188 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x188 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x188 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x188 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x188 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 3.0
    x189 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x189 += einsum(l3, (0, 1, 2, 3, 4, 5), x188, (6, 7, 4, 1, 0, 2), (3, 5, 6, 7)) * 0.16666666666666
    x190 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x190 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x190 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1))
    x191 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x191 += einsum(x165, (0, 1, 2, 3), (0, 1, 2, 3))
    x191 += einsum(x68, (0, 1, 2, 3), x190, (4, 5, 0, 2, 6, 3), (5, 4, 1, 6)) * -0.5
    x192 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x192 += einsum(x179, (0, 1, 2, 3), (0, 1, 3, 2))
    x192 += einsum(x179, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x192 += einsum(x180, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.16666666666662
    x192 += einsum(x180, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.16666666666666
    x192 += einsum(x185, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x192 += einsum(x185, (0, 1, 2, 3), (1, 0, 2, 3))
    x192 += einsum(x187, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x192 += einsum(x187, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x192 += einsum(x189, (0, 1, 2, 3), (0, 1, 2, 3))
    x192 += einsum(t1, (0, 1), x191, (2, 3, 4, 1), (2, 3, 0, 4)) * 2.0
    x193 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x193 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x193 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x194 = np.zeros((nocc, nocc), dtype=np.float64)
    x194 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    x195 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x195 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x195 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.14285714285714288
    x195 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.14285714285714288
    x195 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.14285714285714288
    x195 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 0.14285714285714288
    x195 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 0.14285714285714288
    x196 = np.zeros((nocc, nocc), dtype=np.float64)
    x196 += einsum(l3, (0, 1, 2, 3, 4, 5), x195, (6, 4, 5, 0, 1, 2), (3, 6)) * 0.58333333333331
    x197 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x197 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x197 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x197 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x197 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * 3.0
    x198 = np.zeros((nocc, nocc), dtype=np.float64)
    x198 += einsum(l3, (0, 1, 2, 3, 4, 5), x197, (6, 5, 3, 0, 1, 2), (4, 6)) * 0.08333333333333
    x199 = np.zeros((nocc, nocc), dtype=np.float64)
    x199 += einsum(x136, (0, 1, 2, 3), x68, (1, 4, 2, 3), (4, 0)) * 0.5
    x200 = np.zeros((nocc, nocc), dtype=np.float64)
    x200 += einsum(x194, (0, 1), (0, 1))
    x200 += einsum(x196, (0, 1), (0, 1))
    x200 += einsum(x198, (0, 1), (0, 1))
    x200 += einsum(x199, (0, 1), (1, 0)) * -1.0
    x201 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x201 += einsum(x137, (0, 1, 2, 3), (0, 2, 1, 3)) * 4.0
    x201 += einsum(x144, (0, 1, 2, 3), (0, 2, 1, 3)) * 4.0
    x201 += einsum(x145, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.0
    x201 += einsum(x139, (0, 1, 2, 3), (0, 2, 1, 3)) * 8.0
    x201 += einsum(x139, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    x201 += einsum(x147, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x201 += einsum(x147, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x201 += einsum(x154, (0, 1, 2, 3), (0, 1, 2, 3))
    x201 += einsum(x154, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x201 += einsum(x155, (0, 1, 2, 3), (0, 1, 2, 3)) * -5.0
    x201 += einsum(x155, (0, 1, 2, 3), (0, 2, 1, 3))
    x201 += einsum(x156, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x201 += einsum(x156, (0, 1, 2, 3), (0, 2, 1, 3)) * 3.0
    x201 += einsum(x129, (0, 1, 2, 3, 4, 5), x157, (2, 6, 1, 5, 7, 4), (0, 3, 6, 7)) * 5.0
    x201 += einsum(x159, (0, 1, 2, 3, 4, 5), x160, (6, 2, 0, 7, 4, 5), (1, 3, 6, 7)) * -1.0
    x201 += einsum(x135, (0, 1, 2, 3, 4, 5), x67, (0, 6, 2, 4, 7, 5), (1, 3, 6, 7))
    x201 += einsum(x129, (0, 1, 2, 3, 4, 5), x67, (0, 6, 2, 5, 7, 4), (1, 3, 6, 7))
    x201 += einsum(x73, (0, 1, 2, 3), x161, (4, 5, 0, 2, 3, 6), (4, 1, 5, 6)) * -2.0
    x201 += einsum(x162, (0, 1, 2, 3), x163, (1, 4, 5, 2, 3, 6), (0, 5, 4, 6))
    x201 += einsum(x164, (0, 1, 2, 3), x73, (4, 5, 1, 2), (0, 4, 5, 3)) * 0.5
    x201 += einsum(x170, (0, 1, 2, 3), x171, (1, 4, 3, 5), (0, 2, 4, 5)) * 3.0
    x201 += einsum(x174, (0, 1, 2, 3), x175, (4, 0, 5, 3), (1, 2, 4, 5)) * 4.0
    x201 += einsum(t2, (0, 1, 2, 3), x177, (4, 2, 3, 5), (4, 0, 1, 5)) * -0.5
    x201 += einsum(t2, (0, 1, 2, 3), x178, (4, 3, 2, 5), (4, 0, 1, 5)) * 4.5
    x201 += einsum(t1, (0, 1), x192, (2, 0, 3, 4), (2, 3, 4, 1)) * -2.0
    x201 += einsum(l1, (0, 1), x193, (2, 3, 0, 4), (1, 2, 3, 4)) * 6.0
    x201 += einsum(t1, (0, 1), x200, (2, 3), (2, 3, 0, 1)) * 8.0
    l1new += einsum(v.ovov, (0, 1, 2, 3), x201, (4, 2, 0, 1), (3, 4)) * -0.25
    x202 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.2
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * 0.2
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -0.2
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -0.2
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -0.2
    x202 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * 0.2
    x203 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x203 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x203 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -1.0
    x204 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x204 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x204 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x205 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x205 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x205 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x206 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x206 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * 3.0
    x206 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x206 += einsum(l3, (0, 1, 2, 3, 4, 5), x202, (4, 6, 5, 2, 7, 1), (3, 6, 0, 7)) * 2.5
    x206 += einsum(x203, (0, 1, 2, 3, 4, 5), x204, (6, 2, 0, 7, 5, 4), (1, 6, 3, 7)) * 0.5
    x206 += einsum(l3, (0, 1, 2, 3, 4, 5), x67, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7)) * 0.5
    x206 += einsum(l3, (0, 1, 2, 3, 4, 5), x67, (3, 6, 5, 2, 7, 1), (4, 6, 0, 7)) * 0.5
    x206 += einsum(x162, (0, 1, 2, 3), x205, (1, 4, 5, 2), (0, 4, 3, 5)) * 4.0
    x206 += einsum(l2, (0, 1, 2, 3), x175, (4, 3, 5, 1), (2, 4, 0, 5)) * 2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x206, (4, 0, 3, 1), (2, 4)) * 0.5
    x207 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x207 += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x207 += einsum(x135, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x207 += einsum(x135, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    x208 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x208 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x208 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x209 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x209 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 0), (5, 6, 1, 4))
    x210 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x210 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3))
    x210 += einsum(x209, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x211 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x211 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 5, 6, 0), (5, 6, 1, 4))
    x212 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x212 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x212 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    x213 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x213 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x213 += einsum(x137, (0, 1, 2, 3), (0, 1, 2, 3))
    x213 += einsum(x210, (0, 1, 2, 3), (0, 1, 2, 3))
    x213 += einsum(x210, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x213 += einsum(x211, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x213 += einsum(x211, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x213 += einsum(x73, (0, 1, 2, 3), x212, (4, 5, 0, 2, 6, 3), (5, 4, 1, 6)) * -0.5
    x214 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x214 += einsum(x131, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x214 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x214 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0))
    x214 += einsum(x68, (0, 1, 2, 3), x207, (0, 4, 1, 5, 6, 3), (4, 5, 6, 2)) * -1.0
    x214 += einsum(x208, (0, 1, 2, 3), x135, (4, 1, 0, 5, 2, 6), (4, 5, 6, 3))
    x214 += einsum(t1, (0, 1), x213, (2, 0, 3, 4), (2, 3, 4, 1)) * 2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x214, (4, 0, 3, 1), (2, 4)) * 0.5
    x215 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x215 += einsum(x129, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x215 += einsum(x129, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    x216 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x216 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x216 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x216 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x217 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x217 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.2
    x217 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x217 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 0.2
    x218 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x218 += einsum(x73, (0, 1, 2, 3), l3, (3, 4, 5, 0, 6, 1), (6, 4, 5, 2))
    x219 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x219 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x219 += einsum(x134, (0, 1, 2, 3), l3, (2, 4, 5, 6, 0, 1), (6, 4, 5, 3)) * -1.0
    x219 += einsum(x218, (0, 1, 2, 3), (0, 1, 2, 3))
    x220 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x220 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x220 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.2
    x221 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x221 += einsum(x73, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 0), (5, 6, 1, 4))
    x222 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x222 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x222 += einsum(x221, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x223 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x223 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -2.9999999999999996
    x223 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    x223 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * 2.9999999999999996
    x223 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * 2.9999999999999996
    x224 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x224 += einsum(x137, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.999999999999999
    x224 += einsum(x165, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x224 += einsum(x222, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x224 += einsum(x222, (0, 1, 2, 3), (1, 0, 2, 3))
    x224 += einsum(x73, (0, 1, 2, 3), x223, (4, 0, 5, 3, 2, 6), (4, 5, 1, 6))
    x225 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x225 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x225 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -0.5
    x225 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * 1.4999999999999998
    x226 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x226 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * 2.9999999999999996
    x226 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * 5.999999999999999
    x226 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2)) * -1.0
    x227 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x227 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x227 += einsum(t2, (0, 1, 2, 3), x225, (4, 5, 0, 6, 3, 2), (4, 5, 1, 6)) * 2.0
    x227 += einsum(t2, (0, 1, 2, 3), x226, (0, 4, 5, 3, 6, 2), (4, 5, 1, 6)) * -1.0
    x228 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x228 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x228 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * 2.9999999999999996
    x229 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x229 += einsum(x139, (0, 1, 2, 3), (1, 0, 2, 3))
    x229 += einsum(x172, (0, 1, 2, 3), (1, 0, 2, 3))
    x229 += einsum(t2, (0, 1, 2, 3), x228, (4, 5, 1, 6, 2, 3), (4, 5, 0, 6)) * 0.25
    x230 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x230 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 1, 0), (2, 3, 4, 5))
    x231 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x231 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    x232 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x232 += einsum(x68, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 0), (5, 6, 1, 4))
    x233 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x233 += einsum(t1, (0, 1), x232, (2, 3, 4, 1), (0, 2, 3, 4)) * -1.0
    x234 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x234 += einsum(x184, (0, 1, 2, 3), (0, 1, 2, 3))
    x234 += einsum(x233, (0, 1, 2, 3), (1, 2, 0, 3))
    x235 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x235 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x235 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 0, 1)) * -1.0
    x236 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x236 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x236 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 2, 1))
    x237 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x237 += einsum(x73, (0, 1, 2, 3), x235, (4, 5, 0, 2, 6, 3), (5, 4, 1, 6))
    x237 += einsum(t2, (0, 1, 2, 3), x236, (4, 5, 1, 6, 2, 3), (4, 5, 0, 6)) * -2.0
    x238 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x238 += einsum(x230, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    x238 += einsum(x230, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    x238 += einsum(x231, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.5
    x238 += einsum(x231, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x238 += einsum(x180, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.16666666666666
    x238 += einsum(x180, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.16666666666662
    x238 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x238 += einsum(x234, (0, 1, 2, 3), (1, 0, 2, 3))
    x238 += einsum(x189, (0, 1, 2, 3), (0, 1, 2, 3))
    x238 += einsum(t1, (0, 1), x237, (2, 3, 4, 1), (3, 2, 0, 4)) * -1.0
    x239 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x239 += einsum(x145, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.4
    x239 += einsum(t3, (0, 1, 2, 3, 4, 5), x135, (6, 1, 2, 7, 3, 5), (6, 7, 0, 4)) * 0.4
    x239 += einsum(t3, (0, 1, 2, 3, 4, 5), x129, (0, 6, 2, 7, 4, 5), (6, 7, 1, 3)) * 0.4
    x239 += einsum(t3, (0, 1, 2, 3, 4, 5), x135, (0, 6, 2, 7, 3, 5), (6, 7, 1, 4)) * 0.2
    x239 += einsum(x215, (0, 1, 2, 3, 4, 5), x216, (6, 2, 0, 7, 4, 5), (1, 3, 6, 7)) * -0.2
    x239 += einsum(x129, (0, 1, 2, 3, 4, 5), x217, (6, 1, 2, 7, 5, 4), (0, 3, 6, 7))
    x239 += einsum(x162, (0, 1, 2, 3), x204, (1, 4, 5, 2, 3, 6), (0, 5, 4, 6)) * 0.2
    x239 += einsum(x219, (0, 1, 2, 3), x73, (4, 5, 2, 1), (0, 4, 5, 3)) * -0.1
    x239 += einsum(x220, (0, 1, 2, 3), t3, (1, 4, 5, 3, 2, 6), (0, 5, 4, 6)) * -1.0
    x239 += einsum(x224, (0, 1, 2, 3), x68, (1, 4, 3, 5), (0, 2, 4, 5)) * 0.1
    x239 += einsum(t2, (0, 1, 2, 3), x227, (4, 1, 5, 2), (4, 5, 0, 3)) * 0.1
    x239 += einsum(t2, (0, 1, 2, 3), x229, (1, 4, 5, 3), (4, 5, 0, 2)) * 0.8
    x239 += einsum(t1, (0, 1), x238, (2, 0, 3, 4), (2, 3, 4, 1)) * -0.4
    x239 += einsum(l1, (0, 1), x73, (2, 3, 0, 4), (1, 2, 3, 4)) * -0.4
    x239 += einsum(t1, (0, 1), x200, (2, 3), (2, 3, 0, 1)) * 0.8
    l1new += einsum(v.ovov, (0, 1, 2, 3), x239, (4, 2, 0, 3), (1, 4)) * 1.25
    x240 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x240 += einsum(t1, (0, 1), l2, (2, 3, 4, 0), (4, 2, 3, 1))
    x241 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x241 += einsum(x240, (0, 1, 2, 3), (0, 2, 1, 3))
    x241 += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x241 += einsum(x73, (0, 1, 2, 3), l3, (3, 4, 5, 0, 6, 1), (6, 4, 5, 2)) * -1.5
    l1new += einsum(v.vvvv, (0, 1, 2, 3), x241, (4, 1, 2, 3), (0, 4)) * -0.5
    x242 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x242 += einsum(x240, (0, 1, 2, 3), (0, 2, 1, 3))
    x242 += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.8333333333333334
    x242 += einsum(x73, (0, 1, 2, 3), l3, (3, 4, 5, 0, 6, 1), (6, 4, 5, 2)) * -0.16666666666666666
    l1new += einsum(v.vvvv, (0, 1, 2, 3), x242, (4, 3, 1, 2), (0, 4)) * 1.5
    x243 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x243 += einsum(f.ov, (0, 1), t2, (2, 3, 1, 4), (0, 2, 3, 4))
    x244 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x244 += einsum(f.ov, (0, 1), t2, (2, 3, 4, 1), (0, 2, 3, 4))
    x245 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x245 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x246 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x246 += einsum(t1, (0, 1), x80, (2, 3, 4, 0), (2, 3, 4, 1))
    x247 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x247 += einsum(x24, (0, 1, 2, 3), t3, (4, 5, 0, 2, 6, 3), (4, 5, 1, 6)) * 3.0
    x248 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x248 += einsum(x77, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4)) * 12.0
    x249 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x249 += einsum(x245, (0, 1, 2, 3), (0, 1, 2, 3)) * 6.0
    x249 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x249 += einsum(x247, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x249 += einsum(x248, (0, 1, 2, 3), (0, 1, 2, 3))
    x250 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x250 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 3, 5, 2), (0, 1, 4, 5))
    x251 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x251 += einsum(t1, (0, 1), x80, (2, 3, 0, 4), (2, 3, 4, 1))
    x252 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x252 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x252 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x253 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x253 += einsum(v.ovov, (0, 1, 2, 3), x252, (4, 5, 2, 6, 3, 1), (0, 4, 5, 6)) * 2.0
    x254 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x254 += einsum(x77, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4)) * 4.0
    x255 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x255 += einsum(x250, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x255 += einsum(x251, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x255 += einsum(x253, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x255 += einsum(x254, (0, 1, 2, 3), (0, 1, 2, 3))
    x256 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x256 += einsum(t1, (0, 1), x32, (2, 3, 4, 1), (2, 0, 3, 4))
    x257 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x257 += einsum(t1, (0, 1), x57, (2, 3, 4, 0), (2, 3, 4, 1))
    x258 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x258 += einsum(x256, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x258 += einsum(x257, (0, 1, 2, 3), (0, 1, 2, 3)) * -8.0
    x259 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x259 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 2, 6, 1, 3), (4, 5, 0, 6))
    x260 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x260 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x260 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x260 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.3333333333333333
    x261 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x261 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x261 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x262 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x262 += einsum(v.oooo, (0, 1, 2, 3), (0, 2, 3, 1)) * 2.0
    x262 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x262 += einsum(x56, (0, 1, 2, 3), (2, 0, 3, 1)) * 2.0
    x262 += einsum(x56, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x263 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x263 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * 8.0
    x263 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -4.0
    x263 += einsum(x243, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    x263 += einsum(x243, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x263 += einsum(x244, (0, 1, 2, 3), (1, 2, 0, 3)) * -2.0
    x263 += einsum(x244, (0, 1, 2, 3), (2, 1, 0, 3)) * 2.0
    x263 += einsum(x249, (0, 1, 2, 3), (0, 1, 2, 3))
    x263 += einsum(x249, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x263 += einsum(x255, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x263 += einsum(x255, (0, 1, 2, 3), (1, 0, 2, 3))
    x263 += einsum(x258, (0, 1, 2, 3), (0, 1, 2, 3))
    x263 += einsum(x258, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x263 += einsum(x259, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x263 += einsum(x259, (0, 1, 2, 3), (1, 0, 2, 3)) * 6.0
    x263 += einsum(x111, (0, 1, 2, 3), x72, (4, 5, 1, 2), (4, 0, 5, 3)) * -4.0
    x263 += einsum(x260, (0, 1, 2, 3), x72, (4, 1, 5, 2), (4, 0, 5, 3)) * 12.0
    x263 += einsum(t1, (0, 1), x261, (2, 3, 1, 4), (0, 3, 2, 4)) * 8.0
    x263 += einsum(t1, (0, 1), x262, (0, 2, 3, 4), (2, 4, 3, 1)) * -4.0
    l1new += einsum(l2, (0, 1, 2, 3), x263, (2, 3, 4, 1), (0, 4)) * -0.25
    x264 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x264 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x264 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    x264 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -1.0
    x265 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x265 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x265 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x266 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x266 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x266 += einsum(x137, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x266 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x266 += einsum(x139, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.0
    x266 += einsum(x68, (0, 1, 2, 3), x264, (0, 4, 5, 2, 6, 3), (4, 5, 1, 6)) * -1.0
    x266 += einsum(x265, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 0), (5, 6, 1, 4)) * 3.0
    l1new += einsum(v.oovv, (0, 1, 2, 3), x266, (4, 0, 1, 3), (2, 4)) * 0.5
    x267 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x267 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x267 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x267 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x267 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3))
    x268 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x268 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x268 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x268 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x268 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x269 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x269 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x269 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x270 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x270 += einsum(x56, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x270 += einsum(x56, (0, 1, 2, 3), (0, 3, 2, 1))
    x271 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x271 += einsum(t2, (0, 1, 2, 3), x267, (4, 5, 1, 3), (4, 0, 5, 2)) * 2.0
    x271 += einsum(t2, (0, 1, 2, 3), x268, (4, 5, 1, 2), (4, 0, 5, 3))
    x271 += einsum(t1, (0, 1), x269, (2, 3, 1, 4), (0, 3, 2, 4)) * -1.0
    x271 += einsum(t1, (0, 1), x270, (2, 0, 3, 4), (2, 3, 4, 1)) * 2.0
    l1new += einsum(l2, (0, 1, 2, 3), x271, (3, 2, 4, 1), (0, 4))
    x272 = np.zeros((nvir, nvir), dtype=np.float64)
    x272 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 0, 6, 2), (1, 6))
    x273 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * 0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * 0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -0.14285714285714288
    x273 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * 0.14285714285714288
    x274 = np.zeros((nvir, nvir), dtype=np.float64)
    x274 += einsum(x272, (0, 1), (0, 1)) * 3.0
    x274 += einsum(l3, (0, 1, 2, 3, 4, 5), x273, (3, 4, 5, 6, 1, 2), (0, 6)) * -6.999999999999999
    x275 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x275 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x275 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -0.5
    l1new += einsum(x274, (0, 1), x275, (2, 3, 0, 1), (3, 2)) * 0.16666666666666
    x276 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x276 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 0, 5, 6), (5, 6, 1, 4))
    x277 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * 0.14285714285714288
    x277 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * 0.14285714285714288
    x278 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x278 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x278 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x278 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x278 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    x278 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x278 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    x279 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x279 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3))
    x279 += einsum(x68, (0, 1, 2, 3), l3, (3, 2, 4, 0, 5, 6), (6, 5, 1, 4)) * -0.5
    x280 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x280 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 5, 0, 6), (5, 6, 1, 4))
    x281 = np.zeros((nocc, nocc), dtype=np.float64)
    x281 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    l1new += einsum(x281, (0, 1), x77, (1, 2), (2, 0)) * -2.0
    l2new += einsum(x281, (0, 1), v.ovov, (2, 3, 1, 4), (3, 4, 2, 0)) * -1.0
    x282 = np.zeros((nocc, nocc), dtype=np.float64)
    x282 += einsum(l2, (0, 1, 2, 3), t2, (3, 4, 0, 1), (2, 4))
    x283 = np.zeros((nocc, nocc), dtype=np.float64)
    x283 += einsum(x281, (0, 1), (0, 1))
    x283 += einsum(x282, (0, 1), (0, 1)) * -0.5
    x283 += einsum(x196, (0, 1), (0, 1))
    x283 += einsum(x198, (0, 1), (0, 1))
    x283 += einsum(t2, (0, 1, 2, 3), x136, (4, 0, 3, 2), (4, 1)) * 0.5
    x284 = np.zeros((nocc, nvir), dtype=np.float64)
    x284 += einsum(t1, (0, 1), (0, 1)) * -12.00000000000048
    x284 += einsum(l1, (0, 1), t2, (1, 2, 3, 0), (2, 3)) * 12.00000000000048
    x284 += einsum(t3, (0, 1, 2, 3, 4, 5), x135, (0, 1, 2, 6, 3, 5), (6, 4)) * 3.0
    x284 += einsum(t2, (0, 1, 2, 3), x276, (1, 0, 4, 2), (4, 3)) * -3.00000000000012
    x284 += einsum(x129, (0, 1, 2, 3, 4, 5), x277, (0, 1, 2, 6, 5, 4), (3, 6)) * -6.999999999999999
    x284 += einsum(l2, (0, 1, 2, 3), x278, (3, 2, 4, 0, 1, 5), (4, 5)) * 3.00000000000012
    x284 += einsum(x111, (0, 1, 2, 3), x279, (1, 0, 4, 3), (4, 2)) * -6.00000000000024
    x284 += einsum(x280, (0, 1, 2, 3), x73, (0, 1, 4, 3), (2, 4)) * 3.00000000000012
    x284 += einsum(t1, (0, 1), x283, (0, 2), (2, 1)) * 12.00000000000048
    x285 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x285 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * 2.0
    x285 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l1new += einsum(x284, (0, 1), x285, (0, 2, 3, 1), (3, 2)) * -0.08333333333333
    x286 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x286 += einsum(l2, (0, 1, 2, 3), x73, (4, 5, 0, 1), (2, 3, 4, 5))
    x287 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x287 += einsum(l3, (0, 1, 2, 3, 4, 5), x183, (6, 7, 5, 1, 0, 2), (3, 4, 6, 7)) * 0.33333333333332
    x288 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x288 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x288 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x288 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x288 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 3.0
    x289 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x289 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x289 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    x289 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    x289 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x290 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x290 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x290 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 2, 1))
    x291 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x291 += einsum(x73, (0, 1, 2, 3), x289, (4, 5, 0, 6, 3, 2), (4, 5, 1, 6)) * -1.0
    x291 += einsum(t2, (0, 1, 2, 3), x290, (4, 1, 5, 6, 3, 2), (4, 5, 0, 6)) * 2.0
    x292 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x292 += einsum(x286, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x292 += einsum(x286, (0, 1, 2, 3), (1, 0, 3, 2))
    x292 += einsum(x146, (0, 1, 2, 3), (0, 2, 3, 1)) * 2.0
    x292 += einsum(x146, (0, 1, 2, 3), (0, 3, 2, 1)) * -6.0
    x292 += einsum(x146, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x292 += einsum(x146, (0, 1, 2, 3), (1, 3, 2, 0)) * 2.0
    x292 += einsum(x287, (0, 1, 2, 3), (0, 1, 2, 3))
    x292 += einsum(x287, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x292 += einsum(x180, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.33333333333324
    x292 += einsum(x180, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.33333333333332
    x292 += einsum(l3, (0, 1, 2, 3, 4, 5), x288, (6, 7, 4, 0, 1, 2), (3, 5, 6, 7)) * -0.33333333333332
    x292 += einsum(t1, (0, 1), x291, (2, 3, 4, 1), (2, 0, 4, 3)) * 2.0
    l1new += einsum(v.ooov, (0, 1, 2, 3), x292, (4, 1, 2, 0), (3, 4)) * -0.25
    x293 = np.zeros((nvir, nvir), dtype=np.float64)
    x293 += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    x293 += einsum(l2, (0, 1, 2, 3), x126, (3, 2, 0, 4), (1, 4)) * -0.5
    x294 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x294 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x294 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    l1new += einsum(x293, (0, 1), x294, (2, 3, 1, 0), (3, 2)) * 2.0
    x295 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x295 += einsum(x230, (0, 1, 2, 3), (0, 1, 3, 2))
    x295 += einsum(x230, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x295 += einsum(x231, (0, 1, 2, 3), (0, 1, 3, 2)) * -5.0
    x295 += einsum(x231, (0, 1, 2, 3), (1, 0, 3, 2))
    x295 += einsum(x180, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.33333333333332
    x295 += einsum(x180, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.33333333333324
    x295 += einsum(x287, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x295 += einsum(x287, (0, 1, 2, 3), (1, 0, 2, 3))
    x295 += einsum(l3, (0, 1, 2, 3, 4, 5), x188, (6, 7, 4, 1, 0, 2), (3, 5, 6, 7)) * 0.33333333333332
    l1new += einsum(v.ooov, (0, 1, 2, 3), x295, (4, 1, 0, 2), (3, 4)) * -0.25
    x296 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x296 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x296 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -0.3333333333333333
    x296 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * 0.3333333333333333
    x296 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * 0.3333333333333333
    x297 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x297 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x297 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    x297 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x297 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    x298 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x298 += einsum(x165, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x298 += einsum(t2, (0, 1, 2, 3), x296, (4, 5, 0, 6, 3, 2), (4, 5, 1, 6))
    x298 += einsum(t2, (0, 1, 2, 3), x297, (4, 5, 0, 6, 2, 3), (4, 5, 1, 6)) * -0.3333333333333333
    x299 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x299 += einsum(t1, (0, 1), x298, (2, 3, 4, 1), (2, 3, 0, 4)) * 3.0
    l1new += einsum(v.ooov, (0, 1, 2, 3), x299, (4, 0, 2, 1), (3, 4)) * 0.5
    x300 = np.zeros((nocc, nvir), dtype=np.float64)
    x300 += einsum(t2, (0, 1, 2, 3), x144, (0, 1, 4, 3), (4, 2))
    x301 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x301 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.2
    x301 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x302 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x302 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x302 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x303 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x303 += einsum(x302, (0, 1, 2, 3), l3, (3, 2, 4, 5, 0, 6), (5, 6, 1, 4))
    x304 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x304 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3))
    x304 += einsum(x73, (0, 1, 2, 3), l3, (2, 4, 3, 0, 5, 6), (6, 5, 1, 4)) * -0.5
    x305 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x305 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 0, 5, 6), (5, 6, 1, 4))
    x306 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x306 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3))
    x306 += einsum(x305, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x307 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x307 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x307 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x308 = np.zeros((nocc, nocc), dtype=np.float64)
    x308 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 1), (3, 4))
    x309 = np.zeros((nocc, nocc), dtype=np.float64)
    x309 += einsum(x194, (0, 1), (0, 1))
    x309 += einsum(x308, (0, 1), (0, 1)) * 0.5
    l1new += einsum(x309, (0, 1), v.ooov, (2, 0, 1, 3), (3, 2))
    x310 = np.zeros((nocc, nvir), dtype=np.float64)
    x310 += einsum(x300, (0, 1), (0, 1))
    x310 += einsum(l2, (0, 1, 2, 3), x301, (3, 2, 4, 1, 0, 5), (4, 5)) * -1.25
    x310 += einsum(x303, (0, 1, 2, 3), x73, (0, 1, 4, 3), (2, 4)) * -0.5
    x310 += einsum(t2, (0, 1, 2, 3), x304, (0, 1, 4, 3), (4, 2))
    x310 += einsum(t2, (0, 1, 2, 3), x306, (0, 1, 4, 2), (4, 3)) * 0.5
    x310 += einsum(l1, (0, 1), x307, (2, 1, 3, 0), (2, 3)) * -1.0
    x310 += einsum(t1, (0, 1), x309, (0, 2), (2, 1))
    l1new += einsum(x310, (0, 1), v.ovov, (2, 1, 0, 3), (3, 2))
    x311 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x311 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x311 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x312 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x312 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x312 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x313 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x313 += einsum(x312, (0, 1, 2, 3), l3, (3, 2, 4, 5, 0, 6), (5, 6, 1, 4))
    x314 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x314 += einsum(x73, (0, 1, 2, 3), l3, (2, 4, 3, 0, 5, 6), (5, 6, 1, 4))
    x315 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x315 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3))
    x315 += einsum(x305, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.75
    x316 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x316 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x316 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x317 = np.zeros((nocc, nocc), dtype=np.float64)
    x317 += einsum(x194, (0, 1), (0, 1))
    x317 += einsum(x308, (0, 1), (0, 1)) * 2.0
    l1new += einsum(x317, (0, 1), v.ooov, (1, 0, 2, 3), (3, 2)) * -1.0
    x318 = np.zeros((nocc, nvir), dtype=np.float64)
    x318 += einsum(l1, (0, 1), (1, 0)) * -2.0
    x318 += einsum(t2, (0, 1, 2, 3), x139, (0, 1, 4, 3), (4, 2))
    x318 += einsum(x300, (0, 1), (0, 1))
    x318 += einsum(l2, (0, 1, 2, 3), x311, (3, 2, 4, 1, 0, 5), (4, 5)) * -1.5
    x318 += einsum(x313, (0, 1, 2, 3), x73, (0, 1, 4, 3), (2, 4)) * -0.5
    x318 += einsum(x307, (0, 1, 2, 3), x314, (0, 1, 4, 2), (4, 3)) * -0.5
    x318 += einsum(t2, (0, 1, 2, 3), x315, (0, 1, 4, 2), (4, 3)) * 2.0
    x318 += einsum(l1, (0, 1), x316, (2, 1, 3, 0), (2, 3)) * -1.0
    x318 += einsum(t1, (0, 1), x317, (0, 2), (2, 1))
    l1new += einsum(x318, (0, 1), v.ovov, (2, 3, 0, 1), (3, 2)) * -1.0
    x319 = np.zeros((nvir, nvir), dtype=np.float64)
    x319 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x320 = np.zeros((nvir, nvir), dtype=np.float64)
    x320 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 0, 4), (1, 4))
    l2new += einsum(x320, (0, 1), v.ovov, (2, 3, 4, 1), (3, 0, 2, 4)) * -1.0
    x321 = np.zeros((nvir, nvir), dtype=np.float64)
    x321 += einsum(x319, (0, 1), (0, 1))
    x321 += einsum(x320, (0, 1), (0, 1)) * 2.0
    l1new += einsum(x321, (0, 1), v.ovvv, (2, 3, 0, 1), (3, 2))
    x322 = np.zeros((nvir, nvir), dtype=np.float64)
    x322 += einsum(x319, (0, 1), (0, 1))
    x322 += einsum(x320, (0, 1), (0, 1)) * 0.5
    l1new += einsum(x322, (0, 1), v.ovvv, (2, 1, 3, 0), (3, 2)) * -1.0
    x323 = np.zeros((nocc, nocc), dtype=np.float64)
    x323 += einsum(x281, (0, 1), (0, 1)) * 2.0
    x323 += einsum(x282, (0, 1), (0, 1)) * -1.0
    x323 += einsum(l3, (0, 1, 2, 3, 4, 5), x195, (6, 4, 5, 0, 1, 2), (3, 6)) * 1.16666666666662
    x323 += einsum(t2, (0, 1, 2, 3), x136, (4, 0, 3, 2), (4, 1))
    x324 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x324 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x324 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    l1new += einsum(x323, (0, 1), x324, (0, 2, 1, 3), (3, 2)) * -0.5
    x325 = np.zeros((nocc, nocc), dtype=np.float64)
    x325 += einsum(l3, (0, 1, 2, 3, 4, 5), x197, (6, 5, 3, 0, 1, 2), (4, 6))
    x326 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x326 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x326 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    l1new += einsum(x325, (0, 1), x326, (0, 1, 2, 3), (3, 2)) * -0.16666666666666
    x327 = np.zeros((nocc, nocc), dtype=np.float64)
    x327 += einsum(x281, (0, 1), (0, 1)) * 12.00000000000048
    x327 += einsum(x194, (0, 1), (0, 1)) * 12.00000000000048
    x327 += einsum(l3, (0, 1, 2, 3, 4, 5), x195, (6, 4, 5, 0, 1, 2), (3, 6)) * 6.999999999999999
    x327 += einsum(x325, (0, 1), (0, 1))
    x327 += einsum(x136, (0, 1, 2, 3), x68, (1, 4, 2, 3), (0, 4)) * -6.00000000000024
    l1new += einsum(f.ov, (0, 1), x327, (2, 0), (1, 2)) * -0.08333333333333
    x328 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x328 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x328 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x329 = np.zeros((nvir, nvir), dtype=np.float64)
    x329 += einsum(t1, (0, 1), x328, (0, 2, 1, 3), (2, 3)) * 2.0
    x330 = np.zeros((nvir, nvir), dtype=np.float64)
    x330 += einsum(f.vv, (0, 1), (0, 1))
    x330 += einsum(x329, (0, 1), (1, 0))
    l1new += einsum(l1, (0, 1), x330, (0, 2), (2, 1))
    x331 = np.zeros((nocc, nocc), dtype=np.float64)
    x331 += einsum(t2, (0, 1, 2, 3), x22, (1, 4, 2, 3), (0, 4)) * 2.0
    x332 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x332 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x332 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x333 = np.zeros((nocc, nocc), dtype=np.float64)
    x333 += einsum(t1, (0, 1), x332, (2, 3, 0, 1), (2, 3)) * 2.0
    x334 = np.zeros((nocc, nvir), dtype=np.float64)
    x334 += einsum(t1, (0, 1), x22, (0, 2, 3, 1), (2, 3)) * 2.0
    x335 = np.zeros((nocc, nvir), dtype=np.float64)
    x335 += einsum(f.ov, (0, 1), (0, 1))
    x335 += einsum(x334, (0, 1), (0, 1))
    l3new += einsum(x335, (0, 1), x135, (2, 3, 4, 0, 5, 6), (5, 1, 6, 2, 3, 4)) * -1.0
    l3new += einsum(x335, (0, 1), l2, (2, 3, 4, 5), (2, 3, 1, 0, 5, 4)) * -1.0
    l3new += einsum(x335, (0, 1), l2, (2, 3, 4, 5), (1, 3, 2, 4, 5, 0)) * -1.0
    l3new += einsum(x335, (0, 1), l2, (2, 3, 4, 5), (2, 3, 1, 4, 5, 0))
    l3new += einsum(x335, (0, 1), l2, (2, 3, 4, 5), (1, 3, 2, 0, 5, 4))
    x336 = np.zeros((nocc, nocc), dtype=np.float64)
    x336 += einsum(t1, (0, 1), x335, (2, 1), (0, 2))
    x337 = np.zeros((nocc, nocc), dtype=np.float64)
    x337 += einsum(f.oo, (0, 1), (0, 1))
    x337 += einsum(x331, (0, 1), (0, 1))
    x337 += einsum(x333, (0, 1), (1, 0))
    x337 += einsum(x336, (0, 1), (0, 1))
    l1new += einsum(l1, (0, 1), x337, (1, 2), (0, 2)) * -1.0
    x338 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x338 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 0, 2), (1, 4, 3, 5))
    l2new += einsum(l2, (0, 1, 2, 3), x338, (3, 4, 1, 5), (0, 5, 2, 4))
    l2new += einsum(x338, (0, 1, 2, 3), x129, (4, 5, 0, 1, 6, 2), (6, 3, 5, 4)) * -1.0
    x339 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x339 += einsum(t2, (0, 1, 2, 3), l3, (3, 4, 5, 6, 0, 1), (6, 4, 5, 2))
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x339, (4, 5, 3, 1), (5, 2, 0, 4))
    x340 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x340 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 4, 5, 3), (0, 2, 4, 5))
    l2new += einsum(x340, (0, 1, 2, 3), l3, (4, 3, 1, 5, 6, 0), (4, 2, 5, 6)) * -1.0
    x341 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x341 += einsum(t2, (0, 1, 2, 3), v.ovvv, (0, 2, 4, 5), (1, 3, 4, 5))
    l2new += einsum(x341, (0, 1, 2, 3), l3, (1, 4, 3, 5, 6, 0), (4, 2, 6, 5)) * -1.0
    x342 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x342 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    l2new += einsum(x33, (0, 1, 2, 3), x342, (0, 4, 5, 3), (5, 4, 1, 2))
    x343 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x343 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 2, 6, 1, 0), (6, 4, 5, 3))
    l2new += einsum(x33, (0, 1, 2, 3), x343, (0, 4, 5, 3), (4, 5, 2, 1))
    l2new += einsum(x343, (0, 1, 2, 3), x94, (4, 3, 2, 5), (1, 5, 0, 4)) * -1.0
    x344 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x344 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5))
    l2new += einsum(x344, (0, 1, 2, 3), x135, (4, 5, 0, 1, 6, 2), (6, 3, 4, 5))
    x345 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x345 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 0, 5), (1, 4, 2, 5))
    l2new += einsum(x345, (0, 1, 2, 3), x149, (4, 5, 0, 1, 6, 2), (3, 6, 5, 4))
    x346 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x346 += einsum(t2, (0, 1, 2, 3), x129, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x346, (4, 2, 5, 1), (5, 3, 0, 4))
    x347 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x347 += einsum(t2, (0, 1, 2, 3), x33, (4, 0, 5, 2), (4, 1, 5, 3))
    l2new += einsum(x347, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (5, 4, 6, 2)) * -1.0
    x348 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x348 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 2, 0, 1, 6), (6, 4, 5, 3))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x348, (1, 4, 5, 3), (4, 5, 0, 2)) * -1.0
    x349 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x349 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 3, 1, 0, 6), (6, 4, 5, 2))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x349, (1, 4, 5, 3), (5, 4, 2, 0)) * -1.0
    x350 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x350 += einsum(l1, (0, 1), v.ooov, (2, 1, 3, 4), (2, 3, 0, 4))
    x351 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x351 += einsum(l2, (0, 1, 2, 3), x0, (2, 4, 5, 1), (3, 4, 0, 5))
    x352 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x352 += einsum(v.oovv, (0, 1, 2, 3), x149, (4, 5, 0, 1, 6, 3), (4, 5, 6, 2))
    x353 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x353 += einsum(x166, (0, 1, 2, 3), x33, (0, 4, 2, 5), (1, 4, 3, 5))
    x354 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x354 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 2, 4, 5), (0, 3, 4, 5))
    x355 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x355 += einsum(x354, (0, 1, 2, 3), l3, (4, 3, 1, 5, 6, 0), (5, 6, 4, 2))
    x356 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x356 += einsum(x32, (0, 1, 2, 3), x149, (4, 5, 0, 1, 6, 3), (4, 5, 6, 2))
    x357 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x357 += einsum(l3, (0, 1, 2, 3, 4, 5), x19, (3, 4, 5, 6, 7, 2), (6, 7, 0, 1))
    x358 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x358 += einsum(v.ovov, (0, 1, 2, 3), x180, (4, 5, 2, 0), (4, 5, 3, 1))
    x359 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x359 += einsum(t1, (0, 1), v.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x360 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x360 += einsum(v.ovov, (0, 1, 2, 3), t3, (0, 2, 4, 1, 5, 6), (4, 5, 6, 3))
    x361 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x361 += einsum(x24, (0, 1, 2, 3), t3, (1, 4, 0, 3, 5, 6), (4, 5, 6, 2)) * 0.49999999999998
    x362 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x362 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x362 += einsum(x359, (0, 1, 2, 3), (0, 3, 2, 1))
    x362 += einsum(x360, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.99999999999996
    x362 += einsum(x361, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x363 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x363 += einsum(x362, (0, 1, 2, 3), l3, (4, 2, 1, 5, 6, 0), (5, 6, 4, 3))
    x364 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x364 += einsum(t1, (0, 1), v.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x365 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x365 += einsum(v.ovov, (0, 1, 2, 3), t3, (2, 4, 5, 3, 1, 6), (4, 5, 0, 6))
    x366 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x366 += einsum(x24, (0, 1, 2, 3), t3, (0, 4, 5, 2, 6, 3), (4, 5, 1, 6)) * 0.49999999999998
    x367 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x367 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x367 += einsum(x56, (0, 1, 2, 3), (3, 0, 2, 1))
    x368 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x368 += einsum(t1, (0, 1), x367, (0, 2, 3, 4), (2, 3, 4, 1))
    x369 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x369 += einsum(x364, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x369 += einsum(x365, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.99999999999996
    x369 += einsum(x366, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x369 += einsum(x368, (0, 1, 2, 3), (0, 2, 1, 3))
    x370 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x370 += einsum(x369, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (6, 2, 4, 5))
    x371 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x371 += einsum(t2, (0, 1, 2, 3), x72, (4, 1, 5, 2), (0, 4, 5, 3))
    x372 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x372 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x372 += einsum(x0, (0, 1, 2, 3), (1, 0, 2, 3))
    x373 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x373 += einsum(t1, (0, 1), x372, (2, 3, 1, 4), (0, 2, 3, 4))
    x374 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x374 += einsum(t1, (0, 1), x105, (2, 3, 4, 1), (0, 2, 3, 4))
    x375 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x375 += einsum(t1, (0, 1), x374, (2, 3, 0, 4), (2, 3, 4, 1))
    x376 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x376 += einsum(x371, (0, 1, 2, 3), (1, 0, 2, 3))
    x376 += einsum(x373, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x376 += einsum(x375, (0, 1, 2, 3), (0, 1, 2, 3))
    x377 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x377 += einsum(x376, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (6, 2, 4, 5))
    x378 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x378 += einsum(x73, (0, 1, 2, 3), x203, (0, 4, 1, 3, 5, 6), (4, 2, 5, 6))
    x379 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x379 += einsum(x307, (0, 1, 2, 3), l3, (4, 2, 5, 6, 1, 0), (6, 4, 5, 3))
    x380 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x380 += einsum(x378, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x380 += einsum(x379, (0, 1, 2, 3), (0, 1, 2, 3))
    x381 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x381 += einsum(v.ovvv, (0, 1, 2, 3), x380, (4, 5, 2, 3), (0, 4, 1, 5)) * 0.5
    x382 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x382 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 5, 1), (3, 4, 0, 5))
    x383 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x383 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x383 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    x384 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x384 += einsum(x383, (0, 1, 2, 3, 4, 5), x67, (0, 6, 2, 4, 7, 5), (6, 1, 7, 3)) * 0.49999999999998
    x385 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x385 += einsum(x203, (0, 1, 2, 3, 4, 5), x204, (6, 2, 0, 7, 5, 3), (1, 6, 4, 7)) * 0.49999999999998
    x386 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x386 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.2
    x386 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x386 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x386 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.2
    x387 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x387 += einsum(l3, (0, 1, 2, 3, 4, 5), x386, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 2.4999999999999
    x388 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x388 += einsum(l3, (0, 1, 2, 3, 4, 5), x67, (5, 6, 4, 1, 7, 2), (3, 6, 0, 7)) * 0.49999999999998
    x389 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x389 += einsum(l3, (0, 1, 2, 3, 4, 5), x67, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7)) * 0.49999999999998
    x390 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x390 += einsum(x68, (0, 1, 2, 3), x149, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    x391 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x391 += einsum(x307, (0, 1, 2, 3), x149, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    x392 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x392 += einsum(x68, (0, 1, 2, 3), x129, (0, 4, 1, 5, 6, 3), (4, 5, 6, 2))
    x393 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x393 += einsum(t2, (0, 1, 2, 3), l3, (3, 4, 2, 5, 6, 0), (5, 6, 1, 4))
    x394 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x394 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x394 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    x394 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2))
    x395 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x395 += einsum(t2, (0, 1, 2, 3), x394, (4, 5, 0, 6, 3, 2), (1, 4, 5, 6))
    x396 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x396 += einsum(x393, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x396 += einsum(x181, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x396 += einsum(x181, (0, 1, 2, 3), (1, 0, 2, 3))
    x396 += einsum(x395, (0, 1, 2, 3), (1, 2, 0, 3))
    x397 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x397 += einsum(t1, (0, 1), x396, (0, 2, 3, 4), (2, 3, 1, 4))
    x398 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x398 += einsum(x382, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x398 += einsum(x384, (0, 1, 2, 3), (1, 0, 3, 2))
    x398 += einsum(x385, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x398 += einsum(x387, (0, 1, 2, 3), (0, 1, 2, 3))
    x398 += einsum(x388, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x398 += einsum(x389, (0, 1, 2, 3), (0, 1, 2, 3))
    x398 += einsum(x390, (0, 1, 2, 3), (0, 1, 2, 3))
    x398 += einsum(x391, (0, 1, 2, 3), (0, 1, 2, 3))
    x398 += einsum(x392, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x398 += einsum(x397, (0, 1, 2, 3), (0, 1, 3, 2))
    x399 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x399 += einsum(v.ovov, (0, 1, 2, 3), x398, (4, 2, 5, 3), (0, 4, 1, 5)) * 0.5
    x400 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x400 += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x401 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x401 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x401 += einsum(x400, (0, 1, 2, 3), (0, 1, 2, 3))
    x401 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3))
    x402 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x402 += einsum(x401, (0, 1, 2, 3), x135, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3))
    x403 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x403 += einsum(f.ov, (0, 1), x68, (2, 3, 1, 4), (2, 3, 0, 4))
    x404 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x404 += einsum(x403, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (6, 2, 4, 5)) * -0.5
    x405 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x405 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 5, 4, 7, 2, 1), (3, 6, 0, 7))
    x406 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x406 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 1, 7, 2), (4, 6, 0, 7))
    x407 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x407 += einsum(l3, (0, 1, 2, 3, 4, 5), x216, (6, 5, 3, 7, 2, 0), (4, 6, 1, 7))
    x408 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x408 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x408 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x409 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x409 += einsum(l3, (0, 1, 2, 3, 4, 5), x408, (4, 6, 5, 1, 7, 2), (3, 6, 0, 7))
    x410 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x410 += einsum(x68, (0, 1, 2, 3), x129, (0, 4, 1, 5, 6, 3), (4, 5, 6, 2)) * 2.00000000000008
    x411 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x411 += einsum(x73, (0, 1, 2, 3), l3, (2, 4, 3, 5, 6, 0), (5, 6, 1, 4))
    x412 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x412 += einsum(t1, (0, 1), x411, (0, 2, 3, 4), (2, 3, 1, 4)) * -2.00000000000008
    x413 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x413 += einsum(x405, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x413 += einsum(x406, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x413 += einsum(x407, (0, 1, 2, 3), (0, 1, 2, 3))
    x413 += einsum(x409, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x413 += einsum(x410, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x413 += einsum(x412, (0, 1, 2, 3), (0, 1, 3, 2))
    x414 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x414 += einsum(v.ovov, (0, 1, 2, 3), x413, (4, 2, 5, 1), (0, 4, 3, 5)) * 0.24999999999999
    x415 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x415 += einsum(v.ovvv, (0, 1, 2, 3), x218, (4, 5, 3, 1), (0, 4, 2, 5)) * -0.5
    x416 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x416 += einsum(t1, (0, 1), x33, (2, 3, 0, 4), (2, 3, 1, 4))
    x417 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x417 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x417 += einsum(x416, (0, 1, 2, 3), (0, 1, 2, 3))
    x418 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x418 += einsum(x417, (0, 1, 2, 3), x135, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3))
    x419 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x419 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x419 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x419 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    x420 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x420 += einsum(t2, (0, 1, 2, 3), x419, (4, 5, 0, 6, 2, 3), (1, 4, 5, 6)) * 0.5
    x421 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x421 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x421 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1))
    x421 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1)) * -1.0
    x422 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x422 += einsum(t2, (0, 1, 2, 3), x421, (0, 4, 5, 2, 6, 3), (1, 4, 5, 6)) * 0.5
    x423 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x423 += einsum(x166, (0, 1, 2, 3), (1, 0, 2, 3))
    x423 += einsum(x420, (0, 1, 2, 3), (1, 2, 0, 3))
    x423 += einsum(x422, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x424 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x424 += einsum(v.ooov, (0, 1, 2, 3), x423, (4, 0, 1, 5), (2, 4, 3, 5))
    x425 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x425 += einsum(v.ovvv, (0, 1, 2, 3), x411, (4, 5, 0, 3), (4, 5, 1, 2)) * -0.5
    x426 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x426 += einsum(v.ooov, (0, 1, 2, 3), x314, (4, 1, 2, 5), (0, 4, 3, 5)) * -0.5
    x427 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x427 += einsum(f.ov, (0, 1), x411, (2, 3, 0, 4), (2, 3, 4, 1)) * -0.5
    x428 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x428 += einsum(f.ov, (0, 1), l1, (2, 3), (0, 3, 1, 2))
    x428 += einsum(x350, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x428 += einsum(x351, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x428 += einsum(x352, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x428 += einsum(x353, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x355, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x428 += einsum(x356, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x428 += einsum(x357, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999997996
    x428 += einsum(x358, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999998
    x428 += einsum(x363, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x370, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x377, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x381, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x428 += einsum(x399, (0, 1, 2, 3), (1, 0, 3, 2))
    x428 += einsum(x402, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x404, (0, 1, 2, 3), (1, 0, 2, 3))
    x428 += einsum(x414, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x428 += einsum(x415, (0, 1, 2, 3), (1, 0, 3, 2))
    x428 += einsum(x418, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x424, (0, 1, 2, 3), (1, 0, 3, 2))
    x428 += einsum(x425, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x426, (0, 1, 2, 3), (1, 0, 3, 2))
    x428 += einsum(x427, (0, 1, 2, 3), (0, 1, 3, 2))
    x428 += einsum(l1, (0, 1), x77, (2, 3), (1, 2, 0, 3)) * 2.0
    l2new += einsum(x428, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x428, (0, 1, 2, 3), (3, 2, 1, 0))
    x429 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x429 += einsum(l1, (0, 1), v.ovvv, (2, 3, 4, 0), (1, 2, 3, 4))
    x430 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x430 += einsum(l1, (0, 1), x33, (1, 2, 3, 4), (2, 3, 0, 4))
    x431 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x431 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x431 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x432 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x432 += einsum(x431, (0, 1, 2, 3), t3, (1, 0, 4, 3, 5, 6), (4, 5, 6, 2)) * 0.49999999999998
    x433 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x433 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x433 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x433 += einsum(x33, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x433 += einsum(x33, (0, 1, 2, 3), (2, 0, 1, 3))
    x434 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x434 += einsum(t2, (0, 1, 2, 3), x433, (1, 4, 0, 5), (4, 2, 3, 5)) * 0.5
    x435 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x435 += einsum(x432, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x435 += einsum(x434, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x436 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x436 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * 3.0
    x436 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x437 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x437 += einsum(x436, (0, 1, 2, 3), t3, (1, 0, 4, 5, 3, 6), (4, 5, 6, 2)) * 0.49999999999998
    x438 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x438 += einsum(v.ovvv, (0, 1, 2, 3), x68, (4, 0, 3, 5), (4, 1, 2, 5)) * 2.0
    x439 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x439 += einsum(x354, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x439 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x439 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x439 += einsum(x359, (0, 1, 2, 3), (0, 2, 3, 1))
    x439 += einsum(x359, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x439 += einsum(x435, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x439 += einsum(x435, (0, 1, 2, 3), (0, 2, 1, 3))
    x439 += einsum(x437, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x439 += einsum(x438, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x440 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x440 += einsum(x439, (0, 1, 2, 3), l3, (1, 4, 2, 5, 6, 0), (5, 6, 4, 3)) * 0.5
    x441 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x441 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 1, 2), (0, 4, 5, 3))
    x442 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x442 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.5
    x442 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x442 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    x443 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x443 += einsum(v.ovov, (0, 1, 2, 3), x442, (2, 4, 5, 1, 6, 3), (0, 4, 5, 6)) * 0.99999999999996
    x444 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x444 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x444 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 2.0
    x445 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x445 += einsum(v.ovov, (0, 1, 2, 3), x444, (2, 4, 5, 3, 6, 1), (0, 4, 5, 6)) * 0.49999999999998
    x446 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x446 += einsum(t2, (0, 1, 2, 3), x13, (4, 3, 2, 5), (0, 1, 4, 5))
    x447 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x447 += einsum(v.ooov, (0, 1, 2, 3), x73, (4, 1, 5, 3), (0, 2, 4, 5)) * 2.0
    x448 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x448 += einsum(x334, (0, 1), x73, (2, 3, 4, 1), (2, 3, 0, 4))
    x449 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x449 += einsum(v.oooo, (0, 1, 2, 3), (0, 2, 3, 1))
    x449 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x449 += einsum(x80, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x449 += einsum(x80, (0, 1, 2, 3), (3, 0, 2, 1))
    x450 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x450 += einsum(t1, (0, 1), x449, (0, 2, 3, 4), (2, 3, 4, 1))
    x451 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x451 += einsum(x441, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x451 += einsum(x443, (0, 1, 2, 3), (2, 1, 0, 3))
    x451 += einsum(x445, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x451 += einsum(x446, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x451 += einsum(x447, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x451 += einsum(x448, (0, 1, 2, 3), (0, 1, 2, 3))
    x451 += einsum(x450, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x452 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x452 += einsum(x451, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (6, 2, 4, 5)) * 0.5
    x453 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x453 += einsum(t2, (0, 1, 2, 3), x33, (4, 1, 5, 2), (4, 0, 5, 3))
    x454 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x454 += einsum(x256, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x454 += einsum(x257, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x455 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x455 += einsum(x33, (0, 1, 2, 3), x68, (4, 2, 3, 5), (0, 1, 4, 5))
    x456 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x456 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x456 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x457 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x457 += einsum(t1, (0, 1), x456, (2, 3, 1, 4), (0, 2, 3, 4))
    x458 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x458 += einsum(x56, (0, 1, 2, 3), (0, 2, 1, 3))
    x458 += einsum(x56, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x459 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x459 += einsum(t1, (0, 1), x458, (2, 3, 4, 0), (2, 3, 4, 1))
    x460 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x460 += einsum(x453, (0, 1, 2, 3), (0, 1, 2, 3))
    x460 += einsum(x454, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x460 += einsum(x454, (0, 1, 2, 3), (1, 0, 2, 3))
    x460 += einsum(x455, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x460 += einsum(x457, (0, 1, 2, 3), (0, 2, 1, 3))
    x460 += einsum(x459, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x461 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x461 += einsum(x460, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (6, 2, 4, 5))
    x462 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x462 += einsum(v.ovov, (0, 1, 2, 3), x68, (4, 2, 1, 5), (0, 4, 3, 5))
    x463 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x463 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x463 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x464 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x464 += einsum(t1, (0, 1), x463, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x465 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x465 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x465 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x465 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3))
    x465 += einsum(x462, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x465 += einsum(x464, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x466 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x466 += einsum(x465, (0, 1, 2, 3), x129, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3))
    x467 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x467 += einsum(t1, (0, 1), x87, (2, 1, 3, 4), (0, 2, 3, 4))
    x468 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x468 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3))
    x468 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new += einsum(x139, (0, 1, 2, 3), x468, (0, 2, 4, 5), (5, 3, 4, 1))
    x469 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x469 += einsum(t1, (0, 1), x468, (2, 0, 3, 4), (2, 3, 1, 4)) * 0.5
    x470 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x470 += einsum(x467, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x470 += einsum(x469, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x471 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x471 += einsum(x470, (0, 1, 2, 3), x129, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3))
    x472 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x472 += einsum(x73, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (6, 4, 5, 2))
    x473 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x473 += einsum(v.ovvv, (0, 1, 2, 3), x472, (4, 5, 3, 1), (0, 4, 2, 5)) * -0.5
    x474 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x474 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 7, 1, 2), (4, 6, 0, 7))
    x475 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x475 += einsum(x68, (0, 1, 2, 3), x135, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3)) * 1.00000000000004
    x476 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x476 += einsum(t1, (0, 1), x411, (2, 0, 3, 4), (2, 3, 1, 4)) * -1.00000000000004
    x477 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x477 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3))
    x477 += einsum(x128, (0, 1, 2, 3), (0, 1, 2, 3))
    x477 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x477 += einsum(x476, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x478 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x478 += einsum(v.ovov, (0, 1, 2, 3), x477, (4, 2, 5, 1), (0, 4, 3, 5)) * 0.49999999999998
    x479 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x479 += einsum(x105, (0, 1, 2, 3), x472, (0, 4, 5, 3), (1, 2, 4, 5)) * -0.5
    x480 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * 0.14285714285714288
    x480 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * 0.14285714285714288
    x481 = np.zeros((nvir, nvir), dtype=np.float64)
    x481 += einsum(l3, (0, 1, 2, 3, 4, 5), x480, (3, 4, 5, 6, 1, 2), (0, 6)) * 1.16666666666662
    x482 = np.zeros((nvir, nvir), dtype=np.float64)
    x482 += einsum(l2, (0, 1, 2, 3), x175, (2, 3, 1, 4), (0, 4))
    x483 = np.zeros((nvir, nvir), dtype=np.float64)
    x483 += einsum(x272, (0, 1), (0, 1)) * 0.49999999999998
    x483 += einsum(x481, (0, 1), (0, 1))
    x483 += einsum(x482, (0, 1), (0, 1)) * -1.0
    x484 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x484 += einsum(x483, (0, 1), v.ovov, (2, 1, 3, 4), (2, 3, 4, 0)) * 0.5
    x485 = np.zeros((nocc, nocc), dtype=np.float64)
    x485 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 1, 0), (3, 4))
    x486 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x486 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 6.999999999999999
    x486 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x486 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x486 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x486 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x486 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x487 = np.zeros((nocc, nocc), dtype=np.float64)
    x487 += einsum(l3, (0, 1, 2, 3, 4, 5), x486, (6, 4, 5, 0, 1, 2), (3, 6)) * 0.16666666666666
    x488 = np.zeros((nocc, nocc), dtype=np.float64)
    x488 += einsum(l3, (0, 1, 2, 3, 4, 5), x197, (6, 5, 3, 0, 1, 2), (4, 6)) * 0.16666666666666
    x489 = np.zeros((nocc, nocc), dtype=np.float64)
    x489 += einsum(l2, (0, 1, 2, 3), x73, (3, 4, 0, 1), (2, 4))
    x490 = np.zeros((nocc, nocc), dtype=np.float64)
    x490 += einsum(x485, (0, 1), (0, 1))
    x490 += einsum(x487, (0, 1), (0, 1)) * -1.0
    x490 += einsum(x488, (0, 1), (0, 1)) * -1.0
    x490 += einsum(x489, (0, 1), (0, 1)) * -1.0
    x491 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x491 += einsum(x490, (0, 1), v.ovov, (2, 3, 1, 4), (2, 0, 4, 3)) * 0.5
    x492 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x492 += einsum(t1, (0, 1), x411, (2, 3, 4, 1), (0, 2, 3, 4)) * -1.0
    x493 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x493 += einsum(v.ovov, (0, 1, 2, 3), x492, (0, 4, 5, 2), (4, 5, 3, 1)) * 0.5
    x494 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x494 += einsum(v.ooov, (0, 1, 2, 3), x411, (4, 1, 2, 5), (0, 4, 3, 5)) * -0.5
    x495 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x495 += einsum(x77, (0, 1), x411, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x496 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x496 += einsum(x429, (0, 1, 2, 3), (0, 1, 2, 3))
    x496 += einsum(x430, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x496 += einsum(x440, (0, 1, 2, 3), (0, 1, 2, 3))
    x496 += einsum(x452, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x496 += einsum(x461, (0, 1, 2, 3), (0, 1, 2, 3))
    x496 += einsum(x466, (0, 1, 2, 3), (0, 1, 2, 3))
    x496 += einsum(x471, (0, 1, 2, 3), (0, 1, 2, 3))
    x496 += einsum(x473, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x496 += einsum(x478, (0, 1, 2, 3), (1, 0, 3, 2))
    x496 += einsum(x479, (0, 1, 2, 3), (0, 1, 2, 3))
    x496 += einsum(x484, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x496 += einsum(x491, (0, 1, 2, 3), (1, 0, 3, 2))
    x496 += einsum(x493, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x496 += einsum(x494, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x496 += einsum(x495, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(x496, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x496, (0, 1, 2, 3), (2, 3, 1, 0))
    x497 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x497 += einsum(v.ooov, (0, 1, 2, 3), x186, (4, 0, 1, 5), (4, 2, 5, 3))
    x498 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x498 += einsum(v.ovvv, (0, 1, 2, 3), x125, (4, 5, 2, 3), (4, 0, 5, 1))
    x499 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x499 += einsum(l2, (0, 1, 2, 3), t2, (3, 4, 1, 5), (2, 4, 0, 5))
    x500 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x500 += einsum(t2, (0, 1, 2, 3), x149, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    x501 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x501 += einsum(t1, (0, 1), x186, (2, 0, 3, 4), (2, 3, 4, 1))
    x502 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x502 += einsum(x499, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x502 += einsum(x500, (0, 1, 2, 3), (0, 1, 2, 3))
    x502 += einsum(x501, (0, 1, 2, 3), (0, 1, 2, 3))
    x503 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x503 += einsum(v.ovov, (0, 1, 2, 3), x502, (4, 2, 5, 3), (0, 4, 1, 5)) * 1.5
    x504 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x504 += einsum(x497, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x504 += einsum(x498, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    x504 += einsum(x503, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x504, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x504, (0, 1, 2, 3), (3, 2, 1, 0)) * -0.3333333333333333
    x505 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x505 += einsum(x319, (0, 1), v.ovov, (2, 3, 4, 1), (2, 4, 0, 3))
    x506 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x506 += einsum(x308, (0, 1), v.ovov, (2, 3, 1, 4), (0, 2, 3, 4))
    x507 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x507 += einsum(x505, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x507 += einsum(x506, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    l2new += einsum(x507, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x507, (0, 1, 2, 3), (2, 3, 1, 0)) * -3.0
    x508 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x508 += einsum(v.ooov, (0, 1, 2, 3), x166, (4, 0, 1, 5), (4, 2, 5, 3))
    x509 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x509 += einsum(l2, (0, 1, 2, 3), x0, (3, 4, 5, 1), (2, 4, 0, 5))
    x510 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x510 += einsum(x166, (0, 1, 2, 3), x33, (1, 4, 2, 5), (0, 4, 3, 5))
    x511 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x511 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 3, 4, 5), (0, 2, 4, 5))
    x512 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x512 += einsum(x511, (0, 1, 2, 3), l3, (4, 3, 1, 5, 6, 0), (5, 6, 4, 2))
    x513 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x513 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 5, 1, 3), (0, 4, 2, 5))
    x514 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x514 += einsum(x513, (0, 1, 2, 3), x135, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3))
    x515 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x515 += einsum(t2, (0, 1, 2, 3), x72, (4, 1, 5, 3), (0, 4, 5, 2))
    x516 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x516 += einsum(x515, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (6, 2, 4, 5)) * 2.0
    x517 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x517 += einsum(l2, (0, 1, 2, 3), t2, (3, 4, 5, 1), (2, 4, 0, 5))
    x518 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x518 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 1, 5), (3, 4, 0, 5))
    x519 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x519 += einsum(x517, (0, 1, 2, 3), (0, 1, 2, 3))
    x519 += einsum(x518, (0, 1, 2, 3), (0, 1, 2, 3))
    x520 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x520 += einsum(v.ovov, (0, 1, 2, 3), x519, (4, 2, 5, 3), (0, 4, 1, 5)) * 2.0
    x521 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x521 += einsum(x508, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x521 += einsum(x509, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x521 += einsum(x510, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x521 += einsum(x512, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x521 += einsum(x514, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x521 += einsum(x516, (0, 1, 2, 3), (0, 1, 2, 3))
    x521 += einsum(x520, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x521, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x521, (0, 1, 2, 3), (3, 2, 1, 0)) * -0.5
    x522 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x522 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 0, 6), (5, 6, 1, 4))
    x523 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x523 += einsum(v.ooov, (0, 1, 2, 3), x522, (4, 0, 1, 5), (4, 2, 5, 3))
    x524 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x524 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 5, 6, 0, 1), (6, 4, 5, 3))
    x525 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x525 += einsum(v.ovvv, (0, 1, 2, 3), x524, (4, 5, 2, 3), (4, 0, 5, 1))
    x526 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x526 += einsum(t2, (0, 1, 2, 3), x149, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3))
    x527 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x527 += einsum(t1, (0, 1), x522, (2, 0, 3, 4), (2, 3, 4, 1))
    x528 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x528 += einsum(x526, (0, 1, 2, 3), (0, 1, 2, 3))
    x528 += einsum(x527, (0, 1, 2, 3), (0, 1, 2, 3))
    x529 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x529 += einsum(v.ovov, (0, 1, 2, 3), x528, (4, 2, 5, 3), (0, 4, 1, 5)) * 0.5
    x530 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x530 += einsum(x523, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x530 += einsum(x525, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x530 += einsum(x529, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x530, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x530, (0, 1, 2, 3), (3, 2, 1, 0)) * -3.0
    x531 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x531 += einsum(x511, (0, 1, 2, 3), l3, (1, 4, 3, 5, 6, 0), (5, 6, 4, 2))
    x532 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x532 += einsum(x513, (0, 1, 2, 3), x129, (4, 5, 0, 1, 6, 2), (4, 5, 6, 3))
    x533 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x533 += einsum(x531, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x533 += einsum(x532, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    l2new += einsum(x533, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x533, (0, 1, 2, 3), (2, 3, 1, 0)) * -0.5
    x534 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x534 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x535 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x535 += einsum(x534, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 2), (6, 1, 4, 5))
    x536 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x536 += einsum(t2, (0, 1, 2, 3), x33, (4, 1, 5, 3), (4, 0, 5, 2))
    x537 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x537 += einsum(x536, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (6, 2, 4, 5))
    x538 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x538 += einsum(x535, (0, 1, 2, 3), (0, 1, 2, 3))
    x538 += einsum(x537, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new += einsum(x538, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x538, (0, 1, 2, 3), (2, 3, 1, 0)) * 2.0
    x539 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x539 += einsum(t2, (0, 1, 2, 3), v.ovvv, (0, 4, 5, 3), (1, 2, 5, 4)) * -1.0
    x539 += einsum(t2, (0, 1, 2, 3), x65, (1, 4, 0, 5), (4, 2, 3, 5))
    l2new += einsum(x539, (0, 1, 2, 3), l3, (4, 1, 2, 5, 6, 0), (3, 4, 6, 5))
    x540 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x540 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 4, 5, 2), (0, 5, 3, 4)) * -1.0
    x540 += einsum(t2, (0, 1, 2, 3), x65, (0, 4, 1, 5), (4, 2, 3, 5))
    l2new += einsum(x540, (0, 1, 2, 3), l3, (4, 2, 1, 5, 6, 0), (4, 3, 5, 6))
    x541 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x541 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x541 += einsum(x245, (0, 1, 2, 3), (1, 0, 2, 3))
    x541 += einsum(x246, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x541 += einsum(t2, (0, 1, 2, 3), x72, (4, 5, 1, 2), (4, 0, 5, 3)) * -1.0
    x541 += einsum(x335, (0, 1), t2, (2, 3, 1, 4), (3, 2, 0, 4))
    l2new += einsum(x541, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (5, 4, 2, 6)) * -1.0
    x542 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x542 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x542 += einsum(x250, (0, 1, 2, 3), (0, 1, 2, 3))
    x542 += einsum(x251, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x542 += einsum(t2, (0, 1, 2, 3), x72, (4, 5, 0, 3), (4, 1, 5, 2)) * -1.0
    x542 += einsum(x335, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4))
    l2new += einsum(x542, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (4, 5, 6, 2)) * -1.0
    x543 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x543 += einsum(t2, (0, 1, 2, 3), x87, (0, 4, 2, 5), (1, 3, 4, 5)) * -1.0
    l2new += einsum(x543, (0, 1, 2, 3), l3, (4, 3, 1, 5, 6, 0), (2, 4, 6, 5)) * -1.0
    x544 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x544 += einsum(t2, (0, 1, 2, 3), x104, (4, 5, 0, 2), (4, 1, 5, 3)) * -1.0
    l2new += einsum(x544, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (5, 4, 2, 6)) * -1.0
    x545 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x545 += einsum(t2, (0, 1, 2, 3), x72, (4, 5, 1, 3), (4, 0, 5, 2))
    l2new += einsum(x545, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (4, 5, 6, 2))
    x546 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x546 += einsum(t2, (0, 1, 2, 3), x24, (0, 4, 5, 2), (1, 4, 3, 5))
    l2new += einsum(x546, (0, 1, 2, 3), x135, (4, 5, 0, 1, 6, 2), (3, 6, 5, 4))
    x547 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x547 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x547 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x547 += einsum(t2, (0, 1, 2, 3), x22, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x547 += einsum(x29, (0, 1, 2, 3), (0, 1, 2, 3))
    x547 += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x547, (2, 4, 0, 5), (5, 1, 4, 3))
    x548 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x548 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x548 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    l2new += einsum(x342, (0, 1, 2, 3), x548, (4, 5, 2, 3), (5, 1, 4, 0)) * -1.0
    x549 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x549 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    x550 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x550 += einsum(t2, (0, 1, 2, 3), x135, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    x550 += einsum(t1, (0, 1), x549, (2, 0, 3, 4), (2, 3, 4, 1))
    x550 += einsum(t2, (0, 1, 2, 3), x162, (1, 4, 5, 3), (4, 0, 5, 2)) * -1.0
    l2new += einsum(x431, (0, 1, 2, 3), x550, (4, 0, 5, 3), (2, 5, 1, 4)) * -1.0
    x551 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x551 += einsum(t2, (0, 1, 2, 3), x135, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    x552 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x552 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x552 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x553 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x553 += einsum(x518, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x553 += einsum(x551, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x553 += einsum(x501, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x553 += einsum(l2, (0, 1, 2, 3), x552, (3, 4, 1, 5), (2, 4, 0, 5)) * -0.5
    l2new += einsum(v.ovov, (0, 1, 2, 3), x553, (4, 2, 5, 1), (5, 3, 4, 0)) * 2.0
    x554 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x554 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x554 += einsum(x32, (0, 1, 2, 3), (0, 1, 3, 2))
    x554 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x554, (2, 4, 1, 5), (0, 5, 4, 3)) * -1.0
    x555 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x555 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x555 += einsum(x32, (0, 1, 2, 3), (0, 1, 3, 2))
    x555 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x555, (3, 4, 0, 5), (5, 1, 2, 4)) * -1.0
    x556 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x556 += einsum(x139, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x556 += einsum(x138, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x556, (4, 5, 0, 3), (1, 2, 5, 4))
    x557 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x557 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x557 += einsum(x211, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x557, (4, 5, 0, 3), (2, 1, 4, 5))
    x558 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x558 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x558 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x558 += einsum(x32, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    l2new += einsum(l2, (0, 1, 2, 3), x558, (3, 4, 1, 5), (0, 5, 2, 4)) * -2.0
    x559 = np.zeros((nvir, nvir), dtype=np.float64)
    x559 += einsum(f.vv, (0, 1), (0, 1)) * 0.6666666666666666
    x559 += einsum(v.ovov, (0, 1, 2, 3), x208, (0, 2, 1, 4), (3, 4)) * -0.3333333333333333
    x559 += einsum(v.ovov, (0, 1, 2, 3), x68, (0, 2, 3, 4), (1, 4)) * 0.3333333333333333
    x559 += einsum(t1, (0, 1), x328, (0, 2, 1, 3), (2, 3)) * 1.3333333333333333
    l2new += einsum(x559, (0, 1), l2, (2, 1, 3, 4), (2, 0, 3, 4)) * 1.5
    x560 = np.zeros((nvir, nvir), dtype=np.float64)
    x560 += einsum(f.vv, (0, 1), (0, 1))
    x560 += einsum(v.ovov, (0, 1, 2, 3), x68, (2, 0, 3, 4), (1, 4)) * -0.5
    x560 += einsum(v.ovov, (0, 1, 2, 3), x265, (2, 0, 1, 4), (3, 4)) * -1.5
    x560 += einsum(x329, (0, 1), (0, 1))
    l2new += einsum(x560, (0, 1), l2, (1, 2, 3, 4), (0, 2, 3, 4))
    x561 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x561 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x561 += einsum(x80, (0, 1, 2, 3), (1, 3, 2, 0))
    x561 += einsum(t1, (0, 1), x65, (2, 3, 4, 1), (3, 2, 4, 0))
    l2new += einsum(l2, (0, 1, 2, 3), x561, (3, 4, 5, 2), (0, 1, 5, 4))
    x562 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x562 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x562 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    l3new += einsum(x562, (0, 1, 2, 3), x135, (4, 0, 5, 2, 6, 7), (6, 3, 7, 4, 1, 5)) * -1.0
    x563 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x563 += einsum(x139, (0, 1, 2, 3), (1, 0, 2, 3))
    x563 += einsum(x549, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new += einsum(x562, (0, 1, 2, 3), x563, (4, 0, 2, 5), (3, 5, 1, 4)) * -1.0
    l2new += einsum(x33, (0, 1, 2, 3), x563, (0, 4, 1, 5), (3, 5, 4, 2))
    x564 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x564 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3))
    x564 += einsum(x549, (0, 1, 2, 3), (1, 0, 2, 3))
    x565 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x565 += einsum(x231, (0, 1, 2, 3), (0, 1, 2, 3))
    x565 += einsum(t1, (0, 1), x564, (2, 3, 4, 1), (2, 3, 4, 0))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x565, (4, 5, 0, 2), (1, 3, 4, 5))
    x566 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x566 += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3))
    x566 += einsum(x186, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x566, (4, 1, 2, 5), (5, 3, 4, 0))
    l2new += einsum(x33, (0, 1, 2, 3), x566, (0, 4, 1, 5), (5, 3, 2, 4))
    x567 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x567 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x567 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 1, 5, 6), (5, 6, 0, 4))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x567, (4, 1, 2, 5), (3, 5, 4, 0)) * -1.0
    x568 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x568 += einsum(x166, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x568 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 0, 5, 6), (5, 6, 1, 4))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x568, (4, 1, 2, 5), (5, 3, 0, 4)) * -1.0
    x569 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x569 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x569 += einsum(x551, (0, 1, 2, 3), (0, 1, 2, 3))
    x569 += einsum(t1, (0, 1), x165, (2, 0, 3, 4), (2, 3, 4, 1))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x569, (4, 2, 5, 3), (5, 1, 4, 0)) * -1.0
    x570 = np.zeros((nocc, nocc), dtype=np.float64)
    x570 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 0, 2), (1, 4))
    x571 = np.zeros((nocc, nocc), dtype=np.float64)
    x571 += einsum(t2, (0, 1, 2, 3), x24, (1, 4, 2, 3), (0, 4))
    x572 = np.zeros((nocc, nocc), dtype=np.float64)
    x572 += einsum(f.oo, (0, 1), (0, 1))
    x572 += einsum(x570, (0, 1), (0, 1))
    x572 += einsum(x571, (0, 1), (0, 1)) * -1.0
    x572 += einsum(x333, (0, 1), (1, 0))
    x572 += einsum(x336, (0, 1), (0, 1))
    l2new += einsum(x572, (0, 1), l2, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    l3new += einsum(x572, (0, 1), l3, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * -1.0
    x573 = np.zeros((nocc, nocc), dtype=np.float64)
    x573 += einsum(f.oo, (0, 1), (0, 1)) * 0.5
    x573 += einsum(t2, (0, 1, 2, 3), x22, (1, 4, 2, 3), (0, 4))
    x573 += einsum(t1, (0, 1), x332, (2, 3, 0, 1), (3, 2))
    x573 += einsum(t1, (0, 1), x335, (2, 1), (0, 2)) * 0.5
    l2new += einsum(x573, (0, 1), l2, (2, 3, 0, 4), (2, 3, 1, 4)) * -2.0
    x574 = np.zeros((nocc, nvir), dtype=np.float64)
    x574 += einsum(f.ov, (0, 1), (0, 1)) * 0.5
    x574 += einsum(x77, (0, 1), (0, 1))
    l2new += einsum(x574, (0, 1), x564, (2, 3, 0, 4), (1, 4, 2, 3)) * -2.0
    l2new += einsum(x574, (0, 1), x566, (2, 3, 0, 4), (4, 1, 2, 3)) * -2.0
    l3new += einsum(x574, (0, 1), x162, (2, 3, 4, 5), (4, 1, 5, 3, 0, 2)) * 2.0
    x575 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x575 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 0, 2), (1, 4, 5, 3)) * 2.0
    x575 += einsum(v.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x575 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    l2new += einsum(x575, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (5, 4, 6, 2)) * 0.5
    x576 = np.zeros((nocc, nocc), dtype=np.float64)
    x576 += einsum(x281, (0, 1), (0, 1))
    x576 += einsum(x194, (0, 1), (0, 1))
    l2new += einsum(x576, (0, 1), v.ovov, (2, 3, 1, 4), (4, 3, 0, 2)) * -1.0
    x577 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x577 += einsum(v.vvvv, (0, 1, 2, 3), l3, (1, 4, 3, 5, 6, 7), (5, 6, 7, 4, 0, 2))
    x578 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x578 += einsum(v.ovvv, (0, 1, 2, 3), x129, (4, 5, 6, 0, 7, 3), (4, 5, 6, 7, 1, 2))
    x579 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x579 += einsum(x73, (0, 1, 2, 3), l3, (2, 4, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4)) * 0.5
    x580 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x580 += einsum(x150, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x580 += einsum(x579, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x581 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x581 += einsum(v.ovov, (0, 1, 2, 3), x580, (4, 5, 6, 0, 2, 7), (4, 5, 6, 3, 1, 7)) * 0.5
    x582 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x582 += einsum(x577, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.5
    x582 += einsum(x578, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x582 += einsum(x581, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    l3new += einsum(x582, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    l3new += einsum(x582, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2)) * -1.0
    x583 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x583 += einsum(v.vvvv, (0, 1, 2, 3), l3, (4, 1, 3, 5, 6, 7), (5, 6, 7, 4, 0, 2))
    x584 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x584 += einsum(v.ovvv, (0, 1, 2, 3), x135, (4, 5, 6, 0, 7, 3), (4, 5, 6, 7, 1, 2))
    x585 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x585 += einsum(t1, (0, 1), x149, (2, 3, 4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x586 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x586 += einsum(v.ovov, (0, 1, 2, 3), x585, (4, 5, 6, 2, 0, 7), (4, 5, 6, 7, 3, 1))
    x587 = np.zeros((nvir, nvir), dtype=np.float64)
    x587 += einsum(v.ovov, (0, 1, 2, 3), x265, (2, 0, 1, 4), (3, 4)) * 0.75
    x588 = np.zeros((nvir, nvir), dtype=np.float64)
    x588 += einsum(v.ovov, (0, 1, 2, 3), x68, (2, 0, 3, 4), (1, 4)) * 0.25
    x589 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x589 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x589 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x590 = np.zeros((nvir, nvir), dtype=np.float64)
    x590 += einsum(t1, (0, 1), x589, (0, 2, 1, 3), (2, 3)) * 0.5
    x591 = np.zeros((nvir, nvir), dtype=np.float64)
    x591 += einsum(x587, (0, 1), (0, 1))
    x591 += einsum(x588, (0, 1), (0, 1))
    x591 += einsum(x590, (0, 1), (0, 1)) * -1.0
    x592 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x592 += einsum(x591, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 2, 3, 0)) * 2.0
    x593 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x593 += einsum(x334, (0, 1), x149, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1))
    x594 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x594 += einsum(x583, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x594 += einsum(x584, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x594 += einsum(x586, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x594 += einsum(x592, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x594 += einsum(x593, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x594, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    l3new += einsum(x594, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2)) * -1.0
    x595 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x595 += einsum(v.ooov, (0, 1, 2, 3), x149, (4, 1, 5, 2, 6, 7), (4, 5, 0, 6, 7, 3))
    x596 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x596 += einsum(x33, (0, 1, 2, 3), x149, (4, 0, 5, 1, 6, 7), (4, 5, 2, 6, 7, 3))
    x597 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x597 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x597 += einsum(x32, (0, 1, 2, 3), (0, 1, 3, 2))
    x597 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.00000000000001
    x598 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x598 += einsum(x597, (0, 1, 2, 3), l3, (4, 5, 2, 6, 0, 7), (6, 7, 1, 4, 5, 3))
    x599 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x599 += einsum(x70, (0, 1, 2, 3), l3, (4, 3, 2, 5, 0, 6), (5, 6, 1, 4)) * 0.5
    x600 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x600 += einsum(v.ovov, (0, 1, 2, 3), x599, (4, 5, 2, 6), (0, 4, 5, 3, 1, 6))
    x601 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x601 += einsum(x595, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x601 += einsum(x596, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x601 += einsum(x598, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x601 += einsum(x600, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    l3new += einsum(x601, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1))
    l3new += einsum(x601, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1)) * -1.0
    x602 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x602 += einsum(v.ovov, (0, 1, 2, 3), x181, (4, 5, 2, 6), (4, 5, 0, 6, 1, 3))
    l3new += einsum(x602, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * 0.5
    l3new += einsum(x602, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1)) * -0.5
    l3new += einsum(x602, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -0.5
    l3new += einsum(x602, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * 0.5
    x603 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x603 += einsum(v.ovov, (0, 1, 2, 3), x411, (4, 5, 2, 6), (0, 4, 5, 3, 1, 6)) * -0.5
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0))
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0)) * -1.0
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2)) * -1.0
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1))
    l3new += einsum(x603, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 2, 1)) * -1.0
    x604 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x604 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x604 += einsum(x80, (0, 1, 2, 3), (0, 2, 1, 3))
    x605 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x605 += einsum(x604, (0, 1, 2, 3), l3, (4, 5, 6, 0, 7, 2), (7, 1, 3, 4, 5, 6)) * 0.5
    x606 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x606 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x606 += einsum(x33, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x607 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x607 += einsum(t1, (0, 1), x606, (2, 3, 4, 1), (0, 2, 3, 4)) * 2.0
    x608 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x608 += einsum(x607, (0, 1, 2, 3), l3, (4, 5, 6, 0, 7, 2), (7, 1, 3, 4, 5, 6)) * 0.5
    x609 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x609 += einsum(x605, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x609 += einsum(x608, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x609, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2))
    l3new += einsum(x609, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1)) * -1.0
    x610 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x610 += einsum(v.ovov, (0, 1, 2, 3), x472, (4, 5, 6, 1), (0, 2, 4, 3, 5, 6)) * -0.5
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0))
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 0, 1)) * -1.0
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1))
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * -1.0
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1)) * -1.0
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 2, 1))
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2))
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -1.0
    l3new += einsum(x610, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * -1.0
    x611 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x611 += einsum(v.ooov, (0, 1, 2, 3), x135, (4, 5, 1, 2, 6, 7), (4, 5, 0, 6, 7, 3))
    x612 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x612 += einsum(x33, (0, 1, 2, 3), x135, (4, 5, 0, 1, 6, 7), (4, 5, 2, 6, 7, 3))
    x613 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x613 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x613 += einsum(x32, (0, 1, 2, 3), (0, 1, 3, 2))
    x613 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.00000000000001
    x614 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x614 += einsum(x613, (0, 1, 2, 3), l3, (4, 2, 5, 6, 7, 0), (6, 7, 1, 4, 5, 3))
    x615 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x615 += einsum(x307, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (6, 4, 5, 2)) * 0.5
    x616 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x616 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x616 += einsum(x615, (0, 1, 2, 3), (0, 1, 2, 3))
    x617 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x617 += einsum(v.ovov, (0, 1, 2, 3), x616, (4, 5, 6, 1), (0, 2, 4, 3, 5, 6))
    x618 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x618 += einsum(x611, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x618 += einsum(x612, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x618 += einsum(x614, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x618 += einsum(x617, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    l3new += einsum(x618, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2))
    l3new += einsum(x618, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * -1.0
    x619 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x619 += einsum(v.ovov, (0, 1, 2, 3), x186, (4, 5, 2, 6), (4, 5, 0, 6, 1, 3))
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -0.5
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1)) * 0.5
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * 0.5
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -0.5
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0))
    l3new += einsum(x619, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0
    x620 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x620 += einsum(v.ovov, (0, 1, 2, 3), x342, (4, 5, 6, 3), (4, 0, 2, 5, 6, 1))
    l3new += einsum(x620, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -0.5
    l3new += einsum(x620, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2))
    l3new += einsum(x620, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.0
    l3new += einsum(x620, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1)) * -1.0
    l3new += einsum(x620, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1))
    l3new += einsum(x620, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * 0.5
    x621 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x621 += einsum(v.ovov, (0, 1, 2, 3), x343, (4, 5, 6, 3), (4, 0, 2, 5, 6, 1))
    l3new += einsum(x621, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -0.5
    l3new += einsum(x621, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -1.0
    l3new += einsum(x621, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1))
    l3new += einsum(x621, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new += einsum(x621, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    l3new += einsum(x621, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * 0.5
    x622 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x622 += einsum(x57, (0, 1, 2, 3), l3, (4, 5, 6, 7, 0, 1), (7, 2, 3, 4, 5, 6))
    x623 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x623 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x623 += einsum(x56, (0, 1, 2, 3), (2, 1, 0, 3))
    x624 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x624 += einsum(x623, (0, 1, 2, 3), l3, (4, 5, 6, 7, 0, 2), (7, 1, 3, 4, 5, 6))
    x625 = np.zeros((nocc, nocc), dtype=np.float64)
    x625 += einsum(t1, (0, 1), x77, (2, 1), (0, 2)) * 2.0
    x626 = np.zeros((nocc, nocc), dtype=np.float64)
    x626 += einsum(x331, (0, 1), (0, 1))
    x626 += einsum(x333, (0, 1), (1, 0))
    x626 += einsum(x625, (0, 1), (0, 1))
    x627 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x627 += einsum(x626, (0, 1), l3, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4))
    x628 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x628 += einsum(x622, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x628 += einsum(x624, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x628 += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x628, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    l3new += einsum(x628, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -1.0
    x629 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x629 += einsum(f.vv, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x630 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x630 += einsum(f.ov, (0, 1), x149, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x631 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x631 += einsum(v.ovvv, (0, 1, 2, 3), x149, (4, 5, 6, 0, 7, 3), (4, 5, 6, 7, 1, 2))
    x632 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x632 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x633 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x633 += einsum(v.ovov, (0, 1, 2, 3), x632, (4, 5, 6, 2, 0, 7), (4, 5, 6, 7, 3, 1))
    x634 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x634 += einsum(x629, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x634 += einsum(x630, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x634 += einsum(x631, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x634 += einsum(x633, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x634, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    l3new += einsum(x634, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x635 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x635 += einsum(v.ovov, (0, 1, 2, 3), x549, (4, 5, 2, 6), (4, 5, 0, 6, 1, 3))
    x636 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x636 += einsum(x546, (0, 1, 2, 3), l3, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3)) * -1.00000000000001
    x637 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x637 += einsum(x635, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x637 += einsum(x636, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    l3new += einsum(x637, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2))
    l3new += einsum(x637, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.0
    l3new += einsum(x637, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1)) * -1.0
    l3new += einsum(x637, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1))
    x638 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x638 += einsum(x56, (0, 1, 2, 3), l3, (4, 5, 6, 7, 0, 1), (7, 2, 3, 4, 5, 6))
    x639 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x639 += einsum(x80, (0, 1, 2, 3), l3, (4, 5, 6, 7, 1, 0), (7, 2, 3, 4, 5, 6))
    x640 = np.zeros((nocc, nocc), dtype=np.float64)
    x640 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x641 = np.zeros((nocc, nocc), dtype=np.float64)
    x641 += einsum(f.oo, (0, 1), (0, 1))
    x641 += einsum(x640, (0, 1), (1, 0))
    x642 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x642 += einsum(x641, (0, 1), l3, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4))
    x643 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x643 += einsum(x638, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x643 += einsum(x639, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x643 += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    l3new += einsum(x643, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1))
    l3new += einsum(x643, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    x644 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x644 += einsum(x513, (0, 1, 2, 3), l3, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3))
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * 2.00000000000002
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2)) * -2.00000000000002
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 2, 1)) * 2.00000000000002
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * 1.00000000000001
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.00000000000001
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1)) * -1.00000000000001
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1)) * 1.00000000000001
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * -2.00000000000002
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -2.00000000000002
    l3new += einsum(x644, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * 2.00000000000002
    x645 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x645 += einsum(l2, (0, 1, 2, 3), v.ooov, (4, 3, 5, 6), (2, 4, 5, 0, 1, 6))
    x646 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x646 += einsum(x344, (0, 1, 2, 3), l3, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3))
    x647 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x647 += einsum(x645, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x647 += einsum(x646, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 1.00000000000001
    l3new += einsum(x647, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    l3new += einsum(x647, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2))
    l3new += einsum(x647, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 2, 1)) * -1.0
    l3new += einsum(x647, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0))
    l3new += einsum(x647, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0))
    l3new += einsum(x647, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * -1.0
    x648 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x648 += einsum(v.ooov, (0, 1, 2, 3), x149, (4, 5, 0, 1, 6, 7), (4, 5, 2, 6, 7, 3))
    x649 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x649 += einsum(x33, (0, 1, 2, 3), x149, (4, 5, 0, 2, 6, 7), (4, 5, 1, 6, 7, 3))
    x650 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x650 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x650 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2))
    x650 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.00000000000001
    x651 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x651 += einsum(x650, (0, 1, 2, 3), l3, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3))
    x652 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x652 += einsum(x648, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x652 += einsum(x649, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x652 += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2))
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 2, 1)) * -1.0
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * -1.0
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1))
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1)) * -1.0
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0))
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0))
    l3new += einsum(x652, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * -1.0
    x653 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x653 += einsum(v.ooov, (0, 1, 2, 3), x149, (4, 5, 1, 2, 6, 7), (4, 5, 0, 6, 7, 3))
    x654 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x654 += einsum(x33, (0, 1, 2, 3), x149, (4, 5, 0, 1, 6, 7), (4, 5, 2, 6, 7, 3))
    x655 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x655 += einsum(x613, (0, 1, 2, 3), l3, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3))
    x656 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x656 += einsum(x653, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x656 += einsum(x654, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x656 += einsum(x655, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x656, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    l3new += einsum(x656, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2)) * -1.0
    l3new += einsum(x656, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -1.0
    l3new += einsum(x656, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0))
    x657 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x657 += einsum(l2, (0, 1, 2, 3), v.ovvv, (4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x658 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x658 += einsum(v.ovov, (0, 1, 2, 3), x166, (4, 5, 2, 6), (4, 5, 0, 6, 1, 3))
    x659 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x659 += einsum(x657, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x659 += einsum(x658, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2))
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * -1.0
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1))
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1)) * -1.0
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0))
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * -1.0
    l3new += einsum(x659, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0))
    x660 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x660 += einsum(l2, (0, 1, 2, 3), v.ovvv, (4, 5, 6, 0), (2, 3, 4, 1, 5, 6))
    x661 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x661 += einsum(v.ovov, (0, 1, 2, 3), x139, (4, 5, 2, 6), (4, 5, 0, 6, 1, 3))
    x662 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x662 += einsum(x660, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x662 += einsum(x661, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new += einsum(x662, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * -1.0
    l3new += einsum(x662, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2))
    l3new += einsum(x662, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0))
    l3new += einsum(x662, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0)) * -1.0
    x663 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x663 += einsum(l2, (0, 1, 2, 3), x33, (3, 4, 5, 6), (2, 4, 5, 0, 1, 6))
    l3new += einsum(x663, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    l3new += einsum(x663, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -1.0
    l3new += einsum(x663, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1))
    l3new += einsum(x663, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new += einsum(x663, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    l3new += einsum(x663, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0))
    x664 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x664 += einsum(l2, (0, 1, 2, 3), x33, (2, 4, 5, 6), (3, 4, 5, 0, 1, 6))
    l3new += einsum(x664, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2))
    l3new += einsum(x664, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2))
    l3new += einsum(x664, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2)) * -1.0
    l3new += einsum(x664, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1)) * -1.0
    l3new += einsum(x664, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 0, 1))
    l3new += einsum(x664, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * -1.0
    x665 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x665 += einsum(l2, (0, 1, 2, 3), v.ooov, (4, 2, 5, 6), (3, 4, 5, 0, 1, 6))
    l3new += einsum(x665, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 2, 1))
    l3new += einsum(x665, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -1.0
    l3new += einsum(x665, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2))
    l3new += einsum(x665, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1))
    l3new += einsum(x665, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 0, 1)) * -1.0
    l3new += einsum(x665, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * -1.0
    x666 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x666 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x666 += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x666 += einsum(x338, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x666 += einsum(x24, (0, 1, 2, 3), x68, (4, 0, 3, 5), (4, 1, 5, 2)) * 1.00000000000001
    x666 += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l3new += einsum(x666, (0, 1, 2, 3), l3, (4, 2, 5, 6, 0, 7), (4, 3, 5, 6, 1, 7))
    x667 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x667 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x667 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x668 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x668 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.499999999999995
    x668 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.499999999999995
    x668 += einsum(x344, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x668 += einsum(v.ovov, (0, 1, 2, 3), x667, (4, 2, 3, 5), (4, 0, 5, 1)) * 0.5
    l3new += einsum(x668, (0, 1, 2, 3), l3, (4, 5, 2, 6, 0, 7), (4, 3, 5, 6, 1, 7)) * -2.00000000000002
    x669 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x669 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x669 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    x670 = np.zeros((nvir, nvir), dtype=np.float64)
    x670 += einsum(f.vv, (0, 1), (0, 1)) * 2.0
    x670 += einsum(t2, (0, 1, 2, 3), x24, (1, 0, 3, 4), (2, 4)) * -1.0
    x670 += einsum(t2, (0, 1, 2, 3), x669, (1, 0, 2, 4), (3, 4)) * -3.0
    x670 += einsum(t1, (0, 1), x328, (0, 2, 1, 3), (3, 2)) * 4.0
    l3new += einsum(x670, (0, 1), l3, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * 0.5
    x671 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x671 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x671 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -1.0
    x672 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x672 += einsum(t1, (0, 1), x671, (2, 3, 4, 5, 1, 6), (2, 3, 4, 0, 5, 6)) * -1.0
    l3new += einsum(x33, (0, 1, 2, 3), x672, (4, 0, 5, 2, 6, 7), (6, 3, 7, 4, 1, 5))

    return {"l1new": l1new, "l2new": l2new, "l3new": l3new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM1
    rdm1_f_oo = np.zeros((nocc, nocc), dtype=np.float64)
    rdm1_f_oo += einsum(delta.oo, (0, 1), (0, 1)) * 2.0
    rdm1_f_ov = np.zeros((nocc, nvir), dtype=np.float64)
    rdm1_f_ov += einsum(t1, (0, 1), (0, 1)) * 2.0
    rdm1_f_vo = np.zeros((nvir, nocc), dtype=np.float64)
    rdm1_f_vo += einsum(l1, (0, 1), (0, 1)) * 2.0
    rdm1_f_vv = np.zeros((nvir, nvir), dtype=np.float64)
    rdm1_f_vv += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 0, 6, 2), (1, 6)) * 0.49999999999998
    rdm1_f_vv += einsum(l1, (0, 1), t1, (1, 2), (0, 2)) * 2.0
    rdm1_f_vv += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4)) * 3.0
    x0 = np.zeros((nocc, nocc), dtype=np.float64)
    x0 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm1_f_oo += einsum(x0, (0, 1), (1, 0)) * -2.0
    x1 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 6.999999999999999
    x1 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    rdm1_f_oo += einsum(l3, (0, 1, 2, 3, 4, 5), x1, (6, 5, 4, 0, 2, 1), (6, 3)) * -0.16666666666666
    x2 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.3333333333333333
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * 0.3333333333333333
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * 0.3333333333333333
    rdm1_f_oo += einsum(l3, (0, 1, 2, 3, 4, 5), x2, (3, 6, 5, 0, 1, 2), (6, 4)) * -0.49999999999998
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x3 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm1_f_oo += einsum(t2, (0, 1, 2, 3), x3, (4, 1, 3, 2), (0, 4)) * -1.0
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x4 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.3333333333333333
    rdm1_f_oo += einsum(t2, (0, 1, 2, 3), x4, (4, 1, 2, 3), (0, 4)) * -3.0
    x5 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(t1, (0, 1), l3, (2, 1, 3, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    rdm1_f_ov += einsum(t3, (0, 1, 2, 3, 4, 5), x5, (0, 1, 2, 6, 3, 5), (6, 4)) * -0.49999999999998
    x6 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(t1, (0, 1), l3, (1, 2, 3, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x7 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.999999999999999
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    x7 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    rdm1_f_ov += einsum(x6, (0, 1, 2, 3, 4, 5), x7, (0, 1, 2, 6, 5, 4), (3, 6)) * 0.16666666666666
    x8 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 5.0
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    x8 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    rdm1_f_ov += einsum(l2, (0, 1, 2, 3), x8, (4, 2, 3, 5, 1, 0), (4, 5)) * 0.5
    x9 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x9 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x10 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x11 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 1, 5, 6), (6, 5, 0, 4)) * -1.0
    x11 += einsum(x10, (0, 1, 2, 3), l3, (3, 2, 4, 5, 1, 6), (6, 5, 0, 4)) * 3.0
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x12 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm1_f_ov += einsum(x11, (0, 1, 2, 3), x12, (1, 0, 4, 3), (2, 4)) * 0.5
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x14 += einsum(x13, (0, 1, 2, 3), l3, (2, 3, 4, 1, 5, 6), (6, 5, 0, 4)) * -1.0
    rdm1_f_ov += einsum(x12, (0, 1, 2, 3), x14, (0, 1, 4, 2), (4, 3)) * 0.5
    x15 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2)) * 2.0
    x15 += einsum(x13, (0, 1, 2, 3), l3, (2, 4, 3, 1, 5, 6), (6, 5, 0, 4)) * -1.0
    rdm1_f_ov += einsum(t2, (0, 1, 2, 3), x15, (0, 1, 4, 3), (4, 2)) * -1.0
    x16 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 1, 5, 6), (5, 6, 0, 4))
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x17 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.2
    rdm1_f_ov += einsum(x16, (0, 1, 2, 3), x17, (0, 1, 4, 3), (2, 4)) * -2.5
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x18 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    rdm1_f_ov += einsum(l1, (0, 1), x18, (2, 1, 3, 0), (2, 3)) * 4.0
    x19 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.14285714285714288
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -0.14285714285714288
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.14285714285714288
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.14285714285714288
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * 0.14285714285714288
    x20 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x20 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 3.0
    x20 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x20 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    x20 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x21 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum(x0, (0, 1), (0, 1)) * 12.00000000000048
    x22 += einsum(l3, (0, 1, 2, 3, 4, 5), x19, (6, 4, 5, 0, 2, 1), (3, 6)) * 6.999999999999999
    x22 += einsum(l3, (0, 1, 2, 3, 4, 5), x20, (3, 6, 5, 0, 1, 2), (4, 6))
    x22 += einsum(l2, (0, 1, 2, 3), x21, (4, 3, 0, 1), (2, 4)) * 18.00000000000072
    x22 += einsum(l2, (0, 1, 2, 3), x12, (4, 2, 0, 1), (3, 4)) * 6.00000000000024
    rdm1_f_ov += einsum(t1, (0, 1), x22, (0, 2), (2, 1)) * -0.16666666666666
    x23 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x23 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x23 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.14285714285714288
    x23 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.14285714285714288
    x23 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 0.14285714285714288
    x23 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.14285714285714288
    x23 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * 0.14285714285714288
    rdm1_f_vv += einsum(l3, (0, 1, 2, 3, 4, 5), x23, (3, 4, 5, 6, 1, 2), (0, 6)) * 1.16666666666662
    x24 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x24 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x24 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x24 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    rdm1_f_vv += einsum(l3, (0, 1, 2, 3, 4, 5), x24, (3, 4, 5, 1, 6, 2), (0, 6)) * 0.16666666666666
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x25 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm1_f_vv += einsum(l2, (0, 1, 2, 3), x25, (2, 3, 1, 4), (0, 4)) * -1.0

    rdm1_f = np.block([[rdm1_f_oo, rdm1_f_ov], [rdm1_f_vo, rdm1_f_vv]])

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM2
    rdm2_f_oooo = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (0, 2, 1, 3))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (0, 2, 1, 3))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_ovov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_ovov += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_ovov += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_ovvo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_ovvo += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovvo += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovvo += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_ovvo += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_voov = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_voov += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_voov += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_voov += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_voov += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_vovo = np.zeros((nvir, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_vovo += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovo += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vvoo = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x0 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.14285714285714288
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -0.14285714285714288
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.14285714285714288
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.14285714285714288
    x0 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * 0.14285714285714288
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(l3, (0, 1, 2, 3, 4, 5), x0, (6, 4, 5, 0, 2, 1), (3, 6)) * 0.3888888888888733
    x2 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 3.0
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    x2 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(l3, (0, 1, 2, 3, 4, 5), x2, (3, 6, 5, 0, 1, 2), (4, 6)) * 0.05555555555555333
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x4 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    rdm2_f_ovoo += einsum(x4, (0, 1, 2, 3), l3, (4, 3, 2, 5, 1, 6), (0, 4, 5, 6)) * 1.5
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(l2, (0, 1, 2, 3), x4, (4, 3, 0, 1), (4, 2))
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x6 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo += einsum(x6, (0, 1, 2, 3), l3, (4, 5, 2, 0, 6, 1), (4, 5, 3, 6)) * 0.5
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 += einsum(l2, (0, 1, 2, 3), x6, (4, 2, 0, 1), (4, 3)) * 0.3333333333333333
    x8 = np.zeros((nocc, nocc), dtype=np.float64)
    x8 += einsum(x1, (0, 1), (0, 1))
    x8 += einsum(x3, (0, 1), (0, 1))
    x8 += einsum(x5, (0, 1), (1, 0))
    x8 += einsum(x7, (0, 1), (1, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (0, 3, 1, 2)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (0, 3, 2, 1)) * 1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (3, 0, 1, 2)) * 1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (3, 0, 2, 1)) * -1.5
    x9 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x9 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_ovoo += einsum(x9, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x9, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x10 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x10 += einsum(t1, (0, 1), x9, (2, 3, 4, 1), (2, 3, 0, 4))
    x11 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x11 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x11 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x11 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x12 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x12 += einsum(l3, (0, 1, 2, 3, 4, 5), x11, (6, 7, 5, 1, 0, 2), (3, 4, 6, 7)) * 0.16666666666667
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x14 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x14 += einsum(l2, (0, 1, 2, 3), x13, (4, 5, 1, 0), (4, 5, 2, 3)) * 0.5
    x15 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x15 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3))
    x15 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x15 += einsum(x14, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_oooo += einsum(x15, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x15, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_oooo += einsum(x15, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x15, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x16 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(x13, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 1), (5, 6, 0, 4))
    x17 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x17 += einsum(t1, (0, 1), x16, (2, 3, 4, 1), (0, 2, 3, 4)) * -0.5
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (3, 0, 2, 1))
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_oooo += einsum(x17, (0, 1, 2, 3), (3, 0, 2, 1))
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x18 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(x18, (0, 1, 2, 3), l3, (4, 2, 3, 5, 1, 6), (5, 6, 0, 4))
    x20 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x20 += einsum(t1, (0, 1), x19, (2, 3, 4, 1), (0, 2, 3, 4)) * 1.5
    rdm2_f_oooo += einsum(x20, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_oooo += einsum(x20, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x21 = np.zeros((nocc, nocc), dtype=np.float64)
    x21 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 1, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (0, 3, 2, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 1, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (0, 3, 2, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x21, (2, 3), (3, 0, 2, 1)) * -1.0
    x22 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x22 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x22 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x22 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x22 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 3.0
    x23 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x23 += einsum(l3, (0, 1, 2, 3, 4, 5), x22, (6, 7, 4, 0, 2, 1), (3, 5, 6, 7)) * 0.16666666666667
    rdm2_f_oooo += einsum(x23, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x23, (0, 1, 2, 3), (2, 3, 0, 1))
    x24 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x24 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    rdm2_f_ovoo += einsum(x24, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x24, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x25 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x25 += einsum(t1, (0, 1), x24, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_oooo += einsum(x25, (0, 1, 2, 3), (3, 2, 1, 0))
    x26 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x26 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_oooo += einsum(x26, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x26, (0, 1, 2, 3), (3, 2, 1, 0))
    x27 = np.zeros((nocc, nocc), dtype=np.float64)
    x27 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 1, 0), (2, 4))
    x28 = np.zeros((nocc, nocc), dtype=np.float64)
    x28 += einsum(l3, (0, 1, 2, 3, 4, 5), x0, (6, 4, 5, 0, 2, 1), (3, 6)) * 1.16666666666662
    x29 = np.zeros((nocc, nocc), dtype=np.float64)
    x29 += einsum(l3, (0, 1, 2, 3, 4, 5), x2, (3, 6, 5, 0, 1, 2), (4, 6)) * 0.16666666666666
    x30 = np.zeros((nocc, nocc), dtype=np.float64)
    x30 += einsum(l2, (0, 1, 2, 3), x13, (4, 2, 0, 1), (4, 3))
    x31 = np.zeros((nocc, nocc), dtype=np.float64)
    x31 += einsum(x27, (0, 1), (0, 1)) * -1.0
    x31 += einsum(x28, (0, 1), (0, 1))
    x31 += einsum(x29, (0, 1), (0, 1))
    x31 += einsum(x30, (0, 1), (1, 0)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x31, (2, 3), (0, 3, 1, 2)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x31, (2, 3), (3, 0, 2, 1)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x31, (2, 3), (0, 3, 1, 2)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x31, (2, 3), (3, 0, 2, 1)) * -0.5
    x32 = np.zeros((nocc, nocc), dtype=np.float64)
    x32 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x32, (2, 3), (0, 3, 1, 2)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x32, (2, 3), (3, 0, 2, 1)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x32, (2, 3), (0, 3, 1, 2)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x32, (2, 3), (3, 0, 2, 1)) * -0.5
    x33 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x33 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    rdm2_f_oooo += einsum(x33, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.50000000000001
    rdm2_f_oooo += einsum(x33, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.50000000000001
    rdm2_f_oooo += einsum(x33, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.50000000000001
    rdm2_f_oooo += einsum(x33, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.50000000000001
    x34 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x34 += einsum(x13, (0, 1, 2, 3), l3, (3, 4, 2, 5, 6, 1), (5, 6, 0, 4))
    x35 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x35 += einsum(t1, (0, 1), x34, (2, 3, 4, 1), (0, 2, 3, 4)) * -0.5
    rdm2_f_oooo += einsum(x35, (0, 1, 2, 3), (3, 0, 1, 2))
    rdm2_f_oooo += einsum(x35, (0, 1, 2, 3), (0, 3, 2, 1))
    rdm2_f_oooo += einsum(x35, (0, 1, 2, 3), (3, 0, 1, 2))
    rdm2_f_oooo += einsum(x35, (0, 1, 2, 3), (0, 3, 2, 1))
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 0), (5, 6, 1, 4))
    rdm2_f_oooo += einsum(t1, (0, 1), x36, (2, 3, 4, 1), (4, 0, 3, 2))
    rdm2_f_ovoo += einsum(x36, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x36, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x37 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x37 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x37 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x38 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x38 += einsum(t1, (0, 1), x37, (2, 3, 4, 1), (0, 2, 3, 4))
    rdm2_f_oooo += einsum(x38, (0, 1, 2, 3), (0, 3, 1, 2))
    x39 = np.zeros((nocc, nocc), dtype=np.float64)
    x39 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 1), (3, 4))
    x40 = np.zeros((nocc, nocc), dtype=np.float64)
    x40 += einsum(delta.oo, (0, 1), (0, 1))
    x40 += einsum(x39, (0, 1), (0, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x40, (2, 3), (0, 3, 1, 2))
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    rdm2_f_ovoo += einsum(x41, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x41, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(x41, (0, 1, 2, 3), (1, 0, 2, 3))
    x42 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oooo += einsum(t1, (0, 1), x42, (2, 3, 4, 1), (0, 4, 2, 3))
    x43 = np.zeros((nocc, nocc), dtype=np.float64)
    x43 += einsum(delta.oo, (0, 1), (0, 1)) * -1.0
    x43 += einsum(x39, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x43, (2, 3), (3, 0, 2, 1)) * -1.0
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x44 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_ovvo += einsum(t2, (0, 1, 2, 3), x44, (4, 1, 5, 2), (0, 5, 3, 4)) * -1.0
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv += einsum(x44, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (4, 2, 5, 6)) * -0.5
    x45 = np.zeros((nocc, nocc), dtype=np.float64)
    x45 += einsum(x44, (0, 1, 2, 3), x6, (4, 0, 2, 3), (4, 1))
    x46 = np.zeros((nocc, nocc), dtype=np.float64)
    x46 += einsum(x39, (0, 1), (0, 1)) * 2.0
    x46 += einsum(x28, (0, 1), (0, 1))
    x46 += einsum(x29, (0, 1), (0, 1))
    x46 += einsum(x45, (0, 1), (1, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x46, (2, 3), (0, 3, 1, 2)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x46, (2, 3), (0, 3, 2, 1)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x46, (2, 3), (3, 0, 1, 2)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x46, (2, 3), (3, 0, 2, 1)) * -0.5
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x47 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x47 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x48 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x48 += einsum(x47, (0, 1, 2, 3), l3, (4, 3, 2, 5, 1, 6), (5, 6, 0, 4))
    x49 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x49 += einsum(t1, (0, 1), x48, (2, 3, 4, 1), (0, 2, 3, 4)) * 0.5
    rdm2_f_oooo += einsum(x49, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_oooo += einsum(x49, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x50 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x50 += einsum(t1, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x51 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x51 += einsum(t1, (0, 1), x50, (2, 3, 4, 5, 1, 6), (2, 3, 4, 0, 5, 6))
    x52 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x52 += einsum(t2, (0, 1, 2, 3), x51, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov += einsum(x52, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo += einsum(x52, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x53 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x53 += einsum(l2, (0, 1, 2, 3), t3, (4, 3, 5, 6, 1, 0), (2, 4, 5, 6))
    rdm2_f_ooov += einsum(x53, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x53, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x54 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x54 += einsum(t2, (0, 1, 2, 3), x41, (4, 1, 5, 3), (4, 5, 0, 2))
    x55 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum(t1, (0, 1), l3, (2, 1, 3, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x56 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x56 += einsum(t3, (0, 1, 2, 3, 4, 5), x55, (0, 6, 2, 7, 3, 5), (6, 7, 1, 4))
    x57 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(t1, (0, 1), l3, (1, 2, 3, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x58 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x58 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x58 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 5.0
    x58 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x58 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x58 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x58 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    x59 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x59 += einsum(x57, (0, 1, 2, 3, 4, 5), x58, (6, 1, 2, 7, 5, 4), (0, 3, 6, 7)) * 0.25
    x60 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x60 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x60 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x60 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x61 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x61 += einsum(x57, (0, 1, 2, 3, 4, 5), x60, (6, 0, 2, 7, 5, 4), (1, 3, 6, 7)) * 0.25
    x62 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x62 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x62 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3))
    x63 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x63 += einsum(x6, (0, 1, 2, 3), x62, (4, 1, 5, 3), (0, 4, 5, 2))
    x64 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x64 += einsum(t2, (0, 1, 2, 3), x34, (4, 1, 5, 3), (4, 5, 0, 2)) * -0.5
    x65 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x65 += einsum(t1, (0, 1), x16, (2, 3, 4, 1), (0, 2, 3, 4)) * -1.0
    x66 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x66 += einsum(t1, (0, 1), x19, (2, 3, 4, 1), (0, 2, 3, 4)) * 3.0
    x67 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x67 += einsum(x65, (0, 1, 2, 3), (1, 2, 0, 3))
    x67 += einsum(x65, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x67 += einsum(x66, (0, 1, 2, 3), (1, 2, 0, 3))
    x68 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x68 += einsum(t1, (0, 1), x67, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.5
    x69 = np.zeros((nocc, nocc), dtype=np.float64)
    x69 += einsum(l3, (0, 1, 2, 3, 4, 5), x0, (6, 4, 5, 0, 2, 1), (3, 6)) * 0.58333333333331
    x70 = np.zeros((nocc, nocc), dtype=np.float64)
    x70 += einsum(l3, (0, 1, 2, 3, 4, 5), x2, (3, 6, 5, 0, 1, 2), (4, 6)) * 0.08333333333333
    x71 = np.zeros((nocc, nocc), dtype=np.float64)
    x71 += einsum(l2, (0, 1, 2, 3), x4, (4, 3, 0, 1), (4, 2)) * 1.5
    x72 = np.zeros((nocc, nocc), dtype=np.float64)
    x72 += einsum(l2, (0, 1, 2, 3), x6, (4, 2, 0, 1), (4, 3)) * 0.5
    x73 = np.zeros((nocc, nocc), dtype=np.float64)
    x73 += einsum(x21, (0, 1), (0, 1))
    x73 += einsum(x69, (0, 1), (0, 1))
    x73 += einsum(x70, (0, 1), (0, 1))
    x73 += einsum(x71, (0, 1), (1, 0))
    x73 += einsum(x72, (0, 1), (1, 0))
    x74 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x74 += einsum(delta.oo, (0, 1), t1, (2, 3), (0, 1, 2, 3))
    x74 += einsum(x54, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x74 += einsum(x56, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.25
    x74 += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x74 += einsum(x61, (0, 1, 2, 3), (1, 0, 2, 3))
    x74 += einsum(x63, (0, 1, 2, 3), (2, 1, 0, 3))
    x74 += einsum(x64, (0, 1, 2, 3), (2, 0, 1, 3))
    x74 += einsum(x68, (0, 1, 2, 3), (1, 0, 2, 3))
    x74 += einsum(t1, (0, 1), x73, (2, 3), (0, 2, 3, 1))
    rdm2_f_ooov += einsum(x74, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x74, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x74, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x74, (0, 1, 2, 3), (2, 0, 3, 1))
    x75 = np.zeros((nocc, nvir), dtype=np.float64)
    x75 += einsum(t3, (0, 1, 2, 3, 4, 5), x55, (0, 1, 2, 6, 3, 5), (6, 4))
    x76 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * 0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * 0.14285714285714288
    x76 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * 0.14285714285714288
    x77 = np.zeros((nocc, nvir), dtype=np.float64)
    x77 += einsum(x57, (0, 1, 2, 3, 4, 5), x76, (1, 0, 2, 6, 5, 4), (3, 6)) * 0.58333333333331
    x78 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 5.0
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    x78 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x79 = np.zeros((nocc, nvir), dtype=np.float64)
    x79 += einsum(l2, (0, 1, 2, 3), x78, (4, 2, 3, 5, 1, 0), (4, 5)) * 0.25
    x80 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x80 += einsum(x18, (0, 1, 2, 3), l3, (3, 2, 4, 5, 1, 6), (5, 6, 0, 4)) * 3.0
    x81 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x81 += einsum(x13, (0, 1, 2, 3), l3, (3, 2, 4, 1, 5, 6), (5, 6, 0, 4))
    x82 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x82 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x82 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x82 += einsum(x81, (0, 1, 2, 3), (1, 0, 2, 3))
    x83 = np.zeros((nocc, nvir), dtype=np.float64)
    x83 += einsum(x13, (0, 1, 2, 3), x82, (0, 1, 4, 2), (4, 3)) * 0.25
    x84 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x84 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 1, 5, 6), (5, 6, 0, 4))
    x85 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x85 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x85 += einsum(x84, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x86 = np.zeros((nocc, nvir), dtype=np.float64)
    x86 += einsum(x6, (0, 1, 2, 3), x85, (1, 0, 4, 3), (4, 2)) * 0.25
    x87 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x87 += einsum(x13, (0, 1, 2, 3), l3, (2, 4, 3, 1, 5, 6), (5, 6, 0, 4))
    x88 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x88 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x88 += einsum(x87, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x89 = np.zeros((nocc, nvir), dtype=np.float64)
    x89 += einsum(t2, (0, 1, 2, 3), x88, (0, 1, 4, 3), (4, 2)) * 0.5
    x90 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x90 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 1, 5, 6), (5, 6, 0, 4))
    rdm2_f_ooov += einsum(x18, (0, 1, 2, 3), x90, (4, 1, 5, 2), (5, 0, 4, 3)) * -1.5
    x91 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x91 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x91 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.2
    x92 = np.zeros((nocc, nvir), dtype=np.float64)
    x92 += einsum(x90, (0, 1, 2, 3), x91, (0, 1, 4, 3), (2, 4)) * 1.25
    x93 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x93 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x93 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x94 = np.zeros((nocc, nvir), dtype=np.float64)
    x94 += einsum(l1, (0, 1), x93, (2, 1, 3, 0), (2, 3))
    x95 = np.zeros((nocc, nvir), dtype=np.float64)
    x95 += einsum(t1, (0, 1), x73, (0, 2), (2, 1))
    x96 = np.zeros((nocc, nvir), dtype=np.float64)
    x96 += einsum(x75, (0, 1), (0, 1)) * 0.24999999999999
    x96 += einsum(x77, (0, 1), (0, 1)) * -1.0
    x96 += einsum(x79, (0, 1), (0, 1)) * -1.0
    x96 += einsum(x83, (0, 1), (0, 1))
    x96 += einsum(x86, (0, 1), (0, 1)) * -1.0
    x96 += einsum(x89, (0, 1), (0, 1))
    x96 += einsum(x92, (0, 1), (0, 1))
    x96 += einsum(x94, (0, 1), (0, 1)) * -1.0
    x96 += einsum(x95, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x96, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x96, (2, 3), (2, 0, 1, 3))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x96, (2, 3), (0, 2, 3, 1))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x96, (2, 3), (2, 0, 3, 1)) * -1.0
    x97 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x97 += einsum(x44, (0, 1, 2, 3), x60, (4, 5, 0, 6, 2, 3), (1, 4, 5, 6)) * 0.5
    rdm2_f_ooov += einsum(x97, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_ooov += einsum(x97, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x97, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x97, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x98 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x98 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 5, 6, 1, 0), (6, 4, 5, 2))
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov += einsum(x98, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo += einsum(x98, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x99 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x99 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x99 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x99 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x100 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x100 += einsum(x99, (0, 1, 2, 3), l3, (4, 5, 2, 6, 0, 1), (6, 4, 5, 3))
    x101 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x101 += einsum(x6, (0, 1, 2, 3), l3, (4, 5, 2, 0, 6, 1), (6, 4, 5, 3))
    x102 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x102 += einsum(x98, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x102 += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3))
    x102 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    x103 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x103 += einsum(x102, (0, 1, 2, 3), x13, (4, 5, 2, 1), (4, 5, 0, 3)) * 0.25
    rdm2_f_ooov += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovo += einsum(x103, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x104 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x104 += einsum(t1, (0, 1), x55, (2, 3, 4, 5, 1, 6), (2, 3, 4, 0, 5, 6))
    rdm2_f_oovo += einsum(x6, (0, 1, 2, 3), x104, (0, 4, 1, 5, 6, 2), (5, 6, 3, 4)) * 0.5
    x105 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x105 += einsum(x99, (0, 1, 2, 3), x104, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    rdm2_f_ooov += einsum(x105, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x105, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x106 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x106 += einsum(x13, (0, 1, 2, 3), x104, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    rdm2_f_ooov += einsum(x106, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x106, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x106, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x106, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x106, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_oovo += einsum(x106, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x106, (0, 1, 2, 3), (2, 1, 3, 0))
    x107 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x107 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 5, 1, 6), (5, 6, 0, 4))
    x108 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x108 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 1), (5, 6, 0, 4))
    x109 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x109 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x109 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2))
    x110 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x110 += einsum(t2, (0, 1, 2, 3), x109, (4, 5, 1, 6, 2, 3), (4, 5, 0, 6))
    x111 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x111 += einsum(x107, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x111 += einsum(x108, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x111 += einsum(x108, (0, 1, 2, 3), (1, 0, 2, 3))
    x111 += einsum(x110, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x112 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x112 += einsum(x111, (0, 1, 2, 3), x6, (4, 1, 5, 3), (4, 0, 2, 5)) * 0.5
    rdm2_f_ooov += einsum(x112, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_oovo += einsum(x112, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x113 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x113 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x113 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -3.0
    x113 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x114 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x114 += einsum(t2, (0, 1, 2, 3), x113, (4, 5, 1, 2, 3, 6), (4, 5, 0, 6))
    x115 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x115 += einsum(t2, (0, 1, 2, 3), x109, (4, 5, 1, 3, 2, 6), (4, 5, 0, 6))
    x116 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x116 += einsum(x114, (0, 1, 2, 3), (0, 1, 2, 3))
    x116 += einsum(x115, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ooov += einsum(x116, (0, 1, 2, 3), x13, (4, 1, 3, 5), (2, 4, 0, 5)) * -0.5
    rdm2_f_oovo += einsum(x116, (0, 1, 2, 3), x6, (4, 1, 3, 5), (2, 4, 5, 0)) * -0.5
    x117 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x117 += einsum(x24, (0, 1, 2, 3), x4, (4, 0, 5, 3), (4, 1, 2, 5)) * 1.5
    rdm2_f_ooov += einsum(x117, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_oovo += einsum(x117, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x118 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x118 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x118 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x118 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x118 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 3.0
    x119 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x119 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3))
    x119 += einsum(x15, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x119 += einsum(l3, (0, 1, 2, 3, 4, 5), x118, (6, 7, 4, 1, 0, 2), (3, 5, 6, 7)) * 0.16666666666667
    rdm2_f_ooov += einsum(t1, (0, 1), x119, (2, 0, 3, 4), (3, 4, 2, 1))
    x120 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x120 += einsum(l1, (0, 1), x6, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x120, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x120, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x121 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x121 += einsum(t3, (0, 1, 2, 3, 4, 5), x57, (0, 6, 2, 7, 4, 5), (6, 7, 1, 3))
    rdm2_f_ooov += einsum(x121, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_ooov += einsum(x121, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_oovo += einsum(x121, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.5
    rdm2_f_oovo += einsum(x121, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.5
    x122 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x122 += einsum(t3, (0, 1, 2, 3, 4, 5), x55, (6, 1, 2, 7, 3, 5), (6, 7, 0, 4))
    rdm2_f_ooov += einsum(x122, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_ooov += einsum(x122, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_oovo += einsum(x122, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.5
    rdm2_f_oovo += einsum(x122, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.5
    x123 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x123 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 2, 6, 1, 0), (6, 4, 5, 3))
    rdm2_f_vvov += einsum(x123, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo += einsum(x123, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(t1, (0, 1), x123, (0, 2, 3, 4), (3, 2, 4, 1))
    x124 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x124 += einsum(t2, (0, 1, 2, 3), x123, (4, 2, 3, 5), (4, 0, 1, 5))
    rdm2_f_ooov += einsum(x124, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x124, (0, 1, 2, 3), (2, 1, 3, 0))
    x125 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x125 += einsum(t3, (0, 1, 2, 3, 4, 5), x57, (0, 6, 2, 7, 5, 3), (6, 7, 1, 4))
    rdm2_f_ooov += einsum(x125, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_ooov += einsum(x125, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_oovo += einsum(x125, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    rdm2_f_oovo += einsum(x125, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    x126 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x126 += einsum(t2, (0, 1, 2, 3), x104, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    rdm2_f_ooov += einsum(x126, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x126, (0, 1, 2, 3), (2, 1, 3, 0))
    x127 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x127 += einsum(l2, (0, 1, 2, 3), t3, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6))
    rdm2_f_ooov += einsum(x127, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x127, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x128 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x128 += einsum(l1, (0, 1), t2, (2, 3, 0, 4), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x128, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x128, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x129 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x129 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x129 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * 4.0
    x129 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x130 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x130 += einsum(x129, (0, 1, 2, 3, 4, 5), x57, (6, 2, 0, 7, 5, 3), (6, 7, 1, 4)) * 0.25
    rdm2_f_ooov += einsum(x130, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x130, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x130, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x130, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x131 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x131 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x131 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x131 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x132 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x132 += einsum(x131, (0, 1, 2, 3, 4, 5), x55, (1, 6, 2, 7, 5, 4), (6, 7, 0, 3)) * 0.25
    rdm2_f_ooov += einsum(x132, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_ooov += einsum(x132, (0, 1, 2, 3), (1, 2, 0, 3))
    x133 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x133 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x133 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm2_f_vovo += einsum(t2, (0, 1, 2, 3), x133, (4, 1, 5, 2), (5, 0, 3, 4)) * -1.0
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv += einsum(x133, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (2, 4, 5, 6)) * -0.5
    x134 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x134 += einsum(x133, (0, 1, 2, 3), t3, (4, 5, 0, 2, 6, 3), (4, 5, 1, 6)) * 0.5
    rdm2_f_ooov += einsum(x134, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_ooov += einsum(x134, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovo += einsum(x134, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_oovo += einsum(x134, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x135 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x135 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x135 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x136 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x136 += einsum(x13, (0, 1, 2, 3), x135, (4, 5, 1, 2, 3, 6), (0, 4, 5, 6))
    x137 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x137 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x137 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x138 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x138 += einsum(x137, (0, 1, 2, 3), l3, (2, 3, 4, 5, 1, 6), (5, 6, 0, 4))
    x139 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x139 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x139 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x139 += einsum(x136, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x139 += einsum(x138, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ooov += einsum(t2, (0, 1, 2, 3), x139, (4, 0, 5, 2), (5, 1, 4, 3)) * -0.5
    x140 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x140 += einsum(x13, (0, 1, 2, 3), l3, (3, 4, 2, 5, 6, 1), (5, 6, 0, 4)) * 0.5
    x141 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x141 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3))
    x141 += einsum(x90, (0, 1, 2, 3), (0, 1, 2, 3))
    x141 += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_ooov += einsum(x141, (0, 1, 2, 3), x6, (4, 1, 3, 5), (2, 4, 0, 5)) * -1.0
    x142 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x142 += einsum(x13, (0, 1, 2, 3), l3, (4, 5, 2, 0, 6, 1), (6, 4, 5, 3))
    x143 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x143 += einsum(t2, (0, 1, 2, 3), x142, (4, 3, 2, 5), (4, 0, 1, 5)) * -0.5
    rdm2_f_ooov += einsum(x143, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x143, (0, 1, 2, 3), (2, 1, 3, 0))
    x144 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x144 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x144 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x144 += einsum(x34, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_ooov += einsum(t2, (0, 1, 2, 3), x144, (4, 1, 5, 2), (0, 5, 4, 3)) * 0.5
    rdm2_f_oovo += einsum(t2, (0, 1, 2, 3), x144, (1, 4, 5, 2), (0, 5, 3, 4)) * 0.5
    rdm2_f_vovo += einsum(t1, (0, 1), x144, (0, 2, 3, 4), (4, 3, 1, 2)) * -0.5
    x145 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x145 += einsum(t1, (0, 1), x34, (2, 3, 4, 1), (0, 2, 3, 4)) * -0.99999999999998
    x146 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x146 += einsum(t1, (0, 1), x37, (2, 3, 4, 1), (0, 2, 3, 4)) * 1.99999999999996
    x147 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x147 += einsum(x26, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.99999999999996
    x147 += einsum(x25, (0, 1, 2, 3), (1, 0, 3, 2)) * 1.99999999999996
    x147 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3))
    x147 += einsum(x33, (0, 1, 2, 3), (1, 0, 3, 2))
    x147 += einsum(x145, (0, 1, 2, 3), (1, 2, 3, 0))
    x147 += einsum(x145, (0, 1, 2, 3), (2, 1, 0, 3))
    x147 += einsum(x146, (0, 1, 2, 3), (1, 2, 0, 3))
    x148 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x148 += einsum(t1, (0, 1), x147, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.50000000000001
    rdm2_f_ooov += einsum(x148, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x148, (0, 1, 2, 3), (2, 1, 3, 0))
    x149 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x149 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 0, 5, 6), (5, 6, 1, 4))
    x150 = np.zeros((nocc, nvir), dtype=np.float64)
    x150 += einsum(t2, (0, 1, 2, 3), x149, (1, 0, 4, 2), (4, 3))
    x151 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 5.0
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    x151 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x152 = np.zeros((nocc, nvir), dtype=np.float64)
    x152 += einsum(l2, (0, 1, 2, 3), x151, (4, 2, 3, 5, 1, 0), (4, 5)) * 0.25
    x153 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x153 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 5, 0, 6), (5, 6, 1, 4))
    x154 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x154 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x154 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2))
    x155 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x155 += einsum(x13, (0, 1, 2, 3), x154, (4, 1, 5, 3, 2, 6), (0, 4, 5, 6))
    x156 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x156 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x156 += einsum(x155, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x157 = np.zeros((nocc, nvir), dtype=np.float64)
    x157 += einsum(x156, (0, 1, 2, 3), x6, (0, 1, 3, 4), (2, 4)) * 0.25
    x158 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x158 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x158 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x158 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x158 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x159 = np.zeros((nocc, nvir), dtype=np.float64)
    x159 += einsum(x158, (0, 1, 2, 3), x9, (1, 0, 4, 3), (4, 2)) * 1.5
    x160 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x160 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x160 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * 0.5
    x161 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x161 += einsum(x13, (0, 1, 2, 3), x160, (1, 4, 5, 2, 6, 3), (0, 4, 5, 6))
    x162 = np.zeros((nocc, nvir), dtype=np.float64)
    x162 += einsum(t2, (0, 1, 2, 3), x161, (4, 0, 1, 2), (4, 3)) * 0.5
    x163 = np.zeros((nocc, nvir), dtype=np.float64)
    x163 += einsum(t2, (0, 1, 2, 3), x81, (0, 1, 4, 3), (4, 2)) * -0.25
    x164 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x164 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x164 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x164 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x165 = np.zeros((nocc, nvir), dtype=np.float64)
    x165 += einsum(l1, (0, 1), x164, (1, 2, 0, 3), (2, 3))
    x166 = np.zeros((nocc, nocc), dtype=np.float64)
    x166 += einsum(x44, (0, 1, 2, 3), x6, (4, 0, 2, 3), (4, 1)) * 0.5
    x167 = np.zeros((nocc, nocc), dtype=np.float64)
    x167 += einsum(x21, (0, 1), (0, 1))
    x167 += einsum(x39, (0, 1), (0, 1))
    x167 += einsum(x69, (0, 1), (0, 1))
    x167 += einsum(x70, (0, 1), (0, 1))
    x167 += einsum(x166, (0, 1), (1, 0))
    x168 = np.zeros((nocc, nvir), dtype=np.float64)
    x168 += einsum(t1, (0, 1), x167, (0, 2), (2, 1))
    x169 = np.zeros((nocc, nvir), dtype=np.float64)
    x169 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x169 += einsum(x75, (0, 1), (0, 1)) * 0.24999999999999
    x169 += einsum(x150, (0, 1), (0, 1))
    x169 += einsum(x77, (0, 1), (0, 1)) * -1.0
    x169 += einsum(x152, (0, 1), (0, 1)) * -1.0
    x169 += einsum(x157, (0, 1), (0, 1))
    x169 += einsum(x159, (0, 1), (0, 1))
    x169 += einsum(x162, (0, 1), (0, 1)) * -1.0
    x169 += einsum(x163, (0, 1), (0, 1)) * -1.0
    x169 += einsum(x165, (0, 1), (0, 1)) * -1.0
    x169 += einsum(x168, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x169, (2, 3), (0, 2, 1, 3)) * -1.0
    x170 = np.zeros((nocc, nocc), dtype=np.float64)
    x170 += einsum(l3, (0, 1, 2, 3, 4, 5), x0, (6, 4, 5, 0, 2, 1), (3, 6)) * 6.999999999999999
    x171 = np.zeros((nocc, nocc), dtype=np.float64)
    x171 += einsum(l3, (0, 1, 2, 3, 4, 5), x2, (3, 6, 5, 0, 1, 2), (4, 6))
    x172 = np.zeros((nocc, nocc), dtype=np.float64)
    x172 += einsum(l2, (0, 1, 2, 3), x4, (4, 3, 0, 1), (4, 2)) * 18.00000000000072
    x173 = np.zeros((nocc, nocc), dtype=np.float64)
    x173 += einsum(l2, (0, 1, 2, 3), x6, (4, 2, 0, 1), (4, 3)) * 6.00000000000024
    x174 = np.zeros((nocc, nocc), dtype=np.float64)
    x174 += einsum(x21, (0, 1), (0, 1)) * 12.00000000000048
    x174 += einsum(x170, (0, 1), (0, 1))
    x174 += einsum(x171, (0, 1), (0, 1))
    x174 += einsum(x172, (0, 1), (1, 0))
    x174 += einsum(x173, (0, 1), (1, 0))
    rdm2_f_ooov += einsum(t1, (0, 1), x174, (2, 3), (3, 0, 2, 1)) * -0.08333333333333
    rdm2_f_oovo += einsum(t1, (0, 1), x174, (2, 3), (0, 3, 1, 2)) * -0.08333333333333
    x175 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x175 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    rdm2_f_vovv += einsum(x175, (0, 1, 2, 3), x6, (4, 0, 5, 1), (2, 4, 3, 5)) * -1.0
    rdm2_f_vvov += einsum(x175, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo += einsum(x175, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_vvvv += einsum(t1, (0, 1), x175, (0, 2, 3, 4), (3, 2, 4, 1))
    x176 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x176 += einsum(t2, (0, 1, 2, 3), x175, (4, 3, 2, 5), (4, 0, 1, 5))
    rdm2_f_ooov += einsum(x176, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x176, (0, 1, 2, 3), (1, 2, 3, 0))
    x177 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x177 += einsum(t2, (0, 1, 2, 3), x104, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    rdm2_f_ooov += einsum(x177, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x177, (0, 1, 2, 3), (2, 1, 3, 0))
    x178 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x178 += einsum(l2, (0, 1, 2, 3), t3, (4, 5, 2, 6, 1, 0), (3, 4, 5, 6))
    rdm2_f_ooov += einsum(x178, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x178, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x179 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x179 += einsum(l1, (0, 1), t2, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x179, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x179, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x180 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x180 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x180 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1))
    x180 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2))
    x180 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * -1.0
    x181 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x181 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x181 += einsum(x149, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x181 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x181 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * 4.0
    x181 += einsum(x13, (0, 1, 2, 3), x180, (4, 5, 1, 3, 2, 6), (4, 5, 0, 6)) * -1.0
    rdm2_f_ooov += einsum(t2, (0, 1, 2, 3), x181, (4, 1, 5, 3), (5, 0, 4, 2)) * -0.5
    x182 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x182 += einsum(t2, (0, 1, 2, 3), x142, (4, 2, 3, 5), (4, 0, 1, 5)) * -0.5
    rdm2_f_ooov += einsum(x182, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x182, (0, 1, 2, 3), (1, 2, 3, 0))
    x183 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x183 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3))
    x183 += einsum(x149, (0, 1, 2, 3), (0, 1, 2, 3))
    x183 += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_ooov += einsum(t2, (0, 1, 2, 3), x183, (4, 1, 5, 2), (5, 0, 4, 3))
    x184 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x184 += einsum(x13, (0, 1, 2, 3), l3, (2, 4, 3, 5, 6, 1), (5, 6, 0, 4))
    x185 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x185 += einsum(x41, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x185 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x185 += einsum(x184, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_ooov += einsum(t2, (0, 1, 2, 3), x185, (4, 0, 5, 3), (1, 5, 4, 2)) * 0.5
    rdm2_f_oovo += einsum(x185, (0, 1, 2, 3), x6, (4, 0, 5, 3), (4, 2, 5, 1)) * 0.5
    x186 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x186 += einsum(t1, (0, 1), x147, (0, 2, 3, 4), (2, 3, 4, 1)) * 0.50000000000001
    rdm2_f_ooov += einsum(x186, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x186, (0, 1, 2, 3), (1, 2, 3, 0))
    x187 = np.zeros((nocc, nvir), dtype=np.float64)
    x187 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x187 += einsum(x75, (0, 1), (0, 1)) * 0.24999999999999
    x187 += einsum(x77, (0, 1), (0, 1)) * -1.0
    x187 += einsum(x79, (0, 1), (0, 1)) * -1.0
    x187 += einsum(x83, (0, 1), (0, 1))
    x187 += einsum(x86, (0, 1), (0, 1)) * -1.0
    x187 += einsum(x89, (0, 1), (0, 1))
    x187 += einsum(x92, (0, 1), (0, 1))
    x187 += einsum(x94, (0, 1), (0, 1)) * -1.0
    x187 += einsum(x95, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x187, (2, 3), (0, 2, 1, 3)) * -1.0
    x188 = np.zeros((nocc, nocc), dtype=np.float64)
    x188 += einsum(x44, (0, 1, 2, 3), x6, (4, 0, 2, 3), (4, 1)) * 6.00000000000024
    x189 = np.zeros((nocc, nocc), dtype=np.float64)
    x189 += einsum(x21, (0, 1), (0, 1)) * 12.00000000000048
    x189 += einsum(x39, (0, 1), (0, 1)) * 12.00000000000048
    x189 += einsum(x170, (0, 1), (0, 1))
    x189 += einsum(x171, (0, 1), (0, 1))
    x189 += einsum(x188, (0, 1), (1, 0))
    rdm2_f_ooov += einsum(t1, (0, 1), x189, (2, 3), (3, 0, 2, 1)) * -0.08333333333333
    rdm2_f_oovo += einsum(t1, (0, 1), x189, (2, 3), (0, 3, 1, 2)) * -0.08333333333333
    x190 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x190 += einsum(t2, (0, 1, 2, 3), x36, (0, 4, 5, 2), (4, 1, 5, 3))
    rdm2_f_ooov += einsum(x190, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x190, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x191 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x191 += einsum(t2, (0, 1, 2, 3), x149, (4, 0, 5, 2), (4, 1, 5, 3))
    rdm2_f_ooov += einsum(x191, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x191, (0, 1, 2, 3), (2, 1, 3, 0))
    x192 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x192 += einsum(t2, (0, 1, 2, 3), x51, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3))
    rdm2_f_ooov += einsum(x192, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x192, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x193 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x193 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 5, 6, 0, 1), (3, 4, 5, 6))
    rdm2_f_ooov += einsum(x193, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x193, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x194 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x194 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x194 += einsum(x34, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x195 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x195 += einsum(t2, (0, 1, 2, 3), x194, (4, 0, 5, 2), (4, 5, 1, 3)) * 0.5
    x196 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x196 += einsum(t1, (0, 1), x48, (2, 3, 4, 1), (0, 2, 3, 4))
    x197 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x197 += einsum(x65, (0, 1, 2, 3), (1, 2, 0, 3))
    x197 += einsum(x65, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x197 += einsum(x196, (0, 1, 2, 3), (1, 2, 0, 3))
    x198 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x198 += einsum(t1, (0, 1), x197, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.5
    x199 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x199 += einsum(delta.oo, (0, 1), t1, (2, 3), (0, 1, 2, 3))
    x199 += einsum(x56, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.25
    x199 += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x199 += einsum(x61, (0, 1, 2, 3), (1, 0, 2, 3))
    x199 += einsum(x63, (0, 1, 2, 3), (2, 1, 0, 3))
    x199 += einsum(x195, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x199 += einsum(x198, (0, 1, 2, 3), (1, 0, 2, 3))
    x199 += einsum(t1, (0, 1), x167, (2, 3), (0, 2, 3, 1))
    rdm2_f_ooov += einsum(x199, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x199, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x199, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x199, (0, 1, 2, 3), (2, 0, 3, 1))
    x200 = np.zeros((nocc, nvir), dtype=np.float64)
    x200 += einsum(x75, (0, 1), (0, 1)) * 0.24999999999999
    x200 += einsum(x150, (0, 1), (0, 1))
    x200 += einsum(x77, (0, 1), (0, 1)) * -1.0
    x200 += einsum(x152, (0, 1), (0, 1)) * -1.0
    x200 += einsum(x157, (0, 1), (0, 1))
    x200 += einsum(x159, (0, 1), (0, 1))
    x200 += einsum(x162, (0, 1), (0, 1)) * -1.0
    x200 += einsum(x163, (0, 1), (0, 1)) * -1.0
    x200 += einsum(x165, (0, 1), (0, 1)) * -1.0
    x200 += einsum(x168, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x200, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x200, (2, 3), (2, 0, 1, 3))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x200, (2, 3), (0, 2, 3, 1))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x200, (2, 3), (2, 0, 3, 1)) * -1.0
    x201 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x201 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 5, 6, 0, 1), (6, 4, 5, 3))
    rdm2_f_vvov += einsum(x201, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo += einsum(x201, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x202 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x202 += einsum(x201, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x202 += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3))
    x202 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    x203 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x203 += einsum(x13, (0, 1, 2, 3), x202, (4, 3, 2, 5), (0, 1, 4, 5)) * 0.25
    rdm2_f_ooov += einsum(x203, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovo += einsum(x203, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x204 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x204 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x204 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x204 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_ovoo += einsum(x204, (0, 1, 2, 3), l3, (4, 2, 3, 5, 0, 6), (1, 4, 5, 6)) * 0.5
    x205 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x205 += einsum(x204, (0, 1, 2, 3), l3, (4, 2, 3, 5, 0, 6), (5, 6, 1, 4))
    x206 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x206 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x206 += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    x206 += einsum(x205, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ooov += einsum(x206, (0, 1, 2, 3), x6, (4, 1, 5, 3), (4, 2, 0, 5)) * 0.5
    rdm2_f_oovo += einsum(x13, (0, 1, 2, 3), x206, (4, 1, 5, 3), (0, 5, 2, 4)) * 0.5
    x207 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x207 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x207 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2)) * -1.0
    x207 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    x208 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x208 += einsum(x13, (0, 1, 2, 3), x207, (4, 5, 1, 2, 3, 6), (0, 4, 5, 6))
    x209 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x209 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x209 += einsum(x208, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x210 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x210 += einsum(x13, (0, 1, 2, 3), x209, (4, 1, 5, 2), (0, 4, 5, 3)) * 0.5
    rdm2_f_ooov += einsum(x210, (0, 1, 2, 3), (2, 0, 1, 3))
    rdm2_f_oovo += einsum(x210, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x211 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x211 += einsum(l3, (0, 1, 2, 3, 4, 5), x11, (6, 7, 5, 1, 0, 2), (3, 4, 6, 7)) * 0.33333333333334
    x212 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x212 += einsum(l2, (0, 1, 2, 3), x13, (4, 5, 1, 0), (4, 5, 2, 3))
    x213 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x213 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x213 += einsum(x211, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x213 += einsum(x212, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x214 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x214 += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3))
    x214 += einsum(x213, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x214 += einsum(l3, (0, 1, 2, 3, 4, 5), x118, (6, 7, 4, 1, 0, 2), (3, 5, 6, 7)) * 0.33333333333334
    rdm2_f_ooov += einsum(t1, (0, 1), x214, (2, 0, 3, 4), (3, 4, 2, 1)) * 0.5
    x215 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x215 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x215 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x215 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x215 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x216 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x216 += einsum(x215, (0, 1, 2, 3), x104, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2)) * 0.5
    rdm2_f_oovo += einsum(x216, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_oovo += einsum(x216, (0, 1, 2, 3), (2, 1, 3, 0))
    x217 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x217 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x217 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 3.0
    rdm2_f_oovo += einsum(x217, (0, 1, 2, 3), x90, (4, 1, 5, 2), (5, 0, 3, 4)) * 0.5
    rdm2_f_vooo += einsum(x217, (0, 1, 2, 3), l3, (4, 2, 3, 5, 1, 6), (4, 0, 5, 6)) * -0.5
    x218 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x218 += einsum(l3, (0, 1, 2, 3, 4, 5), x11, (6, 7, 5, 1, 0, 2), (3, 4, 6, 7))
    x219 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x219 += einsum(l2, (0, 1, 2, 3), x13, (4, 5, 1, 0), (4, 5, 2, 3)) * 2.99999999999994
    x220 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x220 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.99999999999988
    x220 += einsum(x218, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x220 += einsum(x219, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x221 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x221 += einsum(l3, (0, 1, 2, 3, 4, 5), x118, (6, 7, 4, 1, 0, 2), (3, 5, 6, 7))
    x222 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x222 += einsum(x220, (0, 1, 2, 3), (0, 1, 2, 3))
    x222 += einsum(x220, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x222 += einsum(x221, (0, 1, 2, 3), (0, 1, 2, 3))
    x223 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x223 += einsum(t1, (0, 1), x222, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.16666666666667
    rdm2_f_oovo += einsum(x223, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x223, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x224 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x224 += einsum(l1, (0, 1), x13, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_oovo += einsum(x224, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x224, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x225 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x225 += einsum(x11, (0, 1, 2, 3, 4, 5), x55, (1, 6, 2, 7, 3, 5), (0, 6, 7, 4)) * 0.25
    rdm2_f_oovo += einsum(x225, (0, 1, 2, 3), (0, 2, 3, 1))
    rdm2_f_oovo += einsum(x225, (0, 1, 2, 3), (0, 2, 3, 1))
    x226 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x226 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 0, 6), (5, 6, 1, 4))
    x227 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x227 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x227 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 0, 2))
    x228 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x228 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x228 += einsum(x226, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.0
    x228 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x228 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.0
    x228 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x228 += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    x228 += einsum(x13, (0, 1, 2, 3), x227, (4, 5, 1, 3, 6, 2), (5, 4, 0, 6)) * -1.0
    rdm2_f_oovo += einsum(t2, (0, 1, 2, 3), x228, (1, 4, 5, 3), (0, 5, 2, 4)) * -0.5
    x229 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x229 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 1), (5, 6, 0, 4))
    x230 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x230 += einsum(x41, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.0
    x230 += einsum(x229, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x230 += einsum(x87, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovo += einsum(t2, (0, 1, 2, 3), x230, (4, 0, 5, 3), (5, 1, 2, 4)) * -0.5
    x231 = np.zeros((nocc, nvir), dtype=np.float64)
    x231 += einsum(x57, (0, 1, 2, 3, 4, 5), x76, (1, 0, 2, 6, 5, 4), (3, 6)) * 2.33333333333324
    x232 = np.zeros((nocc, nvir), dtype=np.float64)
    x232 += einsum(t1, (0, 1), (0, 1)) * -4.0
    x232 += einsum(x75, (0, 1), (0, 1)) * 0.99999999999996
    x232 += einsum(x231, (0, 1), (0, 1)) * -1.0
    x232 += einsum(l2, (0, 1, 2, 3), x78, (4, 2, 3, 5, 1, 0), (4, 5)) * -1.0
    x232 += einsum(x13, (0, 1, 2, 3), x82, (0, 1, 4, 2), (4, 3))
    x232 += einsum(x6, (0, 1, 2, 3), x85, (1, 0, 4, 3), (4, 2)) * -1.0
    x232 += einsum(t2, (0, 1, 2, 3), x88, (0, 1, 4, 3), (4, 2)) * 2.0
    x232 += einsum(x90, (0, 1, 2, 3), x91, (0, 1, 4, 3), (2, 4)) * 5.0
    x232 += einsum(l1, (0, 1), x93, (2, 1, 3, 0), (2, 3)) * -4.0
    x232 += einsum(t1, (0, 1), x73, (0, 2), (2, 1)) * 4.0
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x232, (2, 3), (2, 0, 3, 1)) * -0.25
    x233 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x233 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x233 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x234 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x234 += einsum(x18, (0, 1, 2, 3), l3, (4, 2, 3, 5, 1, 6), (5, 6, 0, 4)) * 3.0
    x235 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x235 += einsum(x233, (0, 1, 2, 3), (0, 1, 2, 3))
    x235 += einsum(x233, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x235 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovo += einsum(t2, (0, 1, 2, 3), x235, (4, 0, 5, 2), (1, 5, 3, 4)) * 0.5
    x236 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x236 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 5, 6, 0), (5, 6, 1, 4))
    x237 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x237 += einsum(x13, (0, 1, 2, 3), l3, (3, 4, 2, 1, 5, 6), (5, 6, 0, 4))
    x238 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x238 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x238 += einsum(x236, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x238 += einsum(x237, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovo += einsum(t2, (0, 1, 2, 3), x238, (4, 1, 5, 2), (5, 0, 3, 4)) * -0.5
    x239 = np.zeros((nocc, nvir), dtype=np.float64)
    x239 += einsum(t1, (0, 1), (0, 1)) * -4.0
    x239 += einsum(x75, (0, 1), (0, 1)) * 0.99999999999996
    x239 += einsum(x150, (0, 1), (0, 1)) * 4.0
    x239 += einsum(x231, (0, 1), (0, 1)) * -1.0
    x239 += einsum(l2, (0, 1, 2, 3), x151, (4, 2, 3, 5, 1, 0), (4, 5)) * -1.0
    x239 += einsum(x156, (0, 1, 2, 3), x6, (0, 1, 3, 4), (2, 4))
    x239 += einsum(x158, (0, 1, 2, 3), x9, (1, 0, 4, 3), (4, 2)) * 6.0
    x239 += einsum(t2, (0, 1, 2, 3), x161, (4, 0, 1, 2), (4, 3)) * -2.0
    x239 += einsum(t2, (0, 1, 2, 3), x81, (0, 1, 4, 3), (4, 2))
    x239 += einsum(l1, (0, 1), x164, (1, 2, 0, 3), (2, 3)) * -4.0
    x239 += einsum(t1, (0, 1), x167, (0, 2), (2, 1)) * 4.0
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x239, (2, 3), (2, 0, 3, 1)) * -0.25
    x240 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x240 += einsum(x13, (0, 1, 2, 3), l3, (4, 3, 2, 5, 6, 1), (5, 6, 0, 4)) * 0.5
    x241 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x241 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x241 += einsum(x240, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_ovoo += einsum(x241, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_ovoo += einsum(x241, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_ovoo += einsum(x241, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_ovoo += einsum(x241, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x241, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x241, (0, 1, 2, 3), (3, 2, 1, 0))
    rdm2_f_vooo += einsum(x241, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x241, (0, 1, 2, 3), (3, 2, 1, 0))
    x242 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x242 += einsum(x6, (0, 1, 2, 3), l3, (3, 4, 2, 5, 6, 1), (5, 6, 0, 4)) * 0.5
    rdm2_f_ovoo += einsum(x242, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_ovoo += einsum(x242, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x242, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x242, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x243 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x243 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x243 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x243 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    rdm2_f_vooo += einsum(x243, (0, 1, 2, 3), l3, (4, 2, 3, 5, 1, 6), (4, 0, 5, 6)) * -0.5
    x244 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x244 += einsum(x21, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4))
    x245 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x245 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 5, 4, 7, 2, 1), (3, 6, 0, 7))
    rdm2_f_ovvo += einsum(x245, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_ovvo += einsum(x245, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x245, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_voov += einsum(x245, (0, 1, 2, 3), (2, 1, 0, 3))
    x246 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x246 += einsum(t2, (0, 1, 2, 3), x245, (1, 4, 2, 5), (0, 4, 3, 5))
    x247 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x247 += einsum(t2, (0, 1, 2, 3), x55, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    rdm2_f_ovvo += einsum(x247, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x247, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x248 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x248 += einsum(t2, (0, 1, 2, 3), x247, (1, 4, 3, 5), (4, 0, 2, 5))
    x249 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x249 += einsum(x13, (0, 1, 2, 3), l3, (2, 3, 4, 1, 5, 6), (5, 6, 0, 4)) * 0.5
    x250 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x250 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3))
    x250 += einsum(x249, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x251 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x251 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x251 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x252 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x252 += einsum(x250, (0, 1, 2, 3), x251, (4, 1, 0, 5, 6, 3), (2, 4, 5, 6)) * 0.5
    x253 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x253 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7))
    rdm2_f_ovov += einsum(x253, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_ovov += einsum(x253, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_ovvo += einsum(x253, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.25
    rdm2_f_ovvo += einsum(x253, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.25
    rdm2_f_voov += einsum(x253, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.25
    rdm2_f_voov += einsum(x253, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.25
    rdm2_f_vovo += einsum(x253, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    rdm2_f_vovo += einsum(x253, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    x254 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x254 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x254 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -5.0
    x254 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x254 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x254 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x255 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x255 += einsum(l3, (0, 1, 2, 3, 4, 5), x254, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7))
    x256 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x256 += einsum(l3, (0, 1, 2, 3, 4, 5), x60, (6, 3, 5, 7, 2, 1), (4, 6, 0, 7))
    x257 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x257 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x257 += einsum(x255, (0, 1, 2, 3), (0, 1, 2, 3))
    x257 += einsum(x256, (0, 1, 2, 3), (0, 1, 2, 3))
    x258 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x258 += einsum(x13, (0, 1, 2, 3), x257, (1, 4, 2, 5), (0, 4, 3, 5)) * 0.25
    x259 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x259 += einsum(x18, (0, 1, 2, 3), l3, (3, 2, 4, 5, 1, 6), (5, 6, 0, 4))
    x260 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x260 += einsum(x259, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 2, 5, 6)) * 0.75
    x261 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x261 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 2, 7, 1), (4, 6, 0, 7))
    x262 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x262 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.2
    x262 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x262 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -0.2
    x263 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x263 += einsum(l3, (0, 1, 2, 3, 4, 5), x262, (5, 6, 4, 2, 7, 1), (3, 6, 0, 7)) * 5.0
    x264 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x264 += einsum(l3, (0, 1, 2, 3, 4, 5), x131, (6, 3, 5, 7, 2, 0), (4, 6, 1, 7))
    x265 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x265 += einsum(x261, (0, 1, 2, 3), (0, 1, 2, 3))
    x265 += einsum(x263, (0, 1, 2, 3), (0, 1, 2, 3))
    x265 += einsum(x264, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x266 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x266 += einsum(t2, (0, 1, 2, 3), x265, (1, 4, 3, 5), (4, 0, 5, 2)) * 0.25
    x267 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x267 += einsum(x13, (0, 1, 2, 3), l3, (4, 3, 2, 1, 5, 6), (5, 6, 0, 4)) * 0.3333333333333333
    x268 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x268 += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3))
    x268 += einsum(x267, (0, 1, 2, 3), (1, 0, 2, 3))
    x269 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x269 += einsum(t1, (0, 1), x268, (2, 3, 4, 1), (0, 2, 3, 4)) * 3.0
    x270 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x270 += einsum(t2, (0, 1, 2, 3), x269, (4, 0, 1, 5), (4, 5, 2, 3)) * 0.25
    x271 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x271 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.2
    x271 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x271 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 0.2
    x271 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.2
    x271 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.2
    x271 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -0.2
    x272 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x272 += einsum(x271, (0, 1, 2, 3, 4, 5), x57, (6, 1, 2, 7, 5, 4), (6, 7, 0, 3)) * 1.25
    x273 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x273 += einsum(t1, (0, 1), x65, (2, 3, 0, 4), (3, 2, 4, 1)) * 0.5
    x274 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x274 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3))
    x274 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x274 += einsum(x272, (0, 1, 2, 3), (0, 1, 2, 3))
    x274 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x274 += einsum(x63, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x274 += einsum(x64, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x274 += einsum(x273, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x275 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x275 += einsum(t1, (0, 1), x274, (0, 2, 3, 4), (2, 3, 1, 4))
    x276 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x276 += einsum(x8, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 1.5
    x277 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x277 += einsum(x13, (0, 1, 2, 3), l3, (4, 3, 2, 1, 5, 6), (5, 6, 0, 4))
    x278 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x278 += einsum(t1, (0, 1), x277, (2, 3, 4, 1), (0, 2, 3, 4)) * -1.0
    x279 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x279 += einsum(t2, (0, 1, 2, 3), x278, (4, 0, 1, 5), (4, 5, 2, 3)) * 0.25
    x280 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x280 += einsum(x244, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x280 += einsum(x248, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 += einsum(x252, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 += einsum(x258, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 += einsum(x260, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x280 += einsum(x266, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x280 += einsum(x270, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 += einsum(x275, (0, 1, 2, 3), (0, 1, 2, 3))
    x280 += einsum(x276, (0, 1, 2, 3), (1, 0, 2, 3))
    x280 += einsum(x279, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 += einsum(t1, (0, 1), x96, (2, 3), (0, 2, 1, 3))
    rdm2_f_oovv += einsum(x280, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x280, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x280, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x280, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x281 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x281 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 0), (2, 4, 1, 5))
    x282 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x282 += einsum(t2, (0, 1, 2, 3), x281, (1, 4, 3, 5), (0, 4, 2, 5))
    x283 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x283 += einsum(t2, (0, 1, 2, 3), x57, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    x284 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x284 += einsum(t2, (0, 1, 2, 3), x283, (1, 4, 2, 5), (4, 0, 3, 5))
    x285 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x285 += einsum(x13, (0, 1, 2, 3), x160, (1, 4, 5, 3, 6, 2), (0, 4, 5, 6)) * 0.5
    x286 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x286 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.5
    x286 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0))
    x287 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x287 += einsum(t1, (0, 1), x286, (2, 3, 4, 1), (0, 2, 3, 4))
    x288 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x288 += einsum(x285, (0, 1, 2, 3), (1, 2, 0, 3))
    x288 += einsum(x287, (0, 1, 2, 3), (2, 1, 0, 3))
    x289 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x289 += einsum(x288, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (4, 2, 5, 6))
    x290 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x290 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.0
    x290 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x291 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x291 += einsum(x290, (0, 1, 2, 3), l3, (3, 2, 4, 1, 5, 6), (5, 6, 0, 4))
    x292 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x292 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x292 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x292 += einsum(x291, (0, 1, 2, 3), (1, 0, 2, 3))
    x293 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x293 += einsum(x292, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (4, 2, 5, 6)) * 0.25
    x294 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x294 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x294 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x295 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x295 += einsum(x294, (0, 1, 2, 3), x57, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    x296 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x296 += einsum(x13, (0, 1, 2, 3), x295, (1, 4, 3, 5), (0, 4, 2, 5)) * -0.5
    x297 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x297 += einsum(t2, (0, 1, 2, 3), x57, (4, 0, 1, 5, 3, 6), (4, 5, 6, 2))
    x298 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x298 += einsum(t2, (0, 1, 2, 3), x57, (0, 4, 1, 5, 3, 6), (4, 5, 6, 2))
    x299 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x299 += einsum(l2, (0, 1, 2, 3), x6, (4, 2, 5, 1), (4, 3, 5, 0))
    x300 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x300 += einsum(x297, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x300 += einsum(x298, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x300 += einsum(x299, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x301 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x301 += einsum(t2, (0, 1, 2, 3), x300, (1, 4, 2, 5), (4, 0, 5, 3))
    x302 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x302 += einsum(x294, (0, 1, 2, 3), x57, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    x303 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x303 += einsum(t2, (0, 1, 2, 3), x302, (1, 4, 3, 5), (4, 0, 5, 2)) * -0.5
    x304 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x304 += einsum(x282, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x304 += einsum(x284, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x304 += einsum(x289, (0, 1, 2, 3), (1, 0, 2, 3))
    x304 += einsum(x293, (0, 1, 2, 3), (1, 0, 2, 3))
    x304 += einsum(x296, (0, 1, 2, 3), (1, 0, 2, 3))
    x304 += einsum(x301, (0, 1, 2, 3), (0, 1, 2, 3))
    x304 += einsum(x303, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x304, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x304, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x305 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x305 += einsum(l1, (0, 1), t3, (2, 3, 1, 4, 5, 0), (2, 3, 4, 5))
    x306 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x306 += einsum(t2, (0, 1, 2, 3), l3, (3, 4, 5, 1, 0, 6), (6, 4, 5, 2))
    x307 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x307 += einsum(x306, (0, 1, 2, 3), t3, (4, 0, 5, 6, 2, 1), (4, 5, 3, 6))
    x308 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x308 += einsum(x99, (0, 1, 2, 3), l3, (2, 4, 5, 1, 0, 6), (6, 4, 5, 3))
    x309 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x309 += einsum(x6, (0, 1, 2, 3), l3, (3, 4, 5, 0, 6, 1), (6, 4, 5, 2))
    x310 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x310 += einsum(x308, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x310 += einsum(x309, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x311 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x311 += einsum(x310, (0, 1, 2, 3), x60, (4, 5, 0, 6, 2, 1), (4, 5, 6, 3)) * 0.25
    x312 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x312 += einsum(x6, (0, 1, 2, 3), l3, (2, 3, 4, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x313 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x313 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x313 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x313 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    x314 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x314 += einsum(x312, (0, 1, 2, 3, 4, 5), x313, (1, 0, 2, 6, 7, 5), (3, 4, 6, 7)) * -0.08333333333333
    x315 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x315 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 5, 0, 1, 6), (6, 4, 5, 2))
    x316 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x316 += einsum(x315, (0, 1, 2, 3), x131, (4, 5, 0, 6, 2, 1), (4, 5, 6, 3)) * 0.5
    x317 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x317 += einsum(x309, (0, 1, 2, 3), t3, (4, 0, 5, 6, 1, 2), (4, 5, 6, 3)) * -0.5
    x318 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x318 += einsum(l3, (0, 1, 2, 3, 4, 5), x11, (6, 7, 5, 1, 0, 2), (3, 4, 6, 7)) * 0.33333333333332
    x319 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x319 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x319 += einsum(x318, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x319 += einsum(x212, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x320 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x320 += einsum(x294, (0, 1, 2, 3), x319, (1, 0, 4, 5), (4, 5, 2, 3)) * 0.25
    x321 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x321 += einsum(x215, (0, 1, 2, 3), l3, (4, 5, 2, 6, 0, 1), (6, 4, 5, 3))
    x322 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x322 += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x322 += einsum(x321, (0, 1, 2, 3), (0, 1, 2, 3))
    x322 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    x323 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x323 += einsum(t1, (0, 1), x322, (0, 2, 3, 4), (1, 2, 3, 4))
    x324 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x324 += einsum(x13, (0, 1, 2, 3), x323, (4, 3, 2, 5), (0, 1, 4, 5)) * 0.25
    x325 = np.zeros((nvir, nvir), dtype=np.float64)
    x325 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 0, 6, 2), (1, 6))
    x326 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * 0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * 0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -0.14285714285714288
    x326 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * 0.14285714285714288
    x327 = np.zeros((nvir, nvir), dtype=np.float64)
    x327 += einsum(l3, (0, 1, 2, 3, 4, 5), x326, (3, 4, 5, 6, 1, 2), (0, 6)) * 6.999999999999999
    x328 = np.zeros((nvir, nvir), dtype=np.float64)
    x328 += einsum(x325, (0, 1), (0, 1)) * 3.0
    x328 += einsum(x327, (0, 1), (0, 1)) * -1.0
    x329 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x329 += einsum(x328, (0, 1), x6, (2, 3, 0, 4), (2, 3, 4, 1)) * 0.08333333333333
    x330 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x330 += einsum(t1, (0, 1), x111, (0, 2, 3, 4), (2, 3, 1, 4))
    x331 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x331 += einsum(x13, (0, 1, 2, 3), x330, (1, 4, 5, 2), (0, 4, 3, 5)) * 0.5
    x332 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x332 += einsum(t2, (0, 1, 2, 3), x221, (0, 1, 4, 5), (4, 5, 2, 3)) * 0.08333333333333
    x333 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x333 += einsum(x44, (0, 1, 2, 3), x131, (4, 5, 1, 6, 3, 2), (0, 4, 5, 6)) * 0.5
    x334 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x334 += einsum(x18, (0, 1, 2, 3), x24, (1, 4, 5, 2), (0, 4, 5, 3)) * 1.5
    x335 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x335 += einsum(t1, (0, 1), x213, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.5
    x336 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x336 += einsum(l1, (0, 1), x13, (2, 3, 0, 4), (1, 2, 3, 4))
    x337 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x337 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3))
    x337 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3))
    x337 += einsum(x333, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x337 += einsum(x334, (0, 1, 2, 3), (1, 0, 2, 3))
    x337 += einsum(x335, (0, 1, 2, 3), (0, 1, 2, 3))
    x337 += einsum(x336, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x338 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x338 += einsum(t1, (0, 1), x337, (0, 2, 3, 4), (2, 3, 1, 4))
    x339 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x339 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x339 += einsum(x305, (0, 1, 2, 3), (0, 1, 2, 3))
    x339 += einsum(x307, (0, 1, 2, 3), (0, 1, 2, 3))
    x339 += einsum(x311, (0, 1, 2, 3), (0, 1, 3, 2))
    x339 += einsum(x314, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x339 += einsum(x316, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x339 += einsum(x317, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x339 += einsum(x320, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x339 += einsum(x324, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x339 += einsum(x329, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x339 += einsum(x331, (0, 1, 2, 3), (0, 1, 3, 2))
    x339 += einsum(x332, (0, 1, 2, 3), (0, 1, 2, 3))
    x339 += einsum(x338, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x339, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x339, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x340 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x340 += einsum(t2, (0, 1, 2, 3), x57, (0, 4, 1, 5, 2, 6), (4, 5, 6, 3))
    x341 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x341 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x341 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x342 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x342 += einsum(x341, (0, 1, 2, 3), x57, (4, 1, 0, 5, 2, 6), (4, 5, 6, 3))
    x343 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x343 += einsum(x340, (0, 1, 2, 3), (0, 1, 2, 3))
    x343 += einsum(x342, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x344 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x344 += einsum(x13, (0, 1, 2, 3), x343, (1, 4, 3, 5), (0, 4, 2, 5)) * 0.5
    x345 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x345 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 0, 5), (3, 4, 1, 5))
    rdm2_f_ovvo += einsum(x345, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x345, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x346 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x346 += einsum(t2, (0, 1, 2, 3), x57, (0, 4, 1, 5, 6, 3), (4, 5, 6, 2))
    x347 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x347 += einsum(x341, (0, 1, 2, 3), x57, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2)) * 0.5
    x348 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x348 += einsum(t2, (0, 1, 2, 3), x133, (4, 1, 3, 5), (4, 0, 5, 2))
    x349 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x349 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3))
    x349 += einsum(x346, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x349 += einsum(x347, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x349 += einsum(x348, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x350 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x350 += einsum(t2, (0, 1, 2, 3), x349, (1, 4, 2, 5), (4, 0, 5, 3))
    x351 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x351 += einsum(x297, (0, 1, 2, 3), (0, 1, 2, 3))
    x351 += einsum(x298, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x352 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x352 += einsum(t2, (0, 1, 2, 3), x351, (1, 4, 3, 5), (4, 0, 5, 2)) * 0.5
    x353 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x353 += einsum(t1, (0, 1), x19, (2, 3, 4, 1), (0, 2, 3, 4))
    x354 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x354 += einsum(t1, (0, 1), x353, (2, 3, 0, 4), (3, 2, 4, 1))
    x355 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x355 += einsum(t1, (0, 1), x354, (0, 2, 3, 4), (2, 3, 1, 4)) * 1.5
    x356 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x356 += einsum(x344, (0, 1, 2, 3), (1, 0, 2, 3))
    x356 += einsum(x350, (0, 1, 2, 3), (0, 1, 2, 3))
    x356 += einsum(x352, (0, 1, 2, 3), (0, 1, 3, 2))
    x356 += einsum(x355, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x356, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x356, (0, 1, 2, 3), (1, 0, 3, 2))
    x357 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x357 += einsum(t2, (0, 1, 2, 3), x345, (1, 4, 3, 5), (0, 4, 2, 5))
    rdm2_f_oovv += einsum(x357, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x358 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x358 += einsum(x13, (0, 1, 2, 3), x57, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    x359 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x359 += einsum(t2, (0, 1, 2, 3), x358, (1, 4, 3, 5), (4, 0, 5, 2)) * -1.0
    x360 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x360 += einsum(x357, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x360 += einsum(x359, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x360, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x360, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    rdm2_f_oovv += einsum(x360, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x360, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    x361 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x361 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x361 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x361 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    x362 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x362 += einsum(x104, (0, 1, 2, 3, 4, 5), x361, (0, 1, 2, 6, 7, 5), (3, 4, 6, 7)) * 0.16666666666667
    x363 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x363 += einsum(t1, (0, 1), x116, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.3333333333333333
    x364 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x364 += einsum(x363, (0, 1, 2, 3), x6, (4, 0, 5, 3), (4, 1, 5, 2)) * 1.5
    x365 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x365 += einsum(x215, (0, 1, 2, 3), x104, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3))
    x366 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x366 += einsum(x13, (0, 1, 2, 3), x104, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    x367 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x367 += einsum(x18, (0, 1, 2, 3), x90, (4, 1, 5, 2), (0, 4, 5, 3)) * 3.0
    x368 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x368 += einsum(x365, (0, 1, 2, 3), (0, 1, 2, 3))
    x368 += einsum(x366, (0, 1, 2, 3), (0, 1, 2, 3))
    x368 += einsum(x367, (0, 1, 2, 3), (1, 0, 2, 3))
    x369 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x369 += einsum(t1, (0, 1), x368, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x370 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x370 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x370 += einsum(x362, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x370 += einsum(x364, (0, 1, 2, 3), (1, 0, 2, 3))
    x370 += einsum(x369, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x370, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x370, (0, 1, 2, 3), (0, 1, 2, 3))
    x371 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x371 += einsum(t2, (0, 1, 2, 3), x57, (4, 1, 0, 5, 3, 6), (4, 5, 6, 2))
    x372 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x372 += einsum(t2, (0, 1, 2, 3), x371, (1, 4, 2, 5), (4, 0, 5, 3))
    rdm2_f_oovv += einsum(x372, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    rdm2_f_oovv += einsum(x372, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x372, (0, 1, 2, 3), (1, 0, 2, 3)) * 1.5
    rdm2_f_oovv += einsum(x372, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x373 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x373 += einsum(t2, (0, 1, 2, 3), x371, (1, 4, 3, 5), (4, 0, 2, 5))
    rdm2_f_oovv += einsum(x373, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x373, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    rdm2_f_oovv += einsum(x373, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x373, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.5
    x374 = np.zeros((nvir, nvir), dtype=np.float64)
    x374 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x375 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x375 += einsum(x374, (0, 1), t2, (2, 3, 0, 4), (2, 3, 1, 4))
    rdm2_f_oovv += einsum(x375, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    rdm2_f_oovv += einsum(x375, (0, 1, 2, 3), (0, 1, 3, 2))
    x376 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x376 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 5, 0), (3, 4, 1, 5))
    x377 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x377 += einsum(t2, (0, 1, 2, 3), x376, (1, 4, 3, 5), (4, 0, 5, 2))
    rdm2_f_oovv += einsum(x377, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x377, (0, 1, 2, 3), (0, 1, 3, 2)) * -3.0
    rdm2_f_oovv += einsum(x377, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x377, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x378 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x378 += einsum(x374, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1))
    rdm2_f_oovv += einsum(x378, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x378, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    x379 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x379 += einsum(x6, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 7), (5, 6, 7, 0, 1, 4)) * 0.49999999999997
    x380 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x380 += einsum(x104, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x380 += einsum(x379, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x381 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x381 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x381 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x381 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x382 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x382 += einsum(x380, (0, 1, 2, 3, 4, 5), x381, (0, 2, 1, 6, 5, 7), (3, 4, 6, 7)) * 0.16666666666667
    rdm2_f_oovv += einsum(x382, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x382, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x383 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x383 += einsum(x6, (0, 1, 2, 3), l3, (2, 4, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x384 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x384 += einsum(x51, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.00000000000012
    x384 += einsum(x383, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x385 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x385 += einsum(t3, (0, 1, 2, 3, 4, 5), x384, (0, 1, 2, 6, 7, 4), (6, 7, 3, 5)) * 0.24999999999999
    rdm2_f_oovv += einsum(x385, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x385, (0, 1, 2, 3), (0, 1, 2, 3))
    x386 = np.zeros((nvir, nvir), dtype=np.float64)
    x386 += einsum(l2, (0, 1, 2, 3), x215, (2, 3, 0, 4), (1, 4))
    rdm2_f_oovv += einsum(x386, (0, 1), x13, (2, 3, 0, 4), (2, 3, 4, 1)) * -0.5
    x387 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x387 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x387 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x387 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x388 = np.zeros((nvir, nvir), dtype=np.float64)
    x388 += einsum(l2, (0, 1, 2, 3), x387, (3, 2, 1, 4), (4, 0))
    rdm2_f_oovv += einsum(x388, (0, 1), x13, (2, 3, 1, 4), (2, 3, 0, 4)) * 0.5
    x389 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x389 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x389 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x390 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x390 += einsum(l1, (0, 1), x389, (2, 3, 1, 4, 0, 5), (2, 3, 4, 5))
    rdm2_f_oovv += einsum(x390, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x390, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x391 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x391 += einsum(l3, (0, 1, 2, 3, 4, 5), x118, (6, 7, 4, 1, 0, 2), (3, 5, 6, 7)) * 0.3333333333333333
    x392 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x392 += einsum(t1, (0, 1), x391, (0, 2, 3, 4), (2, 3, 4, 1)) * 3.0
    x393 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x393 += einsum(t1, (0, 1), x392, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.16666666666667
    rdm2_f_oovv += einsum(x393, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x393, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x394 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x394 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x395 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x395 += einsum(t3, (0, 1, 2, 3, 4, 5), x394, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4))
    rdm2_f_oovv += einsum(x395, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999997996
    rdm2_f_oovv += einsum(x395, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.49999999999997996
    x396 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x396 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x397 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x397 += einsum(t3, (0, 1, 2, 3, 4, 5), x396, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4))
    rdm2_f_oovv += einsum(x397, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.49999999999997996
    rdm2_f_oovv += einsum(x397, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.49999999999997996
    x398 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x398 += einsum(x315, (0, 1, 2, 3), t3, (4, 5, 0, 1, 6, 2), (4, 5, 3, 6))
    rdm2_f_oovv += einsum(x398, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    rdm2_f_oovv += einsum(x398, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    x399 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x399 += einsum(x153, (0, 1, 2, 3), t3, (0, 4, 1, 5, 6, 3), (2, 4, 5, 6))
    rdm2_f_oovv += einsum(x399, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    rdm2_f_oovv += einsum(x399, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x400 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x400 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 5, 1, 0, 6), (6, 4, 5, 3))
    x401 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x401 += einsum(x400, (0, 1, 2, 3), t3, (4, 5, 0, 1, 6, 2), (4, 5, 3, 6))
    rdm2_f_oovv += einsum(x401, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    rdm2_f_oovv += einsum(x401, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x402 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x402 += einsum(x90, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (2, 4, 5, 6))
    rdm2_f_oovv += einsum(x402, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x402, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x403 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x403 += einsum(t2, (0, 1, 2, 3), l3, (2, 4, 5, 0, 1, 6), (6, 4, 5, 3))
    x404 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x404 += einsum(x403, (0, 1, 2, 3), t3, (4, 5, 0, 6, 1, 2), (4, 5, 3, 6))
    rdm2_f_oovv += einsum(x404, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x404, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x405 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x405 += einsum(x306, (0, 1, 2, 3), t3, (4, 5, 0, 6, 1, 2), (4, 5, 3, 6))
    rdm2_f_oovv += einsum(x405, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x405, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x406 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x406 += einsum(t2, (0, 1, 2, 3), x55, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    rdm2_f_ovvo += einsum(x406, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x406, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x407 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x407 += einsum(t2, (0, 1, 2, 3), x406, (1, 4, 2, 5), (4, 0, 3, 5))
    rdm2_f_oovv += einsum(x407, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x407, (0, 1, 2, 3), (0, 1, 3, 2))
    x408 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x408 += einsum(x41, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (2, 4, 5, 6))
    rdm2_f_oovv += einsum(x408, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x408, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x409 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x409 += einsum(t2, (0, 1, 2, 3), l3, (3, 2, 4, 5, 1, 6), (5, 6, 0, 4))
    x410 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x410 += einsum(x409, (0, 1, 2, 3), t3, (0, 4, 1, 5, 6, 3), (2, 4, 5, 6))
    x411 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x411 += einsum(t3, (0, 1, 2, 3, 4, 5), x104, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4))
    x412 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x412 += einsum(t2, (0, 1, 2, 3), x346, (1, 4, 2, 5), (4, 0, 5, 3))
    x413 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x413 += einsum(x310, (0, 1, 2, 3), t3, (4, 5, 0, 2, 6, 1), (4, 5, 6, 3)) * 0.25
    x414 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x414 += einsum(x13, (0, 1, 2, 3), l3, (2, 3, 4, 1, 5, 6), (5, 6, 0, 4))
    x415 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x415 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x415 += einsum(x414, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x416 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x416 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x416 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x417 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x417 += einsum(x415, (0, 1, 2, 3), x416, (1, 4, 0, 5, 6, 3), (2, 4, 5, 6)) * 0.25
    x418 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x418 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (5, 6, 4, 2, 7, 1), (3, 6, 0, 7))
    x419 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x419 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    x419 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * -1.0
    x420 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x420 += einsum(t3, (0, 1, 2, 3, 4, 5), x419, (6, 0, 2, 7, 5, 3), (1, 6, 4, 7))
    x421 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x421 += einsum(x418, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x421 += einsum(x264, (0, 1, 2, 3), (0, 1, 2, 3))
    x421 += einsum(x420, (0, 1, 2, 3), (1, 0, 3, 2))
    x422 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x422 += einsum(x421, (0, 1, 2, 3), x6, (4, 0, 2, 5), (4, 1, 5, 3)) * 0.25
    x423 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x423 += einsum(t1, (0, 1), x33, (2, 0, 3, 4), (2, 3, 4, 1))
    x424 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x424 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.25
    x424 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x424 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -0.25
    x425 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x425 += einsum(x424, (0, 1, 2, 3, 4, 5), x57, (6, 2, 0, 7, 5, 3), (6, 7, 1, 4)) * 2.0
    x426 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x426 += einsum(x131, (0, 1, 2, 3, 4, 5), x55, (1, 6, 2, 7, 5, 4), (6, 7, 0, 3)) * 0.5
    x427 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x427 += einsum(x133, (0, 1, 2, 3), t3, (4, 5, 1, 2, 6, 3), (4, 5, 0, 6))
    x428 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x428 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x428 += einsum(x423, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.00000000000002
    x428 += einsum(x425, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x426, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x428 += einsum(x427, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x429 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x429 += einsum(t1, (0, 1), x428, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x430 = np.zeros((nocc, nvir), dtype=np.float64)
    x430 += einsum(l1, (0, 1), t2, (2, 1, 0, 3), (2, 3))
    x431 = np.zeros((nocc, nvir), dtype=np.float64)
    x431 += einsum(t2, (0, 1, 2, 3), x9, (0, 1, 4, 3), (4, 2))
    x432 = np.zeros((nocc, nvir), dtype=np.float64)
    x432 += einsum(t2, (0, 1, 2, 3), x90, (0, 1, 4, 2), (4, 3))
    x433 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x433 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x433 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x433 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x433 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    x433 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -1.0
    x433 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x434 = np.zeros((nocc, nvir), dtype=np.float64)
    x434 += einsum(l2, (0, 1, 2, 3), x433, (4, 2, 3, 5, 1, 0), (4, 5)) * 0.25
    x435 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x435 += einsum(x409, (0, 1, 2, 3), (0, 1, 2, 3))
    x435 += einsum(x81, (0, 1, 2, 3), (1, 0, 2, 3))
    x436 = np.zeros((nocc, nvir), dtype=np.float64)
    x436 += einsum(x13, (0, 1, 2, 3), x435, (0, 1, 4, 2), (4, 3)) * 0.25
    x437 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x437 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x437 += einsum(x84, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x438 = np.zeros((nocc, nvir), dtype=np.float64)
    x438 += einsum(x437, (0, 1, 2, 3), x6, (1, 0, 4, 3), (2, 4)) * 0.5
    x439 = np.zeros((nocc, nvir), dtype=np.float64)
    x439 += einsum(t1, (0, 1), x31, (0, 2), (2, 1)) * 0.5
    x440 = np.zeros((nocc, nvir), dtype=np.float64)
    x440 += einsum(x430, (0, 1), (0, 1))
    x440 += einsum(x431, (0, 1), (0, 1)) * -0.5
    x440 += einsum(x75, (0, 1), (0, 1)) * 0.24999999999999
    x440 += einsum(x432, (0, 1), (0, 1)) * -0.25
    x440 += einsum(x77, (0, 1), (0, 1)) * -1.0
    x440 += einsum(x434, (0, 1), (0, 1))
    x440 += einsum(x436, (0, 1), (0, 1))
    x440 += einsum(x438, (0, 1), (0, 1)) * -1.0
    x440 += einsum(x439, (0, 1), (0, 1))
    x441 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x441 += einsum(x305, (0, 1, 2, 3), (0, 1, 2, 3))
    x441 += einsum(x377, (0, 1, 2, 3), (0, 1, 2, 3))
    x441 += einsum(x410, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x441 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x441 += einsum(x411, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000001
    x441 += einsum(x412, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x441 += einsum(x413, (0, 1, 2, 3), (0, 1, 3, 2))
    x441 += einsum(x417, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x441 += einsum(x422, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x441 += einsum(x429, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x441 += einsum(t1, (0, 1), x440, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_oovv += einsum(x441, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x441, (0, 1, 2, 3), (1, 0, 3, 2))
    x442 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x442 += einsum(x309, (0, 1, 2, 3), t3, (4, 5, 0, 6, 2, 1), (4, 5, 6, 3)) * -0.5
    x443 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x443 += einsum(x237, (0, 1, 2, 3), t3, (4, 1, 0, 5, 6, 3), (4, 2, 5, 6)) * -0.5
    x444 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x444 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x444 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x444 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x445 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x445 += einsum(x34, (0, 1, 2, 3), x444, (1, 4, 5, 3), (0, 2, 4, 5)) * -1.0
    x446 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x446 += einsum(x122, (0, 1, 2, 3), (0, 1, 2, 3))
    x446 += einsum(x121, (0, 1, 2, 3), (0, 1, 2, 3))
    x446 += einsum(x366, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x446 += einsum(x445, (0, 1, 2, 3), (0, 2, 1, 3))
    x447 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x447 += einsum(t1, (0, 1), x446, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x448 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x448 += einsum(x284, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x448 += einsum(x442, (0, 1, 2, 3), (0, 1, 3, 2))
    x448 += einsum(x443, (0, 1, 2, 3), (1, 0, 2, 3))
    x448 += einsum(x447, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x448, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x448, (0, 1, 2, 3), (1, 0, 2, 3))
    x449 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x449 += einsum(t2, (0, 1, 2, 3), x245, (1, 4, 3, 5), (0, 4, 2, 5))
    rdm2_f_oovv += einsum(x449, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.25
    rdm2_f_oovv += einsum(x449, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x449, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x449, (0, 1, 2, 3), (1, 0, 3, 2)) * 1.25
    x450 = np.zeros((nocc, nvir), dtype=np.float64)
    x450 += einsum(t2, (0, 1, 2, 3), x9, (0, 1, 4, 2), (4, 3))
    x451 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x451 += einsum(t2, (0, 1, 2, 3), l3, (2, 3, 4, 5, 1, 6), (5, 6, 0, 4))
    x452 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x452 += einsum(x451, (0, 1, 2, 3), t3, (0, 4, 1, 5, 6, 3), (2, 4, 5, 6))
    x453 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x453 += einsum(t1, (0, 1), x450, (2, 3), (0, 2, 1, 3)) * 1.5
    x453 += einsum(x452, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.75
    rdm2_f_oovv += einsum(x453, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x453, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333333
    x454 = np.zeros((nocc, nvir), dtype=np.float64)
    x454 += einsum(t1, (0, 1), x32, (0, 2), (2, 1))
    x455 = np.zeros((nocc, nvir), dtype=np.float64)
    x455 += einsum(x13, (0, 1, 2, 3), x451, (0, 1, 4, 2), (4, 3)) * 0.5
    x456 = np.zeros((nocc, nvir), dtype=np.float64)
    x456 += einsum(x454, (0, 1), (0, 1))
    x456 += einsum(x455, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), x456, (2, 3), (0, 2, 1, 3)) * -0.5
    rdm2_f_oovv += einsum(t1, (0, 1), x456, (2, 3), (2, 0, 3, 1)) * -1.5
    rdm2_f_oovv += einsum(t1, (0, 1), x456, (2, 3), (0, 2, 1, 3)) * -1.5
    rdm2_f_oovv += einsum(t1, (0, 1), x456, (2, 3), (2, 0, 3, 1)) * -0.5
    x457 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x457 += einsum(t2, (0, 1, 2, 3), x358, (1, 4, 3, 5), (4, 0, 5, 2)) * -0.5
    rdm2_f_oovv += einsum(x457, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x457, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x458 = np.zeros((nocc, nvir), dtype=np.float64)
    x458 += einsum(l2, (0, 1, 2, 3), t3, (4, 3, 2, 5, 1, 0), (4, 5))
    x459 = np.zeros((nocc, nvir), dtype=np.float64)
    x459 += einsum(t2, (0, 1, 2, 3), x90, (0, 1, 4, 3), (4, 2))
    x460 = np.zeros((nocc, nvir), dtype=np.float64)
    x460 += einsum(x458, (0, 1), (0, 1))
    x460 += einsum(x459, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), x460, (2, 3), (0, 2, 1, 3)) * 0.25
    rdm2_f_oovv += einsum(t1, (0, 1), x460, (2, 3), (2, 0, 3, 1)) * 1.25
    rdm2_f_oovv += einsum(t1, (0, 1), x460, (2, 3), (0, 2, 1, 3)) * 1.25
    rdm2_f_oovv += einsum(t1, (0, 1), x460, (2, 3), (2, 0, 3, 1)) * 0.25
    x461 = np.zeros((nocc, nvir), dtype=np.float64)
    x461 += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3))
    rdm2_f_oovv += einsum(t1, (0, 1), x461, (2, 3), (0, 2, 1, 3))
    rdm2_f_oovv += einsum(t1, (0, 1), x461, (2, 3), (2, 0, 3, 1)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x461, (2, 3), (0, 2, 1, 3)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x461, (2, 3), (2, 0, 3, 1))
    x462 = np.zeros((nocc, nvir), dtype=np.float64)
    x462 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 0, 1), (4, 5))
    rdm2_f_oovv += einsum(t1, (0, 1), x462, (2, 3), (0, 2, 1, 3)) * 1.25
    rdm2_f_oovv += einsum(t1, (0, 1), x462, (2, 3), (2, 0, 3, 1)) * 0.25
    rdm2_f_oovv += einsum(t1, (0, 1), x462, (2, 3), (0, 2, 1, 3)) * 0.25
    rdm2_f_oovv += einsum(t1, (0, 1), x462, (2, 3), (2, 0, 3, 1)) * 1.25
    x463 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x463 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 5), (3, 4, 1, 5))
    rdm2_f_ovov += einsum(x463, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x463, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x463, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x463, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x464 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x464 += einsum(t2, (0, 1, 2, 3), x57, (4, 0, 1, 5, 2, 6), (4, 5, 6, 3))
    x465 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x465 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x465 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x465 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x466 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x466 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x466 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x466 += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    x466 += einsum(x465, (0, 1, 2, 3), l3, (4, 3, 2, 5, 1, 6), (6, 5, 0, 4)) * -2.0
    x467 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x467 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 1, 5), (2, 4, 0, 5)) * 4.0
    x467 += einsum(x463, (0, 1, 2, 3), (0, 1, 2, 3)) * -8.0
    x467 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x467 += einsum(x406, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x467 += einsum(x464, (0, 1, 2, 3), (0, 1, 2, 3)) * -4.0
    x467 += einsum(x255, (0, 1, 2, 3), (0, 1, 2, 3))
    x467 += einsum(x256, (0, 1, 2, 3), (0, 1, 2, 3))
    x467 += einsum(x99, (0, 1, 2, 3), x57, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2)) * -2.0
    x467 += einsum(l2, (0, 1, 2, 3), x387, (4, 3, 0, 5), (2, 4, 1, 5)) * 4.0
    x467 += einsum(t1, (0, 1), x466, (2, 0, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x467, (1, 4, 3, 5), (0, 4, 2, 5)) * -0.25
    x468 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x468 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x468 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 3.0
    x468 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x468 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x469 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x469 += einsum(x136, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x469 += einsum(x138, (0, 1, 2, 3), (0, 1, 2, 3))
    x470 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x470 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x470 += einsum(l3, (0, 1, 2, 3, 4, 5), x271, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 2.5
    x470 += einsum(l3, (0, 1, 2, 3, 4, 5), x60, (6, 3, 5, 7, 2, 1), (4, 6, 0, 7)) * -0.5
    x470 += einsum(x468, (0, 1, 2, 3), x57, (4, 1, 0, 5, 2, 6), (4, 5, 6, 3))
    x470 += einsum(x13, (0, 1, 2, 3), x57, (0, 4, 1, 5, 2, 6), (4, 5, 6, 3)) * -1.0
    x470 += einsum(t2, (0, 1, 2, 3), x133, (1, 4, 5, 2), (4, 0, 5, 3)) * -2.0
    x470 += einsum(t1, (0, 1), x469, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x470, (0, 4, 2, 5), (4, 1, 5, 3)) * 0.5
    x471 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x471 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3))
    x471 += einsum(x149, (0, 1, 2, 3), (0, 1, 2, 3))
    x472 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x472 += einsum(x471, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 2, 5, 6))
    rdm2_f_oovv += einsum(x472, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x472, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x473 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x473 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 5, 1), (3, 4, 0, 5))
    rdm2_f_ovov += einsum(x473, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x473, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x474 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x474 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 7, 1, 2), (4, 6, 0, 7))
    rdm2_f_ovov += einsum(x474, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_ovov += einsum(x474, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_vovo += einsum(x474, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_vovo += einsum(x474, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.5
    x475 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x475 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 0, 7, 2), (3, 6, 1, 7))
    rdm2_f_ovov += einsum(x475, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_ovov += einsum(x475, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_vovo += einsum(x475, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_vovo += einsum(x475, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.5
    x476 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x476 += einsum(t2, (0, 1, 2, 3), x57, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    rdm2_f_ovov += einsum(x476, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x476, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x477 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x477 += einsum(x13, (0, 1, 2, 3), x55, (0, 4, 1, 5, 6, 2), (4, 5, 3, 6))
    x478 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x478 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x478 += einsum(x34, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x479 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x479 += einsum(x473, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x479 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3))
    x479 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3))
    x479 += einsum(x476, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x479 += einsum(x477, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x479 += einsum(t1, (0, 1), x478, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x479, (1, 4, 2, 5), (0, 4, 5, 3)) * 0.5
    x480 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x480 += einsum(t2, (0, 1, 2, 3), x57, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    rdm2_f_ovov += einsum(x480, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x480, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x481 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x481 += einsum(x13, (0, 1, 2, 3), l3, (2, 4, 3, 1, 5, 6), (5, 6, 0, 4)) * 0.5
    x482 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x482 += einsum(x229, (0, 1, 2, 3), (0, 1, 2, 3))
    x482 += einsum(x481, (0, 1, 2, 3), (0, 1, 2, 3))
    x483 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x483 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3))
    x483 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3))
    x483 += einsum(x480, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x483 += einsum(x477, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x483 += einsum(t1, (0, 1), x482, (0, 2, 3, 4), (2, 3, 4, 1)) * -2.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x483, (0, 4, 3, 5), (4, 1, 2, 5)) * 0.5
    x484 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x484 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3))
    x484 += einsum(x247, (0, 1, 2, 3), (0, 1, 2, 3))
    x484 += einsum(t1, (0, 1), x90, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_oovv += einsum(x484, (0, 1, 2, 3), x6, (4, 0, 5, 2), (1, 4, 3, 5))
    x485 = np.zeros((nvir, nvir), dtype=np.float64)
    x485 += einsum(x325, (0, 1), (0, 1)) * 3.0
    x485 += einsum(x327, (0, 1), (0, 1)) * -1.0
    x485 += einsum(l2, (0, 1, 2, 3), x158, (3, 2, 4, 0), (1, 4)) * 18.00000000000072
    rdm2_f_oovv += einsum(x485, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1)) * -0.08333333333333
    x486 = np.zeros((nvir, nvir), dtype=np.float64)
    x486 += einsum(l2, (0, 1, 2, 3), x387, (3, 2, 1, 4), (4, 0)) * 6.00000000000024
    x487 = np.zeros((nvir, nvir), dtype=np.float64)
    x487 += einsum(x374, (0, 1), (0, 1)) * 18.00000000000072
    x487 += einsum(x325, (0, 1), (0, 1)) * 3.0
    x487 += einsum(x327, (0, 1), (0, 1)) * -1.0
    x487 += einsum(x486, (0, 1), (1, 0)) * -1.0
    rdm2_f_oovv += einsum(x487, (0, 1), t2, (2, 3, 0, 4), (2, 3, 1, 4)) * -0.08333333333333
    x488 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x488 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 2, 0, 5, 6), (5, 6, 1, 4))
    x489 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x489 += einsum(t1, (0, 1), x488, (2, 3, 4, 1), (2, 3, 0, 4))
    x490 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x490 += einsum(t1, (0, 1), x88, (2, 3, 4, 1), (0, 2, 3, 4)) * 0.5
    x491 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x491 += einsum(x26, (0, 1, 2, 3), (0, 1, 2, 3))
    x491 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999997996
    x491 += einsum(x489, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x491 += einsum(x490, (0, 1, 2, 3), (1, 2, 3, 0))
    x492 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x492 += einsum(t2, (0, 1, 2, 3), x491, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_oovv += einsum(x492, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x492, (0, 1, 2, 3), (1, 0, 3, 2))
    x493 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x493 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 1, 5, 6), (5, 6, 0, 4))
    x494 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x494 += einsum(t1, (0, 1), x493, (2, 3, 4, 1), (2, 3, 0, 4))
    x495 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x495 += einsum(t1, (0, 1), x237, (2, 3, 4, 1), (0, 2, 3, 4)) * -0.5
    x496 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x496 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.49999999999997996
    x496 += einsum(x494, (0, 1, 2, 3), (1, 0, 2, 3))
    x496 += einsum(x495, (0, 1, 2, 3), (2, 1, 3, 0))
    x497 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x497 += einsum(t2, (0, 1, 2, 3), x496, (1, 0, 4, 5), (4, 5, 2, 3))
    rdm2_f_oovv += einsum(x497, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x497, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x498 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x498 += einsum(x189, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 0.08333333333333
    rdm2_f_oovv += einsum(x498, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x498, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x499 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x499 += einsum(x174, (0, 1), t2, (0, 2, 3, 4), (1, 2, 3, 4)) * 0.08333333333333
    rdm2_f_oovv += einsum(x499, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x499, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x500 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x500 += einsum(t2, (0, 1, 2, 3), x9, (4, 1, 5, 2), (4, 5, 0, 3))
    x501 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x501 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x501 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x502 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x502 += einsum(x26, (0, 1, 2, 3), (0, 1, 2, 3))
    x502 += einsum(x25, (0, 1, 2, 3), (1, 0, 3, 2))
    x502 += einsum(x38, (0, 1, 2, 3), (1, 2, 0, 3))
    x503 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x503 += einsum(x128, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x503 += einsum(x127, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.0
    x503 += einsum(x500, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x503 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x503 += einsum(x126, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x503 += einsum(t2, (0, 1, 2, 3), x142, (4, 3, 2, 5), (4, 0, 1, 5)) * -1.0
    x503 += einsum(t2, (0, 1, 2, 3), x501, (4, 0, 5, 2), (4, 5, 1, 3)) * 2.0
    x503 += einsum(x13, (0, 1, 2, 3), x41, (4, 1, 5, 3), (4, 5, 0, 2)) * -2.0
    x503 += einsum(t1, (0, 1), x502, (2, 0, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x503, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x504 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x504 += einsum(t2, (0, 1, 2, 3), x41, (0, 4, 5, 3), (4, 5, 1, 2))
    x505 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x505 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x505 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x506 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x506 += einsum(x179, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x506 += einsum(x178, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x506 += einsum(x504, (0, 1, 2, 3), (0, 1, 2, 3))
    x506 += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3))
    x506 += einsum(x177, (0, 1, 2, 3), (0, 2, 1, 3))
    x506 += einsum(x182, (0, 1, 2, 3), (0, 1, 2, 3))
    x506 += einsum(t2, (0, 1, 2, 3), x505, (1, 4, 5, 3), (4, 0, 5, 2)) * -1.0
    x506 += einsum(t2, (0, 1, 2, 3), x37, (1, 4, 5, 2), (4, 0, 5, 3))
    rdm2_f_oovv += einsum(t1, (0, 1), x506, (0, 2, 3, 4), (2, 3, 4, 1))
    x507 = np.zeros((nocc, nvir), dtype=np.float64)
    x507 += einsum(l1, (0, 1), t2, (1, 2, 0, 3), (2, 3))
    x508 = np.zeros((nocc, nvir), dtype=np.float64)
    x508 += einsum(t2, (0, 1, 2, 3), x153, (0, 1, 4, 3), (4, 2))
    x509 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x509 += einsum(x149, (0, 1, 2, 3), (1, 0, 2, 3))
    x509 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x510 = np.zeros((nocc, nocc), dtype=np.float64)
    x510 += einsum(x21, (0, 1), (0, 1))
    x510 += einsum(x39, (0, 1), (0, 1))
    x511 = np.zeros((nocc, nvir), dtype=np.float64)
    x511 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x511 += einsum(x507, (0, 1), (0, 1)) * -1.0
    x511 += einsum(x508, (0, 1), (0, 1)) * 0.5
    x511 += einsum(t2, (0, 1, 2, 3), x237, (0, 1, 4, 2), (4, 3)) * 0.5
    x511 += einsum(t2, (0, 1, 2, 3), x509, (0, 1, 4, 2), (4, 3))
    x511 += einsum(t1, (0, 1), x510, (0, 2), (2, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x511, (2, 3), (0, 2, 1, 3)) * -1.0
    x512 = np.zeros((nocc, nvir), dtype=np.float64)
    x512 += einsum(t1, (0, 1), x21, (0, 2), (2, 1))
    x513 = np.zeros((nocc, nvir), dtype=np.float64)
    x513 += einsum(t2, (0, 1, 2, 3), x88, (0, 1, 4, 3), (4, 2))
    x514 = np.zeros((nocc, nvir), dtype=np.float64)
    x514 += einsum(x512, (0, 1), (0, 1)) * 2.0
    x514 += einsum(x513, (0, 1), (0, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x514, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(t1, (0, 1), x514, (2, 3), (0, 2, 1, 3)) * -0.5
    x515 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x515 += einsum(x305, (0, 1, 2, 3), (0, 1, 2, 3))
    x515 += einsum(x410, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x515 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x515 += einsum(x411, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000001
    x515 += einsum(x412, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x515 += einsum(x413, (0, 1, 2, 3), (0, 1, 3, 2))
    x515 += einsum(x417, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x515 += einsum(x422, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x515 += einsum(x429, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x515 += einsum(t1, (0, 1), x440, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_oovv += einsum(x515, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x515, (0, 1, 2, 3), (1, 0, 3, 2))
    x516 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x516 += einsum(x284, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x516 += einsum(x442, (0, 1, 2, 3), (0, 1, 3, 2))
    x516 += einsum(x443, (0, 1, 2, 3), (1, 0, 2, 3))
    x516 += einsum(x457, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x516 += einsum(x447, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x516, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x516, (0, 1, 2, 3), (1, 0, 2, 3))
    x517 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x517 += einsum(t1, (0, 1), x450, (2, 3), (0, 2, 1, 3)) * 0.5
    x517 += einsum(x452, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    rdm2_f_oovv += einsum(x517, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x517, (0, 1, 2, 3), (1, 0, 3, 2)) * -3.0
    x518 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x518 += einsum(l3, (0, 1, 2, 3, 4, 5), x60, (6, 3, 5, 7, 2, 1), (4, 6, 0, 7)) * 0.25
    x519 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x519 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x519 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x519 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x519 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x520 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x520 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.5
    x520 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x521 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x521 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x521 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0))
    x521 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x522 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x522 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x522 += einsum(x149, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x522 += einsum(x208, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x523 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x523 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.25
    x523 += einsum(x406, (0, 1, 2, 3), (0, 1, 2, 3))
    x523 += einsum(l3, (0, 1, 2, 3, 4, 5), x254, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 0.25
    x523 += einsum(x518, (0, 1, 2, 3), (0, 1, 2, 3))
    x523 += einsum(x519, (0, 1, 2, 3), x57, (4, 0, 1, 5, 2, 6), (4, 5, 6, 3)) * -0.5
    x523 += einsum(x6, (0, 1, 2, 3), x57, (0, 4, 1, 5, 2, 6), (4, 5, 6, 3)) * -0.5
    x523 += einsum(x520, (0, 1, 2, 3), x6, (4, 0, 3, 5), (1, 4, 2, 5)) * -2.0
    x523 += einsum(t2, (0, 1, 2, 3), x521, (0, 4, 5, 2), (4, 1, 5, 3)) * -1.0
    x523 += einsum(t1, (0, 1), x522, (0, 2, 3, 4), (2, 3, 4, 1)) * 0.5
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x523, (1, 4, 3, 5), (4, 0, 5, 2)) * -1.0
    x524 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x524 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x524 += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    x524 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    x525 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x525 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3))
    x525 += einsum(x371, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x525 += einsum(l3, (0, 1, 2, 3, 4, 5), x271, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 5.0
    x525 += einsum(x256, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x525 += einsum(x215, (0, 1, 2, 3), x57, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3)) * 2.0
    x525 += einsum(x13, (0, 1, 2, 3), x57, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3)) * 2.0
    x525 += einsum(t2, (0, 1, 2, 3), x133, (4, 1, 2, 5), (4, 0, 5, 3)) * -4.0
    x525 += einsum(t1, (0, 1), x524, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x525, (0, 4, 2, 5), (1, 4, 3, 5)) * 0.25
    x526 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x526 += einsum(x236, (0, 1, 2, 3), (0, 1, 2, 3))
    x526 += einsum(x13, (0, 1, 2, 3), l3, (3, 4, 2, 1, 5, 6), (5, 6, 0, 4)) * -0.5
    x527 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x527 += einsum(x473, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x527 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3))
    x527 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3))
    x527 += einsum(x476, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x527 += einsum(x477, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x527 += einsum(t1, (0, 1), x526, (0, 2, 3, 4), (2, 3, 4, 1)) * -2.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x527, (1, 4, 2, 5), (4, 0, 3, 5)) * 0.5
    x528 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x528 += einsum(x13, (0, 1, 2, 3), x55, (0, 4, 1, 5, 6, 2), (4, 5, 3, 6)) * 0.5
    x529 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x529 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x529 += einsum(x184, (0, 1, 2, 3), (1, 0, 2, 3))
    x530 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x530 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x530 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x530 += einsum(x480, (0, 1, 2, 3), (0, 1, 2, 3))
    x530 += einsum(x528, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x530 += einsum(t1, (0, 1), x529, (0, 2, 3, 4), (2, 3, 4, 1)) * 0.5
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x530, (0, 4, 3, 5), (1, 4, 5, 2))
    x531 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x531 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3))
    x531 += einsum(x247, (0, 1, 2, 3), (0, 1, 2, 3))
    x531 += einsum(t1, (0, 1), x24, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_oovv += einsum(x531, (0, 1, 2, 3), x6, (4, 0, 2, 5), (4, 1, 5, 3)) * -1.0
    x532 = np.zeros((nvir, nvir), dtype=np.float64)
    x532 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 0, 4), (1, 4))
    x533 = np.zeros((nvir, nvir), dtype=np.float64)
    x533 += einsum(x374, (0, 1), (0, 1)) * 6.00000000000024
    x533 += einsum(x532, (0, 1), (0, 1)) * 12.00000000000048
    x533 += einsum(x325, (0, 1), (0, 1)) * 3.0
    x533 += einsum(x327, (0, 1), (0, 1)) * -1.0
    x533 += einsum(x486, (0, 1), (1, 0)) * -1.0
    rdm2_f_oovv += einsum(x533, (0, 1), t2, (2, 3, 4, 0), (3, 2, 1, 4)) * -0.08333333333333
    x534 = np.zeros((nvir, nvir), dtype=np.float64)
    x534 += einsum(x374, (0, 1), (0, 1)) * 12.00000000000048
    x534 += einsum(x325, (0, 1), (0, 1)) * 3.0
    x534 += einsum(x327, (0, 1), (0, 1)) * -1.0
    x534 += einsum(l2, (0, 1, 2, 3), x215, (2, 3, 0, 4), (1, 4)) * -6.00000000000024
    rdm2_f_oovv += einsum(x534, (0, 1), t2, (2, 3, 0, 4), (3, 2, 4, 1)) * -0.08333333333333
    x535 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x535 += einsum(x179, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x535 += einsum(x178, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x535 += einsum(x504, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x535 += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x535 += einsum(x177, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x535 += einsum(t2, (0, 1, 2, 3), x142, (4, 2, 3, 5), (4, 0, 1, 5)) * -1.0
    x535 += einsum(t2, (0, 1, 2, 3), x505, (1, 4, 5, 3), (4, 0, 5, 2)) * -2.0
    x535 += einsum(t2, (0, 1, 2, 3), x471, (4, 1, 5, 2), (4, 0, 5, 3)) * 2.0
    x535 += einsum(t1, (0, 1), x502, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x535, (0, 2, 3, 4), (3, 2, 1, 4)) * 0.5
    x536 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x536 += einsum(x128, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x536 += einsum(x127, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x536 += einsum(x500, (0, 1, 2, 3), (0, 2, 1, 3))
    x536 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    x536 += einsum(x126, (0, 1, 2, 3), (0, 1, 2, 3))
    x536 += einsum(x143, (0, 1, 2, 3), (0, 1, 2, 3))
    x536 += einsum(t2, (0, 1, 2, 3), x501, (4, 0, 5, 2), (4, 5, 1, 3))
    x536 += einsum(x13, (0, 1, 2, 3), x41, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), x536, (0, 2, 3, 4), (3, 2, 4, 1))
    x537 = np.zeros((nocc, nvir), dtype=np.float64)
    x537 += einsum(t1, (0, 1), (0, 1)) * -2.0
    x537 += einsum(x507, (0, 1), (0, 1)) * -2.0
    x537 += einsum(x508, (0, 1), (0, 1))
    x537 += einsum(t2, (0, 1, 2, 3), x237, (0, 1, 4, 2), (4, 3))
    x537 += einsum(t2, (0, 1, 2, 3), x509, (0, 1, 4, 2), (4, 3)) * 2.0
    x537 += einsum(t1, (0, 1), x510, (0, 2), (2, 1)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x537, (2, 3), (2, 0, 3, 1)) * -0.5
    x538 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x538 += einsum(x13, (0, 1, 2, 3), x154, (4, 1, 5, 3, 2, 6), (0, 4, 5, 6)) * 0.5
    x539 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x539 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x539 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3))
    x539 += einsum(x538, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x540 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x540 += einsum(x539, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 2, 5, 6)) * 0.5
    x541 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x541 += einsum(l3, (0, 1, 2, 3, 4, 5), x271, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 1.25
    x542 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x542 += einsum(x463, (0, 1, 2, 3), (0, 1, 2, 3))
    x542 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x542 += einsum(x541, (0, 1, 2, 3), (0, 1, 2, 3))
    x542 += einsum(x518, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x543 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x543 += einsum(x542, (0, 1, 2, 3), x6, (4, 0, 2, 5), (4, 1, 5, 3))
    x544 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x544 += einsum(x250, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 2, 5, 6)) * 0.5
    x545 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x545 += einsum(l3, (0, 1, 2, 3, 4, 5), x424, (5, 6, 4, 2, 7, 1), (3, 6, 0, 7))
    x546 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x546 += einsum(l3, (0, 1, 2, 3, 4, 5), x131, (6, 3, 5, 7, 2, 0), (4, 6, 1, 7)) * 0.25
    rdm2_f_ovvo += einsum(x546, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_ovvo += einsum(x546, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x546, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_voov += einsum(x546, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x547 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x547 += einsum(x261, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x547 += einsum(x545, (0, 1, 2, 3), (0, 1, 2, 3))
    x547 += einsum(x546, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x548 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x548 += einsum(t2, (0, 1, 2, 3), x547, (0, 4, 2, 5), (4, 1, 5, 3))
    x549 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x549 += einsum(x406, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x549 += einsum(x283, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x550 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x550 += einsum(t2, (0, 1, 2, 3), x549, (0, 4, 2, 5), (4, 1, 5, 3)) * 0.5
    x551 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x551 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x551 += einsum(l3, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 2, 1))
    x552 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x552 += einsum(x13, (0, 1, 2, 3), x551, (4, 1, 5, 6, 3, 2), (0, 4, 5, 6))
    x553 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x553 += einsum(x226, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x553 += einsum(x552, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x554 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x554 += einsum(t1, (0, 1), x553, (2, 3, 4, 1), (0, 2, 3, 4))
    x555 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x555 += einsum(t2, (0, 1, 2, 3), x554, (4, 0, 1, 5), (4, 5, 2, 3)) * 0.25
    x556 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x556 += einsum(t1, (0, 1), x34, (0, 2, 3, 4), (2, 3, 1, 4)) * -1.0
    x557 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x557 += einsum(x346, (0, 1, 2, 3), (0, 1, 2, 3))
    x557 += einsum(x556, (0, 1, 2, 3), (0, 1, 3, 2))
    x558 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x558 += einsum(t2, (0, 1, 2, 3), x557, (0, 4, 2, 5), (4, 1, 5, 3)) * 0.5
    x559 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x559 += einsum(t2, (0, 1, 2, 3), x9, (0, 4, 5, 2), (4, 5, 1, 3))
    x560 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x560 += einsum(x13, (0, 1, 2, 3), x62, (4, 1, 5, 3), (0, 4, 5, 2))
    x561 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x561 += einsum(x559, (0, 1, 2, 3), (0, 1, 2, 3))
    x561 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x561 += einsum(x272, (0, 1, 2, 3), (0, 1, 2, 3))
    x561 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x561 += einsum(x560, (0, 1, 2, 3), (1, 2, 0, 3))
    x561 += einsum(x273, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x562 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x562 += einsum(t1, (0, 1), x561, (0, 2, 3, 4), (2, 3, 1, 4))
    x563 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x563 += einsum(x46, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4)) * 0.5
    x564 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x564 += einsum(x244, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x564 += einsum(x540, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x564 += einsum(x543, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x564 += einsum(x544, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x564 += einsum(x548, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x564 += einsum(x550, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x564 += einsum(x555, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x564 += einsum(x558, (0, 1, 2, 3), (0, 1, 2, 3))
    x564 += einsum(x562, (0, 1, 2, 3), (0, 1, 2, 3))
    x564 += einsum(x563, (0, 1, 2, 3), (1, 0, 2, 3))
    x564 += einsum(x279, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x564 += einsum(t1, (0, 1), x200, (2, 3), (0, 2, 1, 3))
    rdm2_f_oovv += einsum(x564, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x564, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x564, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x564, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x565 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x565 += einsum(l2, (0, 1, 2, 3), t2, (3, 4, 0, 5), (2, 4, 1, 5))
    x566 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x566 += einsum(t2, (0, 1, 2, 3), x565, (0, 4, 2, 5), (1, 4, 3, 5))
    x567 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x567 += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3))
    x567 += einsum(x161, (0, 1, 2, 3), (1, 2, 0, 3))
    x568 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x568 += einsum(x567, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (4, 2, 5, 6)) * 0.5
    x569 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x569 += einsum(x13, (0, 1, 2, 3), x154, (4, 1, 5, 2, 3, 6), (0, 4, 5, 6)) * 0.16666666666666666
    x570 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x570 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x570 += einsum(x149, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.6666666666666666
    x570 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x570 += einsum(x569, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x571 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x571 += einsum(x570, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (4, 2, 5, 6)) * 1.5
    x572 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x572 += einsum(x341, (0, 1, 2, 3), x57, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3))
    x573 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x573 += einsum(x283, (0, 1, 2, 3), (0, 1, 2, 3))
    x573 += einsum(x572, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x574 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x574 += einsum(x13, (0, 1, 2, 3), x573, (1, 4, 3, 5), (0, 4, 2, 5)) * 0.5
    x575 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x575 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 1, 5), (3, 4, 0, 5))
    x576 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x576 += einsum(x341, (0, 1, 2, 3), x57, (4, 1, 0, 5, 3, 6), (4, 5, 6, 2))
    x577 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x577 += einsum(t2, (0, 1, 2, 3), x44, (1, 4, 5, 3), (4, 0, 5, 2)) * 2.0
    x578 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x578 += einsum(x575, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x578 += einsum(x298, (0, 1, 2, 3), (0, 1, 2, 3))
    x578 += einsum(x576, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x578 += einsum(x577, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x579 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x579 += einsum(t2, (0, 1, 2, 3), x578, (1, 4, 2, 5), (4, 0, 5, 3)) * 0.5
    x580 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x580 += einsum(x341, (0, 1, 2, 3), x57, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    x581 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x581 += einsum(x346, (0, 1, 2, 3), (0, 1, 2, 3))
    x581 += einsum(x580, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x582 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x582 += einsum(t2, (0, 1, 2, 3), x581, (1, 4, 3, 5), (4, 0, 5, 2)) * 0.5
    x583 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x583 += einsum(x282, (0, 1, 2, 3), (0, 1, 2, 3))
    x583 += einsum(x566, (0, 1, 2, 3), (0, 1, 2, 3))
    x583 += einsum(x568, (0, 1, 2, 3), (1, 0, 2, 3))
    x583 += einsum(x571, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x583 += einsum(x574, (0, 1, 2, 3), (1, 0, 2, 3))
    x583 += einsum(x579, (0, 1, 2, 3), (0, 1, 2, 3))
    x583 += einsum(x582, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x583, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x583, (0, 1, 2, 3), (1, 0, 2, 3))
    x584 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x584 += einsum(x403, (0, 1, 2, 3), t3, (4, 0, 5, 6, 2, 1), (4, 5, 3, 6))
    x585 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x585 += einsum(x400, (0, 1, 2, 3), x131, (4, 5, 0, 6, 2, 1), (4, 5, 6, 3)) * 0.5
    x586 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x586 += einsum(x201, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x586 += einsum(x321, (0, 1, 2, 3), (0, 1, 2, 3))
    x586 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    x587 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x587 += einsum(t1, (0, 1), x586, (0, 2, 3, 4), (1, 2, 3, 4))
    x588 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x588 += einsum(x13, (0, 1, 2, 3), x587, (4, 3, 2, 5), (0, 1, 4, 5)) * 0.25
    x589 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x589 += einsum(t1, (0, 1), x206, (0, 2, 3, 4), (2, 3, 1, 4))
    x590 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x590 += einsum(x13, (0, 1, 2, 3), x589, (1, 4, 5, 2), (0, 4, 3, 5)) * 0.5
    x591 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x591 += einsum(x133, (0, 1, 2, 3), x131, (4, 5, 1, 6, 3, 2), (4, 5, 0, 6)) * 0.5
    x592 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x592 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3))
    x592 += einsum(x190, (0, 1, 2, 3), (0, 1, 2, 3))
    x592 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    x592 += einsum(x591, (0, 1, 2, 3), (2, 0, 1, 3))
    x592 += einsum(x335, (0, 1, 2, 3), (0, 1, 2, 3))
    x592 += einsum(x336, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x593 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x593 += einsum(t1, (0, 1), x592, (0, 2, 3, 4), (2, 3, 1, 4))
    x594 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x594 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x594 += einsum(x305, (0, 1, 2, 3), (0, 1, 2, 3))
    x594 += einsum(x584, (0, 1, 2, 3), (0, 1, 2, 3))
    x594 += einsum(x311, (0, 1, 2, 3), (0, 1, 3, 2))
    x594 += einsum(x314, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x594 += einsum(x585, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x594 += einsum(x317, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x594 += einsum(x320, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x594 += einsum(x588, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x594 += einsum(x329, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x594 += einsum(x590, (0, 1, 2, 3), (0, 1, 3, 2))
    x594 += einsum(x332, (0, 1, 2, 3), (0, 1, 2, 3))
    x594 += einsum(x593, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x594, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x594, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x595 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x595 += einsum(t2, (0, 1, 2, 3), x463, (0, 4, 2, 5), (4, 1, 5, 3))
    x596 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x596 += einsum(x57, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x596 += einsum(x57, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x597 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x597 += einsum(x6, (0, 1, 2, 3), x596, (4, 1, 0, 5, 2, 6), (4, 5, 3, 6))
    x598 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x598 += einsum(x297, (0, 1, 2, 3), (0, 1, 2, 3))
    x598 += einsum(x597, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x599 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x599 += einsum(t2, (0, 1, 2, 3), x598, (1, 4, 3, 5), (4, 0, 5, 2)) * 0.5
    x600 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x600 += einsum(l2, (0, 1, 2, 3), x6, (4, 3, 5, 1), (4, 2, 5, 0))
    x601 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x601 += einsum(x575, (0, 1, 2, 3), (0, 1, 2, 3))
    x601 += einsum(x600, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x602 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x602 += einsum(t2, (0, 1, 2, 3), x601, (1, 4, 3, 5), (4, 0, 5, 2))
    x603 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x603 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x603 += einsum(x346, (0, 1, 2, 3), (0, 1, 2, 3))
    x603 += einsum(x580, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x604 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x604 += einsum(t2, (0, 1, 2, 3), x603, (1, 4, 2, 5), (4, 0, 5, 3)) * 0.5
    x605 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x605 += einsum(t2, (0, 1, 2, 3), x596, (4, 1, 0, 5, 2, 6), (4, 5, 6, 3))
    x606 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x606 += einsum(t2, (0, 1, 2, 3), x605, (1, 4, 2, 5), (4, 0, 5, 3)) * 0.5
    x607 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x607 += einsum(t1, (0, 1), x196, (2, 3, 0, 4), (3, 2, 4, 1))
    x608 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x608 += einsum(t1, (0, 1), x607, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x609 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x609 += einsum(x595, (0, 1, 2, 3), (0, 1, 2, 3))
    x609 += einsum(x599, (0, 1, 2, 3), (0, 1, 3, 2))
    x609 += einsum(x602, (0, 1, 2, 3), (1, 0, 3, 2))
    x609 += einsum(x604, (0, 1, 2, 3), (0, 1, 2, 3))
    x609 += einsum(x606, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x609 += einsum(x608, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x609, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x609, (0, 1, 2, 3), (1, 0, 3, 2))
    x610 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x610 += einsum(t1, (0, 1), x209, (0, 2, 3, 4), (2, 3, 1, 4))
    x611 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x611 += einsum(x6, (0, 1, 2, 3), x610, (1, 4, 5, 3), (0, 4, 2, 5)) * 0.5
    x612 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x612 += einsum(x191, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x612 += einsum(x365, (0, 1, 2, 3), (0, 1, 2, 3))
    x612 += einsum(x366, (0, 1, 2, 3), (0, 1, 2, 3))
    x613 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x613 += einsum(t1, (0, 1), x612, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    x614 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x614 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    x614 += einsum(x362, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x614 += einsum(x611, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x614 += einsum(x613, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x614, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x614, (0, 1, 2, 3), (0, 1, 2, 3))
    x615 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x615 += einsum(x464, (0, 1, 2, 3), x6, (4, 0, 5, 2), (4, 1, 5, 3))
    rdm2_f_oovv += einsum(x615, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x615, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.5
    rdm2_f_oovv += einsum(x615, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x615, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    x616 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x616 += einsum(x532, (0, 1), x13, (2, 3, 0, 4), (2, 3, 4, 1)) * 1.5
    rdm2_f_oovv += einsum(x616, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x616, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.6666666666666666
    x617 = np.zeros((nvir, nvir), dtype=np.float64)
    x617 += einsum(x374, (0, 1), (0, 1))
    x617 += einsum(x388, (0, 1), (1, 0)) * -1.0
    rdm2_f_oovv += einsum(x617, (0, 1), x13, (2, 3, 0, 4), (2, 3, 1, 4)) * -0.5
    x618 = np.zeros((nvir, nvir), dtype=np.float64)
    x618 += einsum(l2, (0, 1, 2, 3), x387, (3, 2, 4, 0), (1, 4))
    rdm2_f_oovv += einsum(x618, (0, 1), x13, (2, 3, 0, 4), (2, 3, 4, 1)) * -0.5
    x619 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x619 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 5, 4, 1, 7, 2), (3, 6, 0, 7))
    rdm2_f_ovov += einsum(x619, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_ovov += einsum(x619, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_voov += einsum(x619, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.25
    rdm2_f_voov += einsum(x619, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.25
    x620 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x620 += einsum(t2, (0, 1, 2, 3), x50, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    rdm2_f_ovov += einsum(x620, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_ovov += einsum(x620, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_ovvo += einsum(x620, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.5
    rdm2_f_ovvo += einsum(x620, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.5
    rdm2_f_voov += einsum(x620, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_voov += einsum(x620, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_vovo += einsum(x620, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_vovo += einsum(x620, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.5
    x621 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x621 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x621 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 5.0
    x621 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x621 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x622 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x622 += einsum(l3, (0, 1, 2, 3, 4, 5), x621, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 0.25
    rdm2_f_ovov += einsum(x622, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovov += einsum(x622, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x622, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    rdm2_f_vovo += einsum(x622, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x623 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x623 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x623 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    x624 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x624 += einsum(t3, (0, 1, 2, 3, 4, 5), x623, (1, 6, 2, 7, 3, 5), (0, 6, 4, 7)) * 0.25
    rdm2_f_ovov += einsum(x624, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_ovov += einsum(x624, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_voov += einsum(x624, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_voov += einsum(x624, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x625 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x625 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x625 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x626 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x626 += einsum(l3, (0, 1, 2, 3, 4, 5), x625, (6, 3, 5, 7, 2, 1), (4, 6, 0, 7)) * 0.25
    rdm2_f_ovov += einsum(x626, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_ovov += einsum(x626, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_voov += einsum(x626, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_voov += einsum(x626, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x626, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_vovo += einsum(x626, (0, 1, 2, 3), (2, 1, 3, 0))
    x627 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x627 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 3.0
    x627 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x627 += einsum(x50, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x628 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x628 += einsum(t2, (0, 1, 2, 3), x627, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2)) * 0.5
    rdm2_f_ovov += einsum(x628, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_ovvo += einsum(x628, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x628, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x628, (0, 1, 2, 3), (2, 1, 3, 0))
    x629 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x629 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x629 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x630 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x630 += einsum(t2, (0, 1, 2, 3), x629, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    rdm2_f_ovov += einsum(x630, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x630, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x631 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x631 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x631 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x632 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x632 += einsum(l2, (0, 1, 2, 3), x631, (4, 3, 1, 5), (4, 2, 5, 0))
    rdm2_f_ovov += einsum(x632, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_voov += einsum(x632, (0, 1, 2, 3), (3, 0, 1, 2))
    x633 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x633 += einsum(l2, (0, 1, 2, 3), x6, (4, 2, 1, 5), (4, 3, 5, 0))
    rdm2_f_ovov += einsum(x633, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_voov += einsum(x633, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x634 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x634 += einsum(t1, (0, 1), x235, (2, 0, 3, 4), (2, 3, 1, 4)) * 0.5
    rdm2_f_ovov += einsum(x634, (0, 1, 2, 3), (1, 3, 0, 2))
    rdm2_f_ovvo += einsum(x634, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    rdm2_f_voov += einsum(x634, (0, 1, 2, 3), (3, 1, 0, 2)) * -1.0
    rdm2_f_vovo += einsum(x634, (0, 1, 2, 3), (3, 1, 2, 0))
    x635 = np.zeros((nvir, nvir), dtype=np.float64)
    x635 += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    x636 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x636 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x636 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.14285714285714288
    x636 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.14285714285714288
    x636 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 0.14285714285714288
    x636 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -0.14285714285714288
    x636 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * 0.14285714285714288
    x637 = np.zeros((nvir, nvir), dtype=np.float64)
    x637 += einsum(l3, (0, 1, 2, 3, 4, 5), x636, (3, 4, 5, 6, 1, 2), (0, 6)) * 0.58333333333331
    x638 = np.zeros((nvir, nvir), dtype=np.float64)
    x638 += einsum(l3, (0, 1, 2, 3, 4, 5), x361, (3, 4, 5, 1, 6, 2), (0, 6)) * 0.08333333333333
    x639 = np.zeros((nvir, nvir), dtype=np.float64)
    x639 += einsum(l2, (0, 1, 2, 3), x387, (3, 2, 1, 4), (4, 0)) * 0.5
    x640 = np.zeros((nvir, nvir), dtype=np.float64)
    x640 += einsum(x635, (0, 1), (0, 1))
    x640 += einsum(x374, (0, 1), (0, 1)) * 1.5
    x640 += einsum(x325, (0, 1), (0, 1)) * 0.24999999999999
    x640 += einsum(x637, (0, 1), (0, 1))
    x640 += einsum(x638, (0, 1), (0, 1))
    x640 += einsum(x639, (0, 1), (1, 0)) * -1.0
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x640, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x640, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x640, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_voov += einsum(delta.oo, (0, 1), x640, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x640, (2, 3), (2, 0, 3, 1))
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x640, (2, 3), (2, 0, 3, 1))
    x641 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x641 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 5), (2, 4, 1, 5))
    rdm2_f_ovov += einsum(x641, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x641, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x642 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x642 += einsum(x13, (0, 1, 2, 3), x55, (0, 4, 1, 5, 6, 3), (4, 5, 2, 6)) * 0.5
    rdm2_f_ovov += einsum(x642, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_ovov += einsum(x642, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_vovo += einsum(x642, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_vovo += einsum(x642, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    x643 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x643 += einsum(x13, (0, 1, 2, 3), l3, (2, 4, 3, 5, 6, 1), (5, 6, 0, 4)) * 0.5
    x644 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x644 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3))
    x644 += einsum(x24, (0, 1, 2, 3), (1, 0, 2, 3))
    x644 += einsum(x643, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovov += einsum(t1, (0, 1), x644, (2, 0, 3, 4), (3, 4, 2, 1)) * -1.0
    rdm2_f_voov += einsum(t1, (0, 1), x644, (0, 2, 3, 4), (4, 3, 2, 1)) * -1.0
    x645 = np.zeros((nvir, nvir), dtype=np.float64)
    x645 += einsum(x635, (0, 1), (0, 1))
    x645 += einsum(x374, (0, 1), (0, 1)) * 0.5
    x645 += einsum(x532, (0, 1), (0, 1))
    x645 += einsum(x325, (0, 1), (0, 1)) * 0.24999999999999
    x645 += einsum(x637, (0, 1), (0, 1))
    x645 += einsum(x638, (0, 1), (0, 1))
    x645 += einsum(x639, (0, 1), (1, 0)) * -1.0
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x645, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x645, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x645, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_voov += einsum(delta.oo, (0, 1), x645, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x645, (2, 3), (2, 0, 3, 1))
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x645, (2, 3), (2, 0, 3, 1))
    x646 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x646 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x646 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x646 += einsum(x140, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_ovov += einsum(t1, (0, 1), x646, (0, 2, 3, 4), (3, 4, 2, 1)) * -1.0
    rdm2_f_voov += einsum(t1, (0, 1), x646, (2, 0, 3, 4), (4, 3, 2, 1)) * -1.0
    x647 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x647 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x647 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x647 += einsum(x50, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x648 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x648 += einsum(t2, (0, 1, 2, 3), x647, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2)) * 0.5
    rdm2_f_ovov += einsum(x648, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_ovvo += einsum(x648, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x648, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x648, (0, 1, 2, 3), (2, 1, 3, 0))
    x649 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x649 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x649 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -0.3333333333333333
    x650 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x650 += einsum(t2, (0, 1, 2, 3), x649, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3)) * 1.5
    rdm2_f_ovov += einsum(x650, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vovo += einsum(x650, (0, 1, 2, 3), (2, 1, 3, 0))
    x651 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x651 += einsum(x133, (0, 1, 2, 3), x6, (4, 1, 3, 5), (4, 0, 5, 2))
    rdm2_f_ovov += einsum(x651, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_vovo += einsum(x651, (0, 1, 2, 3), (3, 0, 2, 1))
    x652 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x652 += einsum(x233, (0, 1, 2, 3), (0, 1, 2, 3))
    x652 += einsum(x233, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x652 += einsum(x205, (0, 1, 2, 3), (0, 1, 2, 3))
    x653 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x653 += einsum(t1, (0, 1), x652, (2, 0, 3, 4), (2, 3, 1, 4)) * 0.5
    rdm2_f_ovov += einsum(x653, (0, 1, 2, 3), (1, 3, 0, 2))
    rdm2_f_ovvo += einsum(x653, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    rdm2_f_voov += einsum(x653, (0, 1, 2, 3), (3, 1, 0, 2)) * -1.0
    rdm2_f_vovo += einsum(x653, (0, 1, 2, 3), (3, 1, 2, 0))
    x654 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x654 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 3, 5, 1, 7, 2), (4, 6, 0, 7))
    rdm2_f_ovvo += einsum(x654, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.25
    rdm2_f_ovvo += einsum(x654, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.25
    rdm2_f_vovo += einsum(x654, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    rdm2_f_vovo += einsum(x654, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    x655 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x655 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x655 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x655 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x655 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 5.0
    x656 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x656 += einsum(l3, (0, 1, 2, 3, 4, 5), x655, (6, 5, 4, 7, 2, 1), (3, 6, 0, 7)) * 0.25
    rdm2_f_ovvo += einsum(x656, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_ovvo += einsum(x656, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x656, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_voov += einsum(x656, (0, 1, 2, 3), (2, 1, 0, 3))
    x657 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x657 += einsum(l3, (0, 1, 2, 3, 4, 5), x251, (6, 4, 5, 1, 7, 2), (3, 6, 0, 7)) * 0.25
    rdm2_f_ovvo += einsum(x657, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_ovvo += einsum(x657, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_vovo += einsum(x657, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    rdm2_f_vovo += einsum(x657, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x658 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x658 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x658 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x659 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x659 += einsum(l3, (0, 1, 2, 3, 4, 5), x658, (6, 3, 5, 7, 2, 1), (4, 6, 0, 7)) * 0.25
    rdm2_f_ovvo += einsum(x659, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_ovvo += einsum(x659, (0, 1, 2, 3), (1, 2, 3, 0))
    x660 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x660 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x660 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x661 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x661 += einsum(t2, (0, 1, 2, 3), x660, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    rdm2_f_ovvo += einsum(x661, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x661, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x662 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x662 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * 2.0
    x662 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_ovvo += einsum(t2, (0, 1, 2, 3), x662, (4, 1, 5, 3), (0, 5, 2, 4))
    x663 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x663 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 6, 5, 1, 7, 2), (4, 6, 0, 7))
    rdm2_f_ovvo += einsum(x663, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.25
    rdm2_f_ovvo += einsum(x663, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.25
    rdm2_f_voov += einsum(x663, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.25
    rdm2_f_voov += einsum(x663, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.25
    x664 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x664 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x664 += einsum(t3, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x665 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x665 += einsum(l3, (0, 1, 2, 3, 4, 5), x664, (4, 6, 5, 1, 7, 2), (3, 6, 0, 7)) * 0.25
    rdm2_f_ovvo += einsum(x665, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_ovvo += einsum(x665, (0, 1, 2, 3), (1, 2, 3, 0))
    x666 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x666 += einsum(x13, (0, 1, 2, 3), x57, (0, 4, 1, 5, 6, 3), (4, 5, 6, 2)) * 0.5
    rdm2_f_ovvo += einsum(x666, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_ovvo += einsum(x666, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x666, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_voov += einsum(x666, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x667 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x667 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x667 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x667 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0))
    x668 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x668 += einsum(t2, (0, 1, 2, 3), x667, (4, 1, 5, 3), (4, 0, 5, 2))
    rdm2_f_ovvo += einsum(x668, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x668, (0, 1, 2, 3), (2, 1, 0, 3))
    x669 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x669 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x669 += einsum(x24, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x669 += einsum(x184, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovo += einsum(t1, (0, 1), x669, (2, 0, 3, 4), (4, 3, 1, 2)) * -0.5
    x670 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x670 += einsum(t1, (0, 1), x669, (0, 2, 3, 4), (2, 3, 1, 4)) * 0.5
    rdm2_f_ovvo += einsum(x670, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    x671 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x671 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 1, 5), (3, 4, 0, 5))
    rdm2_f_ovvo += einsum(x671, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x671, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x672 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x672 += einsum(l2, (0, 1, 2, 3), x164, (3, 4, 1, 5), (4, 2, 5, 0))
    rdm2_f_ovvo += einsum(x672, (0, 1, 2, 3), (0, 3, 2, 1))
    rdm2_f_voov += einsum(x672, (0, 1, 2, 3), (3, 0, 1, 2))
    x673 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x673 += einsum(t1, (0, 1), x144, (2, 0, 3, 4), (2, 3, 1, 4)) * 0.5
    rdm2_f_ovvo += einsum(x673, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    x674 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x674 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 3.0
    x674 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x675 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x675 += einsum(t2, (0, 1, 2, 3), x674, (4, 0, 1, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    rdm2_f_ovvo += einsum(x675, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x675, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x676 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x676 += einsum(x13, (0, 1, 2, 3), x133, (4, 1, 5, 2), (0, 4, 3, 5))
    rdm2_f_ovvo += einsum(x676, (0, 1, 2, 3), (0, 3, 2, 1))
    rdm2_f_voov += einsum(x676, (0, 1, 2, 3), (3, 0, 1, 2))
    x677 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x677 += einsum(l3, (0, 1, 2, 3, 4, 5), x416, (4, 6, 5, 1, 7, 2), (3, 6, 0, 7)) * 0.25
    rdm2_f_voov += einsum(x677, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_voov += einsum(x677, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x678 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x678 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x678 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.5
    rdm2_f_vovo += einsum(t2, (0, 1, 2, 3), x678, (4, 1, 5, 3), (5, 0, 2, 4)) * -2.0
    x679 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x679 += einsum(t3, (0, 1, 2, 3, 4, 5), x50, (0, 1, 2, 6, 7, 4), (6, 7, 3, 5))
    rdm2_f_ovvv += einsum(x679, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.66666666666668
    rdm2_f_ovvv += einsum(x679, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.66666666666668
    rdm2_f_vovv += einsum(x679, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.66666666666668
    rdm2_f_vovv += einsum(x679, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.66666666666668
    x680 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x680 += einsum(l1, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_ovvv += einsum(x680, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x680, (0, 1, 2, 3), (1, 0, 3, 2))
    x681 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x681 += einsum(t2, (0, 1, 2, 3), x175, (1, 3, 4, 5), (0, 4, 2, 5))
    x682 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x682 += einsum(x381, (0, 1, 2, 3, 4, 5), x50, (0, 2, 1, 6, 7, 5), (6, 7, 3, 4)) * 0.16666666666667
    x683 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x683 += einsum(x44, (0, 1, 2, 3), t3, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2)) * 0.5
    x684 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x684 += einsum(x13, (0, 1, 2, 3), l3, (4, 2, 3, 1, 5, 6), (5, 6, 0, 4)) * 0.5
    x685 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x685 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x685 += einsum(x684, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x686 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x686 += einsum(x294, (0, 1, 2, 3), x685, (1, 0, 4, 5), (4, 2, 3, 5)) * 0.5
    x687 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x687 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -0.2
    x687 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x687 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 0.2
    x687 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -0.2
    x688 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x688 += einsum(l3, (0, 1, 2, 3, 4, 5), x687, (6, 4, 5, 7, 2, 1), (3, 6, 0, 7)) * 1.25
    x689 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x689 += einsum(l3, (0, 1, 2, 3, 4, 5), x389, (6, 4, 5, 1, 7, 2), (3, 6, 0, 7)) * 0.25
    x690 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x690 += einsum(t2, (0, 1, 2, 3), x629, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    x691 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x691 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x691 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x692 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x692 += einsum(l2, (0, 1, 2, 3), x691, (4, 3, 5, 1), (4, 2, 5, 0)) * 2.0
    x693 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x693 += einsum(t1, (0, 1), x233, (2, 0, 3, 4), (2, 3, 1, 4)) * 0.5
    x694 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x694 += einsum(x654, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x694 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x694 += einsum(x620, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x694 += einsum(x688, (0, 1, 2, 3), (0, 1, 2, 3))
    x694 += einsum(x689, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x694 += einsum(x659, (0, 1, 2, 3), (0, 1, 2, 3))
    x694 += einsum(x628, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x694 += einsum(x690, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x694 += einsum(x692, (0, 1, 2, 3), (1, 0, 3, 2))
    x694 += einsum(x299, (0, 1, 2, 3), (1, 0, 3, 2))
    x694 += einsum(x693, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x695 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x695 += einsum(t1, (0, 1), x694, (0, 2, 3, 4), (2, 1, 3, 4))
    x696 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x696 += einsum(t2, (0, 1, 2, 3), x234, (0, 1, 4, 5), (4, 5, 2, 3)) * 0.25
    x697 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x697 += einsum(x680, (0, 1, 2, 3), (0, 1, 2, 3))
    x697 += einsum(x681, (0, 1, 2, 3), (0, 1, 2, 3))
    x697 += einsum(x682, (0, 1, 2, 3), (0, 1, 2, 3))
    x697 += einsum(x683, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x697 += einsum(x686, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x697 += einsum(x695, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x697 += einsum(x696, (0, 1, 2, 3), (0, 1, 2, 3))
    x697 += einsum(t1, (0, 1), x640, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvv += einsum(x697, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x697, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x697, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x697, (0, 1, 2, 3), (1, 0, 3, 2))
    x698 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x698 += einsum(t2, (0, 1, 2, 3), x142, (1, 4, 3, 5), (0, 4, 5, 2)) * -0.5
    rdm2_f_ovvv += einsum(x698, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_ovvv += einsum(x698, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    rdm2_f_vovv += einsum(x698, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x698, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x699 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x699 += einsum(t2, (0, 1, 2, 3), x98, (1, 4, 3, 5), (0, 4, 2, 5))
    rdm2_f_ovvv += einsum(x699, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    rdm2_f_ovvv += einsum(x699, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_vovv += einsum(x699, (0, 1, 2, 3), (1, 0, 2, 3)) * 1.5
    rdm2_f_vovv += einsum(x699, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x700 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x700 += einsum(t2, (0, 1, 2, 3), x98, (1, 4, 2, 5), (0, 4, 5, 3))
    rdm2_f_ovvv += einsum(x700, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_ovvv += einsum(x700, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    rdm2_f_vovv += einsum(x700, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_vovv += einsum(x700, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.5
    x701 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x701 += einsum(t3, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x701 += einsum(t3, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x702 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x702 += einsum(x50, (0, 1, 2, 3, 4, 5), x701, (0, 2, 1, 6, 5, 7), (3, 4, 6, 7)) * 0.16666666666667
    rdm2_f_ovvv += einsum(x702, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_ovvv += einsum(x702, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x702, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_vovv += einsum(x702, (0, 1, 2, 3), (1, 0, 2, 3))
    x703 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x703 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x703 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * 3.0
    x704 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x704 += einsum(x703, (0, 1, 2, 3), t3, (4, 0, 1, 5, 3, 6), (4, 5, 6, 2)) * 0.5
    rdm2_f_ovvv += einsum(x704, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_vovv += einsum(x704, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x705 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x705 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 5, 6, 0, 1), (6, 4, 5, 2))
    x706 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x706 += einsum(t2, (0, 1, 2, 3), l3, (4, 3, 5, 0, 6, 1), (6, 4, 5, 2))
    x707 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x707 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -1.0
    x707 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 0, 1, 2))
    x707 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    x708 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x708 += einsum(t2, (0, 1, 2, 3), x707, (4, 0, 1, 5, 2, 6), (4, 5, 6, 3))
    x709 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x709 += einsum(x705, (0, 1, 2, 3), (0, 1, 2, 3))
    x709 += einsum(x706, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x709 += einsum(x708, (0, 1, 2, 3), (0, 1, 2, 3))
    x710 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x710 += einsum(x13, (0, 1, 2, 3), x709, (1, 4, 2, 5), (0, 3, 4, 5)) * 0.5
    rdm2_f_ovvv += einsum(x710, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_vovv += einsum(x710, (0, 1, 2, 3), (2, 0, 1, 3))
    x711 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x711 += einsum(x321, (0, 1, 2, 3), x6, (4, 0, 5, 2), (4, 5, 1, 3)) * 0.5
    rdm2_f_ovvv += einsum(x711, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x711, (0, 1, 2, 3), (2, 0, 3, 1))
    x712 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x712 += einsum(t2, (0, 1, 2, 3), x142, (1, 4, 2, 5), (0, 4, 5, 3)) * -0.5
    rdm2_f_ovvv += einsum(x712, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x712, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x713 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x713 += einsum(t1, (0, 1), x19, (0, 2, 3, 4), (2, 3, 4, 1)) * 3.0
    rdm2_f_ovvv += einsum(t1, (0, 1), x713, (0, 2, 3, 4), (2, 3, 1, 4)) * -0.5
    x714 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x714 += einsum(l2, (0, 1, 2, 3), t3, (4, 3, 2, 5, 6, 0), (4, 1, 5, 6))
    rdm2_f_ovvv += einsum(x714, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x714, (0, 1, 2, 3), (1, 0, 3, 2))
    x715 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x715 += einsum(t2, (0, 1, 2, 3), x493, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_ovvv += einsum(x715, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x715, (0, 1, 2, 3), (1, 0, 3, 2))
    x716 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x716 += einsum(t3, (0, 1, 2, 3, 4, 5), x55, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4))
    rdm2_f_ovvv += einsum(x716, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.50000000000001
    rdm2_f_ovvv += einsum(x716, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.50000000000001
    rdm2_f_vovv += einsum(x716, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.50000000000001
    rdm2_f_vovv += einsum(x716, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.50000000000001
    x717 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x717 += einsum(t3, (0, 1, 2, 3, 4, 5), x57, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4))
    rdm2_f_ovvv += einsum(x717, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.50000000000001
    rdm2_f_ovvv += einsum(x717, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.50000000000001
    rdm2_f_vovv += einsum(x717, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.50000000000001
    rdm2_f_vovv += einsum(x717, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.50000000000001
    x718 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x718 += einsum(l2, (0, 1, 2, 3), x664, (3, 4, 2, 5, 6, 1), (4, 5, 6, 0)) * 0.5
    rdm2_f_ovvv += einsum(x718, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_ovvv += einsum(x718, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_vovv += einsum(x718, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_vovv += einsum(x718, (0, 1, 2, 3), (3, 0, 1, 2)) * -1.0
    x719 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x719 += einsum(x13, (0, 1, 2, 3), x135, (4, 1, 0, 5, 3, 6), (4, 2, 5, 6))
    x720 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x720 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * 1.5
    x720 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * -1.0
    x721 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x721 += einsum(x705, (0, 1, 2, 3), (0, 2, 1, 3))
    x721 += einsum(x719, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x721 += einsum(x142, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x721 += einsum(t2, (0, 1, 2, 3), x720, (4, 0, 1, 5, 2, 6), (4, 6, 5, 3)) * -2.0
    rdm2_f_ovvv += einsum(t2, (0, 1, 2, 3), x721, (1, 3, 4, 5), (0, 4, 2, 5)) * 0.5
    x722 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x722 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x722 += einsum(x142, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_vovv += einsum(t2, (0, 1, 2, 3), x722, (0, 4, 3, 5), (4, 1, 2, 5)) * -0.5
    x723 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x723 += einsum(t2, (0, 1, 2, 3), x722, (1, 2, 4, 5), (0, 4, 5, 3)) * 0.5
    rdm2_f_ovvv += einsum(x723, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x723, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x724 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x724 += einsum(x13, (0, 1, 2, 3), l3, (4, 5, 2, 0, 6, 1), (6, 4, 5, 3)) * 0.5
    rdm2_f_vvov += einsum(x724, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvov += einsum(x724, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vvov += einsum(x724, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vvov += einsum(x724, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo += einsum(x724, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x725 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x725 += einsum(x175, (0, 1, 2, 3), (0, 1, 2, 3))
    x725 += einsum(x724, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_ovvv += einsum(t2, (0, 1, 2, 3), x725, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x726 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x726 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3))
    x726 += einsum(x481, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x727 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x727 += einsum(t2, (0, 1, 2, 3), x726, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_ovvv += einsum(x727, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x727, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x728 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x728 += einsum(x13, (0, 1, 2, 3), x57, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    x729 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x729 += einsum(t2, (0, 1, 2, 3), x521, (1, 4, 5, 3), (4, 0, 5, 2))
    x730 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x730 += einsum(x345, (0, 1, 2, 3), (0, 1, 2, 3))
    x730 += einsum(x663, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x730 += einsum(x245, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x730 += einsum(x247, (0, 1, 2, 3), (0, 1, 2, 3))
    x730 += einsum(x546, (0, 1, 2, 3), (0, 1, 2, 3))
    x730 += einsum(x665, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x730 += einsum(x728, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x730 += einsum(x729, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x730 += einsum(x670, (0, 1, 2, 3), (0, 1, 3, 2))
    x731 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x731 += einsum(t1, (0, 1), x730, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_ovvv += einsum(x731, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x731, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x732 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x732 += einsum(x641, (0, 1, 2, 3), (0, 1, 2, 3))
    x732 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x732 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x732 += einsum(x480, (0, 1, 2, 3), (0, 1, 2, 3))
    x732 += einsum(x528, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x733 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x733 += einsum(t1, (0, 1), x732, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_ovvv += einsum(x733, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_vovv += einsum(x733, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x734 = np.zeros((nvir, nvir), dtype=np.float64)
    x734 += einsum(l3, (0, 1, 2, 3, 4, 5), x636, (3, 4, 5, 6, 1, 2), (0, 6)) * 1.16666666666662
    x735 = np.zeros((nvir, nvir), dtype=np.float64)
    x735 += einsum(l3, (0, 1, 2, 3, 4, 5), x361, (3, 4, 5, 1, 6, 2), (0, 6)) * 0.16666666666666
    x736 = np.zeros((nvir, nvir), dtype=np.float64)
    x736 += einsum(x635, (0, 1), (0, 1)) * 2.0
    x736 += einsum(x374, (0, 1), (0, 1))
    x736 += einsum(x532, (0, 1), (0, 1)) * 2.0
    x736 += einsum(x325, (0, 1), (0, 1)) * 0.49999999999998
    x736 += einsum(x734, (0, 1), (0, 1))
    x736 += einsum(x735, (0, 1), (0, 1))
    x736 += einsum(x388, (0, 1), (1, 0)) * -1.0
    rdm2_f_ovvv += einsum(t1, (0, 1), x736, (2, 3), (0, 2, 1, 3)) * 0.5
    rdm2_f_vovv += einsum(t1, (0, 1), x736, (2, 3), (2, 0, 3, 1)) * 0.5
    x737 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x737 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 6, 1), (4, 0, 5, 6))
    rdm2_f_ovvv += einsum(x737, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x737, (0, 1, 2, 3), (1, 0, 3, 2))
    x738 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x738 += einsum(l1, (0, 1), t2, (1, 2, 3, 4), (2, 0, 3, 4))
    rdm2_f_ovvv += einsum(x738, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_vovv += einsum(x738, (0, 1, 2, 3), (1, 0, 2, 3))
    x739 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x739 += einsum(x175, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x739 += einsum(x142, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_ovvv += einsum(x6, (0, 1, 2, 3), x739, (1, 2, 4, 5), (0, 4, 3, 5)) * 0.5
    rdm2_f_vovv += einsum(t2, (0, 1, 2, 3), x739, (1, 4, 2, 5), (4, 0, 3, 5)) * -0.5
    x740 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x740 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x740 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x740 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x741 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x741 += einsum(x201, (0, 1, 2, 3), (0, 1, 2, 3))
    x741 += einsum(x740, (0, 1, 2, 3), l3, (4, 3, 5, 6, 1, 0), (6, 4, 5, 2)) * -1.0
    x741 += einsum(x13, (0, 1, 2, 3), l3, (4, 3, 5, 0, 6, 1), (6, 4, 5, 2))
    rdm2_f_ovvv += einsum(t2, (0, 1, 2, 3), x741, (0, 4, 2, 5), (1, 4, 3, 5)) * -0.5
    x742 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x742 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3))
    x742 += einsum(x724, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_ovvv += einsum(t2, (0, 1, 2, 3), x742, (0, 4, 3, 5), (1, 4, 5, 2)) * -1.0
    x743 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x743 += einsum(l2, (0, 1, 2, 3), x387, (4, 3, 1, 5), (4, 2, 5, 0))
    x744 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x744 += einsum(x671, (0, 1, 2, 3), (0, 1, 2, 3))
    x744 += einsum(x663, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x744 += einsum(x245, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x744 += einsum(x406, (0, 1, 2, 3), (0, 1, 2, 3))
    x744 += einsum(x546, (0, 1, 2, 3), (0, 1, 2, 3))
    x744 += einsum(x665, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x744 += einsum(x728, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x744 += einsum(x743, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x744 += einsum(x673, (0, 1, 2, 3), (0, 1, 3, 2))
    x745 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x745 += einsum(t1, (0, 1), x744, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_ovvv += einsum(x745, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x745, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x746 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x746 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x746 += einsum(x488, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x747 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x747 += einsum(t2, (0, 1, 2, 3), x746, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_ovvv += einsum(x747, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x747, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x748 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x748 += einsum(t2, (0, 1, 2, 3), x237, (0, 1, 4, 5), (4, 5, 2, 3)) * -0.5
    rdm2_f_ovvv += einsum(x748, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_vovv += einsum(x748, (0, 1, 2, 3), (1, 0, 2, 3))
    x749 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x749 += einsum(x473, (0, 1, 2, 3), (0, 1, 2, 3))
    x749 += einsum(x474, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x749 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x749 += einsum(x476, (0, 1, 2, 3), (0, 1, 2, 3))
    x749 += einsum(x528, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x750 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x750 += einsum(t1, (0, 1), x749, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_ovvv += einsum(x750, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_vovv += einsum(x750, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x751 = np.zeros((nvir, nvir), dtype=np.float64)
    x751 += einsum(x635, (0, 1), (0, 1)) * 2.0
    x751 += einsum(x374, (0, 1), (0, 1)) * 3.0
    x751 += einsum(x325, (0, 1), (0, 1)) * 0.49999999999998
    x751 += einsum(x734, (0, 1), (0, 1))
    x751 += einsum(x735, (0, 1), (0, 1))
    x751 += einsum(x388, (0, 1), (1, 0)) * -1.0
    rdm2_f_ovvv += einsum(t1, (0, 1), x751, (2, 3), (0, 2, 1, 3)) * 0.5
    rdm2_f_vovv += einsum(t1, (0, 1), x751, (2, 3), (2, 0, 3, 1)) * 0.5
    x752 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x752 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 0, 6), (4, 1, 5, 6))
    rdm2_f_ovvv += einsum(x752, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x752, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x753 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x753 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 3, 0, 6, 1), (6, 4, 5, 2))
    x754 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x754 += einsum(t2, (0, 1, 2, 3), x753, (0, 4, 2, 5), (1, 4, 5, 3))
    x755 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x755 += einsum(x13, (0, 1, 2, 3), x551, (4, 1, 5, 6, 3, 2), (0, 4, 5, 6)) * 0.5
    x756 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x756 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    x756 += einsum(x226, (0, 1, 2, 3), (0, 1, 2, 3))
    x756 += einsum(x755, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x757 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x757 += einsum(t2, (0, 1, 2, 3), x756, (0, 1, 4, 5), (4, 5, 2, 3)) * 0.5
    x758 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x758 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 2, 0, 6, 1), (6, 4, 5, 3))
    x759 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x759 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3))
    x759 += einsum(x758, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x760 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x760 += einsum(t2, (0, 1, 2, 3), x759, (0, 2, 4, 5), (1, 4, 5, 3))
    x761 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x761 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x761 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * 3.0
    x762 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x762 += einsum(t2, (0, 1, 2, 3), x761, (4, 1, 0, 5, 6, 2), (4, 5, 6, 3)) * 0.5
    x763 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x763 += einsum(x44, (0, 1, 2, 3), x6, (4, 0, 5, 3), (4, 1, 5, 2))
    x764 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x764 += einsum(x463, (0, 1, 2, 3), (0, 1, 2, 3))
    x764 += einsum(x654, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x764 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x764 += einsum(x620, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x764 += einsum(x688, (0, 1, 2, 3), (0, 1, 2, 3))
    x764 += einsum(x689, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x764 += einsum(x659, (0, 1, 2, 3), (0, 1, 2, 3))
    x764 += einsum(x648, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x764 += einsum(x762, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x764 += einsum(x763, (0, 1, 2, 3), (1, 0, 3, 2))
    x764 += einsum(x693, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x765 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x765 += einsum(t1, (0, 1), x764, (0, 2, 3, 4), (2, 1, 3, 4))
    x766 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x766 += einsum(x13, (0, 1, 2, 3), l3, (4, 2, 3, 1, 5, 6), (5, 6, 0, 4))
    x767 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x767 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x767 += einsum(x766, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x768 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x768 += einsum(t2, (0, 1, 2, 3), x767, (1, 0, 4, 5), (4, 5, 2, 3)) * 0.25
    x769 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x769 += einsum(x680, (0, 1, 2, 3), (0, 1, 2, 3))
    x769 += einsum(x754, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x769 += einsum(x682, (0, 1, 2, 3), (0, 1, 2, 3))
    x769 += einsum(x683, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x769 += einsum(x757, (0, 1, 2, 3), (0, 1, 2, 3))
    x769 += einsum(x760, (0, 1, 2, 3), (0, 1, 3, 2))
    x769 += einsum(x765, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x769 += einsum(x768, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x769 += einsum(t1, (0, 1), x645, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvv += einsum(x769, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x769, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x769, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x769, (0, 1, 2, 3), (1, 0, 3, 2))
    x770 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x770 += einsum(x13, (0, 1, 2, 3), x201, (1, 4, 2, 5), (0, 4, 5, 3)) * 1.5
    rdm2_f_ovvv += einsum(x770, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_ovvv += einsum(x770, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    rdm2_f_vovv += einsum(x770, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x770, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.6666666666666666
    x771 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x771 += einsum(x321, (0, 1, 2, 3), (0, 1, 2, 3))
    x771 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    x772 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x772 += einsum(x6, (0, 1, 2, 3), x771, (1, 4, 3, 5), (0, 2, 4, 5)) * 0.5
    rdm2_f_ovvv += einsum(x772, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x772, (0, 1, 2, 3), (2, 0, 3, 1))
    x773 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x773 += einsum(x705, (0, 1, 2, 3), (0, 1, 2, 3))
    x773 += einsum(x719, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_ovvv += einsum(x6, (0, 1, 2, 3), x773, (1, 4, 2, 5), (0, 4, 3, 5)) * 0.5
    rdm2_f_vovv += einsum(x13, (0, 1, 2, 3), x773, (1, 4, 2, 5), (4, 0, 3, 5)) * 0.5
    x774 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x774 += einsum(t1, (0, 1), x48, (0, 2, 3, 4), (2, 3, 1, 4))
    x775 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x775 += einsum(t1, (0, 1), x774, (0, 2, 3, 4), (2, 1, 4, 3)) * 0.5
    rdm2_f_ovvv += einsum(x775, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_vovv += einsum(x775, (0, 1, 2, 3), (2, 0, 1, 3))
    x776 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x776 += einsum(t1, (0, 1), x19, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_vovv += einsum(t1, (0, 1), x776, (0, 2, 3, 4), (3, 2, 4, 1)) * 1.5
    x777 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x777 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x777 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x777 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vovv += einsum(x142, (0, 1, 2, 3), x777, (4, 0, 5, 2), (1, 4, 3, 5)) * -0.5
    x778 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x778 += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x778 += einsum(x321, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(t2, (0, 1, 2, 3), x778, (0, 4, 2, 5), (4, 1, 5, 3)) * -0.5
    x779 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x779 += einsum(l3, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * 2.0
    x779 += einsum(l3, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * -1.0
    x780 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x780 += einsum(x123, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.0
    x780 += einsum(x201, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x780 += einsum(x13, (0, 1, 2, 3), x779, (0, 4, 1, 5, 6, 2), (4, 5, 6, 3))
    x780 += einsum(x13, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (6, 4, 5, 2)) * -1.0
    rdm2_f_vovv += einsum(t2, (0, 1, 2, 3), x780, (1, 4, 3, 5), (4, 0, 5, 2)) * -0.5
    x781 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x781 += einsum(x215, (0, 1, 2, 3), l3, (4, 5, 2, 6, 0, 1), (6, 4, 5, 3)) * 0.5
    rdm2_f_vvov += einsum(x781, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvov += einsum(x781, (0, 1, 2, 3), (1, 2, 0, 3))
    x782 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x782 += einsum(t1, (0, 1), x133, (2, 0, 3, 4), (2, 1, 3, 4))
    rdm2_f_vvov += einsum(x782, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vvov += einsum(x782, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x783 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x783 += einsum(t1, (0, 1), l2, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_vvov += einsum(x783, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo += einsum(x783, (0, 1, 2, 3), (2, 1, 3, 0))
    x784 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x784 += einsum(t1, (0, 1), l2, (2, 3, 0, 4), (4, 2, 3, 1))
    rdm2_f_vvov += einsum(x784, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vvvo += einsum(x784, (0, 1, 2, 3), (1, 2, 3, 0))
    x785 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x785 += einsum(x13, (0, 1, 2, 3), x419, (4, 0, 1, 5, 6, 2), (4, 3, 5, 6)) * 0.5
    rdm2_f_vvvo += einsum(x785, (0, 1, 2, 3), (2, 3, 1, 0))
    rdm2_f_vvvo += einsum(x785, (0, 1, 2, 3), (2, 3, 1, 0))
    x786 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x786 += einsum(x13, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 0), (6, 4, 5, 2)) * 0.5
    rdm2_f_vvvo += einsum(x786, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_vvvo += einsum(x786, (0, 1, 2, 3), (1, 2, 3, 0))
    x787 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x787 += einsum(t1, (0, 1), x133, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_vvvo += einsum(x787, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vvvo += einsum(x787, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x788 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x788 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 6, 1, 7), (0, 2, 6, 7))
    rdm2_f_vvvv += einsum(x788, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000001
    rdm2_f_vvvv += einsum(x788, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000001
    x789 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x789 += einsum(l3, (0, 1, 2, 3, 4, 5), x381, (3, 5, 4, 6, 7, 2), (0, 1, 6, 7)) * 0.16666666666667
    x790 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x790 += einsum(l2, (0, 1, 2, 3), x341, (2, 3, 4, 5), (4, 5, 0, 1)) * 0.5
    x791 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x791 += einsum(x783, (0, 1, 2, 3), (0, 1, 2, 3))
    x791 += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3))
    x791 += einsum(x781, (0, 1, 2, 3), (0, 1, 2, 3))
    x791 += einsum(x724, (0, 1, 2, 3), (0, 1, 2, 3))
    x792 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x792 += einsum(t1, (0, 1), x791, (0, 2, 3, 4), (1, 2, 3, 4))
    x793 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x793 += einsum(x789, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x793 += einsum(x790, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x793 += einsum(x792, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvv += einsum(x793, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x793, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x794 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x794 += einsum(l3, (0, 1, 2, 3, 4, 5), x313, (4, 3, 5, 6, 2, 7), (0, 1, 6, 7)) * 0.16666666666667
    rdm2_f_vvvv += einsum(x794, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x794, (0, 1, 2, 3), (0, 1, 2, 3))
    x795 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x795 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 5), (0, 1, 4, 5))
    rdm2_f_vvvv += einsum(x795, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x795, (0, 1, 2, 3), (1, 0, 3, 2))
    x796 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x796 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7))
    rdm2_f_vvvv += einsum(x796, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000001
    rdm2_f_vvvv += einsum(x796, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.50000000000001
    rdm2_f_vvvv += einsum(x796, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000001
    rdm2_f_vvvv += einsum(x796, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.50000000000001
    x797 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x797 += einsum(t1, (0, 1), x142, (0, 2, 3, 4), (1, 2, 3, 4)) * -0.5
    rdm2_f_vvvv += einsum(x797, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_vvvv += einsum(x797, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vvvv += einsum(x797, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_vvvv += einsum(x797, (0, 1, 2, 3), (2, 1, 0, 3))
    x798 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x798 += einsum(x783, (0, 1, 2, 3), (0, 1, 2, 3))
    x798 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(t1, (0, 1), x798, (0, 2, 3, 4), (2, 3, 1, 4))
    x799 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x799 += einsum(x784, (0, 1, 2, 3), (0, 2, 1, 3))
    x799 += einsum(x175, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(t1, (0, 1), x799, (0, 2, 3, 4), (2, 3, 1, 4))
    x800 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x800 += einsum(x783, (0, 1, 2, 3), (0, 1, 2, 3))
    x800 += einsum(x201, (0, 1, 2, 3), (0, 1, 2, 3))
    x800 += einsum(x781, (0, 1, 2, 3), (0, 1, 2, 3))
    x800 += einsum(x724, (0, 1, 2, 3), (0, 1, 2, 3))
    x801 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x801 += einsum(t1, (0, 1), x800, (0, 2, 3, 4), (1, 2, 3, 4))
    x802 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x802 += einsum(x789, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x802 += einsum(x790, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x802 += einsum(x801, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvv += einsum(x802, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x802, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

