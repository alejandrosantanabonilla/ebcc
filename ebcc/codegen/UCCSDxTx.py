# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, direct_sum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 3), ())
    e_cc += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 3, 1, 2), ()) * -1.0
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
    x2 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x2 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x3 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(f.aa.ov, (0, 1), (0, 1))
    x3 += einsum(t1.aa, (0, 1), x2, (0, 2, 1, 3), (2, 3)) * -0.5
    e_cc += einsum(t1.aa, (0, 1), x3, (0, 1), ())

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    t1new = Namespace()
    t2new = Namespace()

    # T amplitudes
    t1new_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    t1new_bb += einsum(f.bb.ov, (0, 1), (0, 1))
    t1new_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    t1new_aa += einsum(f.aa.ov, (0, 1), (0, 1))
    t2new_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 2, 5, 3), (0, 1, 4, 5)) * 2.0
    t2new_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    t2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    t2new_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 2, 5, 3), (0, 1, 4, 5)) * 2.0
    x0 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x0 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(x0, (0, 1), (0, 1))
    x1 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x1 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x2 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x2 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x2 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_bb += einsum(t2.bbbb, (0, 1, 2, 3), x2, (4, 0, 1, 3), (4, 2)) * 2.0
    x3 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (0, 4, 2, 3))
    x4 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x4 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x4 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3))
    t1new_bb += einsum(t2.abab, (0, 1, 2, 3), x4, (1, 4, 0, 2), (4, 3)) * -1.0
    x5 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x5 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x5 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3)) * 0.5
    t1new_bb += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x5, (0, 4, 3, 1), (4, 2)) * -2.0
    x6 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x6 += einsum(t2.abab, (0, 1, 2, 3), (1, 3, 0, 2))
    x6 += einsum(t1.aa, (0, 1), t1.bb, (2, 3), (2, 3, 0, 1))
    t1new_bb += einsum(v.aabb.ovvv, (0, 1, 2, 3), x6, (4, 3, 0, 1), (4, 2))
    t1new_aa += einsum(v.aabb.vvov, (0, 1, 2, 3), x6, (2, 3, 4, 1), (4, 0))
    x7 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x8 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x8 += einsum(t1.bb, (0, 1), x7, (0, 2, 1, 3), (2, 3))
    x9 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x9 += einsum(f.bb.ov, (0, 1), (0, 1))
    x9 += einsum(x0, (0, 1), (0, 1))
    x9 += einsum(x8, (0, 1), (0, 1)) * -1.0
    t1new_bb += einsum(x9, (0, 1), t2.bbbb, (2, 0, 3, 1), (2, 3)) * 2.0
    t1new_aa += einsum(x9, (0, 1), t2.abab, (2, 0, 3, 1), (2, 3))
    x10 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x10 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    t1new_aa += einsum(x10, (0, 1), (0, 1))
    x11 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x11 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x11 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x12 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x12 += einsum(t1.aa, (0, 1), x11, (0, 2, 1, 3), (2, 3))
    x13 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(f.aa.ov, (0, 1), (0, 1))
    x13 += einsum(x10, (0, 1), (0, 1))
    x13 += einsum(x12, (0, 1), (0, 1)) * -1.0
    t1new_bb += einsum(x13, (0, 1), t2.abab, (0, 2, 1, 3), (2, 3))
    t1new_aa += einsum(x13, (0, 1), t2.aaaa, (2, 0, 3, 1), (2, 3)) * 2.0
    x14 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x14 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x14 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new_bb += einsum(t1.bb, (0, 1), x14, (0, 2, 1, 3), (2, 3)) * -1.0
    x15 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x15 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (0, 1, 2, 3), (2, 3))
    x16 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x16 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x17 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x17 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 3), (1, 4))
    x18 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x18 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x18 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x19 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x19 += einsum(t1.bb, (0, 1), x18, (2, 3, 0, 1), (2, 3))
    x20 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x20 += einsum(t1.bb, (0, 1), x9, (2, 1), (0, 2))
    x21 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x21 += einsum(f.bb.oo, (0, 1), (0, 1))
    x21 += einsum(x15, (0, 1), (1, 0))
    x21 += einsum(x16, (0, 1), (1, 0)) * 2.0
    x21 += einsum(x17, (0, 1), (1, 0))
    x21 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x21 += einsum(x20, (0, 1), (1, 0))
    t1new_bb += einsum(t1.bb, (0, 1), x21, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x21, (0, 1), t2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    x22 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x22 += einsum(f.bb.vv, (0, 1), (0, 1))
    x22 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(t1.bb, (0, 1), x22, (1, 2), (0, 2))
    x23 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x23 += einsum(t1.aa, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (3, 4, 0, 2))
    x24 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x24 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x24 += einsum(x23, (0, 1, 2, 3), (0, 1, 3, 2))
    t1new_aa += einsum(t2.abab, (0, 1, 2, 3), x24, (1, 3, 0, 4), (4, 2)) * -1.0
    x25 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x25 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x26 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x26 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x26 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_aa += einsum(t2.aaaa, (0, 1, 2, 3), x26, (4, 1, 0, 3), (4, 2)) * -2.0
    x27 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x27 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x27 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3)) * 0.5
    t1new_aa += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x27, (0, 4, 1, 3), (4, 2)) * 2.0
    x28 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x28 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x28 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new_aa += einsum(t1.aa, (0, 1), x28, (0, 2, 1, 3), (2, 3)) * -1.0
    x29 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x29 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 1), (2, 3))
    x30 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x30 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 3), (0, 4))
    x31 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x31 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x32 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x32 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x32 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x33 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x33 += einsum(t1.aa, (0, 1), x32, (2, 3, 0, 1), (2, 3))
    x34 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x34 += einsum(t1.aa, (0, 1), x13, (2, 1), (0, 2))
    x35 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x35 += einsum(f.aa.oo, (0, 1), (0, 1))
    x35 += einsum(x29, (0, 1), (1, 0))
    x35 += einsum(x30, (0, 1), (1, 0))
    x35 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x35 += einsum(x33, (0, 1), (1, 0)) * -1.0
    x35 += einsum(x34, (0, 1), (1, 0))
    t1new_aa += einsum(t1.aa, (0, 1), x35, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x35, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x36 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x36 += einsum(f.aa.vv, (0, 1), (0, 1))
    x36 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (0, 2, 3, 1), (2, 3)) * -1.0
    t1new_aa += einsum(t1.aa, (0, 1), x36, (1, 2), (0, 2))
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
    x41 += einsum(x28, (0, 1, 2, 3), x40, (0, 4, 2, 5), (1, 4, 3, 5)) * 2.0
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
    x52 += einsum(t2.abab, (0, 1, 2, 3), x23, (1, 3, 4, 5), (4, 0, 5, 2))
    x53 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x53 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x54 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(t2.aaaa, (0, 1, 2, 3), x53, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x55 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x55 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x55 += einsum(x25, (0, 1, 2, 3), (0, 2, 1, 3))
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
    x61 += einsum(t2.aaaa, (0, 1, 2, 3), x49, (4, 5, 0, 1), (4, 5, 2, 3))
    x62 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x62 += einsum(f.aa.oo, (0, 1), (0, 1))
    x62 += einsum(x34, (0, 1), (0, 1))
    x63 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum(x62, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x64 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x64 += einsum(x29, (0, 1), (1, 0))
    x64 += einsum(x30, (0, 1), (1, 0))
    x64 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x64 += einsum(x33, (0, 1), (1, 0)) * -1.0
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
    x69 += einsum(t2.aaaa, (0, 1, 2, 3), x11, (1, 4, 3, 5), (4, 0, 5, 2))
    x70 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum(t2.aaaa, (0, 1, 2, 3), x69, (1, 4, 3, 5), (0, 4, 2, 5)) * -4.0
    x71 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 1), (2, 3))
    x72 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x72 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x73 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x73 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 4, 1, 3), (2, 4))
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
    x78 += einsum(x13, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4)) * -2.0
    x79 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x79 += einsum(t1.aa, (0, 1), x25, (2, 3, 4, 1), (2, 0, 4, 3))
    x80 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x80 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x80 += einsum(x79, (0, 1, 2, 3), (3, 1, 2, 0))
    x81 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x81 += einsum(t1.aa, (0, 1), x80, (0, 2, 3, 4), (2, 3, 4, 1))
    x82 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x82 += einsum(x77, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x82 += einsum(x78, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x82 += einsum(x81, (0, 1, 2, 3), (1, 0, 2, 3))
    x83 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x83 += einsum(t1.aa, (0, 1), x82, (0, 2, 3, 4), (2, 3, 1, 4))
    x84 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x84 += einsum(x68, (0, 1, 2, 3), (0, 1, 2, 3))
    x84 += einsum(x70, (0, 1, 2, 3), (1, 0, 3, 2))
    x84 += einsum(x76, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x84 += einsum(x83, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x84, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x85 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x85 += einsum(f.aa.vv, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4))
    x86 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x86 += einsum(t2.abab, (0, 1, 2, 3), x7, (1, 4, 3, 5), (4, 5, 0, 2))
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
    x90 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x90 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x89, (4, 5, 3, 1), (0, 5, 2, 4))
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), x90, (0, 4, 1, 5), (4, 5, 2, 3)) * 2.0
    x91 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x91 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x92 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x92 += einsum(t1.aa, (0, 1), x91, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    x92 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x92 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    t2new_aaaa += einsum(t1.aa, (0, 1), x92, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x93 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x93 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x93 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x94 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x94 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x94 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x94 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (4, 0, 5, 2)) * 0.5
    x94 += einsum(x40, (0, 1, 2, 3), x93, (0, 4, 5, 2), (4, 1, 5, 3)) * -1.0
    x94 += einsum(t1.aa, (0, 1), x45, (2, 1, 3, 4), (2, 0, 4, 3)) * -0.5
    x94 += einsum(t1.aa, (0, 1), x32, (2, 3, 0, 4), (3, 2, 4, 1)) * -0.5
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x94, (0, 4, 2, 5), (4, 1, 5, 3)) * 2.0
    x95 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x95 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x95 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -0.5
    x96 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x96 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x96 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x97 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x97 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x97 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x98 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x98 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x98 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x98 += einsum(x7, (0, 1, 2, 3), x95, (0, 4, 3, 5), (1, 4, 2, 5)) * -2.0
    x98 += einsum(t1.bb, (0, 1), x96, (2, 1, 3, 4), (2, 0, 4, 3)) * -1.0
    x98 += einsum(t1.bb, (0, 1), x97, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x98, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x99 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x99 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x100 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x100 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x100 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 4), (4, 1, 2, 3))
    x100 += einsum(x99, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x100 += einsum(v.aabb.ovov, (0, 1, 2, 3), x6, (2, 4, 5, 1), (3, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x100, (3, 4, 0, 5), (5, 1, 2, 4))
    x101 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x101 += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x102 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x102 += einsum(t1.bb, (0, 1), v.aabb.ovoo, (2, 3, 4, 0), (4, 1, 2, 3)) * -1.0
    x102 += einsum(x101, (0, 1, 2, 3), (0, 1, 2, 3))
    x102 += einsum(v.aabb.ovov, (0, 1, 2, 3), x95, (2, 4, 3, 5), (4, 5, 0, 1)) * 2.0
    t2new_abab += einsum(t2.aaaa, (0, 1, 2, 3), x102, (4, 5, 1, 3), (0, 4, 2, 5)) * 2.0
    x103 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x103 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x103 += einsum(t1.aa, (0, 1), x24, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    t2new_abab += einsum(x103, (0, 1, 2, 3), x95, (0, 4, 1, 5), (2, 4, 3, 5)) * 2.0
    x104 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x104 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x104 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    x105 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x105 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x105 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 4, 1), (4, 0, 2, 3))
    x105 += einsum(t1.aa, (0, 1), x104, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x105, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x106 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x106 += einsum(v.aabb.vvvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x106 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 4), (4, 1, 2, 3))
    x106 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 2, 3, 4), (3, 4, 2, 1))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x106, (3, 4, 2, 5), (0, 1, 5, 4)) * -1.0
    x107 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x107 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x108 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x108 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x108 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 4, 1), (4, 0, 2, 3))
    x108 += einsum(x107, (0, 1, 2, 3), (1, 0, 3, 2))
    x108 += einsum(v.aabb.ovov, (0, 1, 2, 3), x6, (4, 3, 5, 1), (2, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x108, (1, 4, 0, 5), (5, 4, 2, 3))
    x109 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x109 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 1, 2, 3), (2, 3))
    x110 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x110 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x111 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x111 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x112 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x112 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x112 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x113 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(t1.bb, (0, 1), x112, (0, 2, 1, 3), (2, 3))
    x114 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x114 += einsum(f.bb.vv, (0, 1), (0, 1)) * -1.0
    x114 += einsum(x109, (0, 1), (1, 0)) * -1.0
    x114 += einsum(x110, (0, 1), (1, 0)) * 2.0
    x114 += einsum(x111, (0, 1), (1, 0))
    x114 += einsum(x113, (0, 1), (0, 1)) * -1.0
    x114 += einsum(t1.bb, (0, 1), x9, (0, 2), (2, 1))
    t2new_abab += einsum(x114, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    x115 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x115 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x115 += einsum(x71, (0, 1), (1, 0)) * -1.0
    x115 += einsum(x72, (0, 1), (1, 0))
    x115 += einsum(x73, (0, 1), (1, 0)) * 2.0
    x115 += einsum(x74, (0, 1), (1, 0)) * -1.0
    x115 += einsum(t1.aa, (0, 1), x13, (0, 2), (2, 1))
    t2new_abab += einsum(x115, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x116 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x116 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x116 += einsum(x99, (0, 1, 2, 3), (1, 0, 2, 3))
    x117 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x117 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x117 += einsum(x107, (0, 1, 2, 3), (1, 0, 2, 3))
    x117 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (5, 1, 0, 4))
    x118 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x118 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x118 += einsum(x23, (0, 1, 2, 3), (0, 1, 3, 2))
    x118 += einsum(t1.bb, (0, 1), x116, (1, 2, 3, 4), (0, 2, 4, 3))
    x118 += einsum(t1.bb, (0, 1), x117, (0, 2, 3, 4), (2, 1, 4, 3)) * -1.0
    t2new_abab += einsum(t1.aa, (0, 1), x118, (2, 3, 0, 4), (4, 2, 1, 3)) * -1.0
    x119 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x119 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x119 += einsum(t1.aa, (0, 1), v.aabb.vvvv, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(t1.bb, (0, 1), x119, (1, 2, 3, 4), (3, 0, 4, 2))
    x120 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x120 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x120 += einsum(t1.aa, (0, 1), v.aabb.vvoo, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(t1.bb, (0, 1), x120, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    x121 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x121 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x122 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x122 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x123 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x123 += einsum(t2.abab, (0, 1, 2, 3), x101, (4, 5, 0, 2), (4, 1, 3, 5))
    x124 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x124 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x124 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x124 += einsum(x122, (0, 1, 2, 3), (1, 0, 3, 2))
    x125 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x125 += einsum(t2.bbbb, (0, 1, 2, 3), x124, (1, 4, 3, 5), (0, 4, 2, 5)) * 2.0
    x126 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x126 += einsum(t1.bb, (0, 1), x112, (2, 3, 1, 4), (0, 2, 3, 4))
    x127 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x127 += einsum(t2.bbbb, (0, 1, 2, 3), x126, (4, 1, 3, 5), (0, 4, 2, 5)) * -2.0
    x128 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x128 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x129 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x129 += einsum(t1.bb, (0, 1), x128, (2, 3, 4, 0), (2, 4, 3, 1))
    x130 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x130 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovoo, (0, 2, 4, 5), (1, 4, 5, 3))
    x131 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x131 += einsum(t2.abab, (0, 1, 2, 3), x3, (4, 5, 0, 2), (4, 1, 5, 3))
    x132 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x132 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x132 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x133 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x133 += einsum(t2.bbbb, (0, 1, 2, 3), x132, (1, 4, 5, 3), (0, 4, 5, 2)) * 2.0
    x134 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x134 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3))
    x134 += einsum(x1, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x135 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x135 += einsum(t2.bbbb, (0, 1, 2, 3), x134, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x136 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x136 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x136 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x136 += einsum(x121, (0, 1, 2, 3), (0, 1, 2, 3))
    x137 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x137 += einsum(t1.bb, (0, 1), x136, (2, 3, 1, 4), (0, 2, 3, 4))
    x138 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x138 += einsum(x129, (0, 1, 2, 3), (0, 2, 1, 3))
    x138 += einsum(x130, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x138 += einsum(x131, (0, 1, 2, 3), (0, 2, 1, 3))
    x138 += einsum(x133, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x138 += einsum(x135, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x138 += einsum(x137, (0, 1, 2, 3), (0, 2, 1, 3))
    x139 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x139 += einsum(t1.bb, (0, 1), x138, (2, 0, 3, 4), (2, 3, 1, 4))
    x140 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x140 += einsum(x121, (0, 1, 2, 3), (0, 1, 2, 3))
    x140 += einsum(x122, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x140 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3))
    x140 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x140 += einsum(x127, (0, 1, 2, 3), (1, 0, 2, 3))
    x140 += einsum(x139, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x140, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x140, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x140, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x141 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x141 += einsum(t1.bb, (0, 1), v.bbbb.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x142 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x142 += einsum(t1.bb, (0, 1), x141, (2, 3, 1, 4), (0, 2, 3, 4))
    x143 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x143 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x143 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x144 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x144 += einsum(t2.bbbb, (0, 1, 2, 3), x143, (1, 4, 5, 3), (0, 4, 2, 5))
    x145 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x145 += einsum(t2.bbbb, (0, 1, 2, 3), x144, (4, 1, 5, 3), (0, 4, 2, 5)) * -4.0
    x146 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x146 += einsum(t2.abab, (0, 1, 2, 3), x11, (0, 4, 2, 5), (1, 3, 4, 5))
    x147 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x147 += einsum(t2.abab, (0, 1, 2, 3), x146, (4, 5, 0, 2), (1, 4, 3, 5)) * -1.0
    x148 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x148 += einsum(x109, (0, 1), (1, 0)) * -1.0
    x148 += einsum(x110, (0, 1), (1, 0)) * 2.0
    x148 += einsum(x111, (0, 1), (1, 0))
    x148 += einsum(x113, (0, 1), (0, 1)) * -1.0
    x149 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x149 += einsum(x148, (0, 1), t2.bbbb, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x150 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x150 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x151 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x151 += einsum(x9, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4)) * -2.0
    x152 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x152 += einsum(t1.bb, (0, 1), x1, (2, 3, 4, 1), (2, 0, 4, 3))
    x153 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x153 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x153 += einsum(x152, (0, 1, 2, 3), (3, 1, 2, 0))
    x154 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x154 += einsum(t1.bb, (0, 1), x153, (0, 2, 3, 4), (2, 3, 4, 1))
    x155 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x155 += einsum(x150, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x155 += einsum(x151, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x155 += einsum(x154, (0, 1, 2, 3), (1, 0, 2, 3))
    x156 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x156 += einsum(t1.bb, (0, 1), x155, (0, 2, 3, 4), (2, 3, 1, 4))
    x157 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x157 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    x157 += einsum(x145, (0, 1, 2, 3), (1, 0, 3, 2))
    x157 += einsum(x147, (0, 1, 2, 3), (1, 0, 3, 2))
    x157 += einsum(x149, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x157 += einsum(x156, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x157, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x158 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x158 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x159 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x159 += einsum(t2.bbbb, (0, 1, 2, 3), x128, (4, 5, 0, 1), (4, 5, 2, 3))
    x160 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x160 += einsum(f.bb.oo, (0, 1), (0, 1))
    x160 += einsum(x20, (0, 1), (0, 1))
    x161 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x161 += einsum(x160, (0, 1), t2.bbbb, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x162 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x162 += einsum(x15, (0, 1), (1, 0))
    x162 += einsum(x16, (0, 1), (1, 0)) * 2.0
    x162 += einsum(x17, (0, 1), (1, 0))
    x162 += einsum(x19, (0, 1), (1, 0)) * -1.0
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
    x167 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x168 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x168 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x168 += einsum(x167, (0, 1, 2, 3), (3, 1, 0, 2))
    x168 += einsum(x152, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), x168, (0, 4, 5, 1), (5, 4, 2, 3)) * -2.0
    x169 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x169 += einsum(t1.bb, (0, 1), x167, (2, 3, 0, 4), (2, 3, 4, 1)) * -2.0
    x169 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x169 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    t2new_bbbb += einsum(t1.bb, (0, 1), x169, (2, 3, 0, 4), (2, 3, 1, 4))

    t1new.aa = t1new_aa
    t1new.bb = t1new_bb
    t2new.aaaa = t2new_aaaa
    t2new.abab = t2new_abab
    t2new.bbbb = t2new_bbbb

    return {"t1new": t1new, "t2new": t2new}

def energy_perturbative(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    denom3 = Namespace()
    denom3.aaaaaa = 1 / direct_sum(
            "ia+jb+kc->ijkabc",
            direct_sum("i-a->ia", np.diag(f.aa.oo), np.diag(f.aa.vv)),
            direct_sum("i-a->ia", np.diag(f.aa.oo), np.diag(f.aa.vv)),
            direct_sum("i-a->ia", np.diag(f.aa.oo), np.diag(f.aa.vv)),
    )
    denom3.babbab = 1 / direct_sum(
            "ia+jb+kc->ijkabc",
            direct_sum("i-a->ia", np.diag(f.bb.oo), np.diag(f.bb.vv)),
            direct_sum("i-a->ia", np.diag(f.aa.oo), np.diag(f.aa.vv)),
            direct_sum("i-a->ia", np.diag(f.bb.oo), np.diag(f.bb.vv)),
    )
    denom3.abaaba = 1 / direct_sum(
            "ia+jb+kc->ijkabc",
            direct_sum("i-a->ia", np.diag(f.aa.oo), np.diag(f.aa.vv)),
            direct_sum("i-a->ia", np.diag(f.bb.oo), np.diag(f.bb.vv)),
            direct_sum("i-a->ia", np.diag(f.aa.oo), np.diag(f.aa.vv)),
    )
    denom3.bbbbbb = 1 / direct_sum(
            "ia+jb+kc->ijkabc",
            direct_sum("i-a->ia", np.diag(f.bb.oo), np.diag(f.bb.vv)),
            direct_sum("i-a->ia", np.diag(f.bb.oo), np.diag(f.bb.vv)),
            direct_sum("i-a->ia", np.diag(f.bb.oo), np.diag(f.bb.vv)),
    )

    # energy
    e_pert = 0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (4, 3, 5, 6), denom3.babbab, (4, 1, 5, 3, 0, 6), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (4, 6, 5, 3), denom3.babbab, (4, 1, 5, 6, 0, 3), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (5, 3, 4, 6), denom3.babbab, (5, 1, 4, 3, 0, 6), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (5, 6, 4, 3), denom3.babbab, (5, 1, 4, 6, 0, 3), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aabb.ooov, (1, 2, 5, 6), v.bbbb.ovov, (3, 4, 5, 6), denom3.babbab, (3, 1, 5, 4, 0, 6), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aabb.ooov, (1, 2, 5, 6), v.bbbb.ovov, (3, 6, 5, 4), denom3.babbab, (3, 1, 5, 6, 0, 4), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aabb.ooov, (1, 2, 5, 6), v.bbbb.ovov, (5, 4, 3, 6), denom3.babbab, (5, 1, 3, 4, 0, 6), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 4, 5), v.aaaa.ooov, (1, 2, 6, 0), v.aabb.ovov, (6, 4, 3, 5), denom3.abaaba, (1, 3, 6, 0, 5, 4), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aaaa.ooov, (1, 2, 5, 6), v.aabb.ovov, (5, 6, 3, 4), denom3.abaaba, (1, 3, 5, 0, 4, 6), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aabb.ooov, (1, 2, 5, 6), v.bbbb.ovov, (5, 6, 3, 4), denom3.babbab, (5, 1, 3, 6, 0, 4), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 4, 5), v.aaaa.ooov, (6, 2, 1, 0), v.aabb.ovov, (6, 4, 3, 5), denom3.abaaba, (1, 3, 6, 0, 5, 4), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aaaa.ooov, (5, 2, 1, 6), v.aabb.ovov, (5, 6, 3, 4), denom3.abaaba, (1, 3, 5, 0, 4, 6), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.aabb.ovoo, (5, 0, 6, 2), v.aabb.ovov, (5, 3, 6, 4), denom3.abaaba, (1, 6, 5, 0, 4, 3), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.aabb.ovoo, (4, 5, 6, 2), v.aabb.ovov, (4, 5, 6, 3), denom3.abaaba, (1, 6, 4, 0, 3, 5), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovoo, (1, 0, 6, 3), v.aabb.ovov, (2, 4, 6, 5), denom3.abaaba, (1, 6, 2, 0, 5, 4), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aabb.ovoo, (1, 5, 6, 3), v.aabb.ovov, (2, 5, 6, 4), denom3.abaaba, (1, 6, 2, 0, 4, 5), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ovov, (2, 4, 5, 6), v.bbbb.ovvv, (5, 4, 6, 3), denom3.babbab, (2, 1, 5, 4, 0, 6), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ovov, (2, 4, 5, 6), v.bbbb.ovvv, (5, 6, 4, 3), denom3.babbab, (2, 1, 5, 4, 0, 6), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.aabb.ovov, (5, 3, 2, 6), v.aabb.ovvv, (5, 0, 6, 4), denom3.abaaba, (1, 2, 5, 0, 6, 3), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.aabb.ovov, (4, 5, 2, 6), v.aabb.ovvv, (4, 5, 6, 3), denom3.abaaba, (1, 2, 4, 0, 6, 5), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ovov, (4, 5, 2, 6), v.bbbb.ovvv, (4, 5, 6, 3), denom3.babbab, (4, 1, 2, 5, 0, 6), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), v.bbbb.ovov, (4, 5, 2, 6), v.bbbb.ovvv, (4, 6, 5, 3), denom3.babbab, (4, 1, 2, 5, 0, 6), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.aabb.ovov, (5, 6, 2, 4), v.aaaa.ovvv, (5, 0, 6, 3), denom3.abaaba, (1, 2, 5, 0, 4, 6), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.aabb.ovov, (5, 6, 2, 4), v.aaaa.ovvv, (5, 6, 0, 3), denom3.abaaba, (1, 2, 5, 0, 4, 6), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovov, (2, 4, 3, 6), v.aabb.ovvv, (1, 0, 6, 5), denom3.abaaba, (1, 3, 2, 0, 6, 4), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), v.aabb.ovov, (2, 5, 3, 6), v.aabb.ovvv, (1, 5, 6, 4), denom3.abaaba, (1, 3, 2, 0, 6, 5), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovov, (2, 6, 3, 5), v.aaaa.ovvv, (1, 0, 6, 4), denom3.abaaba, (1, 3, 2, 0, 5, 6), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovov, (2, 6, 3, 5), v.aaaa.ovvv, (1, 6, 0, 4), denom3.abaaba, (1, 3, 2, 0, 5, 6), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.bbbb.ovov, (2, 4, 5, 6), v.aabb.vvov, (0, 3, 5, 6), denom3.babbab, (2, 1, 5, 4, 0, 6), ())
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.bbbb.ovov, (2, 5, 6, 4), v.aabb.vvov, (0, 3, 6, 5), denom3.babbab, (2, 1, 6, 5, 0, 4), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.bbbb.ovov, (5, 4, 2, 6), v.aabb.vvov, (0, 3, 5, 6), denom3.babbab, (5, 1, 2, 4, 0, 6), ()) * -1.0
    e_pert += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), v.bbbb.ovov, (5, 6, 2, 4), v.aabb.vvov, (0, 3, 5, 6), denom3.babbab, (5, 1, 2, 6, 0, 4), ())
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (4, 3, 5, 6), denom3.aaaaaa, (1, 4, 5, 0, 3, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aabb.ooov, (4, 2, 5, 6), v.aabb.ovov, (4, 3, 5, 6), denom3.abaaba, (1, 5, 4, 0, 6, 3), ()) * -4.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ooov, (5, 2, 6, 0), v.aaaa.ovov, (5, 3, 6, 4), denom3.aaaaaa, (1, 5, 6, 0, 3, 4), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (4, 6, 5, 3), denom3.aaaaaa, (1, 4, 5, 0, 6, 3), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (5, 3, 4, 6), denom3.aaaaaa, (1, 5, 4, 0, 3, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ooov, (5, 2, 6, 0), v.aaaa.ovov, (6, 3, 5, 4), denom3.aaaaaa, (1, 6, 5, 0, 3, 4), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (5, 6, 4, 3), denom3.aaaaaa, (1, 5, 4, 0, 6, 3), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (1, 3, 5, 6), v.aaaa.ovov, (2, 4, 5, 6), denom3.aaaaaa, (1, 2, 5, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aabb.ooov, (1, 3, 5, 6), v.aabb.ovov, (2, 4, 5, 6), denom3.abaaba, (1, 5, 2, 0, 6, 4), ()) * 4.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ooov, (1, 3, 6, 0), v.aaaa.ovov, (2, 4, 6, 5), denom3.aaaaaa, (1, 2, 6, 0, 4, 5), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (1, 3, 5, 6), v.aaaa.ovov, (2, 6, 5, 4), denom3.aaaaaa, (1, 2, 5, 0, 6, 4), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (1, 3, 5, 6), v.aaaa.ovov, (5, 4, 2, 6), denom3.aaaaaa, (1, 5, 2, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ooov, (1, 3, 6, 0), v.aaaa.ovov, (6, 4, 2, 5), denom3.aaaaaa, (1, 6, 2, 0, 4, 5), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (1, 3, 5, 6), v.aaaa.ovov, (5, 6, 2, 4), denom3.aaaaaa, (1, 5, 2, 0, 6, 4), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (5, 3, 1, 6), v.aaaa.ovov, (2, 4, 5, 6), denom3.aaaaaa, (1, 2, 5, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ooov, (6, 3, 1, 0), v.aaaa.ovov, (2, 4, 6, 5), denom3.aaaaaa, (1, 2, 6, 0, 4, 5), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (5, 3, 1, 6), v.aaaa.ovov, (2, 6, 5, 4), denom3.aaaaaa, (1, 2, 5, 0, 6, 4), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (5, 3, 1, 6), v.aaaa.ovov, (5, 4, 2, 6), denom3.aaaaaa, (1, 5, 2, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ooov, (6, 3, 1, 0), v.aaaa.ovov, (6, 4, 2, 5), denom3.aaaaaa, (1, 6, 2, 0, 4, 5), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ooov, (5, 3, 1, 6), v.aaaa.ovov, (5, 6, 2, 4), denom3.aaaaaa, (1, 5, 2, 0, 6, 4), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.bbbb, (2, 3, 4, 5), v.aabb.ovoo, (1, 0, 6, 3), v.bbbb.ovov, (2, 4, 6, 5), denom3.babbab, (2, 1, 6, 4, 0, 5), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.bbbb, (2, 3, 4, 5), v.aabb.ovoo, (1, 0, 6, 3), v.bbbb.ovov, (6, 4, 2, 5), denom3.babbab, (6, 1, 2, 4, 0, 5), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (2, 3, 5, 6), v.aaaa.ovvv, (5, 0, 6, 4), denom3.aaaaaa, (1, 2, 5, 0, 3, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (2, 3, 5, 6), v.aaaa.ovvv, (5, 6, 0, 4), denom3.aaaaaa, (1, 2, 5, 0, 3, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ovov, (2, 4, 5, 6), v.aaaa.ovvv, (5, 4, 6, 3), denom3.aaaaaa, (1, 2, 5, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ovov, (2, 4, 5, 6), v.aaaa.ovvv, (5, 6, 4, 3), denom3.aaaaaa, (1, 2, 5, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (2, 5, 6, 3), v.aaaa.ovvv, (6, 0, 5, 4), denom3.aaaaaa, (1, 2, 6, 0, 5, 3), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (2, 5, 6, 3), v.aaaa.ovvv, (6, 5, 0, 4), denom3.aaaaaa, (1, 2, 6, 0, 5, 3), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (5, 3, 2, 6), v.aaaa.ovvv, (5, 0, 6, 4), denom3.aaaaaa, (1, 5, 2, 0, 3, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (5, 3, 2, 6), v.aaaa.ovvv, (5, 6, 0, 4), denom3.aaaaaa, (1, 5, 2, 0, 3, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ovov, (4, 5, 2, 6), v.aaaa.ovvv, (4, 5, 6, 3), denom3.aaaaaa, (1, 4, 2, 0, 5, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aaaa.ovov, (4, 5, 2, 6), v.aaaa.ovvv, (4, 6, 5, 3), denom3.aaaaaa, (1, 4, 2, 0, 5, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (5, 6, 2, 3), v.aaaa.ovvv, (5, 0, 6, 4), denom3.aaaaaa, (1, 5, 2, 0, 6, 3), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aaaa.ovov, (5, 6, 2, 3), v.aaaa.ovvv, (5, 6, 0, 4), denom3.aaaaaa, (1, 5, 2, 0, 6, 3), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovov, (2, 4, 3, 6), v.aaaa.ovvv, (1, 0, 6, 5), denom3.aaaaaa, (1, 2, 3, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovov, (2, 4, 3, 6), v.aabb.ovvv, (1, 0, 6, 5), denom3.babbab, (2, 1, 3, 4, 0, 6), ()) * 2.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovov, (2, 4, 3, 6), v.aaaa.ovvv, (1, 6, 0, 5), denom3.aaaaaa, (1, 2, 3, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ovov, (2, 5, 3, 6), v.aaaa.ovvv, (1, 5, 6, 4), denom3.aaaaaa, (1, 2, 3, 0, 5, 6), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 0, 4), v.aaaa.ovov, (2, 5, 3, 6), v.aaaa.ovvv, (1, 6, 5, 4), denom3.aaaaaa, (1, 2, 3, 0, 5, 6), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovov, (2, 6, 3, 4), v.aaaa.ovvv, (1, 0, 6, 5), denom3.aaaaaa, (1, 2, 3, 0, 6, 4), ()) * -6.0
    e_pert += einsum(l1.aa, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovov, (2, 6, 3, 4), v.aabb.ovvv, (1, 0, 6, 5), denom3.babbab, (2, 1, 3, 6, 0, 4), ()) * -2.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovov, (2, 6, 3, 4), v.aaaa.ovvv, (1, 6, 0, 5), denom3.aaaaaa, (1, 2, 3, 0, 6, 4), ()) * 6.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 3, 4), v.aabb.ovov, (2, 3, 5, 6), v.aabb.vvov, (0, 4, 5, 6), denom3.abaaba, (1, 5, 2, 0, 6, 3), ()) * -4.0
    e_pert += einsum(l1.aa, (0, 1), t2.aaaa, (1, 2, 0, 3), v.aabb.ovov, (2, 4, 5, 6), v.aabb.vvov, (4, 3, 5, 6), denom3.abaaba, (1, 5, 2, 0, 6, 4), ()) * 4.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.bbbb.ooov, (1, 3, 5, 6), v.aabb.ovov, (2, 4, 5, 6), denom3.babbab, (1, 2, 5, 0, 4, 6), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 5), v.bbbb.ooov, (1, 3, 6, 0), v.aabb.ovov, (2, 4, 6, 5), denom3.babbab, (1, 2, 6, 0, 4, 5), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aabb.ooov, (4, 2, 5, 6), v.aabb.ovov, (4, 3, 5, 6), denom3.babbab, (1, 4, 5, 0, 3, 6), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aabb.ooov, (5, 2, 6, 0), v.aabb.ovov, (5, 3, 6, 4), denom3.babbab, (1, 5, 6, 0, 3, 4), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (4, 3, 5, 6), denom3.abaaba, (4, 1, 5, 3, 0, 6), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (4, 6, 5, 3), denom3.abaaba, (4, 1, 5, 6, 0, 3), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (5, 3, 4, 6), denom3.abaaba, (5, 1, 4, 3, 0, 6), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ooov, (4, 2, 5, 6), v.aaaa.ovov, (5, 6, 4, 3), denom3.abaaba, (5, 1, 4, 6, 0, 3), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.bbbb.ooov, (5, 3, 1, 6), v.aabb.ovov, (2, 4, 5, 6), denom3.babbab, (1, 2, 5, 0, 4, 6), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 5), v.bbbb.ooov, (6, 3, 1, 0), v.aabb.ovov, (2, 4, 6, 5), denom3.babbab, (1, 2, 6, 0, 4, 5), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.aabb.ooov, (5, 2, 1, 6), v.aabb.ovov, (5, 4, 3, 6), denom3.babbab, (1, 5, 3, 0, 4, 6), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ooov, (6, 2, 1, 0), v.aabb.ovov, (6, 4, 3, 5), denom3.babbab, (1, 6, 3, 0, 4, 5), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.aabb.ovoo, (5, 6, 1, 3), v.aaaa.ovov, (2, 4, 5, 6), denom3.abaaba, (2, 1, 5, 4, 0, 6), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.aabb.ovoo, (5, 6, 1, 3), v.aaaa.ovov, (2, 6, 5, 4), denom3.abaaba, (2, 1, 5, 6, 0, 4), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.aabb.ovoo, (5, 6, 1, 3), v.aaaa.ovov, (5, 4, 2, 6), denom3.abaaba, (5, 1, 2, 4, 0, 6), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.aabb.ovoo, (5, 6, 1, 3), v.aaaa.ovov, (5, 6, 2, 4), denom3.abaaba, (5, 1, 2, 6, 0, 4), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovov, (2, 4, 3, 6), v.bbbb.ovvv, (1, 0, 6, 5), denom3.babbab, (1, 2, 3, 0, 4, 6), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovov, (2, 4, 3, 6), v.bbbb.ovvv, (1, 6, 0, 5), denom3.babbab, (1, 2, 3, 0, 4, 6), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aabb.ovov, (2, 3, 5, 6), v.bbbb.ovvv, (5, 0, 6, 4), denom3.babbab, (1, 2, 5, 0, 3, 6), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aabb.ovov, (2, 3, 5, 6), v.bbbb.ovvv, (5, 6, 0, 4), denom3.babbab, (1, 2, 5, 0, 3, 6), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aaaa.ovov, (2, 3, 5, 6), v.aabb.ovvv, (5, 6, 0, 4), denom3.abaaba, (2, 1, 5, 3, 0, 6), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ovov, (2, 4, 5, 6), v.aaaa.ovvv, (5, 4, 6, 3), denom3.abaaba, (2, 1, 5, 4, 0, 6), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ovov, (2, 4, 5, 6), v.aaaa.ovvv, (5, 6, 4, 3), denom3.abaaba, (2, 1, 5, 4, 0, 6), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aaaa.ovov, (2, 5, 6, 3), v.aabb.ovvv, (6, 5, 0, 4), denom3.abaaba, (2, 1, 6, 5, 0, 3), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aaaa.ovov, (5, 3, 2, 6), v.aabb.ovvv, (5, 6, 0, 4), denom3.abaaba, (5, 1, 2, 3, 0, 6), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ovov, (4, 5, 2, 6), v.aaaa.ovvv, (4, 5, 6, 3), denom3.abaaba, (4, 1, 2, 5, 0, 6), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aaaa.ovov, (4, 5, 2, 6), v.aaaa.ovvv, (4, 6, 5, 3), denom3.abaaba, (4, 1, 2, 5, 0, 6), ()) * -1.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aaaa.ovov, (5, 6, 2, 3), v.aabb.ovvv, (5, 6, 0, 4), denom3.abaaba, (5, 1, 2, 6, 0, 3), ())
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), v.aabb.ovov, (2, 4, 5, 6), v.aabb.vvov, (4, 3, 5, 6), denom3.babbab, (1, 2, 5, 0, 4, 6), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), v.aabb.ovov, (2, 5, 3, 6), v.aabb.vvov, (5, 4, 1, 6), denom3.babbab, (1, 2, 3, 0, 5, 6), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), v.aabb.ovov, (2, 5, 6, 4), v.aabb.vvov, (5, 3, 6, 0), denom3.babbab, (1, 2, 6, 0, 5, 4), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 5), v.aabb.ovov, (2, 6, 3, 5), v.aabb.vvov, (6, 4, 1, 0), denom3.babbab, (1, 2, 3, 0, 6, 5), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (4, 3, 5, 6), denom3.bbbbbb, (1, 4, 5, 0, 3, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ooov, (5, 2, 6, 0), v.bbbb.ovov, (5, 3, 6, 4), denom3.bbbbbb, (1, 5, 6, 0, 3, 4), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (4, 6, 5, 3), denom3.bbbbbb, (1, 4, 5, 0, 6, 3), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (5, 3, 4, 6), denom3.bbbbbb, (1, 5, 4, 0, 3, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ooov, (5, 2, 6, 0), v.bbbb.ovov, (6, 3, 5, 4), denom3.bbbbbb, (1, 6, 5, 0, 3, 4), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ooov, (4, 2, 5, 6), v.bbbb.ovov, (5, 6, 4, 3), denom3.bbbbbb, (1, 5, 4, 0, 6, 3), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (1, 3, 5, 6), v.bbbb.ovov, (2, 4, 5, 6), denom3.bbbbbb, (1, 2, 5, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ooov, (1, 3, 6, 0), v.bbbb.ovov, (2, 4, 6, 5), denom3.bbbbbb, (1, 2, 6, 0, 4, 5), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (1, 3, 5, 6), v.bbbb.ovov, (2, 6, 5, 4), denom3.bbbbbb, (1, 2, 5, 0, 6, 4), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (1, 3, 5, 6), v.bbbb.ovov, (5, 4, 2, 6), denom3.bbbbbb, (1, 5, 2, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ooov, (1, 3, 6, 0), v.bbbb.ovov, (6, 4, 2, 5), denom3.bbbbbb, (1, 6, 2, 0, 4, 5), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (1, 3, 5, 6), v.bbbb.ovov, (5, 6, 2, 4), denom3.bbbbbb, (1, 5, 2, 0, 6, 4), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (5, 3, 1, 6), v.bbbb.ovov, (2, 4, 5, 6), denom3.bbbbbb, (1, 2, 5, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ooov, (6, 3, 1, 0), v.bbbb.ovov, (2, 4, 6, 5), denom3.bbbbbb, (1, 2, 6, 0, 4, 5), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aabb.ooov, (6, 3, 1, 0), v.aaaa.ovov, (2, 4, 6, 5), denom3.abaaba, (2, 1, 6, 4, 0, 5), ()) * -2.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (5, 3, 1, 6), v.bbbb.ovov, (2, 6, 5, 4), denom3.bbbbbb, (1, 2, 5, 0, 6, 4), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (5, 3, 1, 6), v.bbbb.ovov, (5, 4, 2, 6), denom3.bbbbbb, (1, 5, 2, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ooov, (6, 3, 1, 0), v.bbbb.ovov, (6, 4, 2, 5), denom3.bbbbbb, (1, 6, 2, 0, 4, 5), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aabb.ooov, (6, 3, 1, 0), v.aaaa.ovov, (6, 4, 2, 5), denom3.abaaba, (6, 1, 2, 4, 0, 5), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ooov, (5, 3, 1, 6), v.bbbb.ovov, (5, 6, 2, 4), denom3.bbbbbb, (1, 5, 2, 0, 6, 4), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.aabb.ovoo, (4, 5, 6, 2), v.aabb.ovov, (4, 5, 6, 3), denom3.babbab, (1, 4, 6, 0, 5, 3), ()) * -4.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.aabb.ovoo, (5, 6, 1, 3), v.aabb.ovov, (5, 6, 2, 4), denom3.babbab, (1, 5, 2, 0, 6, 4), ()) * 4.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (2, 3, 5, 6), v.bbbb.ovvv, (5, 0, 6, 4), denom3.bbbbbb, (1, 2, 5, 0, 3, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (2, 3, 5, 6), v.bbbb.ovvv, (5, 6, 0, 4), denom3.bbbbbb, (1, 2, 5, 0, 3, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ovov, (2, 4, 5, 6), v.bbbb.ovvv, (5, 4, 6, 3), denom3.bbbbbb, (1, 2, 5, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ovov, (2, 4, 5, 6), v.bbbb.ovvv, (5, 6, 4, 3), denom3.bbbbbb, (1, 2, 5, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (2, 5, 6, 3), v.bbbb.ovvv, (6, 0, 5, 4), denom3.bbbbbb, (1, 2, 6, 0, 5, 3), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (2, 5, 6, 3), v.bbbb.ovvv, (6, 5, 0, 4), denom3.bbbbbb, (1, 2, 6, 0, 5, 3), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (5, 3, 2, 6), v.bbbb.ovvv, (5, 0, 6, 4), denom3.bbbbbb, (1, 5, 2, 0, 3, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (5, 3, 2, 6), v.bbbb.ovvv, (5, 6, 0, 4), denom3.bbbbbb, (1, 5, 2, 0, 3, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.aabb.ovov, (4, 5, 2, 6), v.aabb.ovvv, (4, 5, 6, 3), denom3.babbab, (1, 4, 2, 0, 5, 6), ()) * 4.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ovov, (4, 5, 2, 6), v.bbbb.ovvv, (4, 5, 6, 3), denom3.bbbbbb, (1, 4, 2, 0, 5, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 0, 3), v.bbbb.ovov, (4, 5, 2, 6), v.bbbb.ovvv, (4, 6, 5, 3), denom3.bbbbbb, (1, 4, 2, 0, 5, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (5, 6, 2, 3), v.bbbb.ovvv, (5, 0, 6, 4), denom3.bbbbbb, (1, 5, 2, 0, 6, 3), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.aabb.ovov, (5, 6, 2, 3), v.aabb.ovvv, (5, 6, 0, 4), denom3.babbab, (1, 5, 2, 0, 6, 3), ()) * -4.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (1, 2, 3, 4), v.bbbb.ovov, (5, 6, 2, 3), v.bbbb.ovvv, (5, 6, 0, 4), denom3.bbbbbb, (1, 5, 2, 0, 6, 3), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovov, (2, 4, 3, 6), v.bbbb.ovvv, (1, 0, 6, 5), denom3.bbbbbb, (1, 2, 3, 0, 4, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovov, (2, 4, 3, 6), v.bbbb.ovvv, (1, 6, 0, 5), denom3.bbbbbb, (1, 2, 3, 0, 4, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ovov, (2, 5, 3, 6), v.bbbb.ovvv, (1, 5, 6, 4), denom3.bbbbbb, (1, 2, 3, 0, 5, 6), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 0, 4), v.bbbb.ovov, (2, 5, 3, 6), v.bbbb.ovvv, (1, 6, 5, 4), denom3.bbbbbb, (1, 2, 3, 0, 5, 6), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovov, (2, 6, 3, 4), v.bbbb.ovvv, (1, 0, 6, 5), denom3.bbbbbb, (1, 2, 3, 0, 6, 4), ()) * -6.0
    e_pert += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovov, (2, 6, 3, 4), v.bbbb.ovvv, (1, 6, 0, 5), denom3.bbbbbb, (1, 2, 3, 0, 6, 4), ()) * 6.0
    e_pert += einsum(l1.bb, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovov, (2, 4, 3, 6), v.aabb.vvov, (6, 5, 1, 0), denom3.abaaba, (2, 1, 3, 4, 0, 6), ()) * 2.0
    e_pert += einsum(l1.bb, (0, 1), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovov, (2, 6, 3, 4), v.aabb.vvov, (6, 5, 1, 0), denom3.abaaba, (2, 1, 3, 6, 0, 4), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), v.bbbb.ooov, (3, 5, 6, 7), v.bbbb.ooov, (5, 4, 6, 7), denom3.babbab, (5, 2, 6, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 7, 5), v.bbbb.ooov, (6, 4, 7, 1), denom3.babbab, (6, 2, 7, 1, 0, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), v.bbbb.ooov, (3, 5, 6, 7), v.bbbb.ooov, (6, 4, 5, 7), denom3.babbab, (5, 2, 6, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 7, 5), v.bbbb.ooov, (7, 4, 6, 1), denom3.babbab, (6, 2, 7, 1, 0, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ooov, (3, 5, 6, 7), denom3.babbab, (3, 4, 6, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 7, 6), v.bbbb.ooov, (3, 5, 7, 1), denom3.babbab, (3, 4, 7, 1, 0, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ooov, (3, 5, 6, 7), denom3.babbab, (5, 2, 6, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 7, 1), v.bbbb.ooov, (3, 5, 7, 6), denom3.babbab, (5, 2, 7, 1, 0, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ooov, (3, 6, 5, 7), denom3.babbab, (6, 2, 5, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 7, 1), v.bbbb.ooov, (3, 7, 5, 6), denom3.babbab, (7, 2, 5, 1, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), v.aabb.ooov, (2, 5, 6, 7), v.aabb.ooov, (5, 4, 6, 7), denom3.babbab, (3, 5, 6, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aabb.ooov, (2, 6, 7, 5), v.aabb.ooov, (6, 4, 7, 1), denom3.babbab, (3, 6, 7, 1, 0, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), v.aaaa.ooov, (2, 5, 6, 7), v.aaaa.ooov, (5, 4, 6, 7), denom3.abaaba, (5, 3, 6, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 6, 7, 5), v.aaaa.ooov, (6, 4, 7, 0), denom3.abaaba, (6, 3, 7, 0, 1, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), v.aaaa.ooov, (2, 5, 6, 7), v.aaaa.ooov, (6, 4, 5, 7), denom3.abaaba, (5, 3, 6, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 6, 7, 5), v.aaaa.ooov, (7, 4, 6, 0), denom3.abaaba, (6, 3, 7, 0, 1, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ooov, (6, 5, 3, 7), denom3.babbab, (3, 4, 6, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 7, 6), v.bbbb.ooov, (7, 5, 3, 1), denom3.babbab, (3, 4, 7, 1, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aabb.ooov, (2, 6, 5, 7), v.aabb.ooov, (6, 4, 3, 7), denom3.babbab, (3, 6, 5, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 7, 5, 6), v.aabb.ooov, (7, 4, 3, 1), denom3.babbab, (3, 7, 5, 1, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aaaa.ooov, (2, 4, 7, 6), v.aabb.ovoo, (7, 0, 3, 5), denom3.abaaba, (4, 3, 7, 0, 1, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aaaa.ooov, (2, 4, 6, 7), v.aabb.ovoo, (6, 7, 3, 5), denom3.abaaba, (2, 5, 6, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aaaa.ooov, (2, 4, 6, 7), v.aabb.ovoo, (6, 7, 3, 5), denom3.abaaba, (4, 3, 6, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aaaa.ooov, (2, 4, 7, 0), v.aabb.ovoo, (7, 6, 3, 5), denom3.abaaba, (2, 5, 7, 0, 1, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aaaa.ooov, (2, 7, 4, 6), v.aabb.ovoo, (7, 0, 3, 5), denom3.abaaba, (7, 3, 4, 0, 1, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aaaa.ooov, (2, 6, 4, 7), v.aabb.ovoo, (6, 7, 3, 5), denom3.abaaba, (6, 3, 4, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aaaa.ooov, (6, 4, 2, 7), v.aabb.ovoo, (6, 7, 3, 5), denom3.abaaba, (2, 5, 6, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aaaa.ooov, (7, 4, 2, 0), v.aabb.ovoo, (7, 6, 3, 5), denom3.abaaba, (2, 5, 7, 0, 1, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 1, 7, 5), denom3.babbab, (4, 2, 6, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.babbab, (3, 2, 6, 5, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.babbab, (3, 2, 6, 7, 0, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.babbab, (4, 2, 6, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ovvv, (6, 1, 7, 5), denom3.babbab, (6, 2, 4, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.babbab, (6, 2, 4, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (6, 4, 3, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.babbab, (3, 2, 6, 5, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ooov, (6, 4, 3, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.babbab, (3, 2, 6, 7, 0, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 5, 7), v.bbbb.ovvv, (3, 1, 7, 6), denom3.babbab, (3, 4, 5, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 5, 7), v.bbbb.ovvv, (3, 7, 1, 6), denom3.babbab, (3, 4, 5, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aaaa.ooov, (2, 4, 7, 5), v.aabb.ovvv, (7, 0, 1, 6), denom3.abaaba, (4, 3, 7, 0, 1, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 4, 6, 7), v.aaaa.ovvv, (6, 0, 7, 5), denom3.abaaba, (4, 3, 6, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ovvv, (6, 1, 7, 5), denom3.babbab, (3, 4, 6, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.babbab, (3, 2, 6, 5, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 4, 6, 7), v.aaaa.ovvv, (6, 5, 0, 7), denom3.abaaba, (2, 3, 6, 5, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aaaa.ooov, (2, 4, 7, 0), v.aabb.ovvv, (7, 5, 1, 6), denom3.abaaba, (2, 3, 7, 0, 6, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aaaa.ooov, (2, 4, 6, 7), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 0, 5, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.babbab, (3, 2, 6, 7, 0, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aabb.ooov, (2, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.babbab, (3, 4, 6, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aaaa.ooov, (2, 4, 6, 7), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (4, 3, 6, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 4, 6, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.abaaba, (2, 3, 6, 7, 1, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 4, 6, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.abaaba, (4, 3, 6, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aaaa.ooov, (2, 7, 4, 5), v.aabb.ovvv, (7, 0, 1, 6), denom3.abaaba, (7, 3, 4, 0, 1, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 6, 4, 7), v.aaaa.ovvv, (6, 0, 7, 5), denom3.abaaba, (6, 3, 4, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aaaa.ooov, (2, 6, 4, 7), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (6, 3, 4, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (2, 6, 4, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.abaaba, (6, 3, 4, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 3, 7), v.bbbb.ovvv, (5, 6, 1, 7), denom3.babbab, (3, 2, 5, 6, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (2, 4, 3, 7), v.bbbb.ovvv, (5, 7, 1, 6), denom3.babbab, (3, 2, 5, 7, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (6, 4, 2, 7), v.aaaa.ovvv, (6, 5, 0, 7), denom3.abaaba, (2, 3, 6, 5, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aaaa.ooov, (7, 4, 2, 0), v.aabb.ovvv, (7, 5, 1, 6), denom3.abaaba, (2, 3, 7, 0, 6, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aaaa.ooov, (6, 4, 2, 7), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 0, 5, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ooov, (6, 4, 2, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.abaaba, (2, 3, 6, 7, 1, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.aabb.ovoo, (6, 0, 7, 4), v.aabb.ovoo, (6, 5, 3, 7), denom3.abaaba, (2, 7, 6, 0, 1, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), v.aabb.ovoo, (5, 6, 3, 7), v.aabb.ovoo, (5, 6, 7, 4), denom3.abaaba, (2, 7, 5, 0, 1, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ovoo, (2, 0, 7, 5), v.aabb.ovoo, (4, 6, 3, 7), denom3.abaaba, (2, 7, 4, 0, 1, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), v.aabb.ovoo, (2, 6, 7, 5), v.aabb.ovoo, (4, 6, 3, 7), denom3.abaaba, (2, 7, 4, 0, 1, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.ovoo, (7, 0, 3, 4), v.aabb.ovvv, (7, 5, 1, 6), denom3.abaaba, (2, 3, 7, 0, 6, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.ovoo, (7, 5, 3, 4), v.aabb.ovvv, (7, 0, 1, 6), denom3.abaaba, (2, 4, 7, 0, 1, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.aabb.ovoo, (6, 7, 3, 4), v.aaaa.ovvv, (6, 0, 7, 5), denom3.abaaba, (2, 4, 6, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.aabb.ovoo, (6, 7, 3, 4), v.aaaa.ovvv, (6, 5, 0, 7), denom3.abaaba, (2, 3, 6, 5, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.aabb.ovoo, (6, 7, 3, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 0, 5, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.aabb.ovoo, (6, 7, 3, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 4, 6, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.aabb.ovoo, (6, 7, 3, 4), v.aaaa.ovvv, (6, 7, 0, 5), denom3.abaaba, (2, 3, 6, 7, 1, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.aabb.ovoo, (6, 7, 3, 4), v.aaaa.ovvv, (6, 7, 0, 5), denom3.abaaba, (2, 4, 6, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ovoo, (2, 0, 3, 5), v.aabb.ovvv, (4, 6, 1, 7), denom3.abaaba, (2, 3, 4, 0, 7, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ovoo, (2, 7, 3, 5), v.aaaa.ovvv, (4, 6, 0, 7), denom3.abaaba, (2, 3, 4, 6, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ovoo, (2, 7, 3, 5), v.aabb.ovvv, (4, 7, 1, 6), denom3.abaaba, (2, 3, 4, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ovoo, (2, 7, 3, 5), v.aaaa.ovvv, (4, 7, 0, 6), denom3.abaaba, (2, 3, 4, 7, 1, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ovoo, (4, 6, 3, 5), v.aabb.ovvv, (2, 0, 1, 7), denom3.abaaba, (2, 5, 4, 0, 1, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ovoo, (4, 7, 3, 5), v.aaaa.ovvv, (2, 0, 7, 6), denom3.abaaba, (2, 5, 4, 0, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ovoo, (4, 7, 3, 5), v.aabb.ovvv, (2, 7, 1, 6), denom3.abaaba, (2, 5, 4, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ovoo, (4, 7, 3, 5), v.aaaa.ovvv, (2, 7, 0, 6), denom3.abaaba, (2, 5, 4, 0, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ovvv, (3, 6, 7, 5), v.bbbb.ovvv, (4, 6, 1, 7), denom3.babbab, (3, 2, 4, 6, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.bbbb.ovvv, (3, 6, 7, 5), v.bbbb.ovvv, (4, 7, 1, 6), denom3.babbab, (3, 2, 4, 7, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.aabb.ovvv, (6, 0, 7, 5), v.aabb.ovvv, (6, 4, 1, 7), denom3.abaaba, (2, 3, 6, 0, 7, 4), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.aaaa.ovvv, (6, 0, 7, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 0, 5, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.aaaa.ovvv, (6, 4, 0, 7), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 4, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), v.aabb.ovvv, (5, 6, 1, 7), v.aabb.ovvv, (5, 6, 7, 4), denom3.abaaba, (2, 3, 5, 0, 7, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), v.bbbb.ovvv, (5, 6, 1, 7), v.bbbb.ovvv, (5, 6, 7, 4), denom3.babbab, (3, 2, 5, 6, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), v.aaaa.ovvv, (5, 6, 0, 7), v.aaaa.ovvv, (5, 6, 7, 4), denom3.abaaba, (2, 3, 5, 6, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), v.bbbb.ovvv, (5, 6, 1, 7), v.bbbb.ovvv, (5, 7, 6, 4), denom3.babbab, (3, 2, 5, 6, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), v.aaaa.ovvv, (5, 6, 0, 7), v.aaaa.ovvv, (5, 7, 6, 4), denom3.abaaba, (2, 3, 5, 6, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.aaaa.ovvv, (6, 7, 0, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 0, 5, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.aaaa.ovvv, (6, 7, 0, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.abaaba, (2, 3, 6, 7, 1, 4), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ovvv, (2, 0, 7, 6), v.aabb.ovvv, (4, 5, 1, 7), denom3.abaaba, (2, 3, 4, 0, 7, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aaaa.ovvv, (2, 0, 7, 5), v.aabb.ovvv, (4, 7, 1, 6), denom3.abaaba, (2, 3, 4, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), v.aabb.ovvv, (2, 6, 7, 5), v.aabb.ovvv, (4, 6, 1, 7), denom3.abaaba, (2, 3, 4, 0, 7, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ovvv, (2, 6, 7, 5), v.aaaa.ovvv, (4, 6, 0, 7), denom3.abaaba, (2, 3, 4, 6, 1, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aaaa.ovvv, (2, 6, 7, 5), v.aaaa.ovvv, (4, 7, 0, 6), denom3.abaaba, (2, 3, 4, 7, 1, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ovvv, (2, 7, 1, 6), v.aaaa.ovvv, (4, 5, 0, 7), denom3.abaaba, (2, 3, 4, 5, 1, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aaaa.ovvv, (2, 7, 0, 5), v.aabb.ovvv, (4, 7, 1, 6), denom3.abaaba, (2, 3, 4, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ovvv, (2, 7, 1, 6), v.aaaa.ovvv, (4, 7, 0, 5), denom3.abaaba, (2, 3, 4, 7, 1, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.bbbb.ooov, (3, 4, 6, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.babbab, (3, 2, 6, 1, 5, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ooov, (3, 4, 7, 1), v.aabb.vvov, (0, 5, 7, 6), denom3.babbab, (3, 2, 7, 1, 5, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.bbbb.ooov, (3, 4, 6, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.babbab, (4, 2, 6, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ooov, (3, 4, 7, 6), v.aabb.vvov, (0, 5, 7, 1), denom3.babbab, (4, 2, 7, 1, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.bbbb.ooov, (3, 6, 4, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.babbab, (6, 2, 4, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ooov, (3, 7, 4, 6), v.aabb.vvov, (0, 5, 7, 1), denom3.babbab, (7, 2, 4, 1, 0, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.bbbb.ooov, (6, 4, 3, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.babbab, (3, 2, 6, 1, 5, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ooov, (7, 4, 3, 1), v.aabb.vvov, (0, 5, 7, 6), denom3.babbab, (3, 2, 7, 1, 5, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aabb.ooov, (2, 4, 6, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.babbab, (3, 2, 6, 1, 5, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), v.aabb.ooov, (2, 4, 6, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.babbab, (3, 4, 6, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ooov, (2, 4, 7, 1), v.aabb.vvov, (0, 5, 7, 6), denom3.babbab, (3, 2, 7, 1, 5, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ooov, (2, 4, 7, 6), v.aabb.vvov, (0, 5, 7, 1), denom3.babbab, (3, 4, 7, 1, 0, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ooov, (2, 4, 3, 7), v.aabb.vvov, (0, 6, 5, 7), denom3.babbab, (3, 2, 5, 1, 6, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ooov, (2, 4, 3, 1), v.aabb.vvov, (0, 6, 5, 7), denom3.babbab, (3, 2, 5, 1, 6, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ooov, (2, 4, 5, 7), v.aabb.vvov, (0, 6, 3, 7), denom3.babbab, (3, 4, 5, 1, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ooov, (2, 4, 5, 7), v.aabb.vvov, (0, 6, 3, 1), denom3.babbab, (3, 4, 5, 1, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ovvv, (3, 1, 7, 6), v.aabb.vvov, (0, 5, 4, 7), denom3.babbab, (3, 2, 4, 1, 5, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ovvv, (3, 7, 1, 6), v.aabb.vvov, (0, 5, 4, 7), denom3.babbab, (3, 2, 4, 1, 5, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.bbbb.ovvv, (6, 1, 7, 5), v.aabb.vvov, (0, 4, 6, 7), denom3.babbab, (3, 2, 6, 1, 4, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.bbbb.ovvv, (6, 5, 1, 7), v.aabb.vvov, (0, 4, 6, 7), denom3.babbab, (3, 2, 6, 5, 0, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.bbbb.ovvv, (6, 7, 1, 5), v.aabb.vvov, (0, 4, 6, 7), denom3.babbab, (3, 2, 6, 1, 4, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.bbbb.ovvv, (6, 7, 1, 5), v.aabb.vvov, (0, 4, 6, 7), denom3.babbab, (3, 2, 6, 7, 0, 5), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ovvv, (4, 6, 1, 7), v.aabb.vvov, (0, 5, 3, 7), denom3.babbab, (3, 2, 4, 6, 0, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.bbbb.ovvv, (4, 7, 1, 6), v.aabb.vvov, (0, 5, 3, 7), denom3.babbab, (3, 2, 4, 7, 0, 6), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), v.aabb.vvov, (0, 5, 6, 7), v.aabb.vvov, (5, 4, 6, 7), denom3.babbab, (3, 2, 6, 1, 5, 7), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), v.aabb.vvov, (0, 6, 4, 7), v.aabb.vvov, (6, 5, 3, 7), denom3.babbab, (3, 2, 4, 1, 6, 7), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), v.aabb.vvov, (0, 6, 7, 5), v.aabb.vvov, (6, 4, 7, 1), denom3.babbab, (3, 2, 7, 1, 6, 5), ()) * -2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.vvov, (0, 7, 4, 6), v.aabb.vvov, (7, 5, 3, 1), denom3.babbab, (3, 2, 4, 1, 7, 6), ()) * 2.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 4, 7, 6), v.aabb.ooov, (7, 5, 3, 1), denom3.abaaba, (4, 3, 7, 0, 1, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 7, 4, 6), v.aabb.ooov, (7, 5, 3, 1), denom3.abaaba, (7, 3, 4, 0, 1, 6), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aabb.ooov, (6, 4, 7, 1), v.aabb.ovoo, (6, 5, 3, 7), denom3.abaaba, (2, 7, 6, 0, 1, 5), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 1, 5), v.aabb.ooov, (2, 6, 7, 5), v.aabb.ovoo, (6, 0, 7, 4), denom3.babbab, (3, 6, 7, 1, 0, 5), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aabb.ooov, (2, 5, 7, 1), v.aabb.ovoo, (4, 6, 3, 7), denom3.abaaba, (2, 7, 4, 0, 1, 6), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.aabb.ooov, (2, 7, 4, 6), v.aabb.ovoo, (7, 0, 3, 5), denom3.babbab, (3, 7, 4, 1, 0, 6), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 4, 7, 6), v.aabb.ovoo, (2, 0, 7, 5), denom3.babbab, (4, 2, 7, 1, 0, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 7, 4, 6), v.aabb.ovoo, (2, 0, 7, 5), denom3.babbab, (7, 2, 4, 1, 0, 6), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aabb.ooov, (6, 4, 3, 7), v.aabb.ovvv, (6, 5, 1, 7), denom3.abaaba, (2, 3, 6, 0, 7, 5), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aabb.ooov, (7, 4, 3, 1), v.aaaa.ovvv, (7, 5, 0, 6), denom3.abaaba, (2, 3, 7, 5, 1, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 1, 5), v.aabb.ooov, (2, 6, 4, 7), v.aabb.ovvv, (6, 0, 7, 5), denom3.babbab, (3, 6, 4, 1, 0, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.aabb.ooov, (2, 7, 4, 5), v.aabb.ovvv, (7, 0, 1, 6), denom3.babbab, (3, 7, 4, 1, 0, 5), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aabb.ooov, (2, 5, 3, 7), v.aabb.ovvv, (4, 6, 1, 7), denom3.abaaba, (2, 3, 4, 0, 7, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 6, 7), v.aabb.ooov, (2, 5, 3, 1), v.aaaa.ovvv, (4, 6, 0, 7), denom3.abaaba, (2, 3, 4, 6, 1, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 4, 5, 7), v.aabb.ovvv, (2, 0, 7, 6), denom3.babbab, (4, 2, 5, 1, 0, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 6, 7), v.bbbb.ooov, (3, 4, 5, 6), v.aabb.ovvv, (2, 0, 1, 7), denom3.babbab, (4, 2, 5, 1, 0, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.aabb.ovoo, (2, 0, 7, 4), v.bbbb.ovvv, (7, 5, 1, 6), denom3.babbab, (3, 2, 7, 5, 0, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 6, 7), v.aabb.ovoo, (2, 0, 3, 5), v.bbbb.ovvv, (4, 6, 1, 7), denom3.babbab, (3, 2, 4, 6, 0, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.aabb.ovvv, (2, 0, 7, 6), v.bbbb.ovvv, (4, 5, 1, 7), denom3.babbab, (3, 2, 4, 5, 0, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.aabb.ovvv, (2, 0, 7, 6), v.bbbb.ovvv, (4, 7, 1, 5), denom3.babbab, (3, 2, 4, 7, 0, 5), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 6, 7), v.aaaa.ooov, (2, 4, 5, 6), v.aabb.vvov, (0, 7, 3, 1), denom3.abaaba, (4, 3, 5, 0, 1, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 4, 5, 7), v.aabb.vvov, (7, 6, 3, 1), denom3.abaaba, (4, 3, 5, 0, 1, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aabb.ovoo, (4, 5, 3, 7), v.aabb.vvov, (0, 6, 7, 1), denom3.abaaba, (2, 7, 4, 0, 1, 5), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aabb.ovoo, (4, 6, 3, 7), v.aabb.vvov, (6, 5, 7, 1), denom3.abaaba, (2, 7, 4, 0, 1, 6), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 1, 5), v.aabb.ovoo, (2, 6, 7, 4), v.aabb.vvov, (0, 6, 7, 5), denom3.babbab, (3, 2, 7, 1, 6, 5), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.aabb.ovoo, (2, 7, 3, 5), v.aabb.vvov, (0, 7, 4, 6), denom3.babbab, (3, 2, 4, 1, 7, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aabb.ovvv, (4, 5, 1, 7), v.aabb.vvov, (0, 6, 3, 7), denom3.abaaba, (2, 3, 4, 0, 7, 5), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aabb.ovvv, (4, 6, 1, 7), v.aabb.vvov, (6, 5, 3, 7), denom3.abaaba, (2, 3, 4, 0, 7, 6), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ovvv, (4, 5, 0, 7), v.aabb.vvov, (7, 6, 3, 1), denom3.abaaba, (2, 3, 4, 5, 1, 7), ()) * -4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ovvv, (4, 7, 0, 5), v.aabb.vvov, (7, 6, 3, 1), denom3.abaaba, (2, 3, 4, 7, 1, 5), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 1, 5), v.aabb.ovvv, (2, 6, 7, 5), v.aabb.vvov, (0, 6, 4, 7), denom3.babbab, (3, 2, 4, 1, 6, 7), ()) * 4.0
    e_pert += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.aabb.ovvv, (2, 7, 1, 6), v.aabb.vvov, (0, 7, 4, 5), denom3.babbab, (3, 2, 4, 1, 7, 5), ()) * -4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aaaa.ooov, (2, 4, 7, 1), v.aabb.ooov, (3, 7, 5, 6), denom3.abaaba, (2, 5, 7, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 1, 6), v.aaaa.ooov, (2, 4, 7, 0), v.aabb.ooov, (3, 7, 5, 6), denom3.abaaba, (2, 5, 7, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (3, 7, 5, 6), v.aaaa.ooov, (7, 4, 2, 1), denom3.abaaba, (2, 5, 7, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 1, 6), v.aabb.ooov, (3, 7, 5, 6), v.aaaa.ooov, (7, 4, 2, 0), denom3.abaaba, (2, 5, 7, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 1, 5), v.aabb.ooov, (3, 6, 7, 5), v.aabb.ovoo, (6, 0, 7, 4), denom3.abaaba, (2, 7, 6, 0, 5, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.aabb.ooov, (3, 6, 7, 5), v.aabb.ovoo, (6, 1, 7, 4), denom3.abaaba, (2, 7, 6, 0, 5, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 0), v.bbbb.ooov, (2, 5, 7, 1), v.aabb.ovoo, (4, 6, 3, 7), denom3.babbab, (2, 4, 7, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.bbbb.ooov, (2, 5, 7, 0), v.aabb.ovoo, (4, 6, 3, 7), denom3.babbab, (2, 4, 7, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 1, 6), v.aabb.ooov, (3, 4, 7, 6), v.aabb.ovoo, (2, 0, 7, 5), denom3.abaaba, (2, 7, 4, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (3, 4, 7, 6), v.aabb.ovoo, (2, 1, 7, 5), denom3.abaaba, (2, 7, 4, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 0), v.aabb.ooov, (6, 4, 7, 1), v.aabb.ovoo, (6, 5, 3, 7), denom3.babbab, (2, 6, 7, 0, 5, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 1), v.aabb.ooov, (6, 4, 7, 0), v.aabb.ovoo, (6, 5, 3, 7), denom3.babbab, (2, 6, 7, 0, 5, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 0), v.bbbb.ooov, (7, 5, 2, 1), v.aabb.ovoo, (4, 6, 3, 7), denom3.babbab, (2, 4, 7, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.bbbb.ooov, (7, 5, 2, 0), v.aabb.ovoo, (4, 6, 3, 7), denom3.babbab, (2, 4, 7, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 0), v.aabb.ooov, (7, 4, 2, 1), v.aabb.ovoo, (7, 6, 3, 5), denom3.babbab, (2, 7, 5, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ooov, (7, 4, 2, 0), v.aabb.ovoo, (7, 6, 3, 5), denom3.babbab, (2, 7, 5, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 1, 5), v.aabb.ooov, (3, 6, 4, 7), v.aabb.ovvv, (6, 0, 7, 5), denom3.abaaba, (2, 4, 6, 0, 7, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.ooov, (3, 7, 4, 6), v.aaaa.ovvv, (7, 0, 1, 5), denom3.abaaba, (2, 4, 7, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.aabb.ooov, (3, 6, 4, 7), v.aabb.ovvv, (6, 1, 7, 5), denom3.abaaba, (2, 4, 6, 0, 7, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.ooov, (3, 7, 4, 6), v.aaaa.ovvv, (7, 1, 0, 5), denom3.abaaba, (2, 4, 7, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 0), v.bbbb.ooov, (2, 5, 3, 7), v.aabb.ovvv, (4, 6, 1, 7), denom3.babbab, (2, 4, 3, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.bbbb.ooov, (2, 5, 3, 0), v.aabb.ovvv, (4, 6, 1, 7), denom3.babbab, (2, 4, 3, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 1, 6), v.aabb.ooov, (3, 4, 5, 7), v.aabb.ovvv, (2, 0, 7, 6), denom3.abaaba, (2, 5, 4, 0, 7, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ooov, (3, 4, 5, 7), v.aaaa.ovvv, (2, 0, 1, 6), denom3.abaaba, (2, 5, 4, 0, 7, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aabb.ooov, (3, 4, 5, 7), v.aabb.ovvv, (2, 1, 7, 6), denom3.abaaba, (2, 5, 4, 0, 7, 1), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ooov, (3, 4, 5, 7), v.aaaa.ovvv, (2, 1, 0, 6), denom3.abaaba, (2, 5, 4, 0, 7, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 0), v.bbbb.ooov, (3, 5, 2, 7), v.aabb.ovvv, (4, 6, 1, 7), denom3.babbab, (2, 4, 3, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.bbbb.ooov, (3, 5, 2, 0), v.aabb.ovvv, (4, 6, 1, 7), denom3.babbab, (2, 4, 3, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 0), v.aabb.ooov, (6, 4, 3, 7), v.aabb.ovvv, (6, 5, 1, 7), denom3.babbab, (2, 6, 3, 0, 5, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 6), v.aabb.ooov, (7, 4, 3, 0), v.aabb.ovvv, (7, 5, 1, 6), denom3.babbab, (2, 7, 3, 0, 5, 6), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 0), v.aabb.ooov, (6, 4, 2, 7), v.aabb.ovvv, (6, 5, 1, 7), denom3.babbab, (2, 6, 3, 0, 5, 7), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ooov, (7, 4, 2, 0), v.aabb.ovvv, (7, 5, 1, 6), denom3.babbab, (2, 7, 3, 0, 5, 6), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ovoo, (4, 6, 3, 5), v.bbbb.ovvv, (2, 0, 1, 7), denom3.babbab, (2, 4, 5, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aabb.ovoo, (4, 6, 3, 5), v.bbbb.ovvv, (2, 1, 0, 7), denom3.babbab, (2, 4, 5, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 6), v.aabb.ovoo, (4, 5, 3, 7), v.bbbb.ovvv, (7, 0, 1, 6), denom3.babbab, (2, 4, 7, 0, 5, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 6), v.aabb.ovoo, (4, 5, 3, 7), v.bbbb.ovvv, (7, 1, 0, 6), denom3.babbab, (2, 4, 7, 0, 5, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.bbbb.ovvv, (2, 0, 7, 6), v.aabb.ovvv, (4, 5, 1, 7), denom3.babbab, (2, 4, 3, 0, 5, 7), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.bbbb.ovvv, (2, 7, 0, 6), v.aabb.ovvv, (4, 5, 1, 7), denom3.babbab, (2, 4, 3, 0, 5, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 6), v.bbbb.ovvv, (3, 0, 7, 6), v.aabb.ovvv, (4, 5, 1, 7), denom3.babbab, (2, 4, 3, 0, 5, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 6), v.bbbb.ovvv, (3, 7, 0, 6), v.aabb.ovvv, (4, 5, 1, 7), denom3.babbab, (2, 4, 3, 0, 5, 7), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aaaa.ooov, (2, 4, 3, 0), v.aabb.vvov, (1, 6, 5, 7), denom3.abaaba, (2, 5, 3, 0, 7, 6), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aaaa.ooov, (2, 4, 3, 7), v.aabb.vvov, (1, 7, 5, 6), denom3.abaaba, (2, 5, 3, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 6, 7), v.aaaa.ooov, (3, 4, 2, 0), v.aabb.vvov, (1, 6, 5, 7), denom3.abaaba, (2, 5, 3, 0, 7, 6), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (4, 5, 0, 6), v.aaaa.ooov, (3, 4, 2, 7), v.aabb.vvov, (1, 7, 5, 6), denom3.abaaba, (2, 5, 3, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.ovoo, (3, 0, 7, 4), v.aabb.vvov, (1, 5, 7, 6), denom3.abaaba, (2, 7, 3, 0, 6, 5), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.aabb.ovoo, (3, 6, 7, 4), v.aabb.vvov, (1, 6, 7, 5), denom3.abaaba, (2, 7, 3, 0, 5, 6), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 5, 6), v.aabb.ovoo, (2, 0, 7, 4), v.aabb.vvov, (1, 5, 7, 6), denom3.abaaba, (2, 7, 3, 0, 6, 5), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 0, 5), v.aabb.ovoo, (2, 6, 7, 4), v.aabb.vvov, (1, 6, 7, 5), denom3.abaaba, (2, 7, 3, 0, 5, 6), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 0), v.aabb.ovoo, (4, 6, 3, 7), v.aabb.vvov, (6, 5, 7, 1), denom3.babbab, (2, 4, 7, 0, 6, 1), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 1), v.aabb.ovoo, (4, 6, 3, 7), v.aabb.vvov, (6, 5, 7, 0), denom3.babbab, (2, 4, 7, 0, 6, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 0), v.aabb.ovoo, (4, 7, 3, 5), v.aabb.vvov, (7, 6, 2, 1), denom3.babbab, (2, 4, 5, 0, 7, 1), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 5, 6, 1), v.aabb.ovoo, (4, 7, 3, 5), v.aabb.vvov, (7, 6, 2, 0), denom3.babbab, (2, 4, 5, 0, 7, 1), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aabb.ovvv, (3, 0, 7, 6), v.aabb.vvov, (1, 5, 4, 7), denom3.abaaba, (2, 4, 3, 0, 7, 5), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aaaa.ovvv, (3, 0, 7, 5), v.aabb.vvov, (1, 7, 4, 6), denom3.abaaba, (2, 4, 3, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), v.aabb.ovvv, (3, 6, 7, 5), v.aabb.vvov, (1, 6, 4, 7), denom3.abaaba, (2, 4, 3, 0, 7, 6), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (2, 4, 5, 6), v.aaaa.ovvv, (3, 7, 0, 5), v.aabb.vvov, (1, 7, 4, 6), denom3.abaaba, (2, 4, 3, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 5, 6), v.aabb.ovvv, (2, 0, 7, 6), v.aabb.vvov, (1, 5, 4, 7), denom3.abaaba, (2, 4, 3, 0, 7, 5), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 5, 6), v.aaaa.ovvv, (2, 0, 7, 5), v.aabb.vvov, (1, 7, 4, 6), denom3.abaaba, (2, 4, 3, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 0, 5), v.aabb.ovvv, (2, 6, 7, 5), v.aabb.vvov, (1, 6, 4, 7), denom3.abaaba, (2, 4, 3, 0, 7, 6), ()) * -2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 5, 6), v.aaaa.ovvv, (2, 7, 0, 5), v.aabb.vvov, (1, 7, 4, 6), denom3.abaaba, (2, 4, 3, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 0), v.aabb.ovvv, (4, 6, 1, 7), v.aabb.vvov, (6, 5, 3, 7), denom3.babbab, (2, 4, 3, 0, 6, 7), ()) * 2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 0), v.aabb.ovvv, (4, 6, 1, 7), v.aabb.vvov, (6, 5, 2, 7), denom3.babbab, (2, 4, 3, 0, 6, 7), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 2, 5, 6), v.aabb.ovvv, (4, 7, 1, 6), v.aabb.vvov, (7, 5, 3, 0), denom3.babbab, (2, 4, 3, 0, 7, 6), ()) * -2.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 6), v.aabb.ovvv, (4, 7, 1, 6), v.aabb.vvov, (7, 5, 2, 0), denom3.babbab, (2, 4, 3, 0, 7, 6), ()) * 2.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 1), v.aaaa.ooov, (3, 5, 6, 7), v.aaaa.ooov, (5, 4, 6, 7), denom3.aaaaaa, (2, 5, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 1), v.bbbb.ooov, (3, 5, 6, 7), v.bbbb.ooov, (5, 4, 6, 7), denom3.bbbbbb, (2, 5, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 1), v.aabb.ooov, (3, 5, 6, 7), v.aabb.ooov, (5, 4, 6, 7), denom3.abaaba, (2, 6, 5, 0, 7, 1), ()) * 4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 6, 7, 5), v.aaaa.ooov, (6, 4, 7, 1), denom3.aaaaaa, (2, 6, 7, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 7, 5), v.bbbb.ooov, (6, 4, 7, 1), denom3.bbbbbb, (2, 6, 7, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aaaa.ooov, (3, 6, 7, 5), v.aaaa.ooov, (6, 4, 7, 0), denom3.aaaaaa, (2, 6, 7, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.bbbb.ooov, (3, 6, 7, 5), v.bbbb.ooov, (6, 4, 7, 0), denom3.bbbbbb, (2, 6, 7, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 1), v.aaaa.ooov, (3, 5, 6, 7), v.aaaa.ooov, (6, 4, 5, 7), denom3.aaaaaa, (2, 5, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 1), v.bbbb.ooov, (3, 5, 6, 7), v.bbbb.ooov, (6, 4, 5, 7), denom3.bbbbbb, (2, 5, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 6, 7, 5), v.aaaa.ooov, (7, 4, 6, 1), denom3.aaaaaa, (2, 6, 7, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 7, 5), v.bbbb.ooov, (7, 4, 6, 1), denom3.bbbbbb, (2, 6, 7, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aaaa.ooov, (3, 6, 7, 5), v.aaaa.ooov, (7, 4, 6, 0), denom3.aaaaaa, (2, 6, 7, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.bbbb.ooov, (3, 6, 7, 5), v.bbbb.ooov, (7, 4, 6, 0), denom3.bbbbbb, (2, 6, 7, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), v.aaaa.ooov, (2, 5, 6, 7), v.aaaa.ooov, (3, 4, 6, 7), denom3.aaaaaa, (2, 4, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), v.bbbb.ooov, (2, 5, 6, 7), v.bbbb.ooov, (3, 4, 6, 7), denom3.bbbbbb, (2, 4, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), v.aabb.ooov, (2, 5, 6, 7), v.aabb.ooov, (3, 4, 6, 7), denom3.abaaba, (2, 6, 4, 0, 7, 1), ()) * -4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 5, 7, 1), v.aaaa.ooov, (3, 4, 7, 6), denom3.aaaaaa, (2, 4, 7, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (2, 5, 7, 1), v.bbbb.ooov, (3, 4, 7, 6), denom3.bbbbbb, (2, 4, 7, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 1, 6), v.aaaa.ooov, (2, 5, 7, 0), v.aaaa.ooov, (3, 4, 7, 6), denom3.aaaaaa, (2, 4, 7, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (2, 5, 7, 0), v.bbbb.ooov, (3, 4, 7, 6), denom3.bbbbbb, (2, 4, 7, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), v.aaaa.ooov, (2, 5, 6, 7), v.aaaa.ooov, (3, 6, 4, 7), denom3.aaaaaa, (2, 6, 4, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), v.bbbb.ooov, (2, 5, 6, 7), v.bbbb.ooov, (3, 6, 4, 7), denom3.bbbbbb, (2, 6, 4, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 5, 7, 1), v.aaaa.ooov, (3, 7, 4, 6), denom3.aaaaaa, (2, 7, 4, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (2, 5, 7, 1), v.bbbb.ooov, (3, 7, 4, 6), denom3.bbbbbb, (2, 7, 4, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 1, 6), v.aaaa.ooov, (2, 5, 7, 0), v.aaaa.ooov, (3, 7, 4, 6), denom3.aaaaaa, (2, 7, 4, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (2, 5, 7, 0), v.bbbb.ooov, (3, 7, 4, 6), denom3.bbbbbb, (2, 7, 4, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ooov, (6, 5, 2, 7), denom3.aaaaaa, (2, 4, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ooov, (6, 5, 2, 7), denom3.bbbbbb, (2, 4, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (3, 4, 7, 6), v.aaaa.ooov, (7, 5, 2, 1), denom3.aaaaaa, (2, 4, 7, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (3, 4, 7, 6), v.bbbb.ooov, (7, 5, 2, 1), denom3.bbbbbb, (2, 4, 7, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 1, 6), v.aaaa.ooov, (3, 4, 7, 6), v.aaaa.ooov, (7, 5, 2, 0), denom3.aaaaaa, (2, 4, 7, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 4, 7, 6), v.bbbb.ooov, (7, 5, 2, 0), denom3.bbbbbb, (2, 4, 7, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), v.aaaa.ooov, (3, 6, 4, 7), v.aaaa.ooov, (6, 5, 2, 7), denom3.aaaaaa, (2, 6, 4, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ooov, (6, 5, 2, 7), denom3.bbbbbb, (2, 6, 4, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (3, 7, 4, 6), v.aaaa.ooov, (7, 5, 2, 1), denom3.aaaaaa, (2, 7, 4, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (3, 7, 4, 6), v.bbbb.ooov, (7, 5, 2, 1), denom3.bbbbbb, (2, 7, 4, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 1, 6), v.aaaa.ooov, (3, 7, 4, 6), v.aaaa.ooov, (7, 5, 2, 0), denom3.aaaaaa, (2, 7, 4, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 7, 4, 6), v.bbbb.ooov, (7, 5, 2, 0), denom3.bbbbbb, (2, 7, 4, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ovvv, (6, 0, 7, 5), denom3.aaaaaa, (2, 4, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 0, 7, 5), denom3.bbbbbb, (2, 4, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ooov, (3, 4, 7, 5), v.aaaa.ovvv, (7, 0, 1, 6), denom3.aaaaaa, (2, 4, 7, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ooov, (3, 4, 7, 5), v.bbbb.ovvv, (7, 0, 1, 6), denom3.bbbbbb, (2, 4, 7, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ovvv, (6, 1, 7, 5), denom3.aaaaaa, (2, 4, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 1, 7, 5), denom3.bbbbbb, (2, 4, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ooov, (3, 4, 7, 5), v.aaaa.ovvv, (7, 1, 0, 6), denom3.aaaaaa, (2, 4, 7, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ooov, (3, 4, 7, 5), v.bbbb.ovvv, (7, 1, 0, 6), denom3.bbbbbb, (2, 4, 7, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ovvv, (6, 5, 1, 7), denom3.aaaaaa, (2, 3, 6, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.bbbbbb, (2, 3, 6, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ooov, (3, 4, 7, 0), v.aaaa.ovvv, (7, 5, 1, 6), denom3.aaaaaa, (2, 3, 7, 0, 5, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ooov, (3, 4, 7, 0), v.bbbb.ovvv, (7, 5, 1, 6), denom3.bbbbbb, (2, 3, 7, 0, 5, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ovvv, (6, 7, 1, 5), denom3.aaaaaa, (2, 3, 6, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.bbbbbb, (2, 3, 6, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ovvv, (6, 7, 1, 5), denom3.aaaaaa, (2, 4, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.bbbbbb, (2, 4, 6, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aaaa.ooov, (3, 4, 6, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.aaaaaa, (2, 4, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.bbbb.ooov, (3, 4, 6, 7), v.bbbb.ovvv, (6, 7, 0, 5), denom3.bbbbbb, (2, 4, 6, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aaaa.ooov, (3, 6, 4, 7), v.aaaa.ovvv, (6, 0, 7, 5), denom3.aaaaaa, (2, 6, 4, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ovvv, (6, 0, 7, 5), denom3.bbbbbb, (2, 6, 4, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ooov, (3, 7, 4, 5), v.aaaa.ovvv, (7, 0, 1, 6), denom3.aaaaaa, (2, 7, 4, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ooov, (3, 7, 4, 5), v.bbbb.ovvv, (7, 0, 1, 6), denom3.bbbbbb, (2, 7, 4, 0, 1, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 6, 4, 7), v.aaaa.ovvv, (6, 1, 7, 5), denom3.aaaaaa, (2, 6, 4, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ovvv, (6, 1, 7, 5), denom3.bbbbbb, (2, 6, 4, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ooov, (3, 7, 4, 5), v.aaaa.ovvv, (7, 1, 0, 6), denom3.aaaaaa, (2, 7, 4, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ooov, (3, 7, 4, 5), v.bbbb.ovvv, (7, 1, 0, 6), denom3.bbbbbb, (2, 7, 4, 0, 1, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (3, 6, 4, 7), v.aaaa.ovvv, (6, 7, 1, 5), denom3.aaaaaa, (2, 6, 4, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.bbbbbb, (2, 6, 4, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aaaa.ooov, (3, 6, 4, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.aaaaaa, (2, 6, 4, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.bbbb.ooov, (3, 6, 4, 7), v.bbbb.ovvv, (6, 7, 0, 5), denom3.bbbbbb, (2, 6, 4, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (6, 4, 3, 7), v.aaaa.ovvv, (6, 5, 1, 7), denom3.aaaaaa, (2, 3, 6, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (6, 4, 3, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.bbbbbb, (2, 3, 6, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ooov, (7, 4, 3, 0), v.aaaa.ovvv, (7, 5, 1, 6), denom3.aaaaaa, (2, 3, 7, 0, 5, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ooov, (7, 4, 3, 0), v.bbbb.ovvv, (7, 5, 1, 6), denom3.bbbbbb, (2, 3, 7, 0, 5, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ooov, (6, 4, 3, 7), v.aaaa.ovvv, (6, 7, 1, 5), denom3.aaaaaa, (2, 3, 6, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ooov, (6, 4, 3, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.bbbbbb, (2, 3, 6, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aaaa.ooov, (2, 4, 6, 7), v.aaaa.ovvv, (6, 5, 1, 7), denom3.aaaaaa, (2, 3, 6, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.bbbb.ooov, (2, 4, 6, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.bbbbbb, (2, 3, 6, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 5, 6), v.aaaa.ooov, (2, 4, 7, 0), v.aaaa.ovvv, (7, 5, 1, 6), denom3.aaaaaa, (2, 3, 7, 0, 5, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.bbbb.ooov, (2, 4, 7, 0), v.bbbb.ovvv, (7, 5, 1, 6), denom3.bbbbbb, (2, 3, 7, 0, 5, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aaaa.ooov, (2, 4, 6, 7), v.aaaa.ovvv, (6, 7, 1, 5), denom3.aaaaaa, (2, 3, 6, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.bbbb.ooov, (2, 4, 6, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.bbbbbb, (2, 3, 6, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aaaa.ooov, (6, 4, 2, 7), v.aaaa.ovvv, (6, 5, 1, 7), denom3.aaaaaa, (2, 3, 6, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.bbbb.ooov, (6, 4, 2, 7), v.bbbb.ovvv, (6, 5, 1, 7), denom3.bbbbbb, (2, 3, 6, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 5, 6), v.aaaa.ooov, (7, 4, 2, 0), v.aaaa.ovvv, (7, 5, 1, 6), denom3.aaaaaa, (2, 3, 7, 0, 5, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.bbbb.ooov, (7, 4, 2, 0), v.bbbb.ovvv, (7, 5, 1, 6), denom3.bbbbbb, (2, 3, 7, 0, 5, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aaaa.ooov, (6, 4, 2, 7), v.aaaa.ovvv, (6, 7, 1, 5), denom3.aaaaaa, (2, 3, 6, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.bbbb.ooov, (6, 4, 2, 7), v.bbbb.ovvv, (6, 7, 1, 5), denom3.bbbbbb, (2, 3, 6, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 5, 3, 7), v.aaaa.ovvv, (4, 6, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (2, 5, 3, 7), v.bbbb.ovvv, (4, 6, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 6, 7), v.aaaa.ooov, (2, 5, 3, 0), v.aaaa.ovvv, (4, 6, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 6, 7), v.bbbb.ooov, (2, 5, 3, 0), v.bbbb.ovvv, (4, 6, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (2, 5, 3, 7), v.aaaa.ovvv, (4, 7, 1, 6), denom3.aaaaaa, (2, 3, 4, 0, 7, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (2, 5, 3, 7), v.bbbb.ovvv, (4, 7, 1, 6), denom3.bbbbbb, (2, 3, 4, 0, 7, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 1, 6), v.aaaa.ooov, (3, 4, 5, 7), v.aaaa.ovvv, (2, 0, 7, 6), denom3.aaaaaa, (2, 4, 5, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 4, 5, 7), v.bbbb.ovvv, (2, 0, 7, 6), denom3.bbbbbb, (2, 4, 5, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 6, 7), v.aaaa.ooov, (3, 4, 5, 6), v.aaaa.ovvv, (2, 0, 1, 7), denom3.aaaaaa, (2, 4, 5, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 6, 7), v.bbbb.ooov, (3, 4, 5, 6), v.bbbb.ovvv, (2, 0, 1, 7), denom3.bbbbbb, (2, 4, 5, 0, 1, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (3, 4, 5, 7), v.aaaa.ovvv, (2, 1, 7, 6), denom3.aaaaaa, (2, 4, 5, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (3, 4, 5, 7), v.bbbb.ovvv, (2, 1, 7, 6), denom3.bbbbbb, (2, 4, 5, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 6, 7), v.aaaa.ooov, (3, 4, 5, 6), v.aaaa.ovvv, (2, 1, 0, 7), denom3.aaaaaa, (2, 4, 5, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 6, 7), v.bbbb.ooov, (3, 4, 5, 6), v.bbbb.ovvv, (2, 1, 0, 7), denom3.bbbbbb, (2, 4, 5, 0, 1, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (3, 4, 5, 7), v.aaaa.ovvv, (2, 7, 1, 6), denom3.aaaaaa, (2, 4, 5, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (3, 4, 5, 7), v.bbbb.ovvv, (2, 7, 1, 6), denom3.bbbbbb, (2, 4, 5, 0, 1, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 1, 6), v.aaaa.ooov, (3, 4, 5, 7), v.aaaa.ovvv, (2, 7, 0, 6), denom3.aaaaaa, (2, 4, 5, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 1, 6), v.bbbb.ooov, (3, 4, 5, 7), v.bbbb.ovvv, (2, 7, 0, 6), denom3.bbbbbb, (2, 4, 5, 0, 1, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (3, 5, 2, 7), v.aaaa.ovvv, (4, 6, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (3, 5, 2, 7), v.bbbb.ovvv, (4, 6, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 6, 7), v.aaaa.ooov, (3, 5, 2, 0), v.aaaa.ovvv, (4, 6, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 6, 7), v.bbbb.ooov, (3, 5, 2, 0), v.bbbb.ovvv, (4, 6, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 6), v.aaaa.ooov, (3, 5, 2, 7), v.aaaa.ovvv, (4, 7, 1, 6), denom3.aaaaaa, (2, 3, 4, 0, 7, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 6), v.bbbb.ooov, (3, 5, 2, 7), v.bbbb.ovvv, (4, 7, 1, 6), denom3.bbbbbb, (2, 3, 4, 0, 7, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 1), v.aabb.ovoo, (5, 6, 3, 7), v.aabb.ovoo, (5, 6, 7, 4), denom3.babbab, (2, 5, 7, 0, 6, 1), ()) * 4.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), v.aabb.ovoo, (6, 7, 2, 5), v.aabb.ovoo, (6, 7, 3, 4), denom3.babbab, (2, 6, 4, 0, 7, 1), ()) * -4.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.aabb.ovoo, (6, 7, 3, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.babbab, (2, 6, 3, 0, 7, 5), ()) * -4.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.aabb.ovoo, (6, 7, 3, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.babbab, (2, 6, 4, 0, 7, 1), ()) * -4.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 1, 5), v.aabb.ovoo, (6, 7, 3, 4), v.aabb.ovvv, (6, 7, 0, 5), denom3.babbab, (2, 6, 4, 0, 7, 1), ()) * 4.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.aabb.ovoo, (6, 7, 2, 4), v.aabb.ovvv, (6, 7, 1, 5), denom3.babbab, (2, 6, 3, 0, 7, 5), ()) * 4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ovvv, (3, 0, 7, 6), v.aaaa.ovvv, (4, 5, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ovvv, (3, 0, 7, 6), v.bbbb.ovvv, (4, 5, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ovvv, (3, 0, 7, 6), v.aaaa.ovvv, (4, 7, 1, 5), denom3.aaaaaa, (2, 3, 4, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ovvv, (3, 0, 7, 6), v.bbbb.ovvv, (4, 7, 1, 5), denom3.bbbbbb, (2, 3, 4, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ovvv, (3, 6, 7, 5), v.aaaa.ovvv, (4, 6, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ovvv, (3, 6, 7, 5), v.bbbb.ovvv, (4, 6, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aaaa.ovvv, (3, 6, 7, 5), v.aaaa.ovvv, (4, 7, 1, 6), denom3.aaaaaa, (2, 3, 4, 0, 7, 6), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 0, 5), v.bbbb.ovvv, (3, 6, 7, 5), v.bbbb.ovvv, (4, 7, 1, 6), denom3.bbbbbb, (2, 3, 4, 0, 7, 6), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ovvv, (3, 7, 0, 6), v.aaaa.ovvv, (4, 5, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ovvv, (3, 7, 0, 6), v.bbbb.ovvv, (4, 5, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 5, 6), v.aaaa.ovvv, (3, 7, 0, 6), v.aaaa.ovvv, (4, 7, 1, 5), denom3.aaaaaa, (2, 3, 4, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 4, 5, 6), v.bbbb.ovvv, (3, 7, 0, 6), v.bbbb.ovvv, (4, 7, 1, 5), denom3.bbbbbb, (2, 3, 4, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovvv, (6, 0, 7, 5), v.aaaa.ovvv, (6, 4, 1, 7), denom3.aaaaaa, (2, 3, 6, 0, 4, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovvv, (6, 0, 7, 5), v.bbbb.ovvv, (6, 4, 1, 7), denom3.bbbbbb, (2, 3, 6, 0, 4, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovvv, (6, 0, 7, 5), v.aaaa.ovvv, (6, 7, 1, 4), denom3.aaaaaa, (2, 3, 6, 0, 7, 4), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovvv, (6, 0, 7, 5), v.bbbb.ovvv, (6, 7, 1, 4), denom3.bbbbbb, (2, 3, 6, 0, 7, 4), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovvv, (6, 4, 1, 7), v.aaaa.ovvv, (6, 7, 0, 5), denom3.aaaaaa, (2, 3, 6, 0, 4, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovvv, (6, 4, 1, 7), v.bbbb.ovvv, (6, 7, 0, 5), denom3.bbbbbb, (2, 3, 6, 0, 4, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 0, 4), v.aaaa.ovvv, (5, 6, 1, 7), v.aaaa.ovvv, (5, 6, 7, 4), denom3.aaaaaa, (2, 3, 5, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 0, 4), v.bbbb.ovvv, (5, 6, 1, 7), v.bbbb.ovvv, (5, 6, 7, 4), denom3.bbbbbb, (2, 3, 5, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 0, 4), v.aabb.ovvv, (5, 6, 1, 7), v.aabb.ovvv, (5, 6, 7, 4), denom3.babbab, (2, 5, 3, 0, 6, 7), ()) * 4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 0, 4), v.aaaa.ovvv, (5, 6, 1, 7), v.aaaa.ovvv, (5, 7, 6, 4), denom3.aaaaaa, (2, 3, 5, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 0, 4), v.bbbb.ovvv, (5, 6, 1, 7), v.bbbb.ovvv, (5, 7, 6, 4), denom3.bbbbbb, (2, 3, 5, 0, 6, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), v.aaaa.ovvv, (6, 7, 0, 5), v.aaaa.ovvv, (6, 7, 1, 4), denom3.aaaaaa, (2, 3, 6, 0, 7, 4), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), v.bbbb.ovvv, (6, 7, 0, 5), v.bbbb.ovvv, (6, 7, 1, 4), denom3.bbbbbb, (2, 3, 6, 0, 7, 4), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), v.aabb.ovvv, (6, 7, 0, 5), v.aabb.ovvv, (6, 7, 1, 4), denom3.babbab, (2, 6, 3, 0, 7, 4), ()) * -4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 5, 6), v.aaaa.ovvv, (2, 0, 7, 6), v.aaaa.ovvv, (4, 5, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.bbbb.ovvv, (2, 0, 7, 6), v.bbbb.ovvv, (4, 5, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 5, 7), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 5, 6), v.aaaa.ovvv, (2, 0, 7, 6), v.aaaa.ovvv, (4, 7, 1, 5), denom3.aaaaaa, (2, 3, 4, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.bbbb.ovvv, (2, 0, 7, 6), v.bbbb.ovvv, (4, 7, 1, 5), denom3.bbbbbb, (2, 3, 4, 0, 7, 5), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aaaa.ovvv, (2, 6, 7, 5), v.aaaa.ovvv, (4, 6, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.bbbb.ovvv, (2, 6, 7, 5), v.bbbb.ovvv, (4, 6, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 6, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aaaa.ovvv, (2, 6, 7, 5), v.aaaa.ovvv, (4, 7, 1, 6), denom3.aaaaaa, (2, 3, 4, 0, 7, 6), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 0, 5), v.bbbb.ovvv, (2, 6, 7, 5), v.bbbb.ovvv, (4, 7, 1, 6), denom3.bbbbbb, (2, 3, 4, 0, 7, 6), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 5, 6), v.aaaa.ovvv, (2, 7, 0, 6), v.aaaa.ovvv, (4, 5, 1, 7), denom3.aaaaaa, (2, 3, 4, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.bbbb.ovvv, (2, 7, 0, 6), v.bbbb.ovvv, (4, 5, 1, 7), denom3.bbbbbb, (2, 3, 4, 0, 5, 7), ()) * 12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 5, 6), v.aaaa.ovvv, (2, 7, 0, 6), v.aaaa.ovvv, (4, 7, 1, 5), denom3.aaaaaa, (2, 3, 4, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (3, 4, 5, 6), v.bbbb.ovvv, (2, 7, 0, 6), v.bbbb.ovvv, (4, 7, 1, 5), denom3.bbbbbb, (2, 3, 4, 0, 7, 5), ()) * -12.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 1, 5), v.aabb.ooov, (3, 4, 6, 7), v.aabb.vvov, (0, 5, 6, 7), denom3.abaaba, (2, 6, 4, 0, 7, 1), ()) * 4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aabb.ooov, (3, 4, 6, 7), v.aabb.vvov, (1, 5, 6, 7), denom3.abaaba, (2, 6, 3, 0, 7, 5), ()) * -4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 4, 0, 5), v.aabb.ooov, (3, 4, 6, 7), v.aabb.vvov, (1, 5, 6, 7), denom3.abaaba, (2, 6, 4, 0, 7, 1), ()) * -4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (3, 4, 0, 5), v.aabb.ooov, (2, 4, 6, 7), v.aabb.vvov, (1, 5, 6, 7), denom3.abaaba, (2, 6, 3, 0, 7, 5), ()) * 4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), v.aabb.vvov, (0, 5, 6, 7), v.aabb.vvov, (1, 4, 6, 7), denom3.abaaba, (2, 6, 3, 0, 7, 4), ()) * -4.0
    e_pert += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 0, 4), v.aabb.vvov, (1, 5, 6, 7), v.aabb.vvov, (5, 4, 6, 7), denom3.abaaba, (2, 6, 3, 0, 7, 5), ()) * 4.0
    e_pert /= 2

    return e_pert

