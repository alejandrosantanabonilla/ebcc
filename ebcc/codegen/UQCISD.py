# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 3), ())
    e_cc += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 2), ()) * -1.0
    e_cc += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 2, 1, 3), ())

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    t1new = Namespace()
    t2new = Namespace()

    # T amplitudes
    t1new_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    t1new_aa += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 2, 1, 3), (0, 4))
    t1new_aa += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (1, 3, 4, 2), (0, 4)) * 2.0
    t1new_aa += einsum(f.aa.vv, (0, 1), t1.aa, (2, 1), (2, 0))
    t1new_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    t1new_bb += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (1, 2, 4, 3), (0, 4)) * -2.0
    t1new_bb += einsum(f.bb.vv, (0, 1), t1.bb, (2, 1), (2, 0))
    t1new_bb += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (0, 2, 4, 3), (1, 4))
    t2new_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    t2new_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    t2new_abab += einsum(t1.aa, (0, 1), v.aabb.ooov, (2, 0, 3, 4), (2, 3, 1, 4)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), v.aabb.oovv, (4, 0, 5, 3), (4, 1, 2, 5)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvvv, (4, 2, 5, 3), (0, 1, 4, 5))
    t2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    t2new_abab += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (2, 0, 3, 4))
    t2new_abab += einsum(t1.aa, (0, 1), v.aabb.vvov, (2, 1, 3, 4), (0, 3, 2, 4))
    t2new_abab += einsum(t1.bb, (0, 1), v.aabb.ovoo, (2, 3, 4, 0), (2, 4, 3, 1)) * -1.0
    t2new_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    x0 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x0 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    t1new_aa += einsum(x0, (0, 1), (0, 1))
    x1 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x1 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x1 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    t1new_aa += einsum(t2.aaaa, (0, 1, 2, 3), x1, (4, 0, 1, 3), (4, 2)) * 2.0
    x2 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x2 += einsum(t1.aa, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (3, 4, 2, 0))
    t1new_aa += einsum(t2.abab, (0, 1, 2, 3), x2, (1, 3, 0, 4), (4, 2)) * -1.0
    x3 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x3 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x3 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x4 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x4 += einsum(t1.aa, (0, 1), x3, (0, 2, 3, 1), (2, 3))
    x5 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x5 += einsum(f.aa.ov, (0, 1), (0, 1))
    x5 += einsum(x0, (0, 1), (0, 1))
    x5 += einsum(x4, (0, 1), (0, 1)) * -1.0
    t1new_aa += einsum(x5, (0, 1), t2.aaaa, (2, 0, 3, 1), (2, 3)) * 2.0
    t1new_bb += einsum(x5, (0, 1), t2.abab, (0, 2, 1, 3), (2, 3))
    x6 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x6 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(x6, (0, 1), (0, 1))
    x7 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x8 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x8 += einsum(t1.bb, (0, 1), x7, (0, 2, 1, 3), (2, 3))
    x9 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x9 += einsum(f.bb.ov, (0, 1), (0, 1))
    x9 += einsum(x6, (0, 1), (0, 1))
    x9 += einsum(x8, (0, 1), (0, 1)) * -1.0
    t1new_aa += einsum(x9, (0, 1), t2.abab, (2, 0, 3, 1), (2, 3))
    t1new_bb += einsum(x9, (0, 1), t2.bbbb, (2, 0, 3, 1), (2, 3)) * 2.0
    x10 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x10 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x10 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new_aa += einsum(t1.aa, (0, 1), x10, (0, 2, 1, 3), (2, 3)) * -1.0
    x11 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x11 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 3), (0, 4))
    x12 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x12 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x13 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x13 += einsum(f.aa.oo, (0, 1), (0, 1))
    x13 += einsum(x11, (0, 1), (1, 0))
    x13 += einsum(x12, (0, 1), (1, 0)) * 2.0
    t1new_aa += einsum(t1.aa, (0, 1), x13, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x13, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x14 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x14 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x14 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    t1new_bb += einsum(t2.bbbb, (0, 1, 2, 3), x14, (4, 0, 1, 3), (4, 2)) * 2.0
    x15 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x15 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x15 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (4, 0, 2, 3))
    t1new_bb += einsum(t2.abab, (0, 1, 2, 3), x15, (1, 4, 0, 2), (4, 3)) * -1.0
    x16 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x16 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x16 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new_bb += einsum(t1.bb, (0, 1), x16, (0, 2, 1, 3), (2, 3)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x16, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x17 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x17 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 2, 1, 3), (0, 4))
    x18 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x18 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 3), (1, 4))
    x19 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x19 += einsum(f.bb.oo, (0, 1), (0, 1))
    x19 += einsum(x17, (0, 1), (1, 0)) * 2.0
    x19 += einsum(x18, (0, 1), (1, 0))
    t1new_bb += einsum(t1.bb, (0, 1), x19, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x19, (0, 1), t2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    x20 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x20 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x21 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x21 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x22 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x22 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2))
    t2new_abab += einsum(x22, (0, 1, 2, 3), (2, 0, 3, 1)) * 2.0
    x23 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x23 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x23 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x24 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x24 += einsum(t2.abab, (0, 1, 2, 3), x23, (1, 3, 4, 5), (0, 4, 2, 5))
    x25 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x25 += einsum(t2.aaaa, (0, 1, 2, 3), x10, (1, 4, 3, 5), (0, 4, 2, 5)) * 2.0
    x26 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x26 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x26 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x26 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3))
    x26 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x26, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x26, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_aaaa += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new_aaaa += einsum(x26, (0, 1, 2, 3), (1, 0, 3, 2))
    x27 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x27 += einsum(f.aa.oo, (0, 1), t2.aaaa, (2, 1, 3, 4), (0, 2, 3, 4))
    x28 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x28 += einsum(x11, (0, 1), (0, 1))
    x28 += einsum(x12, (0, 1), (0, 1)) * 2.0
    x29 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x29 += einsum(x28, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x30 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x30 += einsum(x27, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x30 += einsum(x29, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x30, (0, 1, 2, 3), (1, 0, 2, 3))
    x31 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x31 += einsum(t2.aaaa, (0, 1, 2, 3), x3, (1, 4, 5, 3), (0, 4, 2, 5))
    x32 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x32 += einsum(t2.aaaa, (0, 1, 2, 3), x31, (4, 1, 5, 3), (0, 4, 2, 5)) * -4.0
    x33 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x33 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x34 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x34 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x35 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x35 += einsum(x33, (0, 1), (0, 1))
    x35 += einsum(x34, (0, 1), (0, 1)) * 2.0
    x36 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x36 += einsum(x35, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 4, 0)) * -2.0
    x37 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x37 += einsum(x32, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x37 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x37, (0, 1, 2, 3), (0, 1, 3, 2))
    x38 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x38 += einsum(f.aa.vv, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4))
    x39 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x39 += einsum(t2.abab, (0, 1, 2, 3), x7, (1, 4, 3, 5), (4, 5, 0, 2))
    x40 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x40 += einsum(t2.abab, (0, 1, 2, 3), x39, (1, 3, 4, 5), (0, 4, 2, 5)) * -1.0
    x41 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x41 += einsum(x38, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x41 += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x41, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_aaaa += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3))
    x42 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x42 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x42 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 3, 5, 2), (4, 0, 5, 1)) * -1.0
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), x42, (0, 4, 1, 5), (4, 5, 2, 3)) * 2.0
    x43 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x43 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x43 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x44 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x44 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x44 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x44 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (4, 0, 5, 2))
    x44 += einsum(t2.aaaa, (0, 1, 2, 3), x43, (1, 4, 3, 5), (4, 0, 5, 2)) * -2.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x44, (0, 4, 2, 5), (4, 1, 5, 3))
    x45 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x45 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x45 += einsum(x22, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x45 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_abab += einsum(t2.bbbb, (0, 1, 2, 3), x45, (1, 3, 4, 5), (4, 0, 5, 2)) * 2.0
    x46 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x46 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x46 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 5, 3), (5, 1, 4, 2)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x46, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x47 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x47 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x47 += einsum(x33, (0, 1), (1, 0))
    x47 += einsum(x34, (0, 1), (1, 0)) * 2.0
    t2new_abab += einsum(x47, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x48 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x48 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x49 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x49 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x50 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x50 += einsum(f.bb.vv, (0, 1), (0, 1)) * -0.5
    x50 += einsum(x48, (0, 1), (1, 0))
    x50 += einsum(x49, (0, 1), (1, 0)) * 0.5
    t2new_abab += einsum(x50, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x51 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x51 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x51 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (5, 1, 4, 0))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x51, (1, 4, 0, 5), (5, 4, 2, 3))
    x52 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x52 += einsum(t2.bbbb, (0, 1, 2, 3), x7, (1, 4, 3, 5), (4, 0, 5, 2))
    x53 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x53 += einsum(t2.bbbb, (0, 1, 2, 3), x52, (1, 4, 3, 5), (0, 4, 2, 5)) * -4.0
    x54 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(t2.abab, (0, 1, 2, 3), x3, (0, 4, 5, 2), (1, 3, 4, 5))
    x55 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x55 += einsum(t2.abab, (0, 1, 2, 3), x54, (4, 5, 0, 2), (1, 4, 3, 5)) * -1.0
    x56 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x56 += einsum(x48, (0, 1), (0, 1))
    x56 += einsum(x49, (0, 1), (0, 1)) * 0.5
    x57 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x57 += einsum(x56, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 4, 0)) * -4.0
    x58 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x58 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x58 += einsum(x55, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x58 += einsum(x57, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2))
    x59 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x59 += einsum(f.bb.oo, (0, 1), t2.bbbb, (2, 1, 3, 4), (0, 2, 3, 4))
    x60 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x60 += einsum(x17, (0, 1), (0, 1))
    x60 += einsum(x18, (0, 1), (0, 1)) * 0.5
    x61 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x61 += einsum(x60, (0, 1), t2.bbbb, (2, 1, 3, 4), (2, 0, 3, 4)) * -4.0
    x62 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x62 += einsum(x59, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x62 += einsum(x61, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x62, (0, 1, 2, 3), (1, 0, 2, 3))
    x63 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x63 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x64 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x64 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x65 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x65 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x66 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x66 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x66 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x66 += einsum(x65, (0, 1, 2, 3), (1, 0, 3, 2))
    x67 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x67 += einsum(t2.bbbb, (0, 1, 2, 3), x66, (1, 4, 3, 5), (0, 4, 2, 5)) * 2.0
    x68 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x68 += einsum(x63, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x68 += einsum(x64, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x68 += einsum(x65, (0, 1, 2, 3), (0, 1, 2, 3))
    x68 += einsum(x67, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x68, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x68, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_bbbb += einsum(x68, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new_bbbb += einsum(x68, (0, 1, 2, 3), (1, 0, 3, 2))
    x69 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x69 += einsum(f.bb.vv, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4))
    x70 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x70 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x70 += einsum(x69, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    t2new_bbbb += einsum(x70, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_bbbb += einsum(x70, (0, 1, 2, 3), (0, 1, 2, 3))
    x71 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x71 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x71 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 2, 5, 3), (4, 0, 5, 1))
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), x71, (0, 4, 1, 5), (4, 5, 2, 3)) * 2.0

    t1new.aa = t1new_aa
    t1new.bb = t1new_bb
    t2new.aaaa = t2new_aaaa
    t2new.abab = t2new_abab
    t2new.bbbb = t2new_bbbb

    return {"t1new": t1new, "t2new": t2new}

