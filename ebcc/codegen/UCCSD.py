# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 2, 1, 3), ())
    e_cc += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 3), ())
    e_cc += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 2, 1, 3), ())
    x0 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x0 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x0 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x1 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x1 += einsum(f.bb.ov, (0, 1), (0, 1))
    x1 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    x1 += einsum(t1.bb, (0, 1), x0, (0, 2, 1, 3), (2, 3)) * -0.5
    e_cc += einsum(t1.bb, (0, 1), x1, (0, 1), ())
    x2 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x2 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x2 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x3 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(f.aa.ov, (0, 1), (0, 1))
    x3 += einsum(t1.aa, (0, 1), x2, (0, 2, 3, 1), (2, 3)) * -0.5
    e_cc += einsum(t1.aa, (0, 1), x3, (0, 1), ())

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    t1new = Namespace()
    t2new = Namespace()

    # T amplitudes
    t1new_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    t1new_aa += einsum(f.aa.ov, (0, 1), (0, 1))
    t1new_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    t1new_bb += einsum(f.bb.ov, (0, 1), (0, 1))
    t2new_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    t2new_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    t2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    t2new_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    x0 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x0 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    t1new_aa += einsum(x0, (0, 1), (0, 1))
    x1 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x1 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x2 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x2 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_aa += einsum(t2.aaaa, (0, 1, 2, 3), x2, (4, 0, 1, 3), (4, 2)) * 2.0
    x3 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x3 += einsum(t1.aa, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (3, 4, 0, 2))
    x4 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x4 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x4 += einsum(x3, (0, 1, 2, 3), (0, 1, 3, 2))
    t1new_aa += einsum(t2.abab, (0, 1, 2, 3), x4, (1, 3, 0, 4), (4, 2)) * -1.0
    x5 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x5 += einsum(t2.abab, (0, 1, 2, 3), (1, 3, 0, 2))
    x5 += einsum(t1.aa, (0, 1), t1.bb, (2, 3), (2, 3, 0, 1))
    t1new_aa += einsum(v.aabb.vvov, (0, 1, 2, 3), x5, (2, 3, 4, 1), (4, 0))
    t1new_bb += einsum(v.aabb.ovvv, (0, 1, 2, 3), x5, (4, 3, 0, 1), (4, 2))
    x6 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x6 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x6 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3)) * 0.5
    t1new_aa += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x6, (0, 4, 3, 1), (4, 2)) * -2.0
    x7 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x7 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(x7, (0, 1), (0, 1))
    x8 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x8 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x8 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x9 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x9 += einsum(t1.bb, (0, 1), x8, (0, 2, 1, 3), (2, 3))
    x10 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x10 += einsum(f.bb.ov, (0, 1), (0, 1))
    x10 += einsum(x7, (0, 1), (0, 1))
    x10 += einsum(x9, (0, 1), (0, 1)) * -1.0
    t1new_aa += einsum(x10, (0, 1), t2.abab, (2, 0, 3, 1), (2, 3))
    t1new_bb += einsum(x10, (0, 1), t2.bbbb, (2, 0, 3, 1), (2, 3)) * 2.0
    x11 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x11 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x11 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x12 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x12 += einsum(t1.aa, (0, 1), x11, (0, 2, 3, 1), (2, 3))
    x13 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(f.aa.ov, (0, 1), (0, 1))
    x13 += einsum(x0, (0, 1), (0, 1))
    x13 += einsum(x12, (0, 1), (0, 1)) * -1.0
    t1new_aa += einsum(x13, (0, 1), t2.aaaa, (2, 0, 3, 1), (2, 3)) * 2.0
    t1new_bb += einsum(x13, (0, 1), t2.abab, (0, 2, 1, 3), (2, 3))
    x14 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x14 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x14 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new_aa += einsum(t1.aa, (0, 1), x14, (0, 2, 1, 3), (2, 3)) * -1.0
    x15 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x15 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 1), (2, 3))
    x16 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x16 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 3), (0, 4))
    x17 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x17 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x18 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x18 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x18 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x19 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x19 += einsum(t1.aa, (0, 1), x18, (2, 3, 0, 1), (2, 3))
    x20 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x20 += einsum(t1.aa, (0, 1), x13, (2, 1), (0, 2))
    x21 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x21 += einsum(f.aa.oo, (0, 1), (0, 1))
    x21 += einsum(x15, (0, 1), (1, 0))
    x21 += einsum(x16, (0, 1), (1, 0))
    x21 += einsum(x17, (0, 1), (1, 0)) * 2.0
    x21 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x21 += einsum(x20, (0, 1), (1, 0))
    t1new_aa += einsum(t1.aa, (0, 1), x21, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x21, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x22 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x22 += einsum(f.aa.vv, (0, 1), (0, 1))
    x22 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (0, 1, 2, 3), (2, 3))
    t1new_aa += einsum(t1.aa, (0, 1), x22, (1, 2), (0, 2))
    x23 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x23 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x24 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x24 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x24 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_bb += einsum(t2.bbbb, (0, 1, 2, 3), x24, (4, 0, 1, 3), (4, 2)) * 2.0
    x25 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x25 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (0, 4, 2, 3))
    x26 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x26 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x26 += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3))
    t1new_bb += einsum(t2.abab, (0, 1, 2, 3), x26, (1, 4, 0, 2), (4, 3)) * -1.0
    x27 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x27 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x27 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3)) * 0.5
    t1new_bb += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x27, (0, 4, 3, 1), (4, 2)) * -2.0
    x28 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x28 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x28 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new_bb += einsum(t1.bb, (0, 1), x28, (0, 2, 1, 3), (2, 3)) * -1.0
    x29 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x29 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (0, 1, 2, 3), (2, 3))
    x30 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x30 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x31 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x31 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 3), (1, 4))
    x32 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x32 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x32 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x33 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x33 += einsum(t1.bb, (0, 1), x32, (0, 2, 3, 1), (2, 3))
    x34 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x34 += einsum(t1.bb, (0, 1), x10, (2, 1), (0, 2))
    x35 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x35 += einsum(f.bb.oo, (0, 1), (0, 1))
    x35 += einsum(x29, (0, 1), (1, 0))
    x35 += einsum(x30, (0, 1), (1, 0)) * 2.0
    x35 += einsum(x31, (0, 1), (1, 0))
    x35 += einsum(x33, (0, 1), (1, 0)) * -1.0
    x35 += einsum(x34, (0, 1), (1, 0))
    t1new_bb += einsum(t1.bb, (0, 1), x35, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x35, (0, 1), t2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    x36 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x36 += einsum(f.bb.vv, (0, 1), (0, 1))
    x36 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(t1.bb, (0, 1), x36, (1, 2), (0, 2))
    x37 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x37 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x38 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x38 += einsum(t1.aa, (0, 1), v.aabb.vvov, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(x38, (0, 1, 2, 3), (2, 0, 3, 1))
    x39 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x39 += einsum(t2.abab, (0, 1, 2, 3), x38, (1, 3, 4, 5), (4, 0, 2, 5))
    x40 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x40 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x40 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -0.5
    x41 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum(x14, (0, 1, 2, 3), x40, (0, 4, 2, 5), (1, 4, 3, 5)) * 2.0
    x42 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x42 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2))
    x43 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x43 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x43 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x44 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x44 += einsum(t2.abab, (0, 1, 2, 3), x43, (1, 3, 4, 5), (0, 4, 2, 5))
    x45 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x45 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x45 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x46 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x46 += einsum(t1.aa, (0, 1), x45, (2, 1, 3, 4), (0, 2, 3, 4))
    x47 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x47 += einsum(t2.aaaa, (0, 1, 2, 3), x46, (4, 1, 5, 3), (0, 4, 2, 5)) * -2.0
    x48 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x48 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x49 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x49 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x50 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x50 += einsum(t1.aa, (0, 1), x49, (2, 3, 4, 0), (2, 4, 3, 1))
    x51 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x51 += einsum(t1.aa, (0, 1), x37, (2, 3, 1, 4), (0, 2, 3, 4))
    x52 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x52 += einsum(t2.abab, (0, 1, 2, 3), x3, (1, 3, 4, 5), (4, 0, 5, 2))
    x53 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x53 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x54 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(t2.aaaa, (0, 1, 2, 3), x53, (1, 4, 5, 3), (0, 4, 5, 2)) * 2.0
    x55 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x55 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x55 += einsum(x1, (0, 1, 2, 3), (0, 2, 1, 3))
    x56 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x56 += einsum(t2.aaaa, (0, 1, 2, 3), x55, (4, 1, 5, 3), (0, 4, 5, 2)) * 2.0
    x57 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x57 += einsum(x48, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x57 += einsum(x50, (0, 1, 2, 3), (0, 2, 1, 3))
    x57 += einsum(x51, (0, 1, 2, 3), (0, 2, 1, 3))
    x57 += einsum(x52, (0, 1, 2, 3), (0, 2, 1, 3))
    x57 += einsum(x54, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x57 += einsum(x56, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x58 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x58 += einsum(t1.aa, (0, 1), x57, (2, 0, 3, 4), (2, 3, 1, 4))
    x59 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x59 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3))
    x59 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3))
    x59 += einsum(x41, (0, 1, 2, 3), (1, 0, 3, 2))
    x59 += einsum(x44, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x59 += einsum(x47, (0, 1, 2, 3), (1, 0, 2, 3))
    x59 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x59, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x59, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x59, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x60 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x60 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x61 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x61 += einsum(t2.aaaa, (0, 1, 2, 3), x49, (4, 5, 1, 0), (4, 5, 2, 3)) * -1.0
    x62 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x62 += einsum(f.aa.oo, (0, 1), (0, 1))
    x62 += einsum(x20, (0, 1), (0, 1))
    x63 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum(x62, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x64 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x64 += einsum(x15, (0, 1), (1, 0))
    x64 += einsum(x16, (0, 1), (1, 0))
    x64 += einsum(x17, (0, 1), (1, 0)) * 2.0
    x64 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x65 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x65 += einsum(x64, (0, 1), t2.aaaa, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x66 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x66 += einsum(x60, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x66 += einsum(x61, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x66 += einsum(x63, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x66 += einsum(x65, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x66, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x66, (0, 1, 2, 3), (1, 0, 2, 3))
    x67 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x67 += einsum(t1.aa, (0, 1), v.aaaa.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x68 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum(t1.aa, (0, 1), x67, (2, 3, 1, 4), (0, 2, 3, 4))
    x69 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x69 += einsum(t2.aaaa, (0, 1, 2, 3), x11, (1, 4, 5, 3), (0, 4, 2, 5))
    x70 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum(t2.aaaa, (0, 1, 2, 3), x69, (4, 1, 5, 3), (0, 4, 2, 5)) * -4.0
    x71 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 1), (2, 3))
    x72 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x72 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x73 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x73 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x74 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x74 += einsum(t1.aa, (0, 1), x45, (0, 1, 2, 3), (2, 3))
    x75 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x75 += einsum(x71, (0, 1), (1, 0)) * -1.0
    x75 += einsum(x72, (0, 1), (1, 0))
    x75 += einsum(x73, (0, 1), (1, 0)) * 2.0
    x75 += einsum(x74, (0, 1), (1, 0)) * -1.0
    x76 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x76 += einsum(x75, (0, 1), t2.aaaa, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x77 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x77 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x78 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x78 += einsum(x13, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4)) * -2.0
    x79 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x79 += einsum(t1.aa, (0, 1), x1, (2, 3, 4, 1), (2, 0, 4, 3))
    x80 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x80 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x80 += einsum(x79, (0, 1, 2, 3), (3, 1, 2, 0))
    x81 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x81 += einsum(t1.aa, (0, 1), x80, (0, 2, 3, 4), (2, 3, 4, 1))
    x82 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x82 += einsum(x77, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x82 += einsum(x78, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x82 += einsum(x81, (0, 1, 2, 3), (1, 0, 2, 3))
    x83 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x83 += einsum(t1.aa, (0, 1), x82, (0, 2, 3, 4), (2, 3, 1, 4))
    x84 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x84 += einsum(x68, (0, 1, 2, 3), (0, 1, 2, 3))
    x84 += einsum(x70, (0, 1, 2, 3), (0, 1, 2, 3))
    x84 += einsum(x76, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x84 += einsum(x83, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x84, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x85 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x85 += einsum(f.aa.vv, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4))
    x86 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x86 += einsum(t2.abab, (0, 1, 2, 3), x8, (1, 4, 3, 5), (4, 5, 0, 2))
    x87 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x87 += einsum(t2.abab, (0, 1, 2, 3), x86, (1, 3, 4, 5), (0, 4, 2, 5)) * -1.0
    x88 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x88 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x88 += einsum(x85, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x88 += einsum(x87, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_aaaa += einsum(x88, (0, 1, 2, 3), (0, 1, 2, 3))
    x89 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x89 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x89 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    x90 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x90 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x90 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x89, (4, 5, 1, 3), (0, 5, 2, 4))
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), x90, (0, 4, 1, 5), (4, 5, 2, 3)) * -2.0
    x91 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x91 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x92 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x92 += einsum(t1.aa, (0, 1), x91, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    x92 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x92 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    t2new_aaaa += einsum(t1.aa, (0, 1), x92, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x93 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x93 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x93 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x94 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x94 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x94 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x94 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (4, 0, 5, 2))
    x94 += einsum(x40, (0, 1, 2, 3), x93, (0, 4, 2, 5), (4, 1, 5, 3)) * -2.0
    x94 += einsum(x46, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x94 += einsum(t1.aa, (0, 1), x18, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x94, (0, 4, 2, 5), (4, 1, 5, 3))
    x95 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x95 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x95 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x96 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x96 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x96 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -0.5
    x97 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x97 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x97 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x98 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x98 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x98 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x99 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x99 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x99 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x99 += einsum(x95, (0, 1, 2, 3), x96, (0, 4, 2, 5), (1, 4, 3, 5)) * -2.0
    x99 += einsum(t1.bb, (0, 1), x97, (2, 3, 1, 4), (2, 0, 3, 4)) * -1.0
    x99 += einsum(t1.bb, (0, 1), x98, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x99, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x100 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x100 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x101 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x101 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x101 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 4), (4, 1, 2, 3))
    x101 += einsum(x100, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x101 += einsum(v.aabb.ovov, (0, 1, 2, 3), x5, (2, 4, 5, 1), (3, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x101, (3, 4, 0, 5), (5, 1, 2, 4))
    x102 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x103 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x103 += einsum(t1.bb, (0, 1), v.aabb.ovoo, (2, 3, 4, 0), (4, 1, 2, 3)) * -1.0
    x103 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3))
    x103 += einsum(v.aabb.ovov, (0, 1, 2, 3), x96, (2, 4, 3, 5), (4, 5, 0, 1)) * 2.0
    t2new_abab += einsum(t2.aaaa, (0, 1, 2, 3), x103, (4, 5, 1, 3), (0, 4, 2, 5)) * 2.0
    x104 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x104 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x104 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x104 += einsum(t1.aa, (0, 1), x4, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    t2new_abab += einsum(x104, (0, 1, 2, 3), x96, (0, 4, 1, 5), (2, 4, 3, 5)) * 2.0
    x105 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x105 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x105 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    x106 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x106 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x106 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 4, 1), (4, 0, 2, 3))
    x106 += einsum(t1.aa, (0, 1), x105, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x106, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x107 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x107 += einsum(v.aabb.vvvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x107 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 4), (4, 1, 2, 3))
    x107 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 2, 3, 4), (3, 4, 2, 1))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x107, (3, 4, 2, 5), (0, 1, 5, 4)) * -1.0
    x108 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x108 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x109 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x109 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x109 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 4, 1), (4, 0, 2, 3))
    x109 += einsum(x108, (0, 1, 2, 3), (1, 0, 3, 2))
    x109 += einsum(v.aabb.ovov, (0, 1, 2, 3), x5, (4, 3, 5, 1), (2, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x109, (1, 4, 0, 5), (5, 4, 2, 3))
    x110 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x110 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x110 += einsum(x71, (0, 1), (1, 0)) * -1.0
    x110 += einsum(x72, (0, 1), (1, 0))
    x110 += einsum(x73, (0, 1), (1, 0)) * 2.0
    x110 += einsum(x74, (0, 1), (1, 0)) * -1.0
    x110 += einsum(t1.aa, (0, 1), x13, (0, 2), (2, 1))
    t2new_abab += einsum(x110, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x111 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x111 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 1, 2, 3), (2, 3))
    x112 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x112 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 4, 1, 3), (2, 4))
    x113 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x114 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x114 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x114 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x115 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x115 += einsum(t1.bb, (0, 1), x114, (0, 2, 1, 3), (2, 3))
    x116 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x116 += einsum(f.bb.vv, (0, 1), (0, 1)) * -1.0
    x116 += einsum(x111, (0, 1), (1, 0)) * -1.0
    x116 += einsum(x112, (0, 1), (1, 0)) * 2.0
    x116 += einsum(x113, (0, 1), (1, 0))
    x116 += einsum(x115, (0, 1), (0, 1)) * -1.0
    x116 += einsum(t1.bb, (0, 1), x10, (0, 2), (2, 1))
    t2new_abab += einsum(x116, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    x117 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x117 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x117 += einsum(x100, (0, 1, 2, 3), (1, 0, 2, 3))
    x118 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x118 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x118 += einsum(x108, (0, 1, 2, 3), (1, 0, 2, 3))
    x118 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (5, 1, 0, 4))
    x119 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x119 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x119 += einsum(x3, (0, 1, 2, 3), (0, 1, 3, 2))
    x119 += einsum(t1.bb, (0, 1), x117, (1, 2, 3, 4), (0, 2, 4, 3))
    x119 += einsum(t1.bb, (0, 1), x118, (0, 2, 3, 4), (2, 1, 4, 3)) * -1.0
    t2new_abab += einsum(t1.aa, (0, 1), x119, (2, 3, 0, 4), (4, 2, 1, 3)) * -1.0
    x120 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x120 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x120 += einsum(t1.aa, (0, 1), v.aabb.vvvv, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(t1.bb, (0, 1), x120, (1, 2, 3, 4), (3, 0, 4, 2))
    x121 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x121 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x121 += einsum(t1.aa, (0, 1), v.aabb.vvoo, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(t1.bb, (0, 1), x121, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    x122 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x122 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x123 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x123 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x124 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x124 += einsum(t2.abab, (0, 1, 2, 3), x102, (4, 5, 0, 2), (4, 1, 3, 5))
    x125 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x125 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x125 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x125 += einsum(x123, (0, 1, 2, 3), (1, 0, 3, 2))
    x126 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x126 += einsum(t2.bbbb, (0, 1, 2, 3), x125, (1, 4, 3, 5), (0, 4, 2, 5)) * 2.0
    x127 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x127 += einsum(t1.bb, (0, 1), x114, (2, 3, 1, 4), (0, 2, 3, 4))
    x128 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x128 += einsum(t2.bbbb, (0, 1, 2, 3), x127, (4, 1, 3, 5), (0, 4, 2, 5)) * -2.0
    x129 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x129 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x130 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x130 += einsum(t1.bb, (0, 1), x129, (2, 3, 4, 0), (2, 4, 3, 1))
    x131 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x131 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovoo, (0, 2, 4, 5), (1, 4, 5, 3))
    x132 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x132 += einsum(t2.abab, (0, 1, 2, 3), x25, (4, 5, 0, 2), (4, 1, 5, 3))
    x133 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x133 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x133 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x134 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x134 += einsum(t2.bbbb, (0, 1, 2, 3), x133, (1, 4, 5, 3), (0, 4, 5, 2)) * 2.0
    x135 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x135 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x135 += einsum(x23, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x136 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x136 += einsum(t2.bbbb, (0, 1, 2, 3), x135, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x137 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x137 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x137 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x137 += einsum(x122, (0, 1, 2, 3), (0, 1, 2, 3))
    x138 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x138 += einsum(t1.bb, (0, 1), x137, (2, 3, 1, 4), (0, 2, 3, 4))
    x139 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x139 += einsum(x130, (0, 1, 2, 3), (0, 2, 1, 3))
    x139 += einsum(x131, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x139 += einsum(x132, (0, 1, 2, 3), (0, 2, 1, 3))
    x139 += einsum(x134, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x139 += einsum(x136, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x139 += einsum(x138, (0, 1, 2, 3), (0, 2, 1, 3))
    x140 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x140 += einsum(t1.bb, (0, 1), x139, (2, 0, 3, 4), (2, 3, 1, 4))
    x141 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x141 += einsum(x122, (0, 1, 2, 3), (0, 1, 2, 3))
    x141 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x141 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    x141 += einsum(x126, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x141 += einsum(x128, (0, 1, 2, 3), (1, 0, 2, 3))
    x141 += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x141, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x141, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x141, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x141, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x142 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x142 += einsum(t1.bb, (0, 1), v.bbbb.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x143 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x143 += einsum(t1.bb, (0, 1), x142, (2, 3, 1, 4), (0, 2, 3, 4))
    x144 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x144 += einsum(t2.bbbb, (0, 1, 2, 3), x95, (1, 4, 5, 3), (0, 4, 2, 5))
    x145 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x145 += einsum(t2.bbbb, (0, 1, 2, 3), x144, (4, 1, 5, 3), (0, 4, 2, 5)) * -4.0
    x146 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x146 += einsum(t2.abab, (0, 1, 2, 3), x11, (0, 4, 5, 2), (1, 3, 4, 5))
    x147 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x147 += einsum(t2.abab, (0, 1, 2, 3), x146, (4, 5, 0, 2), (1, 4, 3, 5)) * -1.0
    x148 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x148 += einsum(x111, (0, 1), (1, 0)) * -1.0
    x148 += einsum(x112, (0, 1), (1, 0)) * 2.0
    x148 += einsum(x113, (0, 1), (1, 0))
    x148 += einsum(x115, (0, 1), (0, 1)) * -1.0
    x149 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x149 += einsum(x148, (0, 1), t2.bbbb, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x150 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x150 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x151 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x151 += einsum(x10, (0, 1), t2.bbbb, (2, 3, 4, 1), (0, 2, 3, 4)) * -2.0
    x152 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x152 += einsum(t1.bb, (0, 1), x23, (2, 3, 4, 1), (2, 0, 4, 3))
    x153 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x153 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x153 += einsum(x152, (0, 1, 2, 3), (3, 1, 2, 0))
    x154 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x154 += einsum(t1.bb, (0, 1), x153, (0, 2, 3, 4), (2, 3, 4, 1))
    x155 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x155 += einsum(x150, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x155 += einsum(x151, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x155 += einsum(x154, (0, 1, 2, 3), (1, 0, 2, 3))
    x156 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x156 += einsum(t1.bb, (0, 1), x155, (0, 2, 3, 4), (2, 3, 1, 4))
    x157 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x157 += einsum(x143, (0, 1, 2, 3), (0, 1, 2, 3))
    x157 += einsum(x145, (0, 1, 2, 3), (1, 0, 3, 2))
    x157 += einsum(x147, (0, 1, 2, 3), (1, 0, 3, 2))
    x157 += einsum(x149, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x157 += einsum(x156, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x157, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x158 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x158 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x159 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x159 += einsum(t2.bbbb, (0, 1, 2, 3), x129, (4, 5, 1, 0), (4, 5, 2, 3)) * -1.0
    x160 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x160 += einsum(f.bb.oo, (0, 1), (0, 1))
    x160 += einsum(x34, (0, 1), (0, 1))
    x161 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x161 += einsum(x160, (0, 1), t2.bbbb, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x162 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x162 += einsum(x29, (0, 1), (1, 0))
    x162 += einsum(x30, (0, 1), (1, 0)) * 2.0
    x162 += einsum(x31, (0, 1), (1, 0))
    x162 += einsum(x33, (0, 1), (1, 0)) * -1.0
    x163 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x163 += einsum(x162, (0, 1), t2.bbbb, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x164 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x164 += einsum(x158, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x164 += einsum(x159, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x164 += einsum(x161, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x164 += einsum(x163, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x164, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x164, (0, 1, 2, 3), (1, 0, 2, 3))
    x165 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x165 += einsum(f.bb.vv, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4))
    x166 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x166 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x166 += einsum(x165, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    t2new_bbbb += einsum(x166, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_bbbb += einsum(x166, (0, 1, 2, 3), (0, 1, 2, 3))
    x167 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x167 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x168 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x168 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x168 += einsum(x167, (0, 1, 2, 3), (3, 1, 0, 2))
    x168 += einsum(x152, (0, 1, 2, 3), (3, 1, 0, 2))
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), x168, (0, 4, 5, 1), (5, 4, 2, 3)) * -2.0
    x169 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x169 += einsum(t1.bb, (0, 1), x167, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    x169 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x169 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    t2new_bbbb += einsum(t1.bb, (0, 1), x169, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0

    t1new.aa = t1new_aa
    t1new.bb = t1new_bb
    t2new.aaaa = t2new_aaaa
    t2new.abab = t2new_abab
    t2new.bbbb = t2new_bbbb

    return {"t1new": t1new, "t2new": t2new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    l1new = Namespace()
    l2new = Namespace()

    # L amplitudes
    l1new_aa = np.zeros((nvir[0], nocc[0]), dtype=np.float64)
    l1new_aa += einsum(f.aa.ov, (0, 1), (1, 0))
    l1new_bb = np.zeros((nvir[1], nocc[1]), dtype=np.float64)
    l1new_bb += einsum(f.bb.ov, (0, 1), (1, 0))
    l2new_aaaa = np.zeros((nvir[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    l2new_aaaa += einsum(l2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 0, 5, 1), (4, 5, 2, 3)) * 2.0
    l2new_abab = np.zeros((nvir[0], nvir[1], nocc[0], nocc[1]), dtype=np.float64)
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), v.aabb.vvvv, (4, 0, 5, 1), (4, 5, 2, 3))
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (1, 3, 0, 2))
    l2new_abab += einsum(l1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 0), (3, 4, 2, 1))
    l2new_abab += einsum(l1.aa, (0, 1), v.aabb.vvov, (2, 0, 3, 4), (2, 4, 1, 3))
    l2new_bbbb = np.zeros((nvir[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    l2new_bbbb += einsum(l2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 0, 5, 1), (4, 5, 2, 3)) * 2.0
    x0 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x0 += einsum(t1.bb, (0, 1), l2.abab, (2, 1, 3, 4), (4, 0, 3, 2))
    l1new_aa += einsum(v.aabb.vvoo, (0, 1, 2, 3), x0, (2, 3, 4, 1), (0, 4)) * -1.0
    l2new_abab += einsum(v.aabb.vvov, (0, 1, 2, 3), x0, (4, 2, 5, 1), (0, 3, 5, 4)) * -1.0
    x1 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x1 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    l1new_aa += einsum(v.aaaa.oovv, (0, 1, 2, 3), x1, (4, 0, 1, 3), (2, 4)) * -2.0
    l2new_abab += einsum(v.aabb.ooov, (0, 1, 2, 3), x1, (4, 1, 0, 5), (5, 3, 4, 2)) * -2.0
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), (2, 3, 4, 5))
    l1new_aa += einsum(v.aaaa.ooov, (0, 1, 2, 3), x2, (4, 1, 2, 0), (3, 4)) * 2.0
    x3 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x3 += einsum(t1.aa, (0, 1), x1, (2, 3, 4, 1), (3, 2, 4, 0))
    l1new_aa += einsum(v.aaaa.ooov, (0, 1, 2, 3), x3, (4, 1, 0, 2), (3, 4)) * -2.0
    x4 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x4 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    l1new_aa += einsum(x1, (0, 1, 2, 3), x4, (1, 2, 4, 3), (4, 0)) * 2.0
    x5 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x5 += einsum(t1.aa, (0, 1), v.aaaa.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    l1new_aa += einsum(l2.aaaa, (0, 1, 2, 3), x5, (3, 4, 0, 1), (4, 2)) * 2.0
    x6 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x6 += einsum(t1.bb, (0, 1), v.aabb.vvvv, (2, 3, 4, 1), (0, 4, 2, 3))
    l1new_aa += einsum(l2.abab, (0, 1, 2, 3), x6, (3, 1, 4, 0), (4, 2))
    x7 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x7 += einsum(t1.aa, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new_abab += einsum(x1, (0, 1, 2, 3), x7, (4, 5, 1, 2), (3, 5, 0, 4)) * -2.0
    x8 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x8 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x9 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x9 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x9 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x9 += einsum(x8, (0, 1, 2, 3), (1, 0, 2, 3))
    x9 += einsum(x8, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x10 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x10 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x10 += einsum(x7, (0, 1, 2, 3), (0, 1, 3, 2))
    x11 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x11 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (0, 4, 2, 3))
    x12 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x12 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x12 += einsum(x11, (0, 1, 2, 3), (1, 0, 2, 3))
    x13 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    x14 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x14 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x14 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x15 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x15 += einsum(t1.aa, (0, 1), x14, (0, 2, 3, 1), (2, 3))
    x16 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x16 += einsum(f.aa.ov, (0, 1), (0, 1))
    x16 += einsum(x13, (0, 1), (0, 1))
    x16 += einsum(x15, (0, 1), (0, 1)) * -1.0
    l2new_abab += einsum(l1.bb, (0, 1), x16, (2, 3), (3, 0, 2, 1))
    x17 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x17 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x18 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x18 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x18 += einsum(x17, (0, 1, 2, 3), (1, 0, 3, 2))
    x19 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x19 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x20 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x20 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (1, 5, 0, 4))
    x21 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x21 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x21 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(x0, (0, 1, 2, 3), x21, (1, 4, 2, 5), (3, 4, 5, 0))
    l2new_abab += einsum(l1.aa, (0, 1), x21, (2, 3, 1, 4), (0, 3, 4, 2)) * -1.0
    x22 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x22 += einsum(t1.bb, (0, 1), x21, (2, 1, 3, 4), (0, 2, 3, 4))
    x23 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x23 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x23 += einsum(x19, (0, 1, 2, 3), (1, 0, 3, 2))
    x23 += einsum(x20, (0, 1, 2, 3), (1, 0, 3, 2))
    x23 += einsum(x22, (0, 1, 2, 3), (1, 0, 3, 2))
    x24 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x24 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x24 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x24 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (4, 2, 5, 3), (1, 5, 0, 4))
    x24 += einsum(t2.abab, (0, 1, 2, 3), x9, (4, 5, 0, 2), (1, 3, 5, 4)) * -1.0
    x24 += einsum(t2.bbbb, (0, 1, 2, 3), x10, (1, 3, 4, 5), (0, 2, 5, 4)) * 2.0
    x24 += einsum(t2.abab, (0, 1, 2, 3), x12, (1, 4, 5, 2), (4, 3, 0, 5)) * -1.0
    x24 += einsum(x16, (0, 1), t2.abab, (2, 3, 1, 4), (3, 4, 2, 0))
    x24 += einsum(t1.bb, (0, 1), x18, (1, 2, 3, 4), (0, 2, 4, 3))
    x24 += einsum(t1.bb, (0, 1), x23, (0, 2, 3, 4), (2, 1, 4, 3)) * -1.0
    l1new_aa += einsum(l2.abab, (0, 1, 2, 3), x24, (3, 1, 2, 4), (0, 4)) * -1.0
    x25 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x25 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x25 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x25 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(x8, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x26 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x26 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x26 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x26 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3))
    x27 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x27 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x28 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x28 += einsum(t1.aa, (0, 1), x8, (2, 3, 4, 1), (0, 2, 3, 4))
    x29 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x29 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x30 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x30 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x30 += einsum(x27, (0, 1, 2, 3), (3, 1, 2, 0))
    x30 += einsum(x28, (0, 1, 2, 3), (3, 1, 2, 0))
    x30 += einsum(x29, (0, 1, 2, 3), (2, 1, 3, 0))
    x30 += einsum(x29, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x31 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x31 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x31 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 2, 5, 3), (4, 0, 1, 5)) * -1.0
    x31 += einsum(t2.aaaa, (0, 1, 2, 3), x25, (4, 5, 1, 3), (5, 0, 4, 2)) * -2.0
    x31 += einsum(t2.abab, (0, 1, 2, 3), x21, (1, 3, 4, 5), (5, 0, 4, 2))
    x31 += einsum(x16, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4))
    x31 += einsum(t1.aa, (0, 1), x26, (2, 3, 1, 4), (3, 2, 0, 4))
    x31 += einsum(t1.aa, (0, 1), x30, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    l1new_aa += einsum(l2.aaaa, (0, 1, 2, 3), x31, (4, 3, 2, 1), (0, 4)) * -2.0
    x32 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x32 += einsum(l2.abab, (0, 1, 2, 3), (3, 1, 2, 0))
    x32 += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (4, 5, 2, 0)) * 2.0
    x32 += einsum(t1.bb, (0, 1), x0, (0, 2, 3, 4), (2, 1, 3, 4)) * -1.0
    x32 += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 1, 5), (4, 5, 2, 0)) * 2.0
    l1new_aa += einsum(v.aabb.vvov, (0, 1, 2, 3), x32, (2, 3, 4, 1), (0, 4))
    x33 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x33 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x33 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x34 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x34 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 4, 0, 5)) * 0.25
    x34 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 5, 1), (2, 4, 0, 5))
    l1new_aa += einsum(x33, (0, 1, 2, 3), x34, (4, 0, 2, 1), (3, 4)) * 4.0
    x35 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x35 += einsum(t1.aa, (0, 1), l2.abab, (1, 2, 3, 4), (4, 2, 3, 0))
    l1new_bb += einsum(v.aabb.oovv, (0, 1, 2, 3), x35, (4, 3, 0, 1), (2, 4)) * -1.0
    l2new_abab += einsum(v.aabb.ovvv, (0, 1, 2, 3), x35, (4, 3, 5, 0), (1, 2, 5, 4)) * -1.0
    l2new_abab += einsum(x16, (0, 1), x35, (2, 3, 4, 0), (1, 3, 4, 2)) * -1.0
    x36 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x36 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), (3, 5, 2, 4))
    x37 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x37 += einsum(t1.bb, (0, 1), x35, (2, 1, 3, 4), (2, 0, 3, 4))
    x38 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x38 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x38 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), x38, (4, 2, 5, 0), (1, 3, 5, 4))
    x39 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x39 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), (2, 4))
    x40 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x40 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 0, 1), (2, 4))
    x41 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x41 += einsum(x39, (0, 1), (0, 1))
    x41 += einsum(x40, (0, 1), (0, 1)) * 2.0
    l1new_aa += einsum(f.aa.ov, (0, 1), x41, (2, 0), (1, 2)) * -1.0
    x42 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x42 += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), (3, 4, 1, 2))
    x42 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3))
    x42 += einsum(t2.bbbb, (0, 1, 2, 3), x35, (1, 3, 4, 5), (0, 2, 4, 5)) * 2.0
    x42 += einsum(t2.abab, (0, 1, 2, 3), x0, (1, 4, 5, 2), (4, 3, 5, 0)) * -1.0
    x42 += einsum(t2.abab, (0, 1, 2, 3), x1, (4, 0, 5, 2), (1, 3, 4, 5)) * -2.0
    x42 += einsum(t1.bb, (0, 1), x38, (0, 2, 3, 4), (2, 1, 3, 4)) * -1.0
    x42 += einsum(t1.bb, (0, 1), x41, (2, 3), (0, 1, 2, 3))
    l1new_aa += einsum(v.aabb.ovov, (0, 1, 2, 3), x42, (2, 3, 4, 0), (1, 4)) * -1.0
    x43 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x43 += einsum(t2.abab, (0, 1, 2, 3), x35, (1, 3, 4, 5), (4, 5, 0, 2))
    x44 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x44 += einsum(t2.aaaa, (0, 1, 2, 3), x1, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x45 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x45 += einsum(x2, (0, 1, 2, 3), (1, 0, 3, 2))
    x45 += einsum(x3, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new_aaaa += einsum(v.aaaa.ovov, (0, 1, 2, 3), x45, (4, 5, 0, 2), (3, 1, 5, 4)) * 2.0
    x46 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x46 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 0), (1, 2, 3, 4))
    x46 += einsum(x1, (0, 1, 2, 3), (1, 0, 2, 3))
    x46 += einsum(x43, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x46 += einsum(x44, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x46 += einsum(t1.aa, (0, 1), x45, (0, 2, 3, 4), (2, 4, 3, 1))
    x46 += einsum(t1.aa, (0, 1), x41, (2, 3), (2, 0, 3, 1)) * 0.5
    l1new_aa += einsum(v.aaaa.ovov, (0, 1, 2, 3), x46, (4, 2, 0, 3), (1, 4)) * -2.0
    x47 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x47 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), (1, 5, 2, 4))
    x47 += einsum(t1.bb, (0, 1), x35, (0, 2, 3, 4), (1, 2, 3, 4))
    l1new_aa += einsum(v.aabb.ovvv, (0, 1, 2, 3), x47, (3, 2, 4, 0), (1, 4)) * -1.0
    x48 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x48 += einsum(l2.aaaa, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x48 += einsum(t1.aa, (0, 1), x1, (2, 0, 3, 4), (2, 3, 4, 1))
    l1new_aa += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x48, (4, 0, 3, 1), (2, 4)) * -2.0
    x49 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x49 += einsum(l1.aa, (0, 1), t1.aa, (1, 2), (0, 2))
    x50 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x50 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), (0, 4))
    x51 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x51 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 1), (0, 4))
    x52 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x52 += einsum(x49, (0, 1), (0, 1))
    x52 += einsum(x50, (0, 1), (0, 1))
    x52 += einsum(x51, (0, 1), (0, 1)) * 2.0
    l1new_aa += einsum(x52, (0, 1), x33, (2, 1, 0, 3), (3, 2)) * -1.0
    x53 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), (2, 3))
    x54 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 0), (2, 3))
    x55 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x55 += einsum(t2.abab, (0, 1, 2, 3), x35, (1, 3, 0, 4), (4, 2))
    x56 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x56 += einsum(t2.aaaa, (0, 1, 2, 3), x1, (0, 1, 4, 3), (4, 2)) * -1.0
    x57 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x57 += einsum(l1.aa, (0, 1), t1.aa, (2, 0), (1, 2))
    l1new_aa += einsum(x16, (0, 1), x57, (2, 0), (1, 2)) * -1.0
    x58 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x58 += einsum(x57, (0, 1), (0, 1)) * 0.5
    x58 += einsum(x39, (0, 1), (0, 1)) * 0.5
    x58 += einsum(x40, (0, 1), (0, 1))
    l1new_bb += einsum(x58, (0, 1), v.aabb.ooov, (0, 1, 2, 3), (3, 2)) * -2.0
    l2new_abab += einsum(x58, (0, 1), v.aabb.ovov, (1, 2, 3, 4), (2, 4, 0, 3)) * -2.0
    x59 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x59 += einsum(t1.aa, (0, 1), (0, 1)) * -1.0
    x59 += einsum(x53, (0, 1), (0, 1)) * -1.0
    x59 += einsum(x54, (0, 1), (0, 1)) * -2.0
    x59 += einsum(x55, (0, 1), (0, 1))
    x59 += einsum(x56, (0, 1), (0, 1)) * 2.0
    x59 += einsum(t1.aa, (0, 1), x58, (0, 2), (2, 1)) * 2.0
    l1new_aa += einsum(x59, (0, 1), x14, (0, 2, 3, 1), (3, 2))
    x60 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x60 += einsum(x43, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x60 += einsum(x44, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x60 += einsum(t1.aa, (0, 1), x41, (2, 3), (2, 0, 3, 1)) * 0.5
    l1new_aa += einsum(v.aaaa.ovov, (0, 1, 2, 3), x60, (4, 2, 0, 1), (3, 4)) * 2.0
    x61 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x61 += einsum(l1.bb, (0, 1), t1.bb, (1, 2), (0, 2))
    x62 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x62 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 1), (0, 4))
    x63 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x63 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), (1, 4))
    x64 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x64 += einsum(x61, (0, 1), (0, 1))
    x64 += einsum(x62, (0, 1), (0, 1)) * 2.0
    x64 += einsum(x63, (0, 1), (0, 1))
    l1new_aa += einsum(x64, (0, 1), v.aabb.ovvv, (2, 3, 1, 0), (3, 2))
    x65 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x65 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 0), (2, 3))
    x66 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x66 += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), (2, 3))
    x67 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x67 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    l1new_bb += einsum(v.bbbb.oovv, (0, 1, 2, 3), x67, (4, 1, 0, 3), (2, 4)) * -2.0
    l2new_abab += einsum(v.aabb.ovoo, (0, 1, 2, 3), x67, (4, 3, 2, 5), (1, 5, 0, 4)) * -2.0
    l2new_abab += einsum(x11, (0, 1, 2, 3), x67, (4, 0, 1, 5), (3, 5, 2, 4)) * -2.0
    x68 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x68 += einsum(t2.bbbb, (0, 1, 2, 3), x67, (0, 1, 4, 3), (4, 2)) * -1.0
    x69 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x69 += einsum(t2.abab, (0, 1, 2, 3), x0, (1, 4, 0, 2), (4, 3))
    x70 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x70 += einsum(l1.bb, (0, 1), t1.bb, (2, 0), (1, 2))
    x71 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x71 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 0, 1), (2, 4))
    x72 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x72 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), (3, 4))
    x73 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x73 += einsum(x70, (0, 1), (0, 1))
    x73 += einsum(x71, (0, 1), (0, 1)) * 2.0
    x73 += einsum(x72, (0, 1), (0, 1))
    l2new_abab += einsum(x73, (0, 1), v.aabb.ovov, (2, 3, 1, 4), (3, 4, 2, 0)) * -1.0
    x74 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x74 += einsum(l1.bb, (0, 1), (1, 0)) * -0.5
    x74 += einsum(t1.bb, (0, 1), (0, 1)) * -0.5
    x74 += einsum(x65, (0, 1), (0, 1)) * -1.0
    x74 += einsum(x66, (0, 1), (0, 1)) * -0.5
    x74 += einsum(x68, (0, 1), (0, 1))
    x74 += einsum(x69, (0, 1), (0, 1)) * 0.5
    x74 += einsum(t1.bb, (0, 1), x73, (0, 2), (2, 1)) * 0.5
    l1new_aa += einsum(x74, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (3, 2)) * -2.0
    x75 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x75 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x75 += einsum(x37, (0, 1, 2, 3), (1, 0, 2, 3))
    l1new_aa += einsum(v.aabb.ovoo, (0, 1, 2, 3), x75, (2, 3, 4, 0), (1, 4))
    x76 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x76 += einsum(x57, (0, 1), (0, 1))
    x76 += einsum(x39, (0, 1), (0, 1))
    x76 += einsum(x40, (0, 1), (0, 1)) * 2.0
    x77 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x77 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x77 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    l1new_aa += einsum(x76, (0, 1), x77, (0, 2, 1, 3), (3, 2)) * -1.0
    x78 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x78 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x78 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l1new_aa += einsum(l1.aa, (0, 1), x78, (1, 2, 0, 3), (3, 2)) * -1.0
    x79 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x79 += einsum(x70, (0, 1), (0, 1)) * 0.5
    x79 += einsum(x71, (0, 1), (0, 1))
    x79 += einsum(x72, (0, 1), (0, 1)) * 0.5
    l1new_aa += einsum(x79, (0, 1), v.aabb.ovoo, (2, 3, 0, 1), (3, 2)) * -2.0
    x80 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x80 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 1), (2, 3))
    x81 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x81 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x81 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x82 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x82 += einsum(f.aa.vv, (0, 1), (0, 1))
    x82 += einsum(x80, (0, 1), (1, 0))
    x82 += einsum(t1.aa, (0, 1), x81, (0, 1, 2, 3), (3, 2)) * -1.0
    l1new_aa += einsum(l1.aa, (0, 1), x82, (0, 2), (2, 1))
    x83 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x83 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 1), (2, 3))
    x84 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x84 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 3), (0, 4))
    x85 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x85 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 1, 3), (0, 4))
    x86 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x86 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x86 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x87 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x87 += einsum(t1.aa, (0, 1), x86, (2, 3, 0, 1), (2, 3))
    x88 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x88 += einsum(t1.aa, (0, 1), x16, (2, 1), (0, 2))
    x89 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x89 += einsum(f.aa.oo, (0, 1), (0, 1))
    x89 += einsum(x83, (0, 1), (1, 0))
    x89 += einsum(x84, (0, 1), (0, 1))
    x89 += einsum(x85, (0, 1), (0, 1)) * 2.0
    x89 += einsum(x87, (0, 1), (1, 0)) * -1.0
    x89 += einsum(x88, (0, 1), (0, 1))
    l1new_aa += einsum(l1.aa, (0, 1), x89, (1, 2), (0, 2)) * -1.0
    l2new_abab += einsum(x89, (0, 1), l2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x90 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x90 += einsum(t1.bb, (0, 1), v.bbbb.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    l1new_bb += einsum(l2.bbbb, (0, 1, 2, 3), x90, (3, 4, 1, 0), (4, 2)) * -2.0
    x91 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x91 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), (2, 3, 4, 5))
    l1new_bb += einsum(v.bbbb.ooov, (0, 1, 2, 3), x91, (4, 0, 2, 1), (3, 4)) * 2.0
    x92 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x92 += einsum(t1.bb, (0, 1), x67, (2, 3, 4, 1), (3, 2, 4, 0))
    l1new_bb += einsum(v.bbbb.ooov, (0, 1, 2, 3), x92, (4, 1, 0, 2), (3, 4)) * -2.0
    x93 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x93 += einsum(t1.aa, (0, 1), v.aabb.vvvv, (2, 1, 3, 4), (3, 4, 0, 2))
    l1new_bb += einsum(l2.abab, (0, 1, 2, 3), x93, (4, 1, 2, 0), (4, 3))
    x94 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x94 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    l1new_bb += einsum(x67, (0, 1, 2, 3), x94, (1, 2, 4, 3), (4, 0)) * 2.0
    x95 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x95 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x96 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x96 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x96 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x96 += einsum(x95, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x96 += einsum(x95, (0, 1, 2, 3), (2, 0, 1, 3))
    x97 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x97 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    x98 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x98 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x98 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x99 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x99 += einsum(t1.bb, (0, 1), x98, (0, 2, 1, 3), (2, 3))
    x100 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x100 += einsum(f.bb.ov, (0, 1), (0, 1))
    x100 += einsum(x97, (0, 1), (0, 1))
    x100 += einsum(x99, (0, 1), (0, 1)) * -1.0
    l1new_bb += einsum(x100, (0, 1), x70, (2, 0), (1, 2)) * -1.0
    l2new_abab += einsum(x100, (0, 1), x0, (2, 0, 3, 4), (4, 1, 3, 2)) * -1.0
    l2new_abab += einsum(l1.aa, (0, 1), x100, (2, 3), (0, 3, 1, 2))
    x101 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x101 += einsum(t1.aa, (0, 1), v.aabb.vvov, (2, 1, 3, 4), (3, 4, 0, 2))
    x102 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x102 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    x103 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.5
    x103 += einsum(t1.aa, (0, 1), v.aabb.vvoo, (2, 1, 3, 4), (3, 4, 0, 2)) * 0.5
    x103 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 2, 5, 3), (1, 5, 0, 4)) * 0.5
    x103 += einsum(t2.abab, (0, 1, 2, 3), x96, (1, 4, 5, 3), (4, 5, 0, 2)) * -0.5
    x103 += einsum(t2.aaaa, (0, 1, 2, 3), x12, (4, 5, 1, 3), (5, 4, 0, 2))
    x103 += einsum(t2.abab, (0, 1, 2, 3), x10, (4, 3, 0, 5), (1, 4, 5, 2)) * -0.5
    x103 += einsum(x100, (0, 1), t2.abab, (2, 3, 4, 1), (3, 0, 2, 4)) * 0.5
    x103 += einsum(t1.bb, (0, 1), x102, (2, 1, 3, 4), (0, 2, 3, 4)) * 0.5
    x103 += einsum(t1.aa, (0, 1), x23, (2, 3, 0, 4), (3, 2, 4, 1)) * -0.5
    l1new_bb += einsum(l2.abab, (0, 1, 2, 3), x103, (3, 4, 2, 0), (1, 4)) * -2.0
    x104 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x104 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x104 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x104 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x104 += einsum(x95, (0, 1, 2, 3), (0, 2, 1, 3))
    x105 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x105 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x105 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(x105, (0, 1, 2, 3), x35, (0, 4, 5, 2), (3, 4, 5, 1))
    l2new_abab += einsum(l1.bb, (0, 1), x105, (1, 2, 3, 4), (4, 0, 3, 2)) * -1.0
    x106 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x106 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x106 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x106 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x107 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x108 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x108 += einsum(t1.bb, (0, 1), x95, (2, 3, 4, 1), (0, 2, 3, 4))
    x109 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x109 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x110 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x110 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x110 += einsum(x107, (0, 1, 2, 3), (3, 1, 2, 0))
    x110 += einsum(x108, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x110 += einsum(x109, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x110 += einsum(x109, (0, 1, 2, 3), (3, 0, 2, 1))
    x111 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x111 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x111 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 2, 5, 3), (4, 0, 1, 5)) * -1.0
    x111 += einsum(t2.bbbb, (0, 1, 2, 3), x104, (4, 1, 5, 3), (5, 0, 4, 2)) * -2.0
    x111 += einsum(t2.abab, (0, 1, 2, 3), x105, (4, 5, 0, 2), (5, 1, 4, 3))
    x111 += einsum(x100, (0, 1), t2.bbbb, (2, 3, 4, 1), (0, 2, 3, 4))
    x111 += einsum(t1.bb, (0, 1), x106, (2, 3, 1, 4), (3, 2, 0, 4))
    x111 += einsum(t1.bb, (0, 1), x110, (0, 2, 3, 4), (3, 4, 2, 1))
    l1new_bb += einsum(l2.bbbb, (0, 1, 2, 3), x111, (4, 2, 3, 1), (0, 4)) * 2.0
    x112 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x112 += einsum(l2.abab, (0, 1, 2, 3), (3, 1, 2, 0))
    x112 += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 0, 4, 5)) * 2.0
    x112 += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 2, 5, 0), (3, 1, 4, 5)) * 2.0
    x112 += einsum(t1.aa, (0, 1), x35, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    l1new_bb += einsum(v.aabb.ovvv, (0, 1, 2, 3), x112, (4, 3, 0, 1), (2, 4))
    x113 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x113 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    l1new_bb += einsum(x64, (0, 1), x113, (2, 3, 1, 0), (3, 2)) * -1.0
    x114 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x114 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (2, 4, 0, 5))
    x114 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), (3, 4, 1, 5)) * 0.25
    l1new_bb += einsum(x113, (0, 1, 2, 3), x114, (4, 0, 3, 2), (1, 4)) * 4.0
    x115 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x115 += einsum(x71, (0, 1), (0, 1))
    x115 += einsum(x72, (0, 1), (0, 1)) * 0.5
    l1new_bb += einsum(f.bb.ov, (0, 1), x115, (2, 0), (1, 2)) * -2.0
    x116 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x116 += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), (1, 3, 2, 4))
    x116 += einsum(x0, (0, 1, 2, 3), (0, 1, 2, 3))
    x116 += einsum(t2.abab, (0, 1, 2, 3), x67, (4, 1, 5, 3), (4, 5, 0, 2)) * -2.0
    x116 += einsum(t2.aaaa, (0, 1, 2, 3), x0, (4, 5, 1, 3), (4, 5, 0, 2)) * 2.0
    x116 += einsum(t2.abab, (0, 1, 2, 3), x35, (4, 3, 0, 5), (4, 1, 5, 2)) * -1.0
    x116 += einsum(t1.aa, (0, 1), x38, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    x116 += einsum(t1.aa, (0, 1), x115, (2, 3), (2, 3, 0, 1)) * 2.0
    l1new_bb += einsum(v.aabb.ovov, (0, 1, 2, 3), x116, (4, 2, 0, 1), (3, 4)) * -1.0
    x117 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x117 += einsum(l2.bbbb, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x117 += einsum(t1.bb, (0, 1), x67, (2, 0, 3, 4), (2, 3, 4, 1))
    l1new_bb += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x117, (4, 0, 3, 1), (2, 4)) * -2.0
    x118 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x118 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), (3, 4, 0, 5))
    x118 += einsum(t1.aa, (0, 1), x0, (2, 3, 0, 4), (2, 3, 1, 4))
    l1new_bb += einsum(v.aabb.vvov, (0, 1, 2, 3), x118, (4, 2, 0, 1), (3, 4)) * -1.0
    x119 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x119 += einsum(t2.bbbb, (0, 1, 2, 3), x67, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x120 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x120 += einsum(t2.abab, (0, 1, 2, 3), x0, (4, 5, 0, 2), (4, 5, 1, 3))
    x121 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x121 += einsum(x91, (0, 1, 2, 3), (1, 0, 3, 2))
    x121 += einsum(x92, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new_bbbb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x121, (4, 5, 0, 2), (3, 1, 5, 4)) * 2.0
    x122 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x122 += einsum(x67, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x122 += einsum(x119, (0, 1, 2, 3), (2, 0, 1, 3)) * 2.0
    x122 += einsum(x120, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    x122 += einsum(t1.bb, (0, 1), x121, (0, 2, 3, 4), (4, 2, 3, 1))
    x122 += einsum(t1.bb, (0, 1), x115, (2, 3), (0, 2, 3, 1))
    l1new_bb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x122, (0, 4, 2, 1), (3, 4)) * -2.0
    x123 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x123 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 0), (1, 2, 3, 4))
    x123 += einsum(x119, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x123 += einsum(x120, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x123 += einsum(t1.bb, (0, 1), x115, (2, 3), (2, 0, 3, 1))
    l1new_bb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x123, (4, 0, 2, 3), (1, 4)) * 2.0
    x124 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x124 += einsum(t1.bb, (0, 1), (0, 1)) * -1.0
    x124 += einsum(x65, (0, 1), (0, 1)) * -2.0
    x124 += einsum(x66, (0, 1), (0, 1)) * -1.0
    x124 += einsum(x68, (0, 1), (0, 1)) * 2.0
    x124 += einsum(x69, (0, 1), (0, 1))
    x124 += einsum(t1.bb, (0, 1), x73, (0, 2), (2, 1))
    l1new_bb += einsum(x124, (0, 1), x98, (0, 2, 1, 3), (3, 2))
    x125 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x125 += einsum(x49, (0, 1), (0, 1)) * 0.5
    x125 += einsum(x50, (0, 1), (0, 1)) * 0.5
    x125 += einsum(x51, (0, 1), (0, 1))
    l1new_bb += einsum(x125, (0, 1), v.aabb.vvov, (0, 1, 2, 3), (3, 2)) * 2.0
    x126 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x126 += einsum(l1.aa, (0, 1), (1, 0)) * -0.5
    x126 += einsum(t1.aa, (0, 1), (0, 1)) * -0.5
    x126 += einsum(x53, (0, 1), (0, 1)) * -0.5
    x126 += einsum(x54, (0, 1), (0, 1)) * -1.0
    x126 += einsum(x55, (0, 1), (0, 1)) * 0.5
    x126 += einsum(x56, (0, 1), (0, 1))
    x126 += einsum(t1.aa, (0, 1), x58, (0, 2), (2, 1))
    l1new_bb += einsum(x126, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (3, 2)) * -2.0
    x127 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x127 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x127 += einsum(x37, (0, 1, 2, 3), (0, 1, 3, 2))
    l1new_bb += einsum(v.aabb.ooov, (0, 1, 2, 3), x127, (4, 2, 1, 0), (3, 4))
    x128 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x128 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x128 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    l1new_bb += einsum(x73, (0, 1), x128, (1, 0, 2, 3), (3, 2)) * -1.0
    x129 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x129 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x129 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l1new_bb += einsum(l1.bb, (0, 1), x129, (1, 2, 0, 3), (3, 2)) * -1.0
    x130 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x130 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 1, 2, 3), (2, 3))
    x131 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x131 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x131 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x132 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x132 += einsum(f.bb.vv, (0, 1), (0, 1))
    x132 += einsum(x130, (0, 1), (1, 0))
    x132 += einsum(t1.bb, (0, 1), x131, (0, 2, 1, 3), (3, 2)) * -1.0
    l1new_bb += einsum(l1.bb, (0, 1), x132, (0, 2), (2, 1))
    x133 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x133 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (0, 1, 2, 3), (2, 3))
    x134 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x134 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x135 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x135 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 3), (1, 4))
    x136 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x136 += einsum(t1.bb, (0, 1), x128, (0, 2, 3, 1), (2, 3))
    x137 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x137 += einsum(t1.bb, (0, 1), x100, (2, 1), (0, 2))
    x138 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x138 += einsum(f.bb.oo, (0, 1), (0, 1))
    x138 += einsum(x133, (0, 1), (1, 0))
    x138 += einsum(x134, (0, 1), (0, 1)) * 2.0
    x138 += einsum(x135, (0, 1), (0, 1))
    x138 += einsum(x136, (0, 1), (0, 1)) * -1.0
    x138 += einsum(x137, (0, 1), (0, 1))
    l1new_bb += einsum(l1.bb, (0, 1), x138, (1, 2), (0, 2)) * -1.0
    l2new_abab += einsum(x138, (0, 1), l2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    x139 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x139 += einsum(l1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 0), (1, 2, 3, 4))
    x140 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x140 += einsum(v.aabb.ovoo, (0, 1, 2, 3), x0, (2, 3, 4, 5), (4, 0, 5, 1))
    x141 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x141 += einsum(x0, (0, 1, 2, 3), x11, (0, 1, 4, 5), (2, 4, 3, 5))
    x142 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x142 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 4, 2, 5))
    x143 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x143 += einsum(t2.aaaa, (0, 1, 2, 3), x14, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x144 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x144 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x144 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x145 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x145 += einsum(t1.aa, (0, 1), x144, (2, 1, 3, 4), (2, 0, 3, 4))
    x146 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x146 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x146 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x146 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    x146 += einsum(x143, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x146 += einsum(x145, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x146, (2, 4, 0, 5), (5, 1, 4, 3))
    x147 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x147 += einsum(l2.aaaa, (0, 1, 2, 3), x146, (3, 4, 1, 5), (4, 2, 5, 0)) * 2.0
    x148 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x148 += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x149 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x149 += einsum(t2.bbbb, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 2, 4, 5))
    x150 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x150 += einsum(t2.abab, (0, 1, 2, 3), x14, (0, 4, 5, 2), (1, 3, 4, 5))
    x151 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x151 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x151 += einsum(x148, (0, 1, 2, 3), (0, 1, 2, 3))
    x151 += einsum(x149, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x151 += einsum(x150, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new_abab += einsum(l2.bbbb, (0, 1, 2, 3), x151, (3, 1, 4, 5), (5, 0, 4, 2)) * 2.0
    x152 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x152 += einsum(l2.abab, (0, 1, 2, 3), x151, (3, 1, 4, 5), (4, 2, 5, 0))
    x153 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x153 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3))
    x153 += einsum(x8, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x154 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x154 += einsum(x1, (0, 1, 2, 3), x153, (0, 4, 2, 5), (4, 1, 5, 3)) * 2.0
    x155 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x155 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x155 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x155, (0, 1, 2, 3), x35, (4, 5, 0, 1), (3, 5, 2, 4)) * -1.0
    x156 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x156 += einsum(x1, (0, 1, 2, 3), x155, (0, 2, 4, 5), (4, 1, 5, 3)) * 2.0
    x157 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x157 += einsum(x50, (0, 1), (0, 1))
    x157 += einsum(x51, (0, 1), (0, 1)) * 2.0
    l2new_abab += einsum(x157, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (0, 4, 2, 3)) * -1.0
    x158 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x158 += einsum(x157, (0, 1), v.aaaa.ovov, (2, 1, 3, 4), (2, 3, 0, 4))
    x159 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x159 += einsum(x58, (0, 1), v.aaaa.ovov, (2, 3, 1, 4), (2, 0, 4, 3)) * 2.0
    x160 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x160 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x160 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3))
    x161 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x161 += einsum(l1.aa, (0, 1), x160, (1, 2, 3, 4), (2, 3, 4, 0))
    x162 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x162 += einsum(x13, (0, 1), (0, 1))
    x162 += einsum(x15, (0, 1), (0, 1)) * -1.0
    x163 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x163 += einsum(f.aa.ov, (0, 1), l1.aa, (2, 3), (0, 3, 1, 2))
    x163 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x163 += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x163 += einsum(x141, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x163 += einsum(x147, (0, 1, 2, 3), (1, 0, 3, 2))
    x163 += einsum(x152, (0, 1, 2, 3), (1, 0, 3, 2))
    x163 += einsum(x154, (0, 1, 2, 3), (1, 0, 3, 2))
    x163 += einsum(x156, (0, 1, 2, 3), (1, 0, 3, 2))
    x163 += einsum(x158, (0, 1, 2, 3), (1, 0, 2, 3))
    x163 += einsum(x159, (0, 1, 2, 3), (1, 0, 3, 2))
    x163 += einsum(x161, (0, 1, 2, 3), (0, 1, 3, 2))
    x163 += einsum(l1.aa, (0, 1), x162, (2, 3), (1, 2, 0, 3))
    l2new_aaaa += einsum(x163, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new_aaaa += einsum(x163, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new_aaaa += einsum(x163, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new_aaaa += einsum(x163, (0, 1, 2, 3), (3, 2, 1, 0))
    x164 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x164 += einsum(f.aa.vv, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    x165 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x165 += einsum(f.aa.ov, (0, 1), x1, (2, 3, 0, 4), (2, 3, 1, 4))
    x166 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x166 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x1, (4, 5, 0, 3), (5, 4, 1, 2))
    x167 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x167 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x168 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x168 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x169 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x169 += einsum(t1.aa, (0, 1), x33, (0, 1, 2, 3), (2, 3))
    x170 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x170 += einsum(x80, (0, 1), (1, 0)) * -1.0
    x170 += einsum(x167, (0, 1), (1, 0))
    x170 += einsum(x168, (0, 1), (1, 0)) * 2.0
    x170 += einsum(x169, (0, 1), (1, 0)) * -1.0
    x171 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x171 += einsum(x170, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2)) * -2.0
    x172 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x172 += einsum(x162, (0, 1), x1, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x173 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x173 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x173 += einsum(x164, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x173 += einsum(x165, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x173 += einsum(x166, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x173 += einsum(x171, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x173 += einsum(x172, (0, 1, 2, 3), (1, 0, 2, 3))
    l2new_aaaa += einsum(x173, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_aaaa += einsum(x173, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x174 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x174 += einsum(f.aa.ov, (0, 1), t1.aa, (2, 1), (0, 2))
    x175 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x175 += einsum(x174, (0, 1), l2.aaaa, (2, 3, 4, 1), (0, 4, 2, 3))
    x176 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x176 += einsum(l2.aaaa, (0, 1, 2, 3), x29, (2, 4, 3, 5), (4, 5, 0, 1))
    x177 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x177 += einsum(t1.aa, (0, 1), x162, (2, 1), (2, 0))
    x178 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x178 += einsum(x83, (0, 1), (1, 0))
    x178 += einsum(x84, (0, 1), (0, 1))
    x178 += einsum(x85, (0, 1), (0, 1)) * 2.0
    x178 += einsum(x87, (0, 1), (1, 0)) * -1.0
    x178 += einsum(x177, (0, 1), (1, 0))
    x179 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x179 += einsum(x178, (0, 1), l2.aaaa, (2, 3, 4, 0), (1, 4, 2, 3)) * -2.0
    x180 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x180 += einsum(x175, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x180 += einsum(x176, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x180 += einsum(x179, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new_aaaa += einsum(x180, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_aaaa += einsum(x180, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x181 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x181 += einsum(f.aa.oo, (0, 1), l2.aaaa, (2, 3, 4, 1), (0, 4, 2, 3))
    l2new_aaaa += einsum(x181, (0, 1, 2, 3), (3, 2, 0, 1)) * -2.0
    l2new_aaaa += einsum(x181, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x182 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x182 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x182 += einsum(x27, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    x182 += einsum(x28, (0, 1, 2, 3), (0, 3, 1, 2))
    l2new_aaaa += einsum(l2.aaaa, (0, 1, 2, 3), x182, (2, 4, 3, 5), (0, 1, 4, 5)) * -2.0
    x183 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x183 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x184 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x184 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x184 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x185 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x185 += einsum(t2.bbbb, (0, 1, 2, 3), x184, (1, 4, 5, 3), (4, 0, 5, 2)) * 2.0
    x186 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x186 += einsum(t1.bb, (0, 1), x131, (2, 1, 3, 4), (2, 0, 3, 4))
    x187 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x187 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x187 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x187 += einsum(x183, (0, 1, 2, 3), (0, 1, 2, 3))
    x187 += einsum(x185, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x187 += einsum(x186, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x187, (3, 4, 1, 5), (0, 5, 2, 4))
    x188 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x188 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2))
    x189 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x189 += einsum(t2.abab, (0, 1, 2, 3), x98, (1, 4, 3, 5), (4, 5, 0, 2))
    x190 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x190 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x190 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    x190 += einsum(x188, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x190 += einsum(x189, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new_abab += einsum(l2.aaaa, (0, 1, 2, 3), x190, (4, 5, 3, 1), (0, 5, 2, 4)) * 2.0
    x191 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x191 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x191 += einsum(x17, (0, 1, 2, 3), (1, 0, 2, 3))
    x191 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 5), (3, 5, 0, 4)) * -1.0
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x191, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x192 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x192 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x192 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 4, 1), (0, 4, 2, 3))
    x192 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 5, 3), (1, 5, 2, 4)) * -1.0
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x192, (3, 4, 0, 5), (5, 1, 2, 4)) * -1.0
    x193 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x193 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x193 += einsum(x19, (0, 1, 2, 3), (1, 0, 2, 3))
    x193 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    x193 += einsum(t1.bb, (0, 1), x10, (2, 1, 3, 4), (0, 2, 4, 3))
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x193, (3, 4, 2, 5), (0, 1, 5, 4))
    x194 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x194 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x194 += einsum(x80, (0, 1), (1, 0)) * -1.0
    x194 += einsum(x167, (0, 1), (0, 1))
    x194 += einsum(x168, (0, 1), (0, 1)) * 2.0
    x194 += einsum(t1.aa, (0, 1), x81, (0, 2, 1, 3), (3, 2)) * -1.0
    l2new_abab += einsum(x194, (0, 1), l2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x195 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x195 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 4, 1, 3), (2, 4))
    x196 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x196 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x197 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x197 += einsum(f.bb.vv, (0, 1), (0, 1)) * -1.0
    x197 += einsum(x130, (0, 1), (1, 0)) * -1.0
    x197 += einsum(x195, (0, 1), (0, 1)) * 2.0
    x197 += einsum(x196, (0, 1), (0, 1))
    x197 += einsum(t1.bb, (0, 1), x131, (0, 1, 2, 3), (3, 2)) * -1.0
    l2new_abab += einsum(x197, (0, 1), l2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    x198 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x198 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x198 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x0, (0, 1, 2, 3), x198, (0, 1, 4, 5), (3, 5, 2, 4)) * -1.0
    x199 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x199 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3))
    x199 += einsum(x95, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x0, (0, 1, 2, 3), x199, (0, 4, 1, 5), (3, 5, 2, 4)) * -1.0
    x200 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x200 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x200 += einsum(x8, (0, 1, 2, 3), (0, 2, 1, 3))
    l2new_abab += einsum(x200, (0, 1, 2, 3), x35, (4, 5, 0, 1), (3, 5, 2, 4)) * -1.0
    x201 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x201 += einsum(x62, (0, 1), (0, 1))
    x201 += einsum(x63, (0, 1), (0, 1)) * 0.5
    l2new_abab += einsum(x201, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (3, 0, 2, 4)) * -2.0
    x202 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x202 += einsum(f.bb.vv, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    x203 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x203 += einsum(f.bb.ov, (0, 1), x67, (2, 3, 0, 4), (2, 3, 1, 4))
    x204 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x204 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x67, (4, 5, 0, 3), (5, 4, 1, 2))
    x205 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x205 += einsum(t1.bb, (0, 1), x113, (0, 2, 1, 3), (2, 3))
    x206 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x206 += einsum(x130, (0, 1), (1, 0)) * -1.0
    x206 += einsum(x195, (0, 1), (1, 0)) * 2.0
    x206 += einsum(x196, (0, 1), (1, 0))
    x206 += einsum(x205, (0, 1), (0, 1)) * -1.0
    x207 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x207 += einsum(x206, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2)) * -2.0
    x208 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x208 += einsum(x97, (0, 1), (0, 1))
    x208 += einsum(x99, (0, 1), (0, 1)) * -1.0
    x209 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x209 += einsum(x208, (0, 1), x67, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x210 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x210 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x210 += einsum(x202, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x210 += einsum(x203, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x210 += einsum(x204, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x210 += einsum(x207, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x210 += einsum(x209, (0, 1, 2, 3), (1, 0, 2, 3))
    l2new_bbbb += einsum(x210, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_bbbb += einsum(x210, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x211 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x211 += einsum(l1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 0), (1, 2, 3, 4))
    x212 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x212 += einsum(v.aabb.ooov, (0, 1, 2, 3), x35, (4, 5, 0, 1), (4, 2, 5, 3))
    x213 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x213 += einsum(x35, (0, 1, 2, 3), x7, (4, 5, 2, 3), (0, 4, 1, 5))
    x214 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x214 += einsum(l2.bbbb, (0, 1, 2, 3), x187, (3, 4, 1, 5), (4, 2, 5, 0)) * 2.0
    x215 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x215 += einsum(l2.abab, (0, 1, 2, 3), x190, (4, 5, 2, 0), (4, 3, 5, 1))
    x216 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x216 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x216 += einsum(x95, (0, 1, 2, 3), (0, 2, 1, 3))
    x217 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x217 += einsum(x216, (0, 1, 2, 3), x67, (0, 4, 1, 5), (2, 4, 3, 5)) * 2.0
    x218 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x218 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x218 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x219 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x219 += einsum(x218, (0, 1, 2, 3), x67, (0, 4, 2, 5), (1, 4, 3, 5)) * 2.0
    x220 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x220 += einsum(x201, (0, 1), v.bbbb.ovov, (2, 1, 3, 4), (2, 3, 0, 4)) * 2.0
    x221 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x221 += einsum(x73, (0, 1), v.bbbb.ovov, (2, 3, 1, 4), (2, 0, 4, 3))
    x222 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x222 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x222 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3))
    x223 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x223 += einsum(l1.bb, (0, 1), x222, (1, 2, 3, 4), (2, 3, 4, 0))
    x224 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x224 += einsum(f.bb.ov, (0, 1), l1.bb, (2, 3), (0, 3, 1, 2))
    x224 += einsum(x211, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x224 += einsum(x212, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x224 += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x224 += einsum(x214, (0, 1, 2, 3), (1, 0, 3, 2))
    x224 += einsum(x215, (0, 1, 2, 3), (1, 0, 3, 2))
    x224 += einsum(x217, (0, 1, 2, 3), (1, 0, 3, 2))
    x224 += einsum(x219, (0, 1, 2, 3), (1, 0, 3, 2))
    x224 += einsum(x220, (0, 1, 2, 3), (1, 0, 2, 3))
    x224 += einsum(x221, (0, 1, 2, 3), (1, 0, 3, 2))
    x224 += einsum(x223, (0, 1, 2, 3), (0, 1, 3, 2))
    x224 += einsum(l1.bb, (0, 1), x208, (2, 3), (1, 2, 0, 3))
    l2new_bbbb += einsum(x224, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new_bbbb += einsum(x224, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new_bbbb += einsum(x224, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new_bbbb += einsum(x224, (0, 1, 2, 3), (3, 2, 1, 0))
    x225 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x225 += einsum(f.bb.ov, (0, 1), t1.bb, (2, 1), (0, 2))
    x226 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x226 += einsum(x225, (0, 1), l2.bbbb, (2, 3, 4, 1), (0, 4, 2, 3))
    x227 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x227 += einsum(l2.bbbb, (0, 1, 2, 3), x109, (2, 3, 4, 5), (4, 5, 0, 1))
    x228 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x228 += einsum(t1.bb, (0, 1), x208, (2, 1), (2, 0))
    x229 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x229 += einsum(x133, (0, 1), (1, 0))
    x229 += einsum(x134, (0, 1), (0, 1)) * 2.0
    x229 += einsum(x135, (0, 1), (0, 1))
    x229 += einsum(x136, (0, 1), (0, 1)) * -1.0
    x229 += einsum(x228, (0, 1), (1, 0))
    x230 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x230 += einsum(x229, (0, 1), l2.bbbb, (2, 3, 4, 0), (1, 4, 2, 3)) * -2.0
    x231 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x231 += einsum(x226, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x231 += einsum(x227, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x231 += einsum(x230, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new_bbbb += einsum(x231, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_bbbb += einsum(x231, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x232 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x232 += einsum(f.bb.oo, (0, 1), l2.bbbb, (2, 3, 4, 1), (0, 4, 2, 3))
    l2new_bbbb += einsum(x232, (0, 1, 2, 3), (3, 2, 0, 1)) * -2.0
    l2new_bbbb += einsum(x232, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x233 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x233 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x233 += einsum(x107, (0, 1, 2, 3), (1, 3, 2, 0))
    x233 += einsum(x108, (0, 1, 2, 3), (0, 2, 3, 1))
    l2new_bbbb += einsum(l2.bbbb, (0, 1, 2, 3), x233, (2, 4, 5, 3), (0, 1, 5, 4)) * -2.0

    l1new.aa = l1new_aa
    l1new.bb = l1new_bb
    l2new.aaaa = l2new_aaaa
    l2new.abab = l2new_abab
    l2new.bbbb = l2new_bbbb

    return {"l1new": l1new, "l2new": l2new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    rdm1_f = Namespace()

    delta = Namespace(aa=Namespace(), bb=Namespace())
    delta.aa = Namespace(oo=np.eye(nocc[0]), vv=np.eye(nvir[0]))
    delta.bb = Namespace(oo=np.eye(nocc[1]), vv=np.eye(nvir[1]))

    # RDM1
    rdm1_f_aa_oo = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    rdm1_f_aa_oo += einsum(delta.aa.oo, (0, 1), (0, 1))
    rdm1_f_bb_oo = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    rdm1_f_bb_oo += einsum(delta.bb.oo, (0, 1), (0, 1))
    rdm1_f_aa_ov = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    rdm1_f_aa_ov += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), (2, 3))
    rdm1_f_aa_ov += einsum(t1.aa, (0, 1), (0, 1))
    rdm1_f_aa_ov += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 0), (2, 3)) * 2.0
    rdm1_f_bb_ov = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    rdm1_f_bb_ov += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 0), (2, 3)) * 2.0
    rdm1_f_bb_ov += einsum(t1.bb, (0, 1), (0, 1))
    rdm1_f_bb_ov += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), (2, 3))
    rdm1_f_aa_vo = np.zeros((nvir[0], nocc[0]), dtype=np.float64)
    rdm1_f_aa_vo += einsum(l1.aa, (0, 1), (0, 1))
    rdm1_f_bb_vo = np.zeros((nvir[1], nocc[1]), dtype=np.float64)
    rdm1_f_bb_vo += einsum(l1.bb, (0, 1), (0, 1))
    rdm1_f_aa_vv = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    rdm1_f_aa_vv += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 1), (0, 4)) * 2.0
    rdm1_f_aa_vv += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), (0, 4))
    rdm1_f_aa_vv += einsum(l1.aa, (0, 1), t1.aa, (1, 2), (0, 2))
    rdm1_f_bb_vv = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    rdm1_f_bb_vv += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 1), (0, 4)) * 2.0
    rdm1_f_bb_vv += einsum(l1.bb, (0, 1), t1.bb, (1, 2), (0, 2))
    rdm1_f_bb_vv += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), (1, 4))
    x0 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x0 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), (2, 4))
    rdm1_f_aa_oo += einsum(x0, (0, 1), (1, 0)) * -1.0
    x1 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x1 += einsum(l1.aa, (0, 1), t1.aa, (2, 0), (1, 2))
    rdm1_f_aa_oo += einsum(x1, (0, 1), (1, 0)) * -1.0
    x2 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 0, 1), (2, 4))
    rdm1_f_aa_oo += einsum(x2, (0, 1), (1, 0)) * -2.0
    x3 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x3 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 0, 1), (2, 4))
    rdm1_f_bb_oo += einsum(x3, (0, 1), (1, 0)) * -2.0
    x4 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x4 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), (3, 4))
    rdm1_f_bb_oo += einsum(x4, (0, 1), (1, 0)) * -1.0
    x5 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x5 += einsum(l1.bb, (0, 1), t1.bb, (2, 0), (1, 2))
    rdm1_f_bb_oo += einsum(x5, (0, 1), (1, 0)) * -1.0
    x6 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x6 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm1_f_aa_ov += einsum(t2.aaaa, (0, 1, 2, 3), x6, (0, 1, 4, 3), (4, 2)) * 2.0
    x7 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x7 += einsum(t1.aa, (0, 1), l2.abab, (1, 2, 3, 4), (4, 2, 3, 0))
    rdm1_f_aa_ov += einsum(t2.abab, (0, 1, 2, 3), x7, (1, 3, 0, 4), (4, 2)) * -1.0
    x8 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x8 += einsum(x1, (0, 1), (0, 1))
    x8 += einsum(x0, (0, 1), (0, 1))
    x8 += einsum(x2, (0, 1), (0, 1)) * 2.0
    rdm1_f_aa_ov += einsum(t1.aa, (0, 1), x8, (0, 2), (2, 1)) * -1.0
    x9 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x9 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm1_f_bb_ov += einsum(t2.bbbb, (0, 1, 2, 3), x9, (1, 0, 4, 3), (4, 2)) * -2.0
    x10 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x10 += einsum(t1.bb, (0, 1), l2.abab, (2, 1, 3, 4), (4, 0, 3, 2))
    rdm1_f_bb_ov += einsum(t2.abab, (0, 1, 2, 3), x10, (1, 4, 0, 2), (4, 3)) * -1.0
    x11 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x11 += einsum(x5, (0, 1), (0, 1))
    x11 += einsum(x3, (0, 1), (0, 1)) * 2.0
    x11 += einsum(x4, (0, 1), (0, 1))
    rdm1_f_bb_ov += einsum(t1.bb, (0, 1), x11, (0, 2), (2, 1)) * -1.0

    rdm1_f_aa = np.block([[rdm1_f_aa_oo, rdm1_f_aa_ov], [rdm1_f_aa_vo, rdm1_f_aa_vv]])
    rdm1_f_bb = np.block([[rdm1_f_bb_oo, rdm1_f_bb_ov], [rdm1_f_bb_vo, rdm1_f_bb_vv]])

    rdm1_f.aa = rdm1_f_aa
    rdm1_f.bb = rdm1_f_bb

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    rdm2_f = Namespace()

    delta = Namespace(aa=Namespace(), bb=Namespace())
    delta.aa = Namespace(oo=np.eye(nocc[0]), vv=np.eye(nvir[0]))
    delta.bb = Namespace(oo=np.eye(nocc[1]), vv=np.eye(nvir[1]))

    # RDM2
    rdm2_f_aaaa_oooo = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), delta.aa.oo, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), delta.aa.oo, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_bbbb_oooo = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), delta.bb.oo, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), delta.bb.oo, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_aaaa_ovoo = np.zeros((nocc[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_ovoo += einsum(delta.aa.oo, (0, 1), l1.aa, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_ovoo += einsum(delta.aa.oo, (0, 1), l1.aa, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_abab_ovoo = np.zeros((nocc[0], nvir[1], nocc[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_ovoo += einsum(delta.aa.oo, (0, 1), l1.bb, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ovoo = np.zeros((nocc[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_ovoo += einsum(delta.bb.oo, (0, 1), l1.bb, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ovoo += einsum(delta.bb.oo, (0, 1), l1.bb, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_aaaa_vooo = np.zeros((nvir[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_vooo += einsum(delta.aa.oo, (0, 1), l1.aa, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_aaaa_vooo += einsum(delta.aa.oo, (0, 1), l1.aa, (2, 3), (2, 0, 3, 1))
    rdm2_f_abab_vooo = np.zeros((nvir[0], nocc[1], nocc[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_vooo += einsum(delta.bb.oo, (0, 1), l1.aa, (2, 3), (2, 0, 3, 1))
    rdm2_f_bbbb_vooo = np.zeros((nvir[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_vooo += einsum(delta.bb.oo, (0, 1), l1.bb, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_bbbb_vooo += einsum(delta.bb.oo, (0, 1), l1.bb, (2, 3), (2, 0, 3, 1))
    rdm2_f_aaaa_oovv = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_oovv += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_abab_oovv = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_oovv = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_oovv += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_bbbb_oovv += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_bbbb_oovv += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_ovov = np.zeros((nocc[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_ovov += einsum(l1.aa, (0, 1), t1.aa, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_bbbb_ovov = np.zeros((nocc[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_ovov += einsum(l1.bb, (0, 1), t1.bb, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_aaaa_ovvo = np.zeros((nocc[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_ovvo += einsum(l1.aa, (0, 1), t1.aa, (2, 3), (2, 0, 3, 1))
    rdm2_f_abab_ovvo = np.zeros((nocc[0], nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_ovvo += einsum(l1.bb, (0, 1), t1.aa, (2, 3), (2, 0, 3, 1))
    rdm2_f_bbbb_ovvo = np.zeros((nocc[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_ovvo += einsum(l1.bb, (0, 1), t1.bb, (2, 3), (2, 0, 3, 1))
    rdm2_f_aaaa_voov = np.zeros((nvir[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_voov += einsum(l1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    rdm2_f_abab_voov = np.zeros((nvir[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_voov += einsum(l1.aa, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_voov = np.zeros((nvir[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_voov += einsum(l1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_vovo = np.zeros((nvir[0], nocc[0], nvir[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_vovo += einsum(l1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_bbbb_vovo = np.zeros((nvir[1], nocc[1], nvir[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_vovo += einsum(l1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_aaaa_vvoo = np.zeros((nvir[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_vvoo += einsum(l2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_abab_vvoo = np.zeros((nvir[0], nvir[1], nocc[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_vvoo += einsum(l2.abab, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_vvoo = np.zeros((nvir[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_vvoo += einsum(l2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_abab_ovvv = np.zeros((nocc[0], nvir[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_ovvv += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_abab_vovv = np.zeros((nvir[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_vovv += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), (0, 2, 3, 4))
    rdm2_f_abab_vvov = np.zeros((nvir[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_vvov += einsum(t1.bb, (0, 1), l2.abab, (2, 3, 4, 0), (2, 3, 4, 1))
    rdm2_f_aaaa_vvvv = np.zeros((nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_vvvv += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), (0, 1, 4, 5)) * 2.0
    rdm2_f_abab_vvvv = np.zeros((nvir[0], nvir[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_vvvv += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), (0, 1, 4, 5))
    rdm2_f_bbbb_vvvv = np.zeros((nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_vvvv += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), (0, 1, 4, 5)) * 2.0
    x0 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x0 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_aaaa_oooo += einsum(x0, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x1 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x1 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_aaaa_ovoo += einsum(x1, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    rdm2_f_aaaa_vooo += einsum(x1, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(t1.aa, (0, 1), x1, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_aaaa_oooo += einsum(x2, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x3 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x3 += einsum(l1.aa, (0, 1), t1.aa, (2, 0), (1, 2))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x3, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x3, (2, 3), (3, 0, 1, 2))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x3, (2, 3), (0, 3, 2, 1))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x3, (2, 3), (3, 0, 2, 1)) * -1.0
    x4 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x4 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), (2, 4))
    x5 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x5 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 0, 1), (2, 4))
    x6 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x6 += einsum(x4, (0, 1), (0, 1))
    x6 += einsum(x5, (0, 1), (0, 1)) * 2.0
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x6, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x6, (2, 3), (0, 3, 2, 1))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x6, (2, 3), (3, 0, 1, 2))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x6, (2, 3), (3, 0, 2, 1)) * -1.0
    x7 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x7 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), (3, 5, 2, 4))
    rdm2_f_abab_oooo = np.zeros((nocc[0], nocc[1], nocc[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_oooo += einsum(x7, (0, 1, 2, 3), (3, 1, 2, 0))
    x8 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x8 += einsum(t1.aa, (0, 1), l2.abab, (1, 2, 3, 4), (4, 2, 3, 0))
    rdm2_f_abab_ovoo += einsum(x8, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_abab_ovov = np.zeros((nocc[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_ovov += einsum(t1.bb, (0, 1), x8, (0, 2, 3, 4), (4, 2, 3, 1)) * -1.0
    rdm2_f_abab_ovvv += einsum(t2.abab, (0, 1, 2, 3), x8, (1, 4, 0, 5), (5, 4, 2, 3)) * -1.0
    x9 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x9 += einsum(t1.bb, (0, 1), x8, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_abab_oooo += einsum(x9, (0, 1, 2, 3), (3, 1, 2, 0))
    x10 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x10 += einsum(delta.aa.oo, (0, 1), (0, 1)) * -0.5
    x10 += einsum(x3, (0, 1), (0, 1)) * 0.5
    x10 += einsum(x4, (0, 1), (0, 1)) * 0.5
    x10 += einsum(x5, (0, 1), (0, 1))
    rdm2_f_abab_oooo += einsum(delta.bb.oo, (0, 1), x10, (2, 3), (3, 0, 2, 1)) * -2.0
    x11 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x11 += einsum(l1.bb, (0, 1), t1.bb, (2, 0), (1, 2))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x11, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x11, (2, 3), (3, 0, 1, 2))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x11, (2, 3), (0, 3, 2, 1))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x11, (2, 3), (3, 0, 2, 1)) * -1.0
    x12 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x12 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 0, 1), (2, 4))
    x13 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x13 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), (3, 4))
    x14 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x14 += einsum(x11, (0, 1), (0, 1))
    x14 += einsum(x12, (0, 1), (0, 1)) * 2.0
    x14 += einsum(x13, (0, 1), (0, 1))
    rdm2_f_abab_oooo += einsum(delta.aa.oo, (0, 1), x14, (2, 3), (0, 3, 1, 2)) * -1.0
    x15 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x15 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_bbbb_oooo += einsum(x15, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x16 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x16 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_bbbb_ovoo += einsum(x16, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    rdm2_f_bbbb_vooo += einsum(x16, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x17 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x17 += einsum(t1.bb, (0, 1), x16, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_bbbb_oooo += einsum(x17, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x18 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x18 += einsum(x12, (0, 1), (0, 1))
    x18 += einsum(x13, (0, 1), (0, 1)) * 0.5
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x18, (2, 3), (0, 3, 1, 2)) * -2.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x18, (2, 3), (0, 3, 2, 1)) * 2.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x18, (2, 3), (3, 0, 1, 2)) * 2.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x18, (2, 3), (3, 0, 2, 1)) * -2.0
    x19 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x19 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_aaaa_ooov = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_ooov += einsum(x19, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_aaaa_oovo = np.zeros((nocc[0], nocc[0], nvir[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_oovo += einsum(x19, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x20 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x20 += einsum(t2.abab, (0, 1, 2, 3), x8, (1, 3, 4, 5), (4, 5, 0, 2))
    x21 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x21 += einsum(t2.aaaa, (0, 1, 2, 3), x1, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x22 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x22 += einsum(x3, (0, 1), (0, 1)) * 0.5
    x22 += einsum(x4, (0, 1), (0, 1)) * 0.5
    x22 += einsum(x5, (0, 1), (0, 1))
    x23 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x23 += einsum(delta.aa.oo, (0, 1), t1.aa, (2, 3), (0, 1, 2, 3))
    x23 += einsum(x20, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x23 += einsum(x21, (0, 1, 2, 3), (1, 0, 2, 3)) * -4.0
    x23 += einsum(t1.aa, (0, 1), x22, (2, 3), (0, 2, 3, 1)) * 2.0
    rdm2_f_aaaa_ooov += einsum(x23, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_ooov += einsum(x23, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_aaaa_oovo += einsum(x23, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_aaaa_oovo += einsum(x23, (0, 1, 2, 3), (2, 0, 3, 1))
    x24 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x24 += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), (2, 3))
    x25 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x25 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 0), (2, 3))
    x26 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x26 += einsum(t2.abab, (0, 1, 2, 3), x8, (1, 3, 0, 4), (4, 2))
    x27 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x27 += einsum(t2.aaaa, (0, 1, 2, 3), x1, (0, 1, 4, 3), (4, 2)) * -1.0
    x28 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x28 += einsum(t1.aa, (0, 1), x22, (0, 2), (2, 1)) * 2.0
    x29 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x29 += einsum(x24, (0, 1), (0, 1)) * -1.0
    x29 += einsum(x25, (0, 1), (0, 1)) * -2.0
    x29 += einsum(x26, (0, 1), (0, 1))
    x29 += einsum(x27, (0, 1), (0, 1)) * 2.0
    x29 += einsum(x28, (0, 1), (0, 1))
    rdm2_f_aaaa_ooov += einsum(delta.aa.oo, (0, 1), x29, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_aaaa_ooov += einsum(delta.aa.oo, (0, 1), x29, (2, 3), (2, 0, 1, 3))
    rdm2_f_aaaa_oovo += einsum(delta.aa.oo, (0, 1), x29, (2, 3), (0, 2, 3, 1))
    rdm2_f_aaaa_oovo += einsum(delta.aa.oo, (0, 1), x29, (2, 3), (2, 0, 3, 1)) * -1.0
    rdm2_f_abab_oovo = np.zeros((nocc[0], nocc[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_oovo += einsum(delta.bb.oo, (0, 1), x29, (2, 3), (2, 0, 3, 1)) * -1.0
    x30 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x30 += einsum(x0, (0, 1, 2, 3), (1, 0, 3, 2))
    x30 += einsum(x2, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_oovv += einsum(t2.aaaa, (0, 1, 2, 3), x30, (0, 1, 4, 5), (5, 4, 2, 3)) * -2.0
    x31 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x31 += einsum(t1.aa, (0, 1), x30, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_aaaa_ooov += einsum(x31, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_aaaa_oovo += einsum(x31, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x32 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x32 += einsum(t2.abab, (0, 1, 2, 3), x1, (4, 0, 5, 2), (1, 3, 4, 5)) * -1.0
    rdm2_f_abab_ooov = np.zeros((nocc[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_ooov += einsum(x32, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x33 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x33 += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), (3, 4, 1, 2))
    rdm2_f_abab_ooov += einsum(x33, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x34 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x34 += einsum(t1.bb, (0, 1), l2.abab, (2, 1, 3, 4), (4, 0, 3, 2))
    rdm2_f_abab_vooo += einsum(x34, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    rdm2_f_abab_vovo = np.zeros((nvir[0], nocc[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_vovo += einsum(t1.aa, (0, 1), x34, (2, 3, 0, 4), (4, 3, 1, 2)) * -1.0
    rdm2_f_abab_vovv += einsum(t2.abab, (0, 1, 2, 3), x34, (1, 4, 0, 5), (5, 4, 2, 3)) * -1.0
    x35 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x35 += einsum(t2.abab, (0, 1, 2, 3), x34, (1, 4, 5, 2), (4, 3, 5, 0))
    rdm2_f_abab_ooov += einsum(x35, (0, 1, 2, 3), (3, 0, 2, 1))
    x36 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x36 += einsum(t2.bbbb, (0, 1, 2, 3), x8, (1, 3, 4, 5), (0, 2, 4, 5))
    rdm2_f_abab_ooov += einsum(x36, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x37 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x37 += einsum(x7, (0, 1, 2, 3), (0, 1, 2, 3))
    x37 += einsum(x9, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_ooov += einsum(t1.bb, (0, 1), x37, (0, 2, 3, 4), (4, 2, 3, 1))
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x37, (1, 4, 0, 5), (5, 4, 2, 3))
    x38 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x38 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 0), (2, 3))
    x39 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x39 += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), (2, 3))
    x40 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x40 += einsum(t2.bbbb, (0, 1, 2, 3), x16, (0, 1, 4, 3), (4, 2)) * -1.0
    x41 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x41 += einsum(t2.abab, (0, 1, 2, 3), x34, (1, 4, 0, 2), (4, 3))
    x42 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x42 += einsum(t1.bb, (0, 1), x14, (0, 2), (2, 1)) * 0.5
    x43 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x43 += einsum(t1.bb, (0, 1), (0, 1)) * -0.5
    x43 += einsum(x38, (0, 1), (0, 1)) * -1.0
    x43 += einsum(x39, (0, 1), (0, 1)) * -0.5
    x43 += einsum(x40, (0, 1), (0, 1))
    x43 += einsum(x41, (0, 1), (0, 1)) * 0.5
    x43 += einsum(x42, (0, 1), (0, 1))
    rdm2_f_abab_ooov += einsum(delta.aa.oo, (0, 1), x43, (2, 3), (0, 2, 1, 3)) * -2.0
    x44 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x44 += einsum(x3, (0, 1), (0, 1))
    x44 += einsum(x4, (0, 1), (0, 1))
    x44 += einsum(x5, (0, 1), (0, 1)) * 2.0
    rdm2_f_abab_ooov += einsum(t1.bb, (0, 1), x44, (2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_abab_oovv += einsum(x44, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x45 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x45 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_bbbb_ooov = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_ooov += einsum(x45, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_bbbb_oovo = np.zeros((nocc[1], nocc[1], nvir[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_oovo += einsum(x45, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x46 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x46 += einsum(t2.bbbb, (0, 1, 2, 3), x16, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x47 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x47 += einsum(t2.abab, (0, 1, 2, 3), x34, (4, 5, 0, 2), (4, 5, 1, 3))
    x48 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x48 += einsum(delta.bb.oo, (0, 1), t1.bb, (2, 3), (0, 1, 2, 3))
    x48 += einsum(x46, (0, 1, 2, 3), (1, 0, 2, 3)) * -4.0
    x48 += einsum(x47, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x48 += einsum(t1.bb, (0, 1), x14, (2, 3), (0, 2, 3, 1))
    rdm2_f_bbbb_ooov += einsum(x48, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ooov += einsum(x48, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_bbbb_oovo += einsum(x48, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_bbbb_oovo += einsum(x48, (0, 1, 2, 3), (2, 0, 3, 1))
    x49 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x49 += einsum(x38, (0, 1), (0, 1)) * -1.0
    x49 += einsum(x39, (0, 1), (0, 1)) * -0.5
    x49 += einsum(x40, (0, 1), (0, 1))
    x49 += einsum(x41, (0, 1), (0, 1)) * 0.5
    x49 += einsum(x42, (0, 1), (0, 1))
    rdm2_f_bbbb_ooov += einsum(delta.bb.oo, (0, 1), x49, (2, 3), (0, 2, 1, 3)) * -2.0
    rdm2_f_bbbb_ooov += einsum(delta.bb.oo, (0, 1), x49, (2, 3), (2, 0, 1, 3)) * 2.0
    rdm2_f_bbbb_oovo += einsum(delta.bb.oo, (0, 1), x49, (2, 3), (0, 2, 3, 1)) * 2.0
    rdm2_f_bbbb_oovo += einsum(delta.bb.oo, (0, 1), x49, (2, 3), (2, 0, 3, 1)) * -2.0
    rdm2_f_abab_oovv += einsum(t1.aa, (0, 1), x49, (2, 3), (0, 2, 1, 3)) * -2.0
    x50 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x50 += einsum(x15, (0, 1, 2, 3), (1, 0, 3, 2))
    x50 += einsum(x17, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_bbbb_oovv += einsum(t2.bbbb, (0, 1, 2, 3), x50, (0, 1, 4, 5), (5, 4, 2, 3)) * -2.0
    x51 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x51 += einsum(t1.bb, (0, 1), x50, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_bbbb_ooov += einsum(x51, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_bbbb_oovo += einsum(x51, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x52 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x52 += einsum(t2.abab, (0, 1, 2, 3), x8, (4, 3, 0, 5), (4, 1, 5, 2))
    rdm2_f_abab_oovo += einsum(x52, (0, 1, 2, 3), (2, 1, 3, 0))
    x53 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(t2.aaaa, (0, 1, 2, 3), x34, (4, 5, 1, 3), (4, 5, 0, 2))
    rdm2_f_abab_oovo += einsum(x53, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x54 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), (1, 3, 2, 4))
    rdm2_f_abab_oovo += einsum(x54, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x55 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x55 += einsum(t2.abab, (0, 1, 2, 3), x16, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    rdm2_f_abab_oovo += einsum(x55, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x56 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x56 += einsum(t1.aa, (0, 1), x37, (2, 3, 0, 4), (2, 3, 4, 1))
    rdm2_f_abab_oovo += einsum(x56, (0, 1, 2, 3), (2, 1, 3, 0))
    x57 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x57 += einsum(delta.bb.oo, (0, 1), (0, 1)) * -1.0
    x57 += einsum(x11, (0, 1), (0, 1))
    x57 += einsum(x12, (0, 1), (0, 1)) * 2.0
    x57 += einsum(x13, (0, 1), (0, 1))
    rdm2_f_abab_oovo += einsum(t1.aa, (0, 1), x57, (2, 3), (0, 3, 1, 2)) * -1.0
    x58 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x58 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_aaaa_ovov += einsum(x58, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_aaaa_ovvo += einsum(x58, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_aaaa_voov += einsum(x58, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_aaaa_vovo += einsum(x58, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x59 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x59 += einsum(t2.aaaa, (0, 1, 2, 3), x58, (1, 4, 3, 5), (4, 0, 5, 2))
    x60 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x60 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    x60 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x61 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x61 += einsum(t1.aa, (0, 1), x60, (0, 2, 3, 4), (2, 3, 1, 4))
    x62 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x62 += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x62 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3))
    x62 += einsum(t1.aa, (0, 1), x29, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_oovv += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x62, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_aaaa_oovv += einsum(x62, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_aaaa_oovv += einsum(x62, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x63 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum(x3, (0, 1), t2.aaaa, (2, 0, 3, 4), (1, 2, 3, 4))
    x64 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x64 += einsum(x6, (0, 1), t2.aaaa, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x65 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x65 += einsum(x63, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x65 += einsum(x64, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_aaaa_oovv += einsum(x65, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x65, (0, 1, 2, 3), (1, 0, 2, 3))
    x66 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x66 += einsum(t1.aa, (0, 1), x19, (0, 2, 3, 4), (2, 3, 1, 4))
    x67 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x67 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_aaaa_ovov += einsum(x67, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    rdm2_f_aaaa_ovvo += einsum(x67, (0, 1, 2, 3), (1, 2, 3, 0)) * 4.0
    rdm2_f_aaaa_voov += einsum(x67, (0, 1, 2, 3), (2, 1, 0, 3)) * 4.0
    rdm2_f_aaaa_vovo += einsum(x67, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x68 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum(t2.aaaa, (0, 1, 2, 3), x67, (1, 4, 3, 5), (0, 4, 2, 5))
    x69 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x69 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), (0, 4))
    x70 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 1), (0, 4))
    x71 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum(x69, (0, 1), (0, 1))
    x71 += einsum(x70, (0, 1), (0, 1)) * 2.0
    x72 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x72 += einsum(x71, (0, 1), t2.aaaa, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x73 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x73 += einsum(x66, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x73 += einsum(x68, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x73 += einsum(x72, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_aaaa_oovv += einsum(x73, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x74 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x74 += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 0, 4, 5))
    rdm2_f_abab_ovvo += einsum(x74, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x75 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x75 += einsum(t2.abab, (0, 1, 2, 3), x74, (1, 3, 4, 5), (4, 0, 5, 2))
    x76 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x76 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    x76 += einsum(x75, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    rdm2_f_aaaa_oovv += einsum(x76, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x76, (0, 1, 2, 3), (0, 1, 2, 3))
    x77 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x77 += einsum(t1.aa, (0, 1), x30, (0, 2, 3, 4), (2, 4, 3, 1))
    rdm2_f_aaaa_oovv += einsum(t1.aa, (0, 1), x77, (0, 2, 3, 4), (2, 3, 4, 1)) * -2.0
    x78 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x78 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), (1, 5, 2, 4))
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x78, (3, 4, 0, 5), (5, 1, 2, 4))
    rdm2_f_abab_ovov += einsum(x78, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    rdm2_f_abab_ovvv += einsum(t1.aa, (0, 1), x78, (2, 3, 0, 4), (4, 2, 1, 3)) * -1.0
    x79 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x79 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x79 += einsum(x67, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x79, (0, 4, 2, 5), (4, 1, 5, 3)) * 4.0
    x80 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x80 += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 2, 5, 0), (3, 1, 4, 5))
    rdm2_f_abab_ovvo += einsum(x80, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x81 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x81 += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3))
    x81 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oovv += einsum(t2.bbbb, (0, 1, 2, 3), x81, (1, 3, 4, 5), (4, 0, 5, 2)) * 4.0
    x82 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x82 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3))
    x82 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x82 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x82 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x82 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_abab_oovv += einsum(t1.bb, (0, 1), x82, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    x83 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x83 += einsum(x69, (0, 1), (0, 1)) * 0.5
    x83 += einsum(x70, (0, 1), (0, 1))
    rdm2_f_abab_oovv += einsum(x83, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -2.0
    x84 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x84 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 1), (0, 4))
    x85 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x85 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), (1, 4))
    x86 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x86 += einsum(x84, (0, 1), (0, 1)) * 2.0
    x86 += einsum(x85, (0, 1), (0, 1))
    rdm2_f_abab_oovv += einsum(x86, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    x87 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x87 += einsum(x33, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x87 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x87 += einsum(x35, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x87 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oovv += einsum(t1.aa, (0, 1), x87, (2, 3, 0, 4), (4, 2, 1, 3)) * -2.0
    x88 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x88 += einsum(x11, (0, 1), (0, 1)) * 0.5
    x88 += einsum(x12, (0, 1), (0, 1))
    x88 += einsum(x13, (0, 1), (0, 1)) * 0.5
    rdm2_f_abab_oovv += einsum(x88, (0, 1), t2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x89 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x89 += einsum(t1.aa, (0, 1), (0, 1)) * -1.0
    x89 += einsum(x24, (0, 1), (0, 1)) * -1.0
    x89 += einsum(x25, (0, 1), (0, 1)) * -2.0
    x89 += einsum(x26, (0, 1), (0, 1))
    x89 += einsum(x27, (0, 1), (0, 1)) * 2.0
    x89 += einsum(x28, (0, 1), (0, 1))
    rdm2_f_abab_oovv += einsum(t1.bb, (0, 1), x89, (2, 3), (2, 0, 3, 1)) * -1.0
    x90 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x90 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), (3, 4, 1, 5))
    rdm2_f_bbbb_ovov += einsum(x90, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_bbbb_ovvo += einsum(x90, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_bbbb_voov += einsum(x90, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_bbbb_vovo += einsum(x90, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x91 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x91 += einsum(t2.bbbb, (0, 1, 2, 3), x90, (1, 4, 3, 5), (0, 4, 2, 5))
    x92 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x92 += einsum(x46, (0, 1, 2, 3), (0, 1, 2, 3))
    x92 += einsum(x47, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x93 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x93 += einsum(t1.bb, (0, 1), x92, (0, 2, 3, 4), (2, 3, 1, 4)) * 4.0
    x94 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x94 += einsum(x91, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x94 += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3))
    x94 += einsum(t1.bb, (0, 1), x49, (2, 3), (0, 2, 1, 3)) * 2.0
    rdm2_f_bbbb_oovv += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_bbbb_oovv += einsum(x94, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_bbbb_oovv += einsum(x94, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_bbbb_oovv += einsum(x94, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x95 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x95 += einsum(x11, (0, 1), t2.bbbb, (2, 0, 3, 4), (1, 2, 3, 4))
    x96 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x96 += einsum(x18, (0, 1), t2.bbbb, (2, 0, 3, 4), (2, 1, 3, 4)) * -4.0
    x97 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x97 += einsum(x95, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x97 += einsum(x96, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_bbbb_oovv += einsum(x97, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_bbbb_oovv += einsum(x97, (0, 1, 2, 3), (1, 0, 2, 3))
    x98 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x98 += einsum(t1.bb, (0, 1), x45, (0, 2, 3, 4), (2, 3, 1, 4))
    x99 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x99 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_bbbb_ovov += einsum(x99, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    rdm2_f_bbbb_ovvo += einsum(x99, (0, 1, 2, 3), (1, 2, 3, 0)) * 4.0
    rdm2_f_bbbb_voov += einsum(x99, (0, 1, 2, 3), (2, 1, 0, 3)) * 4.0
    rdm2_f_bbbb_vovo += einsum(x99, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x100 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x100 += einsum(t2.bbbb, (0, 1, 2, 3), x99, (1, 4, 3, 5), (0, 4, 2, 5))
    x101 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x101 += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 1, 5), (4, 5, 2, 0))
    rdm2_f_abab_voov += einsum(x101, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x102 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x102 += einsum(t2.abab, (0, 1, 2, 3), x101, (4, 5, 0, 2), (1, 4, 3, 5))
    x103 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x103 += einsum(x84, (0, 1), (0, 1))
    x103 += einsum(x85, (0, 1), (0, 1)) * 0.5
    x104 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x104 += einsum(x103, (0, 1), t2.bbbb, (2, 3, 4, 0), (2, 3, 4, 1)) * -4.0
    x105 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x105 += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x105 += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x105 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x105 += einsum(x104, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_bbbb_oovv += einsum(x105, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_oovv += einsum(x105, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x106 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x106 += einsum(t1.bb, (0, 1), x50, (0, 2, 3, 4), (2, 4, 3, 1))
    rdm2_f_bbbb_oovv += einsum(t1.bb, (0, 1), x106, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0
    x107 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x107 += einsum(t1.aa, (0, 1), x1, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_aaaa_ovov += einsum(x107, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_aaaa_ovvo += einsum(x107, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    rdm2_f_aaaa_voov += einsum(x107, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_aaaa_vovo += einsum(x107, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x108 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x108 += einsum(l1.aa, (0, 1), t1.aa, (1, 2), (0, 2))
    x109 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x109 += einsum(x108, (0, 1), (0, 1))
    x109 += einsum(x69, (0, 1), (0, 1))
    x109 += einsum(x70, (0, 1), (0, 1)) * 2.0
    rdm2_f_aaaa_ovov += einsum(delta.aa.oo, (0, 1), x109, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_voov += einsum(delta.aa.oo, (0, 1), x109, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_abab_vovo += einsum(delta.bb.oo, (0, 1), x109, (2, 3), (2, 0, 3, 1))
    rdm2_f_abab_vovv += einsum(t1.bb, (0, 1), x109, (2, 3), (2, 0, 3, 1))
    x110 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x110 += einsum(l1.bb, (0, 1), t1.bb, (1, 2), (0, 2))
    x111 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x111 += einsum(x110, (0, 1), (0, 1)) * 0.5
    x111 += einsum(x84, (0, 1), (0, 1))
    x111 += einsum(x85, (0, 1), (0, 1)) * 0.5
    rdm2_f_abab_ovov += einsum(delta.aa.oo, (0, 1), x111, (2, 3), (0, 2, 1, 3)) * 2.0
    rdm2_f_abab_ovvv += einsum(t1.aa, (0, 1), x111, (2, 3), (0, 2, 1, 3)) * 2.0
    x112 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x112 += einsum(t1.bb, (0, 1), x16, (2, 0, 3, 4), (2, 3, 4, 1))
    rdm2_f_bbbb_ovov += einsum(x112, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_bbbb_ovvo += einsum(x112, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    rdm2_f_bbbb_voov += einsum(x112, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_bbbb_vovo += einsum(x112, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x113 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(x110, (0, 1), (0, 1))
    x113 += einsum(x84, (0, 1), (0, 1)) * 2.0
    x113 += einsum(x85, (0, 1), (0, 1))
    rdm2_f_bbbb_ovov += einsum(delta.bb.oo, (0, 1), x113, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ovvo += einsum(delta.bb.oo, (0, 1), x113, (2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_bbbb_voov += einsum(delta.bb.oo, (0, 1), x113, (2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_bbbb_vovo += einsum(delta.bb.oo, (0, 1), x113, (2, 3), (2, 0, 3, 1))
    x114 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x114 += einsum(x108, (0, 1), (0, 1)) * 0.5
    x114 += einsum(x69, (0, 1), (0, 1)) * 0.5
    x114 += einsum(x70, (0, 1), (0, 1))
    rdm2_f_aaaa_ovvo += einsum(delta.aa.oo, (0, 1), x114, (2, 3), (0, 2, 3, 1)) * -2.0
    rdm2_f_aaaa_vovo += einsum(delta.aa.oo, (0, 1), x114, (2, 3), (2, 0, 3, 1)) * 2.0
    x115 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x115 += einsum(t1.aa, (0, 1), x8, (2, 3, 0, 4), (2, 3, 4, 1))
    rdm2_f_abab_ovvo += einsum(x115, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x116 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x116 += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (4, 5, 2, 0))
    rdm2_f_abab_voov += einsum(x116, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x117 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x117 += einsum(t1.bb, (0, 1), x34, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_abab_voov += einsum(x117, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x118 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x118 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), (3, 4, 0, 5))
    rdm2_f_abab_vovo += einsum(x118, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    rdm2_f_abab_vovv += einsum(t1.bb, (0, 1), x118, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    x119 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x119 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_aaaa_ovvv = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_ovvv += einsum(x119, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_aaaa_vovv = np.zeros((nvir[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_vovv += einsum(x119, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x120 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x120 += einsum(t2.aaaa, (0, 1, 2, 3), x1, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_aaaa_ovvv += einsum(x120, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_aaaa_vovv += einsum(x120, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x121 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x121 += einsum(t1.aa, (0, 1), x107, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    rdm2_f_aaaa_ovvv += einsum(x121, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_aaaa_vovv += einsum(x121, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x122 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x122 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3))
    x122 += einsum(x67, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x123 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x123 += einsum(t1.aa, (0, 1), x122, (0, 2, 3, 4), (2, 1, 3, 4))
    x124 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x124 += einsum(x123, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x124 += einsum(t1.aa, (0, 1), x109, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_ovvv += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_aaaa_ovvv += einsum(x124, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_vovv += einsum(x124, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_aaaa_vovv += einsum(x124, (0, 1, 2, 3), (1, 0, 3, 2))
    x125 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x125 += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x125 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x125 += einsum(x115, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_abab_ovvv += einsum(t1.bb, (0, 1), x125, (0, 2, 3, 4), (3, 2, 4, 1))
    x126 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x126 += einsum(t2.bbbb, (0, 1, 2, 3), x16, (0, 1, 4, 5), (4, 5, 2, 3))
    rdm2_f_bbbb_ovvv = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_ovvv += einsum(x126, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_bbbb_vovv = np.zeros((nvir[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_vovv += einsum(x126, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x127 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x127 += einsum(t1.bb, (0, 1), x112, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    rdm2_f_bbbb_ovvv += einsum(x127, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_bbbb_vovv += einsum(x127, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x128 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x128 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_bbbb_ovvv += einsum(x128, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_bbbb_vovv += einsum(x128, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x129 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x129 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3))
    x129 += einsum(x90, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x130 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x130 += einsum(t1.bb, (0, 1), x129, (0, 2, 3, 4), (2, 1, 3, 4)) * 4.0
    x131 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x131 += einsum(x130, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x131 += einsum(t1.bb, (0, 1), x113, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ovvv += einsum(x131, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_ovvv += einsum(x131, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_bbbb_vovv += einsum(x131, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_bbbb_vovv += einsum(x131, (0, 1, 2, 3), (1, 0, 3, 2))
    x132 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x132 += einsum(x116, (0, 1, 2, 3), (0, 1, 2, 3))
    x132 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x132 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_vovv += einsum(t1.aa, (0, 1), x132, (2, 3, 0, 4), (4, 2, 1, 3)) * 2.0
    x133 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x133 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_aaaa_vvov = np.zeros((nvir[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_vvov += einsum(x133, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_aaaa_vvvo = np.zeros((nvir[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_vvvo += einsum(x133, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    rdm2_f_aaaa_vvvv += einsum(t1.aa, (0, 1), x133, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0
    x134 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x134 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_bbbb_vvov = np.zeros((nvir[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_vvov += einsum(x134, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_bbbb_vvvo = np.zeros((nvir[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_vvvo += einsum(x134, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    rdm2_f_bbbb_vvvv += einsum(t1.bb, (0, 1), x134, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0
    x135 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x135 += einsum(t1.aa, (0, 1), l2.abab, (2, 3, 0, 4), (4, 3, 2, 1))
    rdm2_f_abab_vvvo = np.zeros((nvir[0], nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_vvvo += einsum(x135, (0, 1, 2, 3), (2, 1, 3, 0))
    rdm2_f_abab_vvvv += einsum(t1.bb, (0, 1), x135, (0, 2, 3, 4), (3, 2, 4, 1))

    rdm2_f_aaaa = pack_2e(rdm2_f_aaaa_oooo, rdm2_f_aaaa_ooov, rdm2_f_aaaa_oovo, rdm2_f_aaaa_ovoo, rdm2_f_aaaa_vooo, rdm2_f_aaaa_oovv, rdm2_f_aaaa_ovov, rdm2_f_aaaa_ovvo, rdm2_f_aaaa_voov, rdm2_f_aaaa_vovo, rdm2_f_aaaa_vvoo, rdm2_f_aaaa_ovvv, rdm2_f_aaaa_vovv, rdm2_f_aaaa_vvov, rdm2_f_aaaa_vvvo, rdm2_f_aaaa_vvvv)
    rdm2_f_abab = pack_2e(rdm2_f_abab_oooo, rdm2_f_abab_ooov, rdm2_f_abab_oovo, rdm2_f_abab_ovoo, rdm2_f_abab_vooo, rdm2_f_abab_oovv, rdm2_f_abab_ovov, rdm2_f_abab_ovvo, rdm2_f_abab_voov, rdm2_f_abab_vovo, rdm2_f_abab_vvoo, rdm2_f_abab_ovvv, rdm2_f_abab_vovv, rdm2_f_abab_vvov, rdm2_f_abab_vvvo, rdm2_f_abab_vvvv)
    rdm2_f_bbbb = pack_2e(rdm2_f_bbbb_oooo, rdm2_f_bbbb_ooov, rdm2_f_bbbb_oovo, rdm2_f_bbbb_ovoo, rdm2_f_bbbb_vooo, rdm2_f_bbbb_oovv, rdm2_f_bbbb_ovov, rdm2_f_bbbb_ovvo, rdm2_f_bbbb_voov, rdm2_f_bbbb_vovo, rdm2_f_bbbb_vvoo, rdm2_f_bbbb_ovvv, rdm2_f_bbbb_vovv, rdm2_f_bbbb_vvov, rdm2_f_bbbb_vvvo, rdm2_f_bbbb_vvvv)

    rdm2_f_aaaa = rdm2_f_aaaa.swapaxes(1, 2)
    rdm2_f_aabb = rdm2_f_abab.swapaxes(1, 2)
    rdm2_f_bbbb = rdm2_f_bbbb.swapaxes(1, 2)

    rdm2_f.aaaa = rdm2_f_aaaa
    rdm2_f.aabb = rdm2_f_aabb
    rdm2_f.bbbb = rdm2_f_bbbb

    return rdm2_f

def make_ip_mom_kets(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    ket1 = Namespace()
    ket2 = Namespace()

    delta_oo = Namespace()
    delta_oo.aa = np.eye(nocc[0])
    delta_oo.bb = np.eye(nocc[1])
    delta_vv = Namespace()
    delta_vv.aa = np.eye(nvir[0])
    delta_vv.bb = np.eye(nvir[1])

    ket2_o_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nocc[0]), dtype=np.float64)
    ket2_o_abab = np.zeros((nocc[0], nocc[1], nvir[0], nocc[1]), dtype=np.float64)
    ket2_o_baba = np.zeros((nocc[1], nocc[0], nvir[1], nocc[0]), dtype=np.float64)
    ket2_o_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nocc[1]), dtype=np.float64)
    ket1_o_aa = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    ket1_o_aa += einsum("ij->ji", delta_oo.aa)
    ket1_o_bb = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    ket1_o_bb += einsum("ij->ji", delta_oo.bb)
    ket1_v_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    ket1_v_aa += einsum("ia->ia", t1.aa)
    ket1_v_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    ket1_v_bb += einsum("ia->ia", t1.bb)
    ket2_v_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    ket2_v_aaaa += einsum("ijab->jiab", t2.aaaa)
    ket2_v_aaaa -= einsum("ijab->jiba", t2.aaaa)
    ket2_v_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    ket2_v_bbbb += einsum("ijab->jiab", t2.bbbb)
    ket2_v_bbbb -= einsum("ijab->jiba", t2.bbbb)
    ket2_v_baba = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    ket2_v_baba -= einsum("ijab->jiba", t2.abab)
    ket2_v_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    ket2_v_abab -= einsum("ijab->ijab", t2.abab)

    ket1_aa = np.concatenate([ket1_o_aa, ket1_v_aa], axis=1)
    ket1_bb = np.concatenate([ket1_o_bb, ket1_v_bb], axis=1)
    ket2_aaaa = np.concatenate([ket2_o_aaaa, ket2_v_aaaa], axis=3)
    ket2_abab = np.concatenate([ket2_o_abab, ket2_v_abab], axis=3)
    ket2_baba = np.concatenate([ket2_o_baba, ket2_v_baba], axis=3)
    ket2_bbbb = np.concatenate([ket2_o_bbbb, ket2_v_bbbb], axis=3)

    ket1.aa = ket1_aa
    ket1.bb = ket1_bb
    ket2.aaaa = ket2_aaaa
    ket2.abab = ket2_abab
    ket2.baba = ket2_baba
    ket2.bbbb = ket2_bbbb

    return ket1, ket2

def make_ea_mom_kets(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    ket1 = Namespace()
    ket2 = Namespace()

    delta_oo = Namespace()
    delta_oo.aa = np.eye(nocc[0])
    delta_oo.bb = np.eye(nocc[1])
    delta_vv = Namespace()
    delta_vv.aa = np.eye(nvir[0])
    delta_vv.bb = np.eye(nvir[1])

    ket2_v_aaaa = np.zeros((nvir[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    ket2_v_abab = np.zeros((nvir[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    ket2_v_baba = np.zeros((nvir[1], nvir[0], nocc[1], nvir[0]), dtype=np.float64)
    ket2_v_bbbb = np.zeros((nvir[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    ket1_o_aa = np.zeros((nvir[0], nocc[0]), dtype=np.float64)
    ket1_o_aa -= einsum("ia->ai", t1.aa)
    ket1_o_bb = np.zeros((nvir[1], nocc[1]), dtype=np.float64)
    ket1_o_bb -= einsum("ia->ai", t1.bb)
    ket1_v_aa = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    ket1_v_aa += einsum("ab->ba", delta_vv.aa)
    ket1_v_bb = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    ket1_v_bb += einsum("ab->ba", delta_vv.bb)
    ket2_o_aaaa = np.zeros((nvir[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    ket2_o_aaaa -= einsum("ijab->abji", t2.aaaa)
    ket2_o_aaaa += einsum("ijab->baji", t2.aaaa)
    ket2_o_bbbb = np.zeros((nvir[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    ket2_o_bbbb -= einsum("ijab->abji", t2.bbbb)
    ket2_o_bbbb += einsum("ijab->baji", t2.bbbb)
    ket2_o_baba = np.zeros((nvir[1], nvir[0], nocc[1], nocc[0]), dtype=np.float64)
    ket2_o_baba += einsum("ijab->baji", t2.abab)
    ket2_o_abab = np.zeros((nvir[0], nvir[1], nocc[0], nocc[1]), dtype=np.float64)
    ket2_o_abab += einsum("ijab->abij", t2.abab)

    ket1_aa = np.concatenate([ket1_o_aa, ket1_v_aa], axis=1)
    ket1_bb = np.concatenate([ket1_o_bb, ket1_v_bb], axis=1)
    ket2_aaaa = np.concatenate([ket2_o_aaaa, ket2_v_aaaa], axis=3)
    ket2_abab = np.concatenate([ket2_o_abab, ket2_v_abab], axis=3)
    ket2_baba = np.concatenate([ket2_o_baba, ket2_v_baba], axis=3)
    ket2_bbbb = np.concatenate([ket2_o_bbbb, ket2_v_bbbb], axis=3)

    ket2_aaaa *= -1
    ket2_abab *= -1
    ket2_baba *= -1
    ket2_bbbb *= -1

    ket1.aa = ket1_aa
    ket1.bb = ket1_bb
    ket2.aaaa = ket2_aaaa
    ket2.abab = ket2_abab
    ket2.baba = ket2_baba
    ket2.bbbb = ket2_bbbb

    return ket1, ket2

def make_ip_mom_bras(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    bra1 = Namespace()
    bra2 = Namespace()

    delta_oo = Namespace()
    delta_oo.aa = np.eye(nocc[0])
    delta_oo.bb = np.eye(nocc[1])
    delta_vv = Namespace()
    delta_vv.aa = np.eye(nvir[0])
    delta_vv.bb = np.eye(nvir[1])

    x0 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x0 += einsum("ijab->jiab", t2.aaaa)
    x0 += einsum("ijab->jiba", t2.aaaa) * -1
    bra1_o_aa = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    bra1_o_aa += einsum("abij,ikba->kj", l2.aaaa, x0) * -1
    del x0
    x1 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x1 += einsum("ijab->jiab", t2.bbbb) * -1
    x1 += einsum("ijab->jiba", t2.bbbb)
    bra1_o_bb = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    bra1_o_bb += einsum("abij,ikab->kj", l2.bbbb, x1) * -1
    del x1
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x2 += einsum("ia,abjk->kjib", t1.aa, l2.aaaa)
    bra2_o_aaaa = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    bra2_o_aaaa += einsum("ijka->kija", x2)
    bra2_o_aaaa -= einsum("ijka->kjia", x2)
    del x2
    x3 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x3 += einsum("ia,abjk->kjib", t1.bb, l2.bbbb)
    bra2_o_bbbb = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    bra2_o_bbbb += einsum("ijka->kija", x3)
    bra2_o_bbbb -= einsum("ijka->kjia", x3)
    del x3
    bra1_o_aa -= einsum("ai,ja->ji", l1.aa, t1.aa)
    bra1_o_aa += einsum("ij->ji", delta_oo.aa)
    bra1_o_aa += einsum("abij,kjab->ki", l2.abab, t2.abab) * -1
    bra1_o_bb += einsum("ij->ji", delta_oo.bb)
    bra1_o_bb -= einsum("ai,ja->ji", l1.bb, t1.bb)
    bra1_o_bb += einsum("abij,ikab->kj", l2.abab, t2.abab) * -1
    bra1_v_aa = np.zeros((nvir[0], nocc[0]), dtype=np.float64)
    bra1_v_aa += einsum("ai->ai", l1.aa)
    bra1_v_bb = np.zeros((nvir[1], nocc[1]), dtype=np.float64)
    bra1_v_bb += einsum("ai->ai", l1.bb)
    bra2_o_aaaa += einsum("ij,ak->jika", delta_oo.aa, l1.aa)
    bra2_o_aaaa -= einsum("ij,ak->jkia", delta_oo.aa, l1.aa)
    bra2_o_abab = np.zeros((nocc[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    bra2_o_abab += einsum("ia,abjk->ikjb", t1.aa, l2.abab)
    bra2_o_abab -= einsum("ij,ak->jkia", delta_oo.aa, l1.bb)
    bra2_o_baba = np.zeros((nocc[1], nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    bra2_o_baba -= einsum("ij,ak->jkia", delta_oo.bb, l1.aa)
    bra2_o_baba += einsum("ia,bajk->ijkb", t1.bb, l2.abab)
    bra2_o_bbbb += einsum("ij,ak->jika", delta_oo.bb, l1.bb)
    bra2_o_bbbb -= einsum("ij,ak->jkia", delta_oo.bb, l1.bb)
    bra2_v_aaaa = np.zeros((nvir[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    bra2_v_aaaa -= einsum("abij->ajib", l2.aaaa)
    bra2_v_aaaa += einsum("abij->bjia", l2.aaaa)
    bra2_v_baba = np.zeros((nvir[1], nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    bra2_v_baba -= einsum("abij->bija", l2.abab)
    bra2_v_abab = np.zeros((nvir[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    bra2_v_abab -= einsum("abij->ajib", l2.abab)
    bra2_v_bbbb = np.zeros((nvir[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    bra2_v_bbbb -= einsum("abij->ajib", l2.bbbb)
    bra2_v_bbbb += einsum("abij->bjia", l2.bbbb)

    bra1_aa = np.concatenate([bra1_o_aa, bra1_v_aa], axis=0)
    bra1_bb = np.concatenate([bra1_o_bb, bra1_v_bb], axis=0)
    bra2_aaaa = np.concatenate([bra2_o_aaaa, bra2_v_aaaa], axis=0)
    bra2_abab = np.concatenate([bra2_o_abab, bra2_v_abab], axis=0)
    bra2_baba = np.concatenate([bra2_o_baba, bra2_v_baba], axis=0)
    bra2_bbbb = np.concatenate([bra2_o_bbbb, bra2_v_bbbb], axis=0)

    bra1.aa = bra1_aa
    bra1.bb = bra1_bb
    bra2.aaaa = bra2_aaaa
    bra2.abab = bra2_abab
    bra2.baba = bra2_baba
    bra2.bbbb = bra2_bbbb

    return bra1, bra2

def make_ea_mom_bras(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    bra1 = Namespace()
    bra2 = Namespace()

    delta_oo = Namespace()
    delta_oo.aa = np.eye(nocc[0])
    delta_oo.bb = np.eye(nocc[1])
    delta_vv = Namespace()
    delta_vv.aa = np.eye(nvir[0])
    delta_vv.bb = np.eye(nvir[1])

    x0 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x0 += einsum("ijab->jiab", t2.aaaa) * -1
    x0 += einsum("ijab->jiba", t2.aaaa)
    bra1_v_aa = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    bra1_v_aa += einsum("abij,ijac->cb", l2.aaaa, x0) * -1
    del x0
    x1 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x1 += einsum("ijab->jiab", t2.bbbb)
    x1 += einsum("ijab->jiba", t2.bbbb) * -1
    bra1_v_bb = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    bra1_v_bb += einsum("abij,ijbc->ca", l2.bbbb, x1) * -1
    del x1
    x2 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x2 += einsum("ia,bcji->jbca", t1.aa, l2.aaaa)
    bra2_v_aaaa = np.zeros((nvir[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    bra2_v_aaaa += einsum("iabc->cabi", x2)
    bra2_v_aaaa -= einsum("iabc->cbai", x2)
    del x2
    x3 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x3 += einsum("ia,bcji->jbca", t1.bb, l2.bbbb)
    bra2_v_bbbb = np.zeros((nvir[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    bra2_v_bbbb += einsum("iabc->cabi", x3)
    bra2_v_bbbb -= einsum("iabc->cbai", x3)
    del x3
    bra1_o_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    bra1_o_aa -= einsum("ai->ia", l1.aa)
    bra1_o_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    bra1_o_bb -= einsum("ai->ia", l1.bb)
    bra1_v_aa += einsum("ab->ba", delta_vv.aa)
    bra1_v_aa -= einsum("ai,ib->ba", l1.aa, t1.aa)
    bra1_v_aa += einsum("abij,ijcb->ca", l2.abab, t2.abab) * -1
    bra1_v_bb += einsum("abij,ijac->cb", l2.abab, t2.abab) * -1
    bra1_v_bb += einsum("ab->ba", delta_vv.bb)
    bra1_v_bb -= einsum("ai,ib->ba", l1.bb, t1.bb)
    bra2_o_aaaa = np.zeros((nocc[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    bra2_o_aaaa += einsum("abij->jabi", l2.aaaa)
    bra2_o_aaaa -= einsum("abij->jbai", l2.aaaa)
    bra2_o_abab = np.zeros((nocc[0], nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    bra2_o_abab += einsum("abij->ibaj", l2.abab)
    bra2_o_baba = np.zeros((nocc[1], nvir[0], nvir[1], nocc[0]), dtype=np.float64)
    bra2_o_baba += einsum("abij->jabi", l2.abab)
    bra2_o_bbbb = np.zeros((nocc[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    bra2_o_bbbb += einsum("abij->jabi", l2.bbbb)
    bra2_o_bbbb -= einsum("abij->jbai", l2.bbbb)
    bra2_v_aaaa += einsum("ab,ci->baci", delta_vv.aa, l1.aa)
    bra2_v_aaaa -= einsum("ab,ci->bcai", delta_vv.aa, l1.aa)
    bra2_v_abab = np.zeros((nvir[0], nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    bra2_v_abab -= einsum("ab,ci->bcai", delta_vv.aa, l1.bb)
    bra2_v_abab += einsum("ia,bcij->acbj", t1.aa, l2.abab)
    bra2_v_baba = np.zeros((nvir[1], nvir[0], nvir[1], nocc[0]), dtype=np.float64)
    bra2_v_baba -= einsum("ab,ci->bcai", delta_vv.bb, l1.aa)
    bra2_v_baba += einsum("ia,bcji->abcj", t1.bb, l2.abab)
    bra2_v_bbbb += einsum("ab,ci->baci", delta_vv.bb, l1.bb)
    bra2_v_bbbb -= einsum("ab,ci->bcai", delta_vv.bb, l1.bb)

    bra1_aa = np.concatenate([bra1_o_aa, bra1_v_aa], axis=0)
    bra1_bb = np.concatenate([bra1_o_bb, bra1_v_bb], axis=0)
    bra2_aaaa = np.concatenate([bra2_o_aaaa, bra2_v_aaaa], axis=0)
    bra2_abab = np.concatenate([bra2_o_abab, bra2_v_abab], axis=0)
    bra2_baba = np.concatenate([bra2_o_baba, bra2_v_baba], axis=0)
    bra2_bbbb = np.concatenate([bra2_o_bbbb, bra2_v_bbbb], axis=0)

    bra2_aaaa *= -1
    bra2_abab *= -1
    bra2_baba *= -1
    bra2_bbbb *= -1

    bra1.aa = bra1_aa
    bra1.bb = bra1_bb
    bra2.aaaa = bra2_aaaa
    bra2.abab = bra2_abab
    bra2.baba = bra2_baba
    bra2.bbbb = bra2_bbbb

    return bra1, bra2

def hbar_matvec_ip(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, r1=None, r2=None, **kwargs):
    x0 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x0 += einsum("i,iajb->jab", r1.a, v.aabb.ovov)
    r1new_a = np.zeros((nocc[0]), dtype=np.float64)
    r1new_a += einsum("iab,jiab->j", x0, t2.abab) * -1
    del x0
    x1 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x1 += einsum("i,jaib->jab", r1.a, v.aaaa.ovov)
    x2 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x2 += einsum("iab->iab", x1)
    x2 += einsum("iab->iba", x1) * -1
    r1new_a += einsum("iab,ijab->j", x2, t2.aaaa) * -1
    del x2
    x92 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x92 += einsum("ia,jba->ijb", t1.aa, x1)
    del x1
    x93 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x93 += einsum("ija->ija", x92)
    del x92
    x3 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum("ija->ija", r2.aaa)
    x3 += einsum("i,ja->jia", r1.a, t1.aa) * -1
    x4 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x4 += einsum("ijka->ikja", v.aaaa.ooov) * -1
    x4 += einsum("ijka->kija", v.aaaa.ooov)
    x76 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x76 += einsum("ia,jika->jk", t1.aa, x4)
    x78 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x78 += einsum("ij->ij", x76) * -1
    x133 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x133 += einsum("ij->ij", x76) * -1
    del x76
    x171 = np.zeros((nocc[0], nocc[0], nocc[1]), dtype=np.float64)
    x171 += einsum("ija,kila->klj", r2.aba, x4) * -1
    r1new_a += einsum("ija,jika->k", x3, x4) * -1
    del x4
    x5 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x5 += einsum("ija->jia", r2.bab)
    x5 += einsum("i,ja->ija", r1.a, t1.bb) * -1
    x17 = np.zeros((nvir[0]), dtype=np.float64)
    x17 += einsum("ija,ibja->b", x5, v.aabb.ovov)
    x18 = np.zeros((nvir[0]), dtype=np.float64)
    x18 += einsum("a->a", x17) * -1
    del x17
    x116 = np.zeros((nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x116 += einsum("ija,ibjc->bac", x5, v.aabb.ovov)
    x117 = np.zeros((nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x117 += einsum("ija,ibka->kjb", x5, v.aabb.ovov) * -1
    x142 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x142 += einsum("ija,ibca->jbc", x5, v.aabb.ovvv) * -1
    r1new_a += einsum("ija,ikja->k", x5, v.aabb.ooov)
    r2new_bab = np.zeros((nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    r2new_bab += einsum("ija,ikba->jkb", x5, v.aabb.oovv) * -1
    del x5
    x6 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x6 += einsum("ia,jbia->jb", t1.bb, v.aabb.ovov)
    x9 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x9 += einsum("ia->ia", x6)
    del x6
    x7 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x7 += einsum("iajb->jiab", v.aaaa.ovov) * -1
    x7 += einsum("iajb->jiba", v.aaaa.ovov)
    x8 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x8 += einsum("ia,ijba->jb", t1.aa, x7)
    x9 += einsum("ia->ia", x8) * -1
    del x8
    x16 = np.zeros((nvir[0]), dtype=np.float64)
    x16 += einsum("ija,ijab->b", x3, x7)
    del x3
    x18 += einsum("a->a", x16) * -1
    del x16
    x160 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x160 += einsum("ija,ikba->kjb", r2.aba, x7)
    x161 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x161 += einsum("ija->ija", x160) * -1
    x180 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x180 += einsum("ija->ija", x160) * -1
    del x160
    x9 += einsum("ia->ia", f.aa.ov)
    x152 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x152 += einsum("ia,ijab->jb", x9, t2.abab)
    x156 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x156 += einsum("ia->ia", x152)
    x214 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x214 += einsum("ia->ia", x152)
    del x152
    r1new_b = np.zeros((nocc[1]), dtype=np.float64)
    r1new_b += einsum("ia,ija->j", x9, r2.aba) * -1
    x10 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x10 += einsum("ija->ija", r2.aaa) * -1
    x10 += einsum("ija->jia", r2.aaa)
    r1new_a += einsum("ia,jia->j", x9, x10) * -1
    x11 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x11 += einsum("ia,iajb->jb", t1.aa, v.aabb.ovov)
    x14 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x14 += einsum("ia->ia", x11)
    del x11
    x12 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x12 += einsum("iajb->jiab", v.bbbb.ovov)
    x12 += einsum("iajb->jiba", v.bbbb.ovov) * -1
    x13 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x13 += einsum("ia,ijab->jb", t1.bb, x12)
    x14 += einsum("ia->ia", x13) * -1
    del x13
    x44 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x44 += einsum("ija,ikab->jkb", r2.bab, x12)
    x45 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x45 += einsum("ija->ija", x44) * -1
    x113 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x113 += einsum("ija->ija", x44) * -1
    del x44
    x14 += einsum("ia->ia", f.bb.ov)
    x107 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x107 += einsum("ia,jiba->jb", x14, t2.abab)
    x111 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x111 += einsum("ia->ia", x107)
    x173 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x173 += einsum("ia->ia", x107)
    del x107
    r1new_a += einsum("ia,ija->j", x14, r2.bab) * -1
    x15 = np.zeros((nvir[0]), dtype=np.float64)
    x15 += einsum("i,ia->a", r1.a, f.aa.ov)
    x18 += einsum("a->a", x15)
    del x15
    x80 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x80 += einsum("a,ijab->ijb", x18, t2.aaaa)
    x112 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x112 += einsum("ija->jia", x80)
    del x80
    r1new_a += einsum("a,ia->i", x18, t1.aa) * -1
    r2new_bab += einsum("a,ijab->jib", x18, t2.abab)
    del x18
    x19 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x19 += einsum("i,jaib->jab", r1.b, v.aabb.ovov)
    r1new_b += einsum("iab,ijab->j", x19, t2.abab) * -1
    del x19
    x20 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x20 += einsum("i,jaib->jab", r1.b, v.bbbb.ovov)
    x21 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x21 += einsum("iab->iab", x20)
    x21 += einsum("iab->iba", x20) * -1
    r1new_b += einsum("iab,ijab->j", x21, t2.bbbb) * -1
    del x21
    x207 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x207 += einsum("ia,jba->ijb", t1.bb, x20)
    del x20
    x208 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x208 += einsum("ija->ija", x207)
    del x207
    x22 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x22 += einsum("ija->ija", r2.bbb)
    x22 += einsum("i,ja->jia", r1.b, t1.bb) * -1
    x23 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x23 += einsum("ijka->ikja", v.bbbb.ooov) * -1
    x23 += einsum("ijka->kija", v.bbbb.ooov)
    x138 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x138 += einsum("ia,jika->jk", t1.bb, x23)
    x140 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x140 += einsum("ij->ij", x138) * -1
    x194 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x194 += einsum("ij->ij", x138) * -1
    del x138
    x141 = np.zeros((nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x141 += einsum("ija,kila->jkl", r2.bab, x23) * -1
    r1new_b += einsum("ija,jika->k", x22, x23) * -1
    del x23
    x24 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x24 += einsum("ija->ija", r2.aba)
    x24 += einsum("i,ja->jia", r1.b, t1.aa) * -1
    x29 = np.zeros((nvir[1]), dtype=np.float64)
    x29 += einsum("ija,iajb->b", x24, v.aabb.ovov)
    x30 = np.zeros((nvir[1]), dtype=np.float64)
    x30 += einsum("a->a", x29) * -1
    del x29
    x167 = np.zeros((nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x167 += einsum("ija,ibjc->abc", x24, v.aabb.ovov)
    x168 = np.zeros((nocc[0], nocc[0], nvir[1]), dtype=np.float64)
    x168 += einsum("ija,kajb->kib", x24, v.aabb.ovov) * -1
    r1new_b += einsum("ija,iajk->k", x24, v.aabb.ovoo)
    del x24
    x25 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x25 += einsum("ija->ija", r2.bbb)
    x25 += einsum("ija->jia", r2.bbb) * -1
    r1new_b += einsum("ia,ija->j", x14, x25) * -1
    x26 = np.zeros((nvir[1]), dtype=np.float64)
    x26 += einsum("i,ia->a", r1.b, f.bb.ov)
    x30 += einsum("a->a", x26)
    del x26
    x27 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x27 += einsum("iajb->jiab", v.bbbb.ovov) * -1
    x27 += einsum("iajb->jiba", v.bbbb.ovov)
    x28 = np.zeros((nvir[1]), dtype=np.float64)
    x28 += einsum("ija,ijab->b", x22, x27)
    del x22
    x30 += einsum("a->a", x28) * -1
    del x28
    x196 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x196 += einsum("a,ijab->ijb", x30, t2.bbbb)
    x215 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x215 += einsum("ija->jia", x196)
    del x196
    r1new_b += einsum("a,ia->i", x30, t1.bb) * -1
    r2new_aba = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    r2new_aba += einsum("a,ijba->ijb", x30, t2.abab)
    del x30
    x31 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x31 += einsum("i,ijak->jka", r1.a, v.aaaa.oovo)
    x112 += einsum("ija->ija", x31) * -1
    del x31
    x32 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x32 += einsum("ij,ia->ja", f.aa.oo, t1.aa)
    x112 += einsum("i,ja->jia", r1.a, x32)
    del x32
    x33 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x33 += einsum("ija,iabk->jkb", r2.bab, v.bbaa.ovvo)
    x112 += einsum("ija->ija", x33) * -1
    del x33
    x34 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x34 += einsum("i,ijka->jka", r1.a, v.aabb.ooov)
    x35 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x35 += einsum("ija,kjba->kib", x34, t2.abab)
    x112 += einsum("ija->ija", x35)
    del x35
    x113 += einsum("ija->ija", x34)
    del x34
    x36 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x36 += einsum("ija,kbia->jkb", r2.bab, v.aabb.ovov)
    x40 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x40 += einsum("ija->ija", x36)
    x93 += einsum("ija->ija", x36)
    x94 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x94 += einsum("ia,jka->jki", t1.aa, x93)
    del x93
    x95 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x95 += einsum("ijk->jki", x94)
    del x94
    x115 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x115 += einsum("ija->jia", x36)
    del x36
    x37 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x37 += einsum("i,ja->ija", r1.a, t1.aa)
    x37 += einsum("ija->ija", r2.aaa)
    x37 += einsum("ija->jia", r2.aaa) * -1
    x43 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x43 += einsum("ija,iakb->jkb", x37, v.aabb.ovov)
    x45 += einsum("ija->ija", x43)
    x46 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x46 += einsum("ija,kjba->kib", x45, t2.abab)
    del x45
    x112 += einsum("ija->jia", x46) * -1
    del x46
    x113 += einsum("ija->ija", x43)
    del x43
    x115 += einsum("ija,ikab->kjb", x37, x7)
    x141 += einsum("ija,iakl->jkl", x37, v.aabb.ovoo)
    x38 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x38 += einsum("iajb->jiab", v.aaaa.ovov)
    x38 += einsum("iajb->jiba", v.aaaa.ovov) * -1
    x39 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x39 += einsum("ija,ikba->jkb", x37, x38)
    del x38
    x40 += einsum("ija->ija", x39)
    del x39
    x41 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum("ijab->jiab", t2.aaaa) * -1
    x41 += einsum("ijab->jiba", t2.aaaa)
    x42 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x42 += einsum("ija,jkba->ikb", x40, x41)
    del x40
    x112 += einsum("ija->ija", x42)
    del x42
    x106 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x106 += einsum("ia,ijba->jb", x9, x41)
    del x9
    del x41
    x111 += einsum("ia->ia", x106) * -1
    x173 += einsum("ia->ia", x106) * -1
    del x106
    x47 = np.zeros((nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x47 += einsum("i,iabc->bac", r1.a, v.aaaa.ovvv)
    x50 = np.zeros((nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x50 += einsum("abc->abc", x47) * -1
    x81 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x81 += einsum("ia,bac->ibc", t1.aa, x47)
    del x47
    x85 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x85 += einsum("iab->iab", x81)
    del x81
    x48 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x48 += einsum("ija->ija", r2.aaa)
    x48 += einsum("i,ja->ija", r1.a, t1.aa)
    x49 = np.zeros((nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x49 += einsum("ija,jbic->bca", x48, v.aaaa.ovov)
    del x48
    x50 += einsum("abc->cba", x49)
    del x49
    x51 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x51 += einsum("abc,ijcb->ija", x50, t2.aaaa)
    del x50
    x112 += einsum("ija->jia", x51)
    del x51
    x52 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x52 += einsum("iabj->ijba", v.aaaa.ovvo)
    x52 += einsum("ijab->ijab", v.aaaa.oovv) * -1
    x53 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum("ija,ikba->jkb", x37, x52)
    del x37
    x112 += einsum("ija->ija", x53) * -1
    del x53
    x109 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x109 += einsum("ia,ijba->jb", t1.aa, x52)
    del x52
    x111 += einsum("ia->ia", x109)
    x173 += einsum("ia->ia", x109)
    del x109
    x54 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum("ijka->ikja", v.aaaa.ooov)
    x54 += einsum("ijka->kija", v.aaaa.ooov) * -1
    x55 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x55 += einsum("i,jika->jka", r1.a, x54)
    del x54
    x115 += einsum("ija->ija", x55) * -1
    r2new_bab += einsum("ija,ikab->kjb", x115, t2.abab)
    del x115
    x56 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x56 += einsum("ia,jb->ijab", t1.aa, t1.aa)
    x56 += einsum("ijab->jiab", t2.aaaa) * -1
    x56 += einsum("ijab->jiba", t2.aaaa)
    x57 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x57 += einsum("ija,ikba->jkb", x55, x56) * -1
    del x55
    x112 += einsum("ija->jia", x57) * -1
    del x57
    x58 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x58 += einsum("ia,jbka->ijkb", t1.aa, v.aaaa.ovov)
    x59 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x59 += einsum("ia,jkla->jilk", t1.aa, x58)
    x61 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x61 += einsum("ijkl->lkji", x59)
    del x59
    x90 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x90 += einsum("ijka->jkia", x58)
    x90 += einsum("ijka->kjia", x58) * -1
    x100 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x100 += einsum("ijka->ijka", x58) * -1
    x100 += einsum("ijka->ikja", x58)
    del x58
    x60 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x60 += einsum("ia,jkla->ijlk", t1.aa, v.aaaa.ooov)
    x61 += einsum("ijkl->jkli", x60)
    x61 += einsum("ijkl->kjli", x60) * -1
    del x60
    x61 += einsum("ijkl->kilj", v.aaaa.oooo)
    x62 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x62 += einsum("ija,jikl->kla", r2.aaa, x61)
    del x61
    x112 += einsum("ija->jia", x62)
    del x62
    x63 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum("ia,ib->ab", f.aa.ov, t1.aa)
    x71 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum("ab->ba", x63)
    del x63
    x64 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x64 += einsum("ia,iabc->bc", t1.bb, v.bbaa.ovvv)
    x71 += einsum("ab->ab", x64) * -1
    del x64
    x65 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x65 += einsum("ijab->jiba", t2.aaaa)
    x65 += einsum("ia,jb->ijab", t1.aa, t1.aa)
    x66 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x66 += einsum("ijab,ijca->bc", x65, x7)
    x71 += einsum("ab->ab", x66) * -1
    del x66
    x75 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x75 += einsum("ijab,ikba->jk", x65, x7)
    del x7
    x78 += einsum("ij->ji", x75) * -1
    x133 += einsum("ij->ji", x75) * -1
    del x75
    x67 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x67 += einsum("iabc->ibac", v.aaaa.ovvv)
    x67 += einsum("iabc->ibca", v.aaaa.ovvv) * -1
    x68 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum("ia,ibac->bc", t1.aa, x67)
    x71 += einsum("ab->ab", x68) * -1
    del x68
    x102 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum("ijab,icba->jc", x65, x67)
    del x65
    x111 += einsum("ia->ia", x102) * -1
    x173 += einsum("ia->ia", x102) * -1
    del x102
    x169 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x169 += einsum("ia,jbac->jibc", t1.aa, x67) * -1
    del x67
    x69 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x69 += einsum("ijab->ijab", t2.abab)
    x69 += einsum("ia,jb->ijab", t1.aa, t1.bb)
    x70 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum("iajb,ijcb->ca", v.aabb.ovov, x69)
    x71 += einsum("ab->ab", x70)
    del x70
    x77 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x77 += einsum("iajb,kjab->ki", v.aabb.ovov, x69)
    x78 += einsum("ij->ji", x77)
    x133 += einsum("ij->ji", x77)
    del x77
    x108 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x108 += einsum("iabc,jica->jb", v.bbaa.ovvv, x69)
    x111 += einsum("ia->ia", x108)
    x173 += einsum("ia->ia", x108)
    del x108
    x131 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x131 += einsum("iajb,ijac->cb", v.aabb.ovov, x69)
    x132 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x132 += einsum("ab->ab", x131)
    del x131
    x139 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x139 += einsum("iajb,ikab->kj", v.aabb.ovov, x69)
    x140 += einsum("ij->ji", x139)
    x194 += einsum("ij->ji", x139)
    del x139
    x153 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x153 += einsum("iabc,ijac->jb", v.aabb.ovvv, x69)
    del x69
    x156 += einsum("ia->ia", x153)
    x214 += einsum("ia->ia", x153)
    del x153
    x71 += einsum("ab->ab", f.aa.vv) * -1
    x72 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x72 += einsum("ab,ijb->ija", x71, r2.aaa)
    x112 += einsum("ija->ija", x72) * -1
    del x72
    r2new_aba += einsum("ab,ijb->ija", x71, r2.aba) * -1
    del x71
    x73 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x73 += einsum("ia,ja->ij", f.aa.ov, t1.aa)
    x78 += einsum("ij->ij", x73)
    x133 += einsum("ij->ij", x73)
    del x73
    x74 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x74 += einsum("ia,jkia->jk", t1.bb, v.aabb.ooov)
    x78 += einsum("ij->ij", x74)
    x79 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x79 += einsum("ij,ika->jka", x78, x10)
    x112 += einsum("ija->jia", x79) * -1
    del x79
    x110 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x110 += einsum("ia,ij->ja", t1.aa, x78)
    del x78
    x111 += einsum("ia->ia", x110) * -1
    del x110
    x133 += einsum("ij->ij", x74)
    del x74
    x82 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x82 += einsum("ija,iabc->jbc", r2.bab, v.bbaa.ovvv)
    x85 += einsum("iab->iab", x82)
    del x82
    x83 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x83 += einsum("iabc->ibac", v.aaaa.ovvv) * -1
    x83 += einsum("iabc->ibca", v.aaaa.ovvv)
    x84 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x84 += einsum("ija,jbca->ibc", x10, x83)
    del x83
    x85 += einsum("iab->iab", x84)
    del x84
    x86 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x86 += einsum("ia,jba->jib", t1.aa, x85)
    del x85
    x112 += einsum("ija->ija", x86) * -1
    del x86
    x87 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x87 += einsum("i,jkil->jkl", r1.a, v.aaaa.oooo)
    x95 += einsum("ijk->ijk", x87)
    del x87
    x88 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x88 += einsum("ija,klia->jkl", r2.bab, v.aabb.ooov)
    x95 += einsum("ijk->jki", x88)
    del x88
    x89 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x89 += einsum("ija->ija", r2.aaa)
    x89 += einsum("ija->jia", r2.aaa) * -1
    x97 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x97 += einsum("ij,ika->kja", f.aa.oo, x89)
    x112 += einsum("ija->jia", x97) * -1
    del x97
    x90 += einsum("ijka->ikja", v.aaaa.ooov) * -1
    x90 += einsum("ijka->kija", v.aaaa.ooov)
    x91 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x91 += einsum("ija,ikla->klj", x89, x90)
    del x89
    del x90
    x95 += einsum("ijk->ijk", x91)
    del x91
    x96 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x96 += einsum("ia,ijk->jka", t1.aa, x95)
    del x95
    x112 += einsum("ija->jia", x96)
    del x96
    x98 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x98 += einsum("ab,ib->ia", f.aa.vv, t1.aa)
    x111 += einsum("ia->ia", x98)
    x173 += einsum("ia->ia", x98)
    del x98
    x99 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x99 += einsum("ia,iabj->jb", t1.bb, v.bbaa.ovvo)
    x111 += einsum("ia->ia", x99)
    x173 += einsum("ia->ia", x99)
    del x99
    x100 += einsum("ijka->jika", v.aaaa.ooov)
    x100 += einsum("ijka->jkia", v.aaaa.ooov) * -1
    x101 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x101 += einsum("ijab,kjia->kb", t2.aaaa, x100)
    del x100
    x111 += einsum("ia->ia", x101) * -1
    x173 += einsum("ia->ia", x101) * -1
    del x101
    x103 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x103 += einsum("ia,jakb->ijkb", t1.aa, v.aabb.ovov)
    x104 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x104 += einsum("ijka->jika", x103)
    del x103
    x104 += einsum("ijka->ijka", v.aabb.ooov)
    x105 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x105 += einsum("ijab,ikjb->ka", t2.abab, x104)
    x111 += einsum("ia->ia", x105) * -1
    x112 += einsum("i,ja->ija", r1.a, x111)
    del x111
    r2new_aaa = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    r2new_aaa += einsum("ija->ija", x112)
    r2new_aaa += einsum("ija->jia", x112) * -1
    del x112
    x173 += einsum("ia->ia", x105) * -1
    del x105
    x141 += einsum("ija,jkla->kli", r2.bab, x104) * -1
    del x104
    x114 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x114 += einsum("ia,jb->ijab", t1.bb, t1.bb)
    x114 += einsum("ijab->jiab", t2.bbbb) * -1
    x114 += einsum("ijab->jiba", t2.bbbb)
    r2new_bab += einsum("ija,jkba->kib", x113, x114) * -1
    del x113
    x116 += einsum("i,iabc->abc", r1.a, v.aabb.ovvv)
    r2new_bab += einsum("abc,ijac->jib", x116, t2.abab)
    del x116
    x117 += einsum("i,iajk->jka", r1.a, v.aabb.ovoo)
    r2new_bab += einsum("ija,kiab->jkb", x117, t2.abab) * -1
    del x117
    x118 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x118 += einsum("ia,jkla->jkil", t1.bb, v.aabb.ooov)
    x122 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x122 += einsum("ijkl->ijlk", x118)
    del x118
    x119 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x119 += einsum("ia,jbka->jikb", t1.bb, v.aabb.ovov)
    x120 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x120 += einsum("ijka->ikja", x119)
    del x119
    x120 += einsum("iajk->ijka", v.aabb.ovoo)
    x121 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x121 += einsum("ia,jkla->jikl", t1.aa, x120)
    x122 += einsum("ijkl->ijkl", x121)
    del x121
    x149 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x149 += einsum("ijab,ijka->kb", t2.abab, x120)
    x156 += einsum("ia->ia", x149) * -1
    x214 += einsum("ia->ia", x149) * -1
    del x149
    x171 += einsum("ija,kjla->kil", r2.aba, x120) * -1
    del x120
    x122 += einsum("ijkl->ijkl", v.aabb.oooo)
    r2new_bab += einsum("ija,jkil->lka", r2.bab, x122)
    r2new_aba += einsum("ija,ikjl->kla", r2.aba, x122)
    del x122
    x123 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x123 += einsum("iabj->ijab", v.aabb.ovvo)
    x123 += einsum("ia,jbca->jibc", t1.bb, v.aabb.ovvv)
    r2new_bab += einsum("ija,jkab->kib", x10, x123)
    del x10
    del x123
    x124 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x124 += einsum("iabc->ibac", v.bbbb.ovvv)
    x124 += einsum("iabc->ibca", v.bbbb.ovvv) * -1
    x125 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x125 += einsum("ia,jbac->jibc", t1.bb, x124) * -1
    x130 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x130 += einsum("ia,ibac->bc", t1.bb, x124)
    x132 += einsum("ab->ab", x130) * -1
    del x130
    x125 += einsum("iabj->ijba", v.bbbb.ovvo)
    x125 += einsum("ijab->ijab", v.bbbb.oovv) * -1
    r2new_bab += einsum("ija,ikba->kjb", r2.bab, x125)
    del x125
    x126 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x126 += einsum("ia,ib->ab", f.bb.ov, t1.bb)
    x132 += einsum("ab->ba", x126)
    del x126
    x127 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x127 += einsum("ia,iabc->bc", t1.aa, v.aabb.ovvv)
    x132 += einsum("ab->ab", x127) * -1
    del x127
    x128 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x128 += einsum("ijab->jiba", t2.bbbb)
    x128 += einsum("ia,jb->ijba", t1.bb, t1.bb) * -1
    x129 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x129 += einsum("ijab,ijbc->ac", x128, x27)
    x132 += einsum("ab->ab", x129) * -1
    del x129
    x148 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x148 += einsum("iabc,ijcb->ja", x124, x128)
    del x128
    x156 += einsum("ia->ia", x148) * -1
    x214 += einsum("ia->ia", x148) * -1
    del x148
    x132 += einsum("ab->ab", f.bb.vv) * -1
    x193 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x193 += einsum("ab,ijb->ija", x132, r2.bbb)
    x215 += einsum("ija->ija", x193) * -1
    del x193
    r2new_bab += einsum("ab,ijb->ija", x132, r2.bab) * -1
    del x132
    x133 += einsum("ij->ij", f.aa.oo)
    x173 += einsum("ia,ij->ja", t1.aa, x133) * -1
    r2new_bab += einsum("ij,kia->kja", x133, r2.bab) * -1
    r2new_aba += einsum("ij,ika->jka", x133, r2.aba) * -1
    del x133
    x134 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x134 += einsum("ia,ja->ij", f.bb.ov, t1.bb)
    x140 += einsum("ij->ij", x134)
    x194 += einsum("ij->ij", x134)
    del x134
    x135 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x135 += einsum("ia,iajk->jk", t1.aa, v.aabb.ovoo)
    x140 += einsum("ij->ij", x135)
    x194 += einsum("ij->ij", x135)
    del x135
    x136 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x136 += einsum("ijab->jiba", t2.bbbb)
    x136 += einsum("ia,jb->ijab", t1.bb, t1.bb)
    x137 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x137 += einsum("ijab,ikba->jk", x136, x27)
    del x136
    del x27
    x140 += einsum("ij->ji", x137) * -1
    x194 += einsum("ij->ji", x137) * -1
    del x137
    x195 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x195 += einsum("ij,kia->jka", x194, x25)
    del x25
    x215 += einsum("ija->jia", x195) * -1
    del x195
    x213 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x213 += einsum("ia,ij->ja", t1.bb, x194)
    del x194
    x214 += einsum("ia->ia", x213) * -1
    del x213
    x140 += einsum("ij->ij", f.bb.oo)
    x156 += einsum("ia,ij->ja", t1.bb, x140) * -1
    r2new_bab += einsum("ij,ika->jka", x140, r2.bab) * -1
    r2new_aba += einsum("ij,kia->kja", x140, r2.aba) * -1
    del x140
    x141 += einsum("i,ijkl->jkl", r1.a, v.aabb.oooo)
    r2new_bab += einsum("ia,jik->kja", t1.bb, x141) * -1
    del x141
    x142 += einsum("i,iabj->jab", r1.a, v.aabb.ovvo)
    r2new_bab += einsum("ia,jab->jib", t1.aa, x142)
    del x142
    x143 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x143 += einsum("ab,ib->ia", f.bb.vv, t1.bb)
    x156 += einsum("ia->ia", x143)
    x214 += einsum("ia->ia", x143)
    del x143
    x144 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x144 += einsum("ia,iabj->jb", t1.aa, v.aabb.ovvo)
    x156 += einsum("ia->ia", x144)
    x214 += einsum("ia->ia", x144)
    del x144
    x145 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x145 += einsum("ia,jbka->ijkb", t1.bb, v.bbbb.ovov)
    x146 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x146 += einsum("ijka->ijka", x145)
    x146 += einsum("ijka->ikja", x145) * -1
    x189 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x189 += einsum("ia,jkla->jilk", t1.bb, x145)
    x191 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x191 += einsum("ijkl->lkji", x189)
    del x189
    x205 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x205 += einsum("ijka->jkia", x145)
    x205 += einsum("ijka->kjia", x145) * -1
    del x145
    x146 += einsum("ijka->jika", v.bbbb.ooov) * -1
    x146 += einsum("ijka->jkia", v.bbbb.ooov)
    x147 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x147 += einsum("ijab,kjib->ka", t2.bbbb, x146)
    del x146
    x156 += einsum("ia->ia", x147) * -1
    x214 += einsum("ia->ia", x147) * -1
    del x147
    x150 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x150 += einsum("ijab->jiab", t2.bbbb)
    x150 += einsum("ijab->jiba", t2.bbbb) * -1
    x151 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x151 += einsum("ia,ijab->jb", x14, x150)
    del x14
    x156 += einsum("ia->ia", x151) * -1
    x214 += einsum("ia->ia", x151) * -1
    del x151
    x154 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x154 += einsum("iabj->ijba", v.bbbb.ovvo)
    x154 += einsum("ijab->ijab", v.bbbb.oovv) * -1
    x155 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x155 += einsum("ia,ijba->jb", t1.bb, x154)
    x156 += einsum("ia->ia", x155)
    x214 += einsum("ia->ia", x155)
    del x155
    x215 += einsum("i,ja->ija", r1.b, x214)
    del x214
    x156 += einsum("ai->ia", f.bb.vo)
    r2new_bab += einsum("i,ja->jia", r1.a, x156) * -1
    del x156
    x157 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x157 += einsum("i,jaik->jka", r1.b, v.aabb.ovoo)
    x161 += einsum("ija->ija", x157)
    x177 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x177 += einsum("ija,ikab->kjb", x157, t2.abab)
    del x157
    x215 += einsum("ija->ija", x177)
    del x177
    x158 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x158 += einsum("i,ja->ija", r1.b, t1.bb)
    x158 += einsum("ija->ija", r2.bbb)
    x158 += einsum("ija->jia", r2.bbb) * -1
    x159 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x159 += einsum("ija,kbia->kjb", x158, v.aabb.ovov)
    x161 += einsum("ija->ija", x159)
    r2new_aba += einsum("ija,ikba->kjb", x161, x56) * -1
    del x56
    del x161
    x180 += einsum("ija->ija", x159)
    del x159
    x181 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x181 += einsum("ija,ikab->jkb", x180, t2.abab)
    del x180
    x215 += einsum("ija->ija", x181) * -1
    del x181
    x163 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x163 += einsum("ija,ikba->jkb", x158, x12)
    del x12
    x166 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x166 += einsum("ija->jia", x163)
    x178 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x178 += einsum("ija->ija", x163)
    del x163
    x170 = np.zeros((nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x170 += einsum("ija,iabc->jbc", x158, v.bbaa.ovvv)
    x171 += einsum("ija,klia->klj", x158, v.aabb.ooov)
    x187 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x187 += einsum("ija,ikba->kjb", x158, x154)
    del x154
    x215 += einsum("ija->jia", x187) * -1
    del x187
    r2new_aba += einsum("ija,iabk->kjb", x158, v.bbaa.ovvo)
    del x158
    x162 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x162 += einsum("ija,iakb->jkb", r2.aba, v.aabb.ovov)
    x166 += einsum("ija->jia", x162)
    x178 += einsum("ija->ija", x162)
    x179 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x179 += einsum("ija,jkba->kib", x178, x150)
    del x178
    del x150
    x215 += einsum("ija->jia", x179) * -1
    del x179
    x208 += einsum("ija->ija", x162)
    del x162
    x209 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x209 += einsum("ia,jka->jki", t1.bb, x208)
    del x208
    x210 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x210 += einsum("ijk->jki", x209)
    del x209
    x164 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x164 += einsum("ijka->ikja", v.bbbb.ooov)
    x164 += einsum("ijka->kija", v.bbbb.ooov) * -1
    x165 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x165 += einsum("i,jika->jka", r1.b, x164)
    del x164
    x166 += einsum("ija->ija", x165) * -1
    r2new_aba += einsum("ija,kiba->kjb", x166, t2.abab)
    del x166
    x188 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x188 += einsum("ija,ikba->kjb", x165, x114) * -1
    del x114
    del x165
    x215 += einsum("ija->ija", x188) * -1
    del x188
    x167 += einsum("i,iabc->bca", r1.b, v.bbaa.ovvv)
    r2new_aba += einsum("abc,ijbc->ija", x167, t2.abab)
    del x167
    x168 += einsum("i,jkia->jka", r1.b, v.aabb.ooov)
    r2new_aba += einsum("ija,ikba->jkb", x168, t2.abab) * -1
    del x168
    x169 += einsum("iabj->ijba", v.aaaa.ovvo)
    x169 += einsum("ijab->ijab", v.aaaa.oovv) * -1
    r2new_aba += einsum("ija,ikba->kjb", r2.aba, x169)
    del x169
    x170 += einsum("i,ijab->jab", r1.b, v.bbaa.oovv)
    r2new_aba += einsum("ia,jba->ijb", t1.aa, x170)
    del x170
    x171 += einsum("i,jkil->jkl", r1.b, v.aabb.oooo)
    r2new_aba += einsum("ia,ijk->jka", t1.aa, x171) * -1
    del x171
    x172 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x172 += einsum("ijab->ijab", v.bbaa.oovv)
    x172 += einsum("ia,jabc->jibc", t1.bb, v.bbaa.ovvv)
    r2new_aba += einsum("ija,jkba->ikb", r2.aba, x172) * -1
    del x172
    x173 += einsum("ai->ia", f.aa.vo)
    r2new_aba += einsum("i,ja->jia", r1.b, x173) * -1
    del x173
    x174 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x174 += einsum("i,ijak->jka", r1.b, v.bbbb.oovo)
    x215 += einsum("ija->ija", x174) * -1
    del x174
    x175 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x175 += einsum("ij,ia->ja", f.bb.oo, t1.bb)
    x215 += einsum("i,ja->jia", r1.b, x175)
    del x175
    x176 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x176 += einsum("ija,iabk->jkb", r2.aba, v.aabb.ovvo)
    x215 += einsum("ija->ija", x176) * -1
    del x176
    x182 = np.zeros((nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x182 += einsum("i,iabc->bac", r1.b, v.bbbb.ovvv)
    x185 = np.zeros((nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x185 += einsum("abc->abc", x182) * -1
    x198 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x198 += einsum("ia,bac->ibc", t1.bb, x182)
    del x182
    x201 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x201 += einsum("iab->iab", x198)
    del x198
    x183 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x183 += einsum("ija->ija", r2.bbb)
    x183 += einsum("i,ja->ija", r1.b, t1.bb)
    x184 = np.zeros((nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x184 += einsum("ija,jbic->abc", x183, v.bbbb.ovov)
    del x183
    x185 += einsum("abc->acb", x184)
    del x184
    x186 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x186 += einsum("abc,ijcb->ija", x185, t2.bbbb)
    del x185
    x215 += einsum("ija->jia", x186)
    del x186
    x190 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x190 += einsum("ia,jkla->ijlk", t1.bb, v.bbbb.ooov)
    x191 += einsum("ijkl->jkli", x190)
    x191 += einsum("ijkl->kjli", x190) * -1
    del x190
    x191 += einsum("ijkl->kilj", v.bbbb.oooo)
    x192 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x192 += einsum("ija,jikl->kla", r2.bbb, x191)
    del x191
    x215 += einsum("ija->jia", x192)
    del x192
    x197 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x197 += einsum("ija,iabc->jbc", r2.aba, v.aabb.ovvv)
    x201 += einsum("iab->iab", x197)
    del x197
    x199 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x199 += einsum("ija->ija", r2.bbb) * -1
    x199 += einsum("ija->jia", r2.bbb)
    x200 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x200 += einsum("ija,jbac->ibc", x199, x124)
    del x124
    x201 += einsum("iab->iab", x200)
    del x200
    x202 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x202 += einsum("ia,jba->jib", t1.bb, x201)
    del x201
    x215 += einsum("ija->ija", x202) * -1
    del x202
    x212 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x212 += einsum("ij,kia->kja", f.bb.oo, x199)
    x215 += einsum("ija->jia", x212) * -1
    del x212
    x203 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x203 += einsum("i,jkil->jkl", r1.b, v.bbbb.oooo)
    x210 += einsum("ijk->ijk", x203)
    del x203
    x204 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x204 += einsum("ija,iakl->jkl", r2.aba, v.aabb.ovoo)
    x210 += einsum("ijk->jki", x204)
    del x204
    x205 += einsum("ijka->ikja", v.bbbb.ooov) * -1
    x205 += einsum("ijka->kija", v.bbbb.ooov)
    x206 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x206 += einsum("ija,jkla->ikl", x199, x205)
    del x205
    del x199
    x210 += einsum("ijk->jki", x206)
    del x206
    x211 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x211 += einsum("ia,ijk->jka", t1.bb, x210)
    del x210
    x215 += einsum("ija->jia", x211)
    del x211
    r2new_bbb = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    r2new_bbb += einsum("ija->ija", x215)
    r2new_bbb += einsum("ija->jia", x215) * -1
    del x215
    r1new_a -= einsum("i,ij->j", r1.a, f.aa.oo)
    r1new_b -= einsum("i,ij->j", r1.b, f.bb.oo)
    r2new_aaa -= einsum("i,aj->jia", r1.a, f.aa.vo)
    r2new_aaa += einsum("i,aj->ija", r1.a, f.aa.vo)
    r2new_bab += einsum("i,ijak->kja", r1.a, v.aabb.oovo)
    r2new_aba += einsum("i,ijak->kja", r1.b, v.bbaa.oovo)
    r2new_bbb -= einsum("i,aj->jia", r1.b, f.bb.vo)
    r2new_bbb += einsum("i,aj->ija", r1.b, f.bb.vo)

    r1new = Namespace(a=r1new_a, b=r1new_b)
    r2new = Namespace(aaa=r2new_aaa, aba=r2new_aba, bab=r2new_bab, bbb=r2new_bbb)

    return r1new, r2new

def hbar_matvec_ea(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, r1=None, r2=None, **kwargs):
    x0 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x0 += einsum("a,iajb->ijb", r1.a, v.aabb.ovov)
    r1new_a = np.zeros((nvir[0]), dtype=np.float64)
    r1new_a += einsum("ija,ijba->b", x0, t2.abab) * -1
    del x0
    x1 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x1 += einsum("abi->iab", r2.aaa)
    x1 += einsum("a,ib->iab", r1.a, t1.aa) * -1
    x2 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x2 += einsum("iabc->ibac", v.aaaa.ovvv) * -1
    x2 += einsum("iabc->ibca", v.aaaa.ovvv)
    x48 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x48 += einsum("ia,jbca->ijbc", t1.aa, x2)
    x49 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x49 += einsum("ijab->ijab", x48) * -1
    x159 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x159 += einsum("ijab->jiab", x48) * -1
    del x48
    x55 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x55 += einsum("a,ibca->ibc", r1.a, x2)
    x107 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x107 += einsum("iab->iab", x55) * -1
    x73 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x73 += einsum("ia,ibca->bc", t1.aa, x2)
    x76 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x76 += einsum("ab->ab", x73) * -1
    x120 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x120 += einsum("ab->ab", x73) * -1
    del x73
    x87 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x87 += einsum("abi,jcba->ijc", r2.aaa, x2)
    x90 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x90 += einsum("ija->jia", x87) * -1
    del x87
    r1new_a += einsum("iab,icab->c", x1, x2) * -1
    x3 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x3 += einsum("abi->iba", r2.bab)
    x3 += einsum("a,ib->iab", r1.a, t1.bb)
    x18 = np.zeros((nocc[0]), dtype=np.float64)
    x18 += einsum("iab,jaib->j", x3, v.aabb.ovov)
    x19 = np.zeros((nocc[0]), dtype=np.float64)
    x19 += einsum("i->i", x18)
    del x18
    x117 = np.zeros((nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x117 += einsum("iab,jaic->jbc", x3, v.aabb.ovov)
    x119 = np.zeros((nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x119 += einsum("iab,jakb->jki", x3, v.aabb.ovov)
    x136 = np.zeros((nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x136 += einsum("iab,jacb->jic", x3, v.aabb.ovvv)
    x137 = np.zeros((nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x137 += einsum("iab,jbca->jic", x3, v.bbaa.ovvv)
    r1new_a += einsum("iab,ibca->c", x3, v.bbaa.ovvv)
    r2new_bab = np.zeros((nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    r2new_bab += einsum("iab,cadb->dci", x3, v.aabb.vvvv) * -1
    del x3
    x4 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x4 += einsum("a,iajb->jib", r1.a, v.aaaa.ovov)
    x5 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x5 += einsum("ija->ija", x4)
    x5 += einsum("ija->jia", x4) * -1
    r1new_a += einsum("ija,ijab->b", x5, t2.aaaa) * -1
    del x5
    x66 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x66 += einsum("ia,jka->ikj", t1.aa, x4)
    del x4
    x67 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x67 += einsum("ijk->jki", x66) * -1
    del x66
    x6 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x6 += einsum("ia,jbia->jb", t1.bb, v.aabb.ovov)
    x9 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x9 += einsum("ia->ia", x6)
    del x6
    x7 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x7 += einsum("iajb->jiab", v.aaaa.ovov)
    x7 += einsum("iajb->jiba", v.aaaa.ovov) * -1
    x8 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x8 += einsum("ia,ijab->jb", t1.aa, x7)
    x9 += einsum("ia->ia", x8) * -1
    del x8
    x153 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x153 += einsum("abi,ijac->jcb", r2.aba, x7) * -1
    x9 += einsum("ia->ia", f.aa.ov)
    x144 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x144 += einsum("ia,ijab->jb", x9, t2.abab)
    x149 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x149 += einsum("ia->ia", x144)
    x197 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x197 += einsum("ia->ia", x144) * -1
    del x144
    r1new_b = np.zeros((nvir[1]), dtype=np.float64)
    r1new_b += einsum("ia,abi->b", x9, r2.aba)
    x10 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x10 += einsum("abi->iab", r2.aaa)
    x10 += einsum("abi->iba", r2.aaa) * -1
    x92 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x92 += einsum("ab,ibc->iac", f.aa.vv, x10)
    x104 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x104 += einsum("iab->iab", x92) * -1
    del x92
    r1new_a += einsum("ia,iba->b", x9, x10) * -1
    x11 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x11 += einsum("ia,iajb->jb", t1.aa, v.aabb.ovov)
    x14 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x14 += einsum("ia->ia", x11)
    del x11
    x12 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x12 += einsum("iajb->jiab", v.bbbb.ovov)
    x12 += einsum("iajb->jiba", v.bbbb.ovov) * -1
    x13 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x13 += einsum("ia,ijab->jb", t1.bb, x12)
    x14 += einsum("ia->ia", x13) * -1
    del x13
    x105 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x105 += einsum("abi,ijac->jbc", r2.bab, x12) * -1
    x14 += einsum("ia->ia", f.bb.ov)
    x99 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x99 += einsum("ia,jiba->jb", x14, t2.abab)
    x103 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum("ia->ia", x99) * -1
    x165 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x165 += einsum("ia->ia", x99)
    del x99
    r1new_a += einsum("ia,abi->b", x14, r2.bab)
    x15 = np.zeros((nocc[0]), dtype=np.float64)
    x15 += einsum("a,ia->i", r1.a, f.aa.ov)
    x19 += einsum("i->i", x15)
    del x15
    x16 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x16 += einsum("iajb->jiab", v.aaaa.ovov) * -1
    x16 += einsum("iajb->jiba", v.aaaa.ovov)
    x17 = np.zeros((nocc[0]), dtype=np.float64)
    x17 += einsum("iab,ijba->j", x1, x16)
    del x1
    x19 += einsum("i->i", x17) * -1
    del x17
    x86 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x86 += einsum("i,ijab->jab", x19, t2.aaaa)
    x104 += einsum("iab->iba", x86)
    del x86
    r1new_a += einsum("i,ia->a", x19, t1.aa) * -1
    r2new_bab += einsum("i,ijab->baj", x19, t2.abab)
    del x19
    x174 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x174 += einsum("abi,ijac->jcb", r2.aba, x16)
    x175 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x175 += einsum("iab->iab", x174) * -1
    del x174
    x20 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x20 += einsum("a,ibja->ijb", r1.b, v.aabb.ovov)
    r1new_b += einsum("ija,ijab->b", x20, t2.abab) * -1
    del x20
    x21 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x21 += einsum("abi->iab", r2.bbb)
    x21 += einsum("a,ib->iab", r1.b, t1.bb) * -1
    x181 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x181 += einsum("iab,jbka->jki", x21, v.bbbb.ovov)
    x182 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x182 += einsum("ijk->jik", x181)
    del x181
    x187 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x187 += einsum("iab,cbda->icd", x21, v.bbbb.vvvv)
    x198 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x198 += einsum("iab->iba", x187) * -1
    del x187
    x22 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x22 += einsum("iabc->ibac", v.bbbb.ovvv)
    x22 += einsum("iabc->ibca", v.bbbb.ovvv) * -1
    x116 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x116 += einsum("ia,jbac->jibc", t1.bb, x22) * -1
    x125 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x125 += einsum("ia,ibac->bc", t1.bb, x22)
    x127 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x127 += einsum("ab->ab", x125) * -1
    x184 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x184 += einsum("ab->ab", x125) * -1
    del x125
    x156 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x156 += einsum("a,ibac->ibc", r1.b, x22)
    x157 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x157 += einsum("iab->iab", x156) * -1
    r1new_b += einsum("iab,icba->c", x21, x22) * -1
    x23 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x23 += einsum("abi->iab", r2.aba)
    x23 += einsum("a,ib->iba", r1.b, t1.aa)
    x30 = np.zeros((nocc[1]), dtype=np.float64)
    x30 += einsum("iab,iajb->j", x23, v.aabb.ovov)
    x31 = np.zeros((nocc[1]), dtype=np.float64)
    x31 += einsum("i->i", x30)
    del x30
    x160 = np.zeros((nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x160 += einsum("iab,icjb->jac", x23, v.aabb.ovov)
    x162 = np.zeros((nocc[0], nocc[0], nocc[1]), dtype=np.float64)
    x162 += einsum("iab,jakb->jik", x23, v.aabb.ovov)
    x163 = np.zeros((nocc[0], nocc[0], nvir[1]), dtype=np.float64)
    x163 += einsum("iab,jacb->jic", x23, v.aabb.ovvv)
    x164 = np.zeros((nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    x164 += einsum("iab,jbca->ijc", x23, v.bbaa.ovvv)
    r1new_b += einsum("iab,iacb->c", x23, v.aabb.ovvv)
    r2new_aba = np.zeros((nvir[0], nvir[1], nocc[0]), dtype=np.float64)
    r2new_aba += einsum("iab,cadb->cdi", x23, v.aabb.vvvv) * -1
    del x23
    x24 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x24 += einsum("a,iajb->jib", r1.b, v.bbbb.ovov)
    x25 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x25 += einsum("ija->ija", x24) * -1
    x25 += einsum("ija->jia", x24)
    del x24
    r1new_b += einsum("ija,jiab->b", x25, t2.bbbb) * -1
    del x25
    x26 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x26 += einsum("abi->iab", r2.bbb)
    x26 += einsum("abi->iba", r2.bbb) * -1
    r1new_b += einsum("ia,iba->b", x14, x26) * -1
    del x26
    x27 = np.zeros((nocc[1]), dtype=np.float64)
    x27 += einsum("a,ia->i", r1.b, f.bb.ov)
    x31 += einsum("i->i", x27)
    del x27
    x28 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x28 += einsum("iajb->jiab", v.bbbb.ovov) * -1
    x28 += einsum("iajb->jiba", v.bbbb.ovov)
    x29 = np.zeros((nocc[1]), dtype=np.float64)
    x29 += einsum("iab,ijba->j", x21, x28)
    del x21
    x31 += einsum("i->i", x29) * -1
    del x29
    x188 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x188 += einsum("i,ijab->jab", x31, t2.bbbb)
    x198 += einsum("iab->iba", x188)
    del x188
    r1new_b += einsum("i,ia->a", x31, t1.bb) * -1
    r2new_aba += einsum("i,jiab->abj", x31, t2.abab)
    del x31
    x52 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x52 += einsum("abi,ijac->jbc", r2.bab, x28)
    x53 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x53 += einsum("iab->iab", x52) * -1
    del x52
    x32 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x32 += einsum("a,bica->ibc", r1.a, v.aaaa.vovv)
    x104 += einsum("iab->iab", x32) * -1
    del x32
    x33 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x33 += einsum("ab,ib->ia", f.aa.vv, t1.aa)
    x104 += einsum("a,ib->iba", r1.a, x33) * -1
    x165 += einsum("ia->ia", x33)
    del x33
    x34 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x34 += einsum("abi,cbda->idc", r2.aaa, v.aaaa.vvvv)
    x104 += einsum("iab->iab", x34) * -1
    del x34
    x35 = np.zeros((nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x35 += einsum("a,bcda->bdc", r1.a, v.aaaa.vvvv)
    x36 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x36 += einsum("ia,bca->icb", t1.aa, x35)
    del x35
    x104 += einsum("iab->iab", x36)
    del x36
    x37 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x37 += einsum("a,ibca->icb", r1.a, v.bbaa.ovvv)
    x38 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x38 += einsum("iab,jicb->jca", x37, t2.abab)
    x104 += einsum("iab->iab", x38) * -1
    del x38
    x105 += einsum("iab->iab", x37)
    del x37
    x39 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x39 += einsum("abi,jcia->jbc", r2.bab, v.aabb.ovov)
    x42 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x42 += einsum("iab->iab", x39)
    x107 += einsum("iab->iab", x39)
    del x39
    x40 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x40 += einsum("a,ib->iab", r1.a, t1.aa)
    x40 += einsum("abi->iab", r2.aaa) * -1
    x40 += einsum("abi->iba", r2.aaa)
    x41 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum("iab,ijca->jcb", x40, x7)
    x42 += einsum("iab->iba", x41) * -1
    x107 += einsum("iab->iba", x41) * -1
    del x41
    r2new_bab += einsum("iab,ijbc->caj", x107, t2.abab) * -1
    del x107
    x51 = np.zeros((nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x51 += einsum("iab,iajc->jbc", x40, v.aabb.ovov)
    del x40
    x53 += einsum("iab->iab", x51)
    x54 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x54 += einsum("iab,jicb->jca", x53, t2.abab)
    del x53
    x104 += einsum("iab->iba", x54) * -1
    del x54
    x105 += einsum("iab->iab", x51) * -1
    del x51
    x43 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x43 += einsum("ijab->jiab", t2.aaaa)
    x43 += einsum("ijab->jiba", t2.aaaa) * -1
    x44 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x44 += einsum("iab,ijbc->jac", x42, x43)
    del x42
    x104 += einsum("iab->iab", x44) * -1
    del x44
    x165 += einsum("ia,ijab->jb", x9, x43) * -1
    x45 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x45 += einsum("ia,jakb->ikjb", t1.aa, v.aaaa.ovov)
    x46 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x46 += einsum("ijka->ijka", x45) * -1
    x46 += einsum("ijka->ikja", x45)
    del x45
    x46 += einsum("ijka->jika", v.aaaa.ooov)
    x46 += einsum("ijka->jkia", v.aaaa.ooov) * -1
    x47 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x47 += einsum("ia,jikb->jkab", t1.aa, x46)
    x49 += einsum("ijab->ijab", x47) * -1
    x159 += einsum("ijab->jiab", x47) * -1
    del x47
    x94 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x94 += einsum("ijab,kija->kb", t2.aaaa, x46)
    x103 += einsum("ia->ia", x94) * -1
    del x94
    x165 += einsum("ijab,kjia->kb", t2.aaaa, x46) * -1
    del x46
    x49 += einsum("iabj->jiba", v.aaaa.ovvo)
    x49 += einsum("ijab->jiab", v.aaaa.oovv) * -1
    x50 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x50 += einsum("iab,jica->jbc", x10, x49)
    del x49
    x104 += einsum("iab->iab", x50)
    del x50
    x56 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x56 += einsum("ia,jb->ijab", t1.aa, t1.aa)
    x56 += einsum("ijab->jiab", t2.aaaa) * -1
    x56 += einsum("ijab->jiba", t2.aaaa)
    x57 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x57 += einsum("iab,ijcb->jca", x55, x56) * -1
    del x56
    del x55
    x104 += einsum("iab->iab", x57)
    del x57
    x58 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x58 += einsum("ia,jbca->ijcb", t1.aa, v.bbaa.ovvv)
    x62 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x62 += einsum("ijab->ijab", x58)
    del x58
    x59 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x59 += einsum("ia,jakb->ijkb", t1.aa, v.aabb.ovov)
    x60 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x60 += einsum("ijka->jika", x59)
    del x59
    x60 += einsum("ijka->ijka", v.aabb.ooov)
    x61 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x61 += einsum("ia,ijkb->jkab", t1.aa, x60)
    x62 += einsum("ijab->ijab", x61) * -1
    del x61
    x96 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x96 += einsum("ijab,ikjb->ka", t2.abab, x60)
    x103 += einsum("ia->ia", x96)
    x165 += einsum("ia->ia", x96) * -1
    del x96
    x161 = np.zeros((nocc[0], nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x161 += einsum("ia,jkib->jkab", t1.bb, x60) * -1
    del x60
    x62 += einsum("iabj->jiba", v.bbaa.ovvo)
    x63 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum("abi,jica->jbc", r2.bab, x62)
    x104 += einsum("iab->iab", x63)
    del x63
    x64 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x64 += einsum("a,ijka->ikj", r1.a, v.aaaa.ooov)
    x67 += einsum("ijk->ijk", x64)
    del x64
    x65 = np.zeros((nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x65 += einsum("abi,jbka->ikj", r2.aaa, v.aaaa.ovov)
    x67 += einsum("ijk->jki", x65)
    del x65
    x68 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum("ijab->jiba", t2.aaaa)
    x68 += einsum("ia,jb->ijab", t1.aa, t1.aa)
    x69 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x69 += einsum("ijk,jiab->kab", x67, x68)
    del x67
    x104 += einsum("iab->iba", x69) * -1
    del x69
    x72 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x72 += einsum("ijab,ijac->bc", x68, x7)
    del x7
    x76 += einsum("ab->ab", x72) * -1
    x120 += einsum("ab->ab", x72) * -1
    del x72
    x80 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x80 += einsum("ijab,ikba->kj", x16, x68)
    del x16
    x84 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x84 += einsum("ij->ji", x80) * -1
    del x80
    x95 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x95 += einsum("iabc,ijcb->ja", x2, x68)
    x103 += einsum("ia->ia", x95) * -1
    del x95
    x165 += einsum("iabc,ijbc->ja", x2, x68) * -1
    del x2
    del x68
    x70 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum("ia,ib->ab", f.aa.ov, t1.aa)
    x76 += einsum("ab->ba", x70)
    x120 += einsum("ab->ba", x70)
    del x70
    x71 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum("ia,iabc->bc", t1.bb, v.bbaa.ovvv)
    x76 += einsum("ab->ab", x71) * -1
    x120 += einsum("ab->ab", x71) * -1
    del x71
    x74 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x74 += einsum("ijab->ijab", t2.abab)
    x74 += einsum("ia,jb->ijab", t1.aa, t1.bb)
    x75 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x75 += einsum("iajb,ijcb->ca", v.aabb.ovov, x74)
    x76 += einsum("ab->ab", x75)
    x77 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x77 += einsum("ab,ibc->iac", x76, x10)
    del x10
    del x76
    x104 += einsum("iab->iba", x77) * -1
    del x77
    x120 += einsum("ab->ab", x75)
    del x75
    x83 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x83 += einsum("iajb,kjab->ki", v.aabb.ovov, x74)
    x84 += einsum("ij->ji", x83)
    del x83
    x100 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x100 += einsum("iabc,jica->jb", v.bbaa.ovvv, x74)
    x103 += einsum("ia->ia", x100) * -1
    x165 += einsum("ia->ia", x100)
    del x100
    x126 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x126 += einsum("iajb,ijac->cb", v.aabb.ovov, x74)
    x127 += einsum("ab->ab", x126)
    x184 += einsum("ab->ab", x126)
    del x126
    x134 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x134 += einsum("iajb,ikab->kj", v.aabb.ovov, x74)
    x135 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x135 += einsum("ij->ji", x134)
    del x134
    x145 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x145 += einsum("iabc,ijac->jb", v.aabb.ovvv, x74)
    x149 += einsum("ia->ia", x145)
    x197 += einsum("ia->ia", x145) * -1
    del x145
    x78 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x78 += einsum("ia,ja->ij", f.aa.ov, t1.aa)
    x84 += einsum("ij->ij", x78)
    del x78
    x79 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x79 += einsum("ia,jkia->jk", t1.bb, v.aabb.ooov)
    x84 += einsum("ij->ij", x79)
    del x79
    x81 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x81 += einsum("ijka->ikja", v.aaaa.ooov) * -1
    x81 += einsum("ijka->kija", v.aaaa.ooov)
    x82 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x82 += einsum("ia,jika->jk", t1.aa, x81)
    del x81
    x84 += einsum("ij->ij", x82) * -1
    del x82
    x84 += einsum("ij->ij", f.aa.oo)
    x85 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x85 += einsum("ij,abi->jab", x84, r2.aaa)
    x104 += einsum("iab->iab", x85)
    del x85
    x102 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum("ia,ij->ja", t1.aa, x84)
    x103 += einsum("ia->ia", x102)
    x165 += einsum("ia->ia", x102) * -1
    del x102
    r2new_aba += einsum("ij,abi->abj", x84, r2.aba)
    del x84
    x88 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x88 += einsum("iabj->ijba", v.aaaa.ovvo)
    x88 += einsum("ijab->ijab", v.aaaa.oovv) * -1
    x89 = np.zeros((nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x89 += einsum("a,ijba->ijb", r1.a, x88)
    x90 += einsum("ija->ija", x89)
    del x89
    x91 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x91 += einsum("ia,ijb->jba", t1.aa, x90)
    del x90
    x104 += einsum("iab->iba", x91) * -1
    del x91
    x101 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x101 += einsum("ia,ijba->jb", t1.aa, x88)
    del x88
    x103 += einsum("ia->ia", x101) * -1
    x165 += einsum("ia->ia", x101)
    del x101
    x93 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x93 += einsum("ia,iabj->jb", t1.bb, v.bbaa.ovvo)
    x103 += einsum("ia->ia", x93) * -1
    x165 += einsum("ia->ia", x93)
    del x93
    x97 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x97 += einsum("ijab->jiab", t2.aaaa) * -1
    x97 += einsum("ijab->jiba", t2.aaaa)
    x98 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x98 += einsum("ia,ijab->jb", x9, x97)
    del x9
    del x97
    x103 += einsum("ia->ia", x98) * -1
    del x98
    x104 += einsum("a,ib->iab", r1.a, x103) * -1
    del x103
    r2new_aaa = np.zeros((nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    r2new_aaa += einsum("iab->abi", x104)
    r2new_aaa += einsum("iab->bai", x104) * -1
    del x104
    x106 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x106 += einsum("ijab->jiab", t2.bbbb) * -1
    x106 += einsum("ijab->jiba", t2.bbbb)
    x196 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x196 += einsum("ia,ijab->jb", x14, x106)
    x197 += einsum("ia->ia", x196) * -1
    del x196
    r2new_bab += einsum("iab,ijbc->caj", x105, x106) * -1
    del x105
    x108 = np.zeros((nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x108 += einsum("abi->iab", r2.aaa) * -1
    x108 += einsum("abi->iba", r2.aaa)
    x109 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x109 += einsum("ia,jbca->jibc", t1.bb, v.aabb.ovvv)
    x113 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x113 += einsum("ijab->ijab", x109)
    del x109
    x110 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x110 += einsum("ia,jbka->jikb", t1.bb, v.aabb.ovov)
    x111 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x111 += einsum("ijka->ikja", x110)
    del x110
    x111 += einsum("iajk->ijka", v.aabb.ovoo)
    x112 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x112 += einsum("ia,jikb->jkba", t1.bb, x111)
    x113 += einsum("ijab->ijab", x112) * -1
    del x112
    x118 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x118 += einsum("ia,ijkb->jkab", t1.aa, x111) * -1
    x142 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x142 += einsum("ijab,ijka->kb", t2.abab, x111)
    del x111
    x149 += einsum("ia->ia", x142) * -1
    x197 += einsum("ia->ia", x142)
    del x142
    x113 += einsum("iabj->ijab", v.aabb.ovvo)
    x179 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x179 += einsum("abi,ijac->jcb", r2.aba, x113)
    x198 += einsum("iab->iba", x179)
    del x179
    r2new_bab += einsum("iab,ijbc->caj", x108, x113) * -1
    del x113
    del x108
    x114 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x114 += einsum("ia,jbka->ijkb", t1.bb, v.bbbb.ovov)
    x115 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x115 += einsum("ijka->ijka", x114)
    x115 += einsum("ijka->ikja", x114) * -1
    x140 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x140 += einsum("ijka->ijka", x114) * -1
    x140 += einsum("ijka->ikja", x114)
    del x114
    x115 += einsum("ijka->jika", v.bbbb.ooov) * -1
    x115 += einsum("ijka->jkia", v.bbbb.ooov)
    x116 += einsum("ia,jkib->kjab", t1.bb, x115) * -1
    del x115
    x116 += einsum("iabj->ijba", v.bbbb.ovvo)
    x116 += einsum("ijab->ijab", v.bbbb.oovv) * -1
    r2new_bab += einsum("abi,ijca->cbj", r2.bab, x116) * -1
    del x116
    x117 += einsum("a,iabc->ibc", r1.a, v.aabb.ovvv) * -1
    r2new_bab += einsum("iab,ijcb->acj", x117, t2.abab) * -1
    del x117
    x118 += einsum("ijab->ijab", v.bbaa.oovv)
    x118 += einsum("ia,jabc->jibc", t1.bb, v.bbaa.ovvv)
    r2new_bab += einsum("abi,ijcb->acj", r2.bab, x118)
    del x118
    x119 += einsum("a,iajk->ijk", r1.a, v.aabb.ovoo)
    r2new_bab += einsum("ijk,ijab->bak", x119, x74) * -1
    del x119
    x120 += einsum("ab->ab", f.aa.vv) * -1
    r2new_bab += einsum("ab,cbi->cai", x120, r2.bab)
    r2new_aba += einsum("ab,bci->aci", x120, r2.aba)
    del x120
    x121 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x121 += einsum("ia,ib->ab", f.bb.ov, t1.bb)
    x127 += einsum("ab->ba", x121)
    x184 += einsum("ab->ba", x121)
    del x121
    x122 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x122 += einsum("ia,iabc->bc", t1.aa, v.aabb.ovvv)
    x127 += einsum("ab->ab", x122) * -1
    x184 += einsum("ab->ab", x122) * -1
    del x122
    x123 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x123 += einsum("ijab->jiba", t2.bbbb)
    x123 += einsum("ia,jb->ijab", t1.bb, t1.bb)
    x124 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x124 += einsum("ijab,ijca->bc", x123, x28)
    x127 += einsum("ab->ab", x124) * -1
    x184 += einsum("ab->ab", x124) * -1
    del x124
    x127 += einsum("ab->ab", f.bb.vv) * -1
    r2new_bab += einsum("ab,bci->aci", x127, r2.bab)
    r2new_aba += einsum("ab,cbi->cai", x127, r2.aba)
    del x127
    x128 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x128 += einsum("ia,ja->ij", f.bb.ov, t1.bb)
    x135 += einsum("ij->ij", x128)
    del x128
    x129 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x129 += einsum("ia,iajk->jk", t1.aa, v.aabb.ovoo)
    x135 += einsum("ij->ij", x129)
    del x129
    x130 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x130 += einsum("ijab->jiba", t2.bbbb)
    x130 += einsum("ia,jb->ijba", t1.bb, t1.bb) * -1
    x131 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x131 += einsum("ijab,ikba->jk", x130, x28)
    del x28
    x135 += einsum("ij->ji", x131) * -1
    del x131
    x195 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x195 += einsum("ijab,icab->jc", x130, x22)
    del x22
    x197 += einsum("ia->ia", x195) * -1
    del x195
    x132 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x132 += einsum("ijka->ikja", v.bbbb.ooov) * -1
    x132 += einsum("ijka->kija", v.bbbb.ooov)
    x133 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x133 += einsum("ia,jika->jk", t1.bb, x132)
    del x132
    x135 += einsum("ij->ij", x133) * -1
    del x133
    x135 += einsum("ij->ij", f.bb.oo)
    x148 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x148 += einsum("ia,ij->ja", t1.bb, x135)
    x149 += einsum("ia->ia", x148) * -1
    x197 += einsum("ia->ia", x148)
    del x148
    x186 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x186 += einsum("ij,abi->jab", x135, r2.bbb)
    x198 += einsum("iab->iab", x186)
    del x186
    r2new_bab += einsum("ij,abi->abj", x135, r2.bab)
    del x135
    x136 += einsum("a,iabj->ijb", r1.a, v.aabb.ovvo)
    r2new_bab += einsum("ia,ijb->baj", t1.aa, x136)
    del x136
    x137 += einsum("a,ijba->ijb", r1.a, v.bbaa.oovv)
    r2new_bab += einsum("ia,ijb->abj", t1.bb, x137)
    del x137
    x138 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x138 += einsum("ab,ib->ia", f.bb.vv, t1.bb)
    x149 += einsum("ia->ia", x138)
    x198 += einsum("a,ib->iba", r1.b, x138) * -1
    del x138
    x139 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x139 += einsum("ia,iabj->jb", t1.aa, v.aabb.ovvo)
    x149 += einsum("ia->ia", x139)
    x197 += einsum("ia->ia", x139) * -1
    del x139
    x140 += einsum("ijka->jika", v.bbbb.ooov)
    x140 += einsum("ijka->jkia", v.bbbb.ooov) * -1
    x149 += einsum("ijab,kjia->kb", t2.bbbb, x140) * -1
    x170 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x170 += einsum("ia,jikb->jkba", t1.bb, x140)
    x172 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x172 += einsum("ijab->ijba", x170) * -1
    del x170
    x194 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x194 += einsum("ijab,kija->kb", t2.bbbb, x140)
    del x140
    x197 += einsum("ia->ia", x194) * -1
    del x194
    x141 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x141 += einsum("iabc->ibac", v.bbbb.ovvv) * -1
    x141 += einsum("iabc->ibca", v.bbbb.ovvv)
    x149 += einsum("ijab,icab->jc", x130, x141) * -1
    del x130
    x171 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x171 += einsum("ia,jbca->jibc", t1.bb, x141)
    x172 += einsum("ijab->jiab", x171) * -1
    del x171
    x189 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x189 += einsum("abi,jcba->jic", r2.bbb, x141)
    del x141
    x191 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x191 += einsum("ija->ija", x189) * -1
    del x189
    x143 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x143 += einsum("ijab->jiab", t2.bbbb)
    x143 += einsum("ijab->jiba", t2.bbbb) * -1
    x149 += einsum("ia,ijab->jb", x14, x143) * -1
    del x14
    del x143
    x146 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x146 += einsum("iabj->ijba", v.bbbb.ovvo)
    x146 += einsum("ijab->ijab", v.bbbb.oovv) * -1
    x147 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x147 += einsum("ia,ijba->jb", t1.bb, x146)
    x149 += einsum("ia->ia", x147)
    x197 += einsum("ia->ia", x147) * -1
    del x147
    x198 += einsum("a,ib->iab", r1.b, x197) * -1
    del x197
    x190 = np.zeros((nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x190 += einsum("a,ijba->ijb", r1.b, x146)
    del x146
    x191 += einsum("ija->ija", x190)
    del x190
    x192 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x192 += einsum("ia,ijb->jba", t1.bb, x191)
    del x191
    x198 += einsum("iab->iba", x192) * -1
    del x192
    x149 += einsum("ai->ia", f.bb.vo)
    r2new_bab += einsum("a,ib->bai", r1.a, x149) * -1
    del x149
    x150 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x150 += einsum("a,ibca->ibc", r1.b, v.aabb.ovvv)
    x153 += einsum("iab->iab", x150)
    x167 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x167 += einsum("iab,ijac->jcb", x150, t2.abab)
    del x150
    x198 += einsum("iab->iab", x167) * -1
    del x167
    x151 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x151 += einsum("a,ib->iab", r1.b, t1.bb)
    x151 += einsum("abi->iab", r2.bbb) * -1
    x151 += einsum("abi->iba", r2.bbb)
    x152 = np.zeros((nocc[0], nvir[0], nvir[1]), dtype=np.float64)
    x152 += einsum("iab,jcia->jcb", x151, v.aabb.ovov)
    x153 += einsum("iab->iab", x152) * -1
    r2new_aba += einsum("iab,ijac->cbj", x153, x43)
    del x153
    del x43
    x175 += einsum("iab->iab", x152)
    del x152
    x176 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x176 += einsum("iab,ijac->jbc", x175, t2.abab)
    del x175
    x198 += einsum("iab->iab", x176) * -1
    del x176
    x155 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x155 += einsum("iab,ijca->jbc", x151, x12)
    del x12
    del x151
    x157 += einsum("iab->iab", x155) * -1
    x168 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x168 += einsum("iab->iab", x155) * -1
    del x155
    x154 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x154 += einsum("abi,iajc->jbc", r2.aba, v.aabb.ovov)
    x157 += einsum("iab->iab", x154)
    r2new_aba += einsum("iab,jicb->caj", x157, t2.abab) * -1
    del x157
    x168 += einsum("iab->iab", x154)
    del x154
    x169 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x169 += einsum("iab,ijcb->jca", x168, x106)
    del x168
    del x106
    x198 += einsum("iab->iba", x169) * -1
    del x169
    x158 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x158 += einsum("abi->iab", r2.bbb) * -1
    x158 += einsum("abi->iba", r2.bbb)
    x185 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x185 += einsum("ab,icb->ica", x184, x158)
    del x184
    x198 += einsum("iab->iab", x185) * -1
    del x185
    x193 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x193 += einsum("ab,icb->ica", f.bb.vv, x158)
    x198 += einsum("iab->iba", x193) * -1
    del x193
    r2new_aba += einsum("iab,jicb->caj", x158, x62) * -1
    del x62
    x159 += einsum("iabj->ijba", v.aaaa.ovvo)
    x159 += einsum("ijab->ijab", v.aaaa.oovv) * -1
    r2new_aba += einsum("abi,ijca->cbj", r2.aba, x159) * -1
    del x159
    x160 += einsum("a,iabc->ibc", r1.b, v.bbaa.ovvv) * -1
    r2new_aba += einsum("iab,jibc->acj", x160, t2.abab) * -1
    del x160
    x161 += einsum("ijab->ijab", v.aabb.oovv)
    x161 += einsum("ia,jabc->jibc", t1.aa, v.aabb.ovvv)
    r2new_aba += einsum("abi,ijcb->acj", r2.aba, x161)
    del x161
    x162 += einsum("a,ijka->ijk", r1.b, v.aabb.ooov)
    r2new_aba += einsum("ijk,ikab->abj", x162, x74) * -1
    del x162
    del x74
    x163 += einsum("a,ijba->ijb", r1.b, v.aabb.oovv)
    r2new_aba += einsum("ia,ijb->abj", t1.aa, x163)
    del x163
    x164 += einsum("a,iabj->jib", r1.b, v.bbaa.ovvo)
    r2new_aba += einsum("ia,jib->baj", t1.bb, x164)
    del x164
    x165 += einsum("ai->ia", f.aa.vo)
    r2new_aba += einsum("a,ib->bai", r1.b, x165) * -1
    del x165
    x166 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x166 += einsum("a,bica->ibc", r1.b, v.bbbb.vovv)
    x198 += einsum("iab->iab", x166) * -1
    del x166
    x172 += einsum("iabj->jiba", v.bbbb.ovvo)
    x172 += einsum("ijab->jiab", v.bbbb.oovv) * -1
    x173 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x173 += einsum("iab,jicb->jac", x158, x172)
    del x172
    del x158
    x198 += einsum("iab->iab", x173)
    del x173
    x177 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x177 += einsum("ia,jb->ijab", t1.bb, t1.bb)
    x177 += einsum("ijab->jiab", t2.bbbb) * -1
    x177 += einsum("ijab->jiba", t2.bbbb)
    x178 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x178 += einsum("iab,ijcb->jca", x156, x177) * -1
    del x177
    del x156
    x198 += einsum("iab->iab", x178)
    del x178
    x180 = np.zeros((nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x180 += einsum("a,ijka->ikj", r1.b, v.bbbb.ooov)
    x182 += einsum("ijk->ijk", x180)
    del x180
    x183 = np.zeros((nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x183 += einsum("ijk,jiab->kab", x182, x123)
    del x123
    del x182
    x198 += einsum("iab->iba", x183) * -1
    del x183
    r2new_bbb = np.zeros((nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    r2new_bbb += einsum("iab->abi", x198)
    r2new_bbb += einsum("iab->bai", x198) * -1
    del x198
    r1new_a += einsum("a,ba->b", r1.a, f.aa.vv)
    r1new_b += einsum("a,ba->b", r1.b, f.bb.vv)
    r2new_aaa -= einsum("a,bi->bai", r1.a, f.aa.vo)
    r2new_aaa += einsum("a,bi->abi", r1.a, f.aa.vo)
    r2new_bab -= einsum("a,baci->cbi", r1.a, v.aabb.vvvo)
    r2new_aba -= einsum("a,bica->bci", r1.b, v.aabb.vovv)
    r2new_bbb -= einsum("a,bi->bai", r1.b, f.bb.vo)
    r2new_bbb += einsum("a,bi->abi", r1.b, f.bb.vo)

    r1new = Namespace(a=r1new_a, b=r1new_b)
    r2new = Namespace(aaa=r2new_aaa, aba=r2new_aba, bab=r2new_bab, bbb=r2new_bbb)

    r2new.aaa *= -1
    r2new.aba *= -1
    r2new.bab *= -1
    r2new.bbb *= -1

    return r1new, r2new

def make_ee_mom_kets(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):  # pragma: no cover
    delta_oo = Namespace()
    delta_oo.aa = np.eye(nocc[0])
    delta_oo.bb = np.eye(nocc[1])
    delta_vv = Namespace()
    delta_vv.aa = np.eye(nvir[0])
    delta_vv.bb = np.eye(nvir[1])

    ketee1_oo_aaaa = np.zeros((nocc[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    ketee1_oo_aaaa -= einsum("ij,ka->jaki", delta_oo.aa, t1.aa)
    ketee1_oo_bbbb = np.zeros((nocc[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    ketee1_oo_bbbb -= einsum("ij,ka->jaki", delta_oo.bb, t1.bb)
    ketee1_ov_aaaa = np.zeros((nocc[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    ketee1_ov_aaaa -= einsum("ia,jb->iajb", t1.aa, t1.aa)
    ketee1_ov_aaaa -= einsum("ijab->jaib", t2.aaaa)
    ketee1_ov_aaaa += einsum("ijab->jbia", t2.aaaa)
    ketee1_ov_bbbb = np.zeros((nocc[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    ketee1_ov_bbbb -= einsum("ia,jb->iajb", t1.bb, t1.bb)
    ketee1_ov_bbbb -= einsum("ijab->jaib", t2.bbbb)
    ketee1_ov_bbbb += einsum("ijab->jbia", t2.bbbb)
    ketee1_ov_bbaa = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    ketee1_ov_bbaa -= einsum("ia,jb->jbia", t1.aa, t1.bb)
    ketee1_ov_bbaa += einsum("ijab->jbia", t2.abab)
    ketee1_ov_aabb = np.zeros((nocc[0], nvir[0], nocc[1], nvir[1]), dtype=np.float64)
    ketee1_ov_aabb -= einsum("ia,jb->iajb", t1.aa, t1.bb)
    ketee1_ov_aabb += einsum("ijab->iajb", t2.abab)
    ketee1_vo_aaaa = np.zeros((nocc[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    ketee1_vo_aaaa += einsum("ab,ij->jbai", delta_vv.aa, delta_oo.aa)
    ketee1_vo_bbbb = np.zeros((nocc[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    ketee1_vo_bbbb += einsum("ab,ij->jbai", delta_vv.bb, delta_oo.bb)
    ketee1_vv_aaaa = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    ketee1_vv_aaaa += einsum("ab,ic->ibac", delta_vv.aa, t1.aa)
    ketee1_vv_bbbb = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    ketee1_vv_bbbb += einsum("ab,ic->ibac", delta_vv.bb, t1.bb)
    ketee2_oo_aaaaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    ketee2_oo_aaaaaa -= einsum("ij,klab->jlabki", delta_oo.aa, t2.aaaa)
    ketee2_oo_aaaaaa += einsum("ij,klab->jlbaki", delta_oo.aa, t2.aaaa)
    ketee2_oo_aaaaaa += einsum("ij,klab->ljabki", delta_oo.aa, t2.aaaa)
    ketee2_oo_aaaaaa -= einsum("ij,klab->ljbaki", delta_oo.aa, t2.aaaa)
    ketee2_oo_babaaa = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    ketee2_oo_babaaa -= einsum("ij,klab->ljbaki", delta_oo.aa, t2.abab)
    ketee2_oo_ababbb = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    ketee2_oo_ababbb -= einsum("ij,klab->kjabli", delta_oo.bb, t2.abab)
    ketee2_oo_bbbbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    ketee2_oo_bbbbbb -= einsum("ij,klab->jlabki", delta_oo.bb, t2.bbbb)
    ketee2_oo_bbbbbb += einsum("ij,klab->jlbaki", delta_oo.bb, t2.bbbb)
    ketee2_oo_bbbbbb += einsum("ij,klab->ljabki", delta_oo.bb, t2.bbbb)
    ketee2_oo_bbbbbb -= einsum("ij,klab->ljbaki", delta_oo.bb, t2.bbbb)
    ketee2_oo_ababaa = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    ketee2_oo_ababaa -= einsum("ij,klab->jlabki", delta_oo.aa, t2.abab)
    ketee2_oo_bababb = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nocc[1], nocc[1]), dtype=np.float64)
    ketee2_oo_bababb -= einsum("ij,klab->jkbali", delta_oo.bb, t2.abab)
    ketee2_ov_aaaaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    ketee2_ov_aaaaaa -= einsum("ia,jkbc->ikbcja", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa += einsum("ia,jkbc->ikcbja", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa += einsum("ia,jkbc->kibcja", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa -= einsum("ia,jkbc->kicbja", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa -= einsum("ia,jkbc->kjabic", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa += einsum("ia,jkbc->kjacib", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa += einsum("ia,jkbc->kjbaic", t1.aa, t2.aaaa)
    ketee2_ov_aaaaaa -= einsum("ia,jkbc->kjcaib", t1.aa, t2.aaaa)
    ketee2_ov_bbbbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    ketee2_ov_bbbbbb -= einsum("ia,jkbc->ikbcja", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb += einsum("ia,jkbc->ikcbja", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb += einsum("ia,jkbc->kibcja", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb -= einsum("ia,jkbc->kicbja", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb -= einsum("ia,jkbc->kjabic", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb += einsum("ia,jkbc->kjacib", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb += einsum("ia,jkbc->kjbaic", t1.bb, t2.bbbb)
    ketee2_ov_bbbbbb -= einsum("ia,jkbc->kjcaib", t1.bb, t2.bbbb)
    ketee2_ov_ababaa = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    ketee2_ov_ababaa -= einsum("ia,jkbc->ikbcja", t1.aa, t2.abab)
    ketee2_ov_ababaa -= einsum("ia,jkbc->jkacib", t1.aa, t2.abab)
    ketee2_ov_bababb = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nocc[1], nvir[1]), dtype=np.float64)
    ketee2_ov_bababb -= einsum("ia,jkbc->ijcbka", t1.bb, t2.abab)
    ketee2_ov_bababb -= einsum("ia,jkbc->kjabic", t1.bb, t2.abab)
    ketee2_ov_babaaa = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    ketee2_ov_babaaa -= einsum("ia,jkbc->kicbja", t1.aa, t2.abab)
    ketee2_ov_babaaa -= einsum("ia,jkbc->kjcaib", t1.aa, t2.abab)
    ketee2_ov_ababbb = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    ketee2_ov_ababbb -= einsum("ia,jkbc->jibcka", t1.bb, t2.abab)
    ketee2_ov_ababbb -= einsum("ia,jkbc->jkbaic", t1.bb, t2.abab)
    ketee2_vv_aaaaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    ketee2_vv_aaaaaa += einsum("ab,ijcd->jibcad", delta_vv.aa, t2.aaaa)
    ketee2_vv_aaaaaa -= einsum("ab,ijcd->jibdac", delta_vv.aa, t2.aaaa)
    ketee2_vv_aaaaaa -= einsum("ab,ijcd->jicbad", delta_vv.aa, t2.aaaa)
    ketee2_vv_aaaaaa += einsum("ab,ijcd->jidbac", delta_vv.aa, t2.aaaa)
    ketee2_vv_babaaa = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    ketee2_vv_babaaa += einsum("ab,ijcd->jidbac", delta_vv.aa, t2.abab)
    ketee2_vv_ababbb = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    ketee2_vv_ababbb += einsum("ab,ijcd->ijcbad", delta_vv.bb, t2.abab)
    ketee2_vv_bbbbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    ketee2_vv_bbbbbb += einsum("ab,ijcd->jibcad", delta_vv.bb, t2.bbbb)
    ketee2_vv_bbbbbb -= einsum("ab,ijcd->jibdac", delta_vv.bb, t2.bbbb)
    ketee2_vv_bbbbbb -= einsum("ab,ijcd->jicbad", delta_vv.bb, t2.bbbb)
    ketee2_vv_bbbbbb += einsum("ab,ijcd->jidbac", delta_vv.bb, t2.bbbb)
    ketee2_vv_ababaa = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    ketee2_vv_ababaa += einsum("ab,ijcd->ijbdac", delta_vv.aa, t2.abab)
    ketee2_vv_bababb = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    ketee2_vv_bababb += einsum("ab,ijcd->jibcad", delta_vv.bb, t2.abab)

    ketee1_oo_abab = np.zeros((nocc[0], nvir[1], nocc[0], nocc[1]), dtype=np.float64)
    ketee1_oo_baba = np.zeros((nocc[1], nvir[0], nocc[1], nocc[0]), dtype=np.float64)
    ketee1_ov_abab = np.zeros((nocc[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    ketee1_ov_baba = np.zeros((nocc[1], nvir[0], nocc[1], nvir[0]), dtype=np.float64)
    ketee1_vo_abab = np.zeros((nocc[0], nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    ketee1_vo_baba = np.zeros((nocc[1], nvir[0], nvir[1], nocc[0]), dtype=np.float64)
    ketee1_vv_abab = np.zeros((nocc[0], nvir[1], nvir[0], nvir[1]), dtype=np.float64)
    ketee1_vv_baba = np.zeros((nocc[1], nvir[0], nvir[1], nvir[0]), dtype=np.float64)
    ketee2_oo_bbbbaa = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    ketee2_oo_aaaabb = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nocc[1], nocc[1]), dtype=np.float64)
    ketee2_ov_bbbbaa = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    ketee2_ov_aaaabb = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nocc[1], nvir[1]), dtype=np.float64)
    ketee2_vo_aaaaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    ketee2_vo_ababaa = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nvir[0], nocc[0]), dtype=np.float64)
    ketee2_vo_babaaa = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    ketee2_vo_bbbbaa = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nvir[0], nocc[0]), dtype=np.float64)
    ketee2_vo_aaaabb = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nvir[1], nocc[1]), dtype=np.float64)
    ketee2_vo_ababbb = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    ketee2_vo_bababb = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0], nvir[1], nocc[1]), dtype=np.float64)
    ketee2_vo_bbbbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    ketee2_vv_bbbbaa = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    ketee2_vv_aaaabb = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)

    ketee1_aaaa = np.concatenate([np.concatenate([ketee1_oo_aaaa, ketee1_ov_aaaa], axis=-1), np.concatenate([ketee1_vo_aaaa, ketee1_vv_aaaa], axis=-1)], axis=-2)
    ketee1_abab = np.concatenate([np.concatenate([ketee1_oo_abab, ketee1_ov_abab], axis=-1), np.concatenate([ketee1_vo_abab, ketee1_vv_abab], axis=-1)], axis=-2)
    ketee1_baba = np.concatenate([np.concatenate([ketee1_oo_baba, ketee1_ov_baba], axis=-1), np.concatenate([ketee1_vo_baba, ketee1_vv_baba], axis=-1)], axis=-2)
    ketee1_bbbb = np.concatenate([np.concatenate([ketee1_oo_bbbb, ketee1_ov_bbbb], axis=-1), np.concatenate([ketee1_vo_bbbb, ketee1_vv_bbbb], axis=-1)], axis=-2)
    ketee2_aaaaaa = np.concatenate([np.concatenate([ketee2_oo_aaaaaa, ketee2_ov_aaaaaa], axis=-1), np.concatenate([ketee2_vo_aaaaaa, ketee2_vv_aaaaaa], axis=-1)], axis=-2)
    ketee2_ababaa = np.concatenate([np.concatenate([ketee2_oo_ababaa, ketee2_ov_ababaa], axis=-1), np.concatenate([ketee2_vo_ababaa, ketee2_vv_ababaa], axis=-1)], axis=-2)
    ketee2_babaaa = np.concatenate([np.concatenate([ketee2_oo_babaaa, ketee2_ov_babaaa], axis=-1), np.concatenate([ketee2_vo_babaaa, ketee2_vv_babaaa], axis=-1)], axis=-2)
    ketee2_bbbbaa = np.concatenate([np.concatenate([ketee2_oo_bbbbaa, ketee2_ov_bbbbaa], axis=-1), np.concatenate([ketee2_vo_bbbbaa, ketee2_vv_bbbbaa], axis=-1)], axis=-2)
    ketee2_aaaabb = np.concatenate([np.concatenate([ketee2_oo_aaaabb, ketee2_ov_aaaabb], axis=-1), np.concatenate([ketee2_vo_aaaabb, ketee2_vv_aaaabb], axis=-1)], axis=-2)
    ketee2_ababbb = np.concatenate([np.concatenate([ketee2_oo_ababbb, ketee2_ov_ababbb], axis=-1), np.concatenate([ketee2_vo_ababbb, ketee2_vv_ababbb], axis=-1)], axis=-2)
    ketee2_bababb = np.concatenate([np.concatenate([ketee2_oo_bababb, ketee2_ov_bababb], axis=-1), np.concatenate([ketee2_vo_bababb, ketee2_vv_bababb], axis=-1)], axis=-2)
    ketee2_bbbbbb = np.concatenate([np.concatenate([ketee2_oo_bbbbbb, ketee2_ov_bbbbbb], axis=-1), np.concatenate([ketee2_vo_bbbbbb, ketee2_vv_bbbbbb], axis=-1)], axis=-2)

    ketee1 = Namespace(aaaa=ketee1_aaaa, abab=ketee1_abab, baba=ketee1_baba, bbbb=ketee1_bbbb)
    ketee2 = Namespace(aaaaaa=ketee2_aaaaaa, ababaa=ketee2_ababaa, babaaa=ketee2_babaaa, bbbbaa=ketee2_bbbbaa, aaaabb=ketee2_aaaabb, ababbb=ketee2_ababbb, bababb=ketee2_bababb, bbbbbb=ketee2_bbbbbb)

    return ketee1, ketee2

def make_ee_mom_bras(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):  # pragma: no cover
    delta_oo = Namespace()
    delta_oo.aa = np.eye(nocc[0])
    delta_oo.bb = np.eye(nocc[1])
    delta_vv = Namespace()
    delta_vv.aa = np.eye(nvir[0])
    delta_vv.bb = np.eye(nvir[1])

    x0 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x0 += einsum("ia,bajk->jkib", t1.aa, l2.aaaa)
    x19 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x19 += einsum("ijka->ikja", x0)
    x19 -= einsum("ijka->jkia", x0)
    x20 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x20 -= einsum("ijka->ijka", x0)
    x20 += einsum("ijka->jika", x0)
    braee1_oo_aaaa = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    braee1_oo_aaaa += einsum("ijka->kija", x0)
    braee1_oo_aaaa -= einsum("ijka->kjia", x0)
    del x0
    x1 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x1 += einsum("ia,bajk->jkib", t1.bb, l2.bbbb)
    x23 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x23 += einsum("ijka->ikja", x1)
    x23 -= einsum("ijka->jkia", x1)
    x24 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x24 += einsum("ijka->ijka", x1)
    x24 -= einsum("ijka->jika", x1)
    braee1_oo_bbbb = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    braee1_oo_bbbb += einsum("ijka->kija", x1)
    braee1_oo_bbbb -= einsum("ijka->kjia", x1)
    del x1
    x2 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x2 += einsum("ia,abjk->jikb", t1.aa, l2.abab)
    x21 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x21 -= einsum("ijka->ijka", x2)
    braee1_oo_aabb = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    braee1_oo_aabb -= einsum("ijka->jika", x2)
    del x2
    x3 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x3 += einsum("ia,bajk->jkib", t1.bb, l2.abab)
    x22 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x22 -= einsum("ijka->ijka", x3)
    braee1_oo_bbaa = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    braee1_oo_bbaa -= einsum("ijka->kjia", x3)
    del x3
    x4 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x4 += einsum("ia,jb->ijab", t1.aa, t1.aa)
    x4 -= einsum("ijab->jiab", t2.aaaa)
    x4 += einsum("ijab->jiba", t2.aaaa)
    braee1_ov_aabb = np.zeros((nocc[0], nvir[0], nocc[1], nvir[1]), dtype=np.float64)
    braee1_ov_aabb -= einsum("abij,ikca->kcjb", l2.abab, x4)
    x5 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x5 -= einsum("abij->jiab", l2.aaaa)
    x5 += einsum("abij->jiba", l2.aaaa)
    braee1_ov_aaaa = np.zeros((nocc[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    braee1_ov_aaaa += einsum("ijab,ikcb->jakc", x4, x5)
    del x4
    braee1_ov_bbaa = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    braee1_ov_bbaa -= einsum("ijab,ikca->jbkc", t2.abab, x5)
    del x5
    x6 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x6 += einsum("ijab->jiab", t2.aaaa)
    x6 += einsum("ijab->jiba", t2.aaaa) * -1
    x7 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x7 += einsum("abij,ikab->jk", l2.aaaa, x6) * -1
    del x6
    x7 += einsum("ij->ji", delta_oo.aa) * -1
    x7 += einsum("ai,ja->ij", l1.aa, t1.aa)
    x7 += einsum("abij,kjab->ik", l2.abab, t2.abab)
    braee1_ov_aaaa += einsum("ab,ij->jbia", delta_vv.aa, x7) * -1
    del x7
    x8 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x8 += einsum("ijab->jiab", t2.aaaa) * -1
    x8 += einsum("ijab->jiba", t2.aaaa)
    x9 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x9 += einsum("abij,ijca->bc", l2.aaaa, x8) * -1
    del x8
    x9 += einsum("ai,ib->ab", l1.aa, t1.aa)
    x9 += einsum("abij,ijcb->ac", l2.abab, t2.abab)
    braee1_ov_aaaa += einsum("ij,ab->jbia", delta_oo.aa, x9) * -1
    del x9
    x10 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x10 += einsum("ia,jb->ijab", t1.bb, t1.bb)
    x10 -= einsum("ijab->jiab", t2.bbbb)
    x10 += einsum("ijab->jiba", t2.bbbb)
    braee1_ov_bbaa -= einsum("abij,jkcb->kcia", l2.abab, x10)
    x11 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x11 -= einsum("abij->jiab", l2.bbbb)
    x11 += einsum("abij->jiba", l2.bbbb)
    braee1_ov_bbbb = np.zeros((nocc[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    braee1_ov_bbbb += einsum("ijab,ikcb->jakc", x10, x11)
    del x10
    braee1_ov_aabb -= einsum("ijab,jkcb->iakc", t2.abab, x11)
    del x11
    x12 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x12 += einsum("ijab->jiab", t2.bbbb) * -1
    x12 += einsum("ijab->jiba", t2.bbbb)
    x13 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x13 += einsum("abij,ikba->jk", l2.bbbb, x12) * -1
    x14 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x14 += einsum("abij,ijca->bc", l2.bbbb, x12) * -1
    del x12
    x13 += einsum("ij->ji", delta_oo.bb) * -1
    x13 += einsum("ai,ja->ij", l1.bb, t1.bb)
    x13 += einsum("abij,ikab->jk", l2.abab, t2.abab)
    braee1_ov_bbbb += einsum("ab,ij->jbia", delta_vv.bb, x13) * -1
    del x13
    x14 += einsum("ai,ib->ab", l1.bb, t1.bb)
    x14 += einsum("abij,ijac->bc", l2.abab, t2.abab)
    braee1_ov_bbbb += einsum("ij,ab->jbia", delta_oo.bb, x14) * -1
    del x14
    x15 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x15 += einsum("ia,bcji->jbca", t1.aa, l2.aaaa)
    braee1_vv_aaaa = np.zeros((nvir[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    braee1_vv_aaaa -= einsum("iabc->acib", x15)
    braee1_vv_aaaa += einsum("iabc->bcia", x15)
    braee2_ov_aaaaaa = np.zeros((nocc[0], nvir[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_ov_aaaaaa += einsum("ij,kabc->icjkab", delta_oo.aa, x15)
    braee2_ov_aaaaaa -= einsum("ij,kabc->icjkba", delta_oo.aa, x15)
    braee2_ov_aaaaaa -= einsum("ij,kabc->ickjab", delta_oo.aa, x15)
    braee2_ov_aaaaaa += einsum("ij,kabc->ickjba", delta_oo.aa, x15)
    del x15
    x16 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x16 += einsum("ia,bcji->jbca", t1.bb, l2.bbbb)
    braee1_vv_bbbb = np.zeros((nvir[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    braee1_vv_bbbb -= einsum("iabc->acib", x16)
    braee1_vv_bbbb += einsum("iabc->bcia", x16)
    braee2_ov_bbbbbb = np.zeros((nocc[1], nvir[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_ov_bbbbbb += einsum("ij,kabc->icjkab", delta_oo.bb, x16)
    braee2_ov_bbbbbb -= einsum("ij,kabc->icjkba", delta_oo.bb, x16)
    braee2_ov_bbbbbb -= einsum("ij,kabc->ickjab", delta_oo.bb, x16)
    braee2_ov_bbbbbb += einsum("ij,kabc->ickjba", delta_oo.bb, x16)
    del x16
    x17 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x17 += einsum("ia,bcij->jbac", t1.aa, l2.abab)
    braee1_vv_aabb = np.zeros((nvir[0], nvir[0], nocc[1], nvir[1]), dtype=np.float64)
    braee1_vv_aabb += einsum("iabc->abic", x17)
    braee2_ov_aababa = np.zeros((nocc[0], nvir[0], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_ov_aababa -= einsum("ij,kabc->ibkjca", delta_oo.aa, x17)
    braee2_ov_aaabab = np.zeros((nocc[0], nvir[0], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_ov_aaabab -= einsum("ij,kabc->ibjkac", delta_oo.aa, x17)
    del x17
    x18 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x18 += einsum("ia,bcji->jbca", t1.bb, l2.abab)
    braee1_vv_bbaa = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    braee1_vv_bbaa += einsum("iabc->bcia", x18)
    braee2_ov_bbbaba = np.zeros((nocc[1], nvir[1], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_ov_bbbaba -= einsum("ij,kabc->icjkba", delta_oo.bb, x18)
    braee2_ov_bbabab = np.zeros((nocc[1], nvir[1], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_ov_bbabab -= einsum("ij,kabc->ickjab", delta_oo.bb, x18)
    del x18
    x19 += einsum("ij,ak->jika", delta_oo.aa, l1.aa)
    x19 -= einsum("ij,ak->kjia", delta_oo.aa, l1.aa)
    braee2_ov_aaaaaa -= einsum("ab,ijkc->jbkiac", delta_vv.aa, x19)
    del x19
    x20 -= einsum("ij,ak->jkia", delta_oo.aa, l1.aa)
    x20 += einsum("ij,ak->kjia", delta_oo.aa, l1.aa)
    braee2_ov_aaaaaa -= einsum("ab,ijkc->kbjica", delta_vv.aa, x20)
    del x20
    x21 += einsum("ij,ak->jika", delta_oo.aa, l1.bb)
    braee2_ov_aababa += einsum("ab,ijkc->jbkica", delta_vv.aa, x21)
    braee2_ov_aaabab += einsum("ab,ijkc->jbikac", delta_vv.aa, x21)
    del x21
    x22 += einsum("ij,ak->kjia", delta_oo.bb, l1.aa)
    braee2_ov_bbbaba += einsum("ab,ijkc->kbjiac", delta_vv.bb, x22)
    braee2_ov_bbabab += einsum("ab,ijkc->kbijca", delta_vv.bb, x22)
    del x22
    x23 += einsum("ij,ak->jika", delta_oo.bb, l1.bb)
    x23 -= einsum("ij,ak->kjia", delta_oo.bb, l1.bb)
    braee2_ov_bbbbbb -= einsum("ab,ijkc->jbkiac", delta_vv.bb, x23)
    del x23
    x24 += einsum("ij,ak->jkia", delta_oo.bb, l1.bb)
    x24 -= einsum("ij,ak->kjia", delta_oo.bb, l1.bb)
    braee2_ov_bbbbbb -= einsum("ab,ijkc->kbijca", delta_vv.bb, x24)
    del x24
    braee1_oo_aaaa += einsum("ij,ak->jika", delta_oo.aa, l1.aa)
    braee1_oo_aaaa -= einsum("ij,ak->jkia", delta_oo.aa, l1.aa)
    braee1_oo_bbbb += einsum("ij,ak->jika", delta_oo.bb, l1.bb)
    braee1_oo_bbbb -= einsum("ij,ak->jkia", delta_oo.bb, l1.bb)
    braee1_oo_aabb += einsum("ij,ak->jika", delta_oo.aa, l1.bb)
    braee1_oo_bbaa += einsum("ij,ak->jika", delta_oo.bb, l1.aa)
    braee1_ov_aaaa += einsum("ai,jb->jbia", l1.aa, t1.aa)
    braee1_ov_aaaa += einsum("abij,kjcb->kcia", l2.abab, t2.abab)
    braee1_ov_bbbb += einsum("ai,jb->jbia", l1.bb, t1.bb)
    braee1_ov_bbbb += einsum("abij,ikac->kcjb", l2.abab, t2.abab)
    braee1_ov_bbaa += einsum("ai,jb->jbia", l1.aa, t1.bb)
    braee1_ov_aabb += einsum("ai,jb->jbia", l1.bb, t1.aa)
    braee1_vo_aaaa = np.zeros((nvir[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    braee1_vo_aaaa -= einsum("abij->ajib", l2.aaaa)
    braee1_vo_aaaa += einsum("abij->bjia", l2.aaaa)
    braee1_vo_bbbb = np.zeros((nvir[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    braee1_vo_bbbb -= einsum("abij->ajib", l2.bbbb)
    braee1_vo_bbbb += einsum("abij->bjia", l2.bbbb)
    braee1_vo_bbaa = np.zeros((nvir[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    braee1_vo_bbaa += einsum("abij->bjia", l2.abab)
    braee1_vo_aabb = np.zeros((nvir[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    braee1_vo_aabb += einsum("abij->aijb", l2.abab)
    braee1_vv_aaaa += einsum("ab,ci->cbia", delta_vv.aa, l1.aa)
    braee1_vv_bbbb += einsum("ab,ci->cbia", delta_vv.bb, l1.bb)
    braee2_oo_aaaaaa = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_oo_aaaaaa -= einsum("ij,abkl->jilkab", delta_oo.aa, l2.aaaa)
    braee2_oo_aaaaaa += einsum("ij,abkl->jilkba", delta_oo.aa, l2.aaaa)
    braee2_oo_aaaaaa += einsum("ij,abkl->jlikab", delta_oo.aa, l2.aaaa)
    braee2_oo_aaaaaa -= einsum("ij,abkl->jlikba", delta_oo.aa, l2.aaaa)
    braee2_oo_aaaaaa -= einsum("ij,abkl->jlkiab", delta_oo.aa, l2.aaaa)
    braee2_oo_aaaaaa += einsum("ij,abkl->jlkiba", delta_oo.aa, l2.aaaa)
    braee2_oo_bbbbbb = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_oo_bbbbbb -= einsum("ij,abkl->jilkab", delta_oo.bb, l2.bbbb)
    braee2_oo_bbbbbb += einsum("ij,abkl->jilkba", delta_oo.bb, l2.bbbb)
    braee2_oo_bbbbbb += einsum("ij,abkl->jlikab", delta_oo.bb, l2.bbbb)
    braee2_oo_bbbbbb -= einsum("ij,abkl->jlikba", delta_oo.bb, l2.bbbb)
    braee2_oo_bbbbbb -= einsum("ij,abkl->jlkiab", delta_oo.bb, l2.bbbb)
    braee2_oo_bbbbbb += einsum("ij,abkl->jlkiba", delta_oo.bb, l2.bbbb)
    braee2_oo_aababa = np.zeros((nocc[0], nocc[0], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_oo_aababa += einsum("ij,abkl->jilkba", delta_oo.aa, l2.abab)
    braee2_oo_aababa -= einsum("ij,abkl->jkliba", delta_oo.aa, l2.abab)
    braee2_oo_bbabab = np.zeros((nocc[1], nocc[1], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_oo_bbabab += einsum("ij,abkl->jiklab", delta_oo.bb, l2.abab)
    braee2_oo_bbabab -= einsum("ij,abkl->jlkiab", delta_oo.bb, l2.abab)
    braee2_oo_aaabab = np.zeros((nocc[0], nocc[0], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_oo_aaabab += einsum("ij,abkl->jiklab", delta_oo.aa, l2.abab)
    braee2_oo_aaabab -= einsum("ij,abkl->jkilab", delta_oo.aa, l2.abab)
    braee2_oo_bbbaba = np.zeros((nocc[1], nocc[1], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_oo_bbbaba += einsum("ij,abkl->jilkba", delta_oo.bb, l2.abab)
    braee2_oo_bbbaba -= einsum("ij,abkl->jlikba", delta_oo.bb, l2.abab)
    braee2_oo_aabbbb = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_oo_aabbbb -= einsum("ij,abkl->jilkab", delta_oo.aa, l2.bbbb)
    braee2_oo_aabbbb += einsum("ij,abkl->jilkba", delta_oo.aa, l2.bbbb)
    braee2_oo_bbaaaa = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_oo_bbaaaa -= einsum("ij,abkl->jilkab", delta_oo.bb, l2.aaaa)
    braee2_oo_bbaaaa += einsum("ij,abkl->jilkba", delta_oo.bb, l2.aaaa)
    braee2_ov_aaaaaa -= einsum("ia,bcjk->iakjbc", t1.aa, l2.aaaa)
    braee2_ov_aaaaaa += einsum("ia,bcjk->iakjcb", t1.aa, l2.aaaa)
    braee2_ov_aababa += einsum("ia,bcjk->iakjcb", t1.aa, l2.abab)
    braee2_ov_aaabab += einsum("ia,bcjk->iajkbc", t1.aa, l2.abab)
    braee2_ov_aabbbb = np.zeros((nocc[0], nvir[0], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_ov_aabbbb -= einsum("ia,bcjk->iakjbc", t1.aa, l2.bbbb)
    braee2_ov_aabbbb += einsum("ia,bcjk->iakjcb", t1.aa, l2.bbbb)
    braee2_ov_bbaaaa = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_ov_bbaaaa -= einsum("ia,bcjk->iakjbc", t1.bb, l2.aaaa)
    braee2_ov_bbaaaa += einsum("ia,bcjk->iakjcb", t1.bb, l2.aaaa)
    braee2_ov_bbbaba += einsum("ia,bcjk->iakjcb", t1.bb, l2.abab)
    braee2_ov_bbabab += einsum("ia,bcjk->iajkbc", t1.bb, l2.abab)
    braee2_ov_bbbbbb -= einsum("ia,bcjk->iakjbc", t1.bb, l2.bbbb)
    braee2_ov_bbbbbb += einsum("ia,bcjk->iakjcb", t1.bb, l2.bbbb)
    braee2_vv_aaaaaa = np.zeros((nvir[0], nvir[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_vv_aaaaaa -= einsum("ab,cdij->cbjiad", delta_vv.aa, l2.aaaa)
    braee2_vv_aaaaaa += einsum("ab,cdij->dbjiac", delta_vv.aa, l2.aaaa)
    braee2_vv_aaaaaa += einsum("ab,cdij->cbjida", delta_vv.aa, l2.aaaa)
    braee2_vv_aaaaaa -= einsum("ab,cdij->dbjica", delta_vv.aa, l2.aaaa)
    braee2_vv_bbbbbb = np.zeros((nvir[1], nvir[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_vv_bbbbbb -= einsum("ab,cdij->cbjiad", delta_vv.bb, l2.bbbb)
    braee2_vv_bbbbbb += einsum("ab,cdij->dbjiac", delta_vv.bb, l2.bbbb)
    braee2_vv_bbbbbb += einsum("ab,cdij->cbjida", delta_vv.bb, l2.bbbb)
    braee2_vv_bbbbbb -= einsum("ab,cdij->dbjica", delta_vv.bb, l2.bbbb)
    braee2_vv_aababa = np.zeros((nvir[0], nvir[0], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_vv_aababa += einsum("ab,cdij->cbjida", delta_vv.aa, l2.abab)
    braee2_vv_bbabab = np.zeros((nvir[1], nvir[1], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_vv_bbabab += einsum("ab,cdij->dbijca", delta_vv.bb, l2.abab)
    braee2_vv_aaabab = np.zeros((nvir[0], nvir[0], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_vv_aaabab += einsum("ab,cdij->cbijad", delta_vv.aa, l2.abab)
    braee2_vv_bbbaba = np.zeros((nvir[1], nvir[1], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_vv_bbbaba += einsum("ab,cdij->dbjiac", delta_vv.bb, l2.abab)

    braee1_oo_abab = np.zeros((nocc[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    braee1_oo_baba = np.zeros((nocc[1], nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    braee1_ov_abab = np.zeros((nocc[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    braee1_ov_baba = np.zeros((nocc[1], nvir[0], nocc[1], nvir[0]), dtype=np.float64)
    braee1_vo_abab = np.zeros((nvir[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    braee1_vo_baba = np.zeros((nvir[1], nocc[0], nocc[1], nvir[0]), dtype=np.float64)
    braee1_vv_abab = np.zeros((nvir[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    braee1_vv_baba = np.zeros((nvir[1], nvir[0], nocc[1], nvir[0]), dtype=np.float64)
    braee2_vo_aaaaaa = np.zeros((nvir[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_vo_aaabab = np.zeros((nvir[0], nocc[0], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_vo_aababa = np.zeros((nvir[0], nocc[0], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_vo_aabbbb = np.zeros((nvir[0], nocc[0], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_vo_bbaaaa = np.zeros((nvir[1], nocc[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    braee2_vo_bbabab = np.zeros((nvir[1], nocc[1], nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    braee2_vo_bbbaba = np.zeros((nvir[1], nocc[1], nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    braee2_vo_bbbbbb = np.zeros((nvir[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_vv_aabbbb = np.zeros((nvir[0], nvir[0], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    braee2_vv_bbaaaa = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)

    braee1_aaaa = np.concatenate([np.concatenate([braee1_oo_aaaa, braee1_ov_aaaa], axis=1), np.concatenate([braee1_vo_aaaa, braee1_vv_aaaa], axis=1)], axis=0)
    braee1_abab = np.concatenate([np.concatenate([braee1_oo_abab, braee1_ov_abab], axis=1), np.concatenate([braee1_vo_abab, braee1_vv_abab], axis=1)], axis=0)
    braee1_baba = np.concatenate([np.concatenate([braee1_oo_baba, braee1_ov_baba], axis=1), np.concatenate([braee1_vo_baba, braee1_vv_baba], axis=1)], axis=0)
    braee1_bbbb = np.concatenate([np.concatenate([braee1_oo_bbbb, braee1_ov_bbbb], axis=1), np.concatenate([braee1_vo_bbbb, braee1_vv_bbbb], axis=1)], axis=0)
    braee2_aaaaaa = np.concatenate([np.concatenate([braee2_oo_aaaaaa, braee2_ov_aaaaaa], axis=1), np.concatenate([braee2_vo_aaaaaa, braee2_vv_aaaaaa], axis=1)], axis=0)
    braee2_aaabab = np.concatenate([np.concatenate([braee2_oo_aaabab, braee2_ov_aaabab], axis=1), np.concatenate([braee2_vo_aaabab, braee2_vv_aaabab], axis=1)], axis=0)
    braee2_aababa = np.concatenate([np.concatenate([braee2_oo_aababa, braee2_ov_aababa], axis=1), np.concatenate([braee2_vo_aababa, braee2_vv_aababa], axis=1)], axis=0)
    braee2_aabbbb = np.concatenate([np.concatenate([braee2_oo_aabbbb, braee2_ov_aabbbb], axis=1), np.concatenate([braee2_vo_aabbbb, braee2_vv_aabbbb], axis=1)], axis=0)
    braee2_bbaaaa = np.concatenate([np.concatenate([braee2_oo_bbaaaa, braee2_ov_bbaaaa], axis=1), np.concatenate([braee2_vo_bbaaaa, braee2_vv_bbaaaa], axis=1)], axis=0)
    braee2_bbabab = np.concatenate([np.concatenate([braee2_oo_bbabab, braee2_ov_bbabab], axis=1), np.concatenate([braee2_vo_bbabab, braee2_vv_bbabab], axis=1)], axis=0)
    braee2_bbbaba = np.concatenate([np.concatenate([braee2_oo_bbbaba, braee2_ov_bbbaba], axis=1), np.concatenate([braee2_vo_bbbaba, braee2_vv_bbbaba], axis=1)], axis=0)
    braee2_bbbbbb = np.concatenate([np.concatenate([braee2_oo_bbbbbb, braee2_ov_bbbbbb], axis=1), np.concatenate([braee2_vo_bbbbbb, braee2_vv_bbbbbb], axis=1)], axis=0)

    braee1 = Namespace(aaaa=braee1_aaaa, abab=braee1_abab, baba=braee1_baba, bbbb=braee1_bbbb)
    braee2 = Namespace(aaaaaa=braee2_aaaaaa, aaabab=braee2_aaabab, aababa=braee2_aababa, aabbbb=braee2_aabbbb, bbaaaa=braee2_bbaaaa, bbabab=braee2_bbabab, bbbaba=braee2_bbbaba, bbbbbb=braee2_bbbbbb)

    braee1 = Namespace(**{key: val/2 for key, val in braee1.__dict__.items()})
    braee2 = Namespace(**{key: val/2 for key, val in braee2.__dict__.items()})

    return braee1, braee2

def hbar_matvec_ee(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, r1=None, r2=None, **kwargs):
    x0 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x0 += einsum("ijab->ijab", r2.aaaa)
    x0 += einsum("ijab->jiab", r2.aaaa) * -1
    x153 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x153 += einsum("ij,ikab->jkab", f.aa.oo, x0) * 0.5
    x164 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x164 += einsum("ijab->ijab", x153) * -1
    del x153
    x1 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x1 += einsum("iabc->ibac", v.aaaa.ovvv)
    x1 += einsum("iabc->ibca", v.aaaa.ovvv) * -1
    x146 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x146 += einsum("ijab,kcab->ijkc", r2.aaaa, x1)
    x147 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x147 += einsum("ijka->ijka", x146) * -1
    del x146
    x156 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x156 += einsum("ijab,icab->jc", t2.aaaa, x1)
    x163 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x163 += einsum("ia->ia", x156) * -1
    del x156
    x366 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x366 += einsum("ijab,icba->jc", t2.aaaa, x1)
    x373 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x373 += einsum("ia->ia", x366) * -1
    del x366
    ree1new_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    ree1new_aa += einsum("ijab,icab->jc", x0, x1) * 0.5
    del x1
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x2 += einsum("ijka->ikja", v.aaaa.ooov)
    x2 += einsum("ijka->kija", v.aaaa.ooov) * -1
    x36 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x36 += einsum("ia,ijka->jk", r1.aa, x2) * -2
    x45 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x45 += einsum("ia,ijka->jk", t1.aa, x2)
    x47 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x47 += einsum("ij->ij", x45) * -1
    x124 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x124 += einsum("ij->ij", x45) * -1
    del x45
    x136 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x136 += einsum("ijab,ijkc->kabc", r2.aaaa, x2)
    x137 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x137 += einsum("iabc->iabc", x136) * -1
    del x136
    x157 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x157 += einsum("ijab,ijka->kb", t2.aaaa, x2)
    x163 += einsum("ia->ia", x157) * -1
    del x157
    x305 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x305 += einsum("ijab,ikla->kljb", t2.abab, x2)
    x314 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x314 += einsum("ijka->ijka", x305) * -1
    del x305
    x361 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x361 += einsum("ia,ijka->jk", r1.aa, x2)
    x364 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x364 += einsum("ij->ij", x361) * -1
    del x361
    x3 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x3 += einsum("ijab->ijab", r2.aaaa)
    x3 += einsum("ijab->ijba", r2.aaaa) * -1
    x139 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x139 += einsum("ab,ijcb->ijac", f.aa.vv, x3) * 0.5
    x164 += einsum("ijab->ijab", x139) * -1
    del x139
    ree1new_aa += einsum("ijka,ijab->kb", x2, x3) * 0.5
    del x2
    x4 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x4 += einsum("ijab->ijab", r2.abab)
    x4 += einsum("ijab->jiba", r2.baba)
    x8 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x8 += einsum("iajb,kjcb->ikac", v.aabb.ovov, x4)
    x9 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x9 += einsum("ijab->jiba", x8)
    del x8
    x27 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x27 += einsum("iajb,ijcb->ca", v.aabb.ovov, x4) * 0.5
    x29 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x29 += einsum("iajb,kjab->ik", v.aabb.ovov, x4)
    x36 += einsum("ij->ij", x29)
    x132 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x132 += einsum("ij->ji", x29)
    del x29
    x54 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x54 += einsum("iajb,ikac->jkbc", v.aabb.ovov, x4)
    x55 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x55 += einsum("ijab->jiba", x54)
    del x54
    x69 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x69 += einsum("iajb,ijac->cb", v.aabb.ovov, x4) * 0.5
    x73 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x73 += einsum("iajb,ikab->jk", v.aabb.ovov, x4)
    x80 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x80 += einsum("ij->ij", x73)
    x469 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x469 += einsum("ij->ji", x73)
    del x73
    x115 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x115 += einsum("ijka,lkba->ijlb", v.aabb.ooov, x4)
    x118 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x118 += einsum("ijka->ikja", x115)
    del x115
    x121 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x121 += einsum("iabc,jida->jbcd", v.bbaa.ovvv, x4)
    x122 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x122 += einsum("iabc->icab", x121)
    del x121
    x128 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x128 += einsum("iajb,ijcb->ac", v.aabb.ovov, x4)
    x129 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x129 += einsum("ab->ba", x128)
    x334 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x334 += einsum("ab->ba", x128)
    del x128
    x248 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x248 += einsum("abcd,ijbd->ijac", v.aabb.vvvv, x4) * 0.5
    ree2new_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    ree2new_abab += einsum("ijab->ijab", x248)
    ree2new_baba = np.zeros((nocc[1], nocc[0], nvir[1], nvir[0]), dtype=np.float64)
    ree2new_baba += einsum("ijab->jiba", x248)
    del x248
    x252 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x252 += einsum("iajb,klab->ikjl", v.aabb.ovov, x4)
    x253 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x253 += einsum("ijab,ikjl->klab", t2.abab, x252) * 0.5
    del x252
    ree2new_abab += einsum("ijab->ijab", x253)
    ree2new_baba += einsum("ijab->jiba", x253)
    del x253
    x256 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x256 += einsum("iabc,jkac->jikb", v.aabb.ovvv, x4) * 0.5
    x278 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x278 += einsum("ijka->jika", x256)
    del x256
    x257 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x257 += einsum("iajk,ljab->likb", v.aabb.ovoo, x4) * 0.5
    x278 += einsum("ijka->jika", x257) * -1
    del x257
    x263 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x263 += einsum("iajb,klab->ikjl", v.aabb.ovov, x4) * 0.5
    x270 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x270 += einsum("ijkl->jikl", x263)
    del x263
    x276 = np.zeros((nocc[0], nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x276 += einsum("iajb,kjac->ikbc", v.aabb.ovov, x4)
    x277 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x277 += einsum("ia,jkab->kjib", t1.bb, x276) * 0.5
    del x276
    x278 += einsum("ijka->jika", x277) * -1
    del x277
    x285 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x285 += einsum("iajb,ikcb->jkac", v.aabb.ovov, x4)
    x286 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x286 += einsum("ia,jkab->ijkb", t1.aa, x285) * -1
    x385 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x385 += einsum("ia,jkab->ijkb", t1.aa, x285) * -0.5
    del x285
    x286 += einsum("iabc,jkca->jikb", v.bbaa.ovvv, x4)
    x286 += einsum("ijka,ilba->jklb", v.aabb.ooov, x4) * -1
    x291 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x291 += einsum("iabc,ijdc->jdab", v.aabb.ovvv, x4)
    x295 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x295 += einsum("iabc->iabc", x291) * -1
    del x291
    x292 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x292 += einsum("iajk,ijbc->kbac", v.aabb.ovoo, x4)
    x295 += einsum("iabc->iabc", x292)
    del x292
    x293 = np.zeros((nvir[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x293 += einsum("iajb,ijcd->acbd", v.aabb.ovov, x4)
    x294 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x294 += einsum("ia,bcad->icbd", t1.bb, x293)
    del x293
    x295 += einsum("iabc->iabc", x294)
    del x294
    x299 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x299 += einsum("iabc,jicd->jbad", v.bbaa.ovvv, x4)
    x301 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x301 += einsum("iabc->iacb", x299) * -1
    del x299
    x300 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x300 += einsum("ijka,ikbc->jbac", v.aabb.ooov, x4)
    x301 += einsum("iabc->iacb", x300)
    del x300
    x329 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x329 += einsum("iajb,ijac->bc", v.aabb.ovov, x4)
    x331 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x331 += einsum("ab->ba", x329)
    x467 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x467 += einsum("ab->ba", x329)
    del x329
    x353 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x353 += einsum("iajb,ikab->jk", v.aabb.ovov, x4) * 0.5
    x357 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x357 += einsum("ij->ij", x353)
    del x353
    x360 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x360 += einsum("iajb,kjab->ik", v.aabb.ovov, x4) * 0.5
    x364 += einsum("ij->ij", x360)
    del x360
    x385 += einsum("iabc,jkca->jikb", v.bbaa.ovvv, x4) * 0.5
    x385 += einsum("ijka,ilba->jklb", v.aabb.ooov, x4) * -0.5
    x456 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x456 += einsum("iajk,ilab->ljkb", v.aabb.ovoo, x4)
    x459 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x459 += einsum("ijka->jika", x456)
    del x456
    x462 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x462 += einsum("iabc,ijad->jdbc", v.aabb.ovvv, x4)
    x463 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x463 += einsum("iabc->iabc", x462)
    del x462
    ree1new_aa += einsum("iabc,jica->jb", v.bbaa.ovvv, x4) * 0.5
    ree1new_aa += einsum("ijka,ikba->jb", v.aabb.ooov, x4) * -0.5
    ree1new_aa += einsum("ia,jiba->jb", f.bb.ov, x4) * 0.5
    ree1new_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    ree1new_bb += einsum("iabc,ijac->jb", v.aabb.ovvv, x4) * 0.5
    ree1new_bb += einsum("iajk,ijab->kb", v.aabb.ovoo, x4) * -0.5
    ree1new_bb += einsum("ia,ijab->jb", f.aa.ov, x4) * 0.5
    x5 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x5 += einsum("ijab->ijab", r2.aaaa) * -1
    x5 += einsum("ijab->ijba", r2.aaaa)
    x5 += einsum("ijab->jiab", r2.aaaa)
    x5 += einsum("ijab->jiba", r2.aaaa) * -1
    x12 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x12 += einsum("iajb,kica->kjcb", v.aabb.ovov, x5)
    x13 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x13 += einsum("ijab->ijab", x12) * -1
    del x12
    x297 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x297 += einsum("iabc,jida->jdbc", v.aabb.ovvv, x5)
    x301 += einsum("iabc->iabc", x297) * -1
    del x297
    x6 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x6 += einsum("iajb->jiab", v.aaaa.ovov)
    x6 += einsum("iajb->jiba", v.aaaa.ovov) * -1
    x7 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x7 += einsum("ijab,jkac->ikbc", x5, x6)
    x9 += einsum("ijab->ijab", x7) * -1
    del x7
    x116 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x116 += einsum("ia,jkba->ijkb", t1.aa, x9)
    x118 += einsum("ijka->kjia", x116)
    del x116
    ree1new_aa += einsum("ia,jiba->jb", t1.aa, x9) * 0.5
    del x9
    x36 += einsum("ijab,ikba->kj", x0, x6)
    x44 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x44 += einsum("ijab,ikab->jk", t2.aaaa, x6)
    x47 += einsum("ij->ji", x44) * -1
    x124 += einsum("ij->ji", x44) * -1
    del x44
    x56 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x56 += einsum("ijab,ikca->kjcb", x4, x6)
    x59 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x59 += einsum("ijab->ijab", x56)
    del x56
    x359 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x359 += einsum("ijab,ikba->jk", x0, x6) * 0.5
    x364 += einsum("ij->ji", x359)
    del x359
    x10 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x10 += einsum("iajb->jiab", v.bbbb.ovov)
    x10 += einsum("iajb->jiba", v.bbbb.ovov) * -1
    x11 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x11 += einsum("ijab,kica->kjcb", x10, x4)
    x13 += einsum("ijab->ijab", x11) * -1
    del x11
    x286 += einsum("ia,jkba->jkib", t1.bb, x13)
    x385 += einsum("ia,jkba->jkib", t1.bb, x13) * 0.5
    ree1new_aa += einsum("ia,jiba->jb", t1.bb, x13) * 0.5
    del x13
    x75 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x75 += einsum("ia,ijab->jb", t1.bb, x10)
    x76 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x76 += einsum("ia->ia", x75) * -1
    del x75
    x78 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x78 += einsum("ia,ijab->jb", r1.bb, x10)
    x79 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x79 += einsum("ia->ia", x78) * -1
    del x78
    x90 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x90 += einsum("ijab,ikab->kj", t2.bbbb, x10)
    x93 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x93 += einsum("ij->ij", x90) * -1
    x465 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x465 += einsum("ij->ij", x90) * -1
    x495 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x495 += einsum("ij->ji", x90) * -1
    del x90
    x103 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x103 += einsum("ijab,jkbc->ikac", t2.abab, x10)
    x104 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x104 += einsum("ijab->ijab", x103) * -1
    x282 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x282 += einsum("ijab->ijab", x103) * -1
    del x103
    x451 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x451 += einsum("ijab,ijcb->ca", t2.bbbb, x10)
    x453 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x453 += einsum("ab->ba", x451) * -1
    x493 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x493 += einsum("ab->ba", x451) * -1
    del x451
    x14 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x14 += einsum("ijab,kcjb->ikac", t2.abab, v.aabb.ovov)
    x18 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x18 += einsum("ijab->jiab", x14)
    x99 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x99 += einsum("ijab->ijab", x14)
    x172 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x172 += einsum("ijab->ijab", x14)
    x192 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x192 += einsum("ijab->ijab", x14)
    x237 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x237 += einsum("ijab->jiab", x14)
    del x14
    x15 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x15 -= einsum("ijab->jiab", t2.aaaa)
    x15 += einsum("ijab->jiba", t2.aaaa)
    x19 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x19 += einsum("iajb,ikca->kjcb", v.aabb.ovov, x15)
    x22 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x22 -= einsum("ijab->ijab", x19)
    del x19
    x216 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x216 += einsum("ia,ijba->jb", f.aa.ov, x15)
    x223 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x223 -= einsum("ia->ia", x216)
    del x216
    x16 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x16 -= einsum("iajb->jiab", v.aaaa.ovov)
    x16 += einsum("iajb->jiba", v.aaaa.ovov)
    x17 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x17 += einsum("ijab,ikcb->jkac", x15, x16)
    del x15
    x18 += einsum("ijab->jiab", x17)
    del x17
    x64 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x64 += einsum("ijab,ikca->kjcb", t2.abab, x16)
    x66 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x66 -= einsum("ijab->ijab", x64)
    del x64
    x174 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x174 += einsum("ia,ijba->jb", t1.aa, x16)
    x175 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x175 -= einsum("ia->ia", x174)
    x220 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x220 -= einsum("ia->ia", x174)
    del x174
    x194 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x194 += einsum("ia,ijba->jb", r1.aa, x16)
    del x16
    x195 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x195 -= einsum("ia->ia", x194)
    del x194
    x18 += einsum("iabj->ijba", v.aaaa.ovvo)
    x18 -= einsum("ijab->ijab", v.aaaa.oovv)
    x214 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x214 += einsum("ia,ijba->jb", t1.aa, x18)
    x223 += einsum("ia->ia", x214)
    del x214
    ree1new_aa += einsum("ia,ijba->jb", r1.aa, x18)
    del x18
    x20 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x20 += einsum("iajb->jiab", v.bbbb.ovov)
    x20 -= einsum("iajb->jiba", v.bbbb.ovov)
    x21 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x21 += einsum("ijab,jkbc->ikac", t2.abab, x20)
    x22 -= einsum("ijab->ijab", x21)
    del x21
    x392 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x392 += einsum("ia,ijab->jb", t1.bb, x20)
    x393 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x393 -= einsum("ia->ia", x392)
    x437 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x437 -= einsum("ia->ia", x392)
    del x392
    x412 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x412 += einsum("ia,ijab->jb", r1.bb, x20)
    x413 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x413 -= einsum("ia->ia", x412)
    del x412
    x22 += einsum("iabj->jiba", v.bbaa.ovvo)
    x215 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x215 += einsum("ia,jiba->jb", t1.bb, x22)
    x223 += einsum("ia->ia", x215)
    del x215
    ree1new_aa += einsum("ia,jiba->jb", r1.bb, x22)
    del x22
    x23 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x23 += einsum("ijab->ijab", r2.aaaa)
    x23 += einsum("ijab->ijba", r2.aaaa) * -1
    x23 += einsum("ijab->jiab", r2.aaaa) * -1
    x23 += einsum("ijab->jiba", r2.aaaa)
    x286 += einsum("iajk,liba->ljkb", v.aabb.ovoo, x23)
    x385 += einsum("iajk,liba->ljkb", v.aabb.ovoo, x23) * 0.5
    ree1new_aa += einsum("ia,jiba->jb", f.aa.ov, x23) * 0.5
    x24 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x24 += einsum("ia,iabc->bc", r1.bb, v.bbaa.ovvv)
    x27 += einsum("ab->ab", x24) * -1
    x207 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x207 += einsum("ab->ab", x24)
    x334 += einsum("ab->ab", x24) * -2
    del x24
    x25 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x25 += einsum("iajb->jiab", v.aaaa.ovov) * -1
    x25 += einsum("iajb->jiba", v.aaaa.ovov)
    x27 += einsum("ijab,ijac->cb", x25, x3) * 0.5
    x31 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x31 += einsum("ia,ijba->jb", t1.aa, x25)
    x32 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x32 += einsum("ia->ia", x31) * -1
    del x31
    x34 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x34 += einsum("ia,ijba->jb", r1.aa, x25)
    x35 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x35 += einsum("ia->ia", x34) * -1
    del x34
    x39 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x39 += einsum("ijab,ijcb->ac", t2.aaaa, x25)
    x41 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum("ab->ab", x39) * -1
    del x39
    x109 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x109 += einsum("ijab,ijbc->ac", t2.aaaa, x25)
    x111 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x111 += einsum("ab->ab", x109) * -1
    x158 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x158 += einsum("ab->ab", x109) * -1
    del x109
    x127 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x127 += einsum("ijab,ijac->cb", x25, x3)
    x129 += einsum("ab->ab", x127)
    x130 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x130 += einsum("ab,ijbc->ijca", x129, t2.aaaa) * 0.5
    del x129
    x164 += einsum("ijab->jiba", x130)
    del x130
    x334 += einsum("ab->ab", x127)
    del x127
    x131 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x131 += einsum("ijab,ikab->jk", x0, x25)
    del x0
    x132 += einsum("ij->ij", x131)
    del x131
    x133 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x133 += einsum("ij,jkab->kiab", x132, t2.aaaa) * 0.5
    del x132
    x164 += einsum("ijab->jiba", x133)
    del x133
    x160 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x160 += einsum("ijab,ikba->jk", t2.aaaa, x25)
    x161 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x161 += einsum("ij->ij", x160) * -1
    del x160
    x231 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x231 += einsum("ijab,ikca->kjcb", t2.abab, x25)
    x234 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x234 += einsum("ijab->ijab", x231) * -1
    x261 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x261 += einsum("ijab->ijab", x231) * -1
    del x231
    x26 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x26 += einsum("iabc->ibac", v.aaaa.ovvv) * -1
    x26 += einsum("iabc->ibca", v.aaaa.ovvv)
    x27 += einsum("ia,ibca->bc", r1.aa, x26) * -1
    ree1new_aa += einsum("ia,ba->ib", t1.aa, x27) * -1
    del x27
    x40 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x40 += einsum("ia,ibac->bc", t1.aa, x26)
    x41 += einsum("ab->ab", x40) * -1
    del x40
    x110 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x110 += einsum("ia,ibca->bc", t1.aa, x26)
    x111 += einsum("ab->ab", x110) * -1
    del x110
    x120 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x120 += einsum("iabc,jibd->jdac", x26, x5)
    x122 += einsum("iabc->iabc", x120) * -1
    del x120
    x123 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x123 += einsum("ia,jbca->ijbc", t1.aa, x122) * 0.5
    del x122
    x164 += einsum("ijab->jiab", x123)
    del x123
    x290 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x290 += einsum("iabc,ijcd->jabd", x26, x4)
    x295 += einsum("iabc->iabc", x290)
    del x290
    x333 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x333 += einsum("ia,ibca->bc", r1.aa, x26) * 2
    x334 += einsum("ab->ab", x333) * -1
    del x333
    x335 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x335 += einsum("ab,ijbc->ijac", x334, t2.abab) * 0.5
    del x334
    ree2new_abab += einsum("ijab->ijab", x335) * -1
    ree2new_baba += einsum("ijab->jiba", x335) * -1
    del x335
    x339 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x339 += einsum("ijab,icad->jcdb", t2.abab, x26)
    del x26
    x343 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x343 += einsum("iabc->iabc", x339) * -1
    del x339
    x28 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x28 += einsum("ia,jkia->jk", r1.bb, v.aabb.ooov)
    x36 += einsum("ij->ij", x28) * 2
    x211 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x211 += einsum("ij->ij", x28)
    x364 += einsum("ij->ij", x28)
    del x28
    x30 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x30 += einsum("ia,jbia->jb", t1.bb, v.aabb.ovov)
    x32 += einsum("ia->ia", x30)
    x175 += einsum("ia->ia", x30)
    x220 += einsum("ia->ia", x30)
    del x30
    x221 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x221 += einsum("ia,ja->ij", t1.aa, x220)
    del x220
    x222 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x222 += einsum("ia,ji->ja", t1.aa, x221)
    del x221
    x223 -= einsum("ia->ia", x222)
    del x222
    x32 += einsum("ia->ia", f.aa.ov)
    x36 += einsum("ia,ja->ji", r1.aa, x32) * 2
    x46 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x46 += einsum("ia,ja->ij", t1.aa, x32)
    x47 += einsum("ij->ji", x46)
    x124 += einsum("ij->ji", x46)
    del x46
    x117 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x117 += einsum("ia,jkab->jkib", x32, x3)
    x118 += einsum("ijka->kija", x117) * -1
    del x117
    x258 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x258 += einsum("ia,jkab->jikb", x32, x4) * 0.5
    x278 += einsum("ijka->jika", x258)
    del x258
    x308 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x308 += einsum("ia,jkab->jikb", x32, t2.abab)
    x314 += einsum("ijka->jika", x308)
    del x308
    x362 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x362 += einsum("ia,ja->ij", r1.aa, x32)
    del x32
    x364 += einsum("ij->ji", x362)
    del x362
    x33 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x33 += einsum("ia,jbia->jb", r1.bb, v.aabb.ovov)
    x35 += einsum("ia->ia", x33)
    x36 += einsum("ia,ja->ji", t1.aa, x35) * 2
    ree1new_aa += einsum("ia,ij->ja", t1.aa, x36) * -0.5
    del x36
    x272 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x272 += einsum("ia,jkab->jikb", x35, t2.abab)
    x278 += einsum("ijka->jika", x272)
    del x272
    x363 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x363 += einsum("ia,ja->ij", t1.aa, x35)
    del x35
    x364 += einsum("ij->ji", x363)
    del x363
    x365 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x365 += einsum("ij,ikab->jkab", x364, t2.abab)
    del x364
    ree2new_abab += einsum("ijab->ijab", x365) * -1
    ree2new_baba += einsum("ijab->jiba", x365) * -1
    del x365
    x195 += einsum("ia->ia", x33)
    del x33
    x196 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x196 += einsum("ia,jkab->jkib", x195, t2.aaaa)
    x200 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x200 -= einsum("ijka->jkia", x196)
    del x196
    x203 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x203 += einsum("ia,ja->ij", t1.aa, x195)
    del x195
    x204 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x204 += einsum("ij->ij", x203)
    del x203
    x37 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x37 += einsum("ia,iabc->bc", t1.bb, v.bbaa.ovvv)
    x41 += einsum("ab->ab", x37)
    x111 += einsum("ab->ab", x37) * -1
    x218 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x218 += einsum("ab->ab", x37)
    del x37
    x38 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x38 += einsum("ijab,icjb->ac", t2.abab, v.aabb.ovov)
    x41 += einsum("ab->ab", x38) * -1
    x111 += einsum("ab->ab", x38)
    x112 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x112 += einsum("ab,ijbc->ijca", x111, x3) * 0.5
    del x3
    del x111
    x164 += einsum("ijab->ijab", x112)
    del x112
    x158 += einsum("ab->ab", x38)
    del x38
    x159 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x159 += einsum("ia,ba->ib", t1.aa, x158)
    del x158
    x163 += einsum("ia->ia", x159)
    del x159
    x41 += einsum("ab->ab", f.aa.vv)
    x288 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x288 += einsum("ab,ijbc->ijac", x41, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x288)
    ree2new_baba += einsum("ijab->jiba", x288)
    del x288
    x371 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x371 += einsum("ia,ba->ib", t1.aa, x41)
    x373 += einsum("ia->ia", x371)
    del x371
    ree1new_aa += einsum("ia,ba->ib", r1.aa, x41)
    del x41
    x42 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x42 += einsum("ia,jkia->jk", t1.bb, v.aabb.ooov)
    x47 += einsum("ij->ij", x42)
    x124 += einsum("ij->ij", x42)
    x228 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x228 += einsum("ij->ij", x42)
    del x42
    x43 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x43 += einsum("ijab,kajb->ik", t2.abab, v.aabb.ovov)
    x47 += einsum("ij->ji", x43)
    x124 += einsum("ij->ji", x43)
    x161 += einsum("ij->ij", x43)
    del x43
    x162 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x162 += einsum("ia,ji->ja", t1.aa, x161)
    del x161
    x163 += einsum("ia->ia", x162)
    del x162
    x47 += einsum("ij->ij", f.aa.oo)
    x327 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x327 += einsum("ij,ikab->jkab", x47, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x327) * -1
    ree2new_baba += einsum("ijab->jiba", x327) * -1
    del x327
    x372 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x372 += einsum("ia,ij->ja", t1.aa, x47)
    x373 += einsum("ia->ia", x372) * -1
    del x372
    ree1new_aa += einsum("ia,ij->ja", r1.aa, x47) * -1
    del x47
    x48 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x48 += einsum("ijab->ijab", r2.bbbb)
    x48 += einsum("ijab->jiab", r2.bbbb) * -1
    x490 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x490 += einsum("ij,ikab->jkab", f.bb.oo, x48) * 0.5
    x498 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x498 += einsum("ijab->ijab", x490) * -1
    del x490
    x49 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x49 += einsum("iabc->ibac", v.bbbb.ovvv) * -1
    x49 += einsum("iabc->ibca", v.bbbb.ovvv)
    x69 += einsum("ia,ibca->bc", r1.bb, x49) * -1
    x330 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x330 += einsum("ia,ibca->bc", r1.bb, x49) * 2
    x331 += einsum("ab->ab", x330) * -1
    del x330
    x377 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x377 += einsum("ijab,icab->jc", t2.bbbb, x49)
    x384 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x384 += einsum("ia->ia", x377) * -1
    del x377
    x452 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x452 += einsum("ia,ibca->bc", t1.bb, x49)
    x453 += einsum("ab->ab", x452) * -1
    del x452
    x483 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x483 += einsum("ijab,kcba->ijkc", r2.bbbb, x49)
    x484 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x484 += einsum("ijka->ijka", x483) * -1
    del x483
    ree1new_bb += einsum("ijab,icba->jc", x48, x49) * 0.5
    del x48
    del x49
    x50 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x50 += einsum("ijka->ikja", v.bbbb.ooov)
    x50 += einsum("ijka->kija", v.bbbb.ooov) * -1
    x80 += einsum("ia,ijka->jk", r1.bb, x50) * -2
    x91 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x91 += einsum("ia,ijka->jk", t1.bb, x50)
    x93 += einsum("ij->ij", x91) * -1
    x465 += einsum("ij->ij", x91) * -1
    del x91
    x318 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x318 += einsum("ijab,jklb->ikla", t2.abab, x50)
    x324 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x324 += einsum("ijka->ijka", x318) * -1
    del x318
    x354 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x354 += einsum("ia,ijka->jk", r1.bb, x50)
    x357 += einsum("ij->ij", x354) * -1
    del x354
    x378 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x378 += einsum("ijab,ijkb->ka", t2.bbbb, x50)
    x384 += einsum("ia->ia", x378) * -1
    del x378
    x51 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x51 += einsum("ijab->ijab", r2.bbbb) * -1
    x51 += einsum("ijab->ijba", r2.bbbb)
    ree1new_bb += einsum("ijka,ijba->kb", x50, x51) * 0.5
    del x50
    x52 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x52 += einsum("ijab->ijab", r2.bbbb) * -1
    x52 += einsum("ijab->ijba", r2.bbbb)
    x52 += einsum("ijab->jiab", r2.bbbb)
    x52 += einsum("ijab->jiba", r2.bbbb) * -1
    x53 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x53 += einsum("ijab,ikca->jkbc", x10, x52)
    x55 += einsum("ijab->jiba", x53) * -1
    del x53
    x457 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x457 += einsum("ia,jkba->ijkb", t1.bb, x55)
    x459 += einsum("ijka->kjia", x457)
    del x457
    ree1new_bb += einsum("ia,jiba->jb", t1.bb, x55) * 0.5
    del x55
    x57 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x57 += einsum("ijab->ijab", r2.bbbb)
    x57 += einsum("ijab->ijba", r2.bbbb) * -1
    x57 += einsum("ijab->jiab", r2.bbbb) * -1
    x57 += einsum("ijab->jiba", r2.bbbb)
    x58 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x58 += einsum("iajb,jkbc->ikac", v.aabb.ovov, x57)
    x59 += einsum("ijab->ijab", x58)
    del x58
    x259 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x259 += einsum("ia,jkab->ijkb", t1.aa, x59) * 0.5
    x278 += einsum("ijka->jika", x259)
    del x259
    ree1new_bb += einsum("ia,ijab->jb", t1.aa, x59) * 0.5
    del x59
    x255 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x255 += einsum("ijka,klab->ijlb", v.aabb.ooov, x57) * 0.5
    x278 += einsum("ijka->ijka", x255)
    del x255
    x289 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x289 += einsum("iabc,ijad->jbcd", v.bbaa.ovvv, x57)
    x295 += einsum("iabc->iabc", x289)
    del x289
    x296 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x296 += einsum("ia,jbac->ijbc", t1.aa, x295) * 0.5
    del x295
    ree2new_abab += einsum("ijab->ijab", x296)
    ree2new_baba += einsum("ijab->jiba", x296)
    del x296
    ree1new_bb += einsum("ia,ijab->jb", f.bb.ov, x57) * 0.5
    x60 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x60 += einsum("ijab,iakc->jkbc", t2.abab, v.aabb.ovov)
    x63 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x63 += einsum("ijab->jiab", x60)
    x240 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x240 += einsum("ijab->jiab", x60)
    x390 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x390 += einsum("ijab->ijab", x60)
    x410 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x410 += einsum("ijab->ijab", x60)
    x445 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x445 += einsum("ijab->ijab", x60)
    del x60
    x61 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x61 += einsum("ijab->jiab", t2.bbbb)
    x61 -= einsum("ijab->jiba", t2.bbbb)
    x62 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x62 += einsum("ijab,ikac->jkbc", x20, x61)
    del x20
    x63 += einsum("ijab->ijba", x62)
    x390 += einsum("ijab->jiba", x62)
    x410 += einsum("ijab->jiba", x62)
    del x62
    x65 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x65 += einsum("iajb,jkbc->ikac", v.aabb.ovov, x61)
    x66 -= einsum("ijab->ijab", x65)
    del x65
    x433 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x433 += einsum("ia,ijab->jb", f.bb.ov, x61)
    x440 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x440 -= einsum("ia->ia", x433)
    del x433
    x63 += einsum("iabj->ijba", v.bbbb.ovvo)
    x63 -= einsum("ijab->ijab", v.bbbb.oovv)
    x431 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x431 += einsum("ia,ijba->jb", t1.bb, x63)
    x440 += einsum("ia->ia", x431)
    del x431
    ree1new_bb += einsum("ia,ijba->jb", r1.bb, x63)
    del x63
    x66 += einsum("iabj->ijab", v.aabb.ovvo)
    x432 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x432 += einsum("ia,ijab->jb", t1.aa, x66)
    x440 += einsum("ia->ia", x432)
    del x432
    ree1new_bb += einsum("ia,ijab->jb", r1.aa, x66)
    del x66
    x67 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x67 += einsum("ia,iabc->bc", r1.aa, v.aabb.ovvv)
    x69 += einsum("ab->ab", x67) * -1
    x331 += einsum("ab->ab", x67) * -2
    x425 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x425 += einsum("ab->ab", x67)
    del x67
    x68 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x68 += einsum("ijab->ijab", r2.bbbb)
    x68 += einsum("ijab->ijba", r2.bbbb) * -1
    x69 += einsum("ijab,ijbc->ca", x10, x68) * 0.5
    ree1new_bb += einsum("ia,ba->ib", t1.bb, x69) * -1
    del x69
    x328 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x328 += einsum("ijab,ijbc->ac", x10, x68)
    x331 += einsum("ab->ba", x328)
    x332 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x332 += einsum("ab,ijcb->ijca", x331, t2.abab) * 0.5
    del x331
    ree2new_abab += einsum("ijab->ijab", x332) * -1
    ree2new_baba += einsum("ijab->jiba", x332) * -1
    del x332
    x467 += einsum("ab->ba", x328)
    del x328
    x468 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x468 += einsum("ab,ijbc->ijca", x467, t2.bbbb) * 0.5
    del x467
    x498 += einsum("ijab->jiba", x468)
    del x468
    x476 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x476 += einsum("ab,ijcb->ijac", f.bb.vv, x68) * 0.5
    x498 += einsum("ijab->ijab", x476) * -1
    del x476
    x70 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x70 += einsum("ia,iajk->jk", r1.aa, v.aabb.ovoo)
    x80 += einsum("ij->ij", x70) * 2
    x357 += einsum("ij->ij", x70)
    x429 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x429 += einsum("ij->ij", x70)
    del x70
    x71 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x71 += einsum("ijab->ijab", r2.bbbb) * -1
    x71 += einsum("ijab->jiab", r2.bbbb)
    x72 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x72 += einsum("ijab,kiba->jk", x10, x71)
    x80 += einsum("ij->ij", x72)
    x469 += einsum("ij->ji", x72)
    del x72
    x470 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x470 += einsum("ij,jkab->kiab", x469, t2.bbbb) * 0.5
    del x469
    x498 += einsum("ijab->jiba", x470)
    del x470
    x352 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x352 += einsum("ijab,kiba->jk", x10, x71) * 0.5
    x357 += einsum("ij->ij", x352)
    del x352
    x74 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x74 += einsum("ia,iajb->jb", t1.aa, v.aabb.ovov)
    x76 += einsum("ia->ia", x74)
    x393 += einsum("ia->ia", x74)
    x437 += einsum("ia->ia", x74)
    del x74
    x438 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x438 += einsum("ia,ja->ij", t1.bb, x437)
    del x437
    x439 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x439 += einsum("ia,ji->ja", t1.bb, x438)
    del x438
    x440 -= einsum("ia->ia", x439)
    del x439
    x76 += einsum("ia->ia", f.bb.ov)
    x80 += einsum("ia,ja->ji", r1.bb, x76) * 2
    x92 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x92 += einsum("ia,ja->ij", t1.bb, x76)
    x93 += einsum("ij->ji", x92)
    x465 += einsum("ij->ji", x92)
    del x92
    x286 += einsum("ia,jkba->jikb", x76, x4)
    x321 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x321 += einsum("ia,jkba->jkib", x76, t2.abab)
    x324 += einsum("ijka->ikja", x321)
    del x321
    x355 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x355 += einsum("ia,ja->ij", r1.bb, x76)
    x357 += einsum("ij->ji", x355)
    del x355
    x385 += einsum("ia,jkba->jikb", x76, x4) * 0.5
    x458 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x458 += einsum("ia,jkab->jkib", x76, x68)
    del x68
    del x76
    x459 += einsum("ijka->kija", x458) * -1
    del x458
    x77 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x77 += einsum("ia,iajb->jb", r1.aa, v.aabb.ovov)
    x79 += einsum("ia->ia", x77)
    x80 += einsum("ia,ja->ji", t1.bb, x79) * 2
    ree1new_bb += einsum("ia,ij->ja", t1.bb, x80) * -0.5
    del x80
    x286 += einsum("ia,jkba->jikb", x79, t2.abab) * 2
    x356 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x356 += einsum("ia,ja->ij", t1.bb, x79)
    x357 += einsum("ij->ji", x356)
    del x356
    x358 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x358 += einsum("ij,kiab->kjab", x357, t2.abab)
    del x357
    ree2new_abab += einsum("ijab->ijab", x358) * -1
    ree2new_baba += einsum("ijab->jiba", x358) * -1
    del x358
    x385 += einsum("ia,jkba->jikb", x79, t2.abab)
    del x79
    x413 += einsum("ia->ia", x77)
    del x77
    x414 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x414 += einsum("ia,jkab->jkib", x413, t2.bbbb)
    x418 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x418 -= einsum("ijka->jkia", x414)
    del x414
    x421 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x421 += einsum("ia,ja->ij", t1.bb, x413)
    del x413
    x422 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x422 += einsum("ij->ij", x421)
    del x421
    x81 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x81 += einsum("ia,iabc->bc", t1.aa, v.aabb.ovvv)
    x87 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x87 += einsum("ab->ab", x81)
    x435 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x435 += einsum("ab->ab", x81)
    x453 += einsum("ab->ab", x81) * -1
    del x81
    x82 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x82 += einsum("ijab,iajc->bc", t2.abab, v.aabb.ovov)
    x87 += einsum("ab->ab", x82) * -1
    x453 += einsum("ab->ab", x82)
    x454 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x454 += einsum("ab,ijcb->ijca", x453, x51) * 0.5
    del x51
    del x453
    x498 += einsum("ijab->ijab", x454)
    del x454
    x493 += einsum("ab->ab", x82)
    del x82
    x494 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x494 += einsum("ia,ba->ib", t1.bb, x493)
    del x493
    x497 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x497 += einsum("ia->ia", x494)
    del x494
    x83 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x83 += einsum("iajb->jiab", v.bbbb.ovov) * -1
    x83 += einsum("iajb->jiba", v.bbbb.ovov)
    x84 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x84 += einsum("ijab,ijcb->ac", t2.bbbb, x83)
    del x83
    x87 += einsum("ab->ab", x84) * -1
    del x84
    x85 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x85 += einsum("iabc->ibac", v.bbbb.ovvv)
    x85 += einsum("iabc->ibca", v.bbbb.ovvv) * -1
    x86 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x86 += einsum("ia,ibca->bc", t1.bb, x85)
    x87 += einsum("ab->ab", x86) * -1
    del x86
    x298 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x298 += einsum("ijab,jcdb->iacd", x4, x85)
    x301 += einsum("iabc->iabc", x298) * -1
    del x298
    x302 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x302 += einsum("ia,jbca->jibc", t1.bb, x301) * 0.5
    del x301
    ree2new_abab += einsum("ijab->ijab", x302)
    ree2new_baba += einsum("ijab->jiba", x302)
    del x302
    x348 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x348 += einsum("ijab,jcdb->iacd", t2.abab, x85)
    x350 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x350 += einsum("iabc->iabc", x348) * -1
    del x348
    x461 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x461 += einsum("ijab,icdb->jacd", x52, x85)
    x463 += einsum("iabc->iabc", x461) * -1
    del x461
    x464 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x464 += einsum("ia,jbca->ijbc", t1.bb, x463) * 0.5
    del x463
    x498 += einsum("ijab->jiab", x464)
    del x464
    x491 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x491 += einsum("ijab,icab->jc", t2.bbbb, x85)
    del x85
    x497 += einsum("ia->ia", x491) * -1
    del x491
    x87 += einsum("ab->ab", f.bb.vv)
    x287 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x287 += einsum("ab,ijcb->ijca", x87, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x287)
    ree2new_baba += einsum("ijab->jiba", x287)
    del x287
    x382 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x382 += einsum("ia,ba->ib", t1.bb, x87)
    x384 += einsum("ia->ia", x382)
    del x382
    ree1new_bb += einsum("ia,ba->ib", r1.bb, x87)
    del x87
    x88 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x88 += einsum("ia,iajk->jk", t1.aa, v.aabb.ovoo)
    x93 += einsum("ij->ij", x88)
    x465 += einsum("ij->ij", x88)
    x502 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x502 += einsum("ij->ij", x88)
    del x88
    x89 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x89 += einsum("ijab,iakb->jk", t2.abab, v.aabb.ovov)
    x93 += einsum("ij->ji", x89)
    x465 += einsum("ij->ji", x89)
    x466 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x466 += einsum("ij,ikab->kjab", x465, x71) * 0.5
    del x465
    del x71
    x498 += einsum("ijab->ijab", x466) * -1
    del x466
    x495 += einsum("ij->ij", x89)
    del x89
    x496 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x496 += einsum("ia,ji->ja", t1.bb, x495)
    del x495
    x497 += einsum("ia->ia", x496)
    del x496
    x93 += einsum("ij->ij", f.bb.oo)
    x326 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x326 += einsum("ij,kiab->kjab", x93, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x326) * -1
    ree2new_baba += einsum("ijab->jiba", x326) * -1
    del x326
    x383 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x383 += einsum("ia,ij->ja", t1.bb, x93)
    x384 += einsum("ia->ia", x383) * -1
    del x383
    ree1new_bb += einsum("ia,ij->ja", r1.bb, x93) * -1
    del x93
    x94 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x94 += einsum("ijab,cbda->ijdc", r2.aaaa, v.aaaa.vvvv)
    x164 += einsum("ijab->ijab", x94) * 0.5
    del x94
    x95 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x95 += einsum("ijab,kbla->ijlk", r2.aaaa, v.aaaa.ovov)
    x96 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x96 += einsum("ijab,klji->klba", t2.aaaa, x95)
    x164 += einsum("ijab->ijab", x96) * 0.5
    del x96
    x145 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x145 += einsum("ia,jkli->jkla", t1.aa, x95)
    del x95
    x147 += einsum("ijka->ijka", x145)
    del x145
    x148 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x148 += einsum("ia,jkib->jkab", t1.aa, x147) * 0.5
    del x147
    x164 += einsum("ijab->ijab", x148)
    del x148
    x97 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x97 += einsum("ijab->jiab", t2.aaaa)
    x97 += einsum("ijab->jiba", t2.aaaa) * -1
    x98 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x98 += einsum("ijab,ikac->jkbc", x6, x97)
    del x97
    del x6
    x99 += einsum("ijab->jiba", x98)
    del x98
    x99 += einsum("iabj->jiba", v.aaaa.ovvo)
    x99 += einsum("ijab->jiab", v.aaaa.oovv) * -1
    x100 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x100 += einsum("ijab,kjca->ikbc", x5, x99) * 0.5
    del x99
    del x5
    x164 += einsum("ijab->ijab", x100)
    del x100
    x101 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x101 += einsum("ijab->jiab", t2.aaaa) * -1
    x101 += einsum("ijab->jiba", t2.aaaa)
    x102 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x102 += einsum("iajb,ikca->kjcb", v.aabb.ovov, x101)
    x104 += einsum("ijab->ijab", x102) * -1
    x282 += einsum("ijab->ijab", x102) * -1
    del x102
    x236 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x236 += einsum("ijab,ikcb->kjca", x101, x25)
    del x25
    x237 += einsum("ijab->ijba", x236)
    del x236
    x319 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x319 += einsum("iajk,ilba->ljkb", v.aabb.ovoo, x101)
    x324 += einsum("ijka->ijka", x319) * -1
    del x319
    x347 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x347 += einsum("iabc,ijda->jdbc", v.aabb.ovvv, x101)
    x350 += einsum("iabc->iabc", x347) * -1
    del x347
    x370 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x370 += einsum("ia,ijba->jb", f.aa.ov, x101)
    del x101
    x373 += einsum("ia->ia", x370) * -1
    del x370
    x104 += einsum("iabj->jiba", v.bbaa.ovvo)
    x105 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x105 += einsum("ijab,kjcb->kica", x104, x4) * 0.5
    x164 += einsum("ijab->ijab", x105)
    del x105
    x320 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x320 += einsum("ia,jkba->jikb", t1.bb, x104)
    x324 += einsum("ijka->ikja", x320)
    del x320
    x369 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x369 += einsum("ia,jiba->jb", t1.bb, x104)
    x373 += einsum("ia->ia", x369)
    del x369
    ree2new_abab += einsum("ijab,kjbc->ikac", x104, x52) * 0.5
    ree2new_baba += einsum("ijab,jkbc->kica", x104, x52) * -0.5
    del x104
    del x52
    x106 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x106 += einsum("ijab,kalb->ijkl", t2.aaaa, v.aaaa.ovov)
    x107 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x107 += einsum("ijkl->lkji", x106)
    x150 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x150 += einsum("ia,jkil->kjla", t1.aa, x106)
    del x106
    x151 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x151 += einsum("ijka->ijka", x150) * -1
    del x150
    x107 += einsum("ijkl->kilj", v.aaaa.oooo)
    x108 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x108 += einsum("ijab,jikl->klab", r2.aaaa, x107) * 0.5
    del x107
    x164 += einsum("ijab->jiab", x108)
    del x108
    x113 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x113 += einsum("ijka->ikja", v.aaaa.ooov) * -1
    x113 += einsum("ijka->kija", v.aaaa.ooov)
    x114 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x114 += einsum("ijka,jlab->likb", x113, x23)
    x118 += einsum("ijka->jika", x114) * -1
    del x114
    x119 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x119 += einsum("ia,ijkb->jkab", t1.aa, x118) * 0.5
    del x118
    x164 += einsum("ijab->ijba", x119) * -1
    del x119
    x254 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x254 += einsum("ijka,ilab->jklb", x113, x4) * 0.5
    x278 += einsum("ijka->ijka", x254)
    del x254
    x367 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x367 += einsum("ijab,ijka->kb", t2.aaaa, x113)
    del x113
    x373 += einsum("ia->ia", x367) * -1
    del x367
    x125 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x125 += einsum("ijab->ijab", r2.aaaa) * -1
    x125 += einsum("ijab->jiab", r2.aaaa)
    x126 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x126 += einsum("ij,ikab->jkab", x124, x125) * 0.5
    del x124
    del x125
    x164 += einsum("ijab->jiab", x126) * -1
    del x126
    x134 = np.zeros((nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x134 += einsum("ijab,jcid->abdc", r2.aaaa, v.aaaa.ovov)
    x135 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x135 += einsum("ia,bcda->ibcd", t1.aa, x134)
    del x134
    x137 += einsum("iabc->iabc", x135)
    del x135
    x138 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x138 += einsum("ia,jbca->ijbc", t1.aa, x137) * 0.5
    del x137
    x164 += einsum("ijab->ijab", x138)
    del x138
    x140 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x140 += einsum("ijab,jkic->kbac", t2.aaaa, v.aaaa.ooov)
    x143 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x143 += einsum("iabc->iabc", x140)
    del x140
    x141 = np.zeros((nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x141 += einsum("ijab,icjd->abcd", t2.aaaa, v.aaaa.ovov)
    x142 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x142 += einsum("ia,bcad->icbd", t1.aa, x141)
    del x141
    x143 += einsum("iabc->iabc", x142) * -1
    del x142
    x144 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x144 += einsum("ia,jbca->ijbc", r1.aa, x143)
    del x143
    x164 += einsum("ijab->ijab", x144) * -1
    del x144
    x149 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x149 += einsum("ijab,kbca->jikc", t2.aaaa, v.aaaa.ovvv)
    x151 += einsum("ijka->ijka", x149)
    del x149
    x152 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x152 += einsum("ia,jkib->jkab", r1.aa, x151)
    del x151
    x164 += einsum("ijab->ijab", x152) * -1
    del x152
    x154 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x154 += einsum("ijab,ikjb->ka", t2.abab, v.aabb.ooov)
    x163 += einsum("ia->ia", x154)
    x373 += einsum("ia->ia", x154) * -1
    del x154
    x155 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x155 += einsum("ijab,jbca->ic", t2.abab, v.bbaa.ovvv)
    x163 += einsum("ia->ia", x155) * -1
    x164 += einsum("ia,jb->ijab", r1.aa, x163) * -1
    del x163
    ree2new_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    ree2new_aaaa += einsum("ijab->ijab", x164)
    ree2new_aaaa += einsum("ijab->ijba", x164) * -1
    ree2new_aaaa += einsum("ijab->jiab", x164) * -1
    ree2new_aaaa += einsum("ijab->jiba", x164)
    del x164
    x373 += einsum("ia->ia", x155)
    del x155
    x165 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x165 += einsum("ijab,kljb->ikla", t2.abab, v.aabb.ooov)
    x182 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x182 += einsum("ijka->jika", x165)
    del x165
    x166 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x166 -= einsum("ijka->ikja", v.aaaa.ooov)
    x166 += einsum("ijka->kija", v.aaaa.ooov)
    x167 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x167 += einsum("ijab->jiab", t2.aaaa)
    x167 -= einsum("ijab->jiba", t2.aaaa)
    x168 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x168 += einsum("ijka,jlab->iklb", x166, x167)
    del x166
    x182 += einsum("ijka->ikja", x168)
    del x168
    x169 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x169 += einsum("ia,jbca->ijcb", t1.aa, v.aaaa.ovvv)
    x172 += einsum("ijab->ijab", x169)
    del x169
    x170 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x170 += einsum("iajb->jiab", v.aaaa.ovov)
    x170 -= einsum("iajb->jiba", v.aaaa.ovov)
    x171 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x171 += einsum("ijab,ikac->jkbc", x167, x170)
    del x170
    x172 += einsum("ijab->ijab", x171)
    x192 += einsum("ijab->ijab", x171)
    del x171
    x172 += einsum("iabj->jiba", v.aaaa.ovvo)
    x172 -= einsum("ijab->jiab", v.aaaa.oovv)
    x173 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x173 += einsum("ia,jkba->ijkb", t1.aa, x172)
    del x172
    x182 -= einsum("ijka->kija", x173)
    del x173
    x175 += einsum("ia->ia", f.aa.ov)
    x176 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x176 += einsum("ia,jkab->jkib", x175, t2.aaaa)
    x182 += einsum("ijka->kjia", x176)
    del x176
    x202 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x202 += einsum("ia,ja->ij", r1.aa, x175)
    del x175
    x204 += einsum("ij->ij", x202)
    del x202
    x205 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x205 += einsum("ij,jkab->kiab", x204, t2.aaaa)
    del x204
    x224 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x224 += einsum("ijab->jiba", x205)
    del x205
    x177 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x177 += einsum("ia,jakb->ikjb", t1.aa, v.aaaa.ovov)
    x178 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x178 += einsum("ia,jkla->jilk", t1.aa, x177)
    x180 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x180 += einsum("ijkl->lkji", x178)
    del x178
    x197 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x197 -= einsum("ijka->jkia", x177)
    del x177
    x179 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x179 += einsum("ia,jkla->ijlk", t1.aa, v.aaaa.ooov)
    x180 += einsum("ijkl->jkli", x179)
    x180 -= einsum("ijkl->kjli", x179)
    del x179
    x180 += einsum("ijkl->kilj", v.aaaa.oooo)
    x181 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x181 += einsum("ia,ijkl->jkla", t1.aa, x180)
    del x180
    x182 += einsum("ijka->ikja", x181)
    del x181
    x182 -= einsum("ijak->ijka", v.aaaa.oovo)
    x183 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x183 += einsum("ia,ijkb->jkab", r1.aa, x182)
    del x182
    x224 += einsum("ijab->ijab", x183)
    del x183
    x184 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x184 += einsum("ia,bacd->icbd", t1.aa, v.aaaa.vvvv)
    x188 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x188 -= einsum("iabc->iabc", x184)
    del x184
    x185 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x185 += einsum("ijab,jbcd->iacd", t2.abab, v.bbaa.ovvv)
    x188 += einsum("iabc->iabc", x185)
    del x185
    x186 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x186 -= einsum("iabc->ibac", v.aaaa.ovvv)
    x186 += einsum("iabc->ibca", v.aaaa.ovvv)
    x187 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x187 += einsum("ijab,icad->jbcd", x167, x186)
    del x167
    x188 += einsum("iabc->iabc", x187)
    del x187
    x206 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x206 += einsum("ia,ibac->bc", r1.aa, x186)
    x207 -= einsum("ab->ab", x206)
    del x206
    x208 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x208 += einsum("ab,ijbc->ijca", x207, t2.aaaa)
    del x207
    x224 += einsum("ijab->jiab", x208)
    del x208
    x217 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x217 += einsum("ia,ibac->bc", t1.aa, x186)
    del x186
    x218 -= einsum("ab->ab", x217)
    del x217
    x219 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x219 += einsum("ia,ba->ib", t1.aa, x218)
    del x218
    x223 += einsum("ia->ia", x219)
    del x219
    x188 += einsum("aibc->iabc", v.aaaa.vovv)
    x189 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x189 += einsum("ia,jbca->ijbc", r1.aa, x188)
    del x188
    x224 -= einsum("ijab->ijab", x189)
    del x189
    x190 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x190 += einsum("iabc->ibac", v.aaaa.ovvv)
    x190 -= einsum("iabc->ibca", v.aaaa.ovvv)
    x191 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x191 += einsum("ia,jbac->ijbc", t1.aa, x190)
    del x190
    x192 -= einsum("ijab->ijab", x191)
    del x191
    x192 += einsum("iabj->jiba", v.aaaa.ovvo)
    x192 -= einsum("ijab->jiab", v.aaaa.oovv)
    x193 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x193 += einsum("ia,jkba->ijkb", r1.aa, x192)
    del x192
    x200 += einsum("ijka->ikja", x193)
    del x193
    x197 += einsum("ijka->ikja", v.aaaa.ooov)
    x198 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x198 += einsum("ia,jkla->ijkl", r1.aa, x197)
    del x197
    x199 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x199 += einsum("ia,jkil->jkla", t1.aa, x198)
    del x198
    x200 += einsum("ijka->ijka", x199)
    del x199
    x201 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x201 += einsum("ia,jikb->jkab", t1.aa, x200)
    del x200
    x224 -= einsum("ijab->ijab", x201)
    del x201
    x209 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x209 += einsum("ijka->ikja", v.aaaa.ooov)
    x209 -= einsum("ijka->kija", v.aaaa.ooov)
    x210 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x210 += einsum("ia,ijka->jk", r1.aa, x209)
    x211 -= einsum("ij->ij", x210)
    del x210
    x212 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x212 += einsum("ij,ikab->kjab", x211, t2.aaaa)
    del x211
    x224 -= einsum("ijab->ijba", x212)
    del x212
    x227 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x227 += einsum("ia,ijka->jk", t1.aa, x209)
    del x209
    x228 -= einsum("ij->ij", x227)
    del x227
    x213 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x213 += einsum("ia,jiba->jb", f.bb.ov, t2.abab)
    x223 += einsum("ia->ia", x213)
    x224 += einsum("ia,jb->ijab", r1.aa, x223)
    del x223
    ree2new_aaaa += einsum("ijab->ijab", x224)
    ree2new_aaaa -= einsum("ijab->ijba", x224)
    ree2new_aaaa -= einsum("ijab->jiab", x224)
    ree2new_aaaa += einsum("ijab->jiba", x224)
    del x224
    x373 += einsum("ia->ia", x213)
    del x213
    x225 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x225 += einsum("ab,ib->ia", f.aa.vv, t1.aa)
    x230 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x230 -= einsum("ia->ia", x225)
    del x225
    x226 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x226 += einsum("ia,ja->ij", f.aa.ov, t1.aa)
    x228 += einsum("ij->ij", x226)
    del x226
    x228 += einsum("ij->ij", f.aa.oo)
    x229 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x229 += einsum("ia,ij->ja", t1.aa, x228)
    del x228
    x230 += einsum("ia->ia", x229)
    del x229
    x230 -= einsum("ai->ia", f.aa.vo)
    ree2new_aaaa -= einsum("ia,jb->jiba", r1.aa, x230)
    ree2new_aaaa -= einsum("ia,jb->ijab", r1.aa, x230)
    ree2new_aaaa += einsum("ia,jb->ijba", r1.aa, x230)
    ree2new_aaaa += einsum("ia,jb->jiab", r1.aa, x230)
    del x230
    x232 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x232 += einsum("ijab->jiab", t2.bbbb)
    x232 += einsum("ijab->jiba", t2.bbbb) * -1
    x233 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x233 += einsum("iajb,jkbc->ikac", v.aabb.ovov, x232)
    x234 += einsum("ijab->ijab", x233) * -1
    x261 += einsum("ijab->ijab", x233) * -1
    del x233
    x239 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x239 += einsum("ijab,ikac->jkbc", x10, x232)
    del x10
    x240 += einsum("ijab->ijba", x239)
    x445 += einsum("ijab->jiba", x239)
    del x239
    x306 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x306 += einsum("ijka,klab->ijlb", v.aabb.ooov, x232)
    x314 += einsum("ijka->ijka", x306) * -1
    del x306
    x338 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x338 += einsum("iabc,ijad->jbcd", v.bbaa.ovvv, x232)
    x343 += einsum("iabc->iabc", x338) * -1
    del x338
    x381 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x381 += einsum("ia,ijab->jb", f.bb.ov, x232)
    del x232
    x384 += einsum("ia->ia", x381) * -1
    del x381
    x234 += einsum("iabj->ijab", v.aabb.ovvo)
    x235 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x235 += einsum("ijab,jkbc->ikac", x23, x234) * 0.5
    del x23
    ree2new_abab += einsum("ijab->ijab", x235)
    ree2new_baba += einsum("ijab->jiba", x235)
    del x235
    x380 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x380 += einsum("ia,ijab->jb", t1.aa, x234)
    x384 += einsum("ia->ia", x380)
    del x380
    x447 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x447 += einsum("ijab,ikac->kjcb", x234, x4) * 0.5
    del x234
    x498 += einsum("ijab->ijab", x447)
    del x447
    x237 += einsum("iabj->ijba", v.aaaa.ovvo)
    x237 += einsum("ijab->ijab", v.aaaa.oovv) * -1
    x238 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x238 += einsum("ijab,ikbc->jkac", x237, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x238)
    ree2new_baba += einsum("ijab->jiba", x238)
    del x238
    x368 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x368 += einsum("ia,ijba->jb", t1.aa, x237)
    del x237
    x373 += einsum("ia->ia", x368)
    del x368
    x240 += einsum("iabj->ijba", v.bbbb.ovvo)
    x240 += einsum("ijab->ijab", v.bbbb.oovv) * -1
    x241 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x241 += einsum("ijab,kicb->kjca", x240, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x241)
    ree2new_baba += einsum("ijab->jiba", x241)
    del x241
    x379 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x379 += einsum("ia,ijba->jb", t1.bb, x240)
    del x240
    x384 += einsum("ia->ia", x379)
    del x379
    x242 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x242 += einsum("ijab,ickb->jkac", t2.abab, v.aabb.ovov)
    x243 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x243 += einsum("ijab->jiab", x242) * -1
    x284 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x284 += einsum("ijab->jiab", x242) * -1
    del x242
    x243 += einsum("ijab->ijab", v.bbaa.oovv)
    x244 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x244 += einsum("ijab,kibc->kjac", x243, x4) * 0.5
    del x243
    ree2new_abab += einsum("ijab->ijab", x244) * -1
    ree2new_baba += einsum("ijab->jiba", x244) * -1
    del x244
    x245 = np.zeros((nocc[0], nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x245 += einsum("ijab,kajc->ikbc", t2.abab, v.aabb.ovov)
    x246 = np.zeros((nocc[0], nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x246 += einsum("ijab->jiab", x245) * -1
    x274 = np.zeros((nocc[0], nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x274 += einsum("ijab->jiab", x245) * -1
    del x245
    x246 += einsum("ijab->ijab", v.aabb.oovv)
    x247 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x247 += einsum("ijab,ikcb->jkca", x246, x4) * 0.5
    ree2new_abab += einsum("ijab->ijab", x247) * -1
    ree2new_baba += einsum("ijab->jiba", x247) * -1
    del x247
    x313 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x313 += einsum("ia,jkba->jkib", t1.bb, x246)
    del x246
    x314 += einsum("ijka->ijka", x313)
    del x313
    x249 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x249 += einsum("ijab,kalb->ikjl", t2.abab, v.aabb.ovov)
    x250 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x250 += einsum("ijkl->jilk", x249)
    x311 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x311 += einsum("ijkl->jilk", x249)
    del x249
    x250 += einsum("ijkl->ijkl", v.aabb.oooo)
    x251 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x251 += einsum("ijkl,ikab->jlab", x250, x4) * 0.5
    del x250
    ree2new_abab += einsum("ijab->ijab", x251)
    ree2new_baba += einsum("ijab->jiba", x251)
    del x251
    x260 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x260 += einsum("ia,jbca->jibc", t1.bb, v.aabb.ovvv)
    x261 += einsum("ijab->ijab", x260)
    del x260
    x261 += einsum("iabj->ijab", v.aabb.ovvo)
    x262 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x262 += einsum("ia,jkab->ijkb", r1.aa, x261)
    x278 += einsum("ijka->jika", x262)
    del x262
    x307 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x307 += einsum("ia,jkab->ijkb", t1.aa, x261)
    del x261
    x314 += einsum("ijka->jika", x307)
    del x307
    x264 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x264 += einsum("ia,jbka->jikb", t1.bb, v.aabb.ovov)
    x265 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x265 += einsum("ijka->ikja", x264)
    del x264
    x265 += einsum("iajk->ijka", v.aabb.ovoo)
    x266 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x266 += einsum("ia,jkla->ijkl", r1.aa, x265)
    x270 += einsum("ijkl->ijkl", x266)
    del x266
    x310 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x310 += einsum("ia,jkla->ijkl", t1.aa, x265)
    del x265
    x311 += einsum("ijkl->jikl", x310)
    del x310
    x267 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x267 += einsum("ia,jakb->ijkb", t1.aa, v.aabb.ovov)
    x268 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x268 += einsum("ijka->jika", x267)
    del x267
    x268 += einsum("ijka->ijka", v.aabb.ooov)
    x269 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x269 += einsum("ia,jkla->jkil", r1.bb, x268)
    del x268
    x270 += einsum("ijkl->jilk", x269)
    del x269
    x271 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x271 += einsum("ia,jkil->jkla", t1.bb, x270)
    del x270
    x278 += einsum("ijka->jika", x271) * -1
    del x271
    x273 = np.zeros((nocc[0], nocc[0], nvir[1], nvir[1]), dtype=np.float64)
    x273 += einsum("ia,jabc->ijbc", t1.aa, v.aabb.ovvv)
    x274 += einsum("ijab->jiab", x273)
    del x273
    x274 += einsum("ijab->ijab", v.aabb.oovv)
    x275 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x275 += einsum("ia,jkba->jkib", r1.bb, x274)
    del x274
    x278 += einsum("ijka->ijka", x275)
    del x275
    x279 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x279 += einsum("ia,ijkb->jkab", t1.aa, x278)
    del x278
    ree2new_abab += einsum("ijab->ijab", x279) * -1
    ree2new_baba += einsum("ijab->jiba", x279) * -1
    del x279
    x280 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x280 += einsum("ijka->ikja", v.bbbb.ooov) * -1
    x280 += einsum("ijka->kija", v.bbbb.ooov)
    x286 += einsum("ijka,liba->ljkb", x280, x4)
    x385 += einsum("ijka,liba->ljkb", x280, x4) * 0.5
    del x4
    x455 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x455 += einsum("ijka,jlab->likb", x280, x57)
    x459 += einsum("ijka->jika", x455) * -1
    del x455
    x460 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x460 += einsum("ia,ijkb->jkab", t1.bb, x459) * 0.5
    del x459
    x498 += einsum("ijab->ijba", x460) * -1
    del x460
    x473 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x473 += einsum("ijab,jikc->kabc", r2.bbbb, x280)
    x474 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x474 += einsum("iabc->iabc", x473) * -1
    del x473
    x492 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x492 += einsum("ijab,ijkb->ka", t2.bbbb, x280)
    del x280
    x497 += einsum("ia->ia", x492) * -1
    del x492
    x281 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x281 += einsum("ia,jbca->ijcb", t1.aa, v.bbaa.ovvv)
    x282 += einsum("ijab->ijab", x281)
    del x281
    x282 += einsum("iabj->jiba", v.bbaa.ovvo)
    x286 += einsum("ia,jkba->jkib", r1.bb, x282) * 2
    x385 += einsum("ia,jkba->jkib", r1.bb, x282)
    del x282
    x283 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x283 += einsum("ia,jabc->ijbc", t1.bb, v.bbaa.ovvv)
    x284 += einsum("ijab->jiab", x283)
    del x283
    x284 += einsum("ijab->ijab", v.bbaa.oovv)
    x286 += einsum("ia,jkba->ijkb", r1.aa, x284) * 2
    ree2new_abab += einsum("ia,jikb->jkba", t1.bb, x286) * -0.5
    del x286
    x322 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x322 += einsum("ia,jkba->ijkb", t1.aa, x284)
    x324 += einsum("ijka->ijka", x322)
    del x322
    x385 += einsum("ia,jkba->ijkb", r1.aa, x284)
    del x284
    ree2new_baba += einsum("ia,jikb->kjab", t1.bb, x385) * -1
    del x385
    x303 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x303 += einsum("ijab,kajl->iklb", t2.abab, v.aabb.ovoo)
    x314 += einsum("ijka->jika", x303) * -1
    del x303
    x304 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x304 += einsum("ijab,kacb->ikjc", t2.abab, v.aabb.ovvv)
    x314 += einsum("ijka->jika", x304)
    del x304
    x309 = np.zeros((nocc[0], nocc[0], nocc[1], nocc[1]), dtype=np.float64)
    x309 += einsum("ia,jkla->jkil", t1.bb, v.aabb.ooov)
    x311 += einsum("ijkl->ijlk", x309)
    del x309
    x311 += einsum("ijkl->ijkl", v.aabb.oooo)
    x312 = np.zeros((nocc[0], nocc[0], nocc[1], nvir[1]), dtype=np.float64)
    x312 += einsum("ia,jkil->jkla", t1.bb, x311)
    x314 += einsum("ijka->ijka", x312) * -1
    del x312
    x323 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x323 += einsum("ia,ijkl->jkla", t1.aa, x311)
    del x311
    x324 += einsum("ijka->ijka", x323) * -1
    del x323
    x314 += einsum("ijak->ijka", v.aabb.oovo)
    x315 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x315 += einsum("ia,ijkb->jkab", r1.aa, x314)
    del x314
    ree2new_abab += einsum("ijab->ijab", x315) * -1
    ree2new_baba += einsum("ijab->jiba", x315) * -1
    del x315
    x316 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x316 += einsum("ijab,iklb->kjla", t2.abab, v.aabb.ooov)
    x324 += einsum("ijka->ikja", x316) * -1
    del x316
    x317 = np.zeros((nocc[0], nocc[1], nocc[1], nvir[0]), dtype=np.float64)
    x317 += einsum("ijab,kbca->ijkc", t2.abab, v.bbaa.ovvv)
    x324 += einsum("ijka->ikja", x317)
    del x317
    x324 += einsum("ijak->kija", v.bbaa.oovo)
    x325 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x325 += einsum("ia,jikb->jkba", r1.bb, x324)
    del x324
    ree2new_abab += einsum("ijab->ijab", x325) * -1
    ree2new_baba += einsum("ijab->jiba", x325) * -1
    del x325
    x336 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x336 += einsum("ijab,icjk->kacb", t2.abab, v.aabb.ovoo)
    x343 += einsum("iabc->iabc", x336)
    del x336
    x337 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x337 += einsum("ijab,icdb->jacd", t2.abab, v.aabb.ovvv)
    x343 += einsum("iabc->iabc", x337) * -1
    del x337
    x340 = np.zeros((nvir[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x340 += einsum("ijab,icjd->acbd", t2.abab, v.aabb.ovov)
    x341 = np.zeros((nvir[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x341 += einsum("abcd->abcd", x340)
    del x340
    x341 += einsum("abcd->abcd", v.aabb.vvvv)
    x342 = np.zeros((nocc[1], nvir[0], nvir[0], nvir[1]), dtype=np.float64)
    x342 += einsum("ia,bcda->ibcd", t1.bb, x341)
    x343 += einsum("iabc->iabc", x342)
    del x342
    x349 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x349 += einsum("ia,bacd->ibcd", t1.aa, x341)
    del x341
    x350 += einsum("iabc->iabc", x349)
    del x349
    x343 += einsum("abci->iabc", v.aabb.vvvo)
    x344 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x344 += einsum("ia,jbac->ijbc", r1.aa, x343)
    del x343
    ree2new_abab += einsum("ijab->ijab", x344)
    ree2new_baba += einsum("ijab->jiba", x344)
    del x344
    x345 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x345 += einsum("ijab,ikjc->kabc", t2.abab, v.aabb.ooov)
    x350 += einsum("iabc->iabc", x345)
    del x345
    x346 = np.zeros((nocc[0], nvir[0], nvir[1], nvir[1]), dtype=np.float64)
    x346 += einsum("ijab,jcda->idbc", t2.abab, v.bbaa.ovvv)
    x350 += einsum("iabc->iabc", x346) * -1
    del x346
    x350 += einsum("aibc->iabc", v.aabb.vovv)
    x351 = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    x351 += einsum("ia,jbca->jibc", r1.bb, x350)
    del x350
    ree2new_abab += einsum("ijab->ijab", x351)
    ree2new_baba += einsum("ijab->jiba", x351)
    del x351
    x373 += einsum("ai->ia", f.aa.vo)
    ree2new_abab += einsum("ia,jb->jiba", r1.bb, x373)
    ree2new_baba += einsum("ia,jb->ijab", r1.bb, x373)
    del x373
    x374 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x374 += einsum("ia,ijab->jb", f.aa.ov, t2.abab)
    x384 += einsum("ia->ia", x374)
    x440 += einsum("ia->ia", x374)
    del x374
    x375 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x375 += einsum("ijab,iajk->kb", t2.abab, v.aabb.ovoo)
    x384 += einsum("ia->ia", x375) * -1
    x497 += einsum("ia->ia", x375)
    del x375
    x376 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x376 += einsum("ijab,iacb->jc", t2.abab, v.aabb.ovvv)
    x384 += einsum("ia->ia", x376)
    x497 += einsum("ia->ia", x376) * -1
    del x376
    x498 += einsum("ia,jb->ijab", r1.bb, x497) * -1
    del x497
    x384 += einsum("ai->ia", f.bb.vo)
    ree2new_abab += einsum("ia,jb->ijab", r1.aa, x384)
    ree2new_baba += einsum("ia,jb->jiba", r1.aa, x384)
    del x384
    x386 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x386 += einsum("ijab,iakl->jklb", t2.abab, v.aabb.ovoo)
    x400 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x400 += einsum("ijka->jika", x386)
    del x386
    x387 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x387 -= einsum("ijka->ikja", v.bbbb.ooov)
    x387 += einsum("ijka->kija", v.bbbb.ooov)
    x388 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x388 += einsum("ijka,jlab->likb", x387, x61)
    del x387
    x400 += einsum("ijka->jika", x388)
    del x388
    x389 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x389 += einsum("ia,jbca->ijcb", t1.bb, v.bbbb.ovvv)
    x390 += einsum("ijab->ijab", x389)
    del x389
    x390 += einsum("iabj->jiba", v.bbbb.ovvo)
    x390 -= einsum("ijab->jiab", v.bbbb.oovv)
    x391 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x391 += einsum("ia,jkba->ijkb", t1.bb, x390)
    del x390
    x400 -= einsum("ijka->kija", x391)
    del x391
    x393 += einsum("ia->ia", f.bb.ov)
    x394 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x394 += einsum("ia,jkab->jkib", x393, t2.bbbb)
    x400 += einsum("ijka->kjia", x394)
    del x394
    x420 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x420 += einsum("ia,ja->ij", r1.bb, x393)
    del x393
    x422 += einsum("ij->ij", x420)
    del x420
    x423 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x423 += einsum("ij,jkab->kiab", x422, t2.bbbb)
    del x422
    x441 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x441 += einsum("ijab->jiba", x423)
    del x423
    x395 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x395 += einsum("ia,jakb->ikjb", t1.bb, v.bbbb.ovov)
    x396 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x396 += einsum("ia,jkla->jilk", t1.bb, x395)
    x398 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x398 += einsum("ijkl->lkji", x396)
    del x396
    x415 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x415 -= einsum("ijka->jkia", x395)
    del x395
    x397 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x397 += einsum("ia,jkla->ijlk", t1.bb, v.bbbb.ooov)
    x398 += einsum("ijkl->jkli", x397)
    x398 -= einsum("ijkl->kjli", x397)
    del x397
    x398 += einsum("ijkl->kilj", v.bbbb.oooo)
    x399 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x399 += einsum("ia,ijkl->jkla", t1.bb, x398)
    del x398
    x400 += einsum("ijka->ikja", x399)
    del x399
    x400 -= einsum("ijak->ijka", v.bbbb.oovo)
    x401 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x401 += einsum("ia,ijkb->jkab", r1.bb, x400)
    del x400
    x441 += einsum("ijab->ijab", x401)
    del x401
    x402 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x402 += einsum("ia,bcda->ibdc", t1.bb, v.bbbb.vvvv)
    x406 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x406 -= einsum("iabc->iabc", x402)
    del x402
    x403 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x403 += einsum("ijab,iacd->jbcd", t2.abab, v.aabb.ovvv)
    x406 += einsum("iabc->iabc", x403)
    del x403
    x404 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x404 += einsum("iabc->ibac", v.bbbb.ovvv)
    x404 -= einsum("iabc->ibca", v.bbbb.ovvv)
    x405 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x405 += einsum("iabc,ijcd->jdab", x404, x61)
    del x61
    x406 += einsum("iabc->iabc", x405)
    del x405
    x424 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x424 += einsum("ia,ibca->bc", r1.bb, x404)
    x425 -= einsum("ab->ab", x424)
    del x424
    x426 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x426 += einsum("ab,ijbc->ijca", x425, t2.bbbb)
    del x425
    x441 += einsum("ijab->jiab", x426)
    del x426
    x434 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x434 += einsum("ia,ibca->bc", t1.bb, x404)
    del x404
    x435 -= einsum("ab->ab", x434)
    del x434
    x436 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x436 += einsum("ia,ba->ib", t1.bb, x435)
    del x435
    x440 += einsum("ia->ia", x436)
    del x436
    x441 += einsum("ia,jb->ijab", r1.bb, x440)
    del x440
    x406 += einsum("aibc->iabc", v.bbbb.vovv)
    x407 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x407 += einsum("ia,jbca->ijbc", r1.bb, x406)
    del x406
    x441 -= einsum("ijab->ijab", x407)
    del x407
    x408 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x408 -= einsum("iabc->ibac", v.bbbb.ovvv)
    x408 += einsum("iabc->ibca", v.bbbb.ovvv)
    x409 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x409 += einsum("ia,jbca->ijbc", t1.bb, x408)
    del x408
    x410 -= einsum("ijab->ijab", x409)
    del x409
    x410 += einsum("iabj->jiba", v.bbbb.ovvo)
    x410 -= einsum("ijab->jiab", v.bbbb.oovv)
    x411 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x411 += einsum("ia,jkba->ijkb", r1.bb, x410)
    del x410
    x418 += einsum("ijka->ikja", x411)
    del x411
    x415 += einsum("ijka->ikja", v.bbbb.ooov)
    x416 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x416 += einsum("ia,jkla->ijkl", r1.bb, x415)
    del x415
    x417 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x417 += einsum("ia,jkil->jkla", t1.bb, x416)
    del x416
    x418 += einsum("ijka->ijka", x417)
    del x417
    x419 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x419 += einsum("ia,jikb->jkab", t1.bb, x418)
    del x418
    x441 -= einsum("ijab->ijab", x419)
    del x419
    x427 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x427 += einsum("ijka->ikja", v.bbbb.ooov)
    x427 -= einsum("ijka->kija", v.bbbb.ooov)
    x428 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x428 += einsum("ia,ijka->jk", r1.bb, x427)
    x429 -= einsum("ij->ij", x428)
    del x428
    x430 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x430 += einsum("ij,ikab->kjab", x429, t2.bbbb)
    del x429
    x441 -= einsum("ijab->ijba", x430)
    del x430
    ree2new_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    ree2new_bbbb += einsum("ijab->ijab", x441)
    ree2new_bbbb -= einsum("ijab->ijba", x441)
    ree2new_bbbb -= einsum("ijab->jiab", x441)
    ree2new_bbbb += einsum("ijab->jiba", x441)
    del x441
    x501 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x501 += einsum("ia,ijka->jk", t1.bb, x427)
    del x427
    x502 -= einsum("ij->ij", x501)
    del x501
    x442 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x442 += einsum("ijab,cadb->ijcd", r2.bbbb, v.bbbb.vvvv)
    x498 += einsum("ijab->ijab", x442) * 0.5
    del x442
    x443 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x443 += einsum("ijab,kbla->ijlk", r2.bbbb, v.bbbb.ovov)
    x444 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x444 += einsum("ijab,klji->klba", t2.bbbb, x443)
    x498 += einsum("ijab->ijab", x444) * 0.5
    del x444
    x482 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x482 += einsum("ia,jkli->jkla", t1.bb, x443)
    del x443
    x484 += einsum("ijka->ijka", x482)
    del x482
    x485 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x485 += einsum("ia,jkib->jkab", t1.bb, x484) * 0.5
    del x484
    x498 += einsum("ijab->ijab", x485)
    del x485
    x445 += einsum("iabj->jiba", v.bbbb.ovvo)
    x445 += einsum("ijab->jiab", v.bbbb.oovv) * -1
    x446 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x446 += einsum("ijab,jkbc->kica", x445, x57) * 0.5
    del x57
    del x445
    x498 += einsum("ijab->ijab", x446)
    del x446
    x448 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x448 += einsum("ijab,kalb->ijkl", t2.bbbb, v.bbbb.ovov)
    x449 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x449 += einsum("ijkl->lkji", x448)
    x487 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x487 += einsum("ia,jkil->kjla", t1.bb, x448)
    del x448
    x488 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x488 += einsum("ijka->ijka", x487) * -1
    del x487
    x449 += einsum("ijkl->kilj", v.bbbb.oooo)
    x450 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x450 += einsum("ijab,jikl->klab", r2.bbbb, x449) * 0.5
    del x449
    x498 += einsum("ijab->jiab", x450)
    del x450
    x471 = np.zeros((nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x471 += einsum("ijab,jcid->abdc", r2.bbbb, v.bbbb.ovov)
    x472 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x472 += einsum("ia,bcda->ibcd", t1.bb, x471)
    del x471
    x474 += einsum("iabc->iabc", x472)
    del x472
    x475 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x475 += einsum("ia,jbca->ijbc", t1.bb, x474) * 0.5
    del x474
    x498 += einsum("ijab->ijab", x475)
    del x475
    x477 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x477 += einsum("ijab,jkic->kbac", t2.bbbb, v.bbbb.ooov)
    x480 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x480 += einsum("iabc->iabc", x477)
    del x477
    x478 = np.zeros((nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x478 += einsum("ijab,icjd->abcd", t2.bbbb, v.bbbb.ovov)
    x479 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x479 += einsum("ia,bcad->icbd", t1.bb, x478)
    del x478
    x480 += einsum("iabc->iabc", x479) * -1
    del x479
    x481 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x481 += einsum("ia,jbca->ijbc", r1.bb, x480)
    del x480
    x498 += einsum("ijab->ijab", x481) * -1
    del x481
    x486 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x486 += einsum("ijab,kbca->jikc", t2.bbbb, v.bbbb.ovvv)
    x488 += einsum("ijka->ijka", x486)
    del x486
    x489 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x489 += einsum("ia,jkib->jkab", r1.bb, x488)
    del x488
    x498 += einsum("ijab->ijab", x489) * -1
    del x489
    ree2new_bbbb += einsum("ijab->ijab", x498)
    ree2new_bbbb += einsum("ijab->ijba", x498) * -1
    ree2new_bbbb += einsum("ijab->jiab", x498) * -1
    ree2new_bbbb += einsum("ijab->jiba", x498)
    del x498
    x499 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x499 += einsum("ab,ib->ia", f.bb.vv, t1.bb)
    x504 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x504 -= einsum("ia->ia", x499)
    del x499
    x500 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x500 += einsum("ia,ja->ij", f.bb.ov, t1.bb)
    x502 += einsum("ij->ij", x500)
    del x500
    x502 += einsum("ij->ij", f.bb.oo)
    x503 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x503 += einsum("ia,ij->ja", t1.bb, x502)
    del x502
    x504 += einsum("ia->ia", x503)
    del x503
    x504 -= einsum("ai->ia", f.bb.vo)
    ree2new_bbbb -= einsum("ia,jb->jiba", r1.bb, x504)
    ree2new_bbbb -= einsum("ia,jb->ijab", r1.bb, x504)
    ree2new_bbbb += einsum("ia,jb->ijba", r1.bb, x504)
    ree2new_bbbb += einsum("ia,jb->jiab", r1.bb, x504)
    del x504

    ree1new = Namespace(aa=ree1new_aa, bb=ree1new_bb)
    ree2new = Namespace(aaaa=ree2new_aaaa, abab=ree2new_abab, baba=ree2new_baba, bbbb=ree2new_bbbb)

    return ree1new, ree2new

