# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(f.ov, (0, 1), t1, (0, 1), ()) * 2.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x0 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x1 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    e_cc += einsum(x0, (0, 1, 2, 3), x1, (1, 0, 3, 2), ()) * 2.0

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t1new += einsum(t1, (0, 1), f.vv, (2, 1), (0, 2))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(t2, (0, 1, 2, 3), v.ovov, (1, 3, 4, 5), (4, 0, 5, 2))
    t2new += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    t2new += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 4), (3, 2, 4, 1)) * -1.0
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x0 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    x1 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x1 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x1 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2))
    t1new += einsum(x0, (0, 1, 2, 3), x1, (1, 2, 3, 4), (0, 4)) * 2.0
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(t1, (0, 1), v.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x3 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x3 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x3 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x3 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3))
    x3 += einsum(x2, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    t1new += einsum(t2, (0, 1, 2, 3), x3, (4, 1, 0, 3), (4, 2)) * -1.5
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x4 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x4 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x4 += einsum(x2, (0, 1, 2, 3), (0, 2, 1, 3))
    t1new += einsum(x4, (0, 1, 2, 3), t2, (2, 1, 3, 4), (0, 4)) * -0.5
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x5 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x6 = np.zeros((nocc, nvir), dtype=np.float64)
    x6 += einsum(f.ov, (0, 1), (0, 1))
    x6 += einsum(t1, (0, 1), x5, (0, 2, 1, 3), (2, 3)) * 2.0
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x7 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    t1new += einsum(x7, (0, 1, 2, 3), x6, (1, 2), (0, 3))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x8 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    t1new += einsum(t1, (0, 1), x8, (0, 2, 1, 3), (2, 3)) * 2.0
    x9 = np.zeros((nocc, nocc), dtype=np.float64)
    x9 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x10 = np.zeros((nocc, nocc), dtype=np.float64)
    x10 += einsum(x5, (0, 1, 2, 3), x0, (4, 0, 3, 2), (4, 1)) * 2.0
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x11 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    x12 = np.zeros((nocc, nocc), dtype=np.float64)
    x12 += einsum(x11, (0, 1, 2, 3), t1, (2, 3), (0, 1)) * 2.0
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum(f.oo, (0, 1), (1, 0))
    x13 += einsum(x9, (0, 1), (0, 1))
    x13 += einsum(x10, (0, 1), (1, 0))
    x13 += einsum(x12, (0, 1), (1, 0))
    t1new += einsum(x13, (0, 1), t1, (0, 2), (1, 2)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x13, (0, 4), (4, 1, 2, 3)) * -1.0
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 0, 1, 5), (4, 2, 5, 3))
    t2new += einsum(x14, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x15 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x15 += einsum(t1, (0, 1), v.vvvv, (2, 3, 1, 4), (0, 2, 3, 4))
    t2new += einsum(t1, (0, 1), x15, (2, 3, 1, 4), (0, 2, 3, 4))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum(x16, (0, 1, 2, 3), t2, (4, 1, 5, 2), (0, 4, 5, 3))
    t2new += einsum(x17, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x17, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(t2, (0, 1, 2, 3), x16, (4, 1, 2, 5), (4, 0, 3, 5))
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(t1, (0, 1), v.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x20 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x20 += einsum(v.ooov, (0, 1, 2, 3), x0, (4, 2, 3, 5), (0, 1, 4, 5))
    x21 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x21 += einsum(x19, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x21 += einsum(x20, (0, 1, 2, 3), (2, 1, 0, 3))
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(x21, (0, 1, 2, 3), t1, (1, 4), (0, 2, 4, 3))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3))
    x23 += einsum(x18, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x23 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x23, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x23, (0, 1, 2, 3), (1, 0, 2, 3))
    x24 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x24 += einsum(t2, (0, 1, 2, 3), x2, (4, 1, 5, 2), (4, 0, 5, 3))
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x25 += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 += einsum(t1, (0, 1), x25, (2, 3, 1, 4), (0, 2, 3, 4))
    x27 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x27 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x27 += einsum(x26, (0, 1, 2, 3), (0, 2, 1, 3))
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(x27, (0, 1, 2, 3), t1, (2, 4), (0, 1, 4, 3))
    t2new += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x28, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x29 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x29 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 2, 5, 3), (4, 0, 1, 5))
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(x29, (0, 1, 2, 3), t1, (2, 4), (0, 1, 4, 3))
    t2new += einsum(x30, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    t2new += einsum(x30, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(x14, (0, 1, 2, 3), t2, (4, 1, 5, 3), (4, 0, 5, 2))
    t2new += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    t2new += einsum(x31, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum(t2, (0, 1, 2, 3), x2, (4, 1, 5, 3), (4, 0, 5, 2))
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(t1, (0, 1), x32, (2, 3, 0, 4), (2, 3, 1, 4))
    t2new += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x33, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(v.ooov, (0, 1, 2, 3), t1, (2, 4), (0, 1, 4, 3))
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 1), (4, 0, 2, 3))
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x36 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x37 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(v.ovov, (0, 1, 2, 3), x0, (4, 0, 3, 5), (4, 2, 5, 1))
    x39 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * 2.0
    x39 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x39 += einsum(x34, (0, 1, 2, 3), (1, 0, 2, 3))
    x39 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x39 += einsum(x36, (0, 1, 2, 3), x37, (0, 4, 5, 2), (1, 4, 3, 5)) * 2.0
    x39 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x39, (0, 1, 2, 3), t2, (4, 1, 5, 3), (4, 0, 5, 2))
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x40 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x41 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x41 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2))
    x41 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x42 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x43 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x43 += einsum(x40, (0, 1, 2, 3), x0, (4, 0, 3, 5), (4, 1, 5, 2)) * -1.0
    x43 += einsum(x41, (0, 1, 2, 3), t1, (4, 2), (4, 0, 3, 1)) * -1.0
    x43 += einsum(x42, (0, 1, 2, 3), t1, (2, 4), (1, 0, 4, 3)) * -1.0
    t2new += einsum(x43, (0, 1, 2, 3), t2, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x44 += einsum(x34, (0, 1, 2, 3), (1, 0, 2, 3))
    x44 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x44 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x44, (0, 1, 2, 3), t2, (1, 4, 5, 3), (0, 4, 5, 2))
    x45 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x45 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x45 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3))
    x46 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x46 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x46 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x46 += einsum(x45, (0, 1, 2, 3), t1, (1, 4), (0, 2, 4, 3))
    t2new += einsum(x46, (0, 1, 2, 3), t2, (4, 1, 3, 5), (4, 0, 2, 5))
    x47 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x47 += einsum(t1, (0, 1), v.ovvv, (0, 2, 3, 4), (1, 2, 3, 4))
    x48 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x48 += einsum(v.vvvv, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x48 += einsum(x47, (0, 1, 2, 3), (1, 0, 3, 2))
    x48 += einsum(x47, (0, 1, 2, 3), (3, 2, 0, 1))
    t2new += einsum(x48, (0, 1, 2, 3), t2, (4, 5, 3, 0), (4, 5, 2, 1)) * -1.0
    x49 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x49 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x50 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x50 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x50 += einsum(x49, (0, 1, 2, 3), (3, 0, 2, 1))
    x50 += einsum(x49, (0, 1, 2, 3), (2, 1, 3, 0))
    x50 += einsum(v.ovov, (0, 1, 2, 3), x0, (4, 5, 3, 1), (2, 4, 0, 5))
    t2new += einsum(t2, (0, 1, 2, 3), x50, (0, 4, 1, 5), (4, 5, 2, 3))
    x51 = np.zeros((nvir, nvir), dtype=np.float64)
    x51 += einsum(t1, (0, 1), f.ov, (0, 2), (2, 1))
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    x52 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x52 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x53 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 4.0
    x53 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x53 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x54 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x54 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x54 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2)) * 2.0
    x55 = np.zeros((nvir, nvir), dtype=np.float64)
    x55 += einsum(x54, (0, 1, 2, 3), t1, (0, 2), (1, 3)) * 0.5
    x56 = np.zeros((nvir, nvir), dtype=np.float64)
    x56 += einsum(f.vv, (0, 1), (1, 0)) * -0.5
    x56 += einsum(x51, (0, 1), (0, 1)) * 0.5
    x56 += einsum(v.ovov, (0, 1, 2, 3), x52, (0, 2, 3, 4), (1, 4)) * -0.25
    x56 += einsum(x53, (0, 1, 2, 3), v.ovov, (0, 2, 1, 4), (4, 3)) * 0.25
    x56 += einsum(x55, (0, 1), (0, 1)) * -1.0
    t2new += einsum(x56, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 0.6666666666666666
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x58 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x58 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 4.0
    x58 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x58 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 = np.zeros((nvir, nvir), dtype=np.float64)
    x59 += einsum(f.vv, (0, 1), (1, 0)) * -0.5
    x59 += einsum(x51, (0, 1), (0, 1)) * 0.5
    x59 += einsum(x57, (0, 1, 2, 3), v.ovov, (0, 4, 1, 2), (4, 3)) * -0.75
    x59 += einsum(x58, (0, 1, 2, 3), v.ovov, (0, 2, 1, 4), (4, 3)) * 0.25
    x59 += einsum(x55, (0, 1), (0, 1)) * -1.0
    t2new += einsum(t2, (0, 1, 2, 3), x59, (2, 4), (0, 1, 4, 3)) * -2.0
    x60 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x60 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    x60 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x60 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x61 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x61 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x61 += einsum(t1, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    x62 = np.zeros((nocc, nocc), dtype=np.float64)
    x62 += einsum(f.oo, (0, 1), (1, 0))
    x62 += einsum(x9, (0, 1), (0, 1))
    x62 += einsum(v.ovov, (0, 1, 2, 3), x60, (0, 4, 3, 1), (2, 4)) * -1.0
    x62 += einsum(x12, (0, 1), (1, 0))
    x62 += einsum(v.ovov, (0, 1, 2, 3), x61, (4, 0, 3, 1), (2, 4))
    t2new += einsum(t2, (0, 1, 2, 3), x62, (1, 4), (0, 4, 2, 3)) * -1.0
    x63 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x63 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x63 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 2, 5, 3), (5, 1, 0, 4))
    x63 += einsum(x2, (0, 1, 2, 3), t1, (4, 3), (1, 4, 0, 2))
    x64 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x64 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x64 += einsum(t1, (0, 1), x63, (0, 2, 3, 4), (3, 2, 4, 1))
    t2new += einsum(x64, (0, 1, 2, 3), t1, (2, 4), (0, 1, 4, 3))
    x65 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x65 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x65 += einsum(x14, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x65, (0, 1, 2, 3), t2, (4, 1, 3, 5), (0, 4, 2, 5))

    return {"t1new": t1new, "t2new": t2new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    # L amplitudes
    l1new = np.zeros((nvir, nocc), dtype=np.float64)
    l1new += einsum(v.oovv, (0, 1, 2, 3), l1, (3, 1), (2, 0)) * -1.0
    l1new += einsum(f.ov, (0, 1), (1, 0))
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(l2, (0, 1, 2, 3), v.vvvv, (4, 1, 5, 0), (5, 4, 2, 3))
    l2new += einsum(v.ovov, (0, 1, 2, 3), (3, 1, 2, 0))
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x0 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x1 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x3 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.3333333333333333
    x3 += einsum(x0, (0, 1, 2, 3), x1, (0, 4, 5, 2), (1, 4, 3, 5)) * 1.3333333333333333
    x3 += einsum(x2, (0, 1, 2, 3), l2, (4, 3, 5, 0), (5, 1, 4, 2)) * 0.6666666666666666
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x3, (4, 0, 2, 1), (3, 4)) * 1.5
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(t2, (0, 1, 2, 3), f.ov, (4, 2), (4, 0, 1, 3))
    x5 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x5 += einsum(t2, (0, 1, 2, 3), f.ov, (4, 3), (4, 0, 1, 2))
    x6 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x6 += einsum(v.ovvv, (0, 1, 2, 3), t2, (4, 5, 1, 2), (4, 5, 0, 3))
    x7 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x7 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 5, 3, 1), (4, 5, 2, 0))
    x8 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x8 += einsum(x7, (0, 1, 2, 3), t1, (3, 4), (0, 1, 2, 4))
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -0.5
    x9 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x10 = np.zeros((nocc, nvir), dtype=np.float64)
    x10 += einsum(t1, (0, 1), x9, (0, 2, 1, 3), (2, 3))
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(x10, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x12 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x12 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum(v.ovvv, (0, 1, 2, 3), t2, (4, 5, 2, 1), (4, 5, 0, 3))
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(t1, (0, 1), x7, (2, 3, 0, 4), (2, 3, 4, 1))
    x15 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(t2, (0, 1, 2, 3), x10, (4, 3), (0, 1, 4, 2))
    x16 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(x13, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x16 += einsum(x14, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x16 += einsum(x15, (0, 1, 2, 3), (0, 1, 2, 3))
    x17 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x17 += einsum(t1, (0, 1), v.ovov, (2, 1, 3, 4), (0, 3, 2, 4))
    x18 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x18 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x18 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x18 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3))
    x18 += einsum(x17, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x19 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x19 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x19 += einsum(x17, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x20 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x21 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x21 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x22 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x22 += einsum(v.oooo, (0, 1, 2, 3), (2, 1, 3, 0))
    x22 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -0.5
    x22 += einsum(x21, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.5
    x22 += einsum(x21, (0, 1, 2, 3), (3, 2, 0, 1))
    x23 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x23 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x23 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x23 += einsum(x4, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.5
    x23 += einsum(x4, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.5
    x23 += einsum(x5, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.5
    x23 += einsum(x5, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    x23 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x23 += einsum(x12, (0, 1, 2, 3), (1, 0, 2, 3)) * -3.0
    x23 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x23 += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3))
    x23 += einsum(x18, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5)) * 2.0
    x23 += einsum(t2, (0, 1, 2, 3), x19, (4, 1, 5, 2), (4, 0, 5, 3))
    x23 += einsum(t1, (0, 1), x20, (2, 3, 1, 4), (0, 3, 2, 4)) * -1.0
    x23 += einsum(t1, (0, 1), x22, (0, 2, 3, 4), (3, 2, 4, 1)) * 2.0
    l1new += einsum(l2, (0, 1, 2, 3), x23, (3, 2, 4, 1), (0, 4))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x24 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x25 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x25 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x25, (4, 5, 0, 3), (1, 2, 4, 5)) * -1.0
    l2new += einsum(x25, (0, 1, 2, 3), v.ooov, (1, 4, 2, 5), (5, 3, 0, 4))
    l2new += einsum(x25, (0, 1, 2, 3), x17, (1, 2, 4, 5), (5, 3, 0, 4))
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x26 += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3))
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    x27 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 5), (2, 4, 1, 5))
    x27 += einsum(x24, (0, 1, 2, 3), x0, (4, 0, 2, 5), (4, 1, 5, 3)) * -1.0
    x27 += einsum(x26, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3)) * 2.0
    l1new += einsum(x27, (0, 1, 2, 3), v.ovvv, (1, 4, 3, 2), (4, 0)) * -1.0
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x28 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x29 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x29 += einsum(t1, (0, 1), x28, (2, 0, 3, 4), (2, 3, 4, 1)) * -1.0
    l1new += einsum(x29, (0, 1, 2, 3), v.vvvv, (2, 4, 1, 3), (4, 0)) * -0.5
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x30 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.3333333333333333
    x31 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x31 += einsum(t1, (0, 1), x30, (2, 0, 3, 4), (2, 3, 4, 1)) * 3.0
    l1new += einsum(v.vvvv, (0, 1, 2, 3), x31, (4, 3, 0, 1), (2, 4)) * 0.5
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x32, (4, 5, 0, 3), (2, 1, 4, 5)) * -1.0
    l2new += einsum(v.ooov, (0, 1, 2, 3), x32, (4, 0, 2, 5), (5, 3, 4, 1))
    l2new += einsum(v.ooov, (0, 1, 2, 3), x32, (0, 4, 2, 5), (5, 3, 1, 4))
    l2new += einsum(x32, (0, 1, 2, 3), x17, (1, 2, 4, 5), (3, 5, 0, 4))
    l2new += einsum(x32, (0, 1, 2, 3), x17, (0, 2, 4, 5), (3, 5, 4, 1))
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    x33 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x33 += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3))
    l1new += einsum(x33, (0, 1, 2, 3), v.oovv, (1, 2, 3, 4), (4, 0)) * -1.0
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0))
    x34 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x34 += einsum(t1, (0, 1), x33, (2, 0, 3, 4), (2, 3, 4, 1)) * 2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x34, (4, 0, 2, 1), (3, 4)) * -0.5
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 1), (4, 0, 2, 3))
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum(t1, (0, 1), x35, (2, 3, 4, 1), (2, 0, 3, 4))
    x37 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x37 += einsum(x17, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x38 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x38 += einsum(t1, (0, 1), x37, (2, 3, 4, 0), (2, 3, 4, 1))
    x39 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x39 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x39 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x40 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x40 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3))
    x40 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3))
    x41 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x41 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x41 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.3333333333333333
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x42 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    x43 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x43 += einsum(x21, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x43 += einsum(x21, (0, 1, 2, 3), (0, 3, 2, 1)) * 2.0
    x44 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x44 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3))
    x44 += einsum(x39, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x44 += einsum(x2, (0, 1, 2, 3), x40, (4, 5, 1, 2), (4, 0, 5, 3)) * -1.0
    x44 += einsum(x41, (0, 1, 2, 3), x40, (4, 1, 5, 2), (4, 0, 5, 3)) * 3.0
    x44 += einsum(t1, (0, 1), x42, (2, 3, 1, 4), (0, 3, 2, 4)) * 2.0
    x44 += einsum(t1, (0, 1), x43, (2, 3, 4, 0), (2, 4, 3, 1)) * -1.0
    l1new += einsum(l2, (0, 1, 2, 3), x44, (2, 3, 4, 1), (0, 4)) * -1.0
    x45 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x45 += einsum(x32, (0, 1, 2, 3), t1, (4, 3), (0, 1, 4, 2))
    x46 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x46 += einsum(x45, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    x47 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x47 += einsum(x45, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4))
    x48 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x48 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x48 += einsum(x32, (0, 1, 2, 3), (1, 0, 2, 3))
    x49 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x49 += einsum(l2, (0, 1, 2, 3), x24, (4, 5, 1, 0), (2, 3, 4, 5))
    x50 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x50 += einsum(x49, (0, 1, 2, 3), (0, 1, 2, 3))
    x50 += einsum(x49, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x51 = np.zeros((nocc, nocc), dtype=np.float64)
    x51 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x52 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x53 = np.zeros((nocc, nocc), dtype=np.float64)
    x53 += einsum(x52, (0, 1, 2, 3), x28, (0, 4, 3, 2), (4, 1)) * 0.5
    x54 = np.zeros((nocc, nocc), dtype=np.float64)
    x54 += einsum(x51, (0, 1), (0, 1))
    x54 += einsum(x53, (0, 1), (0, 1)) * -1.0
    x55 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x55 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x55 += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x55 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x55 += einsum(x46, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.5
    x55 += einsum(x47, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x55 += einsum(x47, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x55 += einsum(x1, (0, 1, 2, 3), x48, (4, 0, 5, 3), (4, 1, 5, 2)) * 2.0
    x55 += einsum(x2, (0, 1, 2, 3), x25, (4, 0, 5, 3), (4, 1, 5, 2))
    x55 += einsum(l1, (0, 1), x24, (2, 3, 0, 4), (1, 2, 3, 4)) * -0.5
    x55 += einsum(t1, (0, 1), x50, (2, 0, 3, 4), (2, 3, 4, 1)) * -0.25
    x55 += einsum(x54, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    l1new += einsum(v.ovov, (0, 1, 2, 3), x55, (4, 0, 2, 1), (3, 4)) * -1.0
    x56 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x56 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    x56 += einsum(x32, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x58 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x58 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    x59 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x59 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 1, 0), (2, 3, 4, 5))
    x60 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x60 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.000000000000001
    x60 += einsum(x58, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x60 += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x60 += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3))
    x61 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x61 += einsum(x25, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5)) * 0.6666666666666666
    x61 += einsum(x32, (0, 1, 2, 3), t2, (4, 1, 3, 5), (0, 4, 2, 5)) * 0.6666666666666666
    x61 += einsum(x52, (0, 1, 2, 3), x56, (4, 0, 5, 3), (4, 1, 5, 2)) * -0.6666666666666666
    x61 += einsum(x57, (0, 1, 2, 3), l1, (2, 4), (4, 0, 1, 3)) * -0.3333333333333333
    x61 += einsum(t1, (0, 1), x60, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.16666666666666666
    x61 += einsum(x54, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.6666666666666666
    l1new += einsum(v.ovov, (0, 1, 2, 3), x61, (4, 0, 2, 3), (1, 4)) * 1.5
    x62 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x62 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x62 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x62 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x63 = np.zeros((nvir, nvir), dtype=np.float64)
    x63 += einsum(t1, (0, 1), l1, (2, 0), (2, 1))
    x63 += einsum(l2, (0, 1, 2, 3), x62, (2, 3, 4, 0), (1, 4)) * -0.5
    x64 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x64 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2))
    x64 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2)) * -0.5
    l1new += einsum(x63, (0, 1), x64, (2, 3, 1, 0), (3, 2)) * 2.0
    x65 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x65 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x65 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x65 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x66 = np.zeros((nocc, nocc), dtype=np.float64)
    x66 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    l1new += einsum(x66, (0, 1), x10, (1, 2), (2, 0)) * -2.0
    l2new += einsum(v.ovov, (0, 1, 2, 3), x66, (4, 2), (1, 3, 0, 4)) * -1.0
    x67 = np.zeros((nocc, nocc), dtype=np.float64)
    x67 += einsum(l2, (0, 1, 2, 3), t2, (3, 4, 0, 1), (2, 4))
    x68 = np.zeros((nocc, nocc), dtype=np.float64)
    x68 += einsum(x66, (0, 1), (0, 1)) * 2.0
    x68 += einsum(x67, (0, 1), (0, 1)) * -1.0
    x68 += einsum(t2, (0, 1, 2, 3), x28, (0, 4, 3, 2), (4, 1))
    x69 = np.zeros((nocc, nvir), dtype=np.float64)
    x69 += einsum(t1, (0, 1), (0, 1))
    x69 += einsum(t2, (0, 1, 2, 3), l1, (3, 0), (1, 2)) * -1.0
    x69 += einsum(x65, (0, 1, 2, 3), x32, (1, 0, 4, 2), (4, 3)) * 0.5
    x69 += einsum(t1, (0, 1), x68, (0, 2), (2, 1)) * -0.5
    x70 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x70 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * 2.0
    x70 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    l1new += einsum(x69, (0, 1), x70, (0, 2, 3, 1), (3, 2))
    x71 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x71 += einsum(x49, (0, 1, 2, 3), (0, 1, 2, 3))
    x71 += einsum(x49, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x71 += einsum(x45, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.0
    x71 += einsum(x45, (0, 1, 2, 3), (0, 3, 1, 2)) * 6.0
    x71 += einsum(x45, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    x71 += einsum(x45, (0, 1, 2, 3), (1, 3, 0, 2)) * -2.0
    l1new += einsum(x71, (0, 1, 2, 3), v.ooov, (2, 1, 3, 4), (4, 0)) * 0.25
    x72 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x72 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3)) * 5.0
    x72 += einsum(x58, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x72 += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x72 += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3))
    l1new += einsum(x72, (0, 1, 2, 3), v.ooov, (3, 1, 2, 4), (4, 0)) * 0.25
    x73 = np.zeros((nocc, nvir), dtype=np.float64)
    x73 += einsum(x25, (0, 1, 2, 3), t2, (0, 1, 4, 3), (2, 4))
    x74 = np.zeros((nocc, nvir), dtype=np.float64)
    x74 += einsum(x32, (0, 1, 2, 3), t2, (0, 1, 3, 4), (2, 4))
    x75 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x75 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x75 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x76 = np.zeros((nocc, nocc), dtype=np.float64)
    x76 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 1), (3, 4))
    x77 = np.zeros((nocc, nocc), dtype=np.float64)
    x77 += einsum(x51, (0, 1), (0, 1))
    x77 += einsum(x76, (0, 1), (0, 1)) * 0.5
    l1new += einsum(x77, (0, 1), v.ooov, (0, 2, 1, 3), (3, 2))
    x78 = np.zeros((nocc, nvir), dtype=np.float64)
    x78 += einsum(x73, (0, 1), (0, 1))
    x78 += einsum(x74, (0, 1), (0, 1)) * 0.5
    x78 += einsum(x75, (0, 1, 2, 3), l1, (3, 1), (0, 2)) * -1.0
    x78 += einsum(x77, (0, 1), t1, (0, 2), (1, 2))
    l1new += einsum(v.ovov, (0, 1, 2, 3), x78, (0, 3), (1, 2))
    x79 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x79 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x79 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x80 = np.zeros((nocc, nocc), dtype=np.float64)
    x80 += einsum(x51, (0, 1), (0, 1))
    x80 += einsum(x76, (0, 1), (0, 1)) * 2.0
    l1new += einsum(x80, (0, 1), v.ooov, (1, 0, 2, 3), (3, 2)) * -1.0
    x81 = np.zeros((nocc, nvir), dtype=np.float64)
    x81 += einsum(l1, (0, 1), (1, 0)) * -2.0
    x81 += einsum(x73, (0, 1), (0, 1))
    x81 += einsum(x74, (0, 1), (0, 1)) * 2.0
    x81 += einsum(l1, (0, 1), x79, (2, 1, 3, 0), (2, 3)) * -1.0
    x81 += einsum(x80, (0, 1), t1, (0, 2), (1, 2))
    l1new += einsum(v.ovov, (0, 1, 2, 3), x81, (0, 1), (3, 2)) * -1.0
    x82 = np.zeros((nvir, nvir), dtype=np.float64)
    x82 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x83 = np.zeros((nvir, nvir), dtype=np.float64)
    x83 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 0, 4), (1, 4))
    l2new += einsum(x83, (0, 1), v.ovov, (2, 1, 3, 4), (4, 0, 3, 2)) * -1.0
    x84 = np.zeros((nvir, nvir), dtype=np.float64)
    x84 += einsum(x82, (0, 1), (0, 1))
    x84 += einsum(x83, (0, 1), (0, 1)) * 2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x84, (3, 2), (1, 0))
    x85 = np.zeros((nvir, nvir), dtype=np.float64)
    x85 += einsum(x82, (0, 1), (0, 1))
    x85 += einsum(x83, (0, 1), (0, 1)) * 0.5
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x85, (2, 1), (3, 0)) * -1.0
    x86 = np.zeros((nocc, nocc), dtype=np.float64)
    x86 += einsum(x66, (0, 1), (0, 1))
    x86 += einsum(x67, (0, 1), (0, 1)) * -0.5
    x86 += einsum(t2, (0, 1, 2, 3), x28, (0, 4, 3, 2), (4, 1)) * 0.5
    x87 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x87 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x87 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    l1new += einsum(x87, (0, 1, 2, 3), x86, (0, 2), (3, 1)) * -1.0
    x88 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x88 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x88 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2))
    x89 = np.zeros((nvir, nvir), dtype=np.float64)
    x89 += einsum(t1, (0, 1), x88, (0, 2, 1, 3), (2, 3))
    x90 = np.zeros((nvir, nvir), dtype=np.float64)
    x90 += einsum(f.vv, (0, 1), (1, 0)) * 0.5
    x90 += einsum(x89, (0, 1), (1, 0))
    l1new += einsum(l1, (0, 1), x90, (0, 2), (2, 1)) * 2.0
    x91 = np.zeros((nocc, nocc), dtype=np.float64)
    x91 += einsum(t2, (0, 1, 2, 3), x9, (1, 4, 3, 2), (0, 4)) * 2.0
    x92 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x92 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x92 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.5
    x93 = np.zeros((nocc, nocc), dtype=np.float64)
    x93 += einsum(x92, (0, 1, 2, 3), t1, (2, 3), (0, 1)) * 2.0
    x94 = np.zeros((nocc, nvir), dtype=np.float64)
    x94 += einsum(t1, (0, 1), x9, (0, 2, 1, 3), (2, 3)) * 2.0
    x95 = np.zeros((nocc, nvir), dtype=np.float64)
    x95 += einsum(f.ov, (0, 1), (0, 1))
    x95 += einsum(x94, (0, 1), (0, 1))
    l2new += einsum(x25, (0, 1, 2, 3), x95, (2, 4), (4, 3, 0, 1)) * -1.0
    l2new += einsum(x32, (0, 1, 2, 3), x95, (2, 4), (3, 4, 0, 1)) * -1.0
    x96 = np.zeros((nocc, nocc), dtype=np.float64)
    x96 += einsum(x95, (0, 1), t1, (2, 1), (2, 0))
    x97 = np.zeros((nocc, nocc), dtype=np.float64)
    x97 += einsum(f.oo, (0, 1), (1, 0))
    x97 += einsum(x91, (0, 1), (0, 1))
    x97 += einsum(x93, (0, 1), (1, 0))
    x97 += einsum(x96, (0, 1), (0, 1))
    l1new += einsum(x97, (0, 1), l1, (2, 0), (2, 1)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x97, (2, 4), (0, 1, 4, 3)) * -1.0
    x98 = np.zeros((nocc, nocc), dtype=np.float64)
    x98 += einsum(x66, (0, 1), (0, 1)) * 2.0
    x98 += einsum(x51, (0, 1), (0, 1)) * 2.0
    x98 += einsum(x52, (0, 1, 2, 3), x28, (0, 4, 3, 2), (4, 1)) * -1.0
    l1new += einsum(f.ov, (0, 1), x98, (2, 0), (1, 2)) * -0.5
    x99 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 += einsum(v.ovov, (0, 1, 2, 3), t2, (2, 4, 3, 5), (4, 0, 5, 1))
    l2new += einsum(x99, (0, 1, 2, 3), l2, (4, 2, 5, 0), (4, 3, 5, 1))
    x100 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x100 += einsum(v.ooov, (0, 1, 2, 3), x32, (4, 0, 1, 5), (4, 2, 5, 3))
    x101 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x101 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3))
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(x101, (0, 1, 2, 3), l2, (4, 3, 5, 0), (5, 1, 4, 2))
    x103 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x103 += einsum(x32, (0, 1, 2, 3), x17, (1, 4, 2, 5), (0, 4, 3, 5))
    x104 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x104 += einsum(l2, (0, 1, 2, 3), t2, (3, 4, 5, 1), (2, 4, 0, 5))
    x105 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x105 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 1, 5), (3, 4, 0, 5))
    x106 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x106 += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3))
    x106 += einsum(x105, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum(x106, (0, 1, 2, 3), v.ovov, (1, 3, 4, 5), (4, 0, 5, 2)) * 2.0
    x108 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x108 += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x108 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x108 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x108 += einsum(x107, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x108, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x108, (0, 1, 2, 3), (3, 2, 1, 0)) * -0.5
    x109 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x109 += einsum(v.ooov, (0, 1, 2, 3), l1, (4, 1), (0, 2, 4, 3))
    x110 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum(v.ooov, (0, 1, 2, 3), x32, (0, 4, 1, 5), (4, 2, 5, 3))
    x111 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x111 += einsum(x32, (0, 1, 2, 3), x17, (0, 4, 2, 5), (1, 4, 3, 5))
    x112 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x112 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 3, 5), (4, 0, 5, 1))
    x113 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x113 += einsum(x101, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x113 += einsum(x112, (0, 1, 2, 3), (0, 1, 2, 3))
    x114 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x114 += einsum(l2, (0, 1, 2, 3), x113, (2, 4, 1, 5), (3, 4, 0, 5))
    x115 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x115 += einsum(f.ov, (0, 1), l1, (2, 3), (0, 3, 1, 2))
    x115 += einsum(x109, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x115 += einsum(x110, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(x111, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(x114, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(l1, (0, 1), x10, (2, 3), (1, 2, 0, 3)) * 2.0
    l2new += einsum(x115, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x115, (0, 1, 2, 3), (3, 2, 1, 0))
    x116 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x116 += einsum(l1, (0, 1), v.ovvv, (2, 3, 4, 0), (1, 2, 3, 4))
    x117 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x117 += einsum(l1, (0, 1), x17, (1, 2, 3, 4), (2, 3, 0, 4))
    x118 = np.zeros((nvir, nvir), dtype=np.float64)
    x118 += einsum(l2, (0, 1, 2, 3), x62, (2, 3, 1, 4), (0, 4))
    x119 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x119 += einsum(x118, (0, 1), v.ovov, (2, 1, 3, 4), (2, 3, 4, 0)) * 0.5
    x120 = np.zeros((nocc, nocc), dtype=np.float64)
    x120 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 1, 0), (3, 4))
    x121 = np.zeros((nocc, nocc), dtype=np.float64)
    x121 += einsum(l2, (0, 1, 2, 3), x24, (3, 4, 1, 0), (2, 4))
    x122 = np.zeros((nocc, nocc), dtype=np.float64)
    x122 += einsum(x120, (0, 1), (0, 1))
    x122 += einsum(x121, (0, 1), (0, 1)) * -1.0
    x123 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x123 += einsum(v.ovov, (0, 1, 2, 3), x122, (4, 0), (2, 4, 1, 3)) * 0.5
    x124 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x124 += einsum(x116, (0, 1, 2, 3), (0, 1, 2, 3))
    x124 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x124 += einsum(x119, (0, 1, 2, 3), (1, 0, 3, 2))
    x124 += einsum(x123, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x124, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x124, (0, 1, 2, 3), (2, 3, 1, 0))
    x125 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x125 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 5, 3), (4, 0, 5, 1))
    x126 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x126 += einsum(x125, (0, 1, 2, 3), l2, (4, 2, 5, 0), (5, 1, 4, 3))
    l2new += einsum(x126, (0, 1, 2, 3), (2, 3, 0, 1)) * 3.0
    l2new += einsum(x126, (0, 1, 2, 3), (3, 2, 1, 0))
    x127 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x127 += einsum(v.ovov, (0, 1, 2, 3), x82, (4, 1), (2, 0, 4, 3))
    x128 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x128 += einsum(v.ovov, (0, 1, 2, 3), x76, (4, 2), (4, 0, 1, 3))
    x129 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x129 += einsum(x127, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x129 += einsum(x128, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    l2new += einsum(x129, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x129, (0, 1, 2, 3), (2, 3, 1, 0)) * -3.0
    x130 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x130 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x130 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -0.5
    x131 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x131 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x131 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x132 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x132 += einsum(v.ovvv, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x132 += einsum(v.ovvv, (0, 1, 2, 3), (0, 3, 1, 2))
    x133 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x133 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x133 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x133 += einsum(x130, (0, 1, 2, 3), t2, (4, 0, 5, 3), (4, 1, 5, 2)) * 2.0
    x133 += einsum(t2, (0, 1, 2, 3), x131, (1, 4, 5, 2), (0, 4, 3, 5))
    x133 += einsum(t1, (0, 1), x132, (2, 3, 1, 4), (0, 2, 4, 3)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x133, (2, 4, 0, 5), (5, 1, 4, 3))
    x134 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x134 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x134 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -2.0
    x134 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2))
    x134 += einsum(v.ovov, (0, 1, 2, 3), x1, (4, 0, 3, 5), (4, 2, 5, 1)) * 2.0
    l2new += einsum(x134, (0, 1, 2, 3), l2, (4, 2, 5, 0), (4, 3, 5, 1)) * -1.0
    x135 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x135 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x135 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2))
    x135 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 1, 5), (4, 0, 5, 3)) * -1.0
    l2new += einsum(x135, (0, 1, 2, 3), l2, (4, 2, 0, 5), (4, 3, 1, 5)) * -1.0
    x136 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x136 += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x136 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2))
    x136 += einsum(v.ovov, (0, 1, 2, 3), t2, (0, 4, 5, 3), (4, 2, 5, 1)) * -1.0
    l2new += einsum(l2, (0, 1, 2, 3), x136, (3, 4, 0, 5), (5, 1, 2, 4)) * -1.0
    x137 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x137 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1))
    x137 += einsum(t2, (0, 1, 2, 3), x131, (0, 4, 5, 2), (1, 4, 3, 5)) * -1.0
    l2new += einsum(x0, (0, 1, 2, 3), x137, (1, 4, 3, 5), (5, 2, 4, 0))
    x138 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x138 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x138 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 3.0
    x139 = np.zeros((nvir, nvir), dtype=np.float64)
    x139 += einsum(f.vv, (0, 1), (1, 0)) * 0.5
    x139 += einsum(x138, (0, 1, 2, 3), v.ovov, (0, 3, 1, 4), (4, 2)) * -0.25
    x139 += einsum(v.ovov, (0, 1, 2, 3), x52, (0, 2, 4, 3), (1, 4)) * 0.25
    x139 += einsum(x89, (0, 1), (0, 1))
    l2new += einsum(x139, (0, 1), l2, (2, 1, 3, 4), (2, 0, 3, 4)) * 2.0
    x140 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x140 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x140 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.3333333333333333
    x141 = np.zeros((nvir, nvir), dtype=np.float64)
    x141 += einsum(f.vv, (0, 1), (1, 0)) * 0.5
    x141 += einsum(v.ovov, (0, 1, 2, 3), x52, (0, 2, 4, 1), (3, 4)) * -0.25
    x141 += einsum(x140, (0, 1, 2, 3), v.ovov, (0, 4, 1, 3), (4, 2)) * -0.75
    x141 += einsum(x89, (0, 1), (0, 1))
    l2new += einsum(l2, (0, 1, 2, 3), x141, (4, 0), (4, 1, 2, 3)) * 2.0
    x142 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x142 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0))
    x142 += einsum(x21, (0, 1, 2, 3), (2, 1, 0, 3))
    x142 += einsum(x7, (0, 1, 2, 3), (0, 2, 1, 3))
    l2new += einsum(x142, (0, 1, 2, 3), l2, (4, 5, 0, 2), (4, 5, 1, 3))
    x143 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x143 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x143 += einsum(x17, (0, 1, 2, 3), (2, 0, 1, 3))
    x144 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x144 += einsum(x143, (0, 1, 2, 3), t1, (4, 3), (4, 1, 0, 2))
    l2new += einsum(x144, (0, 1, 2, 3), l2, (4, 5, 0, 1), (4, 5, 3, 2))
    x145 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x145 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3))
    x145 += einsum(x45, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new += einsum(x145, (0, 1, 2, 3), v.ovov, (2, 4, 3, 5), (4, 5, 0, 1))
    x146 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x146 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3))
    x146 += einsum(x17, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new += einsum(x25, (0, 1, 2, 3), x146, (0, 4, 2, 5), (5, 3, 4, 1)) * -1.0
    x147 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x147 += einsum(v.ooov, (0, 1, 2, 3), (1, 0, 2, 3))
    x147 += einsum(v.ooov, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    l2new += einsum(x25, (0, 1, 2, 3), x147, (0, 2, 4, 5), (5, 3, 4, 1)) * -1.0
    x148 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x148 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3))
    x148 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x149 = np.zeros((nocc, nocc), dtype=np.float64)
    x149 += einsum(f.oo, (0, 1), (1, 0))
    x149 += einsum(v.ovov, (0, 1, 2, 3), t2, (2, 4, 3, 1), (4, 0))
    x149 += einsum(t2, (0, 1, 2, 3), x148, (1, 4, 3, 2), (0, 4)) * -1.0
    x149 += einsum(x93, (0, 1), (1, 0))
    x149 += einsum(x96, (0, 1), (0, 1))
    l2new += einsum(l2, (0, 1, 2, 3), x149, (3, 4), (0, 1, 2, 4)) * -1.0
    x150 = np.zeros((nocc, nocc), dtype=np.float64)
    x150 += einsum(x66, (0, 1), (0, 1))
    x150 += einsum(x51, (0, 1), (0, 1))
    l2new += einsum(v.ovov, (0, 1, 2, 3), x150, (4, 0), (1, 3, 4, 2)) * -1.0
    x151 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x151 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x151 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 5, 1), (4, 0, 5, 3))
    l2new += einsum(x151, (0, 1, 2, 3), l2, (4, 2, 0, 5), (4, 3, 5, 1))

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
    rdm1_f_vv += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4)) * 3.0
    rdm1_f_vv += einsum(t1, (0, 1), l1, (2, 0), (2, 1)) * 2.0
    x0 = np.zeros((nocc, nocc), dtype=np.float64)
    x0 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm1_f_oo += einsum(x0, (0, 1), (1, 0)) * -2.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x1 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm1_f_oo += einsum(t2, (0, 1, 2, 3), x1, (4, 1, 3, 2), (0, 4)) * -1.0
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x2 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -0.3333333333333333
    rdm1_f_oo += einsum(x2, (0, 1, 2, 3), t2, (4, 1, 2, 3), (4, 0)) * -3.0
    x3 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x3 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    rdm1_f_ov += einsum(x3, (0, 1, 2, 3), t2, (0, 1, 4, 3), (2, 4)) * -2.0
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x5 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x5 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x5 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm1_f_ov += einsum(x5, (0, 1, 2, 3), x4, (1, 0, 4, 2), (4, 3))
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x6 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    rdm1_f_ov += einsum(x6, (0, 1, 2, 3), l1, (3, 1), (0, 2)) * 4.0
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
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 0, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 3, 0))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 3, 0))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 3, 0))
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 1, 3, 0))
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
    x1 += einsum(l2, (0, 1, 2, 3), x0, (4, 3, 1, 0), (2, 4))
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(l2, (0, 1, 2, 3), x2, (4, 2, 1, 0), (3, 4)) * 0.3333333333333333
    x4 = np.zeros((nocc, nocc), dtype=np.float64)
    x4 += einsum(x1, (0, 1), (0, 1))
    x4 += einsum(x3, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x4, (2, 3), (1, 3, 0, 2)) * -1.5
    rdm2_f_oooo += einsum(x4, (0, 1), delta.oo, (2, 3), (3, 1, 0, 2)) * 1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x4, (2, 3), (3, 0, 1, 2)) * 1.5
    rdm2_f_oooo += einsum(x4, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * -1.5
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 1, 0, 2))
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 0, 2))
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x5, (2, 3), (3, 1, 0, 2))
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (3, 1, 0, 2))
    rdm2_f_oooo += einsum(x5, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.0
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
    x8 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x8 += einsum(l2, (0, 1, 2, 3), x2, (4, 5, 1, 0), (2, 3, 4, 5)) * 0.5
    x9 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x9 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x9 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oooo += einsum(x9, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x9, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_oooo += einsum(x9, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x9, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x10 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x10 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_oooo += einsum(x10, (0, 1, 2, 3), (2, 3, 0, 1))
    rdm2_f_oooo += einsum(x10, (0, 1, 2, 3), (3, 2, 1, 0))
    x11 = np.zeros((nocc, nocc), dtype=np.float64)
    x11 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 0, 1), (3, 4))
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x12 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    x13 = np.zeros((nocc, nocc), dtype=np.float64)
    x13 += einsum(x12, (0, 1, 2, 3), t2, (4, 1, 3, 2), (0, 4))
    x14 = np.zeros((nocc, nocc), dtype=np.float64)
    x14 += einsum(x11, (0, 1), (0, 1))
    x14 += einsum(x13, (0, 1), (0, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x14, (2, 3), (1, 3, 0, 2)) * 0.5
    rdm2_f_oooo += einsum(x14, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x14, (2, 3), (1, 3, 0, 2)) * 0.5
    rdm2_f_oooo += einsum(x14, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * 0.5
    x15 = np.zeros((nocc, nocc), dtype=np.float64)
    x15 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x15, (2, 3), (0, 3, 1, 2)) * -0.5
    rdm2_f_oooo += einsum(x15, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x15, (2, 3), (0, 3, 1, 2)) * -1.5
    rdm2_f_oooo += einsum(x15, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -0.5
    x16 = np.zeros((nocc, nocc), dtype=np.float64)
    x16 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 1), (3, 4))
    x17 = np.zeros((nocc, nocc), dtype=np.float64)
    x17 += einsum(delta.oo, (0, 1), (1, 0))
    x17 += einsum(x16, (0, 1), (0, 1)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x17, (2, 3), (1, 3, 0, 2))
    x18 = np.zeros((nocc, nocc), dtype=np.float64)
    x18 += einsum(delta.oo, (0, 1), (1, 0)) * -1.0
    x18 += einsum(x16, (0, 1), (0, 1))
    rdm2_f_oooo += einsum(x18, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -1.0
    x19 = np.zeros((nocc, nocc), dtype=np.float64)
    x19 += einsum(x2, (0, 1, 2, 3), x12, (4, 1, 3, 2), (0, 4))
    x20 = np.zeros((nocc, nocc), dtype=np.float64)
    x20 += einsum(x16, (0, 1), (0, 1)) * 2.0
    x20 += einsum(x19, (0, 1), (1, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x20, (2, 3), (1, 3, 0, 2)) * -0.5
    rdm2_f_oooo += einsum(x20, (0, 1), delta.oo, (2, 3), (3, 1, 0, 2)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x20, (2, 3), (3, 0, 1, 2)) * 0.5
    rdm2_f_oooo += einsum(x20, (0, 1), delta.oo, (2, 3), (1, 2, 0, 3)) * -0.5
    x21 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x21 += einsum(t1, (0, 1), l2, (1, 2, 3, 4), (3, 4, 0, 2))
    rdm2_f_ovoo += einsum(x21, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vooo += einsum(x21, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x22 = np.zeros((nocc, nvir), dtype=np.float64)
    x22 += einsum(x21, (0, 1, 2, 3), t2, (0, 1, 4, 3), (2, 4))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x23 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x23 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x23 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x24 = np.zeros((nocc, nvir), dtype=np.float64)
    x24 += einsum(x23, (0, 1, 2, 3), x6, (0, 1, 4, 2), (4, 3)) * 0.5
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x25 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x26 = np.zeros((nocc, nvir), dtype=np.float64)
    x26 += einsum(x25, (0, 1, 2, 3), l1, (2, 1), (0, 3))
    x27 = np.zeros((nocc, nocc), dtype=np.float64)
    x27 += einsum(l2, (0, 1, 2, 3), x0, (4, 3, 1, 0), (2, 4)) * 1.5
    x28 = np.zeros((nocc, nocc), dtype=np.float64)
    x28 += einsum(l2, (0, 1, 2, 3), x2, (4, 2, 1, 0), (3, 4)) * 0.5
    x29 = np.zeros((nocc, nocc), dtype=np.float64)
    x29 += einsum(x5, (0, 1), (0, 1))
    x29 += einsum(x27, (0, 1), (0, 1))
    x29 += einsum(x28, (0, 1), (0, 1))
    x30 = np.zeros((nocc, nvir), dtype=np.float64)
    x30 += einsum(x29, (0, 1), t1, (0, 2), (1, 2))
    x31 = np.zeros((nocc, nvir), dtype=np.float64)
    x31 += einsum(x22, (0, 1), (0, 1))
    x31 += einsum(x24, (0, 1), (0, 1)) * -1.0
    x31 += einsum(x26, (0, 1), (0, 1)) * -1.0
    x31 += einsum(x30, (0, 1), (0, 1))
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x31, (2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x31, (2, 3), (2, 0, 1, 3))
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x31, (2, 3), (1, 2, 3, 0))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x31, (2, 3), (2, 0, 3, 1)) * -1.0
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum(x21, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 2, 4, 5))
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x33 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovo += einsum(x33, (0, 1, 2, 3), t2, (1, 4, 3, 5), (4, 2, 5, 0)) * -1.0
    x34 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x34 += einsum(x33, (0, 1, 2, 3), x2, (4, 1, 3, 5), (4, 0, 2, 5))
    x35 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x35 += einsum(delta.oo, (0, 1), t1, (2, 3), (1, 0, 2, 3))
    x35 += einsum(x32, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x35 += einsum(x34, (0, 1, 2, 3), (2, 1, 0, 3))
    x35 += einsum(x29, (0, 1), t1, (2, 3), (2, 0, 1, 3))
    rdm2_f_ooov += einsum(x35, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x35, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x35, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x35, (0, 1, 2, 3), (2, 0, 3, 1))
    x36 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x36 += einsum(l2, (0, 1, 2, 3), x2, (4, 5, 1, 0), (2, 3, 4, 5))
    x37 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x37 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x37 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x38 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x38 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x38 += einsum(x37, (0, 1, 2, 3), (1, 0, 2, 3))
    x39 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x39 += einsum(x38, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4)) * 0.5
    rdm2_f_ooov += einsum(x39, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x39, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x40 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 += einsum(l1, (0, 1), x40, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x41, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(x41, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(x6, (0, 1, 2, 3), t2, (4, 1, 3, 5), (0, 2, 4, 5))
    rdm2_f_ooov += einsum(x42, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x42, (0, 1, 2, 3), (1, 2, 3, 0))
    x43 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x43 += einsum(l1, (0, 1), t2, (2, 3, 0, 4), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x43, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x43, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x44 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x44 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    x44 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x45 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x45 += einsum(x44, (0, 1, 2, 3), t2, (1, 4, 3, 5), (0, 2, 4, 5))
    rdm2_f_ooov += einsum(x45, (0, 1, 2, 3), (1, 2, 0, 3))
    x46 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x46 += einsum(x21, (0, 1, 2, 3), x2, (4, 1, 5, 3), (4, 0, 2, 5))
    rdm2_f_ooov += einsum(x46, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x46, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x47 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x47 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333333
    x47 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x47 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333333
    x48 = np.zeros((nocc, nvir), dtype=np.float64)
    x48 += einsum(x6, (0, 1, 2, 3), x47, (1, 0, 3, 4), (2, 4)) * 1.5
    x49 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x49 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x49 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2))
    x49 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_voov += einsum(x49, (0, 1, 2, 3), l2, (4, 2, 5, 1), (4, 0, 5, 3))
    x50 = np.zeros((nocc, nvir), dtype=np.float64)
    x50 += einsum(x49, (0, 1, 2, 3), l1, (2, 1), (0, 3))
    x51 = np.zeros((nocc, nocc), dtype=np.float64)
    x51 += einsum(x2, (0, 1, 2, 3), x12, (4, 1, 3, 2), (0, 4)) * 0.5
    x52 = np.zeros((nocc, nocc), dtype=np.float64)
    x52 += einsum(x5, (0, 1), (0, 1))
    x52 += einsum(x16, (0, 1), (0, 1))
    x52 += einsum(x51, (0, 1), (1, 0))
    x53 = np.zeros((nocc, nvir), dtype=np.float64)
    x53 += einsum(x52, (0, 1), t1, (0, 2), (1, 2))
    x54 = np.zeros((nocc, nvir), dtype=np.float64)
    x54 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x54 += einsum(x48, (0, 1), (0, 1))
    x54 += einsum(x50, (0, 1), (0, 1)) * -1.0
    x54 += einsum(x53, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x54, (2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x54, (2, 3), (2, 1, 3, 0)) * -1.0
    x55 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x55 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3))
    x55 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x56 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x56 += einsum(t1, (0, 1), x55, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_ooov += einsum(x56, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x56, (0, 1, 2, 3), (2, 1, 3, 0))
    x57 = np.zeros((nocc, nocc), dtype=np.float64)
    x57 += einsum(l2, (0, 1, 2, 3), x0, (4, 3, 1, 0), (2, 4)) * 3.0
    x58 = np.zeros((nocc, nocc), dtype=np.float64)
    x58 += einsum(l2, (0, 1, 2, 3), x2, (4, 2, 1, 0), (3, 4))
    x59 = np.zeros((nocc, nocc), dtype=np.float64)
    x59 += einsum(x5, (0, 1), (0, 1)) * 2.0
    x59 += einsum(x57, (0, 1), (0, 1))
    x59 += einsum(x58, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(t1, (0, 1), x59, (2, 3), (3, 0, 2, 1)) * -0.5
    rdm2_f_oovo += einsum(t1, (0, 1), x59, (2, 3), (0, 3, 1, 2)) * -0.5
    x60 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x60 += einsum(x6, (0, 1, 2, 3), t2, (4, 0, 3, 5), (1, 2, 4, 5))
    rdm2_f_ooov += einsum(x60, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_oovo += einsum(x60, (0, 1, 2, 3), (2, 1, 3, 0))
    x61 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x61 += einsum(x21, (0, 1, 2, 3), t2, (0, 4, 5, 3), (1, 2, 4, 5))
    rdm2_f_ooov += einsum(x61, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x61, (0, 1, 2, 3), (1, 2, 3, 0))
    x62 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x62 += einsum(t2, (0, 1, 2, 3), l1, (3, 4), (4, 0, 1, 2))
    rdm2_f_ooov += einsum(x62, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x62, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x63 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x63 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x63 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x64 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x64 += einsum(x63, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 2, 4, 5))
    rdm2_f_ooov += einsum(x64, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x64, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x65 = np.zeros((nocc, nvir), dtype=np.float64)
    x65 += einsum(x23, (0, 1, 2, 3), x6, (0, 1, 4, 2), (4, 3)) * 0.25
    x66 = np.zeros((nocc, nvir), dtype=np.float64)
    x66 += einsum(x25, (0, 1, 2, 3), l1, (2, 1), (0, 3)) * 0.5
    x67 = np.zeros((nocc, nvir), dtype=np.float64)
    x67 += einsum(x29, (0, 1), t1, (0, 2), (1, 2)) * 0.5
    x68 = np.zeros((nocc, nvir), dtype=np.float64)
    x68 += einsum(t1, (0, 1), (0, 1)) * -0.5
    x68 += einsum(x22, (0, 1), (0, 1)) * 0.5
    x68 += einsum(x65, (0, 1), (0, 1)) * -1.0
    x68 += einsum(x66, (0, 1), (0, 1)) * -1.0
    x68 += einsum(x67, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x68, (2, 3), (1, 2, 0, 3)) * -2.0
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x68, (2, 3), (2, 1, 3, 0)) * -2.0
    x69 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x69 += einsum(t1, (0, 1), x55, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_ooov += einsum(x69, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_oovo += einsum(x69, (0, 1, 2, 3), (1, 2, 3, 0))
    x70 = np.zeros((nocc, nocc), dtype=np.float64)
    x70 += einsum(x5, (0, 1), (0, 1)) * 2.0
    x70 += einsum(x16, (0, 1), (0, 1)) * 2.0
    x70 += einsum(x19, (0, 1), (1, 0))
    rdm2_f_ooov += einsum(x70, (0, 1), t1, (2, 3), (1, 2, 0, 3)) * -0.5
    rdm2_f_oovo += einsum(x70, (0, 1), t1, (2, 3), (2, 1, 3, 0)) * -0.5
    x71 = np.zeros((nocc, nvir), dtype=np.float64)
    x71 += einsum(x48, (0, 1), (0, 1))
    x71 += einsum(x50, (0, 1), (0, 1)) * -1.0
    x71 += einsum(x53, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x71, (2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x71, (2, 3), (2, 0, 1, 3))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x71, (2, 3), (1, 2, 3, 0))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x71, (2, 3), (2, 0, 3, 1)) * -1.0
    x72 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x72 += einsum(x6, (0, 1, 2, 3), t2, (0, 4, 3, 5), (1, 2, 4, 5))
    x73 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x73 += einsum(delta.oo, (0, 1), t1, (2, 3), (1, 0, 2, 3))
    x73 += einsum(x72, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x73 += einsum(x34, (0, 1, 2, 3), (2, 1, 0, 3))
    x73 += einsum(x52, (0, 1), t1, (2, 3), (2, 0, 1, 3))
    rdm2_f_ooov += einsum(x73, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x73, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x73, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x73, (0, 1, 2, 3), (2, 0, 3, 1))
    x74 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x74 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3))
    x74 += einsum(x37, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x75 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x75 += einsum(t1, (0, 1), x74, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.5
    rdm2_f_oovo += einsum(x75, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x75, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x76 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x76 += einsum(x40, (0, 1, 2, 3), l1, (2, 4), (4, 0, 1, 3))
    rdm2_f_oovo += einsum(x76, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_oovo += einsum(x76, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x77 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x77 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x77 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3))
    x78 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(x37, (0, 1, 2, 3), x77, (0, 1, 4, 5), (2, 3, 4, 5)) * 0.25
    x79 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x79 += einsum(x2, (0, 1, 2, 3), l1, (2, 4), (4, 0, 1, 3))
    x80 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x80 += einsum(t1, (0, 1), x9, (2, 0, 3, 4), (2, 3, 4, 1))
    x81 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x81 += einsum(x79, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x81 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3))
    x82 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum(x81, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    x83 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x83 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x83 += einsum(x78, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x83 += einsum(x82, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x83, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x83, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x84 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x84 += einsum(x5, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4))
    x85 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x85 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    x85 += einsum(x34, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x86 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum(x85, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    x87 = np.zeros((nocc, nocc), dtype=np.float64)
    x87 += einsum(x57, (0, 1), (0, 1))
    x87 += einsum(x58, (0, 1), (0, 1))
    x88 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x88 += einsum(t2, (0, 1, 2, 3), x87, (1, 4), (4, 0, 2, 3)) * 0.5
    x89 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x89 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x89 += einsum(x86, (0, 1, 2, 3), (0, 1, 2, 3))
    x89 += einsum(x88, (0, 1, 2, 3), (1, 0, 2, 3))
    x89 += einsum(x31, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x89, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x89, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x89, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x89, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x90 = np.zeros((nvir, nvir), dtype=np.float64)
    x90 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x91 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x91 += einsum(x90, (0, 1), t2, (2, 3, 0, 4), (2, 3, 1, 4))
    rdm2_f_oovv += einsum(x91, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    rdm2_f_oovv += einsum(x91, (0, 1, 2, 3), (0, 1, 3, 2))
    x92 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x92 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 5, 0), (3, 4, 1, 5))
    x93 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x93 += einsum(x92, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x93, (0, 1, 2, 3), (0, 1, 3, 2)) * -3.0
    rdm2_f_oovv += einsum(x93, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x93, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.0
    x94 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x94 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 5, 1), (3, 4, 0, 5))
    x95 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x95 += einsum(t2, (0, 1, 2, 3), x94, (1, 4, 3, 5), (4, 0, 5, 2))
    x96 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x96 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 5), (2, 4, 1, 5))
    rdm2_f_ovov += einsum(x96, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x96, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x97 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(x96, (0, 1, 2, 3), x2, (4, 0, 5, 2), (1, 4, 3, 5))
    x98 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x98 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x98 += einsum(x97, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x98, (0, 1, 2, 3), (1, 0, 2, 3))
    x99 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x99 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 0, 5), (3, 4, 1, 5))
    rdm2_f_ovvo += einsum(x99, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x99, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x100 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x100 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x100 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_ovvo += einsum(x100, (0, 1, 2, 3), t2, (4, 1, 3, 5), (4, 2, 5, 0)) * -1.0
    rdm2_f_vovo += einsum(x100, (0, 1, 2, 3), t2, (4, 0, 3, 5), (2, 4, 5, 1)) * -1.0
    x101 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x101 += einsum(x100, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3))
    x102 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x103 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x103 += einsum(t2, (0, 1, 2, 3), x102, (1, 4, 2, 5), (4, 0, 5, 3))
    rdm2_f_oovv += einsum(x103, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x103, (0, 1, 2, 3), (1, 0, 3, 2))
    x104 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x104 += einsum(x99, (0, 1, 2, 3), t2, (4, 0, 5, 2), (4, 1, 5, 3))
    rdm2_f_oovv += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    rdm2_f_oovv += einsum(x104, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x104, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    rdm2_f_oovv += einsum(x104, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x105 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x105 += einsum(x90, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1))
    rdm2_f_oovv += einsum(x105, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x105, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.5
    x106 = np.zeros((nvir, nvir), dtype=np.float64)
    x106 += einsum(x23, (0, 1, 2, 3), l2, (3, 4, 1, 0), (4, 2))
    rdm2_f_oovv += einsum(x2, (0, 1, 2, 3), x106, (3, 4), (0, 1, 2, 4)) * 0.5
    x107 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x107 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x107 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x108 = np.zeros((nvir, nvir), dtype=np.float64)
    x108 += einsum(x107, (0, 1, 2, 3), l2, (4, 2, 0, 1), (4, 3))
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), x108, (3, 4), (0, 1, 4, 2)) * 0.5
    x109 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x109 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 5, 1), (3, 4, 0, 5))
    rdm2_f_ovov += einsum(x109, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x109, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x110 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x110 += einsum(t2, (0, 1, 2, 3), x109, (1, 4, 2, 5), (0, 4, 5, 3))
    rdm2_f_oovv += einsum(x110, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x110, (0, 1, 2, 3), (1, 0, 3, 2))
    x111 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x111 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    x112 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x112 += einsum(x111, (0, 1, 2, 3), (0, 1, 2, 3))
    x112 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x113 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x113 += einsum(x112, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x114 = np.zeros((nocc, nvir), dtype=np.float64)
    x114 += einsum(l1, (0, 1), t2, (2, 1, 0, 3), (2, 3))
    x115 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x115 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x115 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x116 = np.zeros((nocc, nvir), dtype=np.float64)
    x116 += einsum(x6, (0, 1, 2, 3), x115, (1, 0, 3, 4), (2, 4)) * 0.5
    x117 = np.zeros((nocc, nvir), dtype=np.float64)
    x117 += einsum(x14, (0, 1), t1, (0, 2), (1, 2)) * 0.5
    x118 = np.zeros((nocc, nvir), dtype=np.float64)
    x118 += einsum(x114, (0, 1), (0, 1)) * -1.0
    x118 += einsum(x116, (0, 1), (0, 1))
    x118 += einsum(x117, (0, 1), (0, 1))
    rdm2_f_oovv += einsum(x118, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x118, (2, 3), (2, 0, 3, 1))
    x119 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x119 += einsum(x113, (0, 1, 2, 3), (1, 0, 3, 2))
    x119 += einsum(x118, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x119, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x119, (0, 1, 2, 3), (1, 0, 3, 2))
    x120 = np.zeros((nocc, nvir), dtype=np.float64)
    x120 += einsum(t1, (0, 1), x15, (0, 2), (2, 1))
    rdm2_f_oovv += einsum(x120, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(t1, (0, 1), x120, (2, 3), (2, 0, 3, 1)) * -1.5
    rdm2_f_oovv += einsum(x120, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -1.5
    rdm2_f_oovv += einsum(t1, (0, 1), x120, (2, 3), (2, 0, 3, 1)) * -0.5
    x121 = np.zeros((nocc, nvir), dtype=np.float64)
    x121 += einsum(x6, (0, 1, 2, 3), t2, (0, 1, 3, 4), (2, 4))
    rdm2_f_oovv += einsum(x121, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -1.5
    rdm2_f_oovv += einsum(t1, (0, 1), x121, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(x121, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * -0.5
    rdm2_f_oovv += einsum(t1, (0, 1), x121, (2, 3), (2, 0, 3, 1)) * -1.5
    x122 = np.zeros((nocc, nvir), dtype=np.float64)
    x122 += einsum(t2, (0, 1, 2, 3), l1, (3, 1), (0, 2))
    rdm2_f_oovv += einsum(x122, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x122, (2, 3), (2, 0, 3, 1)) * 2.0
    rdm2_f_oovv += einsum(x122, (0, 1), t1, (2, 3), (2, 0, 3, 1)) * 2.0
    rdm2_f_oovv += einsum(t1, (0, 1), x122, (2, 3), (2, 0, 3, 1))
    x123 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x123 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 1, 5), (2, 4, 0, 5))
    x124 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x124 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 0, 5), (3, 4, 1, 5))
    rdm2_f_ovov += einsum(x124, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x124, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x124, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x124, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x125 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x125 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3))
    x125 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x125 += einsum(x115, (0, 1, 2, 3), l2, (3, 4, 5, 1), (5, 0, 4, 2))
    rdm2_f_oovv += einsum(x125, (0, 1, 2, 3), t2, (4, 0, 5, 2), (4, 1, 5, 3)) * -1.0
    x126 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x126 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3))
    x126 += einsum(x100, (0, 1, 2, 3), t2, (0, 4, 2, 5), (1, 4, 3, 5)) * -1.0
    rdm2_f_oovv += einsum(x126, (0, 1, 2, 3), t2, (4, 0, 2, 5), (4, 1, 5, 3))
    x127 = np.zeros((nvir, nvir), dtype=np.float64)
    x127 += einsum(x47, (0, 1, 2, 3), l2, (2, 4, 1, 0), (4, 3)) * 3.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x127, (3, 4), (0, 1, 2, 4)) * -0.5
    x128 = np.zeros((nvir, nvir), dtype=np.float64)
    x128 += einsum(x115, (0, 1, 2, 3), l2, (4, 3, 1, 0), (4, 2))
    x129 = np.zeros((nvir, nvir), dtype=np.float64)
    x129 += einsum(x90, (0, 1), (0, 1)) * 3.0
    x129 += einsum(x128, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x129, (2, 4), (0, 1, 4, 3)) * -0.5
    x130 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x130 += einsum(x55, (0, 1, 2, 3), t2, (0, 1, 4, 5), (2, 3, 4, 5))
    rdm2_f_oovv += einsum(x130, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x130, (0, 1, 2, 3), (1, 0, 3, 2))
    x131 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x131 += einsum(x21, (0, 1, 2, 3), x40, (4, 1, 3, 5), (4, 0, 2, 5))
    x132 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x132 += einsum(x43, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x132 += einsum(x42, (0, 1, 2, 3), (0, 2, 1, 3))
    x132 += einsum(x45, (0, 1, 2, 3), (0, 1, 2, 3))
    x132 += einsum(x131, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x132 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3))
    x133 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x133 += einsum(x132, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_oovv += einsum(x133, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x133, (0, 1, 2, 3), (1, 0, 3, 2))
    x134 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x134 += einsum(t2, (0, 1, 2, 3), x70, (1, 4), (4, 0, 2, 3)) * 0.5
    rdm2_f_oovv += einsum(x134, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x134, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x135 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x135 += einsum(t2, (0, 1, 2, 3), x59, (0, 4), (4, 1, 2, 3)) * 0.5
    rdm2_f_oovv += einsum(x135, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x135, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x136 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x136 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x136 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3))
    x136 += einsum(x60, (0, 1, 2, 3), (0, 2, 1, 3))
    x136 += einsum(x64, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x137 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x137 += einsum(x136, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_oovv += einsum(x137, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x137, (0, 1, 2, 3), (1, 0, 2, 3))
    x138 = np.zeros((nocc, nvir), dtype=np.float64)
    x138 += einsum(l1, (0, 1), t2, (1, 2, 0, 3), (2, 3))
    x139 = np.zeros((nocc, nocc), dtype=np.float64)
    x139 += einsum(x5, (0, 1), (0, 1))
    x139 += einsum(x16, (0, 1), (0, 1))
    x140 = np.zeros((nocc, nvir), dtype=np.float64)
    x140 += einsum(x139, (0, 1), t1, (0, 2), (1, 2))
    x141 = np.zeros((nocc, nvir), dtype=np.float64)
    x141 += einsum(t1, (0, 1), (0, 1))
    x141 += einsum(x138, (0, 1), (0, 1))
    x141 += einsum(x140, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(x141, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x141, (2, 3), (2, 0, 3, 1))
    x142 = np.zeros((nocc, nvir), dtype=np.float64)
    x142 += einsum(x5, (0, 1), t1, (0, 2), (1, 2))
    x143 = np.zeros((nocc, nvir), dtype=np.float64)
    x143 += einsum(x142, (0, 1), (0, 1))
    x143 += einsum(x22, (0, 1), (0, 1))
    rdm2_f_oovv += einsum(t1, (0, 1), x143, (2, 3), (2, 0, 3, 1)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), x143, (2, 3), (0, 2, 1, 3)) * -1.0
    x144 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x144 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * 2.0
    x144 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    rdm2_f_ovvo += einsum(x144, (0, 1, 2, 3), t2, (4, 1, 5, 3), (4, 2, 5, 0))
    x145 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x145 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x145 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x145 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0))
    x146 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x146 += einsum(x144, (0, 1, 2, 3), x2, (4, 1, 3, 5), (0, 4, 2, 5)) * -1.0
    x146 += einsum(x145, (0, 1, 2, 3), t2, (0, 4, 2, 5), (1, 4, 3, 5))
    rdm2_f_oovv += einsum(x146, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x147 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x147 += einsum(l2, (0, 1, 2, 3), t2, (2, 4, 1, 5), (3, 4, 0, 5))
    rdm2_f_ovvo += einsum(x147, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x147, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x148 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x148 += einsum(x107, (0, 1, 2, 3), l2, (4, 2, 5, 0), (5, 1, 4, 3))
    rdm2_f_ovvo += einsum(x148, (0, 1, 2, 3), (1, 2, 3, 0))
    x149 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x149 += einsum(x147, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x149 += einsum(x148, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x149, (1, 4, 2, 5), (4, 0, 5, 3)) * -1.0
    x150 = np.zeros((nvir, nvir), dtype=np.float64)
    x150 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 0, 4), (1, 4))
    x151 = np.zeros((nvir, nvir), dtype=np.float64)
    x151 += einsum(x90, (0, 1), (0, 1))
    x151 += einsum(x150, (0, 1), (0, 1)) * 2.0
    x151 += einsum(x128, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x151, (3, 4), (1, 0, 4, 2)) * -0.5
    x152 = np.zeros((nvir, nvir), dtype=np.float64)
    x152 += einsum(x90, (0, 1), (0, 1)) * 2.0
    x152 += einsum(x106, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(x152, (0, 1), t2, (2, 3, 0, 4), (3, 2, 4, 1)) * -0.5
    x153 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x153 += einsum(x2, (0, 1, 2, 3), x124, (1, 4, 3, 5), (4, 0, 5, 2))
    x154 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x154 += einsum(t2, (0, 1, 2, 3), x20, (1, 4), (4, 0, 2, 3)) * 0.5
    x155 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x155 += einsum(x33, (0, 1, 2, 3), x40, (4, 1, 3, 5), (4, 0, 2, 5))
    x156 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x156 += einsum(x72, (0, 1, 2, 3), (0, 1, 2, 3))
    x156 += einsum(x155, (0, 1, 2, 3), (1, 2, 0, 3))
    x157 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x157 += einsum(x156, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    x158 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x158 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x158 += einsum(x153, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x158 += einsum(x154, (0, 1, 2, 3), (1, 0, 2, 3))
    x158 += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3))
    x158 += einsum(x71, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv += einsum(x158, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x158, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x158, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x158, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x159 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x159 += einsum(x2, (0, 1, 2, 3), x150, (2, 4), (0, 1, 3, 4)) * 1.5
    rdm2_f_oovv += einsum(x159, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x159, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.6666666666666666
    x160 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x160 += einsum(l2, (0, 1, 2, 3), t2, (4, 2, 1, 5), (3, 4, 0, 5))
    x161 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x161 += einsum(x160, (0, 1, 2, 3), t2, (4, 0, 2, 5), (1, 4, 3, 5))
    x162 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x162 += einsum(t2, (0, 1, 2, 3), x147, (0, 4, 2, 5), (4, 1, 5, 3))
    x163 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x163 += einsum(x2, (0, 1, 2, 3), l2, (2, 4, 5, 1), (5, 0, 4, 3))
    x164 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x164 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3))
    x164 += einsum(x163, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x165 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x165 += einsum(x164, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x166 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x166 += einsum(x161, (0, 1, 2, 3), (0, 1, 2, 3))
    x166 += einsum(x162, (0, 1, 2, 3), (0, 1, 2, 3))
    x166 += einsum(x165, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x166, (0, 1, 2, 3), (1, 0, 2, 3))
    x167 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x167 += einsum(t2, (0, 1, 2, 3), x99, (1, 4, 2, 5), (4, 0, 5, 3))
    x168 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x168 += einsum(t2, (0, 1, 2, 3), x124, (0, 4, 2, 5), (4, 1, 5, 3))
    x169 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x169 += einsum(x2, (0, 1, 2, 3), l2, (4, 2, 5, 1), (5, 0, 4, 3))
    x170 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x170 += einsum(x160, (0, 1, 2, 3), (0, 1, 2, 3))
    x170 += einsum(x169, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x171 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x171 += einsum(x170, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x172 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x172 += einsum(x167, (0, 1, 2, 3), (0, 1, 2, 3))
    x172 += einsum(x168, (0, 1, 2, 3), (0, 1, 2, 3))
    x172 += einsum(x171, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_oovv += einsum(x172, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_oovv += einsum(x172, (0, 1, 2, 3), (1, 0, 3, 2))
    x173 = np.zeros((nvir, nvir), dtype=np.float64)
    x173 += einsum(x90, (0, 1), (0, 1))
    x173 += einsum(x128, (0, 1), (0, 1)) * -1.0
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), x173, (3, 4), (0, 1, 4, 2)) * -0.5
    x174 = np.zeros((nvir, nvir), dtype=np.float64)
    x174 += einsum(x49, (0, 1, 2, 3), l2, (3, 4, 1, 0), (4, 2))
    rdm2_f_oovv += einsum(x174, (0, 1), x2, (2, 3, 4, 0), (2, 3, 4, 1)) * 0.5
    x175 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x175 += einsum(x25, (0, 1, 2, 3), l2, (4, 2, 5, 1), (5, 0, 4, 3))
    rdm2_f_ovov += einsum(x175, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_voov += einsum(x175, (0, 1, 2, 3), (2, 1, 0, 3))
    x176 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x176 += einsum(x40, (0, 1, 2, 3), l2, (4, 2, 1, 5), (5, 0, 4, 3))
    rdm2_f_ovov += einsum(x176, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_voov += einsum(x176, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x177 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x177 += einsum(x33, (0, 1, 2, 3), t1, (1, 4), (0, 2, 4, 3))
    rdm2_f_ovov += einsum(x177, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_ovov += einsum(x177, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_vovo += einsum(x177, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_vovo += einsum(x177, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    x178 = np.zeros((nvir, nvir), dtype=np.float64)
    x178 += einsum(t1, (0, 1), l1, (2, 0), (2, 1))
    x179 = np.zeros((nvir, nvir), dtype=np.float64)
    x179 += einsum(x178, (0, 1), (0, 1)) * 2.0
    x179 += einsum(x90, (0, 1), (0, 1)) * 3.0
    x179 += einsum(x128, (0, 1), (0, 1)) * -1.0
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x179, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x179, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x179, (2, 3), (1, 2, 3, 0)) * -0.5
    rdm2_f_voov += einsum(delta.oo, (0, 1), x179, (2, 3), (2, 1, 0, 3)) * -0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x179, (2, 3), (2, 1, 3, 0)) * 0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x179, (2, 3), (2, 1, 3, 0)) * 0.5
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv += einsum(t1, (0, 1), x179, (2, 3), (0, 2, 1, 3)) * 0.5
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv += einsum(x179, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.5
    x180 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x180 += einsum(t1, (0, 1), x21, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovov += einsum(x180, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x180, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x181 = np.zeros((nvir, nvir), dtype=np.float64)
    x181 += einsum(x178, (0, 1), (0, 1)) * 2.0
    x181 += einsum(x90, (0, 1), (0, 1))
    x181 += einsum(x150, (0, 1), (0, 1)) * 2.0
    x181 += einsum(x128, (0, 1), (0, 1)) * -1.0
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x181, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x181, (2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x181, (2, 3), (1, 2, 3, 0)) * -0.5
    rdm2_f_voov += einsum(delta.oo, (0, 1), x181, (2, 3), (2, 1, 0, 3)) * -0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x181, (2, 3), (2, 1, 3, 0)) * 0.5
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x181, (2, 3), (2, 1, 3, 0)) * 0.5
    rdm2_f_ovvv += einsum(t1, (0, 1), x181, (2, 3), (0, 2, 1, 3)) * 0.5
    rdm2_f_vovv += einsum(x181, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 0.5
    x182 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x182 += einsum(t1, (0, 1), x6, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovov += einsum(x182, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_vovo += einsum(x182, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x183 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x183 += einsum(x100, (0, 1, 2, 3), x40, (4, 0, 3, 5), (4, 1, 5, 2))
    rdm2_f_ovov += einsum(x183, (0, 1, 2, 3), (0, 3, 1, 2))
    rdm2_f_vovo += einsum(x183, (0, 1, 2, 3), (3, 0, 2, 1))
    x184 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x184 += einsum(x33, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_ovvo += einsum(x184, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    rdm2_f_ovvo += einsum(x184, (0, 1, 2, 3), (1, 3, 2, 0)) * -1.0
    rdm2_f_voov += einsum(x184, (0, 1, 2, 3), (3, 1, 0, 2)) * -1.0
    rdm2_f_voov += einsum(x184, (0, 1, 2, 3), (3, 1, 0, 2)) * -1.0
    x185 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x185 += einsum(t1, (0, 1), x21, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovvo += einsum(x185, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x185, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x186 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x186 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x186 += einsum(l2, (0, 1, 2, 3), (2, 3, 1, 0))
    x186 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm2_f_ovvo += einsum(x186, (0, 1, 2, 3), t2, (4, 0, 5, 3), (4, 2, 5, 1))
    x187 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x187 += einsum(t1, (0, 1), x6, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_ovvo += einsum(x187, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    rdm2_f_voov += einsum(x187, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x188 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x188 += einsum(x100, (0, 1, 2, 3), x2, (4, 0, 3, 5), (4, 1, 5, 2))
    rdm2_f_ovvo += einsum(x188, (0, 1, 2, 3), (0, 3, 2, 1))
    rdm2_f_voov += einsum(x188, (0, 1, 2, 3), (3, 0, 1, 2))
    x189 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x189 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1))
    x189 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x189 += einsum(l2, (0, 1, 2, 3), (3, 2, 1, 0))
    x190 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x190 += einsum(x189, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5))
    rdm2_f_voov += einsum(x190, (0, 1, 2, 3), (2, 1, 0, 3))
    x191 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x191 += einsum(l2, (0, 1, 2, 3), (2, 3, 0, 1)) * -0.5
    x191 += einsum(l2, (0, 1, 2, 3), (3, 2, 0, 1))
    rdm2_f_vovo += einsum(x191, (0, 1, 2, 3), t2, (4, 0, 5, 3), (2, 4, 5, 1)) * -2.0
    x192 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x192 += einsum(l1, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_ovvv += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vovv += einsum(x192, (0, 1, 2, 3), (1, 0, 3, 2))
    x193 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x193 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x193 += einsum(t2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x194 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x194 += einsum(x193, (0, 1, 2, 3), x6, (1, 0, 4, 5), (4, 2, 3, 5)) * 0.5
    x195 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x195 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x195 += einsum(t2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x196 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x196 += einsum(x195, (0, 1, 2, 3), l2, (4, 3, 5, 1), (5, 0, 4, 2))
    x197 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x197 += einsum(x2, (0, 1, 2, 3), l2, (4, 3, 1, 5), (5, 0, 4, 2))
    x198 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x198 += einsum(x187, (0, 1, 2, 3), (0, 1, 2, 3))
    x198 += einsum(x196, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x198 += einsum(x197, (0, 1, 2, 3), (0, 1, 2, 3))
    x199 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x199 += einsum(x198, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    x200 = np.zeros((nvir, nvir), dtype=np.float64)
    x200 += einsum(x115, (0, 1, 2, 3), l2, (4, 3, 1, 0), (4, 2)) * 0.5
    x201 = np.zeros((nvir, nvir), dtype=np.float64)
    x201 += einsum(x178, (0, 1), (0, 1))
    x201 += einsum(x90, (0, 1), (0, 1)) * 1.5
    x201 += einsum(x200, (0, 1), (0, 1)) * -1.0
    x202 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x202 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    x202 += einsum(x194, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x202 += einsum(x199, (0, 1, 2, 3), (0, 2, 1, 3))
    x202 += einsum(t1, (0, 1), x201, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvv += einsum(x202, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x202, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x202, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x202, (0, 1, 2, 3), (1, 0, 3, 2))
    x203 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x203 += einsum(t2, (0, 1, 2, 3), x21, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_ovvv += einsum(x203, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x203, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x204 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x204 += einsum(t1, (0, 1), x96, (0, 2, 3, 4), (2, 3, 1, 4))
    rdm2_f_ovvv += einsum(x204, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x204, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x205 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x205 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3))
    x205 += einsum(x185, (0, 1, 2, 3), (0, 1, 2, 3))
    x205 += einsum(x190, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x206 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x206 += einsum(x205, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    rdm2_f_ovvv += einsum(x206, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x206, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x207 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x207 += einsum(t2, (0, 1, 2, 3), x6, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_ovvv += einsum(x207, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x207, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x208 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x208 += einsum(t1, (0, 1), x109, (0, 2, 3, 4), (2, 3, 1, 4))
    rdm2_f_ovvv += einsum(x208, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x208, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x209 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x209 += einsum(l1, (0, 1), t2, (1, 2, 3, 4), (2, 0, 3, 4))
    rdm2_f_ovvv += einsum(x209, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_vovv += einsum(x209, (0, 1, 2, 3), (1, 0, 2, 3))
    x210 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x210 += einsum(x147, (0, 1, 2, 3), (0, 1, 2, 3))
    x210 += einsum(x187, (0, 1, 2, 3), (0, 1, 2, 3))
    x210 += einsum(x148, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x211 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x211 += einsum(x210, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    rdm2_f_ovvv += einsum(x211, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vovv += einsum(x211, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x212 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x212 += einsum(x12, (0, 1, 2, 3), x2, (4, 1, 3, 5), (4, 0, 5, 2))
    x213 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x213 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    x213 += einsum(x187, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x213 += einsum(x212, (0, 1, 2, 3), (1, 0, 3, 2))
    x214 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x214 += einsum(x213, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    x215 = np.zeros((nvir, nvir), dtype=np.float64)
    x215 += einsum(x178, (0, 1), (0, 1))
    x215 += einsum(x90, (0, 1), (0, 1)) * 0.5
    x215 += einsum(x150, (0, 1), (0, 1))
    x215 += einsum(x200, (0, 1), (0, 1)) * -1.0
    x216 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x216 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    x216 += einsum(x194, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x216 += einsum(x214, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x216 += einsum(t1, (0, 1), x215, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvv += einsum(x216, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x216, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x216, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x216, (0, 1, 2, 3), (1, 0, 3, 2))
    x217 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x217 += einsum(x12, (0, 1, 2, 3), t1, (1, 4), (0, 4, 2, 3))
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov += einsum(x217, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    rdm2_f_vvov += einsum(x217, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x218 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x218 += einsum(l2, (0, 1, 2, 3), t1, (3, 4), (2, 0, 1, 4))
    rdm2_f_vvov += einsum(x218, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo += einsum(x218, (0, 1, 2, 3), (2, 1, 3, 0))
    x219 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x219 += einsum(l2, (0, 1, 2, 3), t1, (2, 4), (3, 0, 1, 4))
    rdm2_f_vvov += einsum(x219, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vvvo += einsum(x219, (0, 1, 2, 3), (1, 2, 3, 0))
    x220 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x220 += einsum(x12, (0, 1, 2, 3), t1, (0, 4), (1, 4, 2, 3))
    rdm2_f_vvvo += einsum(x220, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vvvo += einsum(x220, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x221 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x221 += einsum(x218, (0, 1, 2, 3), t1, (0, 4), (1, 2, 4, 3))
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(x221, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x221, (0, 1, 2, 3), (1, 0, 3, 2))
    x222 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x222 += einsum(l2, (0, 1, 2, 3), x77, (2, 3, 4, 5), (0, 1, 4, 5)) * 0.5
    x223 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x223 += einsum(x221, (0, 1, 2, 3), (0, 1, 2, 3))
    x223 += einsum(x222, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_vvvv += einsum(x223, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x223, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vvvv += einsum(x223, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x223, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x224 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x224 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 5), (0, 1, 4, 5))
    rdm2_f_vvvv += einsum(x224, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv += einsum(x224, (0, 1, 2, 3), (1, 0, 3, 2))

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

