# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(f.ov, (0, 1), t1, (0, 1), ())
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x0 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    e_cc += einsum(v.oovv, (0, 1, 2, 3), x0, (0, 1, 2, 3), ()) * 0.25

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(t1, (0, 1), v.ovov, (2, 1, 0, 3), (2, 3)) * -1.0
    t1new += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 0, 1, 5, 2, 3), (4, 5)) * 0.25
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t1new += einsum(f.vv, (0, 1), t1, (2, 1), (2, 0))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum(t1, (0, 1), v.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x1 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x1 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new += einsum(t2, (0, 1, 2, 3), x1, (4, 0, 1, 3), (4, 2)) * 0.5
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x2 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    t1new += einsum(v.ovvv, (0, 1, 2, 3), x2, (0, 4, 2, 3), (4, 1)) * 0.5
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum(t1, (0, 1), v.oovv, (2, 0, 3, 1), (2, 3))
    x4 = np.zeros((nocc, nvir), dtype=np.float64)
    x4 += einsum(f.ov, (0, 1), (0, 1))
    x4 += einsum(x3, (0, 1), (0, 1))
    t1new += einsum(x4, (0, 1), t2, (2, 0, 3, 1), (2, 3))
    t2new += einsum(x4, (0, 1), t3, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5))
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x6 = np.zeros((nocc, nocc), dtype=np.float64)
    x6 += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 1), (2, 3))
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 += einsum(f.oo, (0, 1), (0, 1))
    x7 += einsum(x5, (0, 1), (0, 1))
    x7 += einsum(x6, (0, 1), (0, 1))
    x7 += einsum(v.oovv, (0, 1, 2, 3), x2, (1, 4, 2, 3), (0, 4)) * -0.5
    t1new += einsum(t1, (0, 1), x7, (0, 2), (2, 1)) * -1.0
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t1, (0, 1), v.ovvv, (2, 1, 3, 4), (0, 2, 3, 4))
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 2, 5, 6))
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(x0, (0, 1, 2, 3), t3, (4, 2, 1, 5, 6, 3), (0, 4, 5, 6))
    x11 = np.zeros((nocc, nocc), dtype=np.float64)
    x11 += einsum(t1, (0, 1), x4, (2, 1), (2, 0))
    x12 = np.zeros((nocc, nocc), dtype=np.float64)
    x12 += einsum(f.oo, (0, 1), (0, 1))
    x12 += einsum(x11, (0, 1), (1, 0))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(x12, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4)) * -1.0
    x14 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x14 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(x14, (0, 1, 2, 3), x2, (1, 2, 4, 5), (0, 3, 4, 5)) * 0.5
    x16 = np.zeros((nocc, nocc), dtype=np.float64)
    x16 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 1, 2, 3), (0, 4))
    x17 = np.zeros((nocc, nocc), dtype=np.float64)
    x17 += einsum(x6, (0, 1), (0, 1))
    x17 += einsum(x16, (0, 1), (1, 0)) * 0.5
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(x17, (0, 1), t2, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    x19 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x19 += einsum(x8, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x19 += einsum(x9, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x19 += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    x19 += einsum(x13, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x19 += einsum(x15, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x19 += einsum(x18, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x19, (0, 1, 2, 3), (1, 0, 2, 3))
    x20 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x20 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(f.vv, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4))
    x22 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x22 += einsum(x20, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x22 += einsum(x21, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x22, (0, 1, 2, 3), (0, 1, 3, 2))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5))
    x24 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x25 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x25 += einsum(t2, (0, 1, 2, 3), x24, (4, 1, 5, 3), (4, 0, 2, 5)) * -1.0
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 += einsum(t1, (0, 1), v.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x27 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 1, 5, 3), (0, 4, 5, 2))
    x28 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x28 += einsum(t2, (0, 1, 2, 3), x0, (4, 1, 5, 3), (4, 0, 5, 2))
    x29 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x29 += einsum(x26, (0, 1, 2, 3), (0, 1, 2, 3))
    x29 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3))
    x29 += einsum(x28, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(t1, (0, 1), x29, (2, 0, 3, 4), (2, 3, 4, 1))
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x31 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    x31 += einsum(x30, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x31, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x31, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x31, (0, 1, 2, 3), (1, 0, 3, 2))
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 0, 6, 2, 3), (4, 5, 6, 1))
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 1, 5, 3), (0, 4, 2, 5))
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(t2, (0, 1, 2, 3), x33, (4, 1, 5, 3), (4, 0, 5, 2))
    x35 = np.zeros((nvir, nvir), dtype=np.float64)
    x35 += einsum(t1, (0, 1), v.ovvv, (0, 2, 3, 1), (2, 3))
    x36 = np.zeros((nvir, nvir), dtype=np.float64)
    x36 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 4, 3), (2, 4))
    x37 = np.zeros((nvir, nvir), dtype=np.float64)
    x37 += einsum(x35, (0, 1), (0, 1))
    x37 += einsum(x36, (0, 1), (0, 1)) * 0.5
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(x37, (0, 1), t2, (2, 3, 4, 1), (2, 3, 4, 0)) * -1.0
    x39 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x39 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 5, 1, 6, 2, 3), (4, 5, 0, 6))
    x40 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x40 += einsum(v.ovvv, (0, 1, 2, 3), x2, (4, 5, 2, 3), (0, 4, 5, 1)) * 0.5
    x41 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x41 += einsum(x4, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x42 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x42 += einsum(x39, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.5
    x42 += einsum(x40, (0, 1, 2, 3), (0, 2, 1, 3))
    x42 += einsum(x41, (0, 1, 2, 3), (2, 1, 0, 3))
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(t1, (0, 1), x42, (0, 2, 3, 4), (2, 3, 4, 1))
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x44 += einsum(x34, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x44 += einsum(x38, (0, 1, 2, 3), (1, 0, 2, 3))
    x44 += einsum(x43, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x44, (0, 1, 2, 3), (0, 1, 3, 2))
    x45 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x45 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x45 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    t2new += einsum(v.vvvv, (0, 1, 2, 3), x45, (4, 5, 2, 3), (5, 4, 0, 1)) * -1.0
    x46 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x46 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x46 += einsum(v.oovv, (0, 1, 2, 3), x2, (4, 5, 2, 3), (0, 1, 5, 4)) * -0.5
    t2new += einsum(x2, (0, 1, 2, 3), x46, (0, 1, 4, 5), (4, 5, 3, 2)) * -0.5
    x47 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x47 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 2, 3), (4, 5, 6, 0, 7, 1))
    x48 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x48 += einsum(t1, (0, 1), x47, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    t3new += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.5
    t3new += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.5
    t3new += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.5
    t3new += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * 0.5
    t3new += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * 0.5
    t3new += einsum(x48, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -0.5
    x49 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x49 += einsum(v.ovov, (0, 1, 2, 3), t3, (4, 5, 2, 6, 7, 1), (4, 5, 0, 6, 7, 3))
    x50 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x50 += einsum(v.ooov, (0, 1, 2, 3), x2, (0, 1, 4, 5), (2, 3, 4, 5))
    x51 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x51 += einsum(t2, (0, 1, 2, 3), x50, (4, 3, 5, 6), (0, 1, 4, 2, 6, 5)) * 0.5
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * 2.0
    x52 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x53 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x53 += einsum(v.ovvv, (0, 1, 2, 3), x52, (4, 5, 2, 3), (0, 4, 5, 1))
    x54 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x54 += einsum(t2, (0, 1, 2, 3), x53, (1, 4, 5, 6), (0, 5, 4, 2, 3, 6)) * 0.5
    x55 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x55 += einsum(x49, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x55 += einsum(x51, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    x55 += einsum(x54, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x55, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x56 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x56 += einsum(x24, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (0, 4, 5, 6, 7, 2)) * -1.0
    x57 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x57 += einsum(x0, (0, 1, 2, 3), x2, (1, 2, 4, 5), (0, 3, 4, 5))
    x58 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x58 += einsum(t2, (0, 1, 2, 3), x57, (4, 3, 5, 6), (0, 1, 4, 2, 6, 5)) * 0.5
    x59 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x59 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x59 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x60 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x60 += einsum(t2, (0, 1, 2, 3), x59, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6)) * -1.0
    x61 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x61 += einsum(x56, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x61 += einsum(x58, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    x61 += einsum(x60, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x61, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x62 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x62 += einsum(x35, (0, 1), t3, (2, 3, 4, 5, 6, 1), (2, 3, 4, 5, 6, 0)) * -1.0
    x63 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x63 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 2, 3), (4, 5, 6, 0, 1, 7))
    x64 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x64 += einsum(x2, (0, 1, 2, 3), x63, (4, 5, 6, 0, 1, 7), (4, 5, 6, 2, 3, 7)) * 0.25
    x65 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x65 += einsum(x62, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x65 += einsum(x64, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x65, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x65, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x65, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x66 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x66 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 4, 5, 3), (0, 2, 4, 5))
    x67 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x67 += einsum(t2, (0, 1, 2, 3), x66, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    x68 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x68 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x68 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3))
    x69 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x69 += einsum(t2, (0, 1, 2, 3), x68, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6)) * -1.0
    x70 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x70 += einsum(t1, (0, 1), x69, (2, 3, 4, 0, 5, 6), (3, 2, 4, 5, 6, 1)) * -1.0
    x71 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x71 += einsum(x67, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x71 += einsum(x70, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x71, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    x72 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x72 += einsum(t2, (0, 1, 2, 3), x24, (4, 5, 6, 3), (4, 0, 1, 5, 2, 6)) * -1.0
    x73 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x73 += einsum(t1, (0, 1), x72, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x73, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    x74 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x74 += einsum(x6, (0, 1), t3, (2, 3, 0, 4, 5, 6), (2, 3, 1, 4, 5, 6)) * -1.0
    x75 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x75 += einsum(v.oovv, (0, 1, 2, 3), x52, (4, 5, 2, 3), (4, 5, 0, 1))
    x76 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x76 += einsum(x75, (0, 1, 2, 3), t3, (4, 2, 3, 5, 6, 7), (4, 1, 0, 5, 6, 7)) * 0.25
    x77 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x77 += einsum(x74, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x77 += einsum(x76, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x77, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x78 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x78 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    x79 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x79 += einsum(x4, (0, 1), t2, (2, 0, 3, 4), (2, 3, 4, 1)) * -1.0
    x80 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x80 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x80 += einsum(x78, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x80 += einsum(x79, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x81 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x81 += einsum(t2, (0, 1, 2, 3), x80, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6)) * -1.0
    x82 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum(v.ooov, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 2, 6, 7))
    x83 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x83 += einsum(t2, (0, 1, 2, 3), x75, (4, 5, 6, 1), (0, 5, 4, 6, 2, 3)) * -0.5
    x84 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x84 += einsum(x82, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x84 += einsum(x83, (0, 1, 2, 3, 4, 5), (2, 1, 3, 0, 5, 4)) * -1.0
    x85 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x85 += einsum(t1, (0, 1), x84, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1))
    x86 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x86 += einsum(x81, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    x86 += einsum(x85, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x86, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x87 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x87 += einsum(v.oooo, (0, 1, 2, 3), t3, (4, 2, 3, 5, 6, 7), (4, 0, 1, 5, 6, 7))
    x88 = np.zeros((nocc, nocc), dtype=np.float64)
    x88 += einsum(v.oovv, (0, 1, 2, 3), x2, (1, 4, 2, 3), (4, 0)) * -1.0
    x89 = np.zeros((nocc, nocc), dtype=np.float64)
    x89 += einsum(f.oo, (0, 1), (0, 1)) * 2.0
    x89 += einsum(x5, (0, 1), (0, 1)) * 2.0
    x89 += einsum(x88, (0, 1), (1, 0))
    x90 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x90 += einsum(x89, (0, 1), t3, (2, 3, 0, 4, 5, 6), (2, 3, 1, 4, 5, 6)) * 0.5
    x91 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x91 += einsum(x87, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -0.5
    x91 += einsum(x90, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new += einsum(x91, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x92 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x92 += einsum(v.vvvv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 2, 3), (4, 5, 6, 7, 0, 1))
    x93 = np.zeros((nvir, nvir), dtype=np.float64)
    x93 += einsum(f.ov, (0, 1), t1, (0, 2), (1, 2))
    x94 = np.zeros((nvir, nvir), dtype=np.float64)
    x94 += einsum(v.oovv, (0, 1, 2, 3), x2, (0, 1, 3, 4), (4, 2)) * -1.0
    x95 = np.zeros((nvir, nvir), dtype=np.float64)
    x95 += einsum(f.vv, (0, 1), (0, 1)) * -2.0
    x95 += einsum(x93, (0, 1), (0, 1)) * 2.0
    x95 += einsum(x94, (0, 1), (1, 0))
    x96 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x96 += einsum(x95, (0, 1), t3, (2, 3, 4, 5, 6, 0), (2, 3, 4, 5, 6, 1)) * 0.5
    x97 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x97 += einsum(x92, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.5
    x97 += einsum(x96, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new += einsum(x97, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x97, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new += einsum(x97, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x98 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x98 += einsum(t1, (0, 1), v.oooo, (2, 3, 4, 0), (2, 3, 4, 1))
    x99 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x99 += einsum(t2, (0, 1, 2, 3), x98, (4, 5, 1, 6), (0, 4, 5, 6, 2, 3)) * -1.0
    x100 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x100 += einsum(t1, (0, 1), v.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x101 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x101 += einsum(t2, (0, 1, 2, 3), x100, (4, 5, 6, 3), (4, 0, 1, 2, 5, 6)) * -1.0
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    x102 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -0.99999999999999
    x103 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x103 += einsum(v.oovv, (0, 1, 2, 3), x102, (1, 4, 3, 5), (4, 0, 5, 2))
    x104 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x104 += einsum(x103, (0, 1, 2, 3), t3, (4, 5, 1, 6, 7, 3), (4, 5, 0, 6, 7, 2)) * 1.00000000000001
    x105 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x105 += einsum(x99, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x105 += einsum(x101, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    x105 += einsum(x104, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new += einsum(x105, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x106 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x106 += einsum(t2, (0, 1, 2, 3), x27, (4, 1, 5, 6), (0, 4, 5, 2, 3, 6))
    x107 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x107 += einsum(x26, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x107 += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3))
    x108 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x108 += einsum(t2, (0, 1, 2, 3), x107, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6)) * -1.0
    x109 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x109 += einsum(x106, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x109 += einsum(x108, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    t3new += einsum(x109, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x110 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x110 += einsum(x14, (0, 1, 2, 3), t3, (4, 1, 2, 5, 6, 7), (0, 4, 3, 5, 6, 7))
    t3new += einsum(x110, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * 0.5
    t3new += einsum(x110, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -0.5
    t3new += einsum(x110, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -0.5
    t3new += einsum(x110, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * 0.5
    t3new += einsum(x110, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * 0.5
    t3new += einsum(x110, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -0.5
    x111 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x111 += einsum(t1, (0, 1), x14, (2, 0, 3, 4), (2, 3, 4, 1)) * -1.0
    x112 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x112 += einsum(t2, (0, 1, 2, 3), x111, (4, 1, 5, 6), (4, 0, 5, 6, 2, 3)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new += einsum(x112, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0

    return {"t1new": t1new, "t2new": t2new, "t3new": t3new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    # L amplitudes
    l1new = np.zeros((nvir, nocc), dtype=np.float64)
    l1new += einsum(l1, (0, 1), v.ovov, (2, 0, 1, 3), (3, 2)) * -1.0
    l1new += einsum(f.ov, (0, 1), (1, 0))
    l1new += einsum(l2, (0, 1, 2, 3), v.ovvv, (3, 4, 0, 1), (4, 2)) * -0.5
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(l2, (0, 1, 2, 3), v.vvvv, (4, 5, 0, 1), (4, 5, 2, 3)) * 0.5
    l2new += einsum(v.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x0 = np.zeros((nvir, nvir), dtype=np.float64)
    x0 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 6, 1, 2), (0, 6))
    l1new += einsum(x0, (0, 1), v.ovvv, (2, 0, 3, 1), (3, 2)) * 0.08333333333333
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    x2 = np.zeros((nocc, nvir), dtype=np.float64)
    x2 += einsum(t1, (0, 1), v.oovv, (2, 0, 3, 1), (2, 3))
    l1new += einsum(x1, (0, 1), x2, (1, 2), (2, 0)) * -1.0
    l3new = np.zeros((nvir, nvir, nvir, nocc, nocc, nocc), dtype=np.float64)
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (2, 3, 1, 4, 5, 0))
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (2, 1, 3, 4, 5, 0)) * -1.0
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (1, 2, 3, 4, 5, 0))
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (2, 3, 1, 4, 0, 5)) * -1.0
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (2, 1, 3, 4, 0, 5))
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (1, 2, 3, 4, 0, 5)) * -1.0
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (2, 3, 1, 0, 4, 5))
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (2, 1, 3, 0, 4, 5)) * -1.0
    l3new += einsum(x2, (0, 1), l2, (2, 3, 4, 5), (1, 2, 3, 0, 4, 5))
    x3 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x3 += einsum(t1, (0, 1), v.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x4 += einsum(x3, (0, 1, 2, 3), (2, 1, 0, 3))
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 1, 5, 3), (0, 4, 2, 5))
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x7 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    x7 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    x8 = np.zeros((nocc, nvir), dtype=np.float64)
    x8 += einsum(f.ov, (0, 1), (0, 1))
    x8 += einsum(x2, (0, 1), (0, 1))
    x9 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x9 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 5, 2, 3), (0, 1, 4, 5))
    x10 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x10 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x10 += einsum(x3, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    x11 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x11 += einsum(t1, (0, 1), x10, (2, 3, 4, 1), (0, 2, 3, 4)) * 4.0
    x12 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x12 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x12 += einsum(x9, (0, 1, 2, 3), (3, 2, 1, 0))
    x12 += einsum(x11, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x13 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 2, 3), (4, 5, 6, 0, 1, 7))
    l2new += einsum(l3, (0, 1, 2, 3, 4, 5), x13, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7)) * 0.08333333333333
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x14 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x15 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(x13, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5)) * 0.16666666666666
    x15 += einsum(t2, (0, 1, 2, 3), x14, (4, 5, 6, 3), (0, 1, 6, 5, 4, 2))
    x16 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(v.ovvv, (0, 1, 2, 3), t3, (4, 5, 6, 7, 2, 3), (0, 4, 5, 6, 7, 1))
    x16 += einsum(x4, (0, 1, 2, 3), t3, (4, 5, 0, 6, 7, 3), (1, 4, 2, 5, 6, 7)) * -3.00000000000012
    x16 += einsum(t2, (0, 1, 2, 3), x7, (4, 5, 6, 3), (5, 0, 4, 1, 2, 6)) * -6.00000000000024
    x16 += einsum(x8, (0, 1), t3, (2, 3, 4, 5, 6, 1), (0, 2, 3, 4, 5, 6)) * -1.0
    x16 += einsum(t2, (0, 1, 2, 3), x12, (1, 4, 5, 6), (4, 0, 6, 5, 2, 3)) * -1.50000000000006
    x16 += einsum(t1, (0, 1), x15, (2, 3, 4, 0, 5, 6), (4, 3, 5, 2, 6, 1)) * 6.00000000000024
    l1new += einsum(l3, (0, 1, 2, 3, 4, 5), x16, (6, 3, 4, 5, 2, 1), (0, 6)) * -0.08333333333333
    x17 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x17 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    l2new += einsum(x17, (0, 1, 2, 3), x4, (4, 5, 0, 3), (1, 2, 5, 4)) * -0.5
    x18 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x18 += einsum(t1, (0, 1), l2, (2, 3, 4, 0), (4, 2, 3, 1))
    x18 += einsum(x17, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    l1new += einsum(v.vvvv, (0, 1, 2, 3), x18, (4, 3, 2, 1), (0, 4)) * -0.5
    x19 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x19 += einsum(t2, (0, 1, 2, 3), v.ovvv, (4, 5, 2, 3), (0, 1, 4, 5))
    x20 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x20 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 5, 1, 6, 2, 3), (4, 5, 0, 6))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x21 += einsum(x5, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x22 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x22 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x22 += einsum(x9, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x22 += einsum(x11, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x23 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x23 += einsum(v.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -2.0
    x23 += einsum(x19, (0, 1, 2, 3), (2, 1, 0, 3))
    x23 += einsum(x20, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x23 += einsum(t2, (0, 1, 2, 3), x14, (4, 1, 5, 3), (5, 0, 4, 2)) * 4.0
    x23 += einsum(x8, (0, 1), t2, (2, 3, 4, 1), (0, 2, 3, 4)) * 2.0
    x23 += einsum(t1, (0, 1), x21, (2, 3, 1, 4), (3, 2, 0, 4)) * -4.0
    x23 += einsum(t1, (0, 1), x22, (0, 2, 3, 4), (2, 4, 3, 1)) * -1.0
    l1new += einsum(l2, (0, 1, 2, 3), x23, (4, 2, 3, 1), (0, 4)) * 0.25
    x24 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x24 += einsum(t1, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x25 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x25 += einsum(t1, (0, 1), x24, (2, 3, 4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x27 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    x28 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x28 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3))
    x28 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x29 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x29 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    x30 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x30 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    x31 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x31 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x31 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3))
    x32 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x32 += einsum(t1, (0, 1), x31, (2, 3, 4, 1), (0, 2, 3, 4)) * 6.00000000000024
    x33 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x33 += einsum(x29, (0, 1, 2, 3), (1, 0, 3, 2)) * -3.00000000000012
    x33 += einsum(x30, (0, 1, 2, 3), (0, 1, 3, 2))
    x33 += einsum(x32, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x34 = np.zeros((nocc, nocc), dtype=np.float64)
    x34 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    x35 = np.zeros((nocc, nocc), dtype=np.float64)
    x35 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 0, 1, 2), (3, 6))
    x36 = np.zeros((nocc, nocc), dtype=np.float64)
    x36 += einsum(x34, (0, 1), (0, 1))
    x36 += einsum(x35, (0, 1), (0, 1)) * 0.16666666666666
    x37 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x37 += einsum(l1, (0, 1), t2, (2, 3, 4, 0), (1, 2, 3, 4)) * 2.0
    x37 += einsum(l2, (0, 1, 2, 3), t3, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6))
    x37 += einsum(t3, (0, 1, 2, 3, 4, 5), x24, (6, 1, 2, 7, 5, 4), (6, 0, 7, 3)) * -1.0
    x37 += einsum(t2, (0, 1, 2, 3), x17, (4, 3, 2, 5), (4, 0, 1, 5)) * -0.5
    x37 += einsum(t2, (0, 1, 2, 3), x25, (4, 0, 1, 5, 6, 3), (4, 6, 5, 2)) * -1.0
    x37 += einsum(t2, (0, 1, 2, 3), x28, (4, 1, 5, 3), (4, 0, 5, 2)) * 4.0
    x37 += einsum(t1, (0, 1), x33, (0, 2, 3, 4), (2, 4, 3, 1)) * -0.33333333333332
    x37 += einsum(t1, (0, 1), x36, (2, 3), (2, 0, 3, 1)) * 2.0
    l1new += einsum(v.oovv, (0, 1, 2, 3), x37, (4, 0, 1, 3), (2, 4)) * 0.25
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(t2, (0, 1, 2, 3), x24, (4, 1, 0, 5, 3, 6), (4, 5, 6, 2)) * -1.0
    x39 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x39 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x39 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x40 += einsum(t1, (0, 1), x39, (0, 2, 3, 4), (2, 3, 4, 1)) * -2.0
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x40, (4, 0, 1, 3), (2, 4)) * 0.5
    x41 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x43 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3))
    l1new += einsum(v.ovvv, (0, 1, 2, 3), x43, (4, 0, 1, 3), (2, 4)) * -0.25
    x44 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x44 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.0
    x44 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3))
    l1new += einsum(v.ovov, (0, 1, 2, 3), x44, (0, 4, 2, 3), (1, 4)) * 0.5
    x45 = np.zeros((nocc, nocc), dtype=np.float64)
    x45 += einsum(x1, (0, 1), (0, 1)) * 12.00000000000048
    x45 += einsum(x34, (0, 1), (0, 1)) * 6.00000000000024
    x45 += einsum(x35, (0, 1), (0, 1))
    l1new += einsum(x45, (0, 1), v.ooov, (2, 1, 0, 3), (3, 2)) * 0.08333333333333
    x46 = np.zeros((nocc, nvir), dtype=np.float64)
    x46 += einsum(t1, (0, 1), (0, 1)) * -1.0
    x46 += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3)) * -1.0
    x46 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 0, 1), (4, 5)) * -0.25
    x46 += einsum(t3, (0, 1, 2, 3, 4, 5), x24, (2, 0, 1, 6, 5, 4), (6, 3)) * -0.08333333333333
    x46 += einsum(t2, (0, 1, 2, 3), x39, (0, 1, 4, 3), (4, 2)) * -0.5
    x46 += einsum(t1, (0, 1), x45, (0, 2), (2, 1)) * 0.08333333333333
    l1new += einsum(x46, (0, 1), v.oovv, (2, 0, 3, 1), (3, 2)) * -1.0
    x47 = np.zeros((nvir, nvir), dtype=np.float64)
    x47 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x48 = np.zeros((nvir, nvir), dtype=np.float64)
    x48 += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    x48 += einsum(x47, (0, 1), (0, 1)) * 0.5
    l1new += einsum(x48, (0, 1), v.ovvv, (2, 0, 3, 1), (3, 2))
    x49 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x49 += einsum(x29, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.00000000000012
    x49 += einsum(x30, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l1new += einsum(v.ooov, (0, 1, 2, 3), x49, (2, 4, 0, 1), (3, 4)) * 0.08333333333333
    x50 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x50 += einsum(t1, (0, 1), x31, (2, 3, 4, 1), (3, 2, 4, 0))
    l1new += einsum(v.ooov, (0, 1, 2, 3), x50, (4, 2, 0, 1), (3, 4)) * -0.5
    x51 = np.zeros((nvir, nvir), dtype=np.float64)
    x51 += einsum(t1, (0, 1), v.ovvv, (0, 2, 3, 1), (2, 3))
    x52 = np.zeros((nvir, nvir), dtype=np.float64)
    x52 += einsum(f.vv, (0, 1), (0, 1))
    x52 += einsum(x51, (0, 1), (0, 1)) * -1.0
    l1new += einsum(l1, (0, 1), x52, (0, 2), (2, 1))
    x53 = np.zeros((nocc, nocc), dtype=np.float64)
    x53 += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 1), (2, 3))
    x54 = np.zeros((nocc, nocc), dtype=np.float64)
    x54 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 1, 2, 3), (0, 4))
    x55 = np.zeros((nocc, nocc), dtype=np.float64)
    x55 += einsum(f.oo, (0, 1), (0, 1))
    x55 += einsum(x53, (0, 1), (1, 0))
    x55 += einsum(x54, (0, 1), (0, 1)) * 0.5
    x55 += einsum(t1, (0, 1), x8, (2, 1), (0, 2))
    l1new += einsum(l1, (0, 1), x55, (1, 2), (0, 2)) * -1.0
    x56 = np.zeros((nocc, nocc), dtype=np.float64)
    x56 += einsum(x1, (0, 1), (0, 1))
    x56 += einsum(x34, (0, 1), (0, 1)) * 0.5
    x56 += einsum(x35, (0, 1), (0, 1)) * 0.08333333333333
    l1new += einsum(f.ov, (0, 1), x56, (2, 0), (1, 2)) * -1.0
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(f.oo, (0, 1), l2, (2, 3, 4, 1), (0, 4, 2, 3))
    x58 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x58 += einsum(l1, (0, 1), v.ovvv, (2, 0, 3, 4), (1, 2, 3, 4))
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(x57, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(x59, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x59, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x60 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x60 += einsum(f.vv, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x61 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x61 += einsum(t1, (0, 1), v.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x62 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x62 += einsum(t2, (0, 1, 2, 3), v.ovvv, (1, 4, 5, 3), (0, 2, 4, 5))
    x63 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x63 += einsum(v.oovv, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2))
    x64 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x64 += einsum(t2, (0, 1, 2, 3), x4, (0, 1, 4, 5), (4, 2, 3, 5)) * 0.5
    x65 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x65 += einsum(v.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x65 += einsum(x61, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x65 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x65 += einsum(x63, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.49999999999998
    x65 += einsum(x64, (0, 1, 2, 3), (0, 2, 1, 3))
    x66 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x66 += einsum(x65, (0, 1, 2, 3), l3, (4, 1, 2, 5, 6, 0), (5, 6, 4, 3)) * -0.5
    x67 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x67 += einsum(t1, (0, 1), v.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x68 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x68 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x68 += einsum(x67, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x68 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    x69 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x69 += einsum(x68, (0, 1, 2, 3), x24, (4, 5, 0, 1, 2, 6), (4, 5, 6, 3))
    x70 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x70 += einsum(t1, (0, 1), x3, (2, 3, 0, 4), (2, 3, 1, 4))
    x71 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x71 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    x71 += einsum(x70, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x72 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x72 += einsum(x71, (0, 1, 2, 3), x24, (4, 5, 0, 1, 2, 6), (4, 5, 6, 3))
    x73 = np.zeros((nvir, nvir), dtype=np.float64)
    x73 += einsum(x47, (0, 1), (0, 1))
    x73 += einsum(x0, (0, 1), (0, 1)) * 0.16666666666666
    x74 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x74 += einsum(x73, (0, 1), v.oovv, (2, 3, 4, 1), (2, 3, 4, 0)) * -0.5
    x75 = np.zeros((nvir, nvir), dtype=np.float64)
    x75 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 4, 3), (2, 4))
    x76 = np.zeros((nvir, nvir), dtype=np.float64)
    x76 += einsum(x51, (0, 1), (0, 1))
    x76 += einsum(x75, (0, 1), (0, 1)) * 0.5
    x77 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x77 += einsum(x76, (0, 1), l2, (2, 0, 3, 4), (3, 4, 2, 1)) * -1.0
    x78 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x78 += einsum(l1, (0, 1), x14, (1, 2, 3, 4), (2, 3, 0, 4))
    x79 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x79 += einsum(f.ov, (0, 1), x39, (2, 3, 0, 4), (2, 3, 4, 1))
    x80 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x80 += einsum(x2, (0, 1), x39, (2, 3, 0, 4), (2, 3, 4, 1))
    x81 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x81 += einsum(x60, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x81 += einsum(x66, (0, 1, 2, 3), (0, 1, 2, 3))
    x81 += einsum(x69, (0, 1, 2, 3), (0, 1, 2, 3))
    x81 += einsum(x72, (0, 1, 2, 3), (0, 1, 2, 3))
    x81 += einsum(x74, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x81 += einsum(x77, (0, 1, 2, 3), (1, 0, 2, 3))
    x81 += einsum(x78, (0, 1, 2, 3), (1, 0, 2, 3))
    x81 += einsum(x79, (0, 1, 2, 3), (1, 0, 3, 2))
    x81 += einsum(x80, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    l2new += einsum(x81, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l2new += einsum(x81, (0, 1, 2, 3), (3, 2, 0, 1))
    x82 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x82 += einsum(x26, (0, 1, 2, 3), x3, (0, 4, 2, 5), (1, 4, 3, 5)) * -1.0
    x83 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x83 += einsum(v.ovvv, (0, 1, 2, 3), x17, (4, 5, 1, 3), (4, 0, 5, 2))
    x84 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x84 += einsum(t1, (0, 1), x27, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    x85 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x85 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x85 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.49999999999998
    x85 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x85 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3))
    x86 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x86 += einsum(v.oovv, (0, 1, 2, 3), x85, (4, 1, 5, 3), (0, 4, 2, 5)) * 0.5
    x87 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x87 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x87 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    x88 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x88 += einsum(l2, (0, 1, 2, 3), x87, (3, 4, 1, 5), (2, 4, 0, 5))
    x89 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x89 += einsum(v.ooov, (0, 1, 2, 3), x28, (4, 2, 1, 5), (0, 4, 3, 5)) * -1.0
    x90 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x90 += einsum(f.ov, (0, 1), l1, (2, 3), (0, 3, 1, 2))
    x90 += einsum(l1, (0, 1), x2, (2, 3), (1, 2, 0, 3))
    x90 += einsum(x82, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x90 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x90 += einsum(x86, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x90 += einsum(x88, (0, 1, 2, 3), (0, 1, 2, 3))
    x90 += einsum(x89, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new += einsum(x90, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x90, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x90, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new += einsum(x90, (0, 1, 2, 3), (3, 2, 1, 0))
    x91 = np.zeros((nocc, nocc), dtype=np.float64)
    x91 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x92 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x92 += einsum(x91, (0, 1), l2, (2, 3, 4, 1), (0, 4, 2, 3))
    x93 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x93 += einsum(f.ov, (0, 1), t2, (2, 3, 4, 1), (0, 2, 3, 4))
    x94 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x94 += einsum(x93, (0, 1, 2, 3), l3, (4, 5, 3, 6, 1, 2), (0, 6, 4, 5)) * -1.0
    x95 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x95 += einsum(x2, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x96 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x96 += einsum(t2, (0, 1, 2, 3), x14, (4, 1, 5, 3), (0, 4, 5, 2)) * 2.0
    x97 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x97 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x97 += einsum(x5, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.5
    x98 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x98 += einsum(t1, (0, 1), x97, (2, 3, 4, 1), (0, 2, 3, 4)) * 2.0
    x99 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x99 += einsum(t1, (0, 1), x12, (0, 2, 3, 4), (2, 3, 4, 1)) * 0.5
    x100 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x100 += einsum(v.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x100 += einsum(x19, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x100 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999998
    x100 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x100 += einsum(x96, (0, 1, 2, 3), (0, 1, 2, 3))
    x100 += einsum(x98, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x100 += einsum(x99, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x101 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x101 += einsum(x100, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (6, 2, 4, 5)) * -0.5
    x102 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x102 += einsum(x45, (0, 1), v.oovv, (2, 1, 3, 4), (2, 0, 3, 4)) * -0.08333333333333
    x103 = np.zeros((nocc, nocc), dtype=np.float64)
    x103 += einsum(t1, (0, 1), x2, (2, 1), (0, 2))
    x104 = np.zeros((nocc, nocc), dtype=np.float64)
    x104 += einsum(x53, (0, 1), (0, 1))
    x104 += einsum(x54, (0, 1), (1, 0)) * 0.5
    x104 += einsum(x103, (0, 1), (1, 0))
    x105 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x105 += einsum(x104, (0, 1), l2, (2, 3, 4, 1), (4, 0, 2, 3)) * -1.0
    x106 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x106 += einsum(x92, (0, 1, 2, 3), (0, 1, 3, 2))
    x106 += einsum(x94, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    x106 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    x106 += einsum(x102, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x106 += einsum(x105, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new += einsum(x106, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x106, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x107 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x107 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x107 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new += einsum(v.ovvv, (0, 1, 2, 3), x107, (4, 5, 0, 1), (2, 3, 4, 5)) * -0.5
    x108 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x108 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x108 += einsum(x9, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x108 += einsum(t1, (0, 1), x10, (2, 3, 4, 1), (4, 0, 3, 2)) * -2.0
    l2new += einsum(l2, (0, 1, 2, 3), x108, (2, 3, 4, 5), (0, 1, 4, 5)) * 0.5
    x109 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x109 += einsum(x29, (0, 1, 2, 3), (1, 0, 3, 2)) * 3.00000000000012
    x109 += einsum(x30, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x109 += einsum(x32, (0, 1, 2, 3), (2, 1, 3, 0))
    l2new += einsum(v.oovv, (0, 1, 2, 3), x109, (4, 5, 0, 1), (2, 3, 5, 4)) * -0.08333333333333
    x110 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x110 += einsum(f.vv, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x111 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x111 += einsum(f.ov, (0, 1), x24, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x112 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x112 += einsum(v.vvvv, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 7), (5, 6, 7, 4, 0, 1))
    x113 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x113 += einsum(v.ovvv, (0, 1, 2, 3), x24, (4, 5, 6, 0, 7, 1), (4, 5, 6, 7, 2, 3)) * -1.0
    x114 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x114 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x115 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x115 += einsum(x114, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x115 += einsum(x25, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x116 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x116 += einsum(v.oovv, (0, 1, 2, 3), x115, (4, 5, 6, 0, 1, 7), (4, 5, 6, 2, 3, 7)) * 0.25
    x117 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x117 += einsum(x110, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x117 += einsum(x111, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x117 += einsum(x112, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.5
    x117 += einsum(x113, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x117 += einsum(x116, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    l3new += einsum(x117, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new += einsum(x117, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new += einsum(x117, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    x118 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x118 += einsum(x2, (0, 1), x24, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1))
    x119 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x119 += einsum(x76, (0, 1), l3, (2, 3, 0, 4, 5, 6), (4, 5, 6, 2, 3, 1))
    x120 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x120 += einsum(x118, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x120 += einsum(x119, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    l3new += einsum(x120, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new += einsum(x120, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new += einsum(x120, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    x121 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x121 += einsum(v.ooov, (0, 1, 2, 3), x24, (4, 2, 5, 1, 6, 7), (4, 5, 0, 6, 7, 3)) * -1.0
    x122 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x122 += einsum(x3, (0, 1, 2, 3), x24, (0, 4, 5, 2, 6, 7), (5, 4, 1, 6, 7, 3)) * -1.0
    x123 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x123 += einsum(v.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x123 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    x123 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x124 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x124 += einsum(x123, (0, 1, 2, 3), l3, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3))
    x125 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x125 += einsum(x121, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x125 += einsum(x122, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x125 += einsum(x124, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2))
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.0
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -1.0
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0))
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0
    l3new += einsum(x125, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0)) * -1.0
    x126 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x126 += einsum(v.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x126 += einsum(x9, (0, 1, 2, 3), (1, 0, 3, 2))
    x126 += einsum(x11, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x127 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x127 += einsum(x126, (0, 1, 2, 3), l3, (4, 5, 6, 7, 0, 1), (7, 2, 3, 4, 5, 6)) * -0.25
    x128 = np.zeros((nocc, nocc), dtype=np.float64)
    x128 += einsum(f.oo, (0, 1), (0, 1))
    x128 += einsum(x91, (0, 1), (1, 0))
    x129 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x129 += einsum(x128, (0, 1), l3, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4))
    x130 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x130 += einsum(x127, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x130 += einsum(x129, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3))
    l3new += einsum(x130, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * -1.0
    l3new += einsum(x130, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2))
    l3new += einsum(x130, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    x131 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x131 += einsum(l2, (0, 1, 2, 3), v.ovvv, (4, 1, 5, 6), (2, 3, 4, 0, 5, 6))
    x132 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x132 += einsum(v.oovv, (0, 1, 2, 3), x27, (4, 5, 1, 6), (5, 4, 0, 6, 2, 3))
    x133 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x133 += einsum(x131, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x133 += einsum(x132, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.5
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2))
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2)) * -1.0
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0))
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0))
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    l3new += einsum(x133, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * -1.0
    x134 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x134 += einsum(x104, (0, 1), l3, (2, 3, 4, 5, 6, 1), (5, 6, 0, 2, 3, 4))
    l3new += einsum(x134, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new += einsum(x134, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new += einsum(x134, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    x135 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x135 += einsum(l2, (0, 1, 2, 3), v.ooov, (4, 5, 3, 6), (2, 4, 5, 0, 1, 6))
    x136 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x136 += einsum(v.oovv, (0, 1, 2, 3), x17, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x137 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x137 += einsum(x135, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    x137 += einsum(x136, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 0.5
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * -1.0
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2)) * -1.0
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * -1.0
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2))
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new += einsum(x137, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    x138 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x138 += einsum(f.ov, (0, 1), l2, (2, 3, 4, 5), (0, 4, 5, 1, 2, 3))
    x138 += einsum(l1, (0, 1), v.oovv, (2, 3, 4, 5), (1, 2, 3, 0, 4, 5))
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2))
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2)) * -1.0
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -1.0
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2))
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -1.0
    l3new += einsum(x138, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    x139 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x139 += einsum(l2, (0, 1, 2, 3), x3, (3, 4, 5, 6), (2, 5, 4, 0, 1, 6)) * -1.0
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -1.0
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1)) * -1.0
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1))
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1))
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 0, 1))
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 0, 1)) * -1.0
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -1.0
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0
    l3new += einsum(x139, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0))
    x140 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x140 += einsum(v.oovv, (0, 1, 2, 3), x26, (4, 5, 1, 6), (4, 5, 0, 6, 2, 3))
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 0, 2))
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.0
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * -1.0
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0))
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0)) * -1.0
    l3new += einsum(x140, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0

    return {"l1new": l1new, "l2new": l2new, "l3new": l3new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM1
    rdm1_f_oo = np.zeros((nocc, nocc), dtype=np.float64)
    rdm1_f_oo += einsum(delta.oo, (0, 1), (0, 1))
    rdm1_f_ov = np.zeros((nocc, nvir), dtype=np.float64)
    rdm1_f_ov += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3))
    rdm1_f_ov += einsum(t1, (0, 1), (0, 1))
    rdm1_f_ov += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 0, 1), (4, 5)) * 0.25
    rdm1_f_vo = np.zeros((nvir, nocc), dtype=np.float64)
    rdm1_f_vo += einsum(l1, (0, 1), (0, 1))
    rdm1_f_vv = np.zeros((nvir, nvir), dtype=np.float64)
    rdm1_f_vv += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4)) * 0.5
    rdm1_f_vv += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    rdm1_f_vv += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 6, 1, 2), (0, 6)) * 0.08333333333333
    x0 = np.zeros((nocc, nocc), dtype=np.float64)
    x0 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm1_f_oo += einsum(x0, (0, 1), (1, 0)) * -1.0
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    rdm1_f_oo += einsum(x1, (0, 1), (1, 0)) * -0.5
    x2 = np.zeros((nocc, nocc), dtype=np.float64)
    x2 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 0, 1, 2), (3, 6))
    rdm1_f_oo += einsum(x2, (0, 1), (1, 0)) * -0.08333333333333
    x3 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(t1, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    rdm1_f_ov += einsum(t3, (0, 1, 2, 3, 4, 5), x3, (0, 1, 2, 6, 5, 4), (6, 3)) * 0.08333333333333
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x4 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4)) * 0.5
    rdm1_f_ov += einsum(t2, (0, 1, 2, 3), x4, (0, 1, 4, 3), (4, 2)) * 0.5
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(x0, (0, 1), (0, 1)) * 12.00000000000048
    x5 += einsum(x1, (0, 1), (0, 1)) * 6.00000000000024
    x5 += einsum(x2, (0, 1), (0, 1))
    rdm1_f_ov += einsum(t1, (0, 1), x5, (0, 2), (2, 1)) * -0.08333333333333

    rdm1_f = np.block([[rdm1_f_oo, rdm1_f_ov], [rdm1_f_vo, rdm1_f_vv]])

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM2
    rdm2_f_oooo = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (0, 2, 1, 3))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovoo += einsum(delta.oo, (0, 1), l1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_vooo += einsum(delta.oo, (0, 1), l1, (2, 3), (2, 0, 3, 1))
    rdm2_f_oovv = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(l1, (0, 1), t3, (2, 3, 1, 4, 5, 0), (2, 3, 4, 5))
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovv += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_ovov += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_ovvo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_ovvo += einsum(l1, (0, 1), t1, (2, 3), (2, 0, 3, 1))
    rdm2_f_voov = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_voov += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 1, 3))
    rdm2_f_vovo = np.zeros((nvir, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_vovo += einsum(l1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_vvoo = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 5), (0, 1, 4, 5)) * 0.5
    rdm2_f_vvvv += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7)) * 0.16666666666667
    x0 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x0 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    rdm2_f_oooo += einsum(x0, (0, 1, 2, 3), (2, 3, 1, 0)) * -0.16666666666667
    x1 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x1 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_oooo += einsum(x1, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.5
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(t1, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_ovoo += einsum(x2, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    rdm2_f_vooo += einsum(x2, (0, 1, 2, 3), (3, 2, 1, 0))
    x3 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x3 += einsum(t1, (0, 1), x2, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_oooo += einsum(x3, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    x4 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x4 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    rdm2_f_ovoo += einsum(x4, (0, 1, 2, 3), (2, 3, 1, 0)) * -0.5
    rdm2_f_vooo += einsum(x4, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.5
    x5 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x5 += einsum(t1, (0, 1), x4, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_oooo += einsum(x5, (0, 1, 2, 3), (2, 3, 1, 0)) * -0.5
    rdm2_f_oooo += einsum(x5, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.5
    x6 = np.zeros((nocc, nocc), dtype=np.float64)
    x6 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 0, 1), (2, 4))
    x7 = np.zeros((nocc, nocc), dtype=np.float64)
    x7 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 0, 1, 2), (3, 6))
    x8 = np.zeros((nocc, nocc), dtype=np.float64)
    x8 += einsum(x6, (0, 1), (0, 1))
    x8 += einsum(x7, (0, 1), (0, 1)) * 0.16666666666666
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (0, 3, 1, 2)) * -0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (0, 3, 2, 1)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (3, 0, 1, 2)) * 0.5
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x8, (2, 3), (3, 0, 2, 1)) * -0.5
    x9 = np.zeros((nocc, nocc), dtype=np.float64)
    x9 += einsum(l1, (0, 1), t1, (2, 0), (1, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x9, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x9, (2, 3), (3, 0, 1, 2))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x9, (2, 3), (0, 3, 2, 1))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), x9, (2, 3), (3, 0, 2, 1)) * -1.0
    x10 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x10 += einsum(l2, (0, 1, 2, 3), t3, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6))
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_ooov += einsum(x10, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_oovo += einsum(x10, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.5
    x11 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x11 += einsum(t2, (0, 1, 2, 3), l3, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvov += einsum(x11, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_vvvo += einsum(x11, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.5
    x12 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x12 += einsum(t2, (0, 1, 2, 3), x11, (4, 2, 3, 5), (4, 0, 1, 5))
    rdm2_f_ooov += einsum(x12, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.25
    rdm2_f_oovo += einsum(x12, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.25
    x13 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(t1, (0, 1), l3, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x14 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(t1, (0, 1), x13, (2, 3, 4, 5, 1, 6), (3, 4, 2, 5, 0, 6))
    x15 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(t2, (0, 1, 2, 3), x14, (1, 0, 4, 5, 6, 3), (4, 6, 5, 2))
    rdm2_f_ooov += einsum(x15, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_oovo += einsum(x15, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.5
    x16 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x16 += einsum(l1, (0, 1), t2, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_ooov += einsum(x16, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x16, (0, 1, 2, 3), (2, 1, 3, 0))
    x17 = np.zeros((nocc, nvir), dtype=np.float64)
    x17 += einsum(l1, (0, 1), t2, (2, 1, 3, 0), (2, 3))
    x18 = np.zeros((nocc, nvir), dtype=np.float64)
    x18 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 0, 1), (4, 5))
    x19 = np.zeros((nocc, nvir), dtype=np.float64)
    x19 += einsum(t3, (0, 1, 2, 3, 4, 5), x13, (1, 2, 0, 6, 5, 4), (6, 3)) * -1.0
    x20 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x20 += einsum(x2, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x20 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x21 = np.zeros((nocc, nvir), dtype=np.float64)
    x21 += einsum(t2, (0, 1, 2, 3), x20, (0, 1, 4, 3), (4, 2)) * -0.5
    x22 = np.zeros((nocc, nocc), dtype=np.float64)
    x22 += einsum(x9, (0, 1), (0, 1)) * 12.00000000000048
    x22 += einsum(x6, (0, 1), (0, 1)) * 6.00000000000024
    x22 += einsum(x7, (0, 1), (0, 1))
    x23 = np.zeros((nocc, nvir), dtype=np.float64)
    x23 += einsum(t1, (0, 1), x22, (0, 2), (2, 1)) * 0.08333333333333
    x24 = np.zeros((nocc, nvir), dtype=np.float64)
    x24 += einsum(x17, (0, 1), (0, 1)) * -1.0
    x24 += einsum(x18, (0, 1), (0, 1)) * -0.25
    x24 += einsum(x19, (0, 1), (0, 1)) * 0.08333333333333
    x24 += einsum(x21, (0, 1), (0, 1))
    x24 += einsum(x23, (0, 1), (0, 1))
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x24, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_ooov += einsum(delta.oo, (0, 1), x24, (2, 3), (2, 0, 1, 3))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x24, (2, 3), (0, 2, 3, 1))
    rdm2_f_oovo += einsum(delta.oo, (0, 1), x24, (2, 3), (2, 0, 3, 1)) * -1.0
    x25 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x25 += einsum(t3, (0, 1, 2, 3, 4, 5), x13, (1, 2, 6, 7, 4, 5), (6, 7, 0, 3))
    x26 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x26 += einsum(t1, (0, 1), x5, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    x27 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x27 += einsum(t2, (0, 1, 2, 3), x20, (1, 4, 5, 3), (4, 5, 0, 2))
    x28 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x28 += einsum(delta.oo, (0, 1), t1, (2, 3), (0, 1, 2, 3))
    x28 += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.25
    x28 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x28 += einsum(x27, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x28 += einsum(t1, (0, 1), x22, (2, 3), (0, 2, 3, 1)) * 0.08333333333333
    rdm2_f_ooov += einsum(x28, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_ooov += einsum(x28, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_oovo += einsum(x28, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_oovo += einsum(x28, (0, 1, 2, 3), (2, 0, 3, 1))
    x29 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x29 += einsum(x1, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x29 += einsum(x3, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x29 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.33333333333334
    x30 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x30 += einsum(t1, (0, 1), x29, (0, 2, 3, 4), (2, 3, 4, 1)) * 0.5
    rdm2_f_ooov += einsum(x30, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_oovo += einsum(x30, (0, 1, 2, 3), (2, 1, 3, 0))
    x31 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x31 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    rdm2_f_ovov += einsum(x31, (0, 1, 2, 3), (1, 2, 0, 3)) * -0.25
    rdm2_f_ovvo += einsum(x31, (0, 1, 2, 3), (1, 2, 3, 0)) * 0.25
    rdm2_f_voov += einsum(x31, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.25
    rdm2_f_vovo += einsum(x31, (0, 1, 2, 3), (2, 1, 3, 0)) * -0.25
    x32 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x32 += einsum(t2, (0, 1, 2, 3), x31, (1, 4, 3, 5), (0, 4, 2, 5))
    x33 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x33 += einsum(t2, (0, 1, 2, 3), x13, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    rdm2_f_ovov += einsum(x33, (0, 1, 2, 3), (1, 2, 0, 3)) * 0.5
    rdm2_f_ovvo += einsum(x33, (0, 1, 2, 3), (1, 2, 3, 0)) * -0.5
    rdm2_f_voov += einsum(x33, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.5
    rdm2_f_vovo += einsum(x33, (0, 1, 2, 3), (2, 1, 3, 0)) * 0.5
    x34 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x34 += einsum(t1, (0, 1), x4, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3))
    x35 += einsum(x34, (0, 1, 2, 3), (0, 1, 2, 3))
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(t2, (0, 1, 2, 3), x35, (1, 4, 3, 5), (4, 0, 5, 2)) * 0.5
    x37 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x37 += einsum(t2, (0, 1, 2, 3), x2, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x38 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x38 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3))
    x38 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x39 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(t1, (0, 1), x38, (0, 2, 3, 4), (2, 3, 1, 4))
    x40 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x40 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.25
    x40 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x40 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3))
    x40 += einsum(t1, (0, 1), x24, (2, 3), (0, 2, 1, 3))
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x40, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x41 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x41 += einsum(x7, (0, 1), t2, (2, 0, 3, 4), (2, 1, 3, 4))
    x42 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x42 += einsum(x4, (0, 1, 2, 3), t3, (4, 0, 1, 5, 6, 3), (2, 4, 5, 6))
    x43 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x43 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.08333333333333
    x43 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    rdm2_f_oovv += einsum(x43, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_oovv += einsum(x43, (0, 1, 2, 3), (1, 0, 2, 3))
    x44 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x44 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_ovov += einsum(x44, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x44, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x44, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x44, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x45 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x45 += einsum(t2, (0, 1, 2, 3), x44, (1, 4, 3, 5), (0, 4, 2, 5))
    x46 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x46 += einsum(x11, (0, 1, 2, 3), t3, (4, 5, 0, 6, 1, 2), (4, 5, 3, 6))
    x47 = np.zeros((nvir, nvir), dtype=np.float64)
    x47 += einsum(l2, (0, 1, 2, 3), t2, (2, 3, 4, 1), (0, 4))
    x48 = np.zeros((nvir, nvir), dtype=np.float64)
    x48 += einsum(l3, (0, 1, 2, 3, 4, 5), t3, (3, 4, 5, 6, 1, 2), (0, 6))
    x49 = np.zeros((nvir, nvir), dtype=np.float64)
    x49 += einsum(x47, (0, 1), (0, 1))
    x49 += einsum(x48, (0, 1), (0, 1)) * 0.16666666666666
    x50 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x50 += einsum(x49, (0, 1), t2, (2, 3, 4, 0), (2, 3, 1, 4)) * -0.5
    x51 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x51 += einsum(x16, (0, 1, 2, 3), (0, 2, 1, 3))
    x51 += einsum(x10, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x51 += einsum(x12, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.25
    x51 += einsum(x15, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x52 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x52 += einsum(t1, (0, 1), x51, (0, 2, 3, 4), (2, 3, 1, 4))
    x53 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x53 += einsum(x45, (0, 1, 2, 3), (0, 1, 2, 3))
    x53 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.25
    x53 += einsum(x50, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x53 += einsum(x52, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_oovv += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x53, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x54 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x54 += einsum(x9, (0, 1), t2, (2, 0, 3, 4), (1, 2, 3, 4))
    x55 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x55 += einsum(x2, (0, 1, 2, 3), t3, (4, 1, 0, 5, 6, 3), (2, 4, 5, 6))
    x56 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x56 += einsum(x6, (0, 1), t2, (2, 0, 3, 4), (2, 1, 3, 4))
    x57 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x57 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 3, 1)) * 2.0
    x57 += einsum(t2, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x58 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x58 += einsum(x5, (0, 1, 2, 3), x57, (0, 1, 4, 5), (2, 3, 4, 5)) * 0.25
    x59 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x59 += einsum(x54, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 += einsum(x55, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x59 += einsum(x56, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    x59 += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x60 = np.zeros((nocc, nocc, nocc, nocc, nocc, nvir), dtype=np.float64)
    x60 += einsum(t2, (0, 1, 2, 3), l3, (4, 2, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x60 += einsum(x14, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.00000000000012
    rdm2_f_oovv += einsum(t3, (0, 1, 2, 3, 4, 5), x60, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4)) * 0.08333333333333
    x61 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x61 += einsum(x1, (0, 1, 2, 3), (1, 0, 3, 2)) * -3.00000000000012
    x61 += einsum(x3, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.00000000000024
    x61 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x61, (0, 1, 4, 5), (5, 4, 2, 3)) * 0.08333333333333
    x62 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x62 += einsum(x1, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.99999999999994
    x62 += einsum(x3, (0, 1, 2, 3), (0, 1, 3, 2)) * 5.99999999999988
    x62 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2))
    x63 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x63 += einsum(t1, (0, 1), x62, (0, 2, 3, 4), (2, 4, 3, 1)) * -0.16666666666667
    rdm2_f_oovv += einsum(t1, (0, 1), x63, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    x64 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x64 += einsum(t1, (0, 1), x20, (0, 2, 3, 4), (2, 3, 1, 4))
    rdm2_f_ovov += einsum(x64, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_ovvo += einsum(x64, (0, 1, 2, 3), (1, 3, 2, 0))
    rdm2_f_voov += einsum(x64, (0, 1, 2, 3), (3, 1, 0, 2))
    rdm2_f_vovo += einsum(x64, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_ovvv += einsum(t1, (0, 1), x64, (0, 2, 3, 4), (2, 4, 3, 1))
    x65 = np.zeros((nvir, nvir), dtype=np.float64)
    x65 += einsum(l1, (0, 1), t1, (1, 2), (0, 2))
    x66 = np.zeros((nvir, nvir), dtype=np.float64)
    x66 += einsum(x65, (0, 1), (0, 1))
    x66 += einsum(x47, (0, 1), (0, 1)) * 0.5
    x66 += einsum(x48, (0, 1), (0, 1)) * 0.08333333333333
    rdm2_f_ovov += einsum(delta.oo, (0, 1), x66, (2, 3), (0, 2, 1, 3))
    rdm2_f_voov += einsum(delta.oo, (0, 1), x66, (2, 3), (2, 0, 1, 3)) * -1.0
    x67 = np.zeros((nvir, nvir), dtype=np.float64)
    x67 += einsum(x65, (0, 1), (0, 1)) * 12.00000000000048
    x67 += einsum(x47, (0, 1), (0, 1)) * 6.00000000000024
    x67 += einsum(x48, (0, 1), (0, 1))
    rdm2_f_ovvo += einsum(delta.oo, (0, 1), x67, (2, 3), (0, 2, 3, 1)) * -0.08333333333333
    rdm2_f_vovo += einsum(delta.oo, (0, 1), x67, (2, 3), (2, 0, 3, 1)) * 0.08333333333333
    x68 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x68 += einsum(t3, (0, 1, 2, 3, 4, 5), x13, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4)) * -1.0
    rdm2_f_ovvv += einsum(x68, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.16666666666667
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv += einsum(x68, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.16666666666667
    x69 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x69 += einsum(l1, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_ovvv += einsum(x69, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x69, (0, 1, 2, 3), (1, 0, 3, 2))
    x70 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x70 += einsum(l2, (0, 1, 2, 3), t3, (4, 2, 3, 5, 6, 1), (4, 0, 5, 6))
    rdm2_f_ovvv += einsum(x70, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    rdm2_f_vovv += einsum(x70, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x71 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x71 += einsum(t2, (0, 1, 2, 3), x11, (1, 4, 3, 5), (0, 4, 5, 2)) * -1.0
    x72 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x72 += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3))
    x72 += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x72 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x73 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x73 += einsum(t1, (0, 1), x72, (0, 2, 3, 4), (2, 1, 3, 4))
    x74 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x74 += einsum(x71, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x74 += einsum(x73, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x74 += einsum(t1, (0, 1), x66, (2, 3), (0, 2, 1, 3))
    rdm2_f_ovvv += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_ovvv += einsum(x74, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x74, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_vovv += einsum(x74, (0, 1, 2, 3), (1, 0, 3, 2))
    x75 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x75 += einsum(t2, (0, 1, 2, 3), x20, (0, 1, 4, 5), (4, 5, 2, 3)) * 0.5
    rdm2_f_ovvv += einsum(x75, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_vovv += einsum(x75, (0, 1, 2, 3), (1, 0, 3, 2))
    x76 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x76 += einsum(t1, (0, 1), x20, (0, 2, 3, 4), (2, 3, 4, 1)) * -2.0
    rdm2_f_vovv += einsum(t1, (0, 1), x76, (0, 2, 3, 4), (3, 2, 1, 4)) * -0.5
    x77 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x77 += einsum(t1, (0, 1), l2, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_vvov += einsum(x77, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_vvvo += einsum(x77, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_vvvv += einsum(t1, (0, 1), x77, (0, 2, 3, 4), (2, 3, 1, 4))
    x78 = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    x78 += einsum(t1, (0, 1), x11, (0, 2, 3, 4), (3, 2, 1, 4)) * -1.0
    rdm2_f_vvvv += einsum(x78, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    rdm2_f_vvvv += einsum(x78, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

