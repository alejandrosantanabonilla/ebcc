# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 3), ())
    e_cc += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 3, 1, 2), ()) * -1.0
    e_cc += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 2), ()) * -1.0
    x0 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x0 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x0 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x1 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x1 += einsum(f.bb.ov, (0, 1), (0, 1))
    x1 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    x1 += einsum(t1.bb, (0, 1), x0, (0, 2, 3, 1), (2, 3)) * -0.5
    e_cc += einsum(t1.bb, (0, 1), x1, (0, 1), ())
    x2 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x2 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x2 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x3 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(f.aa.ov, (0, 1), (0, 1)) * 2.0
    x3 += einsum(t1.aa, (0, 1), x2, (0, 2, 1, 3), (2, 3)) * -1.0
    e_cc += einsum(t1.aa, (0, 1), x3, (0, 1), ()) * 0.5

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    t1new = Namespace()
    t2new = Namespace()
    t3new = Namespace()

    # T amplitudes
    t1new_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    t1new_bb += einsum(f.bb.ov, (0, 1), (0, 1))
    t1new_bb += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 0, 2, 5, 1, 3), (4, 5)) * 3.0
    t1new_bb += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (0, 4, 2, 3, 5, 1), (4, 5)) * -1.0
    t1new_bb += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 2, 5, 1, 3), (4, 5)) * 2.0
    t1new_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    t1new_aa += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 0, 5, 3, 1), (4, 5)) * 2.0
    t1new_aa += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 0, 2, 5, 3, 1), (4, 5)) * -3.0
    t1new_aa += einsum(f.aa.ov, (0, 1), (0, 1))
    t1new_aa += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (0, 4, 2, 3, 5, 1), (4, 5)) * -1.0
    t2new_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    t2new_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    t2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    t2new_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    x0 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x0 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(x0, (0, 1), (0, 1))
    x1 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x1 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (0, 4, 2, 3))
    x2 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x2 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x2 += einsum(x1, (0, 1, 2, 3), (1, 0, 2, 3))
    t1new_bb += einsum(t2.abab, (0, 1, 2, 3), x2, (1, 4, 0, 2), (4, 3)) * -1.0
    t2new_abab += einsum(x2, (0, 1, 2, 3), t3.abaaba, (4, 0, 2, 5, 6, 3), (4, 1, 5, 6)) * -2.0
    x3 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x3 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x4 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x4 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x4 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_bb += einsum(t2.bbbb, (0, 1, 2, 3), x4, (4, 1, 0, 3), (4, 2)) * -2.0
    t2new_abab += einsum(x4, (0, 1, 2, 3), t3.babbab, (2, 4, 1, 5, 6, 3), (4, 0, 6, 5)) * -2.0
    x5 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x5 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x5 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3)) * 0.5
    t1new_bb += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x5, (0, 4, 3, 1), (4, 2)) * -2.0
    x6 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x6 += einsum(t2.abab, (0, 1, 2, 3), (1, 3, 0, 2))
    x6 += einsum(t1.aa, (0, 1), t1.bb, (2, 3), (2, 3, 0, 1))
    t1new_bb += einsum(v.aabb.ovvv, (0, 1, 2, 3), x6, (4, 3, 0, 1), (4, 2))
    t1new_aa += einsum(v.aabb.vvov, (0, 1, 2, 3), x6, (2, 3, 4, 1), (4, 0))
    x7 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x7 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    t1new_aa += einsum(x7, (0, 1), (0, 1))
    x8 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x8 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x8 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x9 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x9 += einsum(t1.aa, (0, 1), x8, (0, 2, 1, 3), (2, 3))
    x10 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x10 += einsum(f.aa.ov, (0, 1), (0, 1))
    x10 += einsum(x7, (0, 1), (0, 1))
    x10 += einsum(x9, (0, 1), (0, 1)) * -1.0
    t1new_bb += einsum(x10, (0, 1), t2.abab, (0, 2, 1, 3), (2, 3))
    t1new_aa += einsum(x10, (0, 1), t2.aaaa, (2, 0, 3, 1), (2, 3)) * 2.0
    t2new_aaaa += einsum(x10, (0, 1), t3.aaaaaa, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5)) * 6.0
    t2new_abab += einsum(x10, (0, 1), t3.abaaba, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5)) * 2.0
    t2new_bbbb += einsum(x10, (0, 1), t3.babbab, (2, 0, 3, 4, 1, 5), (2, 3, 4, 5)) * 2.0
    x11 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x11 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x11 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x12 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x12 += einsum(t1.bb, (0, 1), x11, (0, 2, 3, 1), (2, 3))
    x13 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x13 += einsum(f.bb.ov, (0, 1), (0, 1))
    x13 += einsum(x0, (0, 1), (0, 1))
    x13 += einsum(x12, (0, 1), (0, 1)) * -1.0
    t1new_bb += einsum(x13, (0, 1), t2.bbbb, (2, 0, 3, 1), (2, 3)) * 2.0
    t1new_aa += einsum(x13, (0, 1), t2.abab, (2, 0, 3, 1), (2, 3))
    t2new_aaaa += einsum(x13, (0, 1), t3.abaaba, (2, 0, 3, 4, 1, 5), (2, 3, 4, 5)) * 2.0
    t2new_abab += einsum(x13, (0, 1), t3.babbab, (2, 3, 0, 4, 5, 1), (3, 2, 5, 4)) * 2.0
    t2new_bbbb += einsum(x13, (0, 1), t3.bbbbbb, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5)) * 6.0
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
    x20 += einsum(t1.bb, (0, 1), x13, (2, 1), (2, 0))
    x21 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x21 += einsum(f.bb.oo, (0, 1), (0, 1))
    x21 += einsum(x15, (0, 1), (1, 0))
    x21 += einsum(x16, (0, 1), (1, 0)) * 2.0
    x21 += einsum(x17, (0, 1), (1, 0))
    x21 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x21 += einsum(x20, (0, 1), (0, 1))
    t1new_bb += einsum(t1.bb, (0, 1), x21, (0, 2), (2, 1)) * -1.0
    t3new_abaaba = np.zeros((nocc[0], nocc[1], nocc[0], nvir[0], nvir[1], nvir[0]), dtype=np.float64)
    t3new_abaaba += einsum(x21, (0, 1), t3.abaaba, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -2.0
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
    t2new_abab += einsum(x24, (0, 1, 2, 3), t3.babbab, (4, 2, 0, 5, 6, 1), (3, 4, 6, 5)) * -2.0
    x25 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x25 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x26 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x26 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x26 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_aa += einsum(t2.aaaa, (0, 1, 2, 3), x26, (4, 0, 1, 3), (4, 2)) * 2.0
    t2new_abab += einsum(x26, (0, 1, 2, 3), t3.abaaba, (1, 4, 2, 5, 6, 3), (0, 4, 5, 6)) * 2.0
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
    x31 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 1, 3), (0, 4))
    x32 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x32 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x32 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x33 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x33 += einsum(t1.aa, (0, 1), x32, (0, 2, 3, 1), (2, 3))
    x34 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x34 += einsum(t1.aa, (0, 1), x10, (2, 1), (2, 0))
    x35 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x35 += einsum(f.aa.oo, (0, 1), (0, 1))
    x35 += einsum(x29, (0, 1), (1, 0))
    x35 += einsum(x30, (0, 1), (1, 0))
    x35 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x35 += einsum(x33, (0, 1), (1, 0)) * -1.0
    x35 += einsum(x34, (0, 1), (0, 1))
    t1new_aa += einsum(t1.aa, (0, 1), x35, (0, 2), (2, 1)) * -1.0
    t2new_abab += einsum(x35, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    t3new_babbab = np.zeros((nocc[1], nocc[0], nocc[1], nvir[1], nvir[0], nvir[1]), dtype=np.float64)
    t3new_babbab += einsum(x35, (0, 1), t3.babbab, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -2.0
    x36 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x36 += einsum(f.aa.vv, (0, 1), (0, 1))
    x36 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (0, 2, 3, 1), (2, 3)) * -1.0
    t1new_aa += einsum(t1.aa, (0, 1), x36, (1, 2), (0, 2))
    x37 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x37 += einsum(t1.aa, (0, 1), v.aaaa.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x38 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x38 += einsum(t1.aa, (0, 1), x37, (2, 3, 1, 4), (0, 2, 3, 4))
    x39 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x39 += einsum(v.aabb.vvov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 1), (4, 5, 6, 0))
    x40 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x40 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 0, 6, 1, 3), (4, 5, 6, 2))
    x41 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x41 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x42 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x42 += einsum(t2.aaaa, (0, 1, 2, 3), x41, (1, 4, 5, 3), (0, 4, 2, 5))
    x43 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x43 += einsum(t2.aaaa, (0, 1, 2, 3), x42, (4, 1, 5, 3), (0, 4, 2, 5)) * -4.0
    x44 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x44 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 1), (2, 3))
    x45 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x45 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x46 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x46 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x47 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x47 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x47 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x48 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x48 += einsum(t1.aa, (0, 1), x47, (0, 1, 2, 3), (2, 3))
    x49 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x49 += einsum(x44, (0, 1), (1, 0)) * -1.0
    x49 += einsum(x45, (0, 1), (1, 0))
    x49 += einsum(x46, (0, 1), (1, 0)) * 2.0
    x49 += einsum(x48, (0, 1), (1, 0)) * -1.0
    x50 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x50 += einsum(x49, (0, 1), t2.aaaa, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x51 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x51 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x52 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x52 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 1), (4, 5, 0, 6))
    x53 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 2, 6, 3, 1), (4, 5, 0, 6)) * -1.0
    x54 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(x10, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4)) * -2.0
    x55 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x55 += einsum(t1.aa, (0, 1), x25, (2, 3, 4, 1), (2, 0, 4, 3))
    x56 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x56 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x56 += einsum(x55, (0, 1, 2, 3), (3, 1, 2, 0))
    x57 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x57 += einsum(t1.aa, (0, 1), x56, (0, 2, 3, 4), (2, 3, 4, 1))
    x58 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x58 += einsum(x51, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x58 += einsum(x52, (0, 1, 2, 3), (2, 1, 0, 3)) * 2.0
    x58 += einsum(x53, (0, 1, 2, 3), (2, 1, 0, 3)) * 6.0
    x58 += einsum(x54, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x58 += einsum(x57, (0, 1, 2, 3), (1, 0, 2, 3))
    x59 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x59 += einsum(t1.aa, (0, 1), x58, (0, 2, 3, 4), (2, 3, 4, 1))
    x60 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x60 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3))
    x60 += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x60 += einsum(x40, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x60 += einsum(x43, (0, 1, 2, 3), (1, 0, 3, 2))
    x60 += einsum(x50, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x60 += einsum(x59, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_aaaa += einsum(x60, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x60, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x61 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x61 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x62 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x62 += einsum(t1.aa, (0, 1), v.aabb.vvov, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(x62, (0, 1, 2, 3), (2, 0, 3, 1))
    x63 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum(t2.abab, (0, 1, 2, 3), x62, (1, 3, 4, 5), (4, 0, 2, 5))
    x64 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x64 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x64 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -0.5
    x65 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x65 += einsum(x28, (0, 1, 2, 3), x64, (0, 4, 2, 5), (1, 4, 3, 5)) * 2.0
    x66 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x66 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2))
    x67 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x67 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x67 += einsum(x66, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x68 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum(t2.abab, (0, 1, 2, 3), x67, (1, 3, 4, 5), (4, 0, 5, 2))
    x69 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x69 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x69 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x70 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum(t1.aa, (0, 1), x69, (2, 3, 1, 4), (2, 0, 3, 4))
    x71 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum(t2.aaaa, (0, 1, 2, 3), x70, (1, 4, 3, 5), (0, 4, 2, 5)) * -2.0
    x72 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x72 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x73 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x73 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x74 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x74 += einsum(t1.aa, (0, 1), x73, (2, 3, 4, 0), (2, 4, 3, 1))
    x75 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x75 += einsum(t1.aa, (0, 1), x61, (2, 3, 1, 4), (0, 2, 3, 4))
    x76 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x76 += einsum(t2.abab, (0, 1, 2, 3), x23, (1, 3, 4, 5), (4, 0, 5, 2))
    x77 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x77 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x77 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x78 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x78 += einsum(t2.aaaa, (0, 1, 2, 3), x77, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x79 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x79 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    x79 += einsum(x25, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x80 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x80 += einsum(t2.aaaa, (0, 1, 2, 3), x79, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x81 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x81 += einsum(x72, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x81 += einsum(x74, (0, 1, 2, 3), (0, 2, 1, 3))
    x81 += einsum(x75, (0, 1, 2, 3), (0, 2, 1, 3))
    x81 += einsum(x76, (0, 1, 2, 3), (0, 2, 1, 3))
    x81 += einsum(x78, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x81 += einsum(x80, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x82 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x82 += einsum(t1.aa, (0, 1), x81, (2, 0, 3, 4), (2, 3, 4, 1))
    x83 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x83 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3))
    x83 += einsum(x63, (0, 1, 2, 3), (0, 1, 2, 3))
    x83 += einsum(x65, (0, 1, 2, 3), (1, 0, 3, 2))
    x83 += einsum(x68, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x83 += einsum(x71, (0, 1, 2, 3), (1, 0, 2, 3))
    x83 += einsum(x82, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x83, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x83, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x83, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x84 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x84 += einsum(f.aa.vv, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4))
    x85 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x85 += einsum(t2.abab, (0, 1, 2, 3), x11, (1, 4, 5, 3), (4, 5, 0, 2))
    x86 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x86 += einsum(t2.abab, (0, 1, 2, 3), x85, (1, 3, 4, 5), (4, 0, 5, 2)) * -1.0
    x87 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x87 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x87 += einsum(x84, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x87 += einsum(x86, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_aaaa += einsum(x87, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_aaaa += einsum(x87, (0, 1, 2, 3), (0, 1, 2, 3))
    x88 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x88 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x89 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x89 += einsum(v.aabb.ooov, (0, 1, 2, 3), t3.abaaba, (4, 2, 1, 5, 3, 6), (4, 0, 5, 6))
    x90 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x90 += einsum(v.aaaa.ooov, (0, 1, 2, 3), t3.aaaaaa, (4, 1, 2, 5, 6, 3), (4, 0, 5, 6))
    x91 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x91 += einsum(t2.aaaa, (0, 1, 2, 3), x73, (4, 5, 1, 0), (4, 5, 2, 3)) * -1.0
    x92 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x92 += einsum(x23, (0, 1, 2, 3), t3.abaaba, (4, 0, 3, 5, 1, 6), (2, 4, 5, 6))
    x93 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x93 += einsum(x25, (0, 1, 2, 3), t3.aaaaaa, (4, 2, 1, 5, 6, 3), (0, 4, 5, 6))
    x94 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x94 += einsum(f.aa.oo, (0, 1), (0, 1))
    x94 += einsum(x34, (0, 1), (1, 0))
    x95 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x95 += einsum(x94, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x96 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x96 += einsum(x29, (0, 1), (1, 0))
    x96 += einsum(x30, (0, 1), (1, 0))
    x96 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x96 += einsum(x33, (0, 1), (1, 0)) * -1.0
    x97 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x97 += einsum(x96, (0, 1), t2.aaaa, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x98 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x98 += einsum(x88, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x98 += einsum(x89, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x98 += einsum(x90, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    x98 += einsum(x91, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x98 += einsum(x92, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x98 += einsum(x93, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.0
    x98 += einsum(x95, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x98 += einsum(x97, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x98, (0, 1, 2, 3), (1, 0, 2, 3))
    x99 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x99 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x99 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    x100 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x100 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x99, (4, 5, 3, 1), (0, 2, 4, 5))
    x101 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x101 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x101 += einsum(x100, (0, 1, 2, 3), (1, 3, 0, 2))
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), x101, (0, 4, 1, 5), (4, 5, 2, 3)) * -2.0
    x102 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x102 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x103 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum(t1.aa, (0, 1), x102, (2, 3, 0, 4), (2, 3, 4, 1)) * -2.0
    x103 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x103 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    t2new_aaaa += einsum(t1.aa, (0, 1), x103, (2, 3, 0, 4), (2, 3, 1, 4))
    x104 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x104 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 0, 4), (2, 1, 3, 4))
    x105 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x105 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x105 += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_abab += einsum(x105, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 2, 6, 3), (5, 4, 6, 1)) * 2.0
    x106 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x106 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 4), (1, 4, 2, 3))
    x107 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x107 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x107 += einsum(x106, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new_abab += einsum(x107, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 0, 3), (4, 5, 6, 1)) * 2.0
    x108 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x108 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 2, 3, 4), (3, 4, 1, 2))
    x109 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x109 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1))
    x109 += einsum(x108, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_abab += einsum(x109, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 2, 1), (5, 4, 3, 6)) * 2.0
    x110 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x110 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 0, 4), (2, 1, 3, 4))
    x111 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x111 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x111 += einsum(x110, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_abab += einsum(x111, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 3, 6, 2), (4, 5, 1, 6)) * -2.0
    x112 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x112 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x113 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x113 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -0.5
    x114 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x114 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x114 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x115 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x115 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x115 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x115 += einsum(x112, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x115 += einsum(x11, (0, 1, 2, 3), x113, (0, 4, 3, 5), (1, 4, 2, 5)) * -1.0
    x115 += einsum(t1.bb, (0, 1), x114, (2, 1, 3, 4), (2, 0, 4, 3)) * -0.5
    x115 += einsum(t1.bb, (0, 1), x18, (2, 3, 0, 4), (3, 2, 4, 1)) * -0.5
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x115, (1, 4, 3, 5), (0, 4, 2, 5)) * 2.0
    x116 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x116 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x116 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x117 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x117 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x117 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x117 += einsum(x41, (0, 1, 2, 3), x64, (0, 4, 2, 5), (1, 4, 3, 5)) * -2.0
    x117 += einsum(t1.aa, (0, 1), x116, (2, 1, 3, 4), (2, 0, 4, 3)) * -1.0
    x117 += einsum(t1.aa, (0, 1), x77, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x117, (0, 4, 2, 5), (4, 1, 5, 3)) * -1.0
    x118 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x118 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 4), (1, 4, 2, 3))
    x119 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x119 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x120 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x120 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x120 += einsum(x118, (0, 1, 2, 3), (1, 0, 3, 2))
    x120 += einsum(x119, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x120 += einsum(v.aabb.ovov, (0, 1, 2, 3), x6, (2, 4, 5, 1), (3, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x120, (3, 4, 0, 5), (5, 1, 2, 4))
    x121 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x121 += einsum(t1.aa, (0, 1), v.aabb.ooov, (2, 0, 3, 4), (3, 4, 2, 1))
    x122 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x122 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x122 += einsum(x121, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x122 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3))
    x122 += einsum(v.aabb.ovov, (0, 1, 2, 3), x64, (0, 4, 1, 5), (2, 3, 4, 5)) * 2.0
    t2new_abab += einsum(t2.bbbb, (0, 1, 2, 3), x122, (1, 3, 4, 5), (4, 0, 5, 2)) * 2.0
    x123 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x123 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x123 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -1.0
    x124 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x124 += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x125 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x125 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x125 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    x125 += einsum(t1.bb, (0, 1), x2, (0, 2, 3, 4), (2, 1, 3, 4)) * -1.0
    t2new_abab += einsum(x123, (0, 1, 2, 3), x125, (4, 5, 0, 2), (1, 4, 3, 5))
    x126 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x126 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 4, 1), (0, 4, 2, 3))
    x127 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x127 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x127 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3))
    x128 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x128 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x128 += einsum(x126, (0, 1, 2, 3), (1, 0, 3, 2))
    x128 += einsum(t1.aa, (0, 1), x127, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x128, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x129 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x129 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 4), (1, 4, 2, 3))
    x130 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x130 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 2, 3, 4), (3, 4, 1, 2))
    x131 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x131 += einsum(v.aabb.vvvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x131 += einsum(x129, (0, 1, 2, 3), (1, 0, 3, 2))
    x131 += einsum(x130, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x131, (3, 4, 2, 5), (0, 1, 5, 4)) * -1.0
    x132 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x132 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 4, 1), (0, 4, 2, 3))
    x133 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x133 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x134 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x134 += einsum(v.aabb.ovov, (0, 1, 2, 3), x6, (4, 3, 5, 1), (4, 2, 5, 0))
    x135 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x135 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x135 += einsum(x132, (0, 1, 2, 3), (1, 0, 3, 2))
    x135 += einsum(x133, (0, 1, 2, 3), (1, 0, 3, 2))
    x135 += einsum(x134, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x135, (1, 4, 0, 5), (5, 4, 2, 3))
    x136 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x136 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 1, 2, 3), (2, 3))
    x137 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x137 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 4, 1, 3), (2, 4))
    x138 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x138 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x139 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x139 += einsum(t1.bb, (0, 1), x114, (0, 1, 2, 3), (2, 3)) * 0.5
    x140 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x140 += einsum(t1.bb, (0, 1), x13, (0, 2), (2, 1)) * 0.5
    x141 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x141 += einsum(f.bb.vv, (0, 1), (0, 1)) * -0.5
    x141 += einsum(x136, (0, 1), (1, 0)) * -0.5
    x141 += einsum(x137, (0, 1), (1, 0))
    x141 += einsum(x138, (0, 1), (1, 0)) * 0.5
    x141 += einsum(x139, (0, 1), (1, 0)) * -1.0
    x141 += einsum(x140, (0, 1), (0, 1))
    t2new_abab += einsum(x141, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    t3new_abaaba += einsum(x141, (0, 1), t3.abaaba, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * -4.0
    x142 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x142 += einsum(t1.aa, (0, 1), x10, (0, 2), (2, 1))
    x143 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x143 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x143 += einsum(x44, (0, 1), (1, 0)) * -1.0
    x143 += einsum(x45, (0, 1), (1, 0))
    x143 += einsum(x46, (0, 1), (1, 0)) * 2.0
    x143 += einsum(x48, (0, 1), (1, 0)) * -1.0
    x143 += einsum(x142, (0, 1), (0, 1))
    t2new_abab += einsum(x143, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    t3new_babbab += einsum(x143, (0, 1), t3.babbab, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * -2.0
    x144 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x144 += einsum(f.bb.oo, (0, 1), (0, 1)) * 0.5
    x144 += einsum(x15, (0, 1), (1, 0)) * 0.5
    x144 += einsum(x16, (0, 1), (1, 0))
    x144 += einsum(x17, (0, 1), (1, 0)) * 0.5
    x144 += einsum(t1.bb, (0, 1), x18, (2, 3, 0, 1), (3, 2)) * -0.5
    x144 += einsum(t1.bb, (0, 1), x13, (2, 1), (2, 0)) * 0.5
    t2new_abab += einsum(x144, (0, 1), t2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x145 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x145 += einsum(t1.aa, (0, 1), v.aabb.vvoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x146 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x146 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x146 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3))
    x147 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x147 += einsum(t1.bb, (0, 1), x146, (2, 1, 3, 4), (2, 0, 3, 4))
    x148 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x148 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (1, 5, 0, 4))
    x149 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x149 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x149 += einsum(x132, (0, 1, 2, 3), (0, 1, 3, 2))
    x149 += einsum(x148, (0, 1, 2, 3), (0, 1, 3, 2))
    x150 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x150 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x150 += einsum(x145, (0, 1, 2, 3), (1, 0, 2, 3))
    x150 += einsum(x147, (0, 1, 2, 3), (0, 1, 2, 3))
    x150 += einsum(t1.aa, (0, 1), x149, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t1.bb, (0, 1), x150, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    x151 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x151 += einsum(t1.aa, (0, 1), v.aabb.vvvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x152 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x152 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x152 += einsum(x151, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_abab += einsum(t1.bb, (0, 1), x152, (1, 2, 3, 4), (3, 0, 4, 2))
    x153 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x153 += einsum(t1.bb, (0, 1), v.aabb.oovv, (2, 3, 4, 1), (0, 4, 2, 3))
    x154 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x154 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x154 += einsum(x153, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_abab += einsum(t1.aa, (0, 1), x154, (2, 3, 0, 4), (4, 2, 1, 3)) * -1.0
    x155 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x155 += einsum(t1.bb, (0, 1), v.bbbb.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x156 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x156 += einsum(t1.bb, (0, 1), x155, (2, 3, 1, 4), (0, 2, 3, 4))
    x157 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x157 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 1, 3), (4, 5, 6, 2))
    x158 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x158 += einsum(v.aabb.ovvv, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 3), (4, 5, 6, 2))
    x159 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x159 += einsum(t2.bbbb, (0, 1, 2, 3), x11, (1, 4, 5, 3), (4, 0, 5, 2))
    x160 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x160 += einsum(t2.bbbb, (0, 1, 2, 3), x159, (1, 4, 3, 5), (4, 0, 5, 2)) * -4.0
    x161 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x161 += einsum(t2.abab, (0, 1, 2, 3), x8, (0, 4, 2, 5), (1, 3, 4, 5))
    x162 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x162 += einsum(t2.abab, (0, 1, 2, 3), x161, (4, 5, 0, 2), (4, 1, 5, 3)) * -1.0
    x163 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x163 += einsum(t1.bb, (0, 1), x114, (0, 1, 2, 3), (2, 3))
    x164 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x164 += einsum(x136, (0, 1), (1, 0)) * -1.0
    x164 += einsum(x137, (0, 1), (1, 0)) * 2.0
    x164 += einsum(x138, (0, 1), (1, 0))
    x164 += einsum(x163, (0, 1), (1, 0)) * -1.0
    x165 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x165 += einsum(x164, (0, 1), t2.bbbb, (2, 3, 4, 0), (2, 3, 1, 4)) * -2.0
    x166 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x166 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x167 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x167 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 2, 6, 1, 3), (4, 5, 0, 6))
    x168 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x168 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 3), (4, 5, 2, 6))
    x169 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x169 += einsum(x13, (0, 1), t2.bbbb, (2, 3, 4, 1), (0, 2, 3, 4)) * -2.0
    x170 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x170 += einsum(t1.bb, (0, 1), x3, (2, 3, 4, 1), (2, 0, 4, 3))
    x171 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x171 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x171 += einsum(x170, (0, 1, 2, 3), (3, 1, 2, 0))
    x172 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x172 += einsum(t1.bb, (0, 1), x171, (0, 2, 3, 4), (2, 3, 4, 1))
    x173 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x173 += einsum(x166, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x173 += einsum(x167, (0, 1, 2, 3), (2, 1, 0, 3)) * 6.0
    x173 += einsum(x168, (0, 1, 2, 3), (2, 1, 0, 3)) * 2.0
    x173 += einsum(x169, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x173 += einsum(x172, (0, 1, 2, 3), (1, 0, 2, 3))
    x174 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x174 += einsum(t1.bb, (0, 1), x173, (0, 2, 3, 4), (2, 3, 4, 1))
    x175 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x175 += einsum(x156, (0, 1, 2, 3), (0, 1, 2, 3))
    x175 += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x175 += einsum(x158, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x175 += einsum(x160, (0, 1, 2, 3), (1, 0, 3, 2))
    x175 += einsum(x162, (0, 1, 2, 3), (1, 0, 3, 2))
    x175 += einsum(x165, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x175 += einsum(x174, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_bbbb += einsum(x175, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x175, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x176 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x176 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x177 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x177 += einsum(v.bbbb.ooov, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 1, 5, 6, 3), (4, 0, 5, 6)) * -1.0
    x178 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x178 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x179 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x179 += einsum(t2.bbbb, (0, 1, 2, 3), x178, (4, 5, 0, 1), (4, 5, 2, 3))
    x180 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x180 += einsum(v.aabb.ovoo, (0, 1, 2, 3), t3.babbab, (4, 0, 3, 5, 1, 6), (4, 2, 5, 6))
    x181 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x181 += einsum(x3, (0, 1, 2, 3), t3.bbbbbb, (4, 1, 2, 5, 6, 3), (0, 4, 5, 6)) * -1.0
    x182 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x182 += einsum(x1, (0, 1, 2, 3), t3.babbab, (4, 2, 1, 5, 3, 6), (0, 4, 5, 6))
    x183 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x183 += einsum(f.bb.oo, (0, 1), (0, 1))
    x183 += einsum(x20, (0, 1), (1, 0))
    x184 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x184 += einsum(x183, (0, 1), t2.bbbb, (2, 1, 3, 4), (0, 2, 3, 4)) * -2.0
    x185 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x185 += einsum(x15, (0, 1), (1, 0))
    x185 += einsum(x16, (0, 1), (1, 0)) * 2.0
    x185 += einsum(x17, (0, 1), (1, 0))
    x185 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x186 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x186 += einsum(x185, (0, 1), t2.bbbb, (2, 0, 3, 4), (1, 2, 3, 4)) * -2.0
    x187 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x187 += einsum(x176, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x187 += einsum(x177, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    x187 += einsum(x179, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x187 += einsum(x180, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x187 += einsum(x181, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.0
    x187 += einsum(x182, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x187 += einsum(x184, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x187 += einsum(x186, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_bbbb += einsum(x187, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x187, (0, 1, 2, 3), (1, 0, 2, 3))
    x188 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x188 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x189 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x189 += einsum(t2.abab, (0, 1, 2, 3), x124, (4, 5, 0, 2), (4, 1, 3, 5))
    x190 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x190 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x190 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x190 += einsum(x112, (0, 1, 2, 3), (1, 0, 3, 2))
    x191 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x191 += einsum(t2.bbbb, (0, 1, 2, 3), x190, (1, 4, 3, 5), (4, 0, 5, 2)) * 2.0
    x192 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x192 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x192 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x193 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x193 += einsum(t1.bb, (0, 1), x192, (2, 3, 1, 4), (2, 0, 3, 4))
    x194 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x194 += einsum(t2.bbbb, (0, 1, 2, 3), x193, (1, 4, 3, 5), (4, 0, 5, 2)) * -2.0
    x195 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x195 += einsum(t1.bb, (0, 1), x178, (2, 3, 4, 0), (2, 4, 3, 1))
    x196 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x196 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovoo, (0, 2, 4, 5), (1, 4, 5, 3))
    x197 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x197 += einsum(t2.abab, (0, 1, 2, 3), x1, (4, 5, 0, 2), (4, 1, 5, 3))
    x198 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x198 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x198 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x199 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x199 += einsum(t2.bbbb, (0, 1, 2, 3), x198, (1, 4, 5, 3), (4, 5, 0, 2)) * 2.0
    x200 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x200 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    x200 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x201 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x201 += einsum(t2.bbbb, (0, 1, 2, 3), x200, (4, 5, 1, 3), (4, 5, 0, 2)) * 2.0
    x202 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x202 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x202 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x202 += einsum(x188, (0, 1, 2, 3), (0, 1, 2, 3))
    x203 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x203 += einsum(t1.bb, (0, 1), x202, (2, 3, 1, 4), (2, 3, 0, 4))
    x204 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x204 += einsum(x195, (0, 1, 2, 3), (0, 2, 1, 3))
    x204 += einsum(x196, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x204 += einsum(x197, (0, 1, 2, 3), (0, 2, 1, 3))
    x204 += einsum(x199, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x204 += einsum(x201, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x204 += einsum(x203, (0, 1, 2, 3), (2, 1, 0, 3))
    x205 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x205 += einsum(t1.bb, (0, 1), x204, (2, 0, 3, 4), (2, 3, 4, 1))
    x206 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x206 += einsum(x188, (0, 1, 2, 3), (0, 1, 2, 3))
    x206 += einsum(x112, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x206 += einsum(x189, (0, 1, 2, 3), (0, 1, 2, 3))
    x206 += einsum(x191, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x206 += einsum(x194, (0, 1, 2, 3), (0, 1, 3, 2))
    x206 += einsum(x205, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x206, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x206, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x206, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x206, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x207 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x207 += einsum(f.bb.vv, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4))
    x208 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x208 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x208 += einsum(x207, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    t2new_bbbb += einsum(x208, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_bbbb += einsum(x208, (0, 1, 2, 3), (0, 1, 2, 3))
    x209 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x209 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x210 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x210 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x210 += einsum(x209, (0, 1, 2, 3), (3, 1, 2, 0))
    x210 += einsum(x170, (0, 1, 2, 3), (3, 1, 2, 0))
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), x210, (0, 4, 1, 5), (4, 5, 2, 3)) * 2.0
    x211 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x211 += einsum(t1.bb, (0, 1), x209, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    x211 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x211 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    t2new_bbbb += einsum(t1.bb, (0, 1), x211, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x212 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x212 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 0, 5, 3, 6), (4, 5, 6, 1))
    x213 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x213 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x214 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x214 += einsum(x212, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x214 += einsum(x213, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    x215 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x215 += einsum(t2.aaaa, (0, 1, 2, 3), x214, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6)) * -4.0
    x216 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x216 += einsum(v.aabb.ooov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 7), (4, 5, 0, 1, 6, 7))
    x217 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x217 += einsum(x32, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 0, 6, 7, 3), (4, 5, 1, 2, 6, 7)) * 3.0
    x218 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x218 += einsum(x216, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x218 += einsum(x217, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x219 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x219 += einsum(t1.aa, (0, 1), x218, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x220 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x220 += einsum(x215, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    x220 += einsum(x219, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new_aaaaaa += einsum(x220, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    x221 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x221 += einsum(x62, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 1, 7), (2, 4, 5, 6, 7, 3))
    x222 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x222 += einsum(t2.aaaa, (0, 1, 2, 3), x25, (4, 0, 1, 5), (4, 2, 3, 5))
    x223 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x223 += einsum(t2.aaaa, (0, 1, 2, 3), x222, (4, 5, 6, 3), (4, 0, 1, 5, 6, 2)) * -1.0
    x224 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x224 += einsum(x70, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 0, 6, 7, 2), (4, 5, 1, 6, 7, 3)) * -6.0
    x225 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x225 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3))
    x225 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x226 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x226 += einsum(t2.aaaa, (0, 1, 2, 3), x225, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6)) * -4.0
    x227 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x227 += einsum(x221, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 2.0
    x227 += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -4.0
    x227 += einsum(x224, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    x227 += einsum(x226, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    t3new_aaaaaa += einsum(x227, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x228 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x228 += einsum(v.aaaa.oooo, (0, 1, 2, 3), t3.aaaaaa, (4, 3, 1, 5, 6, 7), (4, 0, 2, 5, 6, 7)) * -1.0
    x229 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x229 += einsum(f.aa.oo, (0, 1), (0, 1))
    x229 += einsum(x30, (0, 1), (1, 0))
    x229 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x229 += einsum(x34, (0, 1), (0, 1))
    x230 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x230 += einsum(x229, (0, 1), t3.aaaaaa, (2, 3, 0, 4, 5, 6), (2, 3, 1, 4, 5, 6)) * 6.0
    x231 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x231 += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * 6.0
    x231 += einsum(x230, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3))
    t3new_aaaaaa += einsum(x231, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x231, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x231, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x232 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x232 += einsum(v.aaaa.vvvv, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 6, 7, 3, 1), (4, 5, 6, 7, 0, 2)) * -1.0
    x233 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x233 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x233 += einsum(x45, (0, 1), (1, 0))
    x233 += einsum(x46, (0, 1), (1, 0)) * 2.0
    x233 += einsum(x142, (0, 1), (0, 1))
    x234 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x234 += einsum(x233, (0, 1), t3.aaaaaa, (2, 3, 4, 5, 6, 0), (2, 3, 4, 5, 6, 1)) * 6.0
    x235 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x235 += einsum(x232, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    x235 += einsum(x234, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x235, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x235, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x235, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x236 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x236 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 4, 2, 5))
    x237 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x237 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0000000000000204
    x237 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -1.0
    x238 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x238 += einsum(x237, (0, 1, 2, 3), x41, (0, 4, 5, 2), (4, 1, 5, 3)) * 0.9999999999999901
    x239 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x239 += einsum(x236, (0, 1, 2, 3), (0, 1, 2, 3))
    x239 += einsum(x238, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x240 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x240 += einsum(x239, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 1, 6, 7, 3), (4, 5, 0, 6, 7, 2)) * 6.0000000000000595
    x241 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x241 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x241 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -0.499999999999995
    x242 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x242 += einsum(v.aabb.ovov, (0, 1, 2, 3), x241, (0, 4, 1, 5), (2, 3, 4, 5))
    x243 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x243 += einsum(x242, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 1, 7), (4, 5, 2, 6, 7, 3)) * 4.00000000000004
    x244 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x244 += einsum(x240, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    x244 += einsum(x243, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3))
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new_aaaaaa += einsum(x244, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    x245 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x245 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 5, 1, 3), (0, 2, 4, 5))
    x246 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x246 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x246 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x247 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x247 += einsum(t2.aaaa, (0, 1, 2, 3), x246, (1, 4, 3, 5), (0, 2, 4, 5)) * 2.0
    x248 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x248 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x248 += einsum(x245, (0, 1, 2, 3), (0, 1, 3, 2))
    x248 += einsum(x247, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x249 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x249 += einsum(t2.aaaa, (0, 1, 2, 3), x248, (4, 5, 3, 6), (0, 1, 4, 2, 5, 6)) * -2.0
    x250 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x250 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x251 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x251 += einsum(t1.aa, (0, 1), x250, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x252 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x252 += einsum(t2.aaaa, (0, 1, 2, 3), x41, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x253 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x253 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x253 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x253 += einsum(x236, (0, 1, 2, 3), (0, 1, 2, 3))
    x253 += einsum(x252, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x254 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x254 += einsum(t2.aaaa, (0, 1, 2, 3), x253, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6)) * -1.0
    x255 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x255 += einsum(x251, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x255 += einsum(x254, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x256 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x256 += einsum(t1.aa, (0, 1), x255, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x257 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x257 += einsum(x249, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    x257 += einsum(x256, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_aaaaaa += einsum(x257, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x258 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x258 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x258 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -1.0
    x259 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x259 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x258, (4, 5, 3, 1), (0, 2, 4, 5))
    x260 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x260 += einsum(x259, (0, 1, 2, 3), t3.aaaaaa, (4, 1, 0, 5, 6, 7), (4, 3, 2, 5, 6, 7)) * 6.0
    x261 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x261 += einsum(x29, (0, 1), (1, 0))
    x261 += einsum(x33, (0, 1), (1, 0)) * -1.0
    x262 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x262 += einsum(x261, (0, 1), t3.aaaaaa, (2, 3, 0, 4, 5, 6), (2, 3, 1, 4, 5, 6)) * 6.0
    x263 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x263 += einsum(x260, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    x263 += einsum(x262, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x263, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_aaaaaa += einsum(x263, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x263, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x264 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x264 += einsum(t1.aa, (0, 1), x116, (0, 1, 2, 3), (2, 3))
    x265 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x265 += einsum(x44, (0, 1), (1, 0))
    x265 += einsum(x264, (0, 1), (1, 0)) * -1.0
    x266 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x266 += einsum(x265, (0, 1), t3.aaaaaa, (2, 3, 4, 5, 6, 0), (2, 3, 4, 5, 6, 1)) * 6.0
    x267 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x267 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 6, 7, 3, 1), (4, 5, 6, 0, 2, 7)) * -1.0
    x268 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x268 += einsum(x99, (0, 1, 2, 3), x267, (4, 5, 6, 0, 1, 7), (4, 5, 6, 2, 3, 7)) * 6.0
    x269 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x269 += einsum(x266, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x269 += einsum(x268, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x269, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x269, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x269, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x270 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x270 += einsum(t2.aaaa, (0, 1, 2, 3), x37, (4, 5, 3, 6), (4, 0, 1, 2, 6, 5))
    x271 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x271 += einsum(t2.aaaa, (0, 1, 2, 3), x25, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x272 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x272 += einsum(t1.aa, (0, 1), x271, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x273 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x273 += einsum(t2.aaaa, (0, 1, 2, 3), x70, (4, 5, 3, 6), (0, 1, 5, 4, 2, 6))
    x274 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x274 += einsum(x272, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x274 += einsum(x273, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x275 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x275 += einsum(t1.aa, (0, 1), x274, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x276 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x276 += einsum(x270, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -2.0
    x276 += einsum(x275, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_aaaaaa += einsum(x276, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x277 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x277 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 7), (4, 5, 0, 6, 7, 1))
    x278 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x278 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 0, 1, 5), (4, 2, 3, 5))
    x279 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x279 += einsum(t2.aaaa, (0, 1, 2, 3), x278, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x280 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x280 += einsum(t2.aaaa, (0, 1, 2, 3), x51, (4, 5, 1, 6), (4, 5, 0, 2, 3, 6))
    x281 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x281 += einsum(x28, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 0, 6, 7, 2), (4, 5, 1, 6, 7, 3)) * 6.0
    x282 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x282 += einsum(x277, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 2.0
    x282 += einsum(x279, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -4.0
    x282 += einsum(x280, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -4.0
    x282 += einsum(x281, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x282, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x283 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x283 += einsum(x85, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 1, 7), (4, 5, 2, 6, 7, 3)) * -2.00000000000002
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new_aaaaaa += einsum(x283, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x284 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x284 += einsum(x73, (0, 1, 2, 3), t3.aaaaaa, (4, 2, 3, 5, 6, 7), (0, 4, 1, 5, 6, 7))
    t3new_aaaaaa += einsum(x284, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * 6.0
    t3new_aaaaaa += einsum(x284, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -6.0
    t3new_aaaaaa += einsum(x284, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -6.0
    t3new_aaaaaa += einsum(x284, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * 6.0
    t3new_aaaaaa += einsum(x284, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * 6.0
    t3new_aaaaaa += einsum(x284, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -6.0
    x285 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x285 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 6, 7, 1, 3), (4, 5, 6, 0, 7, 2))
    x286 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x286 += einsum(t1.aa, (0, 1), x285, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new_aaaaaa += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 6.0
    t3new_aaaaaa += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    t3new_aaaaaa += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -6.0
    t3new_aaaaaa += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * 6.0
    t3new_aaaaaa += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * 6.0
    t3new_aaaaaa += einsum(x286, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -6.0
    x287 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x287 += einsum(t1.aa, (0, 1), v.aaaa.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x288 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x288 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x289 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x289 += einsum(x287, (0, 1, 2, 3), (0, 2, 1, 3))
    x289 += einsum(x72, (0, 1, 2, 3), (0, 2, 1, 3))
    x289 += einsum(x288, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x290 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x290 += einsum(t1.aa, (0, 1), x55, (2, 3, 0, 4), (3, 2, 4, 1))
    x291 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x291 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x291 += einsum(x25, (0, 1, 2, 3), (0, 2, 1, 3))
    x292 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x292 += einsum(t2.aaaa, (0, 1, 2, 3), x291, (4, 1, 5, 3), (0, 4, 5, 2)) * 2.0
    x293 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x293 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x293 += einsum(x61, (0, 1, 2, 3), (1, 0, 2, 3))
    x294 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x294 += einsum(t1.aa, (0, 1), x293, (2, 3, 1, 4), (2, 3, 0, 4))
    x295 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x295 += einsum(v.aaaa.ooov, (0, 1, 2, 3), x64, (1, 4, 3, 5), (0, 2, 4, 5)) * 2.0
    x296 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x296 += einsum(x76, (0, 1, 2, 3), (0, 1, 2, 3))
    x296 += einsum(x290, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x296 += einsum(x292, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x296 += einsum(x294, (0, 1, 2, 3), (2, 1, 0, 3))
    x296 += einsum(x295, (0, 1, 2, 3), (2, 0, 1, 3))
    x297 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x297 += einsum(x102, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x297 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x297 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 2, 1, 3))
    x298 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x298 += einsum(t1.aa, (0, 1), x297, (2, 3, 0, 4), (2, 3, 4, 1))
    x299 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x299 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x299 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x299 += einsum(x289, (0, 1, 2, 3), (0, 1, 2, 3))
    x299 += einsum(x289, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x299 += einsum(x296, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x299 += einsum(x296, (0, 1, 2, 3), (1, 0, 2, 3))
    x299 += einsum(x74, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x299 += einsum(x74, (0, 1, 2, 3), (1, 0, 2, 3))
    x299 += einsum(x54, (0, 1, 2, 3), (2, 1, 0, 3))
    x299 += einsum(x298, (0, 1, 2, 3), (1, 0, 2, 3))
    x300 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x300 += einsum(t2.aaaa, (0, 1, 2, 3), x299, (4, 5, 1, 6), (0, 4, 5, 2, 3, 6)) * -2.0
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x300, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    x301 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x301 += einsum(t2.abab, (0, 1, 2, 3), v.bbbb.ovvv, (4, 5, 6, 3), (1, 4, 5, 6, 0, 2))
    x302 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x302 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 6, 7, 1), (5, 2, 7, 3, 4, 6))
    x303 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x303 += einsum(x124, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 7, 3), (0, 5, 7, 1, 4, 6))
    x304 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x304 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.00000000000002
    x304 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -1.0
    x305 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x305 += einsum(x11, (0, 1, 2, 3), x304, (0, 4, 3, 5), (1, 4, 2, 5))
    x306 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x306 += einsum(x112, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x306 += einsum(x305, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x307 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x307 += einsum(x306, (0, 1, 2, 3), t3.babbab, (4, 5, 1, 6, 7, 3), (4, 0, 6, 2, 5, 7)) * 2.0
    x308 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x308 += einsum(t2.abab, (0, 1, 2, 3), x8, (0, 4, 2, 5), (1, 3, 4, 5)) * 1.00000000000001
    x309 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x309 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x309 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -0.499999999999995
    x310 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x310 += einsum(v.aabb.ovov, (0, 1, 2, 3), x309, (2, 4, 3, 5), (4, 5, 0, 1)) * 2.00000000000002
    x311 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x311 += einsum(x308, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x311 += einsum(x310, (0, 1, 2, 3), (0, 1, 2, 3))
    x312 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x312 += einsum(x311, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 7, 3), (5, 0, 7, 1, 4, 6)) * 2.0
    x313 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x313 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), (0, 2, 3, 5, 1, 4))
    x313 += einsum(t1.bb, (0, 1), t2.abab, (2, 3, 4, 5), (0, 3, 5, 1, 2, 4)) * -0.5
    x314 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x314 += einsum(x14, (0, 1, 2, 3), x313, (0, 4, 2, 5, 6, 7), (1, 4, 3, 5, 6, 7)) * 2.0
    x315 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x315 += einsum(x193, (0, 1, 2, 3), x313, (0, 4, 2, 5, 6, 7), (1, 4, 3, 5, 6, 7)) * -2.0
    x316 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x316 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovoo, (0, 4, 5, 1), (5, 3, 2, 4))
    x317 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x317 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (0, 4, 5, 3), (1, 5, 2, 4))
    x318 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x318 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x319 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x319 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (0, 4, 2, 5, 6, 1), (4, 6, 5, 3)) * -1.0
    x320 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x320 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x320 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x320 += einsum(x110, (0, 1, 2, 3), (0, 2, 3, 1))
    x320 += einsum(x110, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x321 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x321 += einsum(t2.abab, (0, 1, 2, 3), x320, (0, 4, 2, 5), (1, 3, 4, 5))
    x322 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x322 += einsum(x10, (0, 1), t2.abab, (0, 2, 3, 4), (2, 4, 1, 3))
    x323 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x323 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x323 += einsum(x108, (0, 1, 2, 3), (0, 1, 2, 3))
    x323 += einsum(x316, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x323 += einsum(x317, (0, 1, 2, 3), (0, 1, 2, 3))
    x323 += einsum(x318, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x323 += einsum(x319, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x323 += einsum(x321, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x323 += einsum(x322, (0, 1, 2, 3), (0, 1, 3, 2))
    x324 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x324 += einsum(t2.abab, (0, 1, 2, 3), x323, (4, 5, 6, 2), (4, 1, 5, 3, 0, 6))
    x325 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x325 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (0, 2, 4, 5), (1, 3, 4, 5))
    x326 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x326 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x326 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x327 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x327 += einsum(t2.bbbb, (0, 1, 2, 3), x326, (1, 4, 3, 5), (0, 4, 5, 2)) * 2.0
    x328 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x328 += einsum(t1.bb, (0, 1), x3, (2, 0, 3, 4), (2, 3, 1, 4))
    x329 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x329 += einsum(t2.bbbb, (0, 1, 2, 3), x11, (1, 4, 5, 3), (4, 0, 5, 2)) * 2.0
    x330 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x330 += einsum(x328, (0, 1, 2, 3), (0, 1, 2, 3))
    x330 += einsum(x112, (0, 1, 2, 3), (0, 1, 2, 3))
    x330 += einsum(x329, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x331 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x331 += einsum(t1.bb, (0, 1), x330, (2, 0, 3, 4), (2, 3, 4, 1))
    x332 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x332 += einsum(x155, (0, 1, 2, 3), (0, 2, 1, 3))
    x332 += einsum(x325, (0, 1, 2, 3), (0, 3, 2, 1))
    x332 += einsum(x327, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x332 += einsum(x331, (0, 1, 2, 3), (0, 2, 1, 3))
    x333 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x333 += einsum(t2.abab, (0, 1, 2, 3), x332, (4, 3, 5, 6), (4, 1, 5, 6, 0, 2))
    x334 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x334 += einsum(t2.abab, (0, 1, 2, 3), v.bbbb.ooov, (4, 5, 6, 3), (1, 4, 5, 6, 0, 2))
    x335 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x335 += einsum(t1.bb, (0, 1), x334, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x336 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x336 += einsum(v.aabb.ovoo, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 6, 7, 1), (5, 2, 3, 7, 4, 6))
    x337 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x337 += einsum(x198, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 7, 3), (4, 1, 2, 6, 5, 7)) * 2.0
    x338 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x338 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (0, 2, 3, 4), (3, 4, 1, 2))
    x339 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x339 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 5, 3), (1, 5, 2, 4))
    x340 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x340 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x340 += einsum(x338, (0, 1, 2, 3), (1, 0, 3, 2))
    x340 += einsum(x339, (0, 1, 2, 3), (0, 1, 3, 2))
    x341 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x341 += einsum(t2.abab, (0, 1, 2, 3), x340, (4, 5, 2, 6), (4, 5, 1, 3, 0, 6))
    x342 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x342 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x342 += einsum(x133, (0, 1, 2, 3), (1, 0, 3, 2))
    x342 += einsum(x148, (0, 1, 2, 3), (0, 1, 3, 2))
    x343 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x343 += einsum(t2.abab, (0, 1, 2, 3), x342, (4, 5, 0, 6), (4, 5, 1, 3, 6, 2))
    x344 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x344 += einsum(t1.aa, (0, 1), x1, (2, 3, 0, 4), (2, 3, 1, 4))
    x345 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x345 += einsum(x126, (0, 1, 2, 3), (0, 1, 3, 2))
    x345 += einsum(x344, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x346 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x346 += einsum(t2.abab, (0, 1, 2, 3), x345, (4, 5, 2, 6), (4, 5, 1, 3, 0, 6))
    x347 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x347 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x347 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x348 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x348 += einsum(t1.bb, (0, 1), x347, (2, 1, 3, 4), (2, 0, 3, 4))
    x349 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x349 += einsum(t2.abab, (0, 1, 2, 3), x348, (4, 5, 6, 0), (5, 4, 1, 3, 6, 2))
    x350 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x350 += einsum(x335, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x350 += einsum(x336, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -2.0
    x350 += einsum(x337, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x350 += einsum(x341, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x350 += einsum(x343, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x350 += einsum(x346, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x350 += einsum(x349, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x351 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x351 += einsum(t1.bb, (0, 1), x350, (2, 0, 3, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    x352 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x352 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovoo, (4, 2, 5, 1), (5, 3, 0, 4))
    x353 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x353 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (4, 2, 5, 3), (1, 5, 0, 4))
    x354 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x354 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 6, 1, 3), (4, 6, 5, 0))
    x355 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x355 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 1, 6, 3), (5, 6, 4, 0))
    x356 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x356 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x356 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x356 += einsum(x25, (0, 1, 2, 3), (1, 0, 2, 3))
    x356 += einsum(x25, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x357 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x357 += einsum(t2.abab, (0, 1, 2, 3), x356, (4, 5, 0, 2), (1, 3, 4, 5))
    x358 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x358 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x358 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x358 += einsum(x352, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x358 += einsum(x353, (0, 1, 2, 3), (0, 1, 2, 3))
    x358 += einsum(x354, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x358 += einsum(x355, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x358 += einsum(x357, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x359 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x359 += einsum(t2.abab, (0, 1, 2, 3), x358, (4, 5, 6, 0), (4, 1, 5, 3, 6, 2))
    x360 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x360 += einsum(t1.bb, (0, 1), v.aabb.vvvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x361 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x361 += einsum(t1.aa, (0, 1), x124, (2, 3, 0, 4), (2, 3, 1, 4))
    x362 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x362 += einsum(t2.abab, (0, 1, 2, 3), x1, (4, 1, 0, 5), (4, 3, 2, 5))
    x363 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x363 += einsum(x360, (0, 1, 2, 3), (0, 1, 3, 2))
    x363 += einsum(x361, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x363 += einsum(x362, (0, 1, 2, 3), (0, 1, 3, 2))
    x364 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x364 += einsum(t2.abab, (0, 1, 2, 3), x363, (4, 5, 2, 6), (4, 1, 5, 3, 0, 6))
    x365 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x365 += einsum(t2.abab, (0, 1, 2, 3), x1, (4, 1, 5, 2), (4, 3, 0, 5))
    x366 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x366 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x366 += einsum(x119, (0, 1, 2, 3), (1, 0, 2, 3))
    x367 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x367 += einsum(t1.bb, (0, 1), x366, (1, 2, 3, 4), (0, 2, 3, 4))
    x368 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x368 += einsum(x365, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x368 += einsum(x367, (0, 1, 2, 3), (0, 1, 3, 2))
    x369 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x369 += einsum(t2.abab, (0, 1, 2, 3), x368, (4, 5, 0, 6), (4, 1, 5, 3, 6, 2))
    x370 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x370 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1))
    x370 += einsum(x108, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x371 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x371 += einsum(t2.bbbb, (0, 1, 2, 3), x370, (1, 3, 4, 5), (0, 2, 4, 5))
    x372 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x372 += einsum(t2.abab, (0, 1, 2, 3), x371, (4, 5, 6, 2), (4, 1, 5, 3, 0, 6)) * 2.0
    x373 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x373 += einsum(t2.bbbb, (0, 1, 2, 3), x347, (1, 3, 4, 5), (0, 2, 4, 5))
    x374 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x374 += einsum(t2.abab, (0, 1, 2, 3), x373, (4, 5, 6, 0), (4, 1, 5, 3, 6, 2)) * 2.0
    x375 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x375 += einsum(x301, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x375 += einsum(x302, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    x375 += einsum(x303, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x375 += einsum(x307, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x375 += einsum(x312, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x375 += einsum(x314, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x375 += einsum(x315, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x375 += einsum(x324, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x375 += einsum(x333, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x375 += einsum(x351, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x375 += einsum(x359, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x375 += einsum(x364, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x375 += einsum(x369, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x375 += einsum(x372, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x375 += einsum(x374, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_babbab += einsum(x375, (0, 1, 2, 3, 4, 5), (0, 4, 1, 2, 5, 3)) * -1.0
    t3new_babbab += einsum(x375, (0, 1, 2, 3, 4, 5), (0, 4, 1, 3, 5, 2))
    t3new_babbab += einsum(x375, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 5, 3))
    t3new_babbab += einsum(x375, (0, 1, 2, 3, 4, 5), (1, 4, 0, 3, 5, 2)) * -1.0
    x376 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x376 += einsum(t2.bbbb, (0, 1, 2, 3), x3, (4, 0, 1, 5), (4, 2, 3, 5))
    x377 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x377 += einsum(t2.abab, (0, 1, 2, 3), x376, (4, 5, 6, 3), (4, 1, 5, 6, 0, 2)) * -1.0
    x378 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x378 += einsum(t2.abab, (0, 1, 2, 3), (1, 3, 0, 2))
    x378 += einsum(t1.aa, (0, 1), t1.bb, (2, 3), (2, 3, 0, 1)) * 0.99999999999999
    x379 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x379 += einsum(v.aabb.ovov, (0, 1, 2, 3), x378, (4, 3, 0, 5), (2, 4, 1, 5)) * 1.00000000000001
    x380 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x380 += einsum(x126, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x380 += einsum(x379, (0, 1, 2, 3), (1, 0, 2, 3))
    x381 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x381 += einsum(x380, (0, 1, 2, 3), t3.babbab, (4, 5, 1, 6, 2, 7), (4, 0, 6, 7, 5, 3)) * -2.0
    x382 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x382 += einsum(x132, (0, 1, 2, 3), (0, 1, 3, 2))
    x382 += einsum(x134, (0, 1, 2, 3), (0, 1, 3, 2))
    x383 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x383 += einsum(x382, (0, 1, 2, 3), t3.babbab, (4, 2, 1, 5, 6, 7), (4, 0, 5, 7, 3, 6)) * -2.0
    x384 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x384 += einsum(t1.aa, (0, 1), v.aabb.oooo, (2, 0, 3, 4), (3, 4, 2, 1))
    x385 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x385 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 3, 6, 1), (4, 0, 5, 6)) * -1.0
    x386 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x386 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 6, 3, 1), (5, 2, 4, 6))
    x387 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x387 += einsum(t2.abab, (0, 1, 2, 3), x18, (4, 5, 1, 3), (4, 5, 0, 2))
    x388 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x388 += einsum(t2.abab, (0, 1, 2, 3), x24, (4, 3, 0, 5), (4, 1, 5, 2))
    x389 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x389 += einsum(t2.abab, (0, 1, 2, 3), x109, (4, 3, 2, 5), (4, 1, 0, 5))
    x390 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x390 += einsum(x13, (0, 1), t2.abab, (2, 3, 4, 1), (0, 3, 2, 4))
    x391 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x391 += einsum(v.aabb.ovoo, (0, 1, 2, 3), x64, (0, 4, 1, 5), (2, 3, 4, 5)) * 2.0
    x392 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x392 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x392 += einsum(x384, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x392 += einsum(x145, (0, 1, 2, 3), (1, 0, 2, 3))
    x392 += einsum(x385, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x392 += einsum(x386, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x392 += einsum(x387, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x392 += einsum(x388, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x392 += einsum(x389, (0, 1, 2, 3), (0, 1, 2, 3))
    x392 += einsum(x390, (0, 1, 2, 3), (0, 1, 2, 3))
    x392 += einsum(x391, (0, 1, 2, 3), (1, 0, 2, 3))
    x393 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x393 += einsum(t2.bbbb, (0, 1, 2, 3), x392, (1, 4, 5, 6), (4, 0, 2, 3, 5, 6)) * -2.0
    x394 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x394 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x394 += einsum(x338, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x395 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x395 += einsum(x394, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 2, 7), (4, 1, 6, 7, 5, 3)) * -2.0
    x396 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x396 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 0, 1, 5), (4, 2, 3, 5))
    x397 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x397 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x398 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x398 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 2, 5, 1, 6), (4, 5, 6, 3))
    x399 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x399 += einsum(x396, (0, 1, 2, 3), (0, 2, 1, 3))
    x399 += einsum(x397, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    x399 += einsum(x398, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x400 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x400 += einsum(t2.abab, (0, 1, 2, 3), x399, (4, 5, 6, 3), (4, 1, 5, 6, 0, 2)) * 2.0
    x401 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x401 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x401 += einsum(x133, (0, 1, 2, 3), (1, 0, 3, 2))
    x402 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x402 += einsum(x401, (0, 1, 2, 3), t3.babbab, (4, 2, 0, 5, 6, 7), (4, 1, 5, 7, 3, 6)) * -2.0
    x403 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x403 += einsum(f.bb.oo, (0, 1), (0, 1))
    x403 += einsum(x16, (0, 1), (0, 1)) * 2.0
    x403 += einsum(x17, (0, 1), (0, 1))
    x403 += einsum(x20, (0, 1), (1, 0))
    x404 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x404 += einsum(x403, (0, 1), t3.babbab, (2, 3, 1, 4, 5, 6), (2, 0, 4, 6, 3, 5)) * -2.0
    x405 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x405 += einsum(t1.aa, (0, 1), x132, (2, 3, 4, 0), (2, 3, 4, 1))
    x406 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x406 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x406 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3))
    x407 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x407 += einsum(t2.abab, (0, 1, 2, 3), x406, (4, 1, 5, 3), (4, 5, 0, 2))
    x408 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x408 += einsum(x1, (0, 1, 2, 3), x64, (2, 4, 3, 5), (0, 1, 4, 5)) * 2.0
    x409 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x409 += einsum(x405, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x409 += einsum(x407, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x409 += einsum(x147, (0, 1, 2, 3), (1, 0, 2, 3))
    x409 += einsum(x408, (0, 1, 2, 3), (0, 1, 2, 3))
    x410 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x410 += einsum(t2.bbbb, (0, 1, 2, 3), x409, (4, 1, 5, 6), (4, 0, 2, 3, 5, 6)) * -2.0
    x411 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x411 += einsum(x15, (0, 1), (1, 0))
    x411 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x412 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x412 += einsum(x411, (0, 1), t3.babbab, (2, 3, 0, 4, 5, 6), (2, 1, 4, 6, 3, 5)) * -2.0
    x413 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x413 += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 2.0
    x413 += einsum(x381, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x413 += einsum(x383, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x413 += einsum(x393, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x413 += einsum(x395, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x413 += einsum(x400, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x413 += einsum(x402, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x413 += einsum(x404, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x413 += einsum(x410, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x413 += einsum(x412, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    t3new_babbab += einsum(x413, (0, 1, 2, 3, 4, 5), (0, 4, 1, 2, 5, 3)) * -1.0
    t3new_babbab += einsum(x413, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 5, 3))
    x414 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x414 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 7, 1, 3), (4, 6, 2, 7, 5, 0))
    x415 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x415 += einsum(t2.abab, (0, 1, 2, 3), x414, (4, 5, 1, 6, 7, 0), (4, 5, 3, 6, 7, 2))
    x416 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x416 += einsum(v.aabb.vvvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x416 += einsum(x130, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x417 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x417 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), (0, 2, 3, 5, 1, 4))
    x417 += einsum(t1.aa, (0, 1), t2.bbbb, (2, 3, 4, 5), (2, 3, 4, 5, 0, 1))
    x418 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x418 += einsum(x416, (0, 1, 2, 3), x417, (4, 5, 0, 6, 7, 2), (4, 5, 6, 1, 7, 3)) * 2.0
    x419 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x419 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x419 += einsum(x119, (0, 1, 2, 3), (1, 0, 3, 2))
    x420 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x420 += einsum(x419, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 7, 0), (4, 5, 6, 1, 3, 7)) * -2.0
    x421 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x421 += einsum(t1.aa, (0, 1), v.aabb.oovv, (2, 0, 3, 4), (3, 4, 2, 1))
    x422 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x422 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovvv, (1, 3, 4, 5), (4, 5, 0, 2))
    x423 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x423 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 0, 5, 6, 1), (6, 3, 4, 5))
    x424 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x424 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x424 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x425 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x425 += einsum(t2.abab, (0, 1, 2, 3), x424, (1, 3, 4, 5), (4, 5, 0, 2))
    x426 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x426 += einsum(t2.abab, (0, 1, 2, 3), x24, (1, 4, 0, 5), (4, 3, 5, 2))
    x427 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x427 += einsum(t2.abab, (0, 1, 2, 3), x109, (1, 4, 2, 5), (4, 3, 0, 5))
    x428 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x428 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x428 += einsum(x421, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x428 += einsum(x422, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x428 += einsum(x423, (0, 1, 2, 3), (1, 0, 2, 3)) * -2.0
    x428 += einsum(x425, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x428 += einsum(x426, (0, 1, 2, 3), (0, 1, 2, 3))
    x428 += einsum(x427, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x429 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x429 += einsum(t2.bbbb, (0, 1, 2, 3), x428, (3, 4, 5, 6), (0, 1, 4, 2, 5, 6)) * -2.0
    x430 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x430 += einsum(v.aabb.ovov, (0, 1, 2, 3), x378, (2, 4, 5, 1), (3, 4, 0, 5))
    x431 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x431 += einsum(x118, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.99999999999999
    x431 += einsum(x430, (0, 1, 2, 3), (1, 0, 2, 3))
    x432 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x432 += einsum(x431, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 7, 1), (4, 5, 6, 0, 3, 7)) * -2.00000000000002
    x433 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x433 += einsum(t1.bb, (0, 1), x424, (0, 1, 2, 3), (2, 3))
    x434 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x434 += einsum(x136, (0, 1), (1, 0))
    x434 += einsum(x433, (0, 1), (1, 0)) * -1.0
    x435 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x435 += einsum(x434, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 0), (2, 4, 5, 1, 3, 6)) * -2.0
    x436 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x436 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 3, 7, 1), (4, 6, 0, 2, 5, 7)) * -1.0
    x437 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x437 += einsum(x109, (0, 1, 2, 3), x417, (4, 5, 1, 6, 7, 2), (0, 4, 5, 6, 7, 3))
    x438 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x438 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x438 += einsum(x121, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x438 += einsum(x66, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x439 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x439 += einsum(t2.bbbb, (0, 1, 2, 3), x438, (4, 3, 5, 6), (4, 0, 1, 2, 5, 6)) * -1.0
    x440 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x440 += einsum(f.bb.ov, (0, 1), (0, 1))
    x440 += einsum(x0, (0, 1), (0, 1))
    x441 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x441 += einsum(x440, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 1), (2, 4, 0, 5, 3, 6)) * -1.0
    x442 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x442 += einsum(x436, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x442 += einsum(x437, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x442 += einsum(x439, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x442 += einsum(x441, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x443 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x443 += einsum(t1.bb, (0, 1), x442, (0, 2, 3, 4, 5, 6), (2, 3, 4, 1, 5, 6)) * 2.0
    x444 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x444 += einsum(f.bb.vv, (0, 1), (0, 1))
    x444 += einsum(x138, (0, 1), (1, 0)) * -1.0
    x445 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x445 += einsum(x444, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 0), (2, 4, 5, 1, 3, 6)) * -2.0
    x446 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x446 += einsum(x166, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x446 += einsum(x168, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x447 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x447 += einsum(t2.abab, (0, 1, 2, 3), x446, (4, 5, 1, 6), (4, 5, 6, 3, 0, 2)) * 2.0
    x448 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x448 += einsum(x415, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x448 += einsum(x418, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x448 += einsum(x420, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    x448 += einsum(x429, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x448 += einsum(x432, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x448 += einsum(x435, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    x448 += einsum(x443, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x448 += einsum(x445, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x448 += einsum(x447, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    t3new_babbab += einsum(x448, (0, 1, 2, 3, 4, 5), (0, 4, 1, 2, 5, 3)) * -1.0
    t3new_babbab += einsum(x448, (0, 1, 2, 3, 4, 5), (0, 4, 1, 3, 5, 2))
    x449 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x449 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (0, 4, 2, 5, 6, 3), (5, 1, 4, 6))
    x450 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x450 += einsum(t2.bbbb, (0, 1, 2, 3), x449, (4, 3, 5, 6), (0, 1, 2, 4, 5, 6))
    x451 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x451 += einsum(t2.abab, (0, 1, 2, 3), x167, (4, 5, 1, 6), (5, 4, 3, 6, 0, 2)) * -1.0
    x452 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x452 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 0, 1), (2, 3))
    x453 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x453 += einsum(t1.bb, (0, 1), x452, (0, 2), (1, 2))
    x454 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x454 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x5, (0, 2, 3, 4), (4, 1)) * 2.0
    x455 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x455 += einsum(x453, (0, 1), (0, 1))
    x455 += einsum(x454, (0, 1), (0, 1)) * -1.0
    x456 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x456 += einsum(x455, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 1), (2, 4, 5, 0, 3, 6)) * -2.0
    x457 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x457 += einsum(t2.bbbb, (0, 1, 2, 3), x85, (4, 3, 5, 6), (4, 0, 1, 2, 5, 6))
    x458 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x458 += einsum(t1.bb, (0, 1), x457, (0, 2, 3, 4, 5, 6), (3, 2, 4, 1, 5, 6)) * 2.0
    x459 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x459 += einsum(x450, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 4.0
    x459 += einsum(x451, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -6.0
    x459 += einsum(x456, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x459 += einsum(x458, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    t3new_babbab += einsum(x459, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 5, 3))
    t3new_babbab += einsum(x459, (0, 1, 2, 3, 4, 5), (1, 4, 0, 3, 5, 2)) * -1.0
    x460 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x460 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x460 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x460 += einsum(x236, (0, 1, 2, 3), (1, 0, 3, 2)) * 1.00000000000001
    x460 += einsum(x241, (0, 1, 2, 3), x8, (0, 4, 2, 5), (4, 1, 5, 3)) * -2.00000000000002
    x460 += einsum(t1.aa, (0, 1), x47, (2, 1, 3, 4), (2, 0, 4, 3)) * -1.0
    x460 += einsum(t1.aa, (0, 1), x32, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    t3new_babbab += einsum(x460, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 2, 7), (4, 1, 5, 6, 3, 7)) * 2.0
    x461 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x461 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x461 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -0.49999999999999495
    x462 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x462 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.9999999999999901
    x462 += einsum(x121, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.9999999999999901
    x462 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.9999999999999901
    x462 += einsum(x85, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x462 += einsum(v.aabb.ovov, (0, 1, 2, 3), x461, (0, 4, 1, 5), (2, 3, 4, 5)) * 2.0000000000000004
    t3new_babbab += einsum(x462, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 7, 1), (4, 2, 5, 6, 3, 7)) * 6.0000000000000595
    x463 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x463 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x463 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3))
    x464 = np.zeros((nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x464 += einsum(v.bbbb.vvvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x464 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x463, (0, 2, 4, 5), (3, 5, 4, 1))
    t3new_babbab += einsum(x464, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 0, 7, 3), (4, 5, 6, 2, 7, 1)) * -2.0
    x465 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x465 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x465 += einsum(x178, (0, 1, 2, 3), (2, 0, 3, 1))
    x465 += einsum(x178, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x465 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x463, (4, 5, 1, 3), (0, 5, 2, 4))
    t3new_babbab += einsum(x465, (0, 1, 2, 3), t3.babbab, (0, 4, 2, 5, 6, 7), (1, 4, 3, 5, 6, 7)) * -2.0
    x466 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x466 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x466 += einsum(x195, (0, 1, 2, 3), (1, 0, 2, 3))
    x467 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x467 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x467 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x468 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x468 += einsum(t2.bbbb, (0, 1, 2, 3), x467, (1, 4, 5, 3), (4, 5, 0, 2)) * 2.0
    x469 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x469 += einsum(t2.bbbb, (0, 1, 2, 3), x200, (4, 1, 5, 3), (4, 5, 0, 2)) * 2.0
    x470 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x470 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x470 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3))
    x471 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x471 += einsum(t1.bb, (0, 1), x470, (2, 3, 4, 1), (2, 3, 4, 0))
    x472 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x472 += einsum(t1.bb, (0, 1), x471, (2, 0, 3, 4), (4, 2, 3, 1))
    x473 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x473 += einsum(x196, (0, 1, 2, 3), (0, 2, 1, 3))
    x473 += einsum(x197, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x473 += einsum(x468, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x473 += einsum(x469, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x473 += einsum(x203, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x473 += einsum(x472, (0, 1, 2, 3), (0, 2, 1, 3))
    x474 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x474 += einsum(x209, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x474 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x474 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 2, 1, 3))
    x475 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x475 += einsum(t1.bb, (0, 1), x474, (2, 3, 0, 4), (2, 3, 4, 1))
    x476 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x476 += einsum(x466, (0, 1, 2, 3), (0, 1, 2, 3))
    x476 += einsum(x466, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x476 += einsum(x473, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x476 += einsum(x473, (0, 1, 2, 3), (1, 2, 0, 3))
    x476 += einsum(x169, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x476 += einsum(x475, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x477 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x477 += einsum(t2.abab, (0, 1, 2, 3), x476, (1, 4, 5, 6), (4, 5, 6, 3, 0, 2))
    t3new_babbab += einsum(x477, (0, 1, 2, 3, 4, 5), (1, 4, 0, 3, 5, 2))
    t3new_babbab += einsum(x477, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 5, 3)) * -1.0
    x478 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x478 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 6, 7, 3), (4, 6, 5, 0, 7, 1))
    x479 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x479 += einsum(t2.abab, (0, 1, 2, 3), x37, (4, 5, 2, 6), (1, 3, 4, 0, 6, 5))
    x480 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x480 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ooov, (4, 0, 5, 3), (1, 5, 4, 2))
    x481 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x481 += einsum(t2.abab, (0, 1, 2, 3), x480, (4, 1, 5, 6), (4, 3, 0, 5, 6, 2))
    x482 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x482 += einsum(x62, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 7, 1), (4, 6, 2, 5, 7, 3))
    x483 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x483 += einsum(t2.abab, (0, 1, 2, 3), x23, (4, 3, 5, 0), (1, 4, 5, 2))
    x484 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x484 += einsum(t2.abab, (0, 1, 2, 3), x483, (4, 1, 5, 6), (4, 3, 5, 0, 6, 2))
    x485 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x485 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.00000000000002
    x485 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -1.0
    x486 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x486 += einsum(x41, (0, 1, 2, 3), x485, (0, 4, 3, 5), (1, 4, 2, 5))
    x487 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x487 += einsum(x236, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x487 += einsum(x486, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x488 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x488 += einsum(x487, (0, 1, 2, 3), t3.abaaba, (4, 5, 1, 6, 7, 3), (5, 7, 4, 0, 6, 2)) * 2.0
    x489 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x489 += einsum(v.aabb.ovov, (0, 1, 2, 3), x241, (0, 4, 1, 5), (2, 3, 4, 5)) * 2.0
    x490 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x490 += einsum(x85, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x490 += einsum(x489, (0, 1, 2, 3), (0, 1, 2, 3))
    x491 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x491 += einsum(x490, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 7, 1), (4, 6, 5, 2, 7, 3)) * 2.00000000000002
    x492 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x492 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 3, 5))
    x492 += einsum(t1.aa, (0, 1), t2.abab, (2, 3, 4, 5), (3, 5, 0, 2, 4, 1)) * -0.5
    x493 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x493 += einsum(x28, (0, 1, 2, 3), x492, (4, 5, 0, 6, 2, 7), (4, 5, 1, 6, 3, 7)) * 2.0
    x494 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x494 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 3, 5)) * 2.0
    x494 += einsum(t1.aa, (0, 1), t2.abab, (2, 3, 4, 5), (3, 5, 0, 2, 4, 1)) * -1.0
    x495 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x495 += einsum(x70, (0, 1, 2, 3), x494, (4, 5, 0, 6, 2, 7), (4, 5, 1, 6, 3, 7)) * -1.0
    x496 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x496 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ooov, (4, 0, 1, 5), (3, 5, 4, 2))
    x497 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x497 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 2, 1, 5), (3, 5, 0, 4))
    x498 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x498 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x498 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x498 += einsum(x104, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x498 += einsum(x104, (0, 1, 2, 3), (0, 3, 1, 2))
    x499 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x499 += einsum(t2.abab, (0, 1, 2, 3), x498, (1, 3, 4, 5), (4, 5, 0, 2))
    x500 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x500 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x500 += einsum(x106, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x501 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x501 += einsum(t2.aaaa, (0, 1, 2, 3), x500, (4, 5, 1, 3), (4, 5, 0, 2)) * 2.0
    x502 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x502 += einsum(x13, (0, 1), t2.abab, (2, 0, 3, 4), (1, 4, 2, 3))
    x503 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x503 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x503 += einsum(x106, (0, 1, 2, 3), (1, 0, 2, 3))
    x503 += einsum(x496, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x503 += einsum(x497, (0, 1, 2, 3), (1, 0, 2, 3))
    x503 += einsum(x449, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x503 += einsum(x423, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x503 += einsum(x499, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x503 += einsum(x501, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x503 += einsum(x502, (0, 1, 2, 3), (0, 1, 2, 3))
    x504 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x504 += einsum(t2.abab, (0, 1, 2, 3), x503, (3, 4, 5, 6), (1, 4, 5, 0, 6, 2))
    x505 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x505 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x506 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x506 += einsum(x505, (0, 1, 2, 3), (1, 0, 2, 3))
    x506 += einsum(x236, (0, 1, 2, 3), (0, 1, 2, 3))
    x506 += einsum(x252, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x507 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x507 += einsum(t1.aa, (0, 1), x506, (2, 0, 3, 4), (2, 3, 4, 1))
    x508 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x508 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x508 += einsum(x245, (0, 1, 2, 3), (0, 1, 3, 2))
    x508 += einsum(x247, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x508 += einsum(x507, (0, 1, 2, 3), (0, 3, 1, 2))
    x509 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x509 += einsum(t2.abab, (0, 1, 2, 3), x508, (4, 5, 6, 2), (1, 3, 4, 0, 5, 6))
    x510 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x510 += einsum(v.aabb.ooov, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 6, 7, 3), (4, 6, 5, 0, 1, 7))
    x511 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x511 += einsum(t2.abab, (0, 1, 2, 3), x25, (4, 5, 6, 2), (1, 3, 4, 0, 6, 5))
    x512 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x512 += einsum(t1.aa, (0, 1), x511, (2, 3, 4, 5, 6, 0), (2, 3, 4, 5, 6, 1))
    x513 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x513 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x513 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x514 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x514 += einsum(x513, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 7, 3), (5, 7, 4, 0, 1, 6)) * 2.0
    x515 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x515 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 5), (3, 5, 0, 4))
    x516 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x516 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x516 += einsum(x118, (0, 1, 2, 3), (1, 0, 3, 2))
    x516 += einsum(x515, (0, 1, 2, 3), (1, 0, 3, 2))
    x517 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x517 += einsum(t2.abab, (0, 1, 2, 3), x516, (3, 4, 5, 6), (1, 4, 5, 6, 0, 2))
    x518 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x518 += einsum(x133, (0, 1, 2, 3), (1, 0, 2, 3))
    x518 += einsum(x134, (0, 1, 2, 3), (1, 0, 2, 3))
    x519 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x519 += einsum(t2.abab, (0, 1, 2, 3), x518, (1, 4, 5, 6), (4, 3, 5, 6, 0, 2))
    x520 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x520 += einsum(t1.bb, (0, 1), x23, (0, 2, 3, 4), (1, 2, 3, 4))
    x521 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x521 += einsum(x119, (0, 1, 2, 3), (1, 0, 2, 3))
    x521 += einsum(x520, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x522 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x522 += einsum(t2.abab, (0, 1, 2, 3), x521, (3, 4, 5, 6), (1, 4, 5, 6, 0, 2))
    x523 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x523 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x523 += einsum(x132, (0, 1, 2, 3), (1, 0, 3, 2))
    x524 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x524 += einsum(t2.abab, (0, 1, 2, 3), x523, (1, 4, 5, 6), (4, 3, 5, 6, 0, 2))
    x525 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x525 += einsum(x510, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 2.0
    x525 += einsum(x512, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x525 += einsum(x514, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x525 += einsum(x517, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5)) * -1.0
    x525 += einsum(x519, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x525 += einsum(x522, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x525 += einsum(x524, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5)) * -1.0
    x526 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x526 += einsum(t1.aa, (0, 1), x525, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 6, 1))
    x527 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x527 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x527 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x527 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    x527 += einsum(x3, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x528 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x528 += einsum(t2.abab, (0, 1, 2, 3), x527, (4, 5, 1, 3), (4, 5, 0, 2))
    x529 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x529 += einsum(t2.aaaa, (0, 1, 2, 3), x127, (4, 5, 1, 3), (4, 5, 0, 2)) * 2.0
    x530 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x530 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x530 += einsum(x1, (0, 1, 2, 3), (1, 0, 2, 3))
    x530 += einsum(x385, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x530 += einsum(x386, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x530 += einsum(x528, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x530 += einsum(x529, (0, 1, 2, 3), (1, 0, 2, 3))
    x531 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x531 += einsum(t2.abab, (0, 1, 2, 3), x530, (1, 4, 5, 6), (4, 3, 5, 0, 6, 2))
    x532 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x532 += einsum(t1.bb, (0, 1), x62, (0, 2, 3, 4), (1, 2, 3, 4))
    x533 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x533 += einsum(t2.abab, (0, 1, 2, 3), x23, (1, 4, 5, 0), (3, 4, 5, 2))
    x534 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x534 += einsum(x151, (0, 1, 2, 3), (1, 0, 2, 3))
    x534 += einsum(x532, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x534 += einsum(x533, (0, 1, 2, 3), (1, 0, 2, 3))
    x535 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x535 += einsum(t2.abab, (0, 1, 2, 3), x534, (3, 4, 5, 6), (1, 4, 5, 0, 6, 2))
    x536 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x536 += einsum(v.aabb.vvov, (0, 1, 2, 3), x6, (4, 3, 5, 1), (4, 2, 5, 0))
    x537 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x537 += einsum(x145, (0, 1, 2, 3), (1, 0, 2, 3))
    x537 += einsum(x536, (0, 1, 2, 3), (1, 0, 2, 3))
    x538 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x538 += einsum(t2.abab, (0, 1, 2, 3), x537, (1, 4, 5, 6), (4, 3, 5, 0, 6, 2))
    x539 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x539 += einsum(x478, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    x539 += einsum(x479, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x539 += einsum(x481, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x539 += einsum(x482, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x539 += einsum(x484, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x539 += einsum(x488, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x539 += einsum(x491, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x539 += einsum(x493, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x539 += einsum(x495, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x539 += einsum(x504, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x539 += einsum(x509, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x539 += einsum(x526, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x539 += einsum(x531, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x539 += einsum(x535, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x539 += einsum(x538, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new_abaaba += einsum(x539, (0, 1, 2, 3, 4, 5), (2, 0, 3, 4, 1, 5)) * -1.0
    t3new_abaaba += einsum(x539, (0, 1, 2, 3, 4, 5), (2, 0, 3, 5, 1, 4))
    t3new_abaaba += einsum(x539, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5))
    t3new_abaaba += einsum(x539, (0, 1, 2, 3, 4, 5), (3, 0, 2, 5, 1, 4)) * -1.0
    x540 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x540 += einsum(t2.abab, (0, 1, 2, 3), x222, (4, 5, 6, 2), (1, 3, 4, 0, 5, 6)) * -1.0
    x541 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x541 += einsum(x119, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.99999999999999
    x541 += einsum(x430, (0, 1, 2, 3), (0, 1, 3, 2))
    x542 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x542 += einsum(x541, (0, 1, 2, 3), t3.abaaba, (4, 5, 3, 6, 0, 7), (5, 1, 4, 2, 6, 7)) * -2.00000000000002
    x543 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x543 += einsum(x518, (0, 1, 2, 3), t3.abaaba, (4, 0, 3, 5, 6, 7), (1, 6, 4, 2, 5, 7)) * -2.0
    x544 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x544 += einsum(t1.bb, (0, 1), v.aabb.oooo, (2, 3, 4, 0), (4, 1, 2, 3))
    x545 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x545 += einsum(t2.abab, (0, 1, 2, 3), x2, (1, 4, 5, 2), (4, 3, 5, 0))
    x546 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x546 += einsum(t2.abab, (0, 1, 2, 3), x32, (0, 4, 5, 2), (1, 3, 4, 5))
    x547 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x547 += einsum(t2.abab, (0, 1, 2, 3), x107, (3, 4, 5, 2), (1, 4, 5, 0))
    x548 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x548 += einsum(x10, (0, 1), t2.abab, (2, 3, 1, 4), (3, 4, 0, 2))
    x549 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x549 += einsum(v.aabb.ooov, (0, 1, 2, 3), x113, (2, 4, 3, 5), (4, 5, 0, 1)) * 2.0
    x550 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x550 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x550 += einsum(x544, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x550 += einsum(x153, (0, 1, 2, 3), (0, 1, 3, 2))
    x550 += einsum(x354, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x550 += einsum(x355, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x550 += einsum(x545, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x550 += einsum(x546, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x550 += einsum(x547, (0, 1, 2, 3), (0, 1, 2, 3))
    x550 += einsum(x548, (0, 1, 2, 3), (0, 1, 2, 3))
    x550 += einsum(x549, (0, 1, 2, 3), (0, 1, 3, 2))
    x551 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x551 += einsum(t2.aaaa, (0, 1, 2, 3), x550, (4, 5, 1, 6), (4, 5, 0, 6, 2, 3)) * -2.0
    x552 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x552 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x552 += einsum(x118, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x553 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x553 += einsum(x552, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 0, 7), (5, 1, 4, 3, 6, 7)) * -2.0
    x554 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x554 += einsum(x278, (0, 1, 2, 3), (0, 2, 1, 3))
    x554 += einsum(x212, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x554 += einsum(x213, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    x555 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x555 += einsum(t2.abab, (0, 1, 2, 3), x554, (4, 5, 6, 2), (1, 3, 4, 0, 5, 6)) * 2.0
    x556 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x556 += einsum(x523, (0, 1, 2, 3), t3.abaaba, (4, 0, 2, 5, 6, 7), (1, 6, 4, 3, 5, 7)) * -2.0
    x557 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x557 += einsum(f.aa.oo, (0, 1), (0, 1))
    x557 += einsum(x30, (0, 1), (0, 1))
    x557 += einsum(x31, (0, 1), (0, 1)) * 2.0
    x557 += einsum(x34, (0, 1), (1, 0))
    x558 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x558 += einsum(x557, (0, 1), t3.abaaba, (2, 3, 1, 4, 5, 6), (3, 5, 2, 0, 4, 6)) * -2.0
    x559 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x559 += einsum(t1.bb, (0, 1), x133, (2, 0, 3, 4), (2, 1, 3, 4))
    x560 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x560 += einsum(t2.abab, (0, 1, 2, 3), x291, (4, 0, 5, 2), (1, 3, 4, 5))
    x561 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x561 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x561 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3))
    x562 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x562 += einsum(t1.aa, (0, 1), x561, (2, 3, 4, 1), (2, 3, 4, 0))
    x563 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x563 += einsum(x113, (0, 1, 2, 3), x23, (0, 2, 4, 5), (1, 3, 4, 5)) * 2.0
    x564 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x564 += einsum(x559, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x564 += einsum(x560, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x564 += einsum(x562, (0, 1, 2, 3), (0, 1, 3, 2))
    x564 += einsum(x563, (0, 1, 2, 3), (0, 1, 2, 3))
    x565 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x565 += einsum(t2.aaaa, (0, 1, 2, 3), x564, (4, 5, 6, 1), (4, 5, 0, 6, 2, 3)) * -2.0
    x566 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x566 += einsum(x261, (0, 1), t3.abaaba, (2, 3, 0, 4, 5, 6), (3, 5, 2, 1, 4, 6)) * -2.0
    x567 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x567 += einsum(x540, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 2.0
    x567 += einsum(x542, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x567 += einsum(x543, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x567 += einsum(x551, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x567 += einsum(x553, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x567 += einsum(x555, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x567 += einsum(x556, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x567 += einsum(x558, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x567 += einsum(x565, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x567 += einsum(x566, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_abaaba += einsum(x567, (0, 1, 2, 3, 4, 5), (2, 0, 3, 4, 1, 5)) * -1.0
    t3new_abaaba += einsum(x567, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5))
    x568 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x568 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 7, 3, 1), (5, 2, 4, 6, 0, 7))
    x569 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x569 += einsum(t2.abab, (0, 1, 2, 3), x568, (4, 1, 5, 6, 0, 7), (4, 3, 5, 6, 2, 7))
    x570 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x570 += einsum(v.aabb.vvvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x570 += einsum(x129, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x571 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x571 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 3, 5))
    x571 += einsum(t1.bb, (0, 1), t2.aaaa, (2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x572 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x572 += einsum(x570, (0, 1, 2, 3), x571, (4, 0, 5, 6, 2, 7), (4, 1, 5, 6, 7, 3)) * 2.0
    x573 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x573 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x573 += einsum(x126, (0, 1, 2, 3), (1, 0, 3, 2))
    x574 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x574 += einsum(x573, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 7, 2), (1, 7, 4, 5, 6, 3)) * -2.0
    x575 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x575 += einsum(t1.bb, (0, 1), v.aabb.vvoo, (2, 3, 4, 0), (4, 1, 2, 3))
    x576 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x576 += einsum(t2.bbbb, (0, 1, 2, 3), v.aabb.vvov, (4, 5, 1, 3), (0, 2, 4, 5))
    x577 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x577 += einsum(t2.abab, (0, 1, 2, 3), x116, (0, 2, 4, 5), (1, 3, 4, 5))
    x578 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x578 += einsum(t2.abab, (0, 1, 2, 3), x2, (1, 4, 0, 5), (4, 3, 5, 2))
    x579 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x579 += einsum(t2.abab, (0, 1, 2, 3), x107, (3, 4, 0, 5), (1, 4, 5, 2))
    x580 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x580 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1))
    x580 += einsum(x575, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x580 += einsum(x576, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x580 += einsum(x318, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x580 += einsum(x319, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x580 += einsum(x577, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x580 += einsum(x578, (0, 1, 2, 3), (0, 1, 2, 3))
    x580 += einsum(x579, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x581 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x581 += einsum(t2.aaaa, (0, 1, 2, 3), x580, (4, 5, 3, 6), (4, 5, 0, 1, 2, 6)) * -2.0
    x582 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x582 += einsum(v.aabb.ovov, (0, 1, 2, 3), x378, (4, 3, 0, 5), (2, 4, 1, 5))
    x583 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x583 += einsum(x338, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.99999999999999
    x583 += einsum(x582, (0, 1, 2, 3), (0, 1, 3, 2))
    x584 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x584 += einsum(x583, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 7, 3), (1, 7, 4, 5, 6, 2)) * -2.00000000000002
    x585 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x585 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x585 += einsum(x45, (0, 1), (0, 1))
    x585 += einsum(x46, (0, 1), (0, 1)) * 2.0
    x585 += einsum(x142, (0, 1), (1, 0))
    x586 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x586 += einsum(x585, (0, 1), t3.abaaba, (2, 3, 4, 5, 6, 1), (3, 6, 2, 4, 5, 0)) * -2.0
    x587 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x587 += einsum(x265, (0, 1), t3.abaaba, (2, 3, 4, 5, 6, 0), (3, 6, 2, 4, 5, 1)) * -2.0
    x588 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x588 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 1, 7, 3), (5, 7, 4, 6, 0, 2))
    x589 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x589 += einsum(x107, (0, 1, 2, 3), x571, (4, 0, 5, 6, 3, 7), (4, 1, 2, 5, 6, 7))
    x590 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x590 += einsum(t1.bb, (0, 1), v.aabb.ovoo, (2, 3, 4, 0), (4, 1, 2, 3))
    x591 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x591 += einsum(t2.bbbb, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 2, 4, 5))
    x592 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x592 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x592 += einsum(x590, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x592 += einsum(x591, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x592 += einsum(x161, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x593 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x593 += einsum(t2.aaaa, (0, 1, 2, 3), x592, (4, 5, 6, 3), (4, 5, 0, 1, 6, 2)) * -1.0
    x594 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x594 += einsum(x588, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x594 += einsum(x589, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5))
    x594 += einsum(x593, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x595 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x595 += einsum(t1.aa, (0, 1), x594, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x596 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x596 += einsum(x51, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x596 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x596 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x597 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x597 += einsum(t2.abab, (0, 1, 2, 3), x596, (4, 5, 0, 6), (1, 3, 4, 5, 6, 2)) * 2.0
    x598 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x598 += einsum(x569, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -2.0
    x598 += einsum(x572, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x598 += einsum(x574, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x598 += einsum(x581, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x598 += einsum(x584, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x598 += einsum(x586, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x598 += einsum(x587, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x598 += einsum(x595, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x598 += einsum(x597, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    t3new_abaaba += einsum(x598, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5))
    t3new_abaaba += einsum(x598, (0, 1, 2, 3, 4, 5), (3, 0, 2, 5, 1, 4)) * -1.0
    x599 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x599 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x599 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x599 += einsum(x112, (0, 1, 2, 3), (1, 0, 3, 2)) * 1.00000000000001
    x599 += einsum(x11, (0, 1, 2, 3), x309, (0, 4, 3, 5), (1, 4, 2, 5)) * -2.00000000000002
    x599 += einsum(t1.bb, (0, 1), x114, (2, 1, 3, 4), (2, 0, 4, 3)) * -1.0
    x599 += einsum(t1.bb, (0, 1), x18, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t3new_abaaba += einsum(x599, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 2, 7), (4, 1, 5, 6, 3, 7)) * 2.0
    x600 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x600 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x600 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -0.49999999999999495
    x601 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x601 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.9999999999999901
    x601 += einsum(x590, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.9999999999999901
    x601 += einsum(x124, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.9999999999999901
    x601 += einsum(x161, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x601 += einsum(v.aabb.ovov, (0, 1, 2, 3), x600, (2, 4, 3, 5), (4, 5, 0, 1)) * 2.0000000000000004
    t3new_abaaba += einsum(x601, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 2, 6, 7, 3), (4, 0, 5, 6, 1, 7)) * 6.0000000000000595
    x602 = np.zeros((nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x602 += einsum(v.aaaa.vvvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x602 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 4, 1, 5), (5, 2, 3, 4)) * -1.0
    x602 += einsum(t1.aa, (0, 1), x110, (0, 2, 3, 4), (4, 1, 2, 3)) * -1.0
    t3new_abaaba += einsum(x602, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 0, 7, 3), (4, 5, 6, 2, 7, 1)) * -2.0
    x603 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x603 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x603 += einsum(x73, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x603 += einsum(x73, (0, 1, 2, 3), (3, 2, 1, 0))
    x603 += einsum(x100, (0, 1, 2, 3), (1, 3, 0, 2))
    t3new_abaaba += einsum(x603, (0, 1, 2, 3), t3.abaaba, (0, 4, 2, 5, 6, 7), (1, 4, 3, 5, 6, 7)) * -2.0
    x604 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x604 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x604 += einsum(x74, (0, 1, 2, 3), (1, 0, 2, 3))
    x605 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x605 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x605 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x606 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x606 += einsum(t2.aaaa, (0, 1, 2, 3), x605, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x607 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x607 += einsum(t2.aaaa, (0, 1, 2, 3), x291, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x608 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x608 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x608 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x608 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3))
    x609 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x609 += einsum(t1.aa, (0, 1), x608, (2, 3, 1, 4), (2, 3, 0, 4))
    x610 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x610 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x610 += einsum(x25, (0, 1, 2, 3), (0, 2, 1, 3))
    x611 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x611 += einsum(t1.aa, (0, 1), x610, (2, 3, 4, 1), (2, 3, 4, 0))
    x612 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x612 += einsum(t1.aa, (0, 1), x611, (2, 0, 3, 4), (4, 2, 3, 1))
    x613 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x613 += einsum(x72, (0, 1, 2, 3), (0, 2, 1, 3))
    x613 += einsum(x76, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x613 += einsum(x606, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x613 += einsum(x607, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x613 += einsum(x609, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x613 += einsum(x612, (0, 1, 2, 3), (0, 2, 1, 3))
    x614 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x614 += einsum(x604, (0, 1, 2, 3), (0, 1, 2, 3))
    x614 += einsum(x604, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x614 += einsum(x613, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x614 += einsum(x613, (0, 1, 2, 3), (1, 2, 0, 3))
    x614 += einsum(x54, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x614 += einsum(x298, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x615 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x615 += einsum(t2.abab, (0, 1, 2, 3), x614, (0, 4, 5, 6), (1, 3, 4, 5, 6, 2))
    t3new_abaaba += einsum(x615, (0, 1, 2, 3, 4, 5), (3, 0, 2, 5, 1, 4))
    t3new_abaaba += einsum(x615, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5)) * -1.0
    x616 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x616 += einsum(v.bbbb.vvvv, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 6, 7, 3, 1), (4, 5, 6, 7, 0, 2)) * -1.0
    x617 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x617 += einsum(t1.bb, (0, 1), x13, (0, 2), (2, 1))
    x618 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x618 += einsum(f.bb.vv, (0, 1), (0, 1)) * -1.0
    x618 += einsum(x137, (0, 1), (1, 0)) * 2.0
    x618 += einsum(x138, (0, 1), (1, 0))
    x618 += einsum(x617, (0, 1), (0, 1))
    x619 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x619 += einsum(x618, (0, 1), t3.bbbbbb, (2, 3, 4, 5, 6, 0), (2, 3, 4, 1, 5, 6)) * 6.0
    x620 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x620 += einsum(x616, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    x620 += einsum(x619, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new_bbbbbb = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    t3new_bbbbbb += einsum(x620, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_bbbbbb += einsum(x620, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x620, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x621 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x621 += einsum(t2.bbbb, (0, 1, 2, 3), x155, (4, 5, 3, 6), (4, 0, 1, 2, 6, 5))
    x622 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x622 += einsum(t2.bbbb, (0, 1, 2, 3), x3, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x623 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x623 += einsum(t1.bb, (0, 1), x622, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x624 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x624 += einsum(t2.bbbb, (0, 1, 2, 3), x193, (4, 5, 3, 6), (5, 4, 0, 1, 6, 2))
    x625 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x625 += einsum(x623, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x625 += einsum(x624, (0, 1, 2, 3, 4, 5), (0, 3, 2, 1, 5, 4)) * -1.0
    x626 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x626 += einsum(t1.bb, (0, 1), x625, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x627 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x627 += einsum(x621, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -2.0
    x627 += einsum(x626, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_bbbbbb += einsum(x627, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x628 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x628 += einsum(x124, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 3, 7), (0, 4, 5, 6, 7, 1))
    x629 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x629 += einsum(t2.bbbb, (0, 1, 2, 3), x376, (4, 5, 6, 3), (4, 0, 1, 5, 6, 2)) * -1.0
    x630 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x630 += einsum(x193, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 7, 2), (1, 4, 5, 3, 6, 7)) * -6.0
    x631 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x631 += einsum(x167, (0, 1, 2, 3), (0, 1, 2, 3))
    x631 += einsum(x168, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x632 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x632 += einsum(t2.bbbb, (0, 1, 2, 3), x631, (4, 5, 1, 6), (4, 5, 0, 6, 2, 3)) * -12.0
    x633 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x633 += einsum(x628, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * 2.0
    x633 += einsum(x629, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -4.0
    x633 += einsum(x630, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x633 += einsum(x632, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4))
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4))
    t3new_bbbbbb += einsum(x633, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x634 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x634 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x634 += einsum(x325, (0, 1, 2, 3), (0, 1, 3, 2))
    x634 += einsum(x327, (0, 1, 2, 3), (0, 3, 1, 2)) * -1.0
    x635 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x635 += einsum(t2.bbbb, (0, 1, 2, 3), x634, (4, 5, 3, 6), (4, 0, 1, 5, 6, 2)) * -2.0
    x636 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x636 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x637 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x637 += einsum(t1.bb, (0, 1), x636, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x638 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x638 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x638 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x638 += einsum(x112, (0, 1, 2, 3), (0, 1, 2, 3))
    x638 += einsum(x329, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x639 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x639 += einsum(t2.bbbb, (0, 1, 2, 3), x638, (4, 5, 6, 3), (4, 5, 0, 1, 6, 2)) * -1.0
    x640 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x640 += einsum(x637, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x640 += einsum(x639, (0, 1, 2, 3, 4, 5), (3, 2, 1, 0, 5, 4)) * -1.0
    x641 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x641 += einsum(t1.bb, (0, 1), x640, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x642 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x642 += einsum(x635, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x642 += einsum(x641, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_bbbbbb += einsum(x642, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x643 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x643 += einsum(x434, (0, 1), t3.bbbbbb, (2, 3, 4, 5, 6, 0), (2, 3, 4, 1, 5, 6)) * 6.0
    x644 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x644 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 6, 7, 3, 1), (4, 5, 6, 0, 2, 7)) * -1.0
    x645 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x645 += einsum(x463, (0, 1, 2, 3), x644, (4, 5, 6, 0, 1, 7), (4, 5, 6, 2, 3, 7)) * 6.0
    x646 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x646 += einsum(x643, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x646 += einsum(x645, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x646, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_bbbbbb += einsum(x646, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x646, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x647 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x647 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 7), (4, 5, 2, 6, 7, 3))
    x648 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x648 += einsum(t2.bbbb, (0, 1, 2, 3), x396, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x649 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x649 += einsum(t2.bbbb, (0, 1, 2, 3), x166, (4, 5, 1, 6), (4, 5, 0, 2, 3, 6))
    x650 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x650 += einsum(x14, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 7, 2), (1, 4, 5, 3, 6, 7)) * 6.0
    x651 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x651 += einsum(x647, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 2.0
    x651 += einsum(x648, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -4.0
    x651 += einsum(x649, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -4.0
    x651 += einsum(x650, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x651, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x652 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x652 += einsum(x178, (0, 1, 2, 3), t3.bbbbbb, (4, 3, 2, 5, 6, 7), (0, 4, 1, 5, 6, 7)) * -1.0
    t3new_bbbbbb += einsum(x652, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * 6.0
    t3new_bbbbbb += einsum(x652, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -6.0
    t3new_bbbbbb += einsum(x652, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3)) * -6.0
    t3new_bbbbbb += einsum(x652, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * 6.0
    t3new_bbbbbb += einsum(x652, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * 6.0
    t3new_bbbbbb += einsum(x652, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -6.0
    x653 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x653 += einsum(x397, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x653 += einsum(x398, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    x654 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x654 += einsum(t2.bbbb, (0, 1, 2, 3), x653, (4, 5, 6, 3), (4, 0, 1, 5, 6, 2)) * -12.0
    x655 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x655 += einsum(v.aabb.ovoo, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 7), (4, 5, 2, 3, 6, 7))
    x656 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x656 += einsum(x467, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 7, 3), (1, 2, 4, 5, 6, 7))
    x657 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x657 += einsum(x655, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -0.3333333333333333
    x657 += einsum(x656, (0, 1, 2, 3, 4, 5), (2, 3, 1, 0, 4, 5)) * -1.0
    x658 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x658 += einsum(t1.bb, (0, 1), x657, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 6.0
    x659 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x659 += einsum(x654, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x659 += einsum(x658, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new_bbbbbb += einsum(x659, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    x660 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x660 += einsum(x209, (0, 1, 2, 3), (1, 0, 3, 2))
    x660 += einsum(x170, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x661 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x661 += einsum(x660, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 3, 5, 6, 7), (0, 1, 4, 5, 6, 7)) * -6.0
    x662 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x662 += einsum(x411, (0, 1), t3.bbbbbb, (2, 3, 0, 4, 5, 6), (1, 2, 3, 4, 5, 6)) * 6.0
    x663 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x663 += einsum(x661, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    x663 += einsum(x662, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x663, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_bbbbbb += einsum(x663, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x663, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -1.0
    x664 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x664 += einsum(v.bbbb.oooo, (0, 1, 2, 3), t3.bbbbbb, (4, 1, 3, 5, 6, 7), (4, 0, 2, 5, 6, 7))
    x665 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x665 += einsum(f.bb.oo, (0, 1), (0, 1))
    x665 += einsum(x16, (0, 1), (1, 0)) * 2.0
    x665 += einsum(x17, (0, 1), (1, 0))
    x665 += einsum(x20, (0, 1), (0, 1))
    x666 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x666 += einsum(x665, (0, 1), t3.bbbbbb, (2, 3, 0, 4, 5, 6), (1, 2, 3, 4, 5, 6)) * 6.0
    x667 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x667 += einsum(x664, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3)) * 6.0
    x667 += einsum(x666, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new_bbbbbb += einsum(x667, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x667, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x667, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x668 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x668 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0000000000000204
    x668 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -1.0
    x669 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x669 += einsum(x11, (0, 1, 2, 3), x668, (0, 4, 3, 5), (1, 4, 2, 5)) * 0.4999999999999949
    x670 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x670 += einsum(x112, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999999983
    x670 += einsum(x669, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x671 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x671 += einsum(x670, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 1, 6, 7, 3), (0, 4, 5, 2, 6, 7)) * 12.000000000000123
    x672 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x672 += einsum(t2.abab, (0, 1, 2, 3), x8, (0, 4, 2, 5), (1, 3, 4, 5)) * 0.5
    x673 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x673 += einsum(v.aabb.ovov, (0, 1, 2, 3), x309, (2, 4, 3, 5), (4, 5, 0, 1))
    x674 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x674 += einsum(x672, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x674 += einsum(x673, (0, 1, 2, 3), (0, 1, 2, 3))
    x675 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x675 += einsum(x674, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 3, 7), (4, 5, 0, 6, 7, 1)) * 4.00000000000004
    x676 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x676 += einsum(x671, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x676 += einsum(x675, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5))
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3))
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5))
    t3new_bbbbbb += einsum(x676, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3)) * -1.0
    x677 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x677 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 6, 7, 3, 1), (4, 5, 6, 0, 7, 2)) * -1.0
    x678 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x678 += einsum(t1.bb, (0, 1), x677, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    t3new_bbbbbb += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 6.0
    t3new_bbbbbb += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    t3new_bbbbbb += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -6.0
    t3new_bbbbbb += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * 6.0
    t3new_bbbbbb += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * 6.0
    t3new_bbbbbb += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -6.0
    x679 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x679 += einsum(t1.bb, (0, 1), v.bbbb.oovv, (2, 3, 4, 1), (0, 2, 3, 4))
    x680 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x680 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x681 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x681 += einsum(x679, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x681 += einsum(x680, (0, 1, 2, 3), (0, 2, 1, 3))
    x681 += einsum(x196, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x682 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x682 += einsum(t1.bb, (0, 1), x170, (2, 3, 0, 4), (3, 2, 4, 1))
    x683 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x683 += einsum(t2.bbbb, (0, 1, 2, 3), x406, (4, 1, 5, 3), (4, 5, 0, 2))
    x684 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x684 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x684 += einsum(x188, (0, 1, 2, 3), (1, 0, 2, 3))
    x685 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x685 += einsum(t1.bb, (0, 1), x684, (2, 3, 1, 4), (2, 3, 0, 4)) * 0.5
    x686 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x686 += einsum(v.bbbb.ooov, (0, 1, 2, 3), x113, (1, 4, 3, 5), (4, 0, 2, 5))
    x687 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x687 += einsum(x682, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x687 += einsum(x197, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x687 += einsum(x683, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x687 += einsum(x685, (0, 1, 2, 3), (2, 1, 0, 3))
    x687 += einsum(x686, (0, 1, 2, 3), (0, 1, 2, 3))
    x688 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x688 += einsum(x13, (0, 1), t2.bbbb, (2, 3, 4, 1), (0, 2, 3, 4)) * -1.0
    x689 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x689 += einsum(t1.bb, (0, 1), x474, (2, 3, 0, 4), (2, 3, 4, 1)) * 0.5
    x690 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x690 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x690 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    x690 += einsum(x681, (0, 1, 2, 3), (0, 1, 2, 3))
    x690 += einsum(x681, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x690 += einsum(x687, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x690 += einsum(x687, (0, 1, 2, 3), (1, 0, 2, 3))
    x690 += einsum(x195, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x690 += einsum(x195, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x690 += einsum(x688, (0, 1, 2, 3), (2, 1, 0, 3))
    x690 += einsum(x689, (0, 1, 2, 3), (1, 0, 2, 3))
    x691 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x691 += einsum(t2.bbbb, (0, 1, 2, 3), x690, (4, 5, 1, 6), (4, 5, 0, 6, 2, 3)) * -4.0
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0

    t1new.aa = t1new_aa
    t1new.bb = t1new_bb
    t2new.aaaa = t2new_aaaa
    t2new.abab = t2new_abab
    t2new.bbbb = t2new_bbbb
    t3new.aaaaaa = t3new_aaaaaa
    t3new.abaaba = t3new_abaaba
    t3new.babbab = t3new_babbab
    t3new.bbbbbb = t3new_bbbbbb

    return {"t1new": t1new, "t2new": t2new, "t3new": t3new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
    l1new = Namespace()
    l2new = Namespace()
    l3new = Namespace()

    # L amplitudes
    l1new_bb = np.zeros((nvir[1], nocc[1]), dtype=np.float64)
    l1new_bb += einsum(f.bb.ov, (0, 1), (1, 0))
    l1new_bb += einsum(l2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (3, 1, 4, 0), (4, 2)) * 2.0
    l1new_aa = np.zeros((nvir[0], nocc[0]), dtype=np.float64)
    l1new_aa += einsum(f.aa.ov, (0, 1), (1, 0))
    l1new_aa += einsum(l2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (3, 0, 4, 1), (4, 2)) * -2.0
    l2new_aaaa = np.zeros((nvir[0], nvir[0], nocc[0], nocc[0]), dtype=np.float64)
    l2new_aaaa += einsum(l2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 1, 5, 0), (4, 5, 2, 3)) * -2.0
    l2new_abab = np.zeros((nvir[0], nvir[1], nocc[0], nocc[1]), dtype=np.float64)
    l2new_abab += einsum(l1.aa, (0, 1), v.aabb.vvov, (2, 0, 3, 4), (2, 4, 1, 3))
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (1, 3, 0, 2))
    l2new_abab += einsum(l1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 0), (3, 4, 2, 1))
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), v.aabb.vvvv, (4, 0, 5, 1), (4, 5, 2, 3))
    l2new_bbbb = np.zeros((nvir[1], nvir[1], nocc[1], nocc[1]), dtype=np.float64)
    l2new_bbbb += einsum(l2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 1, 5, 0), (4, 5, 2, 3)) * -2.0
    l3new_aaaaaa = np.zeros((nvir[0], nvir[0], nvir[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (0, 5, 3, 1, 2, 4)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (0, 3, 5, 1, 2, 4))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (5, 0, 3, 1, 2, 4))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (3, 0, 5, 1, 2, 4)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (5, 3, 0, 1, 2, 4)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (3, 5, 0, 1, 2, 4))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (0, 5, 3, 2, 1, 4))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (0, 3, 5, 2, 1, 4)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (5, 0, 3, 2, 1, 4)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (3, 0, 5, 2, 1, 4))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (5, 3, 0, 2, 1, 4))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (3, 5, 0, 2, 1, 4)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (0, 5, 3, 2, 4, 1)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (0, 3, 5, 2, 4, 1))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (5, 0, 3, 2, 4, 1))
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (3, 0, 5, 2, 4, 1)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (5, 3, 0, 2, 4, 1)) * -1.0
    l3new_aaaaaa += einsum(l1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (3, 5, 0, 2, 4, 1))
    l3new_babbab = np.zeros((nvir[1], nvir[0], nvir[1], nocc[1], nocc[0], nocc[1]), dtype=np.float64)
    l3new_babbab += einsum(v.bbbb.vvvv, (0, 1, 2, 3), l3.babbab, (1, 4, 3, 5, 6, 7), (0, 4, 2, 5, 6, 7)) * 2.0
    l3new_abaaba = np.zeros((nvir[0], nvir[1], nvir[0], nocc[0], nocc[1], nocc[0]), dtype=np.float64)
    l3new_abaaba += einsum(v.aaaa.vvvv, (0, 1, 2, 3), l3.abaaba, (3, 4, 1, 5, 6, 7), (0, 4, 2, 5, 6, 7)) * -2.0
    l3new_bbbbbb = np.zeros((nvir[1], nvir[1], nvir[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (0, 5, 3, 1, 2, 4)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (0, 3, 5, 1, 2, 4))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (5, 0, 3, 1, 2, 4))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (3, 0, 5, 1, 2, 4)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (5, 3, 0, 1, 2, 4)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (3, 5, 0, 1, 2, 4))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (0, 5, 3, 2, 1, 4))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (0, 3, 5, 2, 1, 4)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (5, 0, 3, 2, 1, 4)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (3, 0, 5, 2, 1, 4))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (5, 3, 0, 2, 1, 4))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (3, 5, 0, 2, 1, 4)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (0, 5, 3, 2, 4, 1)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (0, 3, 5, 2, 4, 1))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (5, 0, 3, 2, 4, 1))
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (3, 0, 5, 2, 4, 1)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (5, 3, 0, 2, 4, 1)) * -1.0
    l3new_bbbbbb += einsum(l1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (3, 5, 0, 2, 4, 1))
    x0 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x0 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x1 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x1 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x1 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x1 += einsum(x0, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x1 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3))
    x2 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x2 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (0, 4, 2, 3))
    x3 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x3 += einsum(x2, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(l1.bb, (0, 1), x3, (1, 2, 3, 4), (4, 0, 3, 2)) * -1.0
    x4 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x4 += einsum(t1.aa, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (3, 4, 0, 2))
    x5 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x5 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x5 += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2))
    x6 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x6 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x7 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x8 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x8 += einsum(t2.bbbb, (0, 1, 2, 3), x7, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x9 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x9 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x9 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x10 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x10 += einsum(t1.bb, (0, 1), x9, (2, 3, 1, 4), (0, 2, 3, 4))
    x11 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x11 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x11 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x11 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    x11 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x11 += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x12 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x12 += einsum(t1.aa, (0, 1), v.aabb.vvov, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new_abab += einsum(l2.aaaa, (0, 1, 2, 3), x12, (4, 5, 3, 1), (0, 5, 2, 4)) * 2.0
    x13 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2))
    x14 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x14 += einsum(t2.abab, (0, 1, 2, 3), x7, (1, 4, 5, 3), (4, 5, 0, 2))
    x15 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x15 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x15 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x15 += einsum(x13, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x15 += einsum(x14, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x16 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x16 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    x17 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x17 += einsum(t1.bb, (0, 1), x7, (0, 2, 3, 1), (2, 3))
    x18 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x18 += einsum(f.bb.ov, (0, 1), (0, 1))
    x18 += einsum(x16, (0, 1), (0, 1))
    x18 += einsum(x17, (0, 1), (0, 1)) * -1.0
    l2new_abab += einsum(l1.aa, (0, 1), x18, (2, 3), (0, 3, 1, 2))
    l3new_babbab += einsum(x18, (0, 1), l2.abab, (2, 3, 4, 5), (3, 2, 1, 5, 4, 0))
    l3new_babbab += einsum(x18, (0, 1), l2.abab, (2, 3, 4, 5), (1, 2, 3, 0, 4, 5))
    l3new_babbab += einsum(x18, (0, 1), l2.abab, (2, 3, 4, 5), (3, 2, 1, 0, 4, 5)) * -1.0
    l3new_babbab += einsum(x18, (0, 1), l2.abab, (2, 3, 4, 5), (1, 2, 3, 5, 4, 0)) * -1.0
    l3new_abaaba += einsum(x18, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 1, 3, 4, 0, 5)) * 2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (1, 2, 3, 0, 4, 5)) * 2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (1, 2, 3, 4, 0, 5)) * -2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (1, 2, 3, 4, 5, 0)) * 2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 1, 3, 0, 4, 5)) * -2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 1, 3, 4, 0, 5)) * 2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 1, 3, 4, 5, 0)) * -2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 3, 1, 0, 4, 5)) * 2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 3, 1, 4, 0, 5)) * -2.0
    l3new_bbbbbb += einsum(x18, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 3, 1, 4, 5, 0)) * 2.0
    x19 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x19 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 4, 1), (0, 4, 2, 3))
    x20 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x20 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 5, 3), (1, 5, 2, 4))
    x21 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x21 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x21 += einsum(x19, (0, 1, 2, 3), (0, 1, 3, 2))
    x21 += einsum(x20, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x22 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x22 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x23 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x23 += einsum(t1.bb, (0, 1), x0, (2, 3, 4, 1), (0, 2, 3, 4))
    x24 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x24 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x25 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x25 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(x22, (0, 1, 2, 3), (3, 1, 2, 0))
    x25 += einsum(x23, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x25 += einsum(x24, (0, 1, 2, 3), (2, 0, 3, 1)) * -1.0
    x25 += einsum(x24, (0, 1, 2, 3), (3, 0, 2, 1))
    x26 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x26 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x27 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x27 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (1, 5, 0, 4))
    x28 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x28 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x28 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(l1.aa, (0, 1), x28, (2, 3, 1, 4), (0, 3, 4, 2)) * -1.0
    x29 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x29 += einsum(t1.bb, (0, 1), x28, (2, 1, 3, 4), (0, 2, 3, 4))
    x30 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x30 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x30 += einsum(x26, (0, 1, 2, 3), (1, 0, 3, 2))
    x30 += einsum(x27, (0, 1, 2, 3), (0, 1, 3, 2))
    x30 += einsum(x29, (0, 1, 2, 3), (0, 1, 3, 2))
    x31 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x31 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 1, 7, 3), (4, 6, 0, 2, 5, 7))
    l2new_bbbb += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), x31, (5, 3, 6, 7, 4, 1), (0, 2, 6, 7)) * -1.9999999999999203
    x32 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x32 += einsum(t2.abab, (0, 1, 2, 3), v.bbbb.ooov, (4, 5, 6, 3), (1, 4, 5, 6, 0, 2))
    x33 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x33 += einsum(t2.abab, (0, 1, 2, 3), x0, (4, 5, 6, 3), (4, 1, 6, 5, 0, 2))
    x34 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x34 += einsum(x31, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -0.9999999999999601
    x34 += einsum(x32, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    x34 += einsum(x32, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x34 += einsum(x33, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x34 += einsum(x33, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x35 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x35 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 7, 1, 3), (4, 6, 2, 7, 5, 0))
    l2new_abab += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), x35, (5, 3, 6, 2, 4, 7), (1, 0, 7, 6)) * 1.9999999999999194
    x36 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x36 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x36 += einsum(x2, (0, 1, 2, 3), (1, 0, 2, 3))
    x37 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x37 += einsum(t2.abab, (0, 1, 2, 3), x36, (4, 5, 6, 2), (1, 4, 5, 3, 0, 6))
    x38 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x38 += einsum(x35, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 0.9999999999999597
    x38 += einsum(t2.bbbb, (0, 1, 2, 3), x28, (4, 3, 5, 6), (0, 1, 4, 2, 6, 5))
    x38 += einsum(x37, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4)) * -1.0
    x39 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x39 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 1, 7, 3), (0, 4, 6, 2, 5, 7)) * 0.9999999999999601
    x39 += einsum(v.aabb.vvov, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 7, 1, 3), (2, 4, 6, 7, 5, 0)) * -0.9999999999999597
    x39 += einsum(x1, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 6, 7, 3), (1, 4, 0, 6, 5, 7)) * -2.0
    x39 += einsum(x3, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 7, 3), (1, 5, 0, 7, 4, 6)) * -2.0
    x39 += einsum(x5, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 7, 1), (0, 4, 5, 6, 3, 7))
    x39 += einsum(t2.abab, (0, 1, 2, 3), x11, (4, 5, 6, 3), (5, 1, 4, 6, 0, 2))
    x39 += einsum(t2.bbbb, (0, 1, 2, 3), x15, (4, 3, 5, 6), (4, 0, 1, 2, 5, 6)) * -1.0
    x39 += einsum(x18, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 1), (0, 2, 4, 5, 3, 6)) * -0.9999999999999597
    x39 += einsum(t2.abab, (0, 1, 2, 3), x21, (4, 5, 2, 6), (5, 1, 4, 3, 0, 6)) * -1.0
    x39 += einsum(t2.abab, (0, 1, 2, 3), x25, (1, 4, 5, 6), (5, 6, 4, 3, 0, 2)) * -1.0
    x39 += einsum(t2.abab, (0, 1, 2, 3), x30, (4, 5, 0, 6), (5, 1, 4, 3, 6, 2))
    x39 += einsum(t1.bb, (0, 1), x34, (2, 3, 4, 0, 5, 6), (4, 3, 2, 1, 5, 6))
    x39 += einsum(t1.aa, (0, 1), x38, (2, 3, 4, 5, 0, 6), (4, 3, 2, 5, 6, 1)) * -1.0
    l1new_bb += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), x39, (6, 3, 5, 2, 4, 1), (0, 6)) * -2.0
    x40 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x40 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 7, 3, 1), (5, 2, 4, 6, 0, 7))
    l2new_abab += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), x40, (4, 6, 3, 5, 7, 2), (0, 1, 7, 6)) * -1.9999999999999194
    x41 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x41 += einsum(t2.aaaa, (0, 1, 2, 3), x36, (4, 5, 6, 3), (4, 5, 0, 1, 6, 2)) * -1.0
    x42 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x42 += einsum(x40, (0, 1, 2, 3, 4, 5), (0, 1, 3, 4, 2, 5)) * 0.9999999999999597
    x42 += einsum(t2.abab, (0, 1, 2, 3), x28, (4, 3, 5, 6), (1, 4, 0, 6, 5, 2)) * -1.0
    x42 += einsum(x41, (0, 1, 2, 3, 4, 5), (1, 0, 3, 4, 2, 5)) * -1.0
    x43 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x43 += einsum(v.aabb.vvov, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 7, 3, 1), (2, 5, 4, 6, 7, 0)) * -0.9999999999999597
    x43 += einsum(x1, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 7), (1, 0, 4, 5, 6, 7)) * -0.5
    x43 += einsum(x3, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 2, 6, 7, 3), (1, 0, 4, 5, 6, 7)) * -1.5
    x43 += einsum(x5, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 1, 7), (0, 5, 4, 3, 6, 7))
    x43 += einsum(t2.abab, (0, 1, 2, 3), x15, (4, 3, 5, 6), (4, 1, 0, 5, 2, 6)) * -1.0
    x43 += einsum(x18, (0, 1), t3.abaaba, (2, 3, 4, 5, 1, 6), (0, 3, 2, 4, 5, 6)) * -0.49999999999998007
    x43 += einsum(t2.aaaa, (0, 1, 2, 3), x21, (4, 5, 3, 6), (5, 4, 0, 1, 2, 6)) * -1.0
    x43 += einsum(t2.aaaa, (0, 1, 2, 3), x30, (4, 5, 1, 6), (5, 4, 0, 6, 2, 3))
    x43 += einsum(t1.aa, (0, 1), x42, (2, 3, 4, 0, 5, 6), (3, 2, 4, 5, 6, 1)) * -1.0
    l1new_bb += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), x43, (6, 4, 3, 5, 0, 2), (1, 6)) * 2.0
    x44 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x44 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x44 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x44 += einsum(x0, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x44 += einsum(x0, (0, 1, 2, 3), (2, 0, 1, 3))
    x45 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x45 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x45 += einsum(x22, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    x45 += einsum(x23, (0, 1, 2, 3), (2, 1, 3, 0))
    x45 += einsum(x24, (0, 1, 2, 3), (2, 0, 3, 1))
    x45 += einsum(x24, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x46 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x46 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 6, 7, 3, 1), (4, 5, 6, 0, 2, 7)) * -1.0
    l2new_bbbb += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), x46, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7)) * 5.9999999999997575
    x47 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x47 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x48 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x48 += einsum(t2.bbbb, (0, 1, 2, 3), x0, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x49 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x49 += einsum(x46, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.9999999999999596
    x49 += einsum(x47, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x49 += einsum(x47, (0, 1, 2, 3, 4, 5), (0, 1, 3, 4, 2, 5))
    x49 += einsum(x48, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    x49 += einsum(x48, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    x50 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x50 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 6, 7, 3, 1), (0, 4, 5, 6, 7, 2)) * -0.4999999999999798
    x50 += einsum(x44, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 7, 3), (2, 4, 1, 5, 6, 7)) * -0.75
    x50 += einsum(x3, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 3, 7), (1, 4, 0, 5, 6, 7)) * 0.25
    x50 += einsum(t2.bbbb, (0, 1, 2, 3), x11, (4, 5, 6, 3), (5, 0, 4, 1, 2, 6)) * -0.5
    x50 += einsum(x18, (0, 1), t3.bbbbbb, (2, 3, 4, 5, 6, 1), (0, 2, 3, 4, 5, 6)) * -0.2499999999999899
    x50 += einsum(t2.bbbb, (0, 1, 2, 3), x45, (1, 4, 5, 6), (5, 0, 4, 6, 2, 3)) * -0.5
    x50 += einsum(t1.bb, (0, 1), x49, (2, 3, 4, 5, 0, 6), (5, 3, 4, 2, 6, 1)) * -0.5
    l1new_bb += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), x50, (6, 3, 4, 5, 2, 1), (0, 6)) * -12.0
    x51 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x51 += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 0, 4, 5))
    x52 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x52 += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 2, 5, 0), (3, 1, 4, 5))
    x53 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.babbab, (4, 6, 5, 1, 7, 2), (3, 0, 6, 7))
    x54 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 5, 4, 7, 2, 1), (3, 0, 6, 7))
    x55 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x55 += einsum(t1.aa, (0, 1), l3.babbab, (2, 1, 3, 4, 5, 6), (4, 6, 2, 3, 5, 0))
    x56 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x56 += einsum(t2.abab, (0, 1, 2, 3), x55, (4, 1, 5, 3, 0, 6), (4, 5, 6, 2))
    x57 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x57 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 3, 5, 7, 0, 2), (4, 1, 6, 7))
    x58 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x58 += einsum(t1.aa, (0, 1), l3.abaaba, (2, 3, 1, 4, 5, 6), (5, 3, 4, 6, 0, 2))
    x59 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x59 += einsum(t2.aaaa, (0, 1, 2, 3), x58, (4, 5, 0, 1, 6, 3), (4, 5, 6, 2)) * -1.0
    x60 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x60 += einsum(t1.aa, (0, 1), l2.abab, (1, 2, 3, 4), (4, 2, 3, 0))
    l2new_abab += einsum(x2, (0, 1, 2, 3), x60, (0, 4, 5, 2), (3, 4, 5, 1))
    x61 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x61 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 6, 1), (5, 4, 6, 0))
    x62 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x62 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (2, 4, 3, 5, 6, 1), (6, 4, 5, 0))
    x63 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x63 += einsum(x60, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x63 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3))
    x63 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3))
    l1new_bb += einsum(v.aabb.oovv, (0, 1, 2, 3), x63, (4, 3, 0, 1), (2, 4)) * -2.0
    l2new_abab += einsum(v.aabb.ovvv, (0, 1, 2, 3), x63, (4, 3, 5, 0), (1, 2, 5, 4)) * -2.0
    l2new_abab += einsum(v.aabb.ovoo, (0, 1, 2, 3), x63, (3, 4, 5, 0), (1, 4, 5, 2)) * 2.0
    x64 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x64 += einsum(l2.abab, (0, 1, 2, 3), (3, 1, 2, 0)) * 0.5
    x64 += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3))
    x64 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3))
    x64 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x64 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x64 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x64 += einsum(x57, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x64 += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x64 += einsum(t1.aa, (0, 1), x63, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    l1new_bb += einsum(v.aabb.ovvv, (0, 1, 2, 3), x64, (4, 3, 0, 1), (2, 4)) * 2.0
    x65 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x65 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    x66 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x66 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 5, 6, 0, 1), (6, 4, 5, 3))
    x67 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x67 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 3, 4, 0), (4, 2, 3, 1)) * 0.3333333333333333
    x67 += einsum(x65, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x67 += einsum(x66, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    l1new_bb += einsum(v.bbbb.vvvv, (0, 1, 2, 3), x67, (4, 3, 1, 2), (0, 4)) * -6.0
    x68 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    x69 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x69 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (4, 5, 3, 0, 6, 1), (6, 5, 4, 2))
    x70 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x70 += einsum(t1.aa, (0, 1), l2.abab, (2, 3, 0, 4), (4, 3, 2, 1)) * 0.5
    x70 += einsum(x68, (0, 1, 2, 3), (0, 1, 2, 3))
    x70 += einsum(x69, (0, 1, 2, 3), (0, 1, 2, 3))
    l1new_bb += einsum(v.aabb.vvvv, (0, 1, 2, 3), x70, (4, 3, 0, 1), (2, 4)) * 2.0
    x71 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x71 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x71 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x72 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x72 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (2, 4, 0, 5))
    x73 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x73 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), (3, 4, 1, 5))
    x74 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x74 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    x75 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x75 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    x76 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x76 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7))
    x77 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x77 += einsum(x72, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.4444444444444444
    x77 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.1111111111111111
    x77 += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3))
    x77 += einsum(x75, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.4444444444444444
    x77 += einsum(x76, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.1111111111111111
    l1new_bb += einsum(x71, (0, 1, 2, 3), x77, (4, 0, 2, 1), (3, 4)) * -9.0
    x78 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x78 += einsum(t1.bb, (0, 1), l3.bbbbbb, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    l3new_babbab += einsum(v.aabb.ovoo, (0, 1, 2, 3), x78, (4, 2, 5, 3, 6, 7), (6, 1, 7, 5, 0, 4)) * -6.0
    l3new_babbab += einsum(x2, (0, 1, 2, 3), x78, (0, 4, 5, 1, 6, 7), (7, 3, 6, 4, 2, 5)) * 6.0
    x79 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x79 += einsum(t2.bbbb, (0, 1, 2, 3), x78, (4, 1, 0, 5, 6, 3), (4, 5, 6, 2))
    x80 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x80 += einsum(t1.bb, (0, 1), l3.babbab, (2, 3, 1, 4, 5, 6), (4, 6, 0, 2, 5, 3))
    l2new_abab += einsum(x19, (0, 1, 2, 3), x80, (0, 4, 1, 5, 6, 3), (2, 5, 6, 4)) * 2.0
    x81 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x81 += einsum(t2.abab, (0, 1, 2, 3), x80, (4, 1, 5, 6, 0, 2), (4, 5, 6, 3))
    x82 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x82 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new_abab += einsum(x2, (0, 1, 2, 3), x82, (4, 0, 1, 5), (3, 5, 2, 4)) * -2.0
    x83 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x83 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    x84 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x84 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 0, 6), (5, 6, 1, 4))
    x85 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x85 += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3))
    x85 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x85 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x86 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x86 += einsum(x79, (0, 1, 2, 3), (0, 1, 2, 3))
    x86 += einsum(x81, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x86 += einsum(t1.bb, (0, 1), x85, (0, 2, 3, 4), (2, 3, 4, 1)) * 0.3333333333333333
    l1new_bb += einsum(x71, (0, 1, 2, 3), x86, (4, 0, 2, 3), (1, 4)) * -6.0
    x87 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x87 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), (3, 4, 0, 5))
    x88 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x88 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 0, 7, 2), (3, 6, 1, 7))
    x89 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x89 += einsum(t2.abab, (0, 1, 2, 3), x80, (4, 1, 5, 3, 0, 6), (4, 5, 6, 2)) * -1.0
    x90 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x90 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 7, 1, 2), (4, 6, 0, 7))
    x91 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x91 += einsum(t1.bb, (0, 1), l3.abaaba, (2, 1, 3, 4, 5, 6), (5, 0, 4, 6, 2, 3))
    l3new_abaaba += einsum(x18, (0, 1), x91, (2, 0, 3, 4, 5, 6), (5, 1, 6, 4, 2, 3)) * 2.0
    x92 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x92 += einsum(t2.aaaa, (0, 1, 2, 3), x91, (4, 5, 0, 1, 3, 6), (4, 5, 6, 2)) * -1.0
    x93 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x93 += einsum(t1.bb, (0, 1), l2.abab, (2, 1, 3, 4), (4, 0, 3, 2))
    l2new_abab += einsum(x4, (0, 1, 2, 3), x93, (4, 0, 2, 5), (5, 1, 3, 4))
    x94 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x94 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (2, 4, 3, 5, 6, 1), (5, 0, 6, 4))
    x95 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x95 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 6, 0), (6, 1, 5, 4))
    x96 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x96 += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3))
    x96 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x96 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    l1new_aa += einsum(v.aabb.vvoo, (0, 1, 2, 3), x96, (2, 3, 4, 1), (0, 4)) * -1.0
    l2new_abab += einsum(v.aabb.ooov, (0, 1, 2, 3), x96, (4, 2, 1, 5), (5, 3, 0, 4))
    x97 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x97 += einsum(x87, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x97 += einsum(x88, (0, 1, 2, 3), (0, 1, 2, 3))
    x97 += einsum(x89, (0, 1, 2, 3), (0, 1, 3, 2))
    x97 += einsum(x90, (0, 1, 2, 3), (0, 1, 2, 3))
    x97 += einsum(x92, (0, 1, 2, 3), (0, 1, 3, 2))
    x97 += einsum(t1.aa, (0, 1), x96, (2, 3, 0, 4), (2, 3, 1, 4)) * 0.5
    l1new_bb += einsum(v.aabb.vvov, (0, 1, 2, 3), x97, (4, 2, 1, 0), (3, 4)) * -2.0
    x98 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x98 += einsum(t1.bb, (0, 1), x55, (2, 3, 4, 1, 5, 6), (2, 3, 0, 4, 5, 6))
    x99 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x99 += einsum(t1.bb, (0, 1), x58, (2, 1, 3, 4, 5, 6), (2, 0, 3, 4, 5, 6))
    x100 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x100 += einsum(x68, (0, 1, 2, 3), (0, 1, 2, 3))
    x100 += einsum(x69, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(v.aabb.ovvv, (0, 1, 2, 3), x100, (4, 3, 5, 1), (5, 2, 0, 4)) * -2.0
    l2new_abab += einsum(x100, (0, 1, 2, 3), x3, (0, 4, 5, 3), (2, 1, 5, 4)) * 2.0
    x101 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x101 += einsum(x60, (0, 1, 2, 3), (0, 1, 2, 3))
    x101 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x101 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x102 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x102 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), (3, 5, 2, 4))
    x103 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x103 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 7, 5, 0, 1, 2), (3, 6, 4, 7))
    x104 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x104 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 7, 5, 0, 1, 2), (4, 7, 3, 6))
    x105 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x105 += einsum(t1.bb, (0, 1), x101, (2, 1, 3, 4), (0, 2, 3, 4))
    x106 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x106 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x106 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x107 += einsum(t1.aa, (0, 1), x106, (2, 3, 4, 1), (2, 3, 0, 4)) * 2.0
    x108 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x108 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3))
    x108 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.9999999999999194
    x108 += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.9999999999999194
    x108 += einsum(x105, (0, 1, 2, 3), (1, 0, 2, 3))
    x108 += einsum(x107, (0, 1, 2, 3), (0, 1, 3, 2))
    x109 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x109 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 0, 1), (2, 4))
    x110 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x110 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), (3, 4))
    x111 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x111 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 4, 5, 0, 1, 2), (3, 6))
    x112 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x112 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 0, 1, 2), (3, 6))
    x113 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x113 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 0, 1, 2), (4, 6))
    x114 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x114 += einsum(x109, (0, 1), (0, 1))
    x114 += einsum(x110, (0, 1), (0, 1)) * 0.5
    x114 += einsum(x111, (0, 1), (0, 1)) * 1.4999999999999394
    x114 += einsum(x112, (0, 1), (0, 1)) * 0.9999999999999597
    x114 += einsum(x113, (0, 1), (0, 1)) * 0.49999999999998007
    x115 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x115 += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), (1, 3, 2, 4)) * 0.5
    x115 += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x115 += einsum(l2.bbbb, (0, 1, 2, 3), t3.babbab, (4, 5, 3, 0, 6, 1), (2, 4, 5, 6))
    x115 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 1, 0), (3, 5, 4, 6))
    x115 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x78, (6, 0, 2, 7, 5, 3), (6, 7, 1, 4)) * -1.5
    x115 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x80, (6, 1, 7, 4, 2, 5), (6, 7, 0, 3)) * -2.0
    x115 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (6, 2, 5, 3, 1, 7), (6, 0, 7, 4))
    x115 += einsum(t2.abab, (0, 1, 2, 3), x98, (4, 1, 5, 3, 0, 6), (4, 5, 6, 2))
    x115 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x91, (6, 7, 2, 1, 5, 4), (6, 7, 0, 3)) * 1.5
    x115 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x58, (6, 4, 2, 0, 7, 5), (6, 1, 7, 3)) * -1.0
    x115 += einsum(t2.aaaa, (0, 1, 2, 3), x99, (4, 5, 1, 0, 6, 3), (4, 5, 6, 2)) * -1.0
    x115 += einsum(t2.abab, (0, 1, 2, 3), x100, (4, 3, 2, 5), (4, 1, 0, 5)) * -1.0
    x115 += einsum(t2.abab, (0, 1, 2, 3), x85, (1, 4, 5, 3), (4, 5, 0, 2)) * -1.0
    x115 += einsum(t2.aaaa, (0, 1, 2, 3), x96, (4, 5, 1, 3), (4, 5, 0, 2))
    x115 += einsum(t2.abab, (0, 1, 2, 3), x101, (4, 3, 0, 5), (4, 1, 5, 2)) * -0.5
    x115 += einsum(t1.aa, (0, 1), x108, (2, 3, 0, 4), (2, 3, 4, 1)) * -0.5
    x115 += einsum(t1.aa, (0, 1), x114, (2, 3), (2, 3, 0, 1))
    l1new_bb += einsum(v.aabb.ovov, (0, 1, 2, 3), x115, (4, 2, 0, 1), (3, 4)) * -2.0
    x116 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x116 += einsum(t1.aa, (0, 1), v.aabb.vvoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x117 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x117 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 2, 5, 3), (1, 5, 0, 4))
    x118 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x118 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 3, 6, 1), (4, 0, 5, 6)) * -1.0
    x119 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x119 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 6, 3, 1), (5, 2, 4, 6))
    x120 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x120 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x120 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x120 += einsum(x0, (0, 1, 2, 3), (1, 0, 2, 3))
    x120 += einsum(x0, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x121 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x121 += einsum(t2.abab, (0, 1, 2, 3), x120, (4, 5, 1, 3), (4, 5, 0, 2))
    x122 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x122 += einsum(t2.aaaa, (0, 1, 2, 3), x36, (4, 5, 1, 3), (4, 5, 0, 2)) * 2.0
    x123 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x123 += einsum(t2.abab, (0, 1, 2, 3), x5, (4, 3, 0, 5), (1, 4, 5, 2))
    x124 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x124 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x124 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x125 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x125 += einsum(t1.bb, (0, 1), x124, (2, 1, 3, 4), (0, 2, 3, 4))
    x126 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x126 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x126 += einsum(x26, (0, 1, 2, 3), (1, 0, 3, 2))
    x126 += einsum(x27, (0, 1, 2, 3), (1, 0, 3, 2))
    x126 += einsum(x29, (0, 1, 2, 3), (1, 0, 3, 2))
    x127 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x127 += einsum(t1.aa, (0, 1), x126, (2, 3, 0, 4), (2, 3, 4, 1))
    x128 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x128 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x128 += einsum(x116, (0, 1, 2, 3), (1, 0, 2, 3))
    x128 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3))
    x128 += einsum(x118, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x128 += einsum(x119, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x128 += einsum(x121, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x128 += einsum(x122, (0, 1, 2, 3), (1, 0, 2, 3))
    x128 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x128 += einsum(x18, (0, 1), t2.abab, (2, 3, 4, 1), (3, 0, 2, 4))
    x128 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3))
    x128 += einsum(x127, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    l1new_bb += einsum(l2.abab, (0, 1, 2, 3), x128, (3, 4, 2, 0), (1, 4)) * -1.0
    x129 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x129 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x129 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x130 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x130 += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x130 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x130 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(v.aabb.ovoo, (0, 1, 2, 3), x130, (2, 4, 3, 5), (1, 5, 0, 4)) * 2.0
    x131 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x131 += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x131 += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3))
    x131 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(v.aabb.vvov, (0, 1, 2, 3), x131, (4, 2, 5, 1), (0, 3, 5, 4)) * -2.0
    l2new_abab += einsum(x18, (0, 1), x131, (2, 0, 3, 4), (4, 1, 3, 2)) * -2.0
    x132 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x132 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    x132 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x133 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x133 += einsum(t1.bb, (0, 1), x132, (2, 3, 4, 1), (0, 2, 3, 4))
    x134 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x134 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x78, (6, 2, 1, 7, 4, 5), (6, 0, 7, 3)) * -0.75
    x134 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x80, (6, 2, 7, 5, 1, 4), (6, 0, 7, 3)) * -0.3333333333333333
    x134 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x91, (6, 7, 2, 0, 5, 3), (6, 1, 7, 4)) * 0.08333333333333333
    x134 += einsum(t2.bbbb, (0, 1, 2, 3), x130, (4, 1, 5, 3), (4, 0, 5, 2)) * -0.3333333333333333
    x134 += einsum(t2.abab, (0, 1, 2, 3), x131, (4, 5, 0, 2), (4, 1, 5, 3)) * 0.16666666666666666
    x134 += einsum(t1.bb, (0, 1), x133, (2, 3, 0, 4), (3, 4, 2, 1)) * -0.5
    x134 += einsum(t1.bb, (0, 1), x114, (2, 3), (2, 0, 3, 1)) * 0.16666666666666666
    l1new_bb += einsum(x129, (0, 1, 2, 3), x134, (4, 0, 1, 2), (3, 4)) * 12.0
    x135 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x135 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x136 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x136 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 2, 6, 3, 1), (4, 5, 0, 6)) * -1.0
    x137 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x137 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 3), (4, 5, 2, 6))
    x138 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x138 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x138 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x138 += einsum(x0, (0, 1, 2, 3), (0, 1, 2, 3))
    x138 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x139 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x139 += einsum(t2.bbbb, (0, 1, 2, 3), x138, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x140 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x140 += einsum(t2.abab, (0, 1, 2, 3), x3, (4, 5, 0, 2), (1, 4, 5, 3))
    x141 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x141 += einsum(x18, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x142 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x142 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x143 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x143 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x143 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x143 += einsum(x142, (0, 1, 2, 3), (0, 1, 2, 3))
    x144 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x144 += einsum(t1.bb, (0, 1), x143, (2, 3, 1, 4), (0, 2, 3, 4))
    x145 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x145 += einsum(t1.bb, (0, 1), x25, (0, 2, 3, 4), (2, 3, 4, 1))
    x146 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x146 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x146 += einsum(x135, (0, 1, 2, 3), (2, 1, 0, 3))
    x146 += einsum(x136, (0, 1, 2, 3), (2, 1, 0, 3)) * -3.0
    x146 += einsum(x137, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x146 += einsum(x139, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x146 += einsum(x140, (0, 1, 2, 3), (2, 0, 1, 3))
    x146 += einsum(x141, (0, 1, 2, 3), (2, 1, 0, 3))
    x146 += einsum(x144, (0, 1, 2, 3), (2, 1, 0, 3))
    x146 += einsum(x145, (0, 1, 2, 3), (1, 2, 0, 3))
    l1new_bb += einsum(l2.bbbb, (0, 1, 2, 3), x146, (4, 2, 3, 1), (0, 4)) * 2.0
    x147 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x147 += einsum(x65, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x147 += einsum(x66, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    l2new_abab += einsum(v.aabb.ovvv, (0, 1, 2, 3), x147, (4, 5, 2, 3), (1, 5, 0, 4)) * 6.0
    x148 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x148 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), (2, 3, 4, 5))
    x149 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x149 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    x150 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x150 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 7, 0, 1, 2), (3, 5, 6, 7))
    l2new_bbbb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x150, (4, 5, 2, 0), (3, 1, 4, 5)) * 1.9999999999999203
    x151 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x151 += einsum(x148, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0000000000000397
    x151 += einsum(x149, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.9999999999999982
    x151 += einsum(x150, (0, 1, 2, 3), (0, 1, 3, 2))
    x152 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x152 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 0), (1, 2, 3, 4)) * 0.3333333333333468
    x152 += einsum(l2.bbbb, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6)) * 1.0000000000000404
    x152 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 0, 1), (3, 4, 5, 6)) * 0.3333333333333468
    x152 += einsum(t2.bbbb, (0, 1, 2, 3), x147, (4, 2, 3, 5), (4, 0, 1, 5)) * 1.0000000000000404
    x152 += einsum(t1.bb, (0, 1), x151, (0, 2, 3, 4), (2, 4, 3, 1)) * -0.33333333333333354
    l1new_bb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x152, (4, 0, 2, 3), (1, 4)) * 5.9999999999997575
    x153 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x153 += einsum(t1.bb, (0, 1), x82, (2, 3, 4, 1), (2, 3, 0, 4))
    x154 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x154 += einsum(t1.bb, (0, 1), x78, (2, 3, 4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x155 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x155 += einsum(t1.bb, (0, 1), x80, (2, 3, 4, 1, 5, 6), (2, 3, 0, 4, 5, 6))
    x156 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x156 += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x156 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    x156 += einsum(t1.bb, (0, 1), x153, (0, 2, 3, 4), (4, 2, 3, 1)) * 0.3333333333333333
    x156 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x156 += einsum(t2.bbbb, (0, 1, 2, 3), x154, (4, 0, 1, 5, 6, 3), (5, 4, 6, 2))
    x156 += einsum(t2.abab, (0, 1, 2, 3), x155, (4, 1, 5, 6, 0, 2), (5, 4, 6, 3)) * 0.3333333333333333
    l1new_bb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x156, (0, 4, 2, 1), (3, 4)) * -6.0
    x157 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x157 += einsum(l1.bb, (0, 1), t1.bb, (1, 2), (0, 2))
    x158 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x158 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 1), (0, 4))
    x159 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x159 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), (1, 4))
    x160 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x160 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 6, 1, 2), (0, 6))
    x161 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x161 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 0, 6, 2), (1, 6))
    x162 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x162 += einsum(x157, (0, 1), (0, 1))
    x162 += einsum(x158, (0, 1), (0, 1)) * 2.0
    x162 += einsum(x159, (0, 1), (0, 1))
    x162 += einsum(x160, (0, 1), (0, 1)) * 1.9999999999999194
    x162 += einsum(x161, (0, 1), (0, 1)) * 0.9999999999999601
    x163 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x163 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x163 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    l1new_bb += einsum(x162, (0, 1), x163, (2, 1, 0, 3), (3, 2)) * -1.0
    x164 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x164 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 0), (2, 3))
    x165 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x165 += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), (2, 3))
    x166 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x166 += einsum(l2.bbbb, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 3, 5, 0, 1), (4, 5))
    x167 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x167 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 3, 5, 0, 1), (4, 5))
    x168 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x168 += einsum(l2.aaaa, (0, 1, 2, 3), t3.abaaba, (2, 4, 3, 0, 5, 1), (4, 5))
    x169 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x169 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x78, (0, 1, 2, 6, 4, 5), (6, 3))
    x170 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x170 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x80, (0, 2, 6, 5, 1, 4), (6, 3)) * -1.0
    x171 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x171 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x91, (1, 6, 0, 2, 3, 5), (6, 4))
    x172 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x172 += einsum(l1.bb, (0, 1), t1.bb, (2, 0), (1, 2))
    x173 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x173 += einsum(x172, (0, 1), (0, 1))
    x173 += einsum(x109, (0, 1), (0, 1)) * 2.0
    x173 += einsum(x110, (0, 1), (0, 1))
    x173 += einsum(x111, (0, 1), (0, 1)) * 2.9999999999998788
    x173 += einsum(x112, (0, 1), (0, 1)) * 1.9999999999999194
    x173 += einsum(x113, (0, 1), (0, 1)) * 0.9999999999999601
    x174 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x174 += einsum(t1.bb, (0, 1), (0, 1)) * -0.5
    x174 += einsum(x164, (0, 1), (0, 1)) * -1.0
    x174 += einsum(x165, (0, 1), (0, 1)) * -0.5
    x174 += einsum(x166, (0, 1), (0, 1)) * -1.5
    x174 += einsum(x167, (0, 1), (0, 1)) * -1.0
    x174 += einsum(x168, (0, 1), (0, 1)) * -0.5
    x174 += einsum(x169, (0, 1), (0, 1)) * 1.4999999999999394
    x174 += einsum(x170, (0, 1), (0, 1)) * 0.9999999999999597
    x174 += einsum(x171, (0, 1), (0, 1)) * 0.49999999999998007
    x174 += einsum(t2.bbbb, (0, 1, 2, 3), x130, (0, 1, 4, 3), (4, 2)) * -1.0
    x174 += einsum(t2.abab, (0, 1, 2, 3), x131, (1, 4, 0, 2), (4, 3))
    x174 += einsum(t1.bb, (0, 1), x173, (0, 2), (2, 1)) * 0.5
    l1new_bb += einsum(x174, (0, 1), x7, (0, 2, 3, 1), (3, 2)) * 2.0
    x175 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x175 += einsum(l1.aa, (0, 1), t1.aa, (1, 2), (0, 2))
    x176 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x176 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), (0, 4))
    x177 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x177 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 1), (0, 4))
    x178 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x178 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 0, 6, 2), (1, 6))
    x179 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x179 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 6, 1, 2), (0, 6))
    x180 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x180 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (3, 4, 5, 6, 1, 2), (0, 6))
    x181 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x181 += einsum(x175, (0, 1), (0, 1)) * 1.00000000000004
    x181 += einsum(x176, (0, 1), (0, 1)) * 1.00000000000004
    x181 += einsum(x177, (0, 1), (0, 1)) * 2.00000000000008
    x181 += einsum(x178, (0, 1), (0, 1))
    x181 += einsum(x179, (0, 1), (1, 0)) * 1.9999999999999991
    x181 += einsum(x180, (0, 1), (1, 0)) * 2.9999999999999982
    l1new_bb += einsum(x181, (0, 1), v.aabb.vvov, (1, 0, 2, 3), (3, 2)) * 0.9999999999999601
    x182 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x182 += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), (2, 3))
    x183 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x183 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 0), (2, 3))
    x184 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x184 += einsum(l2.bbbb, (0, 1, 2, 3), t3.babbab, (2, 4, 3, 0, 5, 1), (4, 5))
    x185 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x185 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 2, 5, 1, 0), (4, 5))
    x186 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x186 += einsum(l2.aaaa, (0, 1, 2, 3), t3.aaaaaa, (4, 2, 3, 5, 0, 1), (4, 5))
    x187 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x187 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (0, 2, 3, 5, 1, 6), (6, 4))
    x188 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x188 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x58, (1, 4, 0, 2, 6, 5), (6, 3)) * -1.0
    x189 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x189 += einsum(t1.aa, (0, 1), l3.aaaaaa, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    l3new_abaaba += einsum(v.aabb.ooov, (0, 1, 2, 3), x189, (4, 0, 5, 1, 6, 7), (6, 3, 7, 5, 2, 4)) * -6.0
    l3new_abaaba += einsum(x4, (0, 1, 2, 3), x189, (2, 4, 5, 3, 6, 7), (6, 1, 7, 4, 0, 5)) * -6.0
    x190 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x190 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x189, (0, 1, 2, 6, 4, 5), (6, 3))
    x191 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x191 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new_abab += einsum(x191, (0, 1, 2, 3), x4, (4, 5, 1, 2), (3, 5, 0, 4)) * -2.0
    x192 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x192 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 1, 6), (5, 6, 0, 4))
    x193 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x193 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    x194 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x194 += einsum(x191, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x194 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x194 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3))
    x195 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x195 += einsum(l1.aa, (0, 1), t1.aa, (2, 0), (1, 2))
    x196 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x196 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), (2, 4))
    x197 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x197 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 0, 1), (2, 4))
    x198 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x198 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 0, 1, 2), (4, 6))
    x199 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x199 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 0, 1, 2), (3, 6))
    x200 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x200 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 4, 5, 0, 1, 2), (3, 6))
    x201 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x201 += einsum(x195, (0, 1), (0, 1))
    x201 += einsum(x196, (0, 1), (0, 1))
    x201 += einsum(x197, (0, 1), (0, 1)) * 2.0
    x201 += einsum(x198, (0, 1), (0, 1)) * 0.9999999999999601
    x201 += einsum(x199, (0, 1), (0, 1)) * 1.9999999999999194
    x201 += einsum(x200, (0, 1), (0, 1)) * 2.9999999999998788
    x202 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x202 += einsum(l1.aa, (0, 1), (1, 0)) * -0.5
    x202 += einsum(t1.aa, (0, 1), (0, 1)) * -0.5
    x202 += einsum(x182, (0, 1), (0, 1)) * -0.5
    x202 += einsum(x183, (0, 1), (0, 1)) * -1.0
    x202 += einsum(x184, (0, 1), (0, 1)) * -0.5
    x202 += einsum(x185, (0, 1), (0, 1)) * -1.0
    x202 += einsum(x186, (0, 1), (0, 1)) * -1.5
    x202 += einsum(x187, (0, 1), (0, 1)) * 0.49999999999998007
    x202 += einsum(x188, (0, 1), (0, 1)) * 0.9999999999999597
    x202 += einsum(x190, (0, 1), (0, 1)) * 1.4999999999999394
    x202 += einsum(t2.abab, (0, 1, 2, 3), x63, (1, 3, 0, 4), (4, 2))
    x202 += einsum(t2.aaaa, (0, 1, 2, 3), x194, (0, 1, 4, 3), (4, 2)) * -3.0
    x202 += einsum(t1.aa, (0, 1), x201, (0, 2), (2, 1)) * 0.5
    l1new_bb += einsum(x202, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (3, 2)) * -2.0
    x203 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x203 += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.3333333333333333
    x203 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x203 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    l1new_bb += einsum(v.bbbb.oovv, (0, 1, 2, 3), x203, (0, 4, 1, 3), (2, 4)) * -6.0
    x204 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x204 += einsum(t1.bb, (0, 1), x101, (2, 1, 3, 4), (0, 2, 3, 4)) * 0.5000000000000202
    x205 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x205 += einsum(t1.aa, (0, 1), x106, (2, 3, 4, 1), (2, 3, 0, 4)) * 1.0000000000000404
    x206 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x206 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5000000000000202
    x206 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3))
    x206 += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3))
    x206 += einsum(x204, (0, 1, 2, 3), (1, 0, 3, 2))
    x206 += einsum(x205, (0, 1, 2, 3), (0, 1, 2, 3))
    l1new_bb += einsum(v.aabb.ooov, (0, 1, 2, 3), x206, (4, 2, 1, 0), (3, 4)) * 1.9999999999999194
    x207 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x207 += einsum(x148, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333468
    x207 += einsum(x149, (0, 1, 2, 3), (0, 1, 3, 2))
    x207 += einsum(x150, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.33333333333333354
    x207 += einsum(t1.bb, (0, 1), x130, (2, 3, 4, 1), (0, 2, 3, 4)) * 0.3333333333333468
    l1new_bb += einsum(v.bbbb.ooov, (0, 1, 2, 3), x207, (1, 4, 0, 2), (3, 4)) * -5.9999999999997575
    x208 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x208 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (3, 4, 5, 6, 1, 2), (0, 6))
    l1new_bb += einsum(x208, (0, 1), x71, (2, 3, 0, 1), (3, 2)) * -2.9999999999998788
    x209 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x209 += einsum(t1.bb, (0, 1), x132, (2, 3, 4, 1), (2, 3, 0, 4)) * 3.0
    l1new_bb += einsum(v.bbbb.ooov, (0, 1, 2, 3), x209, (4, 0, 2, 1), (3, 4)) * 2.0
    x210 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x210 += einsum(x172, (0, 1), (0, 1)) * 1.00000000000004
    x210 += einsum(x109, (0, 1), (0, 1)) * 2.00000000000008
    x210 += einsum(x110, (0, 1), (0, 1)) * 1.00000000000004
    x210 += einsum(x111, (0, 1), (1, 0)) * 2.9999999999999982
    x210 += einsum(x112, (0, 1), (1, 0)) * 1.9999999999999991
    x210 += einsum(x113, (0, 1), (1, 0))
    l1new_bb += einsum(x210, (0, 1), v.bbbb.ooov, (1, 0, 2, 3), (3, 2)) * -0.9999999999999601
    x211 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x211 += einsum(x195, (0, 1), (0, 1)) * 1.00000000000004
    x211 += einsum(x196, (0, 1), (0, 1)) * 1.00000000000004
    x211 += einsum(x197, (0, 1), (0, 1)) * 2.00000000000008
    x211 += einsum(x198, (0, 1), (1, 0))
    x211 += einsum(x199, (0, 1), (0, 1)) * 1.9999999999999991
    x211 += einsum(x200, (0, 1), (0, 1)) * 2.9999999999999982
    l1new_bb += einsum(x211, (0, 1), v.aabb.ooov, (1, 0, 2, 3), (3, 2)) * -0.9999999999999601
    x212 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x212 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x212 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l1new_bb += einsum(l1.bb, (0, 1), x212, (1, 2, 0, 3), (3, 2)) * -1.0
    x213 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x213 += einsum(x111, (0, 1), (0, 1)) * 2.9999999999999982
    x213 += einsum(x112, (0, 1), (0, 1)) * 1.9999999999999991
    x213 += einsum(x113, (0, 1), (0, 1))
    l1new_bb += einsum(x213, (0, 1), v.bbbb.ooov, (2, 0, 1, 3), (3, 2)) * 0.9999999999999601
    x214 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x214 += einsum(x172, (0, 1), (0, 1)) * 0.5
    x214 += einsum(x109, (0, 1), (0, 1))
    x214 += einsum(x110, (0, 1), (0, 1)) * 0.5
    l1new_bb += einsum(x214, (0, 1), v.bbbb.ooov, (2, 0, 1, 3), (3, 2)) * 2.0
    x215 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x215 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 1, 2, 3), (2, 3))
    x216 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x216 += einsum(f.bb.vv, (0, 1), (0, 1))
    x216 += einsum(x215, (0, 1), (1, 0))
    x216 += einsum(t1.bb, (0, 1), x9, (0, 1, 2, 3), (3, 2)) * -1.0
    l1new_bb += einsum(l1.bb, (0, 1), x216, (0, 2), (2, 1))
    x217 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x217 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (0, 1, 2, 3), (2, 3))
    x218 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x218 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 1, 2), (0, 4)) * -1.0
    x219 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x219 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 3), (1, 4))
    x220 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x220 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x220 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x221 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x221 += einsum(t1.bb, (0, 1), x220, (2, 3, 0, 1), (2, 3))
    x222 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x222 += einsum(t1.bb, (0, 1), x18, (2, 1), (0, 2))
    x223 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x223 += einsum(f.bb.oo, (0, 1), (0, 1))
    x223 += einsum(x217, (0, 1), (1, 0))
    x223 += einsum(x218, (0, 1), (0, 1)) * 2.0
    x223 += einsum(x219, (0, 1), (0, 1))
    x223 += einsum(x221, (0, 1), (1, 0)) * -1.0
    x223 += einsum(x222, (0, 1), (0, 1))
    l1new_bb += einsum(l1.bb, (0, 1), x223, (1, 2), (0, 2)) * -1.0
    l3new_abaaba += einsum(x223, (0, 1), l3.abaaba, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * -2.0
    x224 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x224 += einsum(x172, (0, 1), (0, 1)) * 0.3333333333333468
    x224 += einsum(x109, (0, 1), (0, 1)) * 0.6666666666666936
    x224 += einsum(x110, (0, 1), (0, 1)) * 0.3333333333333468
    x224 += einsum(x111, (0, 1), (0, 1))
    x224 += einsum(x112, (0, 1), (0, 1)) * 0.6666666666666667
    x224 += einsum(x113, (0, 1), (0, 1)) * 0.33333333333333354
    l1new_bb += einsum(f.bb.ov, (0, 1), x224, (2, 0), (1, 2)) * -2.9999999999998788
    x225 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x225 += einsum(x16, (0, 1), (0, 1))
    x225 += einsum(x17, (0, 1), (0, 1)) * -1.0
    l1new_bb += einsum(x172, (0, 1), x225, (1, 2), (2, 0)) * -1.0
    x226 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x226 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x227 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x227 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x227 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x227 += einsum(x226, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x227 += einsum(x226, (0, 1, 2, 3), (0, 2, 1, 3))
    x228 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x228 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 4, 2, 5))
    x229 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x229 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x229 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x230 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x230 += einsum(t2.aaaa, (0, 1, 2, 3), x229, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0
    x231 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x231 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x231 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x232 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x232 += einsum(t1.aa, (0, 1), x231, (2, 1, 3, 4), (0, 2, 3, 4))
    x233 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x233 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x233 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x233 += einsum(x228, (0, 1, 2, 3), (0, 1, 2, 3))
    x233 += einsum(x230, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x233 += einsum(x232, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x234 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x234 += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (0, 4, 2, 3))
    l2new_abab += einsum(l2.bbbb, (0, 1, 2, 3), x234, (3, 1, 4, 5), (5, 0, 4, 2)) * 2.0
    x235 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x235 += einsum(t2.bbbb, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 2, 4, 5))
    x236 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x236 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x236 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x237 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x237 += einsum(t2.abab, (0, 1, 2, 3), x236, (0, 4, 2, 5), (1, 3, 4, 5))
    x238 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x238 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x238 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    x238 += einsum(x235, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x238 += einsum(x237, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x239 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x239 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    x240 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x240 += einsum(t1.aa, (0, 1), x236, (0, 2, 1, 3), (2, 3))
    x241 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x241 += einsum(f.aa.ov, (0, 1), (0, 1))
    x241 += einsum(x239, (0, 1), (0, 1))
    x241 += einsum(x240, (0, 1), (0, 1)) * -1.0
    l2new_abab += einsum(x241, (0, 1), x63, (2, 3, 4, 0), (1, 3, 4, 2)) * -2.0
    l2new_abab += einsum(l1.bb, (0, 1), x241, (2, 3), (3, 0, 2, 1))
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 3, 1, 4, 5, 0)) * 2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 3, 1, 0, 4, 5)) * 2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 1, 3, 4, 0, 5)) * 2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (1, 2, 3, 4, 5, 0)) * 2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (1, 2, 3, 0, 4, 5)) * 2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 3, 1, 4, 0, 5)) * -2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 1, 3, 4, 5, 0)) * -2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (2, 1, 3, 0, 4, 5)) * -2.0
    l3new_aaaaaa += einsum(x241, (0, 1), l2.aaaa, (2, 3, 4, 5), (1, 2, 3, 4, 0, 5)) * -2.0
    l3new_babbab += einsum(x241, (0, 1), x55, (2, 3, 4, 5, 6, 0), (4, 1, 5, 3, 6, 2)) * 2.0
    l3new_babbab += einsum(x241, (0, 1), l2.bbbb, (2, 3, 4, 5), (2, 1, 3, 4, 0, 5)) * 2.0
    l3new_abaaba += einsum(x241, (0, 1), l2.abab, (2, 3, 4, 5), (1, 3, 2, 0, 5, 4))
    l3new_abaaba += einsum(x241, (0, 1), l2.abab, (2, 3, 4, 5), (2, 3, 1, 4, 5, 0))
    l3new_abaaba += einsum(x241, (0, 1), l2.abab, (2, 3, 4, 5), (2, 3, 1, 0, 5, 4)) * -1.0
    l3new_abaaba += einsum(x241, (0, 1), l2.abab, (2, 3, 4, 5), (1, 3, 2, 4, 5, 0)) * -1.0
    x242 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x242 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (2, 1, 3, 4), (3, 4, 0, 2))
    l2new_abab += einsum(x242, (0, 1, 2, 3), x58, (4, 1, 2, 5, 3, 6), (6, 0, 5, 4)) * 2.0
    x243 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x243 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 5), (3, 5, 0, 4))
    x244 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x244 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x244 += einsum(x242, (0, 1, 2, 3), (1, 0, 2, 3))
    x244 += einsum(x243, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x245 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x245 += einsum(t1.bb, (0, 1), x5, (2, 1, 3, 4), (0, 2, 3, 4))
    x246 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x246 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x246 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3))
    x246 += einsum(x27, (0, 1, 2, 3), (1, 0, 2, 3))
    x246 += einsum(x245, (0, 1, 2, 3), (1, 0, 3, 2))
    x247 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x247 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x248 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x248 += einsum(t1.aa, (0, 1), x226, (2, 3, 4, 1), (0, 2, 3, 4))
    x249 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x249 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x250 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x250 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x250 += einsum(x247, (0, 1, 2, 3), (3, 1, 2, 0))
    x250 += einsum(x248, (0, 1, 2, 3), (3, 1, 2, 0))
    x250 += einsum(x249, (0, 1, 2, 3), (2, 1, 3, 0))
    x250 += einsum(x249, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x251 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x251 += einsum(x40, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 0.9999999999999597
    x251 += einsum(t2.abab, (0, 1, 2, 3), x5, (4, 3, 5, 6), (1, 4, 0, 6, 5, 2)) * -1.0
    x251 += einsum(x41, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x252 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x252 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 3, 7, 1), (5, 7, 4, 6, 0, 2)) * -1.0
    l2new_aaaa += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), x252, (4, 1, 3, 5, 6, 7), (0, 2, 6, 7)) * 1.9999999999999203
    x253 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x253 += einsum(t2.abab, (0, 1, 2, 3), v.aaaa.ooov, (4, 5, 6, 2), (1, 3, 0, 4, 5, 6))
    x254 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x254 += einsum(t2.abab, (0, 1, 2, 3), x226, (4, 5, 6, 2), (1, 3, 4, 0, 6, 5))
    x255 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x255 += einsum(x252, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 0.9999999999999601
    x255 += einsum(x253, (0, 1, 2, 3, 4, 5), (0, 1, 4, 2, 3, 5))
    x255 += einsum(x253, (0, 1, 2, 3, 4, 5), (0, 1, 4, 2, 5, 3)) * -1.0
    x255 += einsum(x254, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x255 += einsum(x254, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x256 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x256 += einsum(v.aabb.ovvv, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 7, 3, 1), (5, 2, 0, 4, 6, 7)) * -0.9999999999999597
    x256 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), t3.abaaba, (4, 5, 6, 3, 7, 1), (5, 7, 0, 4, 6, 2)) * -0.9999999999999601
    x256 += einsum(x227, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 7, 3), (5, 7, 1, 4, 0, 6)) * -2.0
    x256 += einsum(x28, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 7, 1), (4, 6, 3, 5, 2, 7)) * -2.0
    x256 += einsum(x36, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 7, 3), (1, 7, 2, 4, 5, 6))
    x256 += einsum(t2.abab, (0, 1, 2, 3), x233, (4, 5, 6, 2), (1, 3, 5, 0, 4, 6))
    x256 += einsum(t2.aaaa, (0, 1, 2, 3), x238, (4, 5, 6, 3), (4, 5, 6, 0, 1, 2)) * -1.0
    x256 += einsum(x241, (0, 1), t3.abaaba, (2, 3, 4, 5, 6, 1), (3, 6, 0, 2, 4, 5)) * -0.9999999999999597
    x256 += einsum(t2.abab, (0, 1, 2, 3), x244, (3, 4, 5, 6), (1, 4, 6, 0, 5, 2)) * -1.0
    x256 += einsum(t2.abab, (0, 1, 2, 3), x246, (1, 4, 5, 6), (4, 3, 6, 0, 5, 2))
    x256 += einsum(t2.abab, (0, 1, 2, 3), x250, (0, 4, 5, 6), (1, 3, 5, 4, 6, 2))
    x256 += einsum(t1.bb, (0, 1), x251, (2, 0, 3, 4, 5, 6), (2, 1, 5, 3, 4, 6)) * -1.0
    x256 += einsum(t1.aa, (0, 1), x255, (2, 3, 4, 5, 0, 6), (2, 3, 6, 5, 4, 1)) * -1.0
    l1new_aa += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), x256, (4, 1, 6, 3, 5, 2), (0, 6)) * -2.0
    x257 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x257 += einsum(x35, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 0.9999999999999597
    x257 += einsum(t2.bbbb, (0, 1, 2, 3), x5, (4, 3, 5, 6), (0, 1, 4, 2, 6, 5))
    x257 += einsum(x37, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    x258 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x258 += einsum(v.aabb.ovvv, (0, 1, 2, 3), t3.babbab, (4, 5, 6, 7, 1, 3), (4, 6, 7, 2, 0, 5)) * -0.9999999999999597
    x258 += einsum(x227, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 3, 7), (4, 5, 6, 7, 1, 0)) * -0.5
    x258 += einsum(x28, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 7, 1), (4, 5, 6, 7, 3, 2)) * -1.5
    x258 += einsum(x36, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 3, 7), (4, 1, 6, 7, 2, 5))
    x258 += einsum(t2.abab, (0, 1, 2, 3), x238, (4, 5, 6, 2), (1, 4, 3, 5, 6, 0)) * -1.0
    x258 += einsum(x241, (0, 1), t3.babbab, (2, 3, 4, 5, 1, 6), (2, 4, 5, 6, 0, 3)) * -0.49999999999998007
    x258 += einsum(t2.bbbb, (0, 1, 2, 3), x244, (3, 4, 5, 6), (0, 1, 2, 4, 6, 5)) * -1.0
    x258 += einsum(t2.bbbb, (0, 1, 2, 3), x246, (1, 4, 5, 6), (0, 4, 2, 3, 6, 5))
    x258 += einsum(t1.bb, (0, 1), x257, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 6, 5))
    l1new_aa += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), x258, (3, 5, 0, 2, 6, 4), (1, 6)) * 2.0
    x259 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x259 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 6, 7, 3, 1), (4, 5, 6, 0, 2, 7)) * -1.0
    l2new_aaaa += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), x259, (5, 4, 3, 6, 7, 2), (0, 1, 6, 7)) * -5.9999999999997575
    x260 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x260 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x261 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x261 += einsum(t2.aaaa, (0, 1, 2, 3), x226, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x262 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x262 += einsum(x259, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -0.9999999999999596
    x262 += einsum(x260, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x262 += einsum(x260, (0, 1, 2, 3, 4, 5), (0, 1, 3, 4, 2, 5))
    x262 += einsum(x261, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    x262 += einsum(x261, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    x263 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x263 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 6, 7, 1, 3), (0, 4, 5, 6, 7, 2)) * -0.9999999999999596
    x263 += einsum(x227, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 2, 6, 7, 3), (1, 4, 0, 5, 6, 7)) * -1.5
    x263 += einsum(x28, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 1, 7), (3, 4, 2, 5, 6, 7)) * -0.5
    x263 += einsum(t2.aaaa, (0, 1, 2, 3), x233, (4, 5, 6, 3), (5, 0, 4, 1, 2, 6))
    x263 += einsum(x241, (0, 1), t3.aaaaaa, (2, 3, 4, 5, 6, 1), (0, 2, 3, 4, 5, 6)) * 0.4999999999999798
    x263 += einsum(t2.aaaa, (0, 1, 2, 3), x250, (1, 4, 5, 6), (5, 0, 6, 4, 2, 3))
    x263 += einsum(t1.aa, (0, 1), x262, (2, 3, 4, 5, 0, 6), (5, 3, 4, 2, 6, 1))
    l1new_aa += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), x263, (6, 3, 4, 5, 2, 1), (0, 6)) * 6.0
    x264 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x264 += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (4, 5, 2, 0))
    x265 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x265 += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 1, 5), (4, 5, 2, 0))
    x266 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x266 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 3, 5, 7, 0, 2), (6, 7, 4, 1))
    x267 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x267 += einsum(t2.bbbb, (0, 1, 2, 3), x80, (0, 1, 4, 3, 5, 6), (4, 2, 5, 6)) * -1.0
    x268 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x268 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 5, 4, 7, 2, 1), (6, 7, 3, 0))
    x269 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x269 += einsum(t2.abab, (0, 1, 2, 3), x91, (1, 4, 0, 5, 6, 2), (4, 3, 5, 6)) * -1.0
    x270 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x270 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.abaaba, (4, 6, 5, 1, 7, 2), (6, 7, 3, 0))
    x271 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x271 += einsum(l2.abab, (0, 1, 2, 3), (3, 1, 2, 0))
    x271 += einsum(x264, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x271 += einsum(x265, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x271 += einsum(x266, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x271 += einsum(x267, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x271 += einsum(x268, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x271 += einsum(x269, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x271 += einsum(x270, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x271 += einsum(t1.bb, (0, 1), x96, (0, 2, 3, 4), (2, 1, 3, 4)) * -1.0
    l1new_aa += einsum(v.aabb.vvov, (0, 1, 2, 3), x271, (2, 3, 4, 1), (0, 4))
    x272 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x272 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 5, 6, 1, 0), (6, 4, 5, 2))
    x273 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x273 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    x274 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x274 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 3, 4, 0), (4, 2, 3, 1))
    x274 += einsum(x272, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x274 += einsum(x273, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    l1new_aa += einsum(v.aaaa.vvvv, (0, 1, 2, 3), x274, (4, 1, 2, 3), (0, 4)) * 2.0
    x275 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x275 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (4, 5, 3, 0, 6, 1), (4, 2, 6, 5))
    x276 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x276 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 5, 2, 6, 1, 0), (5, 3, 6, 4))
    x277 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x277 += einsum(t1.bb, (0, 1), l2.abab, (2, 3, 4, 0), (3, 1, 4, 2)) * 0.5
    x277 += einsum(x275, (0, 1, 2, 3), (0, 1, 2, 3))
    x277 += einsum(x276, (0, 1, 2, 3), (0, 1, 2, 3))
    l1new_aa += einsum(v.aabb.vvvv, (0, 1, 2, 3), x277, (2, 3, 4, 1), (0, 4)) * 2.0
    x278 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x278 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x278 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x279 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x279 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 4, 0, 5))
    x280 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x280 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 5, 1), (2, 4, 0, 5))
    x281 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x281 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7))
    x282 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x282 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    x283 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x283 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    x284 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x284 += einsum(x279, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x284 += einsum(x280, (0, 1, 2, 3), (0, 1, 2, 3))
    x284 += einsum(x281, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x284 += einsum(x282, (0, 1, 2, 3), (0, 1, 2, 3))
    x284 += einsum(x283, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.25
    l1new_aa += einsum(x278, (0, 1, 2, 3), x284, (4, 0, 3, 2), (1, 4)) * 4.0
    x285 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x285 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x285 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x286 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x286 += einsum(t2.abab, (0, 1, 2, 3), x58, (1, 3, 4, 0, 5, 6), (4, 5, 6, 2))
    x287 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x287 += einsum(t2.aaaa, (0, 1, 2, 3), x189, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2)) * -1.0
    x288 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x288 += einsum(x191, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.3333333333333333
    x288 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x288 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x289 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x289 += einsum(x286, (0, 1, 2, 3), (0, 1, 2, 3))
    x289 += einsum(x287, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x289 += einsum(t1.aa, (0, 1), x288, (0, 2, 3, 4), (2, 3, 4, 1)) * 3.0
    l1new_aa += einsum(x285, (0, 1, 2, 3), x289, (4, 0, 2, 3), (1, 4)) * -2.0
    x290 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x290 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), (1, 5, 2, 4))
    x291 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x291 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 7, 1, 2), (0, 7, 4, 6))
    x292 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x292 += einsum(t2.bbbb, (0, 1, 2, 3), x55, (0, 1, 4, 3, 5, 6), (4, 2, 5, 6))
    x293 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x293 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 0, 7, 2), (1, 7, 3, 6))
    x294 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x294 += einsum(t2.abab, (0, 1, 2, 3), x58, (1, 4, 5, 0, 6, 2), (4, 3, 5, 6)) * -1.0
    x295 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x295 += einsum(x290, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x295 += einsum(x291, (0, 1, 2, 3), (0, 1, 2, 3))
    x295 += einsum(x292, (0, 1, 2, 3), (1, 0, 2, 3))
    x295 += einsum(x293, (0, 1, 2, 3), (0, 1, 2, 3))
    x295 += einsum(x294, (0, 1, 2, 3), (1, 0, 2, 3))
    x295 += einsum(t1.bb, (0, 1), x101, (0, 2, 3, 4), (1, 2, 3, 4)) * 0.5
    l1new_aa += einsum(v.aabb.ovvv, (0, 1, 2, 3), x295, (3, 2, 4, 0), (1, 4)) * -2.0
    x296 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x296 += einsum(x275, (0, 1, 2, 3), (0, 1, 2, 3))
    x296 += einsum(x276, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(x296, (0, 1, 2, 3), x71, (4, 5, 0, 1), (3, 5, 2, 4)) * -2.0
    l2new_abab += einsum(v.aabb.vvov, (0, 1, 2, 3), x296, (4, 3, 5, 1), (0, 4, 5, 2)) * -2.0
    l2new_abab += einsum(x28, (0, 1, 2, 3), x296, (4, 1, 2, 5), (5, 4, 3, 0)) * 2.0
    x297 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x297 += einsum(x191, (0, 1, 2, 3), (1, 0, 2, 3))
    x297 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x297 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    l1new_aa += einsum(v.aaaa.oovv, (0, 1, 2, 3), x297, (0, 4, 1, 3), (2, 4)) * -2.0
    x298 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x298 += einsum(x196, (0, 1), (0, 1))
    x298 += einsum(x197, (0, 1), (0, 1)) * 2.0
    x298 += einsum(x198, (0, 1), (0, 1)) * 0.9999999999999601
    x298 += einsum(x199, (0, 1), (0, 1)) * 1.9999999999999194
    x298 += einsum(x200, (0, 1), (0, 1)) * 2.9999999999998788
    x299 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x299 += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), (3, 4, 1, 2))
    x299 += einsum(x60, (0, 1, 2, 3), (0, 1, 2, 3))
    x299 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 5, 3, 6, 0, 1), (4, 6, 2, 5)) * 2.0
    x299 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x299 += einsum(l2.aaaa, (0, 1, 2, 3), t3.abaaba, (4, 5, 3, 0, 6, 1), (5, 6, 2, 4)) * 2.0
    x299 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x299 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x55, (2, 1, 5, 4, 6, 7), (0, 3, 6, 7)) * 3.0
    x299 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x80, (2, 0, 6, 5, 7, 4), (6, 3, 7, 1)) * -2.0
    x299 += einsum(t2.bbbb, (0, 1, 2, 3), x98, (1, 0, 4, 3, 5, 6), (4, 2, 5, 6)) * -2.0
    x299 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x58, (2, 5, 6, 1, 7, 4), (0, 3, 6, 7)) * -4.0
    x299 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x91, (1, 6, 7, 2, 5, 3), (6, 4, 7, 0)) * 2.0
    x299 += einsum(t2.abab, (0, 1, 2, 3), x99, (1, 4, 5, 0, 6, 2), (4, 3, 5, 6)) * 2.0
    x299 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x189, (6, 0, 2, 7, 5, 3), (1, 4, 6, 7)) * -3.0
    x299 += einsum(t2.abab, (0, 1, 2, 3), x296, (3, 4, 5, 2), (1, 4, 5, 0)) * -2.0
    x299 += einsum(t2.bbbb, (0, 1, 2, 3), x101, (1, 3, 4, 5), (0, 2, 4, 5)) * 2.0
    x299 += einsum(t2.abab, (0, 1, 2, 3), x96, (1, 4, 5, 2), (4, 3, 5, 0)) * -1.0
    x299 += einsum(t2.abab, (0, 1, 2, 3), x297, (0, 4, 5, 2), (1, 3, 4, 5)) * -2.0
    x299 += einsum(t1.bb, (0, 1), x108, (0, 2, 3, 4), (2, 1, 3, 4)) * -1.0
    x299 += einsum(t1.bb, (0, 1), x298, (2, 3), (0, 1, 2, 3))
    l1new_aa += einsum(v.aabb.ovov, (0, 1, 2, 3), x299, (2, 3, 4, 0), (1, 4)) * -1.0
    x300 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x300 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (0, 2, 3, 5, 6, 7), (6, 7, 1, 4))
    x301 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x301 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x58, (1, 4, 6, 2, 7, 5), (6, 7, 0, 3)) * -1.0
    x302 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x302 += einsum(t1.aa, (0, 1), x58, (2, 3, 4, 5, 6, 1), (2, 3, 4, 5, 0, 6))
    x303 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x303 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x189, (6, 2, 1, 7, 4, 5), (6, 7, 0, 3)) * -1.0
    x304 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x304 += einsum(t1.aa, (0, 1), x189, (2, 3, 4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x305 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x305 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), (2, 3, 4, 5))
    x306 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x306 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 7, 0, 1, 2), (3, 5, 6, 7))
    x307 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x307 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    x308 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x308 += einsum(x191, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x308 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    x308 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    l2new_abab += einsum(v.aabb.ooov, (0, 1, 2, 3), x308, (1, 4, 0, 5), (5, 3, 4, 2)) * 2.0
    x309 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x309 += einsum(x305, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x309 += einsum(x306, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.9999999999999601
    x309 += einsum(x307, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.9999999999998788
    x309 += einsum(t1.aa, (0, 1), x308, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x310 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x310 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 0), (1, 2, 3, 4))
    x310 += einsum(x191, (0, 1, 2, 3), (1, 0, 2, 3))
    x310 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 5, 6, 1, 0), (2, 4, 5, 6))
    x310 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x310 += einsum(l2.aaaa, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6)) * 3.0
    x310 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x310 += einsum(x300, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x310 += einsum(x301, (0, 1, 2, 3), (0, 2, 1, 3)) * 2.0
    x310 += einsum(t2.aaaa, (0, 1, 2, 3), x272, (4, 3, 2, 5), (4, 0, 1, 5)) * -1.0
    x310 += einsum(t2.abab, (0, 1, 2, 3), x302, (1, 3, 4, 0, 5, 6), (4, 6, 5, 2)) * -1.0
    x310 += einsum(x303, (0, 1, 2, 3), (0, 2, 1, 3)) * 4.5
    x310 += einsum(t2.aaaa, (0, 1, 2, 3), x304, (4, 0, 1, 5, 6, 3), (4, 6, 5, 2)) * -3.0
    x310 += einsum(t2.abab, (0, 1, 2, 3), x63, (1, 3, 4, 5), (4, 0, 5, 2))
    x310 += einsum(t2.aaaa, (0, 1, 2, 3), x194, (4, 1, 5, 3), (4, 0, 5, 2)) * -6.0
    x310 += einsum(t1.aa, (0, 1), x309, (0, 2, 3, 4), (2, 4, 3, 1)) * -1.0
    x310 += einsum(t1.aa, (0, 1), x298, (2, 3), (2, 0, 3, 1)) * 0.5
    l1new_aa += einsum(v.aaaa.ovov, (0, 1, 2, 3), x310, (4, 0, 2, 1), (3, 4)) * -2.0
    x311 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x311 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (4, 2, 5, 3), (1, 5, 0, 4))
    x312 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x312 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 5, 2, 6, 1, 3), (4, 6, 5, 0))
    x313 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x313 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 1, 6, 3), (5, 6, 4, 0))
    x314 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x314 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x314 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x314 += einsum(x226, (0, 1, 2, 3), (1, 0, 2, 3))
    x314 += einsum(x226, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x315 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x315 += einsum(t2.abab, (0, 1, 2, 3), x314, (4, 5, 0, 2), (1, 3, 4, 5))
    x316 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x316 += einsum(t2.bbbb, (0, 1, 2, 3), x5, (1, 3, 4, 5), (0, 2, 4, 5)) * 2.0
    x317 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x317 += einsum(t2.abab, (0, 1, 2, 3), x36, (1, 4, 5, 2), (4, 3, 0, 5))
    x318 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x318 += einsum(x241, (0, 1), t2.abab, (2, 3, 1, 4), (3, 4, 2, 0))
    x319 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x319 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x319 += einsum(x242, (0, 1, 2, 3), (1, 0, 3, 2))
    x320 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x320 += einsum(t1.bb, (0, 1), x319, (1, 2, 3, 4), (0, 2, 3, 4))
    x321 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x321 += einsum(t1.bb, (0, 1), x126, (0, 2, 3, 4), (2, 1, 3, 4))
    x322 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x322 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x322 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3))
    x322 += einsum(x311, (0, 1, 2, 3), (0, 1, 2, 3))
    x322 += einsum(x312, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x322 += einsum(x313, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x322 += einsum(x315, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x322 += einsum(x316, (0, 1, 2, 3), (0, 1, 3, 2))
    x322 += einsum(x317, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x322 += einsum(x318, (0, 1, 2, 3), (0, 1, 2, 3))
    x322 += einsum(x320, (0, 1, 2, 3), (0, 1, 3, 2))
    x322 += einsum(x321, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l1new_aa += einsum(l2.abab, (0, 1, 2, 3), x322, (3, 1, 2, 4), (0, 4)) * -1.0
    x323 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x323 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x324 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x324 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 1), (4, 5, 0, 6))
    x325 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x325 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 2, 6, 1, 3), (4, 5, 0, 6))
    x326 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x326 += einsum(t2.aaaa, (0, 1, 2, 3), x227, (4, 1, 5, 3), (0, 4, 5, 2)) * 2.0
    x327 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x327 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x328 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x328 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x328 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x328 += einsum(x327, (0, 1, 2, 3), (0, 1, 2, 3))
    x329 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x329 += einsum(t1.aa, (0, 1), x250, (0, 2, 3, 4), (2, 3, 4, 1))
    x330 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x330 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x330 += einsum(x323, (0, 1, 2, 3), (2, 1, 0, 3))
    x330 += einsum(x324, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x330 += einsum(x325, (0, 1, 2, 3), (2, 1, 0, 3)) * -3.0
    x330 += einsum(x326, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x330 += einsum(t2.abab, (0, 1, 2, 3), x28, (1, 3, 4, 5), (5, 0, 4, 2))
    x330 += einsum(x241, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4))
    x330 += einsum(t1.aa, (0, 1), x328, (2, 3, 1, 4), (3, 2, 0, 4))
    x330 += einsum(x329, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    l1new_aa += einsum(l2.aaaa, (0, 1, 2, 3), x330, (4, 2, 3, 1), (0, 4)) * 2.0
    x331 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x331 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    x331 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x332 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x332 += einsum(t1.aa, (0, 1), x331, (2, 3, 4, 1), (0, 2, 3, 4))
    l1new_aa += einsum(v.aaaa.ooov, (0, 1, 2, 3), x332, (2, 4, 0, 1), (3, 4)) * 2.0
    x333 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x333 += einsum(x300, (0, 1, 2, 3), (0, 2, 1, 3))
    x333 += einsum(x301, (0, 1, 2, 3), (0, 2, 1, 3)) * 4.0
    x333 += einsum(x303, (0, 1, 2, 3), (0, 2, 1, 3)) * 9.0
    x333 += einsum(t2.aaaa, (0, 1, 2, 3), x273, (4, 2, 3, 5), (4, 0, 1, 5)) * 6.0
    x333 += einsum(t2.abab, (0, 1, 2, 3), x63, (1, 3, 4, 5), (4, 0, 5, 2)) * 2.0
    x333 += einsum(t2.aaaa, (0, 1, 2, 3), x194, (4, 1, 5, 3), (4, 0, 5, 2)) * -12.0
    x333 += einsum(t1.aa, (0, 1), x332, (2, 3, 0, 4), (3, 4, 2, 1)) * -2.0
    x333 += einsum(t1.aa, (0, 1), x298, (2, 3), (2, 0, 3, 1))
    l1new_aa += einsum(v.aaaa.ovov, (0, 1, 2, 3), x333, (4, 0, 2, 3), (1, 4))
    x334 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x334 += einsum(t1.aa, (0, 1), (0, 1)) * -1.0
    x334 += einsum(x182, (0, 1), (0, 1)) * -1.0
    x334 += einsum(x183, (0, 1), (0, 1)) * -2.0
    x334 += einsum(x184, (0, 1), (0, 1)) * -1.0
    x334 += einsum(x185, (0, 1), (0, 1)) * -2.0
    x334 += einsum(x186, (0, 1), (0, 1)) * -3.0
    x334 += einsum(x187, (0, 1), (0, 1)) * 0.9999999999999601
    x334 += einsum(x188, (0, 1), (0, 1)) * 1.9999999999999194
    x334 += einsum(x190, (0, 1), (0, 1)) * 2.9999999999998788
    x334 += einsum(t2.abab, (0, 1, 2, 3), x63, (1, 3, 0, 4), (4, 2)) * 2.0
    x334 += einsum(t2.aaaa, (0, 1, 2, 3), x194, (0, 1, 4, 3), (4, 2)) * -6.0
    x334 += einsum(t1.aa, (0, 1), x201, (0, 2), (2, 1))
    l1new_aa += einsum(x334, (0, 1), x236, (0, 2, 1, 3), (3, 2))
    x335 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x335 += einsum(x175, (0, 1), (0, 1)) * 0.5
    x335 += einsum(x176, (0, 1), (0, 1)) * 0.5
    x335 += einsum(x177, (0, 1), (0, 1))
    x335 += einsum(x180, (0, 1), (0, 1)) * 1.4999999999999394
    x336 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x336 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x336 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    l1new_aa += einsum(x335, (0, 1), x336, (2, 1, 0, 3), (3, 2)) * -2.0
    l2new_abab += einsum(x100, (0, 1, 2, 3), x336, (4, 3, 2, 5), (5, 1, 4, 0)) * -2.0
    x337 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x337 += einsum(x157, (0, 1), (0, 1)) * 0.5000000000000202
    x337 += einsum(x158, (0, 1), (0, 1)) * 1.0000000000000404
    x337 += einsum(x159, (0, 1), (0, 1)) * 0.5000000000000202
    x337 += einsum(x208, (0, 1), (0, 1)) * 1.4999999999999998
    x337 += einsum(x160, (0, 1), (0, 1))
    x337 += einsum(x161, (0, 1), (1, 0)) * 0.5000000000000002
    l1new_aa += einsum(x337, (0, 1), v.aabb.ovvv, (2, 3, 1, 0), (3, 2)) * 1.9999999999999194
    x338 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x338 += einsum(l1.bb, (0, 1), (1, 0)) * -1.0
    x338 += einsum(t1.bb, (0, 1), (0, 1)) * -1.0
    x338 += einsum(x164, (0, 1), (0, 1)) * -2.0
    x338 += einsum(x165, (0, 1), (0, 1)) * -1.0
    x338 += einsum(x166, (0, 1), (0, 1)) * -3.0
    x338 += einsum(x167, (0, 1), (0, 1)) * -2.0
    x338 += einsum(x168, (0, 1), (0, 1)) * -1.0
    x338 += einsum(x169, (0, 1), (0, 1)) * 2.9999999999998788
    x338 += einsum(x170, (0, 1), (0, 1)) * 1.9999999999999194
    x338 += einsum(x171, (0, 1), (0, 1)) * 0.9999999999999601
    x338 += einsum(t2.bbbb, (0, 1, 2, 3), x130, (0, 1, 4, 3), (4, 2)) * -2.0
    x338 += einsum(t2.abab, (0, 1, 2, 3), x131, (1, 4, 0, 2), (4, 3)) * 2.0
    x338 += einsum(t1.bb, (0, 1), x173, (0, 2), (2, 1))
    l1new_aa += einsum(x338, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (3, 2)) * -1.0
    x339 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x339 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3))
    x339 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.9999999999999194
    x339 += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.9999999999999194
    x339 += einsum(x105, (0, 1, 2, 3), (0, 1, 2, 3))
    x339 += einsum(x107, (0, 1, 2, 3), (1, 0, 3, 2))
    l1new_aa += einsum(v.aabb.ovoo, (0, 1, 2, 3), x339, (3, 2, 4, 0), (1, 4))
    x340 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x340 += einsum(x178, (0, 1), (0, 1)) * 0.5000000000000002
    x340 += einsum(x179, (0, 1), (0, 1))
    l1new_aa += einsum(x340, (0, 1), x336, (2, 1, 0, 3), (3, 2)) * -1.9999999999999194
    x341 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x341 += einsum(x307, (0, 1, 2, 3), (0, 3, 2, 1)) * -2.9999999999998788
    x341 += einsum(t1.aa, (0, 1), x288, (2, 3, 4, 1), (3, 2, 4, 0)) * 3.0
    l1new_aa += einsum(v.aaaa.ooov, (0, 1, 2, 3), x341, (4, 0, 2, 1), (3, 4)) * -2.0
    x342 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x342 += einsum(x305, (0, 1, 2, 3), (1, 0, 3, 2))
    x342 += einsum(x306, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.9999999999999601
    l1new_aa += einsum(v.aaaa.ooov, (0, 1, 2, 3), x342, (1, 4, 2, 0), (3, 4)) * -2.0
    x343 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x343 += einsum(x195, (0, 1), (0, 1)) * 1.00000000000004
    x343 += einsum(x196, (0, 1), (0, 1)) * 1.00000000000004
    x343 += einsum(x197, (0, 1), (0, 1)) * 2.00000000000008
    x343 += einsum(x198, (0, 1), (0, 1))
    x343 += einsum(x199, (0, 1), (0, 1)) * 1.9999999999999991
    x344 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x344 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x344 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    l1new_aa += einsum(x343, (0, 1), x344, (1, 0, 2, 3), (3, 2)) * -0.9999999999999601
    x345 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x345 += einsum(x172, (0, 1), (0, 1))
    x345 += einsum(x109, (0, 1), (0, 1)) * 2.0
    x345 += einsum(x110, (0, 1), (0, 1))
    x345 += einsum(x111, (0, 1), (1, 0)) * 2.9999999999998788
    x345 += einsum(x112, (0, 1), (1, 0)) * 1.9999999999999194
    x345 += einsum(x113, (0, 1), (0, 1)) * 0.9999999999999601
    l1new_aa += einsum(x345, (0, 1), v.aabb.ovoo, (2, 3, 1, 0), (3, 2)) * -1.0
    x346 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x346 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x346 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l1new_aa += einsum(l1.aa, (0, 1), x346, (1, 2, 0, 3), (3, 2)) * -1.0
    x347 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x347 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 1), (2, 3))
    x348 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x348 += einsum(f.aa.vv, (0, 1), (0, 1))
    x348 += einsum(x347, (0, 1), (1, 0))
    x348 += einsum(t1.aa, (0, 1), x278, (0, 1, 2, 3), (3, 2)) * -1.0
    l1new_aa += einsum(l1.aa, (0, 1), x348, (0, 2), (2, 1))
    x349 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x349 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 1), (2, 3))
    x350 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x350 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 1, 3), (0, 4))
    x351 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x351 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 1, 3), (0, 4))
    x352 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x352 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x352 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x353 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x353 += einsum(t1.aa, (0, 1), x352, (2, 3, 0, 1), (2, 3))
    x354 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x354 += einsum(t1.aa, (0, 1), x241, (2, 1), (0, 2))
    x355 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x355 += einsum(f.aa.oo, (0, 1), (0, 1))
    x355 += einsum(x349, (0, 1), (1, 0))
    x355 += einsum(x350, (0, 1), (0, 1))
    x355 += einsum(x351, (0, 1), (0, 1)) * 2.0
    x355 += einsum(x353, (0, 1), (1, 0)) * -1.0
    x355 += einsum(x354, (0, 1), (0, 1))
    l1new_aa += einsum(l1.aa, (0, 1), x355, (1, 2), (0, 2)) * -1.0
    l2new_abab += einsum(x355, (0, 1), l2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    l3new_babbab += einsum(x355, (0, 1), l3.babbab, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * -2.0
    x356 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x356 += einsum(x195, (0, 1), (0, 1)) * 1.00000000000004
    x356 += einsum(x196, (0, 1), (0, 1)) * 1.00000000000004
    x356 += einsum(x197, (0, 1), (0, 1)) * 2.00000000000008
    x356 += einsum(x198, (0, 1), (0, 1))
    x356 += einsum(x199, (0, 1), (0, 1)) * 1.9999999999999991
    x356 += einsum(x200, (0, 1), (0, 1)) * 2.9999999999999982
    l1new_aa += einsum(f.aa.ov, (0, 1), x356, (2, 0), (1, 2)) * -0.9999999999999601
    l2new_abab += einsum(x356, (0, 1), v.aabb.ovov, (1, 2, 3, 4), (2, 4, 0, 3)) * -0.9999999999999601
    x357 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x357 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x357 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    l1new_aa += einsum(x200, (0, 1), x357, (0, 1, 2, 3), (3, 2)) * 2.9999999999998788
    x358 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x358 += einsum(x239, (0, 1), (0, 1))
    x358 += einsum(x240, (0, 1), (0, 1)) * -1.0
    l1new_aa += einsum(x195, (0, 1), x358, (1, 2), (2, 0)) * -1.0
    x359 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x359 += einsum(l1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 0), (1, 2, 3, 4))
    x360 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x360 += einsum(l2.abab, (0, 1, 2, 3), x234, (3, 1, 4, 5), (2, 4, 0, 5))
    x361 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x361 += einsum(x2, (0, 1, 2, 3), x93, (0, 1, 4, 5), (4, 2, 5, 3))
    x362 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x362 += einsum(x272, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    x362 += einsum(x273, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x363 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x363 += einsum(x285, (0, 1, 2, 3), x362, (4, 2, 5, 3), (0, 4, 1, 5)) * 6.0
    x364 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x364 += einsum(x192, (0, 1, 2, 3), (0, 1, 2, 3))
    x364 += einsum(x193, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0000000000000004
    x365 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x365 += einsum(t1.aa, (0, 1), x364, (2, 0, 3, 4), (2, 3, 1, 4)) * 0.22222222222223104
    x366 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x366 += einsum(x279, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.11111111111111552
    x366 += einsum(x280, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.4444444444444621
    x366 += einsum(x281, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.11111111111111108
    x366 += einsum(x282, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.44444444444444453
    x366 += einsum(x286, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.22222222222223104
    x366 += einsum(x283, (0, 1, 2, 3), (0, 1, 2, 3))
    x366 += einsum(x287, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666932
    x366 += einsum(x365, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x367 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x367 += einsum(x229, (0, 1, 2, 3), x366, (4, 0, 5, 3), (1, 4, 2, 5)) * 8.999999999999643
    x368 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x368 += einsum(t1.bb, (0, 1), x106, (0, 2, 3, 4), (2, 1, 3, 4)) * 2.0
    x369 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x369 += einsum(l2.abab, (0, 1, 2, 3), (3, 1, 2, 0))
    x369 += einsum(x264, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x369 += einsum(x265, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x369 += einsum(x266, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.999999999999881
    x369 += einsum(x267, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x369 += einsum(x268, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.999999999999842
    x369 += einsum(x269, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x369 += einsum(x270, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.999999999999881
    x369 += einsum(x368, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x370 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x370 += einsum(v.aabb.ovov, (0, 1, 2, 3), x369, (2, 3, 4, 5), (0, 4, 1, 5))
    x371 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x371 += einsum(v.aabb.ovvv, (0, 1, 2, 3), x296, (2, 3, 4, 5), (0, 4, 1, 5)) * 2.0
    x372 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x372 += einsum(t1.aa, (0, 1), x278, (2, 3, 1, 4), (0, 2, 3, 4))
    x373 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x373 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x373 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x373 += einsum(x372, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x374 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x374 += einsum(l2.aaaa, (0, 1, 2, 3), x373, (3, 4, 5, 1), (2, 4, 0, 5)) * 2.0
    x375 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x375 += einsum(x308, (0, 1, 2, 3), x357, (1, 4, 2, 5), (0, 4, 3, 5)) * 2.0
    x376 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x376 += einsum(x176, (0, 1), (0, 1))
    x376 += einsum(x177, (0, 1), (0, 1)) * 2.0
    x376 += einsum(x178, (0, 1), (0, 1)) * 0.9999999999999601
    x376 += einsum(x179, (0, 1), (0, 1)) * 1.9999999999999194
    x376 += einsum(x180, (0, 1), (0, 1)) * 2.9999999999998788
    x377 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x377 += einsum(x376, (0, 1), v.aaaa.ovov, (2, 1, 3, 4), (2, 3, 0, 4))
    x378 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x378 += einsum(v.aabb.ovoo, (0, 1, 2, 3), x96, (2, 3, 4, 5), (0, 4, 1, 5))
    x379 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x379 += einsum(x226, (0, 1, 2, 3), (0, 1, 2, 3))
    x379 += einsum(x226, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x379, (0, 1, 2, 3), x60, (4, 5, 0, 1), (3, 5, 2, 4))
    l3new_babbab += einsum(x379, (0, 1, 2, 3), x55, (4, 5, 6, 7, 0, 2), (6, 3, 7, 5, 1, 4)) * 2.0
    x380 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x380 += einsum(x191, (0, 1, 2, 3), x379, (0, 4, 2, 5), (1, 4, 3, 5)) * 2.0
    x381 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x381 += einsum(x201, (0, 1), v.aaaa.ovov, (2, 3, 1, 4), (0, 2, 4, 3))
    x382 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x382 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x382 += einsum(x226, (0, 1, 2, 3), (0, 1, 2, 3))
    x383 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x383 += einsum(l1.aa, (0, 1), x382, (1, 2, 3, 4), (2, 3, 0, 4))
    x384 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x384 += einsum(f.aa.ov, (0, 1), l1.aa, (2, 3), (0, 3, 1, 2))
    x384 += einsum(x359, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x384 += einsum(x360, (0, 1, 2, 3), (0, 1, 2, 3))
    x384 += einsum(x361, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x384 += einsum(x363, (0, 1, 2, 3), (1, 0, 3, 2))
    x384 += einsum(x367, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x384 += einsum(x370, (0, 1, 2, 3), (1, 0, 3, 2))
    x384 += einsum(x371, (0, 1, 2, 3), (1, 0, 3, 2))
    x384 += einsum(x374, (0, 1, 2, 3), (0, 1, 2, 3))
    x384 += einsum(x375, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x384 += einsum(x377, (0, 1, 2, 3), (1, 0, 2, 3))
    x384 += einsum(x378, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x384 += einsum(x380, (0, 1, 2, 3), (0, 1, 2, 3))
    x384 += einsum(x381, (0, 1, 2, 3), (0, 1, 3, 2))
    x384 += einsum(x383, (0, 1, 2, 3), (0, 1, 2, 3))
    x384 += einsum(l1.aa, (0, 1), x358, (2, 3), (1, 2, 0, 3))
    l2new_aaaa += einsum(x384, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new_aaaa += einsum(x384, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new_aaaa += einsum(x384, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new_aaaa += einsum(x384, (0, 1, 2, 3), (3, 2, 1, 0))
    x385 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x385 += einsum(f.aa.vv, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    x386 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x386 += einsum(x19, (0, 1, 2, 3), x91, (0, 1, 4, 5, 6, 3), (4, 5, 6, 2))
    x387 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x387 += einsum(t1.bb, (0, 1), v.aabb.vvvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x388 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x388 += einsum(t2.bbbb, (0, 1, 2, 3), v.aabb.vvov, (4, 5, 1, 3), (0, 2, 4, 5))
    x389 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x389 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (0, 4, 5, 3), (1, 5, 2, 4))
    x390 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x390 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x391 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x391 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (0, 4, 2, 5, 6, 1), (4, 6, 5, 3)) * -1.0
    x392 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x392 += einsum(t2.abab, (0, 1, 2, 3), x285, (0, 2, 4, 5), (1, 3, 4, 5))
    x393 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x393 += einsum(t2.abab, (0, 1, 2, 3), x36, (1, 4, 0, 5), (4, 3, 2, 5))
    x394 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x394 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1))
    x394 += einsum(x387, (0, 1, 2, 3), (0, 1, 3, 2))
    x394 += einsum(x388, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x394 += einsum(x389, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x394 += einsum(x390, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.999999999999921
    x394 += einsum(x391, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.99999999999992
    x394 += einsum(x392, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x394 += einsum(x393, (0, 1, 2, 3), (0, 1, 3, 2))
    x395 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x395 += einsum(x394, (0, 1, 2, 3), l3.abaaba, (4, 1, 3, 5, 0, 6), (5, 6, 4, 2)) * -2.0
    x396 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x396 += einsum(t1.aa, (0, 1), v.aaaa.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x397 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x397 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 5, 1, 3), (0, 2, 4, 5))
    x398 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x398 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 0, 5, 3, 6), (4, 5, 6, 1))
    x399 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x399 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x400 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x400 += einsum(t2.aaaa, (0, 1, 2, 3), x231, (1, 3, 4, 5), (0, 2, 4, 5)) * 2.0
    x401 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x401 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x401 += einsum(x226, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x402 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x402 += einsum(t2.aaaa, (0, 1, 2, 3), x401, (0, 4, 1, 5), (4, 2, 3, 5)) * -1.0
    x403 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x403 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x403 += einsum(x396, (0, 1, 2, 3), (0, 2, 3, 1))
    x403 += einsum(x397, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x403 += einsum(x398, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.9999999999999606
    x403 += einsum(x399, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.999999999999881
    x403 += einsum(x400, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x403 += einsum(x402, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x404 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x404 += einsum(x403, (0, 1, 2, 3), l3.aaaaaa, (4, 1, 2, 5, 6, 0), (5, 6, 4, 3)) * -6.0
    x405 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x405 += einsum(t1.bb, (0, 1), x36, (0, 2, 3, 4), (2, 1, 3, 4))
    x406 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x406 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x406 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    x406 += einsum(x235, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x406 += einsum(x237, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x406 += einsum(x405, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new_abab += einsum(x406, (0, 1, 2, 3), x55, (0, 4, 5, 1, 6, 2), (3, 5, 6, 4)) * 2.0
    x407 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x407 += einsum(x406, (0, 1, 2, 3), x58, (0, 1, 4, 5, 2, 6), (4, 5, 6, 3)) * 2.0
    x408 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x408 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x409 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x409 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x409 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x409 += einsum(x408, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x409 += einsum(x228, (0, 1, 2, 3), (0, 1, 2, 3))
    x409 += einsum(x230, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x410 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x410 += einsum(x409, (0, 1, 2, 3), x189, (4, 5, 0, 1, 2, 6), (4, 5, 6, 3)) * 6.0
    x411 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x411 += einsum(t1.aa, (0, 1), x226, (2, 3, 0, 4), (2, 3, 1, 4))
    x412 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x412 += einsum(t1.aa, (0, 1), x278, (2, 1, 3, 4), (0, 2, 3, 4))
    x413 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x413 += einsum(x411, (0, 1, 2, 3), (0, 1, 2, 3))
    x413 += einsum(x412, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x414 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x414 += einsum(x413, (0, 1, 2, 3), x189, (4, 5, 0, 1, 2, 6), (4, 5, 6, 3)) * 6.0
    x415 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x415 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x415 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new_abab += einsum(x415, (0, 1, 2, 3), x80, (0, 4, 1, 5, 6, 2), (3, 5, 6, 4)) * 2.0
    x416 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x416 += einsum(x415, (0, 1, 2, 3), x91, (0, 1, 4, 5, 2, 6), (4, 5, 6, 3)) * 2.0
    x417 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x417 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x194, (4, 5, 0, 3), (4, 5, 1, 2)) * 6.0
    x418 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x418 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x419 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x419 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x420 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x420 += einsum(t1.aa, (0, 1), x336, (0, 1, 2, 3), (2, 3))
    x421 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x421 += einsum(x347, (0, 1), (1, 0)) * -1.0
    x421 += einsum(x418, (0, 1), (1, 0))
    x421 += einsum(x419, (0, 1), (1, 0)) * 2.0
    x421 += einsum(x420, (0, 1), (1, 0)) * -1.0
    x422 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x422 += einsum(x421, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 2, 0)) * -2.0
    x423 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x423 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x332, (0, 4, 5, 2), (4, 5, 3, 1)) * 2.0
    x424 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x424 += einsum(x358, (0, 1), x297, (2, 3, 0, 4), (2, 3, 4, 1)) * 2.0
    x425 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x425 += einsum(f.aa.ov, (0, 1), x288, (2, 3, 0, 4), (2, 3, 4, 1)) * 6.0
    x426 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x426 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x426 += einsum(x385, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x426 += einsum(x386, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x426 += einsum(x395, (0, 1, 2, 3), (1, 0, 3, 2))
    x426 += einsum(x404, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x426 += einsum(x407, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x426 += einsum(x410, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x426 += einsum(x414, (0, 1, 2, 3), (0, 1, 3, 2))
    x426 += einsum(x416, (0, 1, 2, 3), (0, 1, 3, 2))
    x426 += einsum(x417, (0, 1, 2, 3), (0, 1, 3, 2))
    x426 += einsum(x422, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x426 += einsum(x423, (0, 1, 2, 3), (0, 1, 2, 3))
    x426 += einsum(x424, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x426 += einsum(x425, (0, 1, 2, 3), (1, 0, 2, 3))
    l2new_aaaa += einsum(x426, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_aaaa += einsum(x426, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x427 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x427 += einsum(f.aa.ov, (0, 1), t1.aa, (2, 1), (0, 2))
    x428 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x428 += einsum(x427, (0, 1), l2.aaaa, (2, 3, 4, 1), (0, 4, 2, 3))
    x429 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x429 += einsum(l2.aaaa, (0, 1, 2, 3), x249, (2, 4, 3, 5), (4, 5, 0, 1))
    x430 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x430 += einsum(f.aa.ov, (0, 1), t2.abab, (2, 3, 1, 4), (3, 4, 0, 2))
    x431 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x431 += einsum(x430, (0, 1, 2, 3), l3.abaaba, (4, 1, 5, 6, 0, 3), (2, 6, 4, 5))
    x432 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x432 += einsum(f.aa.ov, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4))
    x433 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x433 += einsum(x432, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 3, 6, 2, 1), (0, 6, 4, 5))
    x434 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x434 += einsum(x358, (0, 1), t2.abab, (2, 3, 1, 4), (3, 4, 2, 0))
    x435 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x435 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x435 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3))
    x435 += einsum(x311, (0, 1, 2, 3), (0, 1, 2, 3))
    x435 += einsum(x312, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.999999999999921
    x435 += einsum(x313, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.99999999999992
    x435 += einsum(x315, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x435 += einsum(x316, (0, 1, 2, 3), (0, 1, 3, 2))
    x435 += einsum(x317, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x435 += einsum(x434, (0, 1, 2, 3), (0, 1, 2, 3))
    x435 += einsum(x320, (0, 1, 2, 3), (0, 1, 3, 2))
    x435 += einsum(x321, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x436 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x436 += einsum(x435, (0, 1, 2, 3), l3.abaaba, (4, 1, 5, 6, 0, 2), (6, 3, 4, 5)) * -2.0
    x437 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x437 += einsum(t2.abab, (0, 1, 2, 3), x5, (1, 3, 4, 5), (0, 4, 5, 2))
    x438 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x438 += einsum(x358, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x439 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x439 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x439 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x439 += einsum(x327, (0, 1, 2, 3), (1, 0, 2, 3))
    x440 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x440 += einsum(t1.aa, (0, 1), x439, (2, 3, 1, 4), (0, 2, 3, 4))
    x441 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x441 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x441 += einsum(x323, (0, 1, 2, 3), (1, 0, 2, 3))
    x441 += einsum(x324, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.9999999999999606
    x441 += einsum(x325, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.999999999999881
    x441 += einsum(x326, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x441 += einsum(x437, (0, 1, 2, 3), (0, 2, 1, 3))
    x441 += einsum(x438, (0, 1, 2, 3), (1, 0, 2, 3))
    x441 += einsum(x440, (0, 1, 2, 3), (2, 0, 1, 3))
    x441 += einsum(x329, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x442 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x442 += einsum(x441, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 3, 6, 0, 1), (6, 2, 4, 5)) * -6.0
    x443 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x443 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x443 += einsum(x226, (0, 1, 2, 3), (0, 2, 1, 3))
    x444 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x444 += einsum(x272, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x444 += einsum(x273, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    l2new_abab += einsum(v.aabb.vvov, (0, 1, 2, 3), x444, (4, 5, 0, 1), (5, 3, 4, 2)) * 2.0
    x445 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x445 += einsum(x443, (0, 1, 2, 3), x444, (0, 4, 5, 3), (1, 2, 4, 5)) * 2.0
    x446 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x446 += einsum(t1.aa, (0, 1), x358, (2, 1), (0, 2))
    x447 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x447 += einsum(x349, (0, 1), (1, 0))
    x447 += einsum(x350, (0, 1), (0, 1))
    x447 += einsum(x351, (0, 1), (0, 1)) * 2.0
    x447 += einsum(x353, (0, 1), (1, 0)) * -1.0
    x447 += einsum(x446, (0, 1), (0, 1))
    x448 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x448 += einsum(x447, (0, 1), l2.aaaa, (2, 3, 4, 0), (4, 1, 2, 3)) * -2.0
    x449 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x449 += einsum(x428, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x449 += einsum(x429, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x449 += einsum(x431, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x449 += einsum(x433, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.0
    x449 += einsum(x436, (0, 1, 2, 3), (0, 1, 3, 2))
    x449 += einsum(x442, (0, 1, 2, 3), (0, 1, 2, 3))
    x449 += einsum(x445, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x449 += einsum(x448, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new_aaaa += einsum(x449, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_aaaa += einsum(x449, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x450 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x450 += einsum(f.aa.oo, (0, 1), l2.aaaa, (2, 3, 4, 1), (0, 4, 2, 3))
    l2new_aaaa += einsum(x450, (0, 1, 2, 3), (3, 2, 0, 1)) * -2.0
    l2new_aaaa += einsum(x450, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x451 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x451 += einsum(x305, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.00000000000004
    x451 += einsum(t1.aa, (0, 1), x191, (2, 3, 4, 1), (2, 3, 4, 0)) * 1.00000000000004
    x451 += einsum(x306, (0, 1, 2, 3), (0, 1, 3, 2))
    x451 += einsum(x307, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.9999999999999982
    l2new_aaaa += einsum(v.aaaa.ovov, (0, 1, 2, 3), x451, (4, 5, 2, 0), (1, 3, 5, 4)) * -1.9999999999999203
    x452 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x452 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x452 += einsum(x247, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    x452 += einsum(x248, (0, 1, 2, 3), (0, 3, 1, 2))
    l2new_aaaa += einsum(l2.aaaa, (0, 1, 2, 3), x452, (3, 4, 2, 5), (0, 1, 4, 5)) * 2.0
    x453 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x453 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1))
    x453 += einsum(x387, (0, 1, 2, 3), (0, 1, 3, 2))
    x453 += einsum(x388, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x453 += einsum(x389, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x453 += einsum(x390, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.999999999999921
    x453 += einsum(x391, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.99999999999992
    x453 += einsum(t2.abab, (0, 1, 2, 3), x278, (0, 2, 4, 5), (1, 3, 5, 4)) * -1.0
    x453 += einsum(x393, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(x453, (0, 1, 2, 3), l3.babbab, (4, 2, 1, 5, 6, 0), (3, 4, 6, 5)) * 2.0
    x454 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x454 += einsum(t1.aa, (0, 1), v.aabb.vvvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x455 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x455 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 2, 1, 5), (3, 5, 0, 4))
    x456 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x456 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovvv, (1, 3, 4, 5), (4, 5, 0, 2))
    x457 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x457 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (0, 4, 2, 5, 6, 3), (5, 1, 4, 6))
    x458 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x458 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 0, 5, 6, 1), (6, 3, 4, 5))
    x459 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x459 += einsum(t2.abab, (0, 1, 2, 3), x5, (1, 4, 0, 5), (3, 4, 5, 2))
    x460 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x460 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x460 += einsum(x454, (0, 1, 2, 3), (1, 0, 2, 3))
    x460 += einsum(x455, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x460 += einsum(x456, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x460 += einsum(x457, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.99999999999992
    x460 += einsum(x458, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.999999999999921
    x460 += einsum(t2.abab, (0, 1, 2, 3), x9, (1, 3, 4, 5), (5, 4, 0, 2)) * -1.0
    x460 += einsum(x459, (0, 1, 2, 3), (0, 1, 2, 3))
    l2new_abab += einsum(x460, (0, 1, 2, 3), l3.abaaba, (4, 0, 3, 5, 6, 2), (4, 1, 5, 6)) * 2.0
    x461 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x461 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x461 += einsum(x396, (0, 1, 2, 3), (0, 2, 3, 1)) * 0.5
    x461 += einsum(x397, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x461 += einsum(x398, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.49999999999998
    x461 += einsum(x399, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.4999999999999405
    x461 += einsum(t2.aaaa, (0, 1, 2, 3), x231, (1, 3, 4, 5), (0, 2, 5, 4)) * -1.0
    x461 += einsum(t2.aaaa, (0, 1, 2, 3), x401, (1, 4, 0, 5), (4, 2, 3, 5)) * 0.5
    l2new_abab += einsum(x461, (0, 1, 2, 3), l3.abaaba, (1, 4, 2, 5, 6, 0), (3, 4, 5, 6)) * 4.0
    x462 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x462 += einsum(t1.bb, (0, 1), v.bbbb.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x463 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x463 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovvv, (0, 2, 4, 5), (1, 3, 4, 5))
    x464 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x464 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 0, 2, 5, 6, 3), (4, 5, 6, 1))
    x465 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x465 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 2, 5, 1, 6), (4, 5, 6, 3))
    x466 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x466 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x466 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x467 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x467 += einsum(t2.bbbb, (0, 1, 2, 3), x466, (1, 3, 4, 5), (0, 2, 4, 5)) * 2.0
    x468 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x468 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x468 += einsum(x0, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x469 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x469 += einsum(t2.bbbb, (0, 1, 2, 3), x468, (0, 4, 1, 5), (4, 2, 3, 5))
    x470 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x470 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x470 += einsum(x462, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x470 += einsum(x463, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x470 += einsum(x464, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.999999999999881
    x470 += einsum(x465, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.99999999999996
    x470 += einsum(x467, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x470 += einsum(x469, (0, 1, 2, 3), (0, 2, 1, 3))
    l2new_abab += einsum(x470, (0, 1, 2, 3), l3.babbab, (1, 4, 2, 5, 6, 0), (4, 3, 6, 5)) * 2.0
    x471 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x471 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.5
    x471 += einsum(x116, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.5
    x471 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x471 += einsum(x118, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.99999999999996
    x471 += einsum(x119, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.9999999999999605
    x471 += einsum(t2.abab, (0, 1, 2, 3), x120, (4, 5, 1, 3), (5, 4, 0, 2)) * -0.5
    x471 += einsum(t2.aaaa, (0, 1, 2, 3), x36, (4, 5, 1, 3), (5, 4, 0, 2))
    x471 += einsum(t2.abab, (0, 1, 2, 3), x5, (4, 3, 0, 5), (1, 4, 5, 2)) * -0.5
    x471 += einsum(x18, (0, 1), t2.abab, (2, 3, 4, 1), (3, 0, 2, 4)) * 0.5
    x471 += einsum(t1.bb, (0, 1), x124, (2, 1, 3, 4), (0, 2, 3, 4)) * 0.5
    x471 += einsum(t1.aa, (0, 1), x126, (2, 3, 0, 4), (3, 2, 4, 1)) * -0.5
    l2new_abab += einsum(x471, (0, 1, 2, 3), l3.abaaba, (4, 5, 3, 6, 0, 2), (4, 5, 6, 1)) * -4.0
    x472 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x472 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x472 += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3))
    x472 += einsum(x311, (0, 1, 2, 3), (0, 1, 2, 3))
    x472 += einsum(x312, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.999999999999921
    x472 += einsum(x313, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.99999999999992
    x472 += einsum(x315, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x472 += einsum(x316, (0, 1, 2, 3), (0, 1, 3, 2))
    x472 += einsum(x317, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x472 += einsum(x318, (0, 1, 2, 3), (0, 1, 2, 3))
    x472 += einsum(x320, (0, 1, 2, 3), (0, 1, 3, 2))
    x472 += einsum(x321, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new_abab += einsum(x472, (0, 1, 2, 3), l3.babbab, (4, 5, 1, 6, 2, 0), (5, 4, 3, 6)) * -2.0
    x473 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x473 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x473 += einsum(x323, (0, 1, 2, 3), (2, 1, 0, 3)) * 0.5
    x473 += einsum(x324, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.49999999999998
    x473 += einsum(x325, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.4999999999999405
    x473 += einsum(t2.aaaa, (0, 1, 2, 3), x227, (4, 1, 5, 3), (5, 0, 4, 2)) * -1.0
    x473 += einsum(t2.abab, (0, 1, 2, 3), x28, (1, 3, 4, 5), (5, 0, 4, 2)) * 0.5
    x473 += einsum(x241, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4)) * 0.5
    x473 += einsum(t1.aa, (0, 1), x328, (2, 3, 1, 4), (3, 2, 0, 4)) * 0.5
    x473 += einsum(t1.aa, (0, 1), x250, (0, 2, 3, 4), (3, 2, 4, 1)) * -0.5
    l2new_abab += einsum(x473, (0, 1, 2, 3), l3.abaaba, (4, 5, 3, 2, 6, 1), (4, 5, 0, 6)) * -4.0
    x474 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x474 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x474 += einsum(x135, (0, 1, 2, 3), (2, 1, 0, 3))
    x474 += einsum(x136, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.999999999999881
    x474 += einsum(x137, (0, 1, 2, 3), (2, 1, 0, 3)) * -0.99999999999996
    x474 += einsum(x139, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x474 += einsum(x140, (0, 1, 2, 3), (2, 0, 1, 3))
    x474 += einsum(x141, (0, 1, 2, 3), (2, 1, 0, 3))
    x474 += einsum(x144, (0, 1, 2, 3), (2, 1, 0, 3))
    x474 += einsum(x145, (0, 1, 2, 3), (1, 2, 0, 3))
    l2new_abab += einsum(x474, (0, 1, 2, 3), l3.babbab, (4, 5, 3, 1, 6, 2), (5, 4, 6, 0)) * 2.0
    x475 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x475 += einsum(t1.aa, (0, 1), x5, (2, 3, 0, 4), (2, 3, 4, 1))
    x476 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x476 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x476 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x476 += einsum(x13, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x476 += einsum(x14, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x476 += einsum(x475, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new_abab += einsum(x476, (0, 1, 2, 3), x91, (4, 0, 2, 5, 6, 3), (6, 1, 5, 4)) * 2.0
    x477 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x477 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.5
    x477 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x477 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 0, 4), (2, 3, 1, 4)) * 0.5
    x477 += einsum(x228, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x477 += einsum(t2.aaaa, (0, 1, 2, 3), x229, (1, 4, 5, 3), (0, 4, 2, 5)) * -1.0
    l2new_abab += einsum(x477, (0, 1, 2, 3), x58, (4, 5, 0, 6, 1, 2), (3, 5, 6, 4)) * -4.0
    x478 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x478 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x479 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x479 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x479 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x479 += einsum(x478, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x479 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x479 += einsum(t2.bbbb, (0, 1, 2, 3), x129, (1, 4, 5, 3), (0, 4, 2, 5)) * -1.0
    l2new_abab += einsum(x479, (0, 1, 2, 3), x80, (0, 4, 1, 2, 5, 6), (6, 3, 5, 4)) * 4.0
    x480 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x480 += einsum(t1.aa, (0, 1), x226, (2, 0, 3, 4), (2, 3, 1, 4))
    x480 += einsum(x232, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new_abab += einsum(x480, (0, 1, 2, 3), x58, (4, 5, 0, 6, 1, 2), (3, 5, 6, 4)) * -2.0
    x481 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x481 += einsum(t1.bb, (0, 1), x0, (2, 0, 3, 4), (2, 3, 1, 4))
    x482 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x482 += einsum(x481, (0, 1, 2, 3), (0, 1, 2, 3))
    x482 += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new_abab += einsum(x482, (0, 1, 2, 3), x80, (0, 4, 1, 2, 5, 6), (6, 3, 5, 4)) * -2.0
    x483 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x483 += einsum(x264, (0, 1, 2, 3), (0, 1, 2, 3))
    x483 += einsum(x265, (0, 1, 2, 3), (0, 1, 2, 3))
    x483 += einsum(x266, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.4999999999999405
    x483 += einsum(x267, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x483 += einsum(x268, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.999999999999921
    x483 += einsum(x269, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x483 += einsum(x270, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.4999999999999405
    x483 += einsum(t1.bb, (0, 1), x106, (0, 2, 3, 4), (2, 1, 3, 4)) * -1.0
    l2new_abab += einsum(x483, (0, 1, 2, 3), x7, (0, 4, 5, 1), (3, 5, 2, 4)) * -2.0
    x484 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x484 += einsum(x61, (0, 1, 2, 3), (0, 1, 2, 3))
    x484 += einsum(x62, (0, 1, 2, 3), (0, 1, 2, 3))
    x485 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x485 += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5000000000000198
    x485 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5000000000000198
    x485 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.7499999999999999
    x485 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3))
    x485 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5000000000000198
    x485 += einsum(x57, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.7499999999999999
    x485 += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5000000000000198
    x485 += einsum(t1.aa, (0, 1), x484, (2, 3, 0, 4), (2, 3, 4, 1)) * -0.5000000000000198
    l2new_abab += einsum(x229, (0, 1, 2, 3), x485, (4, 5, 0, 2), (3, 5, 1, 4)) * 3.999999999999842
    x486 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x486 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x486 += einsum(x243, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l2new_abab += einsum(x486, (0, 1, 2, 3), x58, (4, 0, 2, 5, 3, 6), (6, 1, 5, 4)) * 2.0
    x487 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x487 += einsum(l2.bbbb, (0, 1, 2, 3), (2, 3, 0, 1))
    x487 += einsum(x72, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x487 += einsum(x73, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.5
    x487 += einsum(x74, (0, 1, 2, 3), (1, 0, 3, 2)) * 4.4999999999998215
    x487 += einsum(x79, (0, 1, 2, 3), (1, 0, 3, 2)) * -3.0
    x487 += einsum(x75, (0, 1, 2, 3), (1, 0, 3, 2)) * 1.999999999999921
    x487 += einsum(x81, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x487 += einsum(x76, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.49999999999998
    x487 += einsum(t1.bb, (0, 1), x132, (0, 2, 3, 4), (3, 2, 1, 4)) * 3.0
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), x487, (2, 4, 3, 5), (1, 5, 0, 4)) * 2.0
    x488 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x488 += einsum(l2.aaaa, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.22222222222223104
    x488 += einsum(x279, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.11111111111111552
    x488 += einsum(x280, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.4444444444444621
    x488 += einsum(x281, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.11111111111111108
    x488 += einsum(x282, (0, 1, 2, 3), (1, 0, 3, 2)) * 0.44444444444444453
    x488 += einsum(x286, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.22222222222223104
    x488 += einsum(x283, (0, 1, 2, 3), (1, 0, 3, 2))
    x488 += einsum(x287, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.6666666666666932
    x488 += einsum(t1.aa, (0, 1), x364, (0, 2, 3, 4), (3, 2, 1, 4)) * 0.22222222222223104
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), x488, (0, 4, 1, 5), (5, 3, 4, 2)) * 8.999999999999643
    x489 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x489 += einsum(x290, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000002
    x489 += einsum(x291, (0, 1, 2, 3), (0, 1, 2, 3))
    x489 += einsum(x292, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000004
    x489 += einsum(x293, (0, 1, 2, 3), (0, 1, 2, 3))
    x489 += einsum(x294, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000004
    x489 += einsum(t1.bb, (0, 1), x484, (0, 2, 3, 4), (2, 1, 3, 4)) * 1.00000000000004
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), x489, (4, 3, 5, 0), (1, 4, 5, 2)) * 1.99999999999992
    x490 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x490 += einsum(x87, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.50000000000002
    x490 += einsum(x88, (0, 1, 2, 3), (0, 1, 2, 3))
    x490 += einsum(x89, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000004
    x490 += einsum(x90, (0, 1, 2, 3), (0, 1, 2, 3))
    x490 += einsum(x92, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000004
    x490 += einsum(t1.aa, (0, 1), x106, (2, 3, 0, 4), (2, 3, 4, 1)) * 1.00000000000004
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), x490, (4, 2, 5, 1), (5, 3, 0, 4)) * 1.99999999999992
    x491 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x491 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x491 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x491 += einsum(t1.bb, (0, 1), x9, (2, 1, 3, 4), (0, 2, 4, 3)) * -1.0
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x491, (3, 4, 1, 5), (0, 5, 2, 4)) * -1.0
    x492 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x492 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x492 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x492 += einsum(x412, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x492, (2, 4, 0, 5), (5, 1, 4, 3)) * -1.0
    x493 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x493 += einsum(x102, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5000000000000202
    x493 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3))
    x493 += einsum(x104, (0, 1, 2, 3), (0, 1, 2, 3))
    x493 += einsum(x204, (0, 1, 2, 3), (1, 0, 2, 3))
    x493 += einsum(x205, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), x493, (4, 2, 5, 0), (1, 3, 5, 4)) * 1.9999999999999194
    x494 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x494 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x494 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x131, (0, 1, 2, 3), x494, (0, 1, 4, 5), (3, 5, 2, 4)) * -2.0
    l3new_abaaba += einsum(x494, (0, 1, 2, 3), x91, (0, 1, 4, 5, 6, 7), (6, 3, 7, 5, 2, 4)) * 2.0
    x495 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x495 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x495 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x495, (0, 1, 2, 3), x63, (4, 5, 0, 1), (3, 5, 2, 4)) * -2.0
    l3new_babbab += einsum(x495, (0, 1, 2, 3), x55, (4, 5, 6, 7, 0, 1), (6, 3, 7, 5, 2, 4)) * 2.0
    x496 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x496 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x496 += einsum(x242, (0, 1, 2, 3), (1, 0, 2, 3))
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x496, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x497 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x497 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x497 += einsum(x19, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x497, (3, 4, 0, 5), (5, 1, 2, 4)) * -1.0
    x498 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x498 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x498 += einsum(x26, (0, 1, 2, 3), (1, 0, 2, 3))
    x498 += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3))
    x498 += einsum(x245, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new_abab += einsum(l2.abab, (0, 1, 2, 3), x498, (3, 4, 2, 5), (0, 1, 5, 4))
    x499 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x499 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 4, 1, 3), (2, 4))
    x500 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x500 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x501 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x501 += einsum(f.bb.vv, (0, 1), (0, 1)) * -1.0
    x501 += einsum(x215, (0, 1), (1, 0)) * -1.0
    x501 += einsum(x499, (0, 1), (0, 1)) * 2.0
    x501 += einsum(x500, (0, 1), (0, 1))
    x501 += einsum(t1.bb, (0, 1), x466, (0, 1, 2, 3), (3, 2)) * -1.0
    l2new_abab += einsum(x501, (0, 1), l2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -1.0
    x502 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x502 += einsum(t1.aa, (0, 1), x278, (0, 2, 1, 3), (2, 3))
    x503 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x503 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x503 += einsum(x347, (0, 1), (1, 0)) * -1.0
    x503 += einsum(x418, (0, 1), (0, 1))
    x503 += einsum(x419, (0, 1), (0, 1)) * 2.0
    x503 += einsum(x502, (0, 1), (1, 0)) * -1.0
    l2new_abab += einsum(x503, (0, 1), l2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    l3new_babbab += einsum(x503, (0, 1), l3.babbab, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -2.0
    x504 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x504 += einsum(x158, (0, 1), (0, 1))
    x504 += einsum(x159, (0, 1), (0, 1)) * 0.5
    x504 += einsum(x208, (0, 1), (0, 1)) * 1.4999999999999394
    x504 += einsum(x160, (0, 1), (0, 1)) * 0.9999999999999597
    x504 += einsum(x161, (0, 1), (0, 1)) * 0.49999999999998007
    l2new_abab += einsum(x504, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (3, 0, 2, 4)) * -2.0
    x505 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x505 += einsum(x176, (0, 1), (0, 1)) * 0.5
    x505 += einsum(x177, (0, 1), (0, 1))
    x505 += einsum(x178, (0, 1), (0, 1)) * 0.49999999999998007
    x505 += einsum(x179, (0, 1), (0, 1)) * 0.9999999999999597
    x505 += einsum(x180, (0, 1), (0, 1)) * 1.4999999999999394
    l2new_abab += einsum(x505, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (0, 4, 2, 3)) * -2.0
    x506 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x506 += einsum(x0, (0, 1, 2, 3), (0, 1, 2, 3))
    x506 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    l2new_abab += einsum(x506, (0, 1, 2, 3), x93, (0, 2, 4, 5), (5, 3, 4, 1)) * -1.0
    l3new_abaaba += einsum(x506, (0, 1, 2, 3), x91, (0, 2, 4, 5, 6, 7), (6, 3, 7, 5, 1, 4)) * 2.0
    x507 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x507 += einsum(f.bb.oo, (0, 1), (0, 1)) * 0.5
    x507 += einsum(x217, (0, 1), (1, 0)) * 0.5
    x507 += einsum(x218, (0, 1), (0, 1))
    x507 += einsum(x219, (0, 1), (0, 1)) * 0.5
    x507 += einsum(t1.bb, (0, 1), x220, (2, 3, 0, 1), (3, 2)) * -0.5
    x507 += einsum(t1.bb, (0, 1), x18, (2, 1), (0, 2)) * 0.5
    l2new_abab += einsum(x507, (0, 1), l2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x508 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x508 += einsum(x172, (0, 1), (0, 1)) * 0.5
    x508 += einsum(x109, (0, 1), (0, 1))
    x508 += einsum(x110, (0, 1), (0, 1)) * 0.5
    x508 += einsum(x111, (0, 1), (0, 1)) * 1.4999999999999394
    x508 += einsum(x112, (0, 1), (0, 1)) * 0.9999999999999597
    x508 += einsum(x113, (0, 1), (0, 1)) * 0.49999999999998007
    l2new_abab += einsum(x508, (0, 1), v.aabb.ovov, (2, 3, 1, 4), (3, 4, 2, 0)) * -2.0
    x509 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x509 += einsum(l1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 0), (1, 2, 3, 4))
    x510 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x510 += einsum(l2.abab, (0, 1, 2, 3), x12, (4, 5, 2, 0), (3, 4, 1, 5))
    x511 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x511 += einsum(x4, (0, 1, 2, 3), x60, (4, 5, 2, 3), (4, 0, 5, 1))
    x512 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x512 += einsum(x65, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    x512 += einsum(x66, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x513 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x513 += einsum(x512, (0, 1, 2, 3), x71, (4, 5, 1, 3), (4, 0, 5, 2)) * 2.0
    x514 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x514 += einsum(t1.bb, (0, 1), x132, (2, 0, 3, 4), (2, 3, 1, 4)) * 3.0
    x515 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x515 += einsum(x72, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x515 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x515 += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.4999999999998215
    x515 += einsum(x79, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x515 += einsum(x75, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.999999999999921
    x515 += einsum(x81, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x515 += einsum(x76, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.49999999999998
    x515 += einsum(x514, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x516 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x516 += einsum(x515, (0, 1, 2, 3), x7, (1, 4, 5, 3), (4, 0, 5, 2)) * 2.0
    x517 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x517 += einsum(t1.aa, (0, 1), x484, (2, 3, 0, 4), (2, 3, 4, 1)) * 2.0
    x518 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x518 += einsum(l2.abab, (0, 1, 2, 3), (3, 1, 2, 0))
    x518 += einsum(x51, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x518 += einsum(x52, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x518 += einsum(x53, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.999999999999881
    x518 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.999999999999842
    x518 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x518 += einsum(x57, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.999999999999881
    x518 += einsum(x59, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x518 += einsum(x517, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x519 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x519 += einsum(v.aabb.ovov, (0, 1, 2, 3), x518, (4, 5, 0, 1), (2, 4, 3, 5))
    x520 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x520 += einsum(v.aabb.vvov, (0, 1, 2, 3), x100, (4, 5, 0, 1), (2, 4, 3, 5)) * 2.0
    x521 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x521 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x521 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x521 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x522 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x522 += einsum(l2.bbbb, (0, 1, 2, 3), x521, (3, 4, 5, 1), (2, 4, 0, 5)) * 2.0
    x523 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x523 += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x523 += einsum(x83, (0, 1, 2, 3), (0, 1, 2, 3))
    x523 += einsum(x84, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x524 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x524 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x524 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x525 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x525 += einsum(x523, (0, 1, 2, 3), x524, (1, 4, 2, 5), (0, 4, 3, 5)) * 6.0
    x526 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x526 += einsum(x504, (0, 1), v.bbbb.ovov, (2, 1, 3, 4), (2, 3, 4, 0)) * 2.0
    x527 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x527 += einsum(v.aabb.ooov, (0, 1, 2, 3), x101, (4, 5, 0, 1), (2, 4, 3, 5))
    x528 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x528 += einsum(x506, (0, 1, 2, 3), x82, (0, 4, 2, 5), (4, 1, 5, 3)) * 2.0
    x529 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x529 += einsum(x173, (0, 1), v.bbbb.ovov, (2, 3, 1, 4), (2, 0, 4, 3))
    x530 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x530 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x530 += einsum(x0, (0, 1, 2, 3), (0, 1, 2, 3))
    x531 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x531 += einsum(l1.bb, (0, 1), x530, (1, 2, 3, 4), (2, 3, 0, 4))
    x532 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x532 += einsum(f.bb.ov, (0, 1), l1.bb, (2, 3), (0, 3, 1, 2))
    x532 += einsum(x509, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x532 += einsum(x510, (0, 1, 2, 3), (0, 1, 2, 3))
    x532 += einsum(x511, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x532 += einsum(x513, (0, 1, 2, 3), (1, 0, 3, 2))
    x532 += einsum(x516, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x532 += einsum(x519, (0, 1, 2, 3), (1, 0, 3, 2))
    x532 += einsum(x520, (0, 1, 2, 3), (1, 0, 3, 2))
    x532 += einsum(x522, (0, 1, 2, 3), (0, 1, 2, 3))
    x532 += einsum(x525, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x532 += einsum(x526, (0, 1, 2, 3), (1, 0, 3, 2))
    x532 += einsum(x527, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x532 += einsum(x528, (0, 1, 2, 3), (0, 1, 2, 3))
    x532 += einsum(x529, (0, 1, 2, 3), (1, 0, 3, 2))
    x532 += einsum(x531, (0, 1, 2, 3), (0, 1, 2, 3))
    x532 += einsum(l1.bb, (0, 1), x225, (2, 3), (1, 2, 0, 3))
    l2new_bbbb += einsum(x532, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new_bbbb += einsum(x532, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new_bbbb += einsum(x532, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new_bbbb += einsum(x532, (0, 1, 2, 3), (3, 2, 1, 0))
    x533 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x533 += einsum(f.bb.ov, (0, 1), t1.bb, (2, 1), (0, 2))
    x534 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x534 += einsum(x533, (0, 1), l2.bbbb, (2, 3, 4, 1), (0, 4, 2, 3))
    x535 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x535 += einsum(l2.bbbb, (0, 1, 2, 3), x24, (2, 3, 4, 5), (4, 5, 0, 1))
    x536 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x536 += einsum(f.bb.ov, (0, 1), t2.bbbb, (2, 3, 4, 1), (0, 2, 3, 4))
    x537 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x537 += einsum(x536, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 3, 6, 1, 2), (0, 6, 4, 5)) * -1.0
    x538 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x538 += einsum(f.bb.ov, (0, 1), t2.abab, (2, 3, 4, 1), (0, 3, 2, 4))
    x539 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x539 += einsum(x538, (0, 1, 2, 3), l3.babbab, (4, 3, 5, 6, 2, 1), (0, 6, 4, 5))
    x540 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x540 += einsum(x225, (0, 1), t2.abab, (2, 3, 4, 1), (3, 0, 2, 4))
    x541 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x541 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x541 += einsum(x116, (0, 1, 2, 3), (1, 0, 2, 3))
    x541 += einsum(x117, (0, 1, 2, 3), (0, 1, 2, 3))
    x541 += einsum(x118, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.99999999999992
    x541 += einsum(x119, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.999999999999921
    x541 += einsum(x121, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x541 += einsum(x122, (0, 1, 2, 3), (1, 0, 2, 3))
    x541 += einsum(x123, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x541 += einsum(x540, (0, 1, 2, 3), (0, 1, 2, 3))
    x541 += einsum(x125, (0, 1, 2, 3), (0, 1, 2, 3))
    x541 += einsum(x127, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x542 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x542 += einsum(x541, (0, 1, 2, 3), l3.babbab, (4, 3, 5, 6, 2, 0), (6, 1, 4, 5)) * -2.0
    x543 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x543 += einsum(t2.bbbb, (0, 1, 2, 3), x1, (4, 1, 5, 3), (0, 4, 5, 2)) * 2.0
    x544 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x544 += einsum(t2.abab, (0, 1, 2, 3), x36, (4, 5, 0, 2), (1, 4, 5, 3))
    x545 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x545 += einsum(x225, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x546 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x546 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x546 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x546 += einsum(x142, (0, 1, 2, 3), (1, 0, 2, 3))
    x547 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x547 += einsum(t1.bb, (0, 1), x546, (2, 3, 1, 4), (0, 2, 3, 4))
    x548 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x548 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x548 += einsum(x22, (0, 1, 2, 3), (3, 1, 0, 2))
    x548 += einsum(x23, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x548 += einsum(x24, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x548 += einsum(x24, (0, 1, 2, 3), (3, 0, 2, 1))
    x549 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x549 += einsum(t1.bb, (0, 1), x548, (0, 2, 3, 4), (2, 3, 4, 1))
    x550 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x550 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x550 += einsum(x135, (0, 1, 2, 3), (1, 0, 2, 3))
    x550 += einsum(x136, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.999999999999881
    x550 += einsum(x137, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.9999999999999606
    x550 += einsum(x543, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x550 += einsum(x544, (0, 1, 2, 3), (0, 2, 1, 3))
    x550 += einsum(x545, (0, 1, 2, 3), (1, 0, 2, 3))
    x550 += einsum(x547, (0, 1, 2, 3), (2, 0, 1, 3))
    x550 += einsum(x549, (0, 1, 2, 3), (1, 0, 2, 3))
    x551 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x551 += einsum(x550, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 3, 6, 0, 1), (6, 2, 4, 5)) * -6.0
    x552 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x552 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x552 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3))
    x553 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x553 += einsum(x147, (0, 1, 2, 3), x552, (0, 4, 5, 3), (4, 5, 1, 2)) * 6.0
    x554 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x554 += einsum(t1.bb, (0, 1), x225, (2, 1), (0, 2))
    x555 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x555 += einsum(x217, (0, 1), (1, 0))
    x555 += einsum(x218, (0, 1), (0, 1)) * 2.0
    x555 += einsum(x219, (0, 1), (0, 1))
    x555 += einsum(x221, (0, 1), (1, 0)) * -1.0
    x555 += einsum(x554, (0, 1), (0, 1))
    x556 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x556 += einsum(x555, (0, 1), l2.bbbb, (2, 3, 4, 0), (4, 1, 2, 3)) * -2.0
    x557 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x557 += einsum(x534, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x557 += einsum(x535, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x557 += einsum(x537, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.0
    x557 += einsum(x539, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x557 += einsum(x542, (0, 1, 2, 3), (0, 1, 3, 2))
    x557 += einsum(x551, (0, 1, 2, 3), (0, 1, 2, 3))
    x557 += einsum(x553, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x557 += einsum(x556, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new_bbbb += einsum(x557, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_bbbb += einsum(x557, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x558 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x558 += einsum(f.bb.vv, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    x559 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x559 += einsum(x242, (0, 1, 2, 3), x55, (4, 5, 6, 1, 2, 3), (4, 5, 6, 0))
    x560 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x560 += einsum(t2.abab, (0, 1, 2, 3), x71, (1, 3, 4, 5), (4, 5, 0, 2))
    x561 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x561 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x561 += einsum(x454, (0, 1, 2, 3), (1, 0, 2, 3))
    x561 += einsum(x455, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x561 += einsum(x456, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x561 += einsum(x457, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.99999999999992
    x561 += einsum(x458, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.999999999999921
    x561 += einsum(x560, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x561 += einsum(x459, (0, 1, 2, 3), (1, 0, 2, 3))
    x562 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x562 += einsum(x561, (0, 1, 2, 3), l3.babbab, (4, 3, 1, 5, 2, 6), (5, 6, 4, 0)) * -2.0
    x563 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x563 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x563 += einsum(x462, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x563 += einsum(x463, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x563 += einsum(x464, (0, 1, 2, 3), (0, 2, 1, 3)) * -2.999999999999881
    x563 += einsum(x465, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.9999999999999606
    x563 += einsum(x467, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x563 += einsum(x469, (0, 1, 2, 3), (0, 2, 1, 3))
    x564 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x564 += einsum(x563, (0, 1, 2, 3), l3.bbbbbb, (4, 1, 2, 5, 6, 0), (5, 6, 4, 3)) * -6.0
    x565 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x565 += einsum(x476, (0, 1, 2, 3), x80, (4, 5, 0, 6, 2, 3), (4, 5, 6, 1)) * 2.0
    x566 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x566 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x566 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x566 += einsum(x478, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x566 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    x566 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x567 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x567 += einsum(x566, (0, 1, 2, 3), x78, (4, 5, 0, 1, 2, 6), (4, 5, 6, 3)) * 6.0
    x568 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x568 += einsum(x482, (0, 1, 2, 3), x78, (4, 5, 0, 1, 2, 6), (4, 5, 6, 3)) * 6.0
    x569 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x569 += einsum(x486, (0, 1, 2, 3), x55, (4, 5, 0, 6, 2, 3), (4, 5, 6, 1)) * 2.0
    x570 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x570 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x130, (4, 5, 0, 3), (4, 5, 1, 2)) * 2.0
    x571 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x571 += einsum(t1.bb, (0, 1), x163, (0, 1, 2, 3), (2, 3))
    x572 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x572 += einsum(x215, (0, 1), (1, 0)) * -1.0
    x572 += einsum(x499, (0, 1), (1, 0)) * 2.0
    x572 += einsum(x500, (0, 1), (1, 0))
    x572 += einsum(x571, (0, 1), (1, 0)) * -1.0
    x573 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x573 += einsum(x572, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 2, 0)) * -2.0
    x574 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x574 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x133, (0, 4, 5, 2), (4, 5, 3, 1)) * 6.0
    x575 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x575 += einsum(x225, (0, 1), x85, (2, 3, 0, 4), (2, 3, 4, 1)) * 2.0
    x576 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x576 += einsum(f.bb.ov, (0, 1), x85, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x577 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x577 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x577 += einsum(x558, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x577 += einsum(x559, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x577 += einsum(x562, (0, 1, 2, 3), (1, 0, 3, 2))
    x577 += einsum(x564, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x577 += einsum(x565, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x577 += einsum(x567, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x577 += einsum(x568, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x577 += einsum(x569, (0, 1, 2, 3), (0, 1, 3, 2))
    x577 += einsum(x570, (0, 1, 2, 3), (0, 1, 3, 2))
    x577 += einsum(x573, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x577 += einsum(x574, (0, 1, 2, 3), (0, 1, 2, 3))
    x577 += einsum(x575, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x577 += einsum(x576, (0, 1, 2, 3), (1, 0, 3, 2))
    l2new_bbbb += einsum(x577, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new_bbbb += einsum(x577, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x578 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x578 += einsum(f.bb.oo, (0, 1), l2.bbbb, (2, 3, 4, 1), (0, 4, 2, 3))
    l2new_bbbb += einsum(x578, (0, 1, 2, 3), (3, 2, 0, 1)) * -2.0
    l2new_bbbb += einsum(x578, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x579 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x579 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x579 += einsum(x22, (0, 1, 2, 3), (1, 3, 2, 0))
    x579 += einsum(x23, (0, 1, 2, 3), (0, 2, 3, 1))
    l2new_bbbb += einsum(l2.bbbb, (0, 1, 2, 3), x579, (2, 4, 5, 3), (0, 1, 5, 4)) * -2.0
    x580 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x580 += einsum(x148, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333468
    x580 += einsum(x153, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333468
    x580 += einsum(x149, (0, 1, 2, 3), (0, 1, 3, 2))
    l2new_bbbb += einsum(v.bbbb.ovov, (0, 1, 2, 3), x580, (4, 5, 0, 2), (3, 1, 5, 4)) * -5.9999999999997575
    x581 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x581 += einsum(l2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x582 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x582 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x194, (4, 5, 2, 6), (4, 5, 0, 6, 3, 1)) * 6.0
    x583 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x583 += einsum(x581, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x583 += einsum(x582, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0)) * -1.0
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0))
    l3new_aaaaaa += einsum(x583, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * -1.0
    x584 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x584 += einsum(l2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 3, 5, 6), (2, 4, 5, 0, 1, 6))
    x585 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x585 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x444, (4, 5, 6, 1), (4, 0, 2, 5, 6, 3)) * 2.0
    x586 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x586 += einsum(x584, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x586 += einsum(x585, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 2, 1)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 2, 1))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 0, 1)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0)) * -1.0
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0))
    l3new_aaaaaa += einsum(x586, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    x587 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x587 += einsum(x421, (0, 1), l3.aaaaaa, (2, 3, 1, 4, 5, 6), (4, 5, 6, 2, 3, 0)) * 6.0
    x588 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x588 += einsum(x358, (0, 1), x189, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1)) * 6.0
    x589 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x589 += einsum(x587, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x589 += einsum(x588, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    l3new_aaaaaa += einsum(x589, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new_aaaaaa += einsum(x589, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x589, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    x590 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x590 += einsum(x447, (0, 1), l3.aaaaaa, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4)) * 6.0
    l3new_aaaaaa += einsum(x590, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new_aaaaaa += einsum(x590, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x590, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    x591 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x591 += einsum(v.aabb.ovoo, (0, 1, 2, 3), x91, (2, 3, 4, 5, 6, 7), (4, 5, 0, 6, 7, 1))
    x592 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x592 += einsum(t2.aaaa, (0, 1, 2, 3), x229, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0000000000000204
    x593 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x593 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x593 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x593 += einsum(x228, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x593 += einsum(x592, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x593 += einsum(x232, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x594 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x594 += einsum(x593, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3)) * 6.0
    x595 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x595 += einsum(t2.abab, (0, 1, 2, 3), x236, (0, 4, 2, 5), (1, 3, 4, 5)) * 1.00000000000001
    x596 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x596 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x596 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    x596 += einsum(x595, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x597 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x597 += einsum(x596, (0, 1, 2, 3), l3.abaaba, (4, 1, 5, 6, 0, 7), (6, 7, 2, 4, 5, 3)) * 2.0
    x598 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x598 += einsum(x379, (0, 1, 2, 3), x189, (4, 5, 0, 2, 6, 7), (4, 5, 1, 6, 7, 3)) * 6.0
    x599 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x599 += einsum(x495, (0, 1, 2, 3), x189, (4, 5, 0, 1, 6, 7), (4, 5, 2, 6, 7, 3)) * 6.0
    x600 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x600 += einsum(x591, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 2.0
    x600 += einsum(x594, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x600 += einsum(x597, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x600 += einsum(x598, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x600 += einsum(x599, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2))
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0))
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0
    l3new_aaaaaa += einsum(x600, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0)) * -1.0
    x601 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x601 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 2, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x602 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x602 += einsum(x601, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x602 += einsum(x304, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x603 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x603 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x602, (4, 5, 6, 0, 2, 7), (4, 5, 6, 7, 1, 3)) * 6.0
    l3new_aaaaaa += einsum(x603, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x603, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new_aaaaaa += einsum(x603, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    x604 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x604 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x604 += einsum(x247, (0, 1, 2, 3), (1, 3, 2, 0))
    x604 += einsum(x248, (0, 1, 2, 3), (0, 2, 3, 1))
    x605 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x605 += einsum(x604, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 6, 7, 0, 3), (7, 1, 2, 4, 5, 6)) * -6.0
    x606 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x606 += einsum(f.aa.oo, (0, 1), (0, 1))
    x606 += einsum(x427, (0, 1), (1, 0))
    x607 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x607 += einsum(x606, (0, 1), l3.aaaaaa, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4)) * 6.0
    x608 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x608 += einsum(x605, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    x608 += einsum(x607, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    l3new_aaaaaa += einsum(x608, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    l3new_aaaaaa += einsum(x608, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x608, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    x609 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x609 += einsum(f.aa.vv, (0, 1), l3.aaaaaa, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x610 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x610 += einsum(f.aa.ov, (0, 1), x189, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x611 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x611 += einsum(v.aaaa.vvvv, (0, 1, 2, 3), l3.aaaaaa, (4, 1, 3, 5, 6, 7), (5, 6, 7, 4, 0, 2))
    x612 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x612 += einsum(x609, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    x612 += einsum(x610, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 6.0
    x612 += einsum(x611, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    l3new_aaaaaa += einsum(x612, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new_aaaaaa += einsum(x612, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new_aaaaaa += einsum(x612, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    x613 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x613 += einsum(l2.aaaa, (0, 1, 2, 3), x226, (3, 4, 5, 6), (2, 4, 5, 0, 1, 6))
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 0, 1)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 0, 1)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * 2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -2.0
    l3new_aaaaaa += einsum(x613, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * 2.0
    x614 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x614 += einsum(x249, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 6, 7, 0, 1), (7, 2, 3, 4, 5, 6))
    l3new_aaaaaa += einsum(x614, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -6.0
    l3new_aaaaaa += einsum(x614, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * 6.0
    l3new_aaaaaa += einsum(x614, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * 6.0
    l3new_aaaaaa += einsum(x614, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1)) * -6.0
    l3new_aaaaaa += einsum(x614, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -6.0
    l3new_aaaaaa += einsum(x614, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * 6.0
    x615 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x615 += einsum(x235, (0, 1, 2, 3), l3.abaaba, (4, 1, 5, 6, 0, 7), (6, 7, 2, 4, 5, 3))
    x616 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x616 += einsum(x2, (0, 1, 2, 3), x91, (0, 1, 4, 5, 6, 7), (4, 5, 2, 7, 6, 3)) * -1.0
    x617 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x617 += einsum(x615, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 4.00000000000004
    x617 += einsum(x616, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2))
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -1.0
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0
    l3new_aaaaaa += einsum(x617, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0))
    x618 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x618 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x189, (4, 5, 6, 0, 7, 3), (4, 5, 6, 7, 1, 2)) * -1.0
    l3new_aaaaaa += einsum(x618, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -6.0
    l3new_aaaaaa += einsum(x618, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * 6.0
    l3new_aaaaaa += einsum(x618, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * 6.0
    l3new_aaaaaa += einsum(x618, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -6.0
    l3new_aaaaaa += einsum(x618, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -6.0
    l3new_aaaaaa += einsum(x618, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * 6.0
    x619 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x619 += einsum(l2.abab, (0, 1, 2, 3), v.bbbb.ovvv, (4, 5, 6, 1), (3, 4, 5, 6, 2, 0))
    x620 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x620 += einsum(l2.abab, (0, 1, 2, 3), v.aabb.vvov, (4, 0, 5, 6), (3, 5, 1, 6, 2, 4))
    x621 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x621 += einsum(v.aabb.ooov, (0, 1, 2, 3), x58, (4, 5, 6, 0, 1, 7), (4, 2, 5, 3, 6, 7))
    x622 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x622 += einsum(x4, (0, 1, 2, 3), x58, (4, 5, 2, 6, 3, 7), (4, 0, 5, 1, 6, 7)) * -1.0
    x623 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x623 += einsum(t2.bbbb, (0, 1, 2, 3), x7, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.00000000000002
    x624 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x624 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x624 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x624 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x624 += einsum(x623, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x624 += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x625 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x625 += einsum(x624, (0, 1, 2, 3), l3.babbab, (4, 5, 2, 6, 7, 0), (6, 1, 4, 3, 7, 5)) * 2.0
    x626 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x626 += einsum(t2.abab, (0, 1, 2, 3), x7, (1, 4, 5, 3), (4, 5, 0, 2)) * 1.00000000000001
    x627 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x627 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x627 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x627 += einsum(x13, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.00000000000002
    x627 += einsum(x626, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x628 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x628 += einsum(x627, (0, 1, 2, 3), l3.abaaba, (4, 5, 3, 6, 7, 2), (7, 0, 5, 1, 6, 4)) * 2.0
    x629 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x629 += einsum(x506, (0, 1, 2, 3), x80, (4, 0, 2, 5, 6, 7), (4, 1, 5, 3, 6, 7)) * 2.0
    x630 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x630 += einsum(x524, (0, 1, 2, 3), x80, (4, 0, 2, 5, 6, 7), (4, 1, 5, 3, 6, 7)) * 2.0
    x631 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x631 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x296, (4, 1, 5, 6), (0, 2, 3, 4, 5, 6)) * 2.0
    x632 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x632 += einsum(v.aabb.ovov, (0, 1, 2, 3), x100, (4, 5, 6, 1), (2, 4, 3, 5, 0, 6)) * 2.0
    x633 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x633 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x96, (4, 2, 5, 6), (0, 4, 3, 1, 5, 6))
    x634 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x634 += einsum(v.aabb.ovov, (0, 1, 2, 3), x63, (4, 5, 6, 0), (2, 4, 3, 5, 6, 1)) * 2.0
    x635 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x635 += einsum(l2.abab, (0, 1, 2, 3), x530, (3, 4, 5, 6), (4, 5, 1, 6, 2, 0))
    x636 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x636 += einsum(l2.abab, (0, 1, 2, 3), x28, (4, 5, 2, 6), (3, 4, 1, 5, 6, 0))
    x637 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x637 += einsum(l1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 5), (1, 4, 0, 5, 2, 3))
    x637 += einsum(x619, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x637 += einsum(x620, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x637 += einsum(x621, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    x637 += einsum(x622, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    x637 += einsum(x625, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x637 += einsum(x628, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x637 += einsum(x629, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x637 += einsum(x630, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x637 += einsum(x631, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x637 += einsum(x632, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x637 += einsum(x633, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x637 += einsum(x634, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x637 += einsum(x635, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x637 += einsum(x636, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    l3new_babbab += einsum(x637, (0, 1, 2, 3, 4, 5), (2, 5, 3, 0, 4, 1))
    l3new_babbab += einsum(x637, (0, 1, 2, 3, 4, 5), (3, 5, 2, 0, 4, 1)) * -1.0
    l3new_babbab += einsum(x637, (0, 1, 2, 3, 4, 5), (2, 5, 3, 1, 4, 0)) * -1.0
    l3new_babbab += einsum(x637, (0, 1, 2, 3, 4, 5), (3, 5, 2, 1, 4, 0))
    x638 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x638 += einsum(l2.bbbb, (0, 1, 2, 3), v.aabb.ovoo, (4, 5, 6, 3), (2, 6, 0, 1, 4, 5))
    x639 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x639 += einsum(v.aabb.ovov, (0, 1, 2, 3), x66, (4, 5, 6, 3), (4, 2, 5, 6, 0, 1))
    x640 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x640 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x640 += einsum(x19, (0, 1, 2, 3), (0, 1, 3, 2))
    x640 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.00000000000001
    x641 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x641 += einsum(x640, (0, 1, 2, 3), l3.babbab, (4, 2, 5, 6, 7, 0), (6, 1, 4, 5, 7, 3)) * -2.0
    x642 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x642 += einsum(x498, (0, 1, 2, 3), l3.babbab, (4, 5, 6, 7, 2, 0), (7, 1, 4, 6, 3, 5)) * -2.0
    x643 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x643 += einsum(x3, (0, 1, 2, 3), x55, (4, 0, 5, 6, 7, 2), (4, 1, 5, 6, 7, 3)) * 2.0
    x644 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x644 += einsum(t1.bb, (0, 1), x16, (2, 1), (0, 2))
    x645 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x645 += einsum(x217, (0, 1), (1, 0))
    x645 += einsum(x219, (0, 1), (0, 1))
    x645 += einsum(x644, (0, 1), (0, 1))
    x645 += einsum(x221, (0, 1), (1, 0)) * -1.0
    x646 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x646 += einsum(x645, (0, 1), l3.babbab, (2, 3, 4, 5, 6, 0), (5, 1, 2, 4, 6, 3)) * -2.0
    x647 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x647 += einsum(f.bb.oo, (0, 1), (0, 1))
    x647 += einsum(x533, (0, 1), (1, 0))
    x648 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x648 += einsum(x647, (0, 1), l3.babbab, (2, 3, 4, 5, 6, 0), (5, 1, 2, 4, 6, 3)) * -2.0
    x649 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x649 += einsum(x638, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 2.0
    x649 += einsum(x639, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 2.0
    x649 += einsum(x641, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x649 += einsum(x642, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x649 += einsum(x643, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x649 += einsum(x646, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x649 += einsum(x648, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    l3new_babbab += einsum(x649, (0, 1, 2, 3, 4, 5), (3, 5, 2, 0, 4, 1)) * -1.0
    l3new_babbab += einsum(x649, (0, 1, 2, 3, 4, 5), (3, 5, 2, 1, 4, 0))
    x650 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x650 += einsum(l2.bbbb, (0, 1, 2, 3), v.aabb.ovvv, (4, 5, 6, 1), (2, 3, 0, 6, 4, 5))
    x651 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x651 += einsum(f.bb.vv, (0, 1), l3.babbab, (2, 3, 1, 4, 5, 6), (4, 6, 0, 2, 5, 3))
    x652 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x652 += einsum(f.bb.ov, (0, 1), x80, (2, 3, 0, 4, 5, 6), (2, 3, 1, 4, 5, 6))
    x653 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x653 += einsum(v.aabb.vvvv, (0, 1, 2, 3), l3.babbab, (4, 1, 3, 5, 6, 7), (5, 7, 4, 2, 6, 0))
    x654 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x654 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x80, (4, 5, 0, 3, 6, 7), (4, 5, 1, 2, 6, 7)) * -1.0
    x655 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x655 += einsum(v.aabb.vvov, (0, 1, 2, 3), x80, (4, 5, 2, 6, 7, 1), (4, 5, 6, 3, 7, 0))
    x656 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x656 += einsum(v.aabb.ovvv, (0, 1, 2, 3), x55, (4, 5, 6, 3, 7, 0), (4, 5, 6, 2, 7, 1))
    x657 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x657 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.99999999999999
    x657 += einsum(x242, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.99999999999999
    x657 += einsum(x243, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x658 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x658 += einsum(x657, (0, 1, 2, 3), l3.babbab, (4, 5, 0, 6, 2, 7), (6, 7, 4, 1, 3, 5)) * -2.00000000000002
    x659 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x659 += einsum(x572, (0, 1), l3.babbab, (2, 3, 1, 4, 5, 6), (4, 6, 2, 0, 5, 3)) * -2.0
    x660 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x660 += einsum(x28, (0, 1, 2, 3), x80, (4, 5, 0, 6, 2, 7), (4, 5, 6, 1, 3, 7)) * 2.0
    x661 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x661 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 6, 7), (5, 7, 1, 4, 6, 0))
    x662 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x662 += einsum(x661, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x662 += einsum(x98, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x663 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x663 += einsum(v.aabb.ovov, (0, 1, 2, 3), x662, (4, 5, 2, 6, 7, 0), (4, 5, 3, 6, 7, 1)) * 2.0
    x664 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x664 += einsum(x225, (0, 1), x80, (2, 3, 0, 4, 5, 6), (2, 3, 4, 1, 5, 6)) * 2.0
    x665 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x665 += einsum(v.aabb.ovov, (0, 1, 2, 3), x85, (4, 5, 2, 6), (4, 5, 3, 6, 0, 1)) * 2.0
    x666 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x666 += einsum(l1.aa, (0, 1), v.bbbb.ovov, (2, 3, 4, 5), (2, 4, 3, 5, 1, 0)) * -1.0
    x666 += einsum(x650, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 2.0
    x666 += einsum(x651, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -2.0
    x666 += einsum(x652, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 2.0
    x666 += einsum(x653, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 2.0
    x666 += einsum(x654, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -2.0
    x666 += einsum(x655, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -2.0
    x666 += einsum(x656, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -2.0
    x666 += einsum(x658, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x666 += einsum(x659, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x666 += einsum(x660, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x666 += einsum(x663, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x666 += einsum(x664, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x666 += einsum(x665, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5)) * -1.0
    l3new_babbab += einsum(x666, (0, 1, 2, 3, 4, 5), (3, 5, 2, 0, 4, 1))
    l3new_babbab += einsum(x666, (0, 1, 2, 3, 4, 5), (2, 5, 3, 0, 4, 1)) * -1.0
    x667 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x667 += einsum(l2.bbbb, (0, 1, 2, 3), x2, (3, 4, 5, 6), (2, 4, 0, 1, 5, 6))
    x668 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x668 += einsum(v.aabb.ovov, (0, 1, 2, 3), x65, (4, 5, 6, 3), (4, 2, 5, 6, 0, 1)) * -1.0
    x669 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x669 += einsum(t1.bb, (0, 1), x17, (2, 1), (0, 2)) * -1.0
    x670 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x670 += einsum(x218, (0, 1), (0, 1)) * 2.0
    x670 += einsum(x669, (0, 1), (0, 1))
    x671 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x671 += einsum(x670, (0, 1), l3.babbab, (2, 3, 4, 5, 6, 0), (5, 1, 2, 4, 6, 3)) * -2.0
    x672 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x672 += einsum(x667, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x672 += einsum(x668, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * 6.0
    x672 += einsum(x671, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    l3new_babbab += einsum(x672, (0, 1, 2, 3, 4, 5), (3, 5, 2, 0, 4, 1))
    l3new_babbab += einsum(x672, (0, 1, 2, 3, 4, 5), (3, 5, 2, 1, 4, 0)) * -1.0
    x673 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x673 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.99999999999999
    x673 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.99999999999999
    x673 += einsum(x228, (0, 1, 2, 3), (0, 1, 2, 3))
    x673 += einsum(x230, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x673 += einsum(t1.aa, (0, 1), x231, (2, 1, 3, 4), (0, 2, 4, 3)) * -0.99999999999999
    l3new_babbab += einsum(x673, (0, 1, 2, 3), l3.babbab, (4, 2, 5, 6, 0, 7), (4, 3, 5, 6, 1, 7)) * 2.00000000000002
    x674 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x674 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x674 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    x674 += einsum(x235, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0000000000000204
    x674 += einsum(x595, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l3new_babbab += einsum(x674, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 1, 6, 7, 0), (4, 3, 5, 6, 2, 7)) * 6.0
    x675 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x675 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x675 += einsum(x22, (0, 1, 2, 3), (1, 3, 0, 2))
    x675 += einsum(x23, (0, 1, 2, 3), (0, 2, 1, 3))
    x675 += einsum(x24, (0, 1, 2, 3), (2, 1, 0, 3))
    x675 += einsum(x24, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    l3new_babbab += einsum(x675, (0, 1, 2, 3), l3.babbab, (4, 5, 6, 2, 7, 0), (4, 5, 6, 1, 7, 3)) * -2.0
    x676 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x676 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (2, 4, 3, 5, 6, 7), (5, 7, 0, 1, 6, 4))
    x676 += einsum(x155, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    l3new_babbab += einsum(v.bbbb.ovov, (0, 1, 2, 3), x676, (4, 5, 2, 0, 6, 7), (1, 7, 3, 5, 6, 4)) * 2.0
    x677 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x677 += einsum(l2.aaaa, (0, 1, 2, 3), v.aabb.ooov, (4, 3, 5, 6), (5, 6, 2, 4, 0, 1))
    x678 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x678 += einsum(x657, (0, 1, 2, 3), l3.abaaba, (4, 0, 5, 6, 7, 2), (7, 1, 6, 3, 4, 5)) * -2.00000000000002
    x679 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x679 += einsum(x498, (0, 1, 2, 3), l3.abaaba, (4, 5, 6, 7, 0, 2), (1, 5, 7, 3, 4, 6)) * -2.0
    x680 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x680 += einsum(x28, (0, 1, 2, 3), x91, (4, 0, 2, 5, 6, 7), (4, 1, 5, 3, 6, 7)) * 2.0
    x681 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x681 += einsum(x447, (0, 1), l3.abaaba, (2, 3, 4, 5, 6, 0), (6, 3, 5, 1, 2, 4)) * -2.0
    x682 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x682 += einsum(v.aabb.ovov, (0, 1, 2, 3), x444, (4, 5, 6, 1), (2, 3, 0, 4, 5, 6)) * 2.0
    x683 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x683 += einsum(x606, (0, 1), l3.abaaba, (2, 3, 4, 5, 6, 0), (6, 3, 5, 1, 2, 4)) * -2.0
    x684 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x684 += einsum(x677, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 2.0
    x684 += einsum(x678, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x684 += einsum(x679, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x684 += einsum(x680, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x684 += einsum(x681, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x684 += einsum(x682, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x684 += einsum(x683, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    l3new_abaaba += einsum(x684, (0, 1, 2, 3, 4, 5), (5, 1, 4, 2, 0, 3)) * -1.0
    l3new_abaaba += einsum(x684, (0, 1, 2, 3, 4, 5), (5, 1, 4, 3, 0, 2))
    x685 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x685 += einsum(l2.abab, (0, 1, 2, 3), v.aabb.ovvv, (4, 5, 6, 1), (3, 6, 2, 4, 0, 5))
    x686 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x686 += einsum(l2.abab, (0, 1, 2, 3), v.aaaa.ovvv, (4, 5, 6, 0), (3, 1, 2, 4, 5, 6))
    x687 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x687 += einsum(v.aabb.ovoo, (0, 1, 2, 3), x80, (4, 2, 3, 5, 6, 7), (4, 5, 6, 0, 7, 1))
    x688 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x688 += einsum(x2, (0, 1, 2, 3), x80, (0, 4, 1, 5, 6, 7), (4, 5, 6, 2, 7, 3)) * -1.0
    x689 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x689 += einsum(t2.aaaa, (0, 1, 2, 3), x229, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.00000000000002
    x690 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x690 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x690 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x690 += einsum(x228, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x690 += einsum(x689, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x690 += einsum(x232, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x691 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x691 += einsum(x690, (0, 1, 2, 3), l3.abaaba, (4, 5, 2, 6, 7, 0), (7, 5, 6, 1, 4, 3)) * 2.0
    x692 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x692 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x692 += einsum(x234, (0, 1, 2, 3), (0, 1, 2, 3))
    x692 += einsum(x235, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.00000000000002
    x692 += einsum(x595, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x693 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x693 += einsum(x692, (0, 1, 2, 3), l3.babbab, (4, 5, 1, 6, 7, 0), (6, 4, 7, 2, 5, 3)) * 2.0
    x694 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x694 += einsum(x379, (0, 1, 2, 3), x58, (4, 5, 0, 6, 2, 7), (4, 5, 6, 1, 7, 3)) * 2.0
    x695 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x695 += einsum(x357, (0, 1, 2, 3), x58, (4, 5, 0, 6, 2, 7), (4, 5, 6, 1, 7, 3)) * 2.0
    x696 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x696 += einsum(v.aabb.ovov, (0, 1, 2, 3), x296, (4, 3, 5, 6), (2, 4, 0, 5, 1, 6)) * 2.0
    x697 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x697 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x100, (4, 5, 6, 1), (4, 5, 0, 2, 6, 3)) * 2.0
    x698 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x698 += einsum(v.aabb.ovov, (0, 1, 2, 3), x131, (4, 2, 5, 6), (4, 3, 0, 5, 1, 6)) * 2.0
    x699 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x699 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x63, (4, 5, 6, 2), (4, 5, 6, 0, 3, 1)) * 2.0
    x700 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x700 += einsum(l2.abab, (0, 1, 2, 3), x3, (3, 4, 5, 6), (4, 1, 2, 5, 0, 6))
    x701 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x701 += einsum(l2.abab, (0, 1, 2, 3), x382, (2, 4, 5, 6), (3, 1, 4, 5, 0, 6))
    x702 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x702 += einsum(l1.aa, (0, 1), v.aabb.ovov, (2, 3, 4, 5), (4, 5, 1, 2, 0, 3))
    x702 += einsum(x685, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x702 += einsum(x686, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x702 += einsum(x687, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    x702 += einsum(x688, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -2.0
    x702 += einsum(x691, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x702 += einsum(x693, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x702 += einsum(x694, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x702 += einsum(x695, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x702 += einsum(x696, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x702 += einsum(x697, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x702 += einsum(x698, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x702 += einsum(x699, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x702 += einsum(x700, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x702 += einsum(x701, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    l3new_abaaba += einsum(x702, (0, 1, 2, 3, 4, 5), (4, 1, 5, 2, 0, 3))
    l3new_abaaba += einsum(x702, (0, 1, 2, 3, 4, 5), (5, 1, 4, 2, 0, 3)) * -1.0
    l3new_abaaba += einsum(x702, (0, 1, 2, 3, 4, 5), (4, 1, 5, 3, 0, 2)) * -1.0
    l3new_abaaba += einsum(x702, (0, 1, 2, 3, 4, 5), (5, 1, 4, 3, 0, 2))
    x703 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x703 += einsum(l2.aaaa, (0, 1, 2, 3), v.aabb.vvov, (4, 1, 5, 6), (5, 6, 2, 3, 0, 4))
    x704 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x704 += einsum(f.aa.vv, (0, 1), l3.abaaba, (2, 3, 1, 4, 5, 6), (5, 3, 4, 6, 0, 2))
    x705 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x705 += einsum(f.aa.ov, (0, 1), x58, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x706 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x706 += einsum(v.aabb.vvvv, (0, 1, 2, 3), l3.abaaba, (4, 3, 1, 5, 6, 7), (6, 2, 5, 7, 4, 0))
    x707 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x707 += einsum(v.aabb.vvov, (0, 1, 2, 3), x91, (4, 2, 5, 6, 7, 1), (4, 3, 5, 6, 7, 0))
    x708 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x708 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), x58, (4, 5, 6, 7, 0, 3), (4, 5, 6, 7, 1, 2)) * -1.0
    x709 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x709 += einsum(v.aabb.ovvv, (0, 1, 2, 3), x58, (4, 3, 5, 6, 0, 7), (4, 2, 5, 6, 7, 1))
    x710 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x710 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1)) * 0.99999999999999
    x710 += einsum(x19, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.99999999999999
    x710 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x711 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x711 += einsum(x710, (0, 1, 2, 3), l3.abaaba, (4, 5, 2, 6, 0, 7), (1, 5, 6, 7, 4, 3)) * -2.00000000000002
    x712 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x712 += einsum(x421, (0, 1), l3.abaaba, (2, 3, 1, 4, 5, 6), (5, 3, 4, 6, 2, 0)) * -2.0
    x713 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x713 += einsum(x3, (0, 1, 2, 3), x58, (0, 4, 5, 6, 2, 7), (1, 4, 5, 6, 7, 3)) * 2.0
    x714 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x714 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 6, 7), (6, 1, 5, 7, 0, 4))
    x715 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x715 += einsum(x714, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x715 += einsum(x99, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x716 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x716 += einsum(v.aabb.ovov, (0, 1, 2, 3), x715, (4, 2, 5, 6, 0, 7), (4, 3, 5, 6, 1, 7)) * 2.0
    x717 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x717 += einsum(x358, (0, 1), x58, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x718 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x718 += einsum(v.aabb.ovov, (0, 1, 2, 3), x297, (4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * 2.0
    x719 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x719 += einsum(l1.bb, (0, 1), v.aaaa.ovov, (2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    x719 += einsum(x703, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -2.0
    x719 += einsum(x704, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 2.0
    x719 += einsum(x705, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -2.0
    x719 += einsum(x706, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -2.0
    x719 += einsum(x707, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 2.0
    x719 += einsum(x708, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 2.0
    x719 += einsum(x709, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 2.0
    x719 += einsum(x711, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x719 += einsum(x712, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x719 += einsum(x713, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x719 += einsum(x716, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x719 += einsum(x717, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x719 += einsum(x718, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    l3new_abaaba += einsum(x719, (0, 1, 2, 3, 4, 5), (5, 1, 4, 2, 0, 3))
    l3new_abaaba += einsum(x719, (0, 1, 2, 3, 4, 5), (4, 1, 5, 2, 0, 3)) * -1.0
    x720 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x720 += einsum(l2.aaaa, (0, 1, 2, 3), x4, (4, 5, 3, 6), (4, 5, 2, 6, 0, 1))
    l3new_abaaba += einsum(x720, (0, 1, 2, 3, 4, 5), (5, 1, 4, 2, 0, 3)) * 2.0
    l3new_abaaba += einsum(x720, (0, 1, 2, 3, 4, 5), (5, 1, 4, 3, 0, 2)) * -2.0
    x721 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x721 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * 0.499999999999995
    x721 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.499999999999995
    x721 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x721 += einsum(t2.bbbb, (0, 1, 2, 3), x7, (1, 4, 5, 3), (0, 4, 2, 5)) * -1.0
    x721 += einsum(t1.bb, (0, 1), x9, (2, 3, 1, 4), (0, 2, 4, 3)) * -0.499999999999995
    l3new_abaaba += einsum(x721, (0, 1, 2, 3), l3.abaaba, (4, 2, 5, 6, 0, 7), (4, 3, 5, 6, 1, 7)) * 4.00000000000004
    x722 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x722 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x722 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x722 += einsum(x13, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0000000000000204
    x722 += einsum(x626, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    l3new_abaaba += einsum(x722, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 3, 6, 7, 2), (4, 1, 5, 6, 0, 7)) * 6.0
    x723 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x723 += einsum(f.bb.vv, (0, 1), (0, 1)) * -0.5
    x723 += einsum(x215, (0, 1), (1, 0)) * -0.5
    x723 += einsum(x499, (0, 1), (0, 1))
    x723 += einsum(x500, (0, 1), (0, 1)) * 0.5
    x723 += einsum(t1.bb, (0, 1), x466, (0, 1, 2, 3), (3, 2)) * -0.5
    l3new_abaaba += einsum(x723, (0, 1), l3.abaaba, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -4.0
    x724 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x724 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x724 += einsum(x247, (0, 1, 2, 3), (1, 3, 2, 0))
    x724 += einsum(x248, (0, 1, 2, 3), (0, 2, 3, 1))
    x724 += einsum(x249, (0, 1, 2, 3), (2, 1, 3, 0))
    x724 += einsum(x249, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l3new_abaaba += einsum(x724, (0, 1, 2, 3), l3.abaaba, (4, 5, 6, 3, 7, 0), (4, 5, 6, 2, 7, 1)) * 2.0
    x725 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x725 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (2, 4, 3, 5, 6, 7), (6, 4, 5, 7, 0, 1))
    x725 += einsum(x302, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    l3new_abaaba += einsum(v.aaaa.ovov, (0, 1, 2, 3), x725, (4, 5, 6, 7, 2, 0), (1, 5, 3, 7, 4, 6)) * 2.0
    x726 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x726 += einsum(v.aabb.ooov, (0, 1, 2, 3), x55, (4, 5, 6, 7, 0, 1), (4, 5, 2, 6, 7, 3))
    x727 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x727 += einsum(x4, (0, 1, 2, 3), x55, (4, 5, 6, 7, 2, 3), (4, 5, 0, 6, 7, 1))
    x728 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x728 += einsum(t2.bbbb, (0, 1, 2, 3), x7, (1, 4, 5, 3), (0, 4, 2, 5)) * 2.0000000000000204
    x729 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x729 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x729 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x729 += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.00000000000001
    x729 += einsum(x728, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x729 += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x730 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x730 += einsum(x729, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 2, 6, 7, 0), (6, 7, 1, 4, 5, 3)) * 6.0
    x731 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x731 += einsum(x627, (0, 1, 2, 3), l3.babbab, (4, 3, 5, 6, 2, 7), (6, 7, 0, 4, 5, 1)) * 2.0
    x732 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x732 += einsum(x0, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x732 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3))
    x733 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x733 += einsum(x732, (0, 1, 2, 3), x78, (4, 5, 0, 1, 6, 7), (4, 5, 2, 6, 7, 3)) * 6.0
    x734 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x734 += einsum(x524, (0, 1, 2, 3), x78, (4, 5, 0, 2, 6, 7), (4, 5, 1, 6, 7, 3)) * 6.0
    x735 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x735 += einsum(x726, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 2.0
    x735 += einsum(x727, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * 2.0
    x735 += einsum(x730, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x735 += einsum(x731, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5))
    x735 += einsum(x733, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x735 += einsum(x734, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2))
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0))
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -1.0
    l3new_bbbbbb += einsum(x735, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0)) * -1.0
    x736 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x736 += einsum(f.bb.vv, (0, 1), l3.bbbbbb, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x737 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x737 += einsum(f.bb.ov, (0, 1), x78, (2, 3, 4, 0, 5, 6), (2, 3, 4, 1, 5, 6))
    x738 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x738 += einsum(v.bbbb.vvvv, (0, 1, 2, 3), l3.bbbbbb, (4, 3, 1, 5, 6, 7), (5, 6, 7, 4, 0, 2)) * -1.0
    x739 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x739 += einsum(x736, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    x739 += einsum(x737, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 6.0
    x739 += einsum(x738, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -6.0
    l3new_bbbbbb += einsum(x739, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0))
    l3new_bbbbbb += einsum(x739, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0))
    l3new_bbbbbb += einsum(x739, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    x740 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x740 += einsum(x572, (0, 1), l3.bbbbbb, (2, 3, 1, 4, 5, 6), (4, 5, 6, 2, 3, 0)) * 6.0
    x741 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x741 += einsum(x225, (0, 1), x78, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1)) * 6.0
    x742 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x742 += einsum(x740, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x742 += einsum(x741, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    l3new_bbbbbb += einsum(x742, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new_bbbbbb += einsum(x742, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x742, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    x743 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x743 += einsum(l2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 3, 5, 6), (2, 4, 5, 0, 1, 6))
    x744 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x744 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x147, (4, 5, 6, 1), (0, 2, 4, 3, 5, 6)) * 6.0
    x745 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x745 += einsum(x743, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x745 += einsum(x744, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 1, 2))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 1, 2)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 3, 5, 0, 2, 1)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (5, 3, 4, 0, 2, 1))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 0, 1))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 0, 1)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 0, 1)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0)) * -1.0
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0))
    l3new_bbbbbb += einsum(x745, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    x746 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x746 += einsum(l2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 5, 6, 1), (2, 3, 4, 0, 5, 6))
    x747 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x747 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x130, (4, 5, 2, 6), (0, 4, 5, 3, 1, 6)) * 2.0
    x748 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x748 += einsum(x746, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x748 += einsum(x747, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (3, 5, 4, 2, 1, 0)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (4, 3, 5, 2, 1, 0)) * -1.0
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0))
    l3new_bbbbbb += einsum(x748, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * -1.0
    x749 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x749 += einsum(x555, (0, 1), l3.bbbbbb, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4)) * 6.0
    l3new_bbbbbb += einsum(x749, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 0, 2))
    l3new_bbbbbb += einsum(x749, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x749, (0, 1, 2, 3, 4, 5), (5, 3, 4, 2, 1, 0))
    x750 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x750 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x750 += einsum(x22, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    x750 += einsum(x23, (0, 1, 2, 3), (0, 3, 1, 2))
    x751 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x751 += einsum(x750, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 6, 7, 0, 2), (7, 1, 3, 4, 5, 6)) * -6.0
    x752 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x752 += einsum(x647, (0, 1), l3.bbbbbb, (2, 3, 4, 5, 6, 0), (5, 6, 1, 2, 3, 4)) * 6.0
    x753 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x753 += einsum(x751, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3))
    x753 += einsum(x752, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    l3new_bbbbbb += einsum(x753, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2))
    l3new_bbbbbb += einsum(x753, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -1.0
    l3new_bbbbbb += einsum(x753, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    x754 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x754 += einsum(x24, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 6, 7, 0, 1), (7, 2, 3, 4, 5, 6))
    l3new_bbbbbb += einsum(x754, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * -6.0
    l3new_bbbbbb += einsum(x754, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * 6.0
    l3new_bbbbbb += einsum(x754, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * 6.0
    l3new_bbbbbb += einsum(x754, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1)) * -6.0
    l3new_bbbbbb += einsum(x754, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -6.0
    l3new_bbbbbb += einsum(x754, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * 6.0
    x755 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x755 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 2, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x756 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x756 += einsum(x755, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x756 += einsum(x154, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x757 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x757 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x756, (4, 5, 6, 0, 2, 7), (4, 5, 6, 1, 3, 7)) * 6.0
    l3new_bbbbbb += einsum(x757, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -1.0
    l3new_bbbbbb += einsum(x757, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0))
    l3new_bbbbbb += einsum(x757, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * -1.0
    x758 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x758 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), x78, (4, 5, 6, 0, 7, 3), (4, 5, 6, 7, 1, 2)) * -1.0
    l3new_bbbbbb += einsum(x758, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * -6.0
    l3new_bbbbbb += einsum(x758, (0, 1, 2, 3, 4, 5), (3, 5, 4, 1, 2, 0)) * 6.0
    l3new_bbbbbb += einsum(x758, (0, 1, 2, 3, 4, 5), (4, 3, 5, 1, 2, 0)) * 6.0
    l3new_bbbbbb += einsum(x758, (0, 1, 2, 3, 4, 5), (5, 3, 4, 1, 2, 0)) * -6.0
    l3new_bbbbbb += einsum(x758, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * -6.0
    l3new_bbbbbb += einsum(x758, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * 6.0
    x759 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x759 += einsum(l2.bbbb, (0, 1, 2, 3), x0, (3, 4, 5, 6), (2, 4, 5, 0, 1, 6))
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 1, 2)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 1, 2)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 1, 2)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (3, 4, 5, 0, 2, 1)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (4, 5, 3, 0, 2, 1)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (5, 4, 3, 0, 2, 1)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 0, 2)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 0, 2)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 0, 2)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 0, 1)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 0, 1)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 0, 1)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (3, 4, 5, 1, 2, 0)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (4, 5, 3, 1, 2, 0)) * 2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (5, 4, 3, 1, 2, 0)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (3, 4, 5, 2, 1, 0)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (4, 5, 3, 2, 1, 0)) * -2.0
    l3new_bbbbbb += einsum(x759, (0, 1, 2, 3, 4, 5), (5, 4, 3, 2, 1, 0)) * 2.0

    l1new.aa = l1new_aa
    l1new.bb = l1new_bb
    l2new.aaaa = l2new_aaaa
    l2new.abab = l2new_abab
    l2new.bbbb = l2new_bbbb
    l3new.aaaaaa = l3new_aaaaaa
    l3new.abaaba = l3new_abaaba
    l3new.babbab = l3new_babbab
    l3new.bbbbbb = l3new_bbbbbb

    return {"l1new": l1new, "l2new": l2new, "l3new": l3new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
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
    rdm1_f_aa_ov += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 2, 5, 1, 0), (4, 5)) * 2.0
    rdm1_f_aa_ov += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 0), (2, 3)) * 2.0
    rdm1_f_aa_ov += einsum(t1.aa, (0, 1), (0, 1))
    rdm1_f_aa_ov += einsum(l2.bbbb, (0, 1, 2, 3), t3.babbab, (2, 4, 3, 0, 5, 1), (4, 5))
    rdm1_f_aa_ov += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), (2, 3))
    rdm1_f_aa_ov += einsum(l2.aaaa, (0, 1, 2, 3), t3.aaaaaa, (4, 2, 3, 5, 0, 1), (4, 5)) * 3.0
    rdm1_f_bb_ov = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    rdm1_f_bb_ov += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), (2, 3))
    rdm1_f_bb_ov += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 0), (2, 3)) * 2.0
    rdm1_f_bb_ov += einsum(t1.bb, (0, 1), (0, 1))
    rdm1_f_bb_ov += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 3, 5, 0, 1), (4, 5)) * 2.0
    rdm1_f_bb_ov += einsum(l2.bbbb, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 3, 5, 0, 1), (4, 5)) * 3.0
    rdm1_f_bb_ov += einsum(l2.aaaa, (0, 1, 2, 3), t3.abaaba, (2, 4, 3, 0, 5, 1), (4, 5))
    rdm1_f_aa_vo = np.zeros((nvir[0], nocc[0]), dtype=np.float64)
    rdm1_f_aa_vo += einsum(l1.aa, (0, 1), (0, 1))
    rdm1_f_bb_vo = np.zeros((nvir[1], nocc[1]), dtype=np.float64)
    rdm1_f_bb_vo += einsum(l1.bb, (0, 1), (0, 1))
    rdm1_f_aa_vv = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    rdm1_f_aa_vv += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (3, 4, 5, 6, 1, 2), (0, 6)) * 2.9999999999998788
    rdm1_f_aa_vv += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 1), (0, 4)) * 2.0
    rdm1_f_aa_vv += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 6, 1, 2), (0, 6)) * 1.9999999999999194
    rdm1_f_aa_vv += einsum(l1.aa, (0, 1), t1.aa, (1, 2), (0, 2))
    rdm1_f_aa_vv += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), (0, 4))
    rdm1_f_aa_vv += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 0, 6, 2), (1, 6)) * 0.9999999999999601
    rdm1_f_bb_vv = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    rdm1_f_bb_vv += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (3, 4, 5, 6, 1, 2), (0, 6)) * 2.9999999999998788
    rdm1_f_bb_vv += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 1), (0, 4)) * 2.0
    rdm1_f_bb_vv += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 6, 1, 2), (0, 6)) * 1.9999999999999194
    rdm1_f_bb_vv += einsum(l1.bb, (0, 1), t1.bb, (1, 2), (0, 2))
    rdm1_f_bb_vv += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), (1, 4))
    rdm1_f_bb_vv += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 0, 6, 2), (1, 6)) * 0.9999999999999601
    x0 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x0 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 4, 5, 0, 1, 2), (3, 6))
    rdm1_f_aa_oo += einsum(x0, (0, 1), (1, 0)) * -2.9999999999998788
    x1 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x1 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 0, 1, 2), (3, 6))
    rdm1_f_aa_oo += einsum(x1, (0, 1), (1, 0)) * -1.9999999999999194
    x2 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 0, 1), (2, 4))
    rdm1_f_aa_oo += einsum(x2, (0, 1), (1, 0)) * -2.0
    x3 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x3 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 0, 1, 2), (4, 6))
    rdm1_f_aa_oo += einsum(x3, (0, 1), (1, 0)) * -0.9999999999999601
    x4 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x4 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), (2, 4))
    rdm1_f_aa_oo += einsum(x4, (0, 1), (1, 0)) * -1.0
    x5 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x5 += einsum(l1.aa, (0, 1), t1.aa, (2, 0), (1, 2))
    rdm1_f_aa_oo += einsum(x5, (0, 1), (1, 0)) * -1.0
    x6 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x6 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 0, 1, 2), (4, 6))
    rdm1_f_bb_oo += einsum(x6, (0, 1), (1, 0)) * -0.9999999999999601
    x7 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x7 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 4, 5, 0, 1, 2), (3, 6))
    rdm1_f_bb_oo += einsum(x7, (0, 1), (1, 0)) * -2.9999999999998788
    x8 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x8 += einsum(l1.bb, (0, 1), t1.bb, (2, 0), (1, 2))
    rdm1_f_bb_oo += einsum(x8, (0, 1), (1, 0)) * -1.0
    x9 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x9 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 0, 1, 2), (3, 6))
    rdm1_f_bb_oo += einsum(x9, (0, 1), (1, 0)) * -1.9999999999999194
    x10 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x10 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 0, 1), (2, 4))
    rdm1_f_bb_oo += einsum(x10, (0, 1), (1, 0)) * -2.0
    x11 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x11 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), (3, 4))
    rdm1_f_bb_oo += einsum(x11, (0, 1), (1, 0)) * -1.0
    x12 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x12 += einsum(t1.aa, (0, 1), l3.aaaaaa, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    rdm1_f_aa_ov += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x12, (1, 0, 2, 6, 4, 5), (6, 3)) * 2.9999999999998788
    x13 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(t1.aa, (0, 1), l3.abaaba, (2, 3, 1, 4, 5, 6), (5, 3, 4, 6, 0, 2))
    rdm1_f_aa_ov += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x13, (1, 4, 2, 0, 6, 5), (6, 3)) * -1.9999999999999194
    x14 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x14 += einsum(t1.aa, (0, 1), l3.babbab, (2, 1, 3, 4, 5, 6), (4, 6, 2, 3, 5, 0))
    rdm1_f_aa_ov += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x14, (0, 2, 5, 3, 1, 6), (6, 4)) * 0.9999999999999601
    x15 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x15 += einsum(t1.aa, (0, 1), l2.abab, (1, 2, 3, 4), (4, 2, 3, 0)) * 0.5
    x15 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 6, 1), (5, 4, 6, 0))
    x15 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (2, 4, 3, 5, 6, 1), (6, 4, 5, 0))
    rdm1_f_aa_ov += einsum(t2.abab, (0, 1, 2, 3), x15, (1, 3, 0, 4), (4, 2)) * -2.0
    x16 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x16 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    x16 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 1, 6), (5, 6, 0, 4))
    x16 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4)) * 3.0
    rdm1_f_aa_ov += einsum(t2.aaaa, (0, 1, 2, 3), x16, (0, 1, 4, 3), (4, 2)) * 2.0
    x17 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x17 += einsum(x5, (0, 1), (0, 1))
    x17 += einsum(x4, (0, 1), (0, 1))
    x17 += einsum(x2, (0, 1), (0, 1)) * 2.0
    x17 += einsum(x3, (0, 1), (0, 1)) * 0.9999999999999601
    x17 += einsum(x1, (0, 1), (0, 1)) * 1.9999999999999194
    x17 += einsum(x0, (0, 1), (0, 1)) * 2.9999999999998788
    rdm1_f_aa_ov += einsum(t1.aa, (0, 1), x17, (0, 2), (2, 1)) * -1.0
    x18 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x18 += einsum(t1.bb, (0, 1), l3.abaaba, (2, 1, 3, 4, 5, 6), (5, 0, 4, 6, 2, 3))
    rdm1_f_bb_ov += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x18, (1, 6, 2, 0, 3, 5), (6, 4)) * 0.9999999999999601
    x19 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x19 += einsum(t1.bb, (0, 1), l3.bbbbbb, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    rdm1_f_bb_ov += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x19, (0, 1, 2, 6, 5, 4), (6, 3)) * 2.9999999999998788
    x20 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x20 += einsum(t1.bb, (0, 1), l3.babbab, (2, 3, 1, 4, 5, 6), (4, 6, 0, 2, 5, 3))
    rdm1_f_bb_ov += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x20, (2, 0, 6, 5, 1, 4), (6, 3)) * -1.9999999999999194
    x21 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x21 += einsum(t1.bb, (0, 1), l2.abab, (2, 1, 3, 4), (4, 0, 3, 2)) * 0.5
    x21 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (2, 4, 3, 5, 6, 1), (5, 0, 6, 4))
    x21 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 6, 0), (6, 1, 5, 4))
    rdm1_f_bb_ov += einsum(t2.abab, (0, 1, 2, 3), x21, (1, 4, 0, 2), (4, 3)) * -2.0
    x22 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x22 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    x22 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4)) * 3.0
    x22 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 0, 6), (5, 6, 1, 4))
    rdm1_f_bb_ov += einsum(t2.bbbb, (0, 1, 2, 3), x22, (0, 1, 4, 3), (4, 2)) * 2.0
    x23 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x23 += einsum(x8, (0, 1), (0, 1)) * 1.00000000000004
    x23 += einsum(x10, (0, 1), (0, 1)) * 2.00000000000008
    x23 += einsum(x11, (0, 1), (0, 1)) * 1.00000000000004
    x23 += einsum(x7, (0, 1), (0, 1)) * 2.9999999999999982
    x23 += einsum(x9, (0, 1), (0, 1)) * 1.9999999999999991
    x23 += einsum(x6, (0, 1), (0, 1))
    rdm1_f_bb_ov += einsum(t1.bb, (0, 1), x23, (0, 2), (2, 1)) * -0.9999999999999601

    rdm1_f_aa = np.block([[rdm1_f_aa_oo, rdm1_f_aa_ov], [rdm1_f_aa_vo, rdm1_f_aa_vv]])
    rdm1_f_bb = np.block([[rdm1_f_bb_oo, rdm1_f_bb_ov], [rdm1_f_bb_vo, rdm1_f_bb_vv]])

    rdm1_f.aa = rdm1_f_aa
    rdm1_f.bb = rdm1_f_bb

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, l1=None, l2=None, l3=None, **kwargs):
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
    rdm2_f_aaaa_oovv += einsum(l1.aa, (0, 1), t3.aaaaaa, (2, 3, 1, 4, 5, 0), (2, 3, 4, 5)) * 6.0
    rdm2_f_aaaa_oovv += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_aaaa_oovv += einsum(l1.bb, (0, 1), t3.abaaba, (2, 1, 3, 4, 0, 5), (2, 3, 4, 5)) * 2.0
    rdm2_f_abab_oovv = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_oovv += einsum(l1.aa, (0, 1), t3.abaaba, (2, 3, 1, 4, 5, 0), (2, 3, 4, 5)) * 2.0
    rdm2_f_abab_oovv += einsum(l1.bb, (0, 1), t3.babbab, (2, 3, 1, 4, 5, 0), (3, 2, 5, 4)) * 2.0
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_oovv = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_oovv += einsum(l1.bb, (0, 1), t3.bbbbbb, (2, 3, 1, 4, 5, 0), (2, 3, 4, 5)) * 6.0
    rdm2_f_bbbb_oovv += einsum(l1.aa, (0, 1), t3.babbab, (2, 1, 3, 4, 0, 5), (2, 3, 4, 5)) * 2.0
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
    rdm2_f_abab_ovvv += einsum(l2.bbbb, (0, 1, 2, 3), t3.babbab, (2, 4, 3, 5, 6, 1), (4, 0, 6, 5)) * 2.0
    rdm2_f_abab_ovvv += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_abab_ovvv += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 2, 5, 6, 0), (4, 1, 5, 6)) * 2.0
    rdm2_f_abab_vovv = np.zeros((nvir[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_vovv += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 3, 5, 6, 1), (0, 4, 6, 5)) * 2.0
    rdm2_f_abab_vovv += einsum(l2.aaaa, (0, 1, 2, 3), t3.abaaba, (2, 4, 3, 5, 6, 1), (0, 4, 5, 6)) * 2.0
    rdm2_f_abab_vovv += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 3, 4), (0, 2, 3, 4))
    rdm2_f_abab_vvov = np.zeros((nvir[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_vvov += einsum(t1.bb, (0, 1), l2.abab, (2, 3, 4, 0), (2, 3, 4, 1))
    rdm2_f_aaaa_vvvv = np.zeros((nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_vvvv += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7)) * 6.000000000000116
    rdm2_f_aaaa_vvvv += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 5), (0, 1, 4, 5)) * 2.0
    rdm2_f_aaaa_vvvv += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 6, 1, 7), (0, 2, 6, 7)) * 2.0000000000000404
    rdm2_f_abab_vvvv = np.zeros((nvir[0], nvir[1], nvir[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_vvvv += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7)) * 2.0000000000000404
    rdm2_f_abab_vvvv += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 6, 7, 2), (1, 0, 7, 6)) * 2.0000000000000404
    rdm2_f_abab_vvvv += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 5), (0, 1, 4, 5))
    rdm2_f_bbbb_vvvv = np.zeros((nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_vvvv += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (3, 4, 5, 6, 7, 2), (0, 1, 6, 7)) * 6.000000000000116
    rdm2_f_bbbb_vvvv += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 5), (0, 1, 4, 5)) * 2.0
    rdm2_f_bbbb_vvvv += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 6, 1, 7), (0, 2, 6, 7)) * 2.0000000000000404
    x0 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x0 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    rdm2_f_aaaa_oooo += einsum(x0, (0, 1, 2, 3), (2, 3, 1, 0)) * -6.000000000000116
    x1 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x1 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 7, 0, 1, 2), (3, 5, 6, 7))
    rdm2_f_aaaa_oooo += einsum(x1, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0000000000000404
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_aaaa_oooo += einsum(x2, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x3 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_aaaa_ovoo += einsum(x3, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    rdm2_f_aaaa_vooo += einsum(x3, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x4 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x4 += einsum(t1.aa, (0, 1), x3, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_aaaa_oooo += einsum(x4, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x5 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x5 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 1), (2, 4))
    x6 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x6 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 0, 1), (2, 4))
    x7 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x7 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 0, 1, 2), (4, 6))
    x8 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x8 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 0, 1, 2), (3, 6))
    x9 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x9 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 4, 5, 0, 1, 2), (3, 6))
    x10 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x10 += einsum(x5, (0, 1), (0, 1))
    x10 += einsum(x6, (0, 1), (0, 1)) * 2.0
    x10 += einsum(x7, (0, 1), (0, 1)) * 0.9999999999999601
    x10 += einsum(x8, (0, 1), (0, 1)) * 1.9999999999999194
    x10 += einsum(x9, (0, 1), (0, 1)) * 2.9999999999998788
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x10, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x10, (2, 3), (0, 3, 2, 1))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x10, (2, 3), (3, 0, 1, 2))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x10, (2, 3), (3, 0, 2, 1)) * -1.0
    x11 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x11 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 1, 6), (5, 6, 0, 4))
    rdm2_f_aaaa_ovoo += einsum(x11, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    rdm2_f_aaaa_vooo += einsum(x11, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x12 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x12 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    rdm2_f_aaaa_ovoo += einsum(x12, (0, 1, 2, 3), (2, 3, 1, 0)) * -6.0
    rdm2_f_aaaa_vooo += einsum(x12, (0, 1, 2, 3), (3, 2, 1, 0)) * 6.0
    x13 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x13 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x14 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x14 += einsum(t1.aa, (0, 1), x13, (2, 3, 4, 1), (0, 2, 3, 4)) * 2.0
    rdm2_f_aaaa_oooo += einsum(x14, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_aaaa_oooo += einsum(x14, (0, 1, 2, 3), (3, 0, 2, 1))
    x15 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x15 += einsum(l1.aa, (0, 1), t1.aa, (2, 0), (1, 2))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x15, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x15, (2, 3), (3, 0, 1, 2))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x15, (2, 3), (0, 3, 2, 1))
    rdm2_f_aaaa_oooo += einsum(delta.aa.oo, (0, 1), x15, (2, 3), (3, 0, 2, 1)) * -1.0
    x16 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x16 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 7, 5, 0, 1, 2), (4, 7, 3, 6))
    rdm2_f_abab_oooo = np.zeros((nocc[0], nocc[1], nocc[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_oooo += einsum(x16, (0, 1, 2, 3), (3, 1, 2, 0)) * 2.0000000000000404
    x17 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x17 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 7, 5, 0, 1, 2), (3, 6, 4, 7))
    rdm2_f_abab_oooo += einsum(x17, (0, 1, 2, 3), (3, 1, 2, 0)) * 2.0000000000000404
    x18 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x18 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 0, 1), (3, 5, 2, 4))
    rdm2_f_abab_oooo += einsum(x18, (0, 1, 2, 3), (3, 1, 2, 0))
    x19 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x19 += einsum(t1.aa, (0, 1), l2.abab, (1, 2, 3, 4), (4, 2, 3, 0))
    rdm2_f_abab_ovoo += einsum(x19, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    x20 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x20 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 6, 1), (5, 4, 6, 0))
    rdm2_f_abab_ovoo += einsum(x20, (0, 1, 2, 3), (3, 1, 2, 0)) * -2.0
    x21 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x21 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (2, 4, 3, 5, 6, 1), (6, 4, 5, 0))
    rdm2_f_abab_ovoo += einsum(x21, (0, 1, 2, 3), (3, 1, 2, 0)) * -2.0
    x22 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x22 += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x22 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    x22 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oooo += einsum(t1.bb, (0, 1), x22, (2, 1, 3, 4), (4, 0, 3, 2)) * 2.0
    rdm2_f_abab_oovo = np.zeros((nocc[0], nocc[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_oovo += einsum(t2.abab, (0, 1, 2, 3), x22, (4, 3, 0, 5), (5, 1, 2, 4)) * 2.0
    rdm2_f_abab_oovv += einsum(x22, (0, 1, 2, 3), t3.babbab, (4, 2, 0, 5, 6, 1), (3, 4, 6, 5)) * -4.0
    x23 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x23 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (2, 4, 3, 5, 6, 1), (5, 0, 6, 4))
    rdm2_f_abab_vooo += einsum(x23, (0, 1, 2, 3), (3, 1, 2, 0)) * -2.0
    x24 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x24 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 6, 0), (6, 1, 5, 4))
    rdm2_f_abab_vooo += einsum(x24, (0, 1, 2, 3), (3, 1, 2, 0)) * -2.0
    x25 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x25 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x25 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3))
    x26 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x26 += einsum(t1.aa, (0, 1), x25, (2, 3, 4, 1), (2, 3, 0, 4)) * 2.0
    rdm2_f_abab_oooo += einsum(x26, (0, 1, 2, 3), (2, 1, 3, 0))
    x27 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x27 += einsum(delta.aa.oo, (0, 1), (0, 1)) * -0.3333333333333468
    x27 += einsum(x15, (0, 1), (0, 1)) * 0.3333333333333468
    x27 += einsum(x5, (0, 1), (0, 1)) * 0.3333333333333468
    x27 += einsum(x6, (0, 1), (0, 1)) * 0.6666666666666936
    x27 += einsum(x7, (0, 1), (0, 1)) * 0.33333333333333354
    x27 += einsum(x8, (0, 1), (0, 1)) * 0.6666666666666667
    x27 += einsum(x9, (0, 1), (0, 1))
    rdm2_f_abab_oooo += einsum(delta.bb.oo, (0, 1), x27, (2, 3), (3, 0, 2, 1)) * -2.9999999999998788
    x28 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x28 += einsum(l1.bb, (0, 1), t1.bb, (2, 0), (1, 2))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x28, (2, 3), (0, 3, 1, 2)) * -1.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x28, (2, 3), (3, 0, 1, 2))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x28, (2, 3), (0, 3, 2, 1))
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x28, (2, 3), (3, 0, 2, 1)) * -1.0
    x29 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x29 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 0, 1), (2, 4))
    x30 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x30 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 1), (3, 4))
    x31 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x31 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 4, 5, 0, 1, 2), (3, 6))
    x32 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x32 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 0, 1, 2), (3, 6))
    x33 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x33 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 0, 1, 2), (4, 6))
    x34 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x34 += einsum(x28, (0, 1), (0, 1)) * 0.3333333333333468
    x34 += einsum(x29, (0, 1), (0, 1)) * 0.6666666666666936
    x34 += einsum(x30, (0, 1), (0, 1)) * 0.3333333333333468
    x34 += einsum(x31, (0, 1), (0, 1))
    x34 += einsum(x32, (0, 1), (0, 1)) * 0.6666666666666667
    x34 += einsum(x33, (0, 1), (0, 1)) * 0.33333333333333354
    rdm2_f_abab_oooo += einsum(delta.aa.oo, (0, 1), x34, (2, 3), (0, 3, 1, 2)) * -2.9999999999998788
    rdm2_f_abab_oovo += einsum(t1.aa, (0, 1), x34, (2, 3), (0, 3, 1, 2)) * -2.9999999999998788
    x35 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x35 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_bbbb_oooo += einsum(x35, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x36 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x36 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 1, 3, 4), (3, 4, 0, 2))
    rdm2_f_bbbb_ovoo += einsum(x36, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    rdm2_f_bbbb_vooo += einsum(x36, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x37 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x37 += einsum(t1.bb, (0, 1), x36, (2, 3, 4, 1), (2, 3, 0, 4))
    rdm2_f_bbbb_oooo += einsum(x37, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x38 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x38 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 7, 0, 1, 2), (3, 5, 6, 7))
    rdm2_f_bbbb_oooo += einsum(x38, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0000000000000404
    x39 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x39 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 7, 5, 0, 1, 2), (3, 4, 6, 7))
    rdm2_f_bbbb_oooo += einsum(x39, (0, 1, 2, 3), (2, 3, 1, 0)) * -6.000000000000116
    x40 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x40 += einsum(x29, (0, 1), (0, 1))
    x40 += einsum(x30, (0, 1), (0, 1)) * 0.5
    x40 += einsum(x31, (0, 1), (0, 1)) * 1.4999999999999394
    x40 += einsum(x32, (0, 1), (0, 1)) * 0.9999999999999597
    x40 += einsum(x33, (0, 1), (0, 1)) * 0.49999999999998007
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x40, (2, 3), (0, 3, 1, 2)) * -2.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x40, (2, 3), (0, 3, 2, 1)) * 2.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x40, (2, 3), (3, 0, 1, 2)) * 2.0
    rdm2_f_bbbb_oooo += einsum(delta.bb.oo, (0, 1), x40, (2, 3), (3, 0, 2, 1)) * -2.0
    x41 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x41 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 2, 3, 5, 6, 1), (5, 6, 0, 4))
    rdm2_f_bbbb_ovoo += einsum(x41, (0, 1, 2, 3), (2, 3, 1, 0)) * -6.0
    rdm2_f_bbbb_vooo += einsum(x41, (0, 1, 2, 3), (3, 2, 1, 0)) * 6.0
    x42 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x42 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 0, 6), (5, 6, 1, 4))
    rdm2_f_bbbb_ovoo += einsum(x42, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    rdm2_f_bbbb_vooo += einsum(x42, (0, 1, 2, 3), (3, 2, 1, 0)) * 2.0
    x43 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x43 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3))
    x43 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x44 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x44 += einsum(t1.bb, (0, 1), x43, (2, 3, 4, 1), (0, 2, 3, 4)) * 6.0
    rdm2_f_bbbb_oooo += einsum(x44, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    rdm2_f_bbbb_oooo += einsum(x44, (0, 1, 2, 3), (3, 0, 2, 1))
    x45 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x45 += einsum(l2.aaaa, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6))
    rdm2_f_aaaa_ooov = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_ooov += einsum(x45, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_aaaa_oovo = np.zeros((nocc[0], nocc[0], nvir[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_oovo += einsum(x45, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    x46 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x46 += einsum(t1.aa, (0, 1), l3.abaaba, (2, 3, 1, 4, 5, 6), (5, 3, 4, 6, 0, 2))
    rdm2_f_abab_ovvv += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x46, (1, 6, 0, 2, 7, 5), (7, 6, 3, 4)) * 2.0000000000000404
    x47 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x47 += einsum(t1.aa, (0, 1), x46, (2, 3, 4, 5, 6, 1), (2, 3, 4, 5, 6, 0)) * -1.0
    x48 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x48 += einsum(t2.abab, (0, 1, 2, 3), x47, (1, 3, 4, 0, 5, 6), (4, 6, 5, 2)) * -1.0
    rdm2_f_aaaa_ooov += einsum(x48, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_aaaa_oovo += einsum(x48, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x49 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x49 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_aaaa_ooov += einsum(x49, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_aaaa_oovo += einsum(x49, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x50 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x50 += einsum(t1.aa, (0, 1), l3.aaaaaa, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x51 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x51 += einsum(t1.aa, (0, 1), x50, (2, 3, 4, 5, 1, 6), (2, 3, 4, 5, 0, 6))
    x52 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x52 += einsum(t2.aaaa, (0, 1, 2, 3), x51, (4, 0, 1, 5, 6, 3), (4, 6, 5, 2)) * -1.0
    rdm2_f_aaaa_ooov += einsum(x52, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_aaaa_oovo += einsum(x52, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    x53 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x53 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 5, 6, 1, 0), (2, 4, 5, 6))
    rdm2_f_aaaa_ooov += einsum(x53, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_aaaa_oovo += einsum(x53, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x54 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x54 += einsum(t2.abab, (0, 1, 2, 3), x20, (1, 3, 4, 5), (4, 0, 5, 2))
    x55 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x55 += einsum(t1.aa, (0, 1), l3.babbab, (2, 1, 3, 4, 5, 6), (4, 6, 2, 3, 5, 0))
    rdm2_f_abab_ovvv += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (2, 0, 6, 5, 1, 7), (7, 6, 4, 3)) * 2.0000000000000404
    x56 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x56 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (2, 0, 3, 5, 6, 7), (6, 7, 1, 4)) * -1.0
    x57 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x57 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x46, (1, 4, 6, 2, 7, 5), (6, 7, 0, 3)) * -1.0
    x58 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x58 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x50, (6, 1, 2, 7, 4, 5), (6, 7, 0, 3))
    x59 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x59 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x59 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    x59 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oovv += einsum(x59, (0, 1, 2, 3), t3.abaaba, (0, 4, 1, 5, 6, 3), (2, 4, 5, 6)) * 6.0
    x60 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x60 += einsum(t2.aaaa, (0, 1, 2, 3), x59, (1, 4, 5, 3), (0, 4, 5, 2)) * 12.0
    x61 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x61 += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3))
    x61 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x62 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x62 += einsum(t2.abab, (0, 1, 2, 3), x61, (1, 3, 4, 5), (0, 4, 5, 2))
    x63 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x63 += einsum(t1.aa, (0, 1), x13, (2, 3, 4, 1), (0, 2, 3, 4))
    x64 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x64 += einsum(t1.aa, (0, 1), x63, (2, 0, 3, 4), (3, 2, 4, 1)) * 2.0
    x65 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x65 += einsum(x15, (0, 1), (0, 1))
    x65 += einsum(x5, (0, 1), (0, 1))
    x65 += einsum(x6, (0, 1), (0, 1)) * 2.0
    x65 += einsum(x7, (0, 1), (0, 1)) * 0.9999999999999601
    x65 += einsum(x8, (0, 1), (0, 1)) * 1.9999999999999194
    x65 += einsum(x9, (0, 1), (0, 1)) * 2.9999999999998788
    x66 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x66 += einsum(delta.aa.oo, (0, 1), t1.aa, (2, 3), (0, 1, 2, 3))
    x66 += einsum(x54, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x66 += einsum(x56, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x66 += einsum(x57, (0, 1, 2, 3), (1, 0, 2, 3)) * -4.0
    x66 += einsum(x58, (0, 1, 2, 3), (1, 0, 2, 3)) * -9.0
    x66 += einsum(x60, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x66 += einsum(x62, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x66 += einsum(x64, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x66 += einsum(t1.aa, (0, 1), x65, (2, 3), (0, 2, 3, 1))
    rdm2_f_aaaa_ooov += einsum(x66, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_ooov += einsum(x66, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_aaaa_oovo += einsum(x66, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_aaaa_oovo += einsum(x66, (0, 1, 2, 3), (2, 0, 3, 1))
    x67 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x67 += einsum(l1.bb, (0, 1), t2.abab, (2, 1, 3, 0), (2, 3))
    x68 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x68 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 0), (2, 3))
    x69 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x69 += einsum(l2.bbbb, (0, 1, 2, 3), t3.babbab, (2, 4, 3, 0, 5, 1), (4, 5))
    x70 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x70 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 2, 5, 1, 0), (4, 5))
    x71 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x71 += einsum(l2.aaaa, (0, 1, 2, 3), t3.aaaaaa, (4, 2, 3, 5, 0, 1), (4, 5))
    x72 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x72 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (0, 2, 3, 5, 1, 6), (6, 4))
    x73 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x73 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x46, (1, 4, 0, 2, 6, 5), (6, 3)) * -1.0
    x74 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x74 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x50, (0, 1, 2, 6, 4, 5), (6, 3))
    x75 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x75 += einsum(t2.abab, (0, 1, 2, 3), x22, (1, 3, 0, 4), (4, 2)) * 2.0
    x76 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x76 += einsum(t2.aaaa, (0, 1, 2, 3), x59, (0, 1, 4, 3), (4, 2)) * -6.0
    x77 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x77 += einsum(t1.aa, (0, 1), x65, (0, 2), (2, 1))
    x78 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x78 += einsum(x67, (0, 1), (0, 1)) * -1.0
    x78 += einsum(x68, (0, 1), (0, 1)) * -2.0
    x78 += einsum(x69, (0, 1), (0, 1)) * -1.0
    x78 += einsum(x70, (0, 1), (0, 1)) * -2.0
    x78 += einsum(x71, (0, 1), (0, 1)) * -3.0
    x78 += einsum(x72, (0, 1), (0, 1)) * 0.9999999999999601
    x78 += einsum(x73, (0, 1), (0, 1)) * 1.9999999999999194
    x78 += einsum(x74, (0, 1), (0, 1)) * 2.9999999999998788
    x78 += einsum(x75, (0, 1), (0, 1))
    x78 += einsum(x76, (0, 1), (0, 1))
    x78 += einsum(x77, (0, 1), (0, 1))
    rdm2_f_aaaa_ooov += einsum(delta.aa.oo, (0, 1), x78, (2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_aaaa_ooov += einsum(delta.aa.oo, (0, 1), x78, (2, 3), (2, 0, 1, 3))
    rdm2_f_aaaa_oovo += einsum(delta.aa.oo, (0, 1), x78, (2, 3), (0, 2, 3, 1))
    rdm2_f_aaaa_oovo += einsum(delta.aa.oo, (0, 1), x78, (2, 3), (2, 0, 3, 1)) * -1.0
    x79 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x79 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 5, 6, 1, 0), (6, 4, 5, 2))
    rdm2_f_aaaa_vvov = np.zeros((nvir[0], nvir[0], nocc[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_vvov += einsum(x79, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_aaaa_vvvo = np.zeros((nvir[0], nvir[0], nvir[0], nocc[0]), dtype=np.float64)
    rdm2_f_aaaa_vvvo += einsum(x79, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x80 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x80 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    rdm2_f_aaaa_vvov += einsum(x80, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_aaaa_vvvo += einsum(x80, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    x81 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x81 += einsum(x79, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x81 += einsum(x80, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    rdm2_f_abab_oovv += einsum(x81, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 1, 6, 2), (4, 5, 3, 6)) * 2.0
    x82 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x82 += einsum(t2.aaaa, (0, 1, 2, 3), x81, (4, 2, 3, 5), (0, 1, 4, 5)) * 2.0
    rdm2_f_aaaa_ooov += einsum(x82, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_aaaa_oovo += einsum(x82, (0, 1, 2, 3), (1, 0, 3, 2))
    x83 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x83 += einsum(x2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x83 += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2))
    x83 += einsum(x1, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.0000000000000202
    x83 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2)) * 3.000000000000058
    x84 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x84 += einsum(t1.aa, (0, 1), x83, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_aaaa_ooov += einsum(x84, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_aaaa_oovo += einsum(x84, (0, 1, 2, 3), (2, 1, 3, 0))
    x85 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x85 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x50, (0, 2, 6, 7, 3, 5), (1, 4, 6, 7))
    rdm2_f_abab_ooov = np.zeros((nocc[0], nocc[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_ooov += einsum(x85, (0, 1, 2, 3), (3, 0, 2, 1)) * -3.0
    x86 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x86 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 5, 3, 6, 0, 1), (4, 6, 2, 5))
    rdm2_f_abab_ooov += einsum(x86, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x87 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x87 += einsum(t1.bb, (0, 1), l3.babbab, (2, 3, 1, 4, 5, 6), (4, 6, 0, 2, 5, 3))
    rdm2_f_abab_vovv += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x87, (2, 0, 6, 5, 1, 7), (7, 6, 4, 3)) * -2.0000000000000404
    x88 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x88 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x87, (0, 2, 6, 5, 7, 4), (6, 3, 7, 1)) * -1.0
    rdm2_f_abab_ooov += einsum(x88, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x89 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x89 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x55, (1, 2, 4, 5, 6, 7), (0, 3, 6, 7))
    rdm2_f_abab_ooov += einsum(x89, (0, 1, 2, 3), (3, 0, 2, 1)) * -3.0
    x90 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x90 += einsum(t1.bb, (0, 1), x55, (2, 3, 1, 4, 5, 6), (2, 3, 0, 4, 5, 6)) * -1.0
    x91 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x91 += einsum(t2.bbbb, (0, 1, 2, 3), x90, (0, 1, 4, 3, 5, 6), (4, 2, 5, 6)) * -1.0
    rdm2_f_abab_ooov += einsum(x91, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x92 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x92 += einsum(l2.aaaa, (0, 1, 2, 3), t3.abaaba, (4, 5, 3, 0, 6, 1), (5, 6, 2, 4))
    rdm2_f_abab_ooov += einsum(x92, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x93 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x93 += einsum(l1.aa, (0, 1), t2.abab, (2, 3, 0, 4), (3, 4, 1, 2))
    rdm2_f_abab_ooov += einsum(x93, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x94 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x94 += einsum(t1.bb, (0, 1), l3.abaaba, (2, 1, 3, 4, 5, 6), (5, 0, 4, 6, 2, 3))
    rdm2_f_abab_vovv += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x94, (1, 6, 0, 2, 7, 5), (7, 6, 3, 4)) * -2.0000000000000404
    x95 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x95 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x94, (1, 6, 7, 2, 3, 5), (6, 4, 7, 0))
    rdm2_f_abab_ooov += einsum(x95, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x96 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x96 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x46, (2, 5, 6, 1, 7, 4), (0, 3, 6, 7)) * -1.0
    rdm2_f_abab_ooov += einsum(x96, (0, 1, 2, 3), (3, 0, 2, 1)) * -4.0
    x97 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x97 += einsum(t1.bb, (0, 1), x46, (2, 1, 3, 4, 5, 6), (2, 0, 4, 3, 5, 6)) * -1.0
    x98 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x98 += einsum(t2.abab, (0, 1, 2, 3), x97, (1, 4, 0, 5, 6, 2), (4, 3, 5, 6))
    rdm2_f_abab_ooov += einsum(x98, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x99 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x99 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (4, 5, 3, 0, 6, 1), (4, 2, 6, 5))
    rdm2_f_abab_vvov += einsum(x99, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x100 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x100 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 5, 2, 6, 1, 0), (5, 3, 6, 4))
    rdm2_f_abab_vvov += einsum(x100, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x101 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x101 += einsum(x99, (0, 1, 2, 3), (0, 1, 2, 3))
    x101 += einsum(x100, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_ooov += einsum(t2.abab, (0, 1, 2, 3), x101, (3, 4, 5, 2), (0, 1, 5, 4)) * 2.0
    rdm2_f_abab_ovvv += einsum(t2.aaaa, (0, 1, 2, 3), x101, (4, 5, 1, 3), (0, 4, 2, 5)) * 4.0
    rdm2_f_abab_vovv += einsum(t2.abab, (0, 1, 2, 3), x101, (3, 4, 0, 5), (5, 1, 2, 4)) * -2.0
    rdm2_f_abab_vvvv += einsum(t1.aa, (0, 1), x101, (2, 3, 0, 4), (4, 2, 1, 3)) * 2.0
    x102 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x102 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x102 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    rdm2_f_abab_ooov += einsum(t2.abab, (0, 1, 2, 3), x102, (0, 4, 5, 2), (5, 1, 4, 3)) * -2.0
    x103 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum(t1.bb, (0, 1), l2.abab, (2, 1, 3, 4), (4, 0, 3, 2))
    rdm2_f_abab_vooo += einsum(x103, (0, 1, 2, 3), (3, 1, 2, 0)) * -1.0
    x104 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x104 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3))
    x104 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x104 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_abab_ooov += einsum(t2.abab, (0, 1, 2, 3), x104, (1, 4, 5, 2), (0, 4, 5, 3))
    rdm2_f_abab_vovo = np.zeros((nvir[0], nocc[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_vovo += einsum(t1.aa, (0, 1), x104, (2, 3, 0, 4), (4, 3, 1, 2)) * -1.0
    rdm2_f_abab_vovv += einsum(t2.abab, (0, 1, 2, 3), x104, (1, 4, 0, 5), (5, 4, 2, 3)) * -1.0
    x105 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x105 += einsum(x19, (0, 1, 2, 3), (0, 1, 2, 3))
    x105 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x105 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_abab_ooov += einsum(t2.bbbb, (0, 1, 2, 3), x105, (1, 3, 4, 5), (5, 0, 4, 2)) * -2.0
    rdm2_f_abab_ovov = np.zeros((nocc[0], nvir[1], nocc[0], nvir[1]), dtype=np.float64)
    rdm2_f_abab_ovov += einsum(t1.bb, (0, 1), x105, (0, 2, 3, 4), (4, 2, 3, 1)) * -1.0
    rdm2_f_abab_ovvo += einsum(t1.aa, (0, 1), x105, (2, 3, 0, 4), (4, 3, 1, 2)) * -1.0
    rdm2_f_abab_ovvv += einsum(t2.abab, (0, 1, 2, 3), x105, (1, 4, 0, 5), (5, 4, 2, 3)) * -1.0
    x106 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x106 += einsum(t1.bb, (0, 1), x105, (2, 1, 3, 4), (2, 0, 3, 4))
    x107 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x107 += einsum(x18, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0000000000000404
    x107 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0000000000000404
    x107 += einsum(x106, (0, 1, 2, 3), (0, 1, 2, 3))
    x107 += einsum(x26, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_abab_ooov += einsum(t1.bb, (0, 1), x107, (0, 2, 3, 4), (4, 2, 3, 1))
    x108 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x108 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 0), (2, 3))
    x109 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x109 += einsum(l1.aa, (0, 1), t2.abab, (1, 2, 0, 3), (2, 3))
    x110 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x110 += einsum(l2.bbbb, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 3, 5, 0, 1), (4, 5))
    x111 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x111 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 3, 5, 0, 1), (4, 5))
    x112 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x112 += einsum(l2.aaaa, (0, 1, 2, 3), t3.abaaba, (2, 4, 3, 0, 5, 1), (4, 5))
    x113 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(t1.bb, (0, 1), l3.bbbbbb, (2, 3, 1, 4, 5, 6), (4, 5, 6, 0, 2, 3))
    x114 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x114 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x113, (0, 1, 2, 6, 4, 5), (6, 3))
    x115 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x115 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x87, (0, 2, 6, 5, 1, 4), (6, 3)) * -1.0
    x116 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x116 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x94, (1, 6, 0, 2, 5, 3), (6, 4)) * -1.0
    x117 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x117 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x117 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x117 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3))
    x118 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x118 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x118 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    x118 += einsum(x24, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oovo += einsum(t2.aaaa, (0, 1, 2, 3), x118, (4, 5, 1, 3), (0, 5, 2, 4)) * -4.0
    rdm2_f_abab_oovv += einsum(x118, (0, 1, 2, 3), t3.abaaba, (4, 0, 2, 5, 6, 3), (4, 1, 5, 6)) * -4.0
    rdm2_f_abab_voov += einsum(t1.bb, (0, 1), x118, (0, 2, 3, 4), (4, 2, 3, 1)) * -2.0
    x119 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x119 += einsum(x28, (0, 1), (0, 1))
    x119 += einsum(x29, (0, 1), (0, 1)) * 2.0
    x119 += einsum(x30, (0, 1), (0, 1))
    x119 += einsum(x31, (0, 1), (0, 1)) * 2.9999999999998788
    x119 += einsum(x32, (0, 1), (0, 1)) * 1.9999999999999194
    x119 += einsum(x33, (0, 1), (0, 1)) * 0.9999999999999601
    x120 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x120 += einsum(t1.bb, (0, 1), (0, 1)) * -1.0
    x120 += einsum(x108, (0, 1), (0, 1)) * -2.0
    x120 += einsum(x109, (0, 1), (0, 1)) * -1.0
    x120 += einsum(x110, (0, 1), (0, 1)) * -3.0
    x120 += einsum(x111, (0, 1), (0, 1)) * -2.0
    x120 += einsum(x112, (0, 1), (0, 1)) * -1.0
    x120 += einsum(x114, (0, 1), (0, 1)) * 2.9999999999998788
    x120 += einsum(x115, (0, 1), (0, 1)) * 1.9999999999999194
    x120 += einsum(x116, (0, 1), (0, 1)) * 0.9999999999999601
    x120 += einsum(t2.bbbb, (0, 1, 2, 3), x117, (0, 1, 4, 3), (4, 2)) * -2.0
    x120 += einsum(t2.abab, (0, 1, 2, 3), x118, (1, 4, 0, 2), (4, 3)) * 2.0
    x120 += einsum(t1.bb, (0, 1), x119, (0, 2), (2, 1))
    rdm2_f_abab_ooov += einsum(delta.aa.oo, (0, 1), x120, (2, 3), (0, 2, 1, 3)) * -1.0
    x121 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x121 += einsum(x15, (0, 1), (0, 1)) * 0.5000000000000202
    x121 += einsum(x5, (0, 1), (0, 1)) * 0.5000000000000202
    x121 += einsum(x6, (0, 1), (0, 1)) * 1.0000000000000404
    x121 += einsum(x7, (0, 1), (0, 1)) * 0.5000000000000002
    x121 += einsum(x8, (0, 1), (0, 1))
    x121 += einsum(x9, (0, 1), (0, 1)) * 1.4999999999999998
    rdm2_f_abab_ooov += einsum(t1.bb, (0, 1), x121, (2, 3), (3, 0, 2, 1)) * -1.9999999999999194
    rdm2_f_abab_oovv += einsum(x121, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.9999999999999194
    x122 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x122 += einsum(t1.bb, (0, 1), x113, (2, 3, 4, 5, 1, 6), (3, 4, 2, 5, 0, 6))
    x123 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x123 += einsum(t2.bbbb, (0, 1, 2, 3), x122, (1, 0, 4, 5, 6, 3), (4, 6, 5, 2))
    rdm2_f_bbbb_ooov = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_ooov += einsum(x123, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_bbbb_oovo = np.zeros((nocc[1], nocc[1], nvir[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_oovo += einsum(x123, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    x124 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x124 += einsum(l2.bbbb, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 3, 6, 0, 1), (2, 4, 5, 6))
    rdm2_f_bbbb_ooov += einsum(x124, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_bbbb_oovo += einsum(x124, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    x125 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x125 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 3, 4, 0), (1, 2, 3, 4))
    rdm2_f_bbbb_ooov += einsum(x125, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_bbbb_oovo += einsum(x125, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x126 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x126 += einsum(t1.bb, (0, 1), x87, (2, 3, 4, 1, 5, 6), (2, 3, 4, 0, 5, 6)) * -1.0
    x127 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x127 += einsum(t2.abab, (0, 1, 2, 3), x126, (4, 1, 5, 6, 0, 2), (4, 6, 5, 3)) * -1.0
    rdm2_f_bbbb_ooov += einsum(x127, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_bbbb_oovo += einsum(x127, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x128 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x128 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 0, 1), (3, 4, 5, 6))
    rdm2_f_bbbb_ooov += einsum(x128, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_bbbb_oovo += einsum(x128, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x129 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x129 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x113, (1, 2, 6, 7, 4, 5), (6, 7, 0, 3))
    x130 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x130 += einsum(t1.bb, (0, 1), x41, (2, 3, 4, 1), (2, 3, 0, 4))
    x131 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x131 += einsum(t1.bb, (0, 1), x130, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    x132 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x132 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x87, (6, 2, 7, 5, 1, 4), (6, 7, 0, 3)) * -1.0
    x133 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x133 += einsum(t2.abab, (0, 1, 2, 3), x24, (4, 5, 0, 2), (4, 1, 5, 3))
    x134 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x134 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x94, (6, 7, 0, 2, 3, 5), (6, 7, 1, 4))
    x135 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x135 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x135 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x136 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x136 += einsum(t2.bbbb, (0, 1, 2, 3), x135, (1, 4, 5, 3), (4, 5, 0, 2)) * 4.0
    x137 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x137 += einsum(x103, (0, 1, 2, 3), (0, 1, 2, 3))
    x137 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x138 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x138 += einsum(t2.abab, (0, 1, 2, 3), x137, (4, 5, 0, 2), (4, 5, 1, 3))
    x139 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x139 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x139 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -1.0
    x140 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x140 += einsum(x139, (0, 1, 2, 3), x42, (4, 0, 5, 2), (1, 4, 5, 3)) * 2.0
    x141 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x141 += einsum(delta.bb.oo, (0, 1), t1.bb, (2, 3), (0, 1, 2, 3))
    x141 += einsum(x129, (0, 1, 2, 3), (1, 0, 2, 3)) * -9.0
    x141 += einsum(x131, (0, 1, 2, 3), (1, 0, 2, 3)) * 6.0
    x141 += einsum(x132, (0, 1, 2, 3), (1, 0, 2, 3)) * -4.0
    x141 += einsum(x133, (0, 1, 2, 3), (1, 0, 2, 3)) * 2.0
    x141 += einsum(x134, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x141 += einsum(x136, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x141 += einsum(x138, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x141 += einsum(x140, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x141 += einsum(t1.bb, (0, 1), x119, (2, 3), (0, 2, 3, 1))
    rdm2_f_bbbb_ooov += einsum(x141, (0, 1, 2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ooov += einsum(x141, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    rdm2_f_bbbb_oovo += einsum(x141, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    rdm2_f_bbbb_oovo += einsum(x141, (0, 1, 2, 3), (2, 0, 3, 1))
    x142 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x142 += einsum(t2.bbbb, (0, 1, 2, 3), x117, (0, 1, 4, 3), (4, 2)) * -1.0
    x143 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x143 += einsum(t2.abab, (0, 1, 2, 3), x118, (1, 4, 0, 2), (4, 3))
    x144 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x144 += einsum(t1.bb, (0, 1), x119, (0, 2), (2, 1)) * 0.5
    x145 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x145 += einsum(x108, (0, 1), (0, 1)) * -1.0
    x145 += einsum(x109, (0, 1), (0, 1)) * -0.5
    x145 += einsum(x110, (0, 1), (0, 1)) * -1.5
    x145 += einsum(x111, (0, 1), (0, 1)) * -1.0
    x145 += einsum(x112, (0, 1), (0, 1)) * -0.5
    x145 += einsum(x114, (0, 1), (0, 1)) * 1.4999999999999394
    x145 += einsum(x115, (0, 1), (0, 1)) * 0.9999999999999597
    x145 += einsum(x116, (0, 1), (0, 1)) * 0.49999999999998007
    x145 += einsum(x142, (0, 1), (0, 1))
    x145 += einsum(x143, (0, 1), (0, 1))
    x145 += einsum(x144, (0, 1), (0, 1))
    rdm2_f_bbbb_ooov += einsum(delta.bb.oo, (0, 1), x145, (2, 3), (0, 2, 1, 3)) * -2.0
    rdm2_f_bbbb_ooov += einsum(delta.bb.oo, (0, 1), x145, (2, 3), (2, 0, 1, 3)) * 2.0
    rdm2_f_bbbb_oovo += einsum(delta.bb.oo, (0, 1), x145, (2, 3), (0, 2, 3, 1)) * 2.0
    rdm2_f_bbbb_oovo += einsum(delta.bb.oo, (0, 1), x145, (2, 3), (2, 0, 3, 1)) * -2.0
    rdm2_f_abab_oovv += einsum(t1.aa, (0, 1), x145, (2, 3), (0, 2, 1, 3)) * -2.0
    x146 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x146 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    rdm2_f_bbbb_vvov = np.zeros((nvir[1], nvir[1], nocc[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_vvov += einsum(x146, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_bbbb_vvvo = np.zeros((nvir[1], nvir[1], nvir[1], nocc[1]), dtype=np.float64)
    rdm2_f_bbbb_vvvo += einsum(x146, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    x147 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x147 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 5, 6, 0, 1), (6, 4, 5, 3))
    rdm2_f_bbbb_vvov += einsum(x147, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_bbbb_vvvo += einsum(x147, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    x148 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x148 += einsum(x146, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x148 += einsum(x147, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    rdm2_f_abab_ovvv += einsum(t2.abab, (0, 1, 2, 3), x148, (1, 4, 3, 5), (0, 4, 2, 5)) * -6.0
    x149 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x149 += einsum(t2.bbbb, (0, 1, 2, 3), x148, (4, 2, 3, 5), (4, 0, 1, 5)) * 6.0
    rdm2_f_bbbb_ooov += einsum(x149, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_bbbb_oovo += einsum(x149, (0, 1, 2, 3), (2, 1, 3, 0))
    x150 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x150 += einsum(x35, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333269
    x150 += einsum(x37, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333269
    x150 += einsum(x39, (0, 1, 2, 3), (0, 1, 3, 2))
    x150 += einsum(x38, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333336
    x151 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x151 += einsum(t1.bb, (0, 1), x150, (0, 2, 3, 4), (2, 3, 4, 1)) * 6.000000000000116
    rdm2_f_bbbb_ooov += einsum(x151, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    rdm2_f_bbbb_oovo += einsum(x151, (0, 1, 2, 3), (2, 1, 3, 0))
    x152 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x152 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x113, (6, 0, 2, 7, 3, 5), (6, 7, 1, 4))
    rdm2_f_abab_oovo += einsum(x152, (0, 1, 2, 3), (2, 1, 3, 0)) * -3.0
    x153 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x153 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x46, (6, 4, 0, 2, 7, 5), (6, 1, 7, 3)) * -1.0
    rdm2_f_abab_oovo += einsum(x153, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x154 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x154 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x94, (6, 7, 1, 2, 5, 4), (6, 7, 0, 3)) * -1.0
    rdm2_f_abab_oovo += einsum(x154, (0, 1, 2, 3), (2, 1, 3, 0)) * -3.0
    x155 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x155 += einsum(t2.aaaa, (0, 1, 2, 3), x97, (4, 5, 0, 1, 6, 3), (4, 5, 6, 2)) * -1.0
    rdm2_f_abab_oovo += einsum(x155, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x156 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x156 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 1, 0), (3, 5, 4, 6))
    rdm2_f_abab_oovo += einsum(x156, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x157 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x157 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x55, (6, 2, 3, 5, 1, 7), (6, 0, 7, 4))
    rdm2_f_abab_oovo += einsum(x157, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x158 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x158 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x87, (6, 1, 7, 4, 2, 5), (6, 7, 0, 3)) * -1.0
    rdm2_f_abab_oovo += einsum(x158, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x159 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x159 += einsum(t2.abab, (0, 1, 2, 3), x90, (4, 1, 5, 3, 0, 6), (4, 5, 6, 2)) * -1.0
    rdm2_f_abab_oovo += einsum(x159, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x160 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x160 += einsum(l1.bb, (0, 1), t2.abab, (2, 3, 4, 0), (1, 3, 2, 4))
    rdm2_f_abab_oovo += einsum(x160, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x161 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x161 += einsum(l2.bbbb, (0, 1, 2, 3), t3.babbab, (4, 5, 3, 0, 6, 1), (2, 4, 5, 6))
    rdm2_f_abab_oovo += einsum(x161, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x162 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x162 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 5, 3, 6, 0, 1), (6, 4, 5, 2))
    rdm2_f_abab_vvvo = np.zeros((nvir[0], nvir[1], nvir[0], nocc[1]), dtype=np.float64)
    rdm2_f_abab_vvvo += einsum(x162, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x163 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x163 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (4, 5, 3, 0, 6, 1), (6, 5, 4, 2))
    rdm2_f_abab_vvvo += einsum(x163, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x164 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x164 += einsum(x162, (0, 1, 2, 3), (0, 1, 2, 3))
    x164 += einsum(x163, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_oovo += einsum(t2.abab, (0, 1, 2, 3), x164, (4, 3, 2, 5), (0, 1, 5, 4)) * 2.0
    rdm2_f_abab_ovvv += einsum(t2.abab, (0, 1, 2, 3), x164, (1, 4, 2, 5), (0, 4, 5, 3)) * -2.0
    rdm2_f_abab_vovv += einsum(t2.bbbb, (0, 1, 2, 3), x164, (1, 3, 4, 5), (4, 0, 5, 2)) * 4.0
    x165 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x165 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.3333333333333333
    x165 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3))
    x165 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.3333333333333333
    rdm2_f_abab_oovo += einsum(t2.abab, (0, 1, 2, 3), x165, (1, 4, 5, 3), (0, 5, 2, 4)) * -6.0
    rdm2_f_abab_oovv += einsum(x165, (0, 1, 2, 3), t3.babbab, (0, 4, 1, 5, 6, 3), (4, 2, 6, 5)) * 6.0
    x166 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x166 += einsum(x18, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.4999999999999899
    x166 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3))
    x166 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3))
    x166 += einsum(t1.bb, (0, 1), x105, (2, 1, 3, 4), (2, 0, 3, 4)) * 0.4999999999999899
    x166 += einsum(t1.aa, (0, 1), x25, (2, 3, 4, 1), (2, 3, 4, 0)) * 0.9999999999999798
    rdm2_f_abab_oovo += einsum(t1.aa, (0, 1), x166, (2, 3, 0, 4), (4, 3, 1, 2)) * 2.0000000000000404
    x167 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x167 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3)) * -0.33333333333333337
    x167 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.33333333333333337
    x167 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x168 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x168 += einsum(x15, (0, 1), (0, 1))
    x168 += einsum(x5, (0, 1), (0, 1))
    x168 += einsum(x6, (0, 1), (0, 1)) * 2.0
    x168 += einsum(x7, (0, 1), (0, 1)) * 0.99999999999996
    x168 += einsum(x8, (0, 1), (0, 1)) * 1.9999999999999192
    x168 += einsum(x9, (0, 1), (0, 1)) * 2.9999999999998783
    x169 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x169 += einsum(t1.aa, (0, 1), (0, 1)) * -1.00000000000004
    x169 += einsum(x67, (0, 1), (0, 1)) * -1.00000000000004
    x169 += einsum(x68, (0, 1), (0, 1)) * -2.00000000000008
    x169 += einsum(x69, (0, 1), (0, 1)) * -1.00000000000004
    x169 += einsum(x70, (0, 1), (0, 1)) * -2.00000000000008
    x169 += einsum(x71, (0, 1), (0, 1)) * -3.0000000000001195
    x169 += einsum(x72, (0, 1), (0, 1))
    x169 += einsum(x73, (0, 1), (0, 1)) * 1.9999999999999991
    x169 += einsum(x74, (0, 1), (0, 1)) * 2.9999999999999982
    x169 += einsum(t2.abab, (0, 1, 2, 3), x22, (1, 3, 0, 4), (4, 2)) * 2.00000000000008
    x169 += einsum(t2.aaaa, (0, 1, 2, 3), x167, (0, 1, 4, 3), (4, 2)) * -6.000000000000239
    x169 += einsum(t1.aa, (0, 1), x168, (0, 2), (2, 1)) * 1.00000000000004
    rdm2_f_abab_oovo += einsum(delta.bb.oo, (0, 1), x169, (2, 3), (2, 0, 3, 1)) * -0.9999999999999601
    x170 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x170 += einsum(x15, (0, 1), t2.aaaa, (2, 0, 3, 4), (1, 2, 3, 4))
    x171 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x171 += einsum(x61, (0, 1, 2, 3), t3.abaaba, (4, 0, 2, 5, 1, 6), (4, 3, 5, 6)) * -2.0
    x172 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x172 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x172 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3))
    x173 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x173 += einsum(x172, (0, 1, 2, 3), t3.aaaaaa, (4, 0, 1, 5, 6, 3), (2, 4, 5, 6)) * -6.0
    x174 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x174 += einsum(t1.aa, (0, 1), x13, (2, 3, 4, 1), (0, 2, 3, 4)) * 0.3333333333333333
    x175 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x175 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x175 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    x176 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x176 += einsum(x174, (0, 1, 2, 3), x175, (1, 2, 4, 5), (0, 3, 4, 5)) * 6.0
    x177 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x177 += einsum(x5, (0, 1), (0, 1)) * 0.5000000000000203
    x177 += einsum(x6, (0, 1), (0, 1)) * 1.0000000000000406
    x177 += einsum(x8, (0, 1), (0, 1))
    x178 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x178 += einsum(x177, (0, 1), t2.aaaa, (2, 0, 3, 4), (1, 2, 3, 4)) * -3.999999999999838
    x179 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x179 += einsum(x170, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x179 += einsum(x171, (0, 1, 2, 3), (1, 0, 3, 2))
    x179 += einsum(x173, (0, 1, 2, 3), (0, 1, 2, 3))
    x179 += einsum(x176, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x179 += einsum(x178, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x179, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_aaaa_oovv += einsum(x179, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x180 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x180 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_aaaa_ovov += einsum(x180, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    rdm2_f_aaaa_ovvo += einsum(x180, (0, 1, 2, 3), (1, 2, 3, 0)) * 4.0
    rdm2_f_aaaa_voov += einsum(x180, (0, 1, 2, 3), (2, 1, 0, 3)) * 4.0
    rdm2_f_aaaa_vovo += einsum(x180, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x181 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x181 += einsum(t2.aaaa, (0, 1, 2, 3), x180, (1, 4, 3, 5), (0, 4, 2, 5))
    x182 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x182 += einsum(x164, (0, 1, 2, 3), t3.abaaba, (4, 0, 5, 6, 1, 2), (4, 5, 3, 6)) * -4.0
    x183 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x183 += einsum(x81, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 0, 6, 1, 2), (4, 5, 6, 3)) * -6.0
    x184 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x184 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 4, 1), (0, 4))
    x185 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x185 += einsum(l2.aaaa, (0, 1, 2, 3), t2.aaaa, (2, 3, 4, 1), (0, 4))
    x186 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x186 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 0, 6, 2), (1, 6))
    x187 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x187 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 6, 1, 2), (0, 6))
    x188 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x188 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (3, 4, 5, 6, 1, 2), (0, 6))
    x189 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x189 += einsum(x184, (0, 1), (0, 1))
    x189 += einsum(x185, (0, 1), (0, 1)) * 2.0
    x189 += einsum(x186, (0, 1), (0, 1)) * 0.9999999999999597
    x189 += einsum(x187, (0, 1), (0, 1)) * 1.999999999999919
    x189 += einsum(x188, (0, 1), (0, 1)) * 2.999999999999883
    x190 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x190 += einsum(x189, (0, 1), t2.aaaa, (2, 3, 4, 0), (2, 3, 1, 4)) * -2.0
    x191 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x191 += einsum(t2.aaaa, (0, 1, 2, 3), x81, (4, 2, 3, 5), (0, 1, 4, 5))
    x192 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x192 += einsum(x49, (0, 1, 2, 3), (0, 2, 1, 3))
    x192 += einsum(x53, (0, 1, 2, 3), (0, 2, 1, 3))
    x192 += einsum(x45, (0, 1, 2, 3), (0, 2, 1, 3)) * 3.0
    x192 += einsum(x48, (0, 1, 2, 3), (0, 2, 1, 3))
    x192 += einsum(x52, (0, 1, 2, 3), (0, 2, 1, 3)) * 3.0
    x192 += einsum(x191, (0, 1, 2, 3), (2, 1, 0, 3))
    x193 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x193 += einsum(t1.aa, (0, 1), x192, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    x194 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x194 += einsum(x181, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x194 += einsum(x182, (0, 1, 2, 3), (1, 0, 2, 3))
    x194 += einsum(x183, (0, 1, 2, 3), (0, 1, 3, 2))
    x194 += einsum(x190, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x194 += einsum(x193, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_aaaa_oovv += einsum(x194, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_aaaa_oovv += einsum(x194, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x195 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x195 += einsum(t2.abab, (0, 1, 2, 3), x55, (4, 1, 5, 3, 0, 6), (4, 5, 6, 2))
    rdm2_f_abab_ovvo += einsum(x195, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x196 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x196 += einsum(t2.abab, (0, 1, 2, 3), x195, (1, 3, 4, 5), (4, 0, 2, 5))
    x197 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x197 += einsum(l2.abab, (0, 1, 2, 3), t2.aaaa, (4, 2, 5, 0), (3, 1, 4, 5))
    rdm2_f_abab_ovvo += einsum(x197, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x198 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x198 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.babbab, (4, 6, 5, 1, 7, 2), (3, 0, 6, 7))
    rdm2_f_abab_ovvo += einsum(x198, (0, 1, 2, 3), (2, 1, 3, 0)) * 3.0
    x199 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x199 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 5, 4, 7, 2, 1), (3, 0, 6, 7))
    rdm2_f_abab_ovvo += einsum(x199, (0, 1, 2, 3), (2, 1, 3, 0)) * 4.0
    x200 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x200 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 3, 5, 7, 0, 2), (4, 1, 6, 7))
    rdm2_f_abab_ovvo += einsum(x200, (0, 1, 2, 3), (2, 1, 3, 0)) * 3.0
    x201 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x201 += einsum(x197, (0, 1, 2, 3), (0, 1, 2, 3))
    x201 += einsum(x198, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x201 += einsum(x199, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x201 += einsum(x200, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x202 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x202 += einsum(t2.abab, (0, 1, 2, 3), x201, (1, 3, 4, 5), (4, 0, 5, 2)) * 2.0
    x203 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x203 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7))
    rdm2_f_aaaa_ovov += einsum(x203, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_aaaa_ovvo += einsum(x203, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_aaaa_voov += einsum(x203, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_aaaa_vovo += einsum(x203, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x204 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x204 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    rdm2_f_aaaa_ovov += einsum(x204, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    rdm2_f_aaaa_ovvo += einsum(x204, (0, 1, 2, 3), (1, 2, 3, 0)) * 4.0
    rdm2_f_aaaa_voov += einsum(x204, (0, 1, 2, 3), (2, 1, 0, 3)) * 4.0
    rdm2_f_aaaa_vovo += einsum(x204, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x205 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x205 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.aaaaaa, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    rdm2_f_aaaa_ovov += einsum(x205, (0, 1, 2, 3), (1, 2, 0, 3)) * -9.0
    rdm2_f_aaaa_ovvo += einsum(x205, (0, 1, 2, 3), (1, 2, 3, 0)) * 9.0
    rdm2_f_aaaa_voov += einsum(x205, (0, 1, 2, 3), (2, 1, 0, 3)) * 9.0
    rdm2_f_aaaa_vovo += einsum(x205, (0, 1, 2, 3), (2, 1, 3, 0)) * -9.0
    x206 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x206 += einsum(x203, (0, 1, 2, 3), (0, 1, 2, 3))
    x206 += einsum(x204, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x206 += einsum(x205, (0, 1, 2, 3), (0, 1, 2, 3)) * 9.0
    x207 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x207 += einsum(t2.aaaa, (0, 1, 2, 3), x206, (1, 4, 3, 5), (4, 0, 5, 2)) * 2.0
    x208 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x208 += einsum(t2.abab, (0, 1, 2, 3), x46, (1, 3, 4, 0, 5, 6), (4, 5, 6, 2))
    rdm2_f_aaaa_ovov += einsum(x208, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_aaaa_ovvo += einsum(x208, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    rdm2_f_aaaa_voov += einsum(x208, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_aaaa_vovo += einsum(x208, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x209 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x209 += einsum(t2.aaaa, (0, 1, 2, 3), x50, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2)) * -1.0
    rdm2_f_aaaa_ovov += einsum(x209, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_aaaa_ovvo += einsum(x209, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    rdm2_f_aaaa_voov += einsum(x209, (0, 1, 2, 3), (2, 1, 0, 3)) * -6.0
    rdm2_f_aaaa_vovo += einsum(x209, (0, 1, 2, 3), (2, 1, 3, 0)) * 6.0
    x210 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x210 += einsum(t1.aa, (0, 1), x13, (2, 0, 3, 4), (2, 3, 1, 4))
    x211 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x211 += einsum(x208, (0, 1, 2, 3), (0, 1, 2, 3))
    x211 += einsum(x209, (0, 1, 2, 3), (0, 1, 2, 3)) * 3.0
    x211 += einsum(x210, (0, 1, 2, 3), (0, 1, 3, 2))
    x212 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x212 += einsum(t2.aaaa, (0, 1, 2, 3), x211, (1, 4, 3, 5), (4, 0, 5, 2)) * 4.0
    x213 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x213 += einsum(t2.aaaa, (0, 1, 2, 3), x46, (4, 5, 0, 1, 6, 3), (4, 5, 6, 2)) * -1.0
    rdm2_f_abab_ovvo += einsum(x213, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x214 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x214 += einsum(t1.aa, (0, 1), x21, (2, 3, 0, 4), (2, 3, 4, 1))
    x215 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x215 += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3))
    x215 += einsum(x214, (0, 1, 2, 3), (0, 1, 2, 3))
    x216 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x216 += einsum(t2.abab, (0, 1, 2, 3), x215, (1, 3, 4, 5), (4, 0, 5, 2)) * 2.0
    x217 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x217 += einsum(t2.abab, (0, 1, 2, 3), x19, (1, 3, 4, 5), (4, 5, 0, 2))
    x218 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x218 += einsum(t2.aaaa, (0, 1, 2, 3), x3, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x219 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x219 += einsum(x217, (0, 1, 2, 3), (0, 1, 2, 3))
    x219 += einsum(x218, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x219 += einsum(x56, (0, 1, 2, 3), (0, 1, 2, 3))
    x219 += einsum(x54, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x219 += einsum(x57, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x219 += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3)) * 9.0
    x220 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x220 += einsum(t1.aa, (0, 1), x219, (0, 2, 3, 4), (2, 3, 4, 1))
    x221 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x221 += einsum(x196, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x221 += einsum(x202, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x221 += einsum(x207, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x221 += einsum(x212, (0, 1, 2, 3), (0, 1, 2, 3))
    x221 += einsum(x216, (0, 1, 2, 3), (0, 1, 2, 3))
    x221 += einsum(x220, (0, 1, 2, 3), (0, 1, 3, 2))
    x221 += einsum(t1.aa, (0, 1), x78, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_oovv += einsum(x221, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x221, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_aaaa_oovv += einsum(x221, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_aaaa_oovv += einsum(x221, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x222 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x222 += einsum(x20, (0, 1, 2, 3), t3.abaaba, (4, 0, 2, 5, 1, 6), (3, 4, 5, 6))
    x223 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x223 += einsum(x12, (0, 1, 2, 3), t3.aaaaaa, (4, 0, 1, 5, 6, 3), (2, 4, 5, 6))
    x224 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x224 += einsum(x7, (0, 1), (0, 1))
    x224 += einsum(x9, (0, 1), (0, 1)) * 3.000000000000004
    x225 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x225 += einsum(x224, (0, 1), t2.aaaa, (2, 0, 3, 4), (1, 2, 3, 4)) * -1.9999999999999194
    x226 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x226 += einsum(x222, (0, 1, 2, 3), (0, 1, 3, 2)) * -4.0
    x226 += einsum(x223, (0, 1, 2, 3), (0, 1, 2, 3)) * -18.0
    x226 += einsum(x225, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x226, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x226, (0, 1, 2, 3), (1, 0, 3, 2))
    x227 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x227 += einsum(l2.bbbb, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 0, 4, 5))
    rdm2_f_abab_ovvo += einsum(x227, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x228 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x228 += einsum(t2.abab, (0, 1, 2, 3), x227, (1, 3, 4, 5), (4, 0, 5, 2))
    x229 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x229 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    x229 += einsum(x228, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    rdm2_f_aaaa_oovv += einsum(x229, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_oovv += einsum(x229, (0, 1, 2, 3), (0, 1, 2, 3))
    x230 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x230 += einsum(t2.aaaa, (0, 1, 2, 3), l3.abaaba, (2, 4, 3, 5, 6, 7), (6, 4, 5, 7, 0, 1))
    x230 += einsum(x47, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * 1.0000000000000606
    rdm2_f_aaaa_oovv += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x230, (1, 4, 0, 2, 6, 7), (6, 7, 3, 5)) * 1.9999999999999194
    x231 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x231 += einsum(t2.aaaa, (0, 1, 2, 3), l3.aaaaaa, (4, 2, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x231 += einsum(x51, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0000000000000584
    rdm2_f_aaaa_oovv += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x231, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4)) * 5.999999999999766
    x232 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x232 += einsum(x2, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0000000000000404
    x232 += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.0000000000000404
    x232 += einsum(x1, (0, 1, 2, 3), (0, 1, 3, 2))
    x232 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2)) * 3.000000000000004
    rdm2_f_aaaa_oovv += einsum(t2.aaaa, (0, 1, 2, 3), x232, (0, 1, 4, 5), (5, 4, 2, 3)) * 1.9999999999999194
    x233 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x233 += einsum(x2, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.9999999999999798
    x233 += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.9999999999999798
    x233 += einsum(x1, (0, 1, 2, 3), (0, 1, 3, 2))
    x233 += einsum(x0, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.999999999999998
    x234 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x234 += einsum(t1.aa, (0, 1), x233, (0, 2, 3, 4), (2, 4, 3, 1)) * -1.0
    rdm2_f_aaaa_oovv += einsum(t1.aa, (0, 1), x234, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0000000000000404
    x235 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x235 += einsum(t2.abab, (0, 1, 2, 3), l3.abaaba, (4, 3, 2, 5, 6, 7), (6, 1, 5, 7, 0, 4))
    x235 += einsum(x97, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0000000000000606
    rdm2_f_abab_oovv += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x235, (1, 6, 0, 2, 7, 5), (7, 6, 3, 4)) * -1.9999999999999194
    x236 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x236 += einsum(t2.abab, (0, 1, 2, 3), l3.babbab, (4, 2, 3, 5, 6, 7), (5, 7, 1, 4, 6, 0))
    x236 += einsum(x90, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 1.0000000000000606
    rdm2_f_abab_oovv += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x236, (0, 2, 6, 5, 1, 7), (7, 6, 4, 3)) * -1.9999999999999194
    x237 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x237 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 3, 5))
    x237 += einsum(t1.aa, (0, 1), t2.abab, (2, 3, 4, 5), (3, 5, 0, 2, 4, 1)) * -0.5
    rdm2_f_abab_oovv += einsum(x101, (0, 1, 2, 3), x237, (4, 0, 2, 5, 3, 6), (5, 4, 6, 1)) * -4.0
    x238 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x238 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), (0, 2, 3, 5, 1, 4))
    x238 += einsum(t1.bb, (0, 1), t2.abab, (2, 3, 4, 5), (0, 3, 5, 1, 2, 4)) * -0.5
    rdm2_f_abab_oovv += einsum(x164, (0, 1, 2, 3), x238, (0, 4, 1, 5, 6, 2), (6, 4, 3, 5)) * -4.0
    x239 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x239 += einsum(x146, (0, 1, 2, 3), (0, 2, 1, 3)) * -3.0
    x239 += einsum(x147, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_abab_oovv += einsum(x239, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 1, 6, 2), (5, 4, 6, 3)) * 2.0
    x240 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x240 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_bbbb_ovov += einsum(x240, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    rdm2_f_bbbb_ovvo += einsum(x240, (0, 1, 2, 3), (1, 2, 3, 0)) * 4.0
    rdm2_f_bbbb_voov += einsum(x240, (0, 1, 2, 3), (2, 1, 0, 3)) * 4.0
    rdm2_f_bbbb_vovo += einsum(x240, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x241 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x241 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 0, 5), (3, 4, 1, 5))
    rdm2_f_bbbb_ovov += einsum(x241, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_bbbb_ovvo += einsum(x241, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_bbbb_voov += einsum(x241, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_bbbb_vovo += einsum(x241, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x242 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x242 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    rdm2_f_bbbb_ovov += einsum(x242, (0, 1, 2, 3), (1, 2, 0, 3)) * -9.0
    rdm2_f_bbbb_ovvo += einsum(x242, (0, 1, 2, 3), (1, 2, 3, 0)) * 9.0
    rdm2_f_bbbb_voov += einsum(x242, (0, 1, 2, 3), (2, 1, 0, 3)) * 9.0
    rdm2_f_bbbb_vovo += einsum(x242, (0, 1, 2, 3), (2, 1, 3, 0)) * -9.0
    x243 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x243 += einsum(t2.bbbb, (0, 1, 2, 3), x113, (4, 0, 1, 5, 6, 3), (4, 5, 6, 2)) * -1.0
    rdm2_f_bbbb_ovov += einsum(x243, (0, 1, 2, 3), (1, 2, 0, 3)) * 6.0
    rdm2_f_bbbb_ovvo += einsum(x243, (0, 1, 2, 3), (1, 2, 3, 0)) * -6.0
    rdm2_f_bbbb_voov += einsum(x243, (0, 1, 2, 3), (2, 1, 0, 3)) * -6.0
    rdm2_f_bbbb_vovo += einsum(x243, (0, 1, 2, 3), (2, 1, 3, 0)) * 6.0
    x244 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x244 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 7, 1, 2), (3, 6, 0, 7))
    rdm2_f_bbbb_ovov += einsum(x244, (0, 1, 2, 3), (1, 2, 0, 3)) * -4.0
    rdm2_f_bbbb_ovvo += einsum(x244, (0, 1, 2, 3), (1, 2, 3, 0)) * 4.0
    rdm2_f_bbbb_voov += einsum(x244, (0, 1, 2, 3), (2, 1, 0, 3)) * 4.0
    rdm2_f_bbbb_vovo += einsum(x244, (0, 1, 2, 3), (2, 1, 3, 0)) * -4.0
    x245 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x245 += einsum(t2.abab, (0, 1, 2, 3), x87, (4, 1, 5, 6, 0, 2), (4, 5, 6, 3))
    rdm2_f_bbbb_ovov += einsum(x245, (0, 1, 2, 3), (1, 2, 0, 3)) * 2.0
    rdm2_f_bbbb_ovvo += einsum(x245, (0, 1, 2, 3), (1, 2, 3, 0)) * -2.0
    rdm2_f_bbbb_voov += einsum(x245, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_bbbb_vovo += einsum(x245, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    x246 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x246 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 0, 7, 2), (4, 6, 1, 7))
    rdm2_f_bbbb_ovov += einsum(x246, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_bbbb_ovvo += einsum(x246, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_bbbb_voov += einsum(x246, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_bbbb_vovo += einsum(x246, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x247 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x247 += einsum(x240, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x247 += einsum(x241, (0, 1, 2, 3), (0, 1, 2, 3))
    x247 += einsum(x242, (0, 1, 2, 3), (0, 1, 2, 3)) * 9.0
    x247 += einsum(x243, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x247 += einsum(x244, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x247 += einsum(x245, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x247 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3))
    x247 += einsum(t1.bb, (0, 1), x43, (2, 0, 3, 4), (2, 3, 4, 1)) * -6.0
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x247, (1, 4, 3, 5), (0, 4, 2, 5))
    x248 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x248 += einsum(l2.abab, (0, 1, 2, 3), t2.bbbb, (4, 3, 5, 1), (4, 5, 2, 0))
    rdm2_f_abab_voov += einsum(x248, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x249 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x249 += einsum(l2.aaaa, (0, 1, 2, 3), t2.abab, (3, 4, 1, 5), (4, 5, 2, 0))
    rdm2_f_abab_voov += einsum(x249, (0, 1, 2, 3), (3, 0, 2, 1)) * 2.0
    x250 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x250 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (6, 3, 5, 7, 0, 2), (6, 7, 4, 1))
    rdm2_f_abab_voov += einsum(x250, (0, 1, 2, 3), (3, 0, 2, 1)) * 3.0
    x251 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x251 += einsum(t2.bbbb, (0, 1, 2, 3), x87, (0, 1, 4, 3, 5, 6), (4, 2, 5, 6)) * -1.0
    rdm2_f_abab_voov += einsum(x251, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x252 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x252 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 5, 4, 7, 2, 1), (6, 7, 3, 0))
    rdm2_f_abab_voov += einsum(x252, (0, 1, 2, 3), (3, 0, 2, 1)) * 4.0
    x253 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x253 += einsum(t2.abab, (0, 1, 2, 3), x94, (1, 4, 5, 0, 6, 2), (4, 3, 5, 6))
    rdm2_f_abab_voov += einsum(x253, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x254 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x254 += einsum(l3.aaaaaa, (0, 1, 2, 3, 4, 5), t3.abaaba, (4, 6, 5, 1, 7, 2), (6, 7, 3, 0))
    rdm2_f_abab_voov += einsum(x254, (0, 1, 2, 3), (3, 0, 2, 1)) * 3.0
    x255 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x255 += einsum(x248, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x255 += einsum(x249, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x255 += einsum(x250, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.75
    x255 += einsum(x251, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x255 += einsum(x252, (0, 1, 2, 3), (0, 1, 2, 3))
    x255 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x255 += einsum(x254, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.75
    x255 += einsum(t1.bb, (0, 1), x25, (0, 2, 3, 4), (2, 1, 3, 4)) * -0.5
    rdm2_f_abab_oovv += einsum(t2.aaaa, (0, 1, 2, 3), x255, (4, 5, 1, 3), (0, 4, 2, 5)) * 8.0
    x256 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x256 += einsum(x20, (0, 1, 2, 3), (0, 1, 2, 3))
    x256 += einsum(x21, (0, 1, 2, 3), (0, 1, 2, 3))
    x257 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x257 += einsum(x198, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x257 += einsum(x199, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.3333333333333333
    x257 += einsum(x195, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x257 += einsum(x200, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x257 += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x257 += einsum(t1.aa, (0, 1), x256, (2, 3, 0, 4), (2, 3, 4, 1)) * 0.6666666666666666
    rdm2_f_abab_oovv += einsum(t2.bbbb, (0, 1, 2, 3), x257, (1, 3, 4, 5), (4, 0, 5, 2)) * -6.0
    x258 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x258 += einsum(x203, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.25
    x258 += einsum(x204, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x258 += einsum(x208, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x258 += einsum(x205, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.25
    x258 += einsum(x209, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x258 += einsum(t1.aa, (0, 1), x13, (2, 0, 3, 4), (2, 3, 4, 1)) * 0.5
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x258, (0, 4, 2, 5), (4, 1, 5, 3)) * -4.0
    x259 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x259 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 0, 5), (1, 5, 2, 4))
    rdm2_f_abab_ovov += einsum(x259, (0, 1, 2, 3), (3, 0, 2, 1)) * -1.0
    x260 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x260 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 6, 5, 7, 1, 2), (0, 7, 4, 6))
    rdm2_f_abab_ovov += einsum(x260, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x261 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x261 += einsum(t2.bbbb, (0, 1, 2, 3), x55, (0, 1, 4, 3, 5, 6), (4, 2, 5, 6))
    rdm2_f_abab_ovov += einsum(x261, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x262 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x262 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (6, 4, 5, 0, 7, 2), (1, 7, 3, 6))
    rdm2_f_abab_ovov += einsum(x262, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x263 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x263 += einsum(t2.abab, (0, 1, 2, 3), x46, (1, 4, 5, 0, 6, 2), (4, 3, 5, 6)) * -1.0
    rdm2_f_abab_ovov += einsum(x263, (0, 1, 2, 3), (3, 0, 2, 1)) * -2.0
    x264 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x264 += einsum(x259, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x264 += einsum(x260, (0, 1, 2, 3), (0, 1, 2, 3))
    x264 += einsum(x261, (0, 1, 2, 3), (0, 1, 2, 3))
    x264 += einsum(x262, (0, 1, 2, 3), (0, 1, 2, 3))
    x264 += einsum(x263, (0, 1, 2, 3), (0, 1, 2, 3))
    x264 += einsum(t1.bb, (0, 1), x256, (0, 2, 3, 4), (2, 1, 3, 4))
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x264, (3, 4, 0, 5), (5, 1, 2, 4)) * 2.0
    x265 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x265 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (6, 4, 5, 0, 7, 2), (3, 6, 1, 7))
    rdm2_f_abab_vovo += einsum(x265, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x266 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x266 += einsum(t2.abab, (0, 1, 2, 3), x87, (4, 1, 5, 3, 0, 6), (4, 5, 6, 2)) * -1.0
    rdm2_f_abab_vovo += einsum(x266, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x267 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x267 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 6, 5, 7, 1, 2), (4, 6, 0, 7))
    rdm2_f_abab_vovo += einsum(x267, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x268 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x268 += einsum(t2.aaaa, (0, 1, 2, 3), x94, (4, 5, 0, 1, 6, 3), (4, 5, 6, 2))
    rdm2_f_abab_vovo += einsum(x268, (0, 1, 2, 3), (2, 1, 3, 0)) * -2.0
    x269 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x269 += einsum(x265, (0, 1, 2, 3), (0, 1, 2, 3))
    x269 += einsum(x266, (0, 1, 2, 3), (0, 1, 2, 3))
    x269 += einsum(x267, (0, 1, 2, 3), (0, 1, 2, 3))
    x269 += einsum(x268, (0, 1, 2, 3), (0, 1, 2, 3))
    x269 += einsum(t1.aa, (0, 1), x25, (2, 3, 0, 4), (2, 3, 4, 1))
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x269, (1, 4, 2, 5), (0, 4, 5, 3)) * 2.0
    x270 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x270 += einsum(x18, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5000000000000202
    x270 += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3))
    x270 += einsum(x16, (0, 1, 2, 3), (0, 1, 2, 3))
    x270 += einsum(t1.bb, (0, 1), x105, (2, 1, 3, 4), (2, 0, 3, 4)) * 0.5000000000000202
    x270 += einsum(t1.aa, (0, 1), x25, (2, 3, 4, 1), (2, 3, 4, 0)) * 1.0000000000000404
    rdm2_f_abab_oovv += einsum(t2.abab, (0, 1, 2, 3), x270, (1, 4, 0, 5), (5, 4, 2, 3)) * 1.9999999999999194
    x271 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x271 += einsum(x160, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x271 += einsum(x161, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x271 += einsum(t2.abab, (0, 1, 2, 3), x36, (4, 1, 5, 3), (4, 5, 0, 2)) * 2.0
    x271 += einsum(x156, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x271 += einsum(t2.abab, (0, 1, 2, 3), x19, (4, 3, 0, 5), (4, 1, 5, 2))
    x271 += einsum(t2.aaaa, (0, 1, 2, 3), x103, (4, 5, 1, 3), (4, 5, 0, 2)) * -2.0
    x271 += einsum(x152, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x271 += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x271 += einsum(x158, (0, 1, 2, 3), (0, 1, 2, 3)) * -4.0
    x271 += einsum(x159, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x271 += einsum(x153, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x271 += einsum(x154, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x271 += einsum(x155, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x271 += einsum(t1.aa, (0, 1), x107, (2, 3, 0, 4), (2, 3, 4, 1))
    rdm2_f_abab_oovv += einsum(t1.bb, (0, 1), x271, (0, 2, 3, 4), (3, 2, 4, 1))
    x272 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x272 += einsum(x184, (0, 1), (0, 1)) * 0.5000000000000202
    x272 += einsum(x185, (0, 1), (0, 1)) * 1.0000000000000404
    x272 += einsum(x186, (0, 1), (0, 1)) * 0.5000000000000002
    x272 += einsum(x187, (0, 1), (0, 1))
    x272 += einsum(x188, (0, 1), (0, 1)) * 1.4999999999999998
    rdm2_f_abab_oovv += einsum(x272, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.9999999999999194
    x273 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x273 += einsum(l2.bbbb, (0, 1, 2, 3), t2.bbbb, (2, 3, 4, 1), (0, 4))
    x274 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x274 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 3, 0, 4), (1, 4))
    x275 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x275 += einsum(l3.bbbbbb, (0, 1, 2, 3, 4, 5), t3.bbbbbb, (3, 4, 5, 6, 1, 2), (0, 6))
    x276 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x276 += einsum(l3.babbab, (0, 1, 2, 3, 4, 5), t3.babbab, (3, 4, 5, 6, 1, 2), (0, 6))
    x277 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x277 += einsum(l3.abaaba, (0, 1, 2, 3, 4, 5), t3.abaaba, (3, 4, 5, 0, 6, 2), (1, 6))
    x278 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x278 += einsum(x273, (0, 1), (0, 1)) * 2.00000000000008
    x278 += einsum(x274, (0, 1), (0, 1)) * 1.00000000000004
    x278 += einsum(x275, (0, 1), (0, 1)) * 2.9999999999999982
    x278 += einsum(x276, (0, 1), (0, 1)) * 1.9999999999999991
    x278 += einsum(x277, (0, 1), (0, 1))
    rdm2_f_abab_oovv += einsum(x278, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -0.9999999999999601
    x279 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x279 += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x279 += einsum(x86, (0, 1, 2, 3), (0, 1, 2, 3))
    x279 += einsum(t2.bbbb, (0, 1, 2, 3), x19, (1, 3, 4, 5), (0, 2, 4, 5))
    x279 += einsum(t2.abab, (0, 1, 2, 3), x103, (1, 4, 5, 2), (4, 3, 5, 0)) * -0.5
    x279 += einsum(x92, (0, 1, 2, 3), (0, 1, 2, 3))
    x279 += einsum(t2.abab, (0, 1, 2, 3), x3, (4, 0, 5, 2), (1, 3, 4, 5)) * -1.0
    x279 += einsum(x89, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    x279 += einsum(x88, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x279 += einsum(x91, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x279 += einsum(x96, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x279 += einsum(x95, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x279 += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x279 += einsum(x85, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.5
    rdm2_f_abab_oovv += einsum(t1.aa, (0, 1), x279, (2, 3, 0, 4), (4, 2, 1, 3)) * -2.0
    x280 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x280 += einsum(x28, (0, 1), (0, 1)) * 1.00000000000004
    x280 += einsum(x29, (0, 1), (0, 1)) * 2.00000000000008
    x280 += einsum(x30, (0, 1), (0, 1)) * 1.00000000000004
    x280 += einsum(x31, (0, 1), (0, 1)) * 2.9999999999999982
    x280 += einsum(x32, (0, 1), (0, 1)) * 1.9999999999999991
    x280 += einsum(x33, (0, 1), (0, 1))
    rdm2_f_abab_oovv += einsum(x280, (0, 1), t2.abab, (2, 0, 3, 4), (2, 1, 3, 4)) * -0.9999999999999601
    x281 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x281 += einsum(t1.aa, (0, 1), (0, 1)) * -1.0
    x281 += einsum(x67, (0, 1), (0, 1)) * -1.0
    x281 += einsum(x68, (0, 1), (0, 1)) * -2.0
    x281 += einsum(x69, (0, 1), (0, 1)) * -1.0
    x281 += einsum(x70, (0, 1), (0, 1)) * -2.0
    x281 += einsum(x71, (0, 1), (0, 1)) * -3.0
    x281 += einsum(x72, (0, 1), (0, 1)) * 0.9999999999999601
    x281 += einsum(x73, (0, 1), (0, 1)) * 1.9999999999999194
    x281 += einsum(x74, (0, 1), (0, 1)) * 2.9999999999998788
    x281 += einsum(x75, (0, 1), (0, 1))
    x281 += einsum(x76, (0, 1), (0, 1))
    x281 += einsum(x77, (0, 1), (0, 1))
    rdm2_f_abab_oovv += einsum(t1.bb, (0, 1), x281, (2, 3), (2, 0, 3, 1)) * -1.0
    x282 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x282 += einsum(x43, (0, 1, 2, 3), t3.bbbbbb, (4, 0, 1, 5, 6, 3), (4, 2, 5, 6)) * -18.0
    x283 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x283 += einsum(x25, (0, 1, 2, 3), t3.babbab, (4, 2, 0, 5, 3, 6), (4, 1, 5, 6)) * -4.0
    x284 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x284 += einsum(x31, (0, 1), (0, 1)) * 3.000000000000004
    x284 += einsum(x32, (0, 1), (0, 1)) * 1.9999999999999996
    x284 += einsum(x33, (0, 1), (0, 1))
    x285 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x285 += einsum(x284, (0, 1), t2.bbbb, (2, 0, 3, 4), (1, 2, 3, 4)) * -1.9999999999999194
    x286 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x286 += einsum(x282, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x286 += einsum(x283, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x286 += einsum(x285, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_bbbb_oovv += einsum(x286, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_bbbb_oovv += einsum(x286, (0, 1, 2, 3), (1, 0, 2, 3))
    x287 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x287 += einsum(t2.bbbb, (0, 1, 2, 3), x240, (1, 4, 3, 5), (4, 0, 5, 2))
    x288 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x288 += einsum(t2.abab, (0, 1, 2, 3), x249, (4, 5, 0, 2), (1, 4, 3, 5))
    x289 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x289 += einsum(x148, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 1, 2), (4, 5, 3, 6)) * -18.0
    x290 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x290 += einsum(x101, (0, 1, 2, 3), t3.babbab, (4, 2, 5, 6, 3, 0), (4, 5, 1, 6)) * -4.0
    x291 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x291 += einsum(x273, (0, 1), (0, 1))
    x291 += einsum(x274, (0, 1), (0, 1)) * 0.5
    x291 += einsum(x275, (0, 1), (0, 1)) * 1.4999999999999416
    x291 += einsum(x276, (0, 1), (0, 1)) * 0.9999999999999595
    x291 += einsum(x277, (0, 1), (0, 1)) * 0.49999999999997985
    x292 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x292 += einsum(x291, (0, 1), t2.bbbb, (2, 3, 4, 0), (2, 3, 1, 4)) * -4.0
    x293 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x293 += einsum(t2.bbbb, (0, 1, 2, 3), x148, (4, 2, 3, 5), (4, 0, 1, 5)) * 3.0
    x294 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x294 += einsum(x125, (0, 1, 2, 3), (0, 2, 1, 3))
    x294 += einsum(x124, (0, 1, 2, 3), (0, 2, 1, 3)) * 3.0
    x294 += einsum(x128, (0, 1, 2, 3), (0, 2, 1, 3))
    x294 += einsum(x123, (0, 1, 2, 3), (0, 2, 1, 3)) * 3.0
    x294 += einsum(x127, (0, 1, 2, 3), (0, 2, 1, 3))
    x294 += einsum(x293, (0, 1, 2, 3), (0, 2, 1, 3))
    x295 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x295 += einsum(t1.bb, (0, 1), x294, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    x296 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x296 += einsum(x287, (0, 1, 2, 3), (0, 1, 2, 3)) * 8.0
    x296 += einsum(x288, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x296 += einsum(x289, (0, 1, 2, 3), (0, 1, 2, 3))
    x296 += einsum(x290, (0, 1, 2, 3), (1, 0, 2, 3))
    x296 += einsum(x292, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x296 += einsum(x295, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_bbbb_oovv += einsum(x296, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_oovv += einsum(x296, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x297 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x297 += einsum(t2.bbbb, (0, 1, 2, 3), x245, (1, 4, 3, 5), (4, 0, 2, 5)) * -1.0
    x298 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x298 += einsum(t2.abab, (0, 1, 2, 3), x253, (4, 5, 0, 2), (4, 1, 3, 5))
    x299 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x299 += einsum(x241, (0, 1, 2, 3), (0, 1, 2, 3))
    x299 += einsum(x242, (0, 1, 2, 3), (0, 1, 2, 3)) * 9.0
    x299 += einsum(x244, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x299 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3))
    x300 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x300 += einsum(t2.bbbb, (0, 1, 2, 3), x299, (1, 4, 3, 5), (4, 0, 5, 2)) * 2.0
    x301 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x301 += einsum(x250, (0, 1, 2, 3), (0, 1, 2, 3))
    x301 += einsum(x252, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.3333333333333333
    x301 += einsum(x254, (0, 1, 2, 3), (0, 1, 2, 3))
    x302 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x302 += einsum(t2.abab, (0, 1, 2, 3), x301, (4, 5, 0, 2), (4, 1, 5, 3)) * 3.0
    x303 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x303 += einsum(t1.bb, (0, 1), x23, (0, 2, 3, 4), (2, 1, 3, 4))
    x304 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x304 += einsum(x251, (0, 1, 2, 3), (0, 1, 2, 3))
    x304 += einsum(x303, (0, 1, 2, 3), (0, 1, 2, 3))
    x305 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x305 += einsum(t2.abab, (0, 1, 2, 3), x304, (4, 5, 0, 2), (4, 1, 5, 3)) * 2.0
    x306 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x306 += einsum(t1.bb, (0, 1), x41, (0, 2, 3, 4), (2, 3, 4, 1)) * -1.0
    x307 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x307 += einsum(x243, (0, 1, 2, 3), (0, 1, 2, 3))
    x307 += einsum(x306, (0, 1, 2, 3), (0, 1, 2, 3))
    x308 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x308 += einsum(t2.bbbb, (0, 1, 2, 3), x307, (1, 4, 3, 5), (4, 0, 5, 2)) * 12.0
    x309 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x309 += einsum(t2.bbbb, (0, 1, 2, 3), x36, (4, 1, 5, 3), (4, 5, 0, 2)) * -1.0
    x310 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x310 += einsum(t2.abab, (0, 1, 2, 3), x103, (4, 5, 0, 2), (4, 5, 1, 3))
    x311 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x311 += einsum(t2.bbbb, (0, 1, 2, 3), x42, (4, 1, 5, 3), (4, 0, 5, 2))
    x312 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x312 += einsum(x309, (0, 1, 2, 3), (0, 1, 2, 3))
    x312 += einsum(x310, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x312 += einsum(x129, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.25
    x312 += einsum(x132, (0, 1, 2, 3), (0, 1, 2, 3))
    x312 += einsum(x311, (0, 1, 2, 3), (0, 1, 2, 3))
    x312 += einsum(x134, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x312 += einsum(x133, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x313 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x313 += einsum(t1.bb, (0, 1), x312, (0, 2, 3, 4), (2, 3, 4, 1)) * 4.0
    x314 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x314 += einsum(x297, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x314 += einsum(x298, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x314 += einsum(x300, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x314 += einsum(x302, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x314 += einsum(x305, (0, 1, 2, 3), (0, 1, 2, 3))
    x314 += einsum(x308, (0, 1, 2, 3), (0, 1, 2, 3))
    x314 += einsum(x313, (0, 1, 2, 3), (0, 1, 3, 2))
    x314 += einsum(t1.bb, (0, 1), x145, (2, 3), (0, 2, 1, 3)) * 2.0
    rdm2_f_bbbb_oovv += einsum(x314, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_bbbb_oovv += einsum(x314, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_bbbb_oovv += einsum(x314, (0, 1, 2, 3), (1, 0, 2, 3))
    rdm2_f_bbbb_oovv += einsum(x314, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x315 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x315 += einsum(x28, (0, 1), t2.bbbb, (2, 0, 3, 4), (1, 2, 3, 4))
    x316 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x316 += einsum(x36, (0, 1, 2, 3), t3.bbbbbb, (4, 0, 1, 5, 6, 3), (2, 4, 5, 6)) * -1.0
    x317 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x317 += einsum(x103, (0, 1, 2, 3), t3.babbab, (4, 2, 0, 5, 3, 6), (1, 4, 5, 6))
    x318 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x318 += einsum(t1.bb, (0, 1), x43, (2, 3, 4, 1), (0, 2, 3, 4)) * 3.0
    x319 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x319 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x319 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3))
    x320 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x320 += einsum(x318, (0, 1, 2, 3), x319, (1, 2, 4, 5), (0, 3, 4, 5)) * 2.0
    x321 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x321 += einsum(x29, (0, 1), (0, 1))
    x321 += einsum(x30, (0, 1), (0, 1)) * 0.5
    x322 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x322 += einsum(x321, (0, 1), t2.bbbb, (2, 0, 3, 4), (1, 2, 3, 4)) * -4.0
    x323 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x323 += einsum(x315, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x323 += einsum(x316, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    x323 += einsum(x317, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x323 += einsum(x320, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x323 += einsum(x322, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    rdm2_f_bbbb_oovv += einsum(x323, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_oovv += einsum(x323, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x324 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x324 += einsum(t2.bbbb, (0, 1, 2, 3), l3.babbab, (2, 4, 3, 5, 6, 7), (5, 7, 0, 1, 6, 4))
    x324 += einsum(x126, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0000000000000606
    rdm2_f_bbbb_oovv += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x324, (0, 2, 6, 7, 1, 4), (6, 7, 3, 5)) * 1.9999999999999194
    x325 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x325 += einsum(t2.bbbb, (0, 1, 2, 3), l3.bbbbbb, (4, 2, 3, 5, 6, 7), (5, 6, 7, 0, 1, 4))
    x325 += einsum(x122, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0000000000000584
    rdm2_f_bbbb_oovv += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x325, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4)) * 5.999999999999766
    x326 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x326 += einsum(x35, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0000000000000404
    x326 += einsum(x37, (0, 1, 2, 3), (0, 1, 3, 2)) * 1.0000000000000404
    x326 += einsum(x39, (0, 1, 2, 3), (0, 1, 3, 2)) * 3.000000000000004
    x326 += einsum(x38, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_bbbb_oovv += einsum(t2.bbbb, (0, 1, 2, 3), x326, (0, 1, 4, 5), (5, 4, 2, 3)) * 1.9999999999999194
    x327 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x327 += einsum(x35, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.3333333333333268
    x327 += einsum(x37, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333268
    x327 += einsum(x39, (0, 1, 2, 3), (0, 1, 3, 2))
    x327 += einsum(x38, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.3333333333333336
    x328 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x328 += einsum(t1.bb, (0, 1), x327, (0, 2, 3, 4), (2, 4, 3, 1)) * -2.999999999999998
    rdm2_f_bbbb_oovv += einsum(t1.bb, (0, 1), x328, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0000000000000404
    x329 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x329 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_aaaa_ovov += einsum(x329, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_aaaa_ovvo += einsum(x329, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_aaaa_voov += einsum(x329, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_aaaa_vovo += einsum(x329, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x330 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x330 += einsum(t1.aa, (0, 1), x59, (0, 2, 3, 4), (2, 3, 1, 4)) * 6.0
    rdm2_f_aaaa_ovov += einsum(x330, (0, 1, 2, 3), (1, 3, 0, 2)) * -1.0
    rdm2_f_aaaa_voov += einsum(x330, (0, 1, 2, 3), (3, 1, 0, 2))
    x331 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x331 += einsum(l1.aa, (0, 1), t1.aa, (1, 2), (0, 2))
    x332 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x332 += einsum(x331, (0, 1), (0, 1)) * 0.5000000000000202
    x332 += einsum(x184, (0, 1), (0, 1)) * 0.5000000000000202
    x332 += einsum(x185, (0, 1), (0, 1)) * 1.0000000000000404
    x332 += einsum(x186, (0, 1), (0, 1)) * 0.5000000000000002
    x332 += einsum(x187, (0, 1), (0, 1))
    x332 += einsum(x188, (0, 1), (0, 1)) * 1.4999999999999998
    rdm2_f_aaaa_ovov += einsum(delta.aa.oo, (0, 1), x332, (2, 3), (0, 2, 1, 3)) * 1.9999999999999194
    rdm2_f_aaaa_ovvo += einsum(delta.aa.oo, (0, 1), x332, (2, 3), (0, 2, 3, 1)) * -1.9999999999999194
    rdm2_f_aaaa_voov += einsum(delta.aa.oo, (0, 1), x332, (2, 3), (2, 0, 1, 3)) * -1.9999999999999194
    rdm2_f_aaaa_vovo += einsum(delta.aa.oo, (0, 1), x332, (2, 3), (2, 0, 3, 1)) * 1.9999999999999194
    x333 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x333 += einsum(l1.bb, (0, 1), t1.bb, (1, 2), (0, 2))
    x334 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x334 += einsum(x333, (0, 1), (0, 1)) * 0.3333333333333468
    x334 += einsum(x273, (0, 1), (0, 1)) * 0.6666666666666936
    x334 += einsum(x274, (0, 1), (0, 1)) * 0.3333333333333468
    x334 += einsum(x275, (0, 1), (0, 1))
    x334 += einsum(x276, (0, 1), (0, 1)) * 0.6666666666666667
    x334 += einsum(x277, (0, 1), (0, 1)) * 0.33333333333333354
    rdm2_f_abab_ovov += einsum(delta.aa.oo, (0, 1), x334, (2, 3), (0, 2, 1, 3)) * 2.9999999999998788
    x335 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x335 += einsum(t1.bb, (0, 1), x165, (0, 2, 3, 4), (2, 3, 4, 1)) * 6.0
    rdm2_f_bbbb_ovov += einsum(x335, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_bbbb_voov += einsum(x335, (0, 1, 2, 3), (2, 1, 0, 3))
    x336 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x336 += einsum(x333, (0, 1), (0, 1)) * 0.5000000000000202
    x336 += einsum(x273, (0, 1), (0, 1)) * 1.0000000000000404
    x336 += einsum(x274, (0, 1), (0, 1)) * 0.5000000000000202
    x336 += einsum(x275, (0, 1), (0, 1)) * 1.4999999999999998
    x336 += einsum(x276, (0, 1), (0, 1))
    x336 += einsum(x277, (0, 1), (0, 1)) * 0.5000000000000002
    rdm2_f_bbbb_ovov += einsum(delta.bb.oo, (0, 1), x336, (2, 3), (0, 2, 1, 3)) * 1.9999999999999194
    rdm2_f_bbbb_ovvo += einsum(delta.bb.oo, (0, 1), x336, (2, 3), (0, 2, 3, 1)) * -1.9999999999999194
    rdm2_f_bbbb_voov += einsum(delta.bb.oo, (0, 1), x336, (2, 3), (2, 0, 1, 3)) * -1.9999999999999194
    rdm2_f_bbbb_vovo += einsum(delta.bb.oo, (0, 1), x336, (2, 3), (2, 0, 3, 1)) * 1.9999999999999194
    x337 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x337 += einsum(t1.aa, (0, 1), x102, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_aaaa_ovvo += einsum(x337, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_aaaa_vovo += einsum(x337, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x338 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x338 += einsum(t1.bb, (0, 1), x117, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_bbbb_ovvo += einsum(x338, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_bbbb_vovo += einsum(x338, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x339 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x339 += einsum(l2.abab, (0, 1, 2, 3), t2.abab, (2, 4, 5, 1), (3, 4, 0, 5))
    rdm2_f_abab_vovo += einsum(x339, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x340 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x340 += einsum(x331, (0, 1), (0, 1)) * 1.00000000000004
    x340 += einsum(x184, (0, 1), (0, 1)) * 1.00000000000004
    x340 += einsum(x185, (0, 1), (0, 1)) * 2.00000000000008
    x340 += einsum(x186, (0, 1), (0, 1))
    x340 += einsum(x187, (0, 1), (0, 1)) * 1.9999999999999991
    x340 += einsum(x188, (0, 1), (0, 1)) * 2.9999999999999982
    rdm2_f_abab_vovo += einsum(delta.bb.oo, (0, 1), x340, (2, 3), (2, 0, 3, 1)) * 0.9999999999999601
    x341 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x341 += einsum(t3.aaaaaa, (0, 1, 2, 3, 4, 5), x50, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4)) * -1.0
    rdm2_f_aaaa_ovvv = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_ovvv += einsum(x341, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.000000000000116
    rdm2_f_aaaa_vovv = np.zeros((nvir[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    rdm2_f_aaaa_vovv += einsum(x341, (0, 1, 2, 3), (1, 0, 3, 2)) * 6.000000000000116
    x342 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x342 += einsum(l2.abab, (0, 1, 2, 3), t3.abaaba, (4, 3, 2, 5, 1, 6), (4, 0, 5, 6))
    rdm2_f_aaaa_ovvv += einsum(x342, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_aaaa_vovv += einsum(x342, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x343 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x343 += einsum(l1.aa, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_aaaa_ovvv += einsum(x343, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_aaaa_vovv += einsum(x343, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x344 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x344 += einsum(l2.aaaa, (0, 1, 2, 3), t3.aaaaaa, (4, 2, 3, 5, 6, 1), (4, 0, 5, 6))
    rdm2_f_aaaa_ovvv += einsum(x344, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    rdm2_f_aaaa_vovv += einsum(x344, (0, 1, 2, 3), (1, 0, 3, 2)) * 6.0
    x345 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x345 += einsum(t3.abaaba, (0, 1, 2, 3, 4, 5), x46, (1, 4, 0, 2, 6, 7), (6, 7, 3, 5))
    rdm2_f_aaaa_ovvv += einsum(x345, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0000000000000404
    rdm2_f_aaaa_vovv += einsum(x345, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0000000000000404
    x346 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x346 += einsum(t2.abab, (0, 1, 2, 3), x162, (1, 3, 4, 5), (0, 4, 2, 5))
    x347 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x347 += einsum(t2.abab, (0, 1, 2, 3), x163, (1, 3, 4, 5), (0, 4, 5, 2))
    x348 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x348 += einsum(t2.aaaa, (0, 1, 2, 3), x81, (1, 4, 3, 5), (0, 2, 4, 5)) * 4.0
    x349 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x349 += einsum(x329, (0, 1, 2, 3), (0, 1, 2, 3))
    x349 += einsum(x180, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x349 += einsum(x203, (0, 1, 2, 3), (0, 1, 2, 3))
    x349 += einsum(x204, (0, 1, 2, 3), (0, 1, 2, 3)) * 4.0
    x349 += einsum(x208, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x349 += einsum(x205, (0, 1, 2, 3), (0, 1, 2, 3)) * 9.0
    x349 += einsum(x209, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x350 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x350 += einsum(t1.aa, (0, 1), x349, (0, 2, 3, 4), (2, 3, 4, 1))
    x351 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x351 += einsum(x331, (0, 1), (0, 1))
    x351 += einsum(x184, (0, 1), (0, 1))
    x351 += einsum(x185, (0, 1), (0, 1)) * 2.0
    x351 += einsum(x186, (0, 1), (0, 1)) * 0.9999999999999601
    x351 += einsum(x187, (0, 1), (0, 1)) * 1.9999999999999194
    x351 += einsum(x188, (0, 1), (0, 1)) * 2.9999999999998788
    x352 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x352 += einsum(x346, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x352 += einsum(x347, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x352 += einsum(x348, (0, 1, 2, 3), (0, 2, 3, 1))
    x352 += einsum(x350, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x352 += einsum(t1.aa, (0, 1), x351, (2, 3), (0, 2, 1, 3))
    rdm2_f_aaaa_ovvv += einsum(x352, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_aaaa_ovvv += einsum(x352, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_vovv += einsum(x352, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_aaaa_vovv += einsum(x352, (0, 1, 2, 3), (1, 0, 3, 2))
    x353 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x353 += einsum(t2.aaaa, (0, 1, 2, 3), x102, (0, 1, 4, 5), (4, 5, 2, 3)) * 2.0
    rdm2_f_aaaa_ovvv += einsum(x353, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_aaaa_vovv += einsum(x353, (0, 1, 2, 3), (1, 0, 3, 2))
    x354 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x354 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3)) * 0.3333333333333333
    x354 += einsum(x11, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.3333333333333333
    x354 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x355 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x355 += einsum(t1.aa, (0, 1), x354, (0, 2, 3, 4), (2, 3, 4, 1)) * 3.0
    rdm2_f_aaaa_ovvv += einsum(t1.aa, (0, 1), x355, (0, 2, 3, 4), (2, 3, 4, 1)) * -2.0
    x356 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x356 += einsum(x227, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x356 += einsum(x197, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x356 += einsum(x198, (0, 1, 2, 3), (0, 1, 2, 3))
    x356 += einsum(x199, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.3333333333333333
    x356 += einsum(x195, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x356 += einsum(x200, (0, 1, 2, 3), (0, 1, 2, 3))
    x356 += einsum(x213, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x356 += einsum(t1.aa, (0, 1), x22, (2, 3, 0, 4), (2, 3, 4, 1)) * -0.6666666666666666
    rdm2_f_abab_ovvv += einsum(t1.bb, (0, 1), x356, (0, 2, 3, 4), (3, 2, 4, 1)) * 3.0
    x357 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x357 += einsum(x259, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x357 += einsum(x260, (0, 1, 2, 3), (0, 1, 2, 3))
    x357 += einsum(x261, (0, 1, 2, 3), (0, 1, 2, 3))
    x357 += einsum(x262, (0, 1, 2, 3), (0, 1, 2, 3))
    x357 += einsum(x263, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_ovvv += einsum(t1.aa, (0, 1), x357, (2, 3, 0, 4), (4, 2, 1, 3)) * -2.0
    x358 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x358 += einsum(x333, (0, 1), (0, 1)) * 1.00000000000004
    x358 += einsum(x273, (0, 1), (0, 1)) * 2.00000000000008
    x358 += einsum(x274, (0, 1), (0, 1)) * 1.00000000000004
    x358 += einsum(x275, (0, 1), (0, 1)) * 2.9999999999999982
    x358 += einsum(x276, (0, 1), (0, 1)) * 1.9999999999999991
    x358 += einsum(x277, (0, 1), (0, 1))
    rdm2_f_abab_ovvv += einsum(t1.aa, (0, 1), x358, (2, 3), (0, 2, 1, 3)) * 0.9999999999999601
    x359 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x359 += einsum(t3.babbab, (0, 1, 2, 3, 4, 5), x87, (0, 2, 6, 7, 1, 4), (6, 7, 3, 5))
    rdm2_f_bbbb_ovvv = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_ovvv += einsum(x359, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0000000000000404
    rdm2_f_bbbb_vovv = np.zeros((nvir[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    rdm2_f_bbbb_vovv += einsum(x359, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0000000000000404
    x360 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x360 += einsum(l2.abab, (0, 1, 2, 3), t3.babbab, (4, 2, 3, 5, 0, 6), (4, 1, 5, 6))
    rdm2_f_bbbb_ovvv += einsum(x360, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_bbbb_vovv += einsum(x360, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x361 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x361 += einsum(l1.bb, (0, 1), t2.bbbb, (2, 1, 3, 4), (2, 0, 3, 4))
    rdm2_f_bbbb_ovvv += einsum(x361, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    rdm2_f_bbbb_vovv += einsum(x361, (0, 1, 2, 3), (1, 0, 3, 2)) * 2.0
    x362 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x362 += einsum(l2.bbbb, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 3, 5, 6, 1), (4, 0, 5, 6))
    rdm2_f_bbbb_ovvv += einsum(x362, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    rdm2_f_bbbb_vovv += einsum(x362, (0, 1, 2, 3), (1, 0, 3, 2)) * 6.0
    x363 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x363 += einsum(t3.bbbbbb, (0, 1, 2, 3, 4, 5), x113, (0, 1, 2, 6, 7, 5), (6, 7, 3, 4)) * -1.0
    rdm2_f_bbbb_ovvv += einsum(x363, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.000000000000116
    rdm2_f_bbbb_vovv += einsum(x363, (0, 1, 2, 3), (1, 0, 3, 2)) * 6.000000000000116
    x364 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x364 += einsum(t2.bbbb, (0, 1, 2, 3), x146, (1, 4, 3, 5), (0, 4, 5, 2)) * -1.0
    x365 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x365 += einsum(t2.bbbb, (0, 1, 2, 3), x147, (1, 4, 3, 5), (0, 4, 2, 5))
    x366 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x366 += einsum(t2.abab, (0, 1, 2, 3), x99, (4, 5, 0, 2), (1, 4, 5, 3))
    x367 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x367 += einsum(t2.abab, (0, 1, 2, 3), x100, (4, 5, 0, 2), (1, 4, 3, 5))
    x368 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x368 += einsum(x240, (0, 1, 2, 3), (0, 1, 2, 3))
    x368 += einsum(x241, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x368 += einsum(x242, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.25
    x368 += einsum(x243, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.5
    x368 += einsum(x244, (0, 1, 2, 3), (0, 1, 2, 3))
    x368 += einsum(x245, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x368 += einsum(x246, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.25
    x369 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x369 += einsum(t1.bb, (0, 1), x368, (0, 2, 3, 4), (2, 3, 4, 1)) * 4.0
    x370 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x370 += einsum(x333, (0, 1), (0, 1))
    x370 += einsum(x273, (0, 1), (0, 1)) * 2.0
    x370 += einsum(x274, (0, 1), (0, 1))
    x370 += einsum(x275, (0, 1), (0, 1)) * 2.9999999999998788
    x370 += einsum(x276, (0, 1), (0, 1)) * 1.9999999999999194
    x370 += einsum(x277, (0, 1), (0, 1)) * 0.9999999999999601
    x371 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x371 += einsum(x364, (0, 1, 2, 3), (0, 1, 2, 3)) * -12.0
    x371 += einsum(x365, (0, 1, 2, 3), (0, 1, 2, 3)) * -4.0
    x371 += einsum(x366, (0, 1, 2, 3), (0, 1, 2, 3)) * -2.0
    x371 += einsum(x367, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x371 += einsum(x369, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x371 += einsum(t1.bb, (0, 1), x370, (2, 3), (0, 2, 1, 3))
    rdm2_f_bbbb_ovvv += einsum(x371, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_bbbb_ovvv += einsum(x371, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_bbbb_vovv += einsum(x371, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    rdm2_f_bbbb_vovv += einsum(x371, (0, 1, 2, 3), (1, 0, 3, 2))
    x372 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x372 += einsum(t2.bbbb, (0, 1, 2, 3), x117, (0, 1, 4, 5), (4, 5, 2, 3)) * 2.0
    rdm2_f_bbbb_ovvv += einsum(x372, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    rdm2_f_bbbb_vovv += einsum(x372, (0, 1, 2, 3), (1, 0, 3, 2))
    x373 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x373 += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3))
    x373 += einsum(x41, (0, 1, 2, 3), (0, 1, 2, 3)) * -3.0
    x373 += einsum(x42, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x374 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x374 += einsum(t1.bb, (0, 1), x373, (0, 2, 3, 4), (2, 3, 4, 1))
    x375 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x375 += einsum(t1.bb, (0, 1), x374, (0, 2, 3, 4), (2, 3, 4, 1)) * 2.0
    rdm2_f_bbbb_ovvv += einsum(x375, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    rdm2_f_bbbb_vovv += einsum(x375, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x376 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x376 += einsum(t1.aa, (0, 1), x354, (0, 2, 3, 4), (2, 3, 4, 1))
    rdm2_f_aaaa_vovv += einsum(t1.aa, (0, 1), x376, (0, 2, 3, 4), (3, 2, 1, 4)) * -6.0
    x377 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x377 += einsum(x79, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.3333333333333333
    x377 += einsum(x80, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    rdm2_f_abab_vovv += einsum(t2.abab, (0, 1, 2, 3), x377, (0, 4, 2, 5), (4, 1, 5, 3)) * -6.0
    x378 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x378 += einsum(x248, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x378 += einsum(x249, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.6666666666666666
    x378 += einsum(x250, (0, 1, 2, 3), (0, 1, 2, 3))
    x378 += einsum(x251, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x378 += einsum(x252, (0, 1, 2, 3), (0, 1, 2, 3)) * 1.3333333333333333
    x378 += einsum(x253, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.6666666666666666
    x378 += einsum(x254, (0, 1, 2, 3), (0, 1, 2, 3))
    x378 += einsum(t1.bb, (0, 1), x104, (0, 2, 3, 4), (2, 1, 3, 4)) * -0.3333333333333333
    rdm2_f_abab_vovv += einsum(t1.aa, (0, 1), x378, (2, 3, 0, 4), (4, 2, 1, 3)) * 3.0
    x379 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x379 += einsum(x339, (0, 1, 2, 3), (0, 1, 2, 3)) * 0.5
    x379 += einsum(x265, (0, 1, 2, 3), (0, 1, 2, 3))
    x379 += einsum(x266, (0, 1, 2, 3), (0, 1, 2, 3))
    x379 += einsum(x267, (0, 1, 2, 3), (0, 1, 2, 3))
    x379 += einsum(x268, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_abab_vovv += einsum(t1.bb, (0, 1), x379, (0, 2, 3, 4), (3, 2, 4, 1)) * -2.0
    x380 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x380 += einsum(x331, (0, 1), (0, 1)) * 0.3333333333333468
    x380 += einsum(x184, (0, 1), (0, 1)) * 0.3333333333333468
    x380 += einsum(x185, (0, 1), (0, 1)) * 0.6666666666666936
    x380 += einsum(x186, (0, 1), (0, 1)) * 0.33333333333333354
    x380 += einsum(x187, (0, 1), (0, 1)) * 0.6666666666666667
    x380 += einsum(x188, (0, 1), (0, 1))
    rdm2_f_abab_vovv += einsum(t1.bb, (0, 1), x380, (2, 3), (2, 0, 3, 1)) * 2.9999999999998788
    x381 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x381 += einsum(t1.aa, (0, 1), l2.aaaa, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_aaaa_vvov += einsum(x381, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_aaaa_vvvo += einsum(x381, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    rdm2_f_aaaa_vvvv += einsum(t1.aa, (0, 1), x381, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0
    x382 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x382 += einsum(t1.bb, (0, 1), l2.bbbb, (2, 3, 4, 0), (4, 2, 3, 1))
    rdm2_f_bbbb_vvov += einsum(x382, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    rdm2_f_bbbb_vvvo += einsum(x382, (0, 1, 2, 3), (2, 1, 3, 0)) * 2.0
    rdm2_f_bbbb_vvvv += einsum(t1.bb, (0, 1), x382, (0, 2, 3, 4), (2, 3, 1, 4)) * 2.0
    x383 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x383 += einsum(t1.aa, (0, 1), l2.abab, (2, 3, 0, 4), (4, 3, 2, 1))
    rdm2_f_abab_vvvo += einsum(x383, (0, 1, 2, 3), (2, 1, 3, 0))
    x384 = np.zeros((nvir[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x384 += einsum(t1.aa, (0, 1), x81, (0, 2, 3, 4), (1, 2, 3, 4)) * 2.0
    rdm2_f_aaaa_vvvv += einsum(x384, (0, 1, 2, 3), (1, 2, 0, 3))
    rdm2_f_aaaa_vvvv += einsum(x384, (0, 1, 2, 3), (1, 2, 3, 0)) * -1.0
    x385 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x385 += einsum(x383, (0, 1, 2, 3), (0, 1, 2, 3))
    x385 += einsum(x162, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x385 += einsum(x163, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    rdm2_f_abab_vvvv += einsum(t1.bb, (0, 1), x385, (0, 2, 3, 4), (3, 2, 4, 1))
    x386 = np.zeros((nvir[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x386 += einsum(t1.bb, (0, 1), x148, (0, 2, 3, 4), (2, 3, 4, 1)) * 6.0
    rdm2_f_bbbb_vvvv += einsum(x386, (0, 1, 2, 3), (0, 1, 3, 2))
    rdm2_f_bbbb_vvvv += einsum(x386, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0

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

