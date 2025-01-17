# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(f.ov, (0, 1), t1, (0, 1), ())
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    e_cc += einsum(v.oovv, (0, 1, 2, 3), x0, (0, 1, 2, 3), ()) * 0.25

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(t3, (0, 1, 2, 3, 4, 5), v.oovv, (2, 1, 5, 4), (0, 3)) * 0.25
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t1new += einsum(t1, (0, 1), f.vv, (2, 1), (0, 2))
    t1new += einsum(v.ovov, (0, 1, 2, 3), t1, (2, 1), (0, 3)) * -1.0
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum(t1, (0, 1), v.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x1 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x1 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new += einsum(t2, (0, 1, 2, 3), x1, (4, 0, 1, 2), (4, 3)) * -0.5
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x2 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    t1new += einsum(v.ovvv, (0, 1, 2, 3), x2, (0, 4, 2, 3), (4, 1)) * 0.5
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum(v.oovv, (0, 1, 2, 3), t1, (1, 3), (0, 2))
    x4 = np.zeros((nocc, nvir), dtype=np.float64)
    x4 += einsum(f.ov, (0, 1), (0, 1))
    x4 += einsum(x3, (0, 1), (0, 1))
    t1new += einsum(t2, (0, 1, 2, 3), x4, (0, 2), (1, 3))
    t2new += einsum(t3, (0, 1, 2, 3, 4, 5), x4, (0, 3), (1, 2, 4, 5))
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x6 = np.zeros((nocc, nocc), dtype=np.float64)
    x6 += einsum(t1, (0, 1), v.ooov, (0, 2, 3, 1), (2, 3)) * -1.0
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 += einsum(f.oo, (0, 1), (1, 0))
    x7 += einsum(x5, (0, 1), (0, 1))
    x7 += einsum(x6, (0, 1), (0, 1))
    x7 += einsum(x2, (0, 1, 2, 3), v.oovv, (0, 4, 2, 3), (4, 1)) * 0.5
    t1new += einsum(x7, (0, 1), t1, (0, 2), (1, 2)) * -1.0
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 5, 1), (4, 0, 5, 3))
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), x9, (4, 1, 5, 3), (4, 0, 2, 5)) * -1.0
    x11 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x11 += einsum(t1, (0, 1), v.ovov, (2, 1, 3, 4), (0, 3, 2, 4))
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 0, 5, 3), (4, 1, 2, 5)) * -1.0
    x13 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum(x0, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5))
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x14 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x14 += einsum(x13, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(t1, (0, 1), x14, (2, 0, 3, 4), (2, 3, 4, 1))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x16 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3))
    x16 += einsum(x15, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x16, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x16, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x16, (0, 1, 2, 3), (1, 0, 3, 2))
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 1, 0, 5, 3, 6), (4, 2, 5, 6))
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), x0, (6, 2, 1, 4), (6, 0, 3, 5)) * -1.0
    x20 = np.zeros((nocc, nocc), dtype=np.float64)
    x20 += einsum(t1, (0, 1), x4, (2, 1), (0, 2))
    x21 = np.zeros((nocc, nocc), dtype=np.float64)
    x21 += einsum(f.oo, (0, 1), (1, 0))
    x21 += einsum(x20, (0, 1), (0, 1))
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(x21, (0, 1), t2, (1, 2, 3, 4), (0, 2, 3, 4))
    x23 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x23 += einsum(v.ooov, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(x23, (0, 1, 2, 3), x2, (1, 2, 4, 5), (0, 3, 4, 5)) * 0.5
    x25 = np.zeros((nocc, nocc), dtype=np.float64)
    x25 += einsum(t2, (0, 1, 2, 3), v.oovv, (1, 4, 2, 3), (0, 4)) * -1.0
    x26 = np.zeros((nocc, nocc), dtype=np.float64)
    x26 += einsum(x6, (0, 1), (0, 1))
    x26 += einsum(x25, (0, 1), (1, 0)) * 0.5
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), x26, (0, 4), (4, 1, 2, 3))
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(x17, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x28 += einsum(x18, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x28 += einsum(x19, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    x28 += einsum(x22, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x28 += einsum(x24, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x28 += einsum(x27, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x28, (0, 1, 2, 3), (1, 0, 2, 3))
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(t3, (0, 1, 2, 3, 4, 5), v.ovvv, (1, 6, 5, 4), (0, 2, 3, 6))
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 0, 5, 2), (4, 1, 5, 3))
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(x30, (0, 1, 2, 3), t2, (4, 1, 5, 3), (4, 0, 5, 2))
    x32 = np.zeros((nvir, nvir), dtype=np.float64)
    x32 += einsum(t1, (0, 1), v.ovvv, (0, 2, 1, 3), (2, 3)) * -1.0
    x33 = np.zeros((nvir, nvir), dtype=np.float64)
    x33 += einsum(v.oovv, (0, 1, 2, 3), t2, (0, 1, 4, 2), (4, 3)) * -1.0
    x34 = np.zeros((nvir, nvir), dtype=np.float64)
    x34 += einsum(x32, (0, 1), (0, 1))
    x34 += einsum(x33, (0, 1), (0, 1)) * 0.5
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(t2, (0, 1, 2, 3), x34, (4, 2), (0, 1, 4, 3))
    x36 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x36 += einsum(t3, (0, 1, 2, 3, 4, 5), v.oovv, (1, 6, 5, 4), (0, 2, 6, 3)) * -1.0
    x37 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x37 += einsum(x2, (0, 1, 2, 3), v.ovvv, (4, 5, 2, 3), (4, 0, 1, 5)) * 0.5
    x38 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x38 += einsum(x4, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    x39 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x39 += einsum(x36, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.5
    x39 += einsum(x37, (0, 1, 2, 3), (0, 2, 1, 3))
    x39 += einsum(x38, (0, 1, 2, 3), (2, 1, 0, 3))
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(x39, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4))
    x41 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(x29, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x41 += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x41 += einsum(x35, (0, 1, 2, 3), (1, 0, 3, 2))
    x41 += einsum(x40, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x41, (0, 1, 2, 3), (0, 1, 3, 2))
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(t2, (0, 1, 2, 3), f.vv, (4, 3), (0, 1, 4, 2))
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(x42, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x44 += einsum(x43, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x44, (0, 1, 2, 3), (0, 1, 3, 2))
    x45 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x45 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x45 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    t2new += einsum(x45, (0, 1, 2, 3), v.vvvv, (2, 3, 4, 5), (1, 0, 4, 5)) * -1.0
    x46 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x46 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x46 += einsum(v.oovv, (0, 1, 2, 3), x2, (4, 5, 2, 3), (1, 0, 5, 4)) * 0.5
    t2new += einsum(x46, (0, 1, 2, 3), x2, (0, 1, 4, 5), (2, 3, 5, 4)) * -0.5
    x47 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x47 += einsum(v.oooo, (0, 1, 2, 3), t1, (2, 4), (0, 1, 3, 4)) * -1.0
    x48 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x48 += einsum(t2, (0, 1, 2, 3), x47, (4, 5, 1, 6), (0, 4, 5, 6, 2, 3)) * -1.0
    x49 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x49 += einsum(v.vvvv, (0, 1, 2, 3), t1, (4, 2), (4, 0, 1, 3)) * -1.0
    x50 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x50 += einsum(x49, (0, 1, 2, 3), t2, (4, 5, 6, 3), (0, 4, 5, 6, 1, 2)) * -1.0
    x51 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x51 += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x51 += einsum(x50, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x51, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x52 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x52 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 3, 5, 6), (1, 0, 4, 2, 5, 6)) * -1.0
    x53 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x53 += einsum(f.ov, (0, 1), t2, (2, 3, 4, 1), (0, 2, 3, 4))
    x54 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x54 += einsum(x0, (0, 1, 2, 3), t1, (4, 3), (0, 4, 2, 1))
    x55 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x55 += einsum(t1, (0, 1), x54, (2, 3, 4, 0), (2, 3, 4, 1))
    x56 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x56 += einsum(x53, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x56 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3))
    x57 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x57 += einsum(t2, (0, 1, 2, 3), x56, (4, 5, 0, 6), (4, 5, 1, 6, 2, 3))
    x58 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x58 += einsum(x52, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x58 += einsum(x57, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x58, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x59 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x59 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 2, 5, 6), (4, 0, 1, 5, 6, 3))
    x60 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x60 += einsum(x0, (0, 1, 2, 3), t2, (4, 5, 6, 3), (0, 4, 5, 2, 1, 6))
    x61 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x61 += einsum(t1, (0, 1), x60, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x62 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x62 += einsum(x61, (0, 1, 2, 3, 4, 5), t1, (3, 6), (0, 1, 2, 4, 6, 5)) * -1.0
    x63 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x63 += einsum(x59, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x63 += einsum(x62, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x63, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x64 = np.zeros((nvir, nvir), dtype=np.float64)
    x64 += einsum(f.ov, (0, 1), t1, (0, 2), (1, 2))
    x65 = np.zeros((nvir, nvir), dtype=np.float64)
    x65 += einsum(f.vv, (0, 1), (1, 0))
    x65 += einsum(x64, (0, 1), (0, 1)) * -1.0
    x66 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x66 += einsum(t3, (0, 1, 2, 3, 4, 5), x65, (3, 6), (0, 1, 2, 6, 4, 5))
    t3new += einsum(x66, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x66, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x66, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x67 = np.zeros((nocc, nocc), dtype=np.float64)
    x67 += einsum(f.oo, (0, 1), (1, 0))
    x67 += einsum(x5, (0, 1), (0, 1))
    x68 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x68 += einsum(t3, (0, 1, 2, 3, 4, 5), x67, (0, 6), (6, 1, 2, 3, 4, 5))
    t3new += einsum(x68, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x68, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x68, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x69 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x69 += einsum(t2, (0, 1, 2, 3), x11, (4, 1, 5, 6), (4, 0, 5, 2, 3, 6))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new += einsum(x69, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x70 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x70 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 5, 6), (0, 1, 5, 4, 2, 6))
    x71 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x71 += einsum(t1, (0, 1), x70, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x72 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x72 += einsum(v.ooov, (0, 1, 2, 3), t2, (4, 5, 6, 3), (4, 5, 1, 0, 2, 6)) * -1.0
    x73 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x73 += einsum(t1, (0, 1), x72, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 1, 6))
    x74 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x74 += einsum(x73, (0, 1, 2, 3, 4, 5), t1, (2, 6), (0, 1, 3, 4, 6, 5)) * -1.0
    x75 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x75 += einsum(x9, (0, 1, 2, 3), t1, (4, 3), (0, 4, 1, 2)) * -1.0
    x76 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x76 += einsum(t2, (0, 1, 2, 3), x75, (4, 5, 1, 6), (5, 4, 0, 2, 3, 6)) * -1.0
    x77 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x77 += einsum(x74, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x77 += einsum(x76, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x78 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(t2, (0, 1, 2, 3), x9, (4, 5, 6, 3), (4, 0, 1, 5, 2, 6)) * -1.0
    x79 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x79 += einsum(t1, (0, 1), x78, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x79, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x80 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x80 += einsum(x23, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4)) * -1.0
    x81 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x81 += einsum(x80, (0, 1, 2, 3), t2, (4, 1, 5, 6), (0, 4, 2, 3, 5, 6)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new += einsum(x81, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0

    return {"t1new": t1new, "t2new": t2new, "t3new": t3new}

