# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 3), ())
    e_cc += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 2), ()) * -1.0
    e_cc += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 2, 1, 3), ())
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
    x3 += einsum(f.aa.ov, (0, 1), (0, 1)) * 2.0
    x3 += einsum(t1.aa, (0, 1), x2, (0, 2, 3, 1), (2, 3)) * -1.0
    e_cc += einsum(t1.aa, (0, 1), x3, (0, 1), ()) * 0.5

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    t1new = Namespace()
    t2new = Namespace()
    t3new = Namespace()

    # T amplitudes
    t1new_bb = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    t1new_bb += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 0, 2, 5, 1, 3), (4, 5)) * 3.0
    t1new_bb += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.abaaba, (0, 4, 2, 3, 5, 1), (4, 5)) * -1.0
    t1new_bb += einsum(f.bb.ov, (0, 1), (0, 1))
    t1new_bb += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 2, 5, 1, 3), (4, 5)) * 2.0
    t1new_aa = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    t1new_aa += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 0, 2, 5, 3, 1), (4, 5)) * -3.0
    t1new_aa += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.babbab, (0, 4, 2, 1, 5, 3), (4, 5))
    t1new_aa += einsum(f.aa.ov, (0, 1), (0, 1))
    t1new_aa += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 0, 5, 3, 1), (4, 5)) * 2.0
    t2new_aaaa = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    t2new_abab = np.zeros((nocc[0], nocc[1], nvir[0], nvir[1]), dtype=np.float64)
    t2new_abab += einsum(v.aabb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    t2new_bbbb = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -2.0
    x0 = np.zeros((nocc[1], nvir[1]), dtype=np.float64)
    x0 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 1, 2, 3), (2, 3))
    t1new_bb += einsum(x0, (0, 1), (0, 1))
    x1 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x1 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x2 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x2 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x2 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_bb += einsum(t2.bbbb, (0, 1, 2, 3), x2, (4, 1, 0, 3), (4, 2)) * -2.0
    t2new_abab += einsum(x2, (0, 1, 2, 3), t3.babbab, (1, 4, 2, 5, 6, 3), (4, 0, 6, 5)) * 2.0
    x3 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x3 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 4, 1), (0, 4, 2, 3))
    x4 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x4 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x4 += einsum(x3, (0, 1, 2, 3), (1, 0, 2, 3))
    t1new_bb += einsum(t2.abab, (0, 1, 2, 3), x4, (1, 4, 0, 2), (4, 3)) * -1.0
    t2new_abab += einsum(x4, (0, 1, 2, 3), t3.abaaba, (4, 0, 2, 5, 6, 3), (4, 1, 5, 6)) * -2.0
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
    t2new_aaaa += einsum(x9, (0, 1), t3.abaaba, (2, 0, 3, 4, 1, 5), (2, 3, 4, 5)) * 2.0
    t2new_abab += einsum(x9, (0, 1), t3.babbab, (2, 3, 0, 4, 5, 1), (3, 2, 5, 4)) * 2.0
    t2new_bbbb += einsum(x9, (0, 1), t3.bbbbbb, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5)) * 6.0
    x10 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x10 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 1), (2, 3))
    t1new_aa += einsum(x10, (0, 1), (0, 1))
    x11 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x11 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x11 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x12 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x12 += einsum(t1.aa, (0, 1), x11, (0, 2, 3, 1), (2, 3))
    x13 = np.zeros((nocc[0], nvir[0]), dtype=np.float64)
    x13 += einsum(f.aa.ov, (0, 1), (0, 1))
    x13 += einsum(x10, (0, 1), (0, 1))
    x13 += einsum(x12, (0, 1), (0, 1)) * -1.0
    t1new_bb += einsum(x13, (0, 1), t2.abab, (0, 2, 1, 3), (2, 3))
    t1new_aa += einsum(x13, (0, 1), t2.aaaa, (2, 0, 3, 1), (2, 3)) * 2.0
    t2new_aaaa += einsum(x13, (0, 1), t3.aaaaaa, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5)) * 6.0
    t2new_abab += einsum(x13, (0, 1), t3.abaaba, (2, 3, 0, 4, 5, 1), (2, 3, 4, 5)) * 2.0
    t2new_bbbb += einsum(x13, (0, 1), t3.babbab, (2, 0, 3, 4, 1, 5), (2, 3, 4, 5)) * 2.0
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
    x18 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x18 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x19 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x19 += einsum(t1.bb, (0, 1), x18, (0, 2, 3, 1), (2, 3))
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
    x23 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x23 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 4, 1), (0, 2, 4, 3))
    x24 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x24 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3))
    x24 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3))
    t1new_aa += einsum(t2.aaaa, (0, 1, 2, 3), x24, (4, 0, 1, 3), (4, 2)) * 2.0
    t2new_abab += einsum(x24, (0, 1, 2, 3), t3.abaaba, (1, 4, 2, 5, 6, 3), (0, 4, 5, 6)) * 2.0
    x25 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x25 += einsum(t1.aa, (0, 1), v.aabb.ovov, (2, 1, 3, 4), (3, 4, 0, 2))
    x26 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x26 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x26 += einsum(x25, (0, 1, 2, 3), (0, 1, 3, 2))
    t1new_aa += einsum(t2.abab, (0, 1, 2, 3), x26, (1, 3, 0, 4), (4, 2)) * -1.0
    t2new_abab += einsum(x26, (0, 1, 2, 3), t3.babbab, (4, 2, 0, 5, 6, 1), (3, 4, 6, 5)) * -2.0
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
    x33 += einsum(f.aa.oo, (0, 1), (0, 1)) * 0.5
    x33 += einsum(x29, (0, 1), (1, 0)) * 0.5
    x33 += einsum(x30, (0, 1), (1, 0)) * 0.5
    x33 += einsum(x31, (0, 1), (1, 0))
    x33 += einsum(t1.aa, (0, 1), x32, (0, 2, 3, 1), (3, 2)) * -0.5
    x33 += einsum(t1.aa, (0, 1), x13, (2, 1), (2, 0)) * 0.5
    t1new_aa += einsum(t1.aa, (0, 1), x33, (0, 2), (2, 1)) * -2.0
    x34 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x34 += einsum(f.aa.vv, (0, 1), (0, 1))
    x34 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (0, 2, 3, 1), (2, 3)) * -1.0
    t1new_aa += einsum(t1.aa, (0, 1), x34, (1, 2), (0, 2))
    x35 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x35 += einsum(t1.aa, (0, 1), v.aaaa.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x36 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x36 += einsum(t1.aa, (0, 1), x35, (2, 3, 1, 4), (0, 2, 3, 4))
    x37 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x37 += einsum(v.aabb.vvov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 1), (4, 5, 6, 0))
    x38 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x38 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 0, 6, 1, 3), (4, 5, 6, 2))
    x39 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x39 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x39 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x40 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x40 += einsum(t2.aaaa, (0, 1, 2, 3), x39, (1, 4, 3, 5), (0, 4, 2, 5))
    x41 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x41 += einsum(t2.aaaa, (0, 1, 2, 3), x40, (4, 1, 5, 3), (0, 4, 2, 5)) * -4.0
    x42 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x42 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 1), (2, 3))
    x43 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x43 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 4, 1, 3), (2, 4))
    x44 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x44 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x45 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x45 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x45 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x46 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x46 += einsum(t1.aa, (0, 1), x45, (0, 2, 1, 3), (2, 3))
    x47 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x47 += einsum(x42, (0, 1), (1, 0)) * -1.0
    x47 += einsum(x43, (0, 1), (1, 0))
    x47 += einsum(x44, (0, 1), (1, 0)) * 2.0
    x47 += einsum(x46, (0, 1), (0, 1)) * -1.0
    x48 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x48 += einsum(x47, (0, 1), t2.aaaa, (2, 3, 4, 0), (2, 3, 4, 1)) * -2.0
    x49 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x49 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x50 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x50 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.abaaba, (4, 2, 5, 6, 3, 1), (4, 5, 0, 6))
    x51 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x51 += einsum(v.aaaa.ovov, (0, 1, 2, 3), t3.aaaaaa, (4, 5, 2, 6, 3, 1), (4, 5, 0, 6)) * -1.0
    x52 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x52 += einsum(x13, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4)) * -2.0
    x53 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x53 += einsum(t1.aa, (0, 1), x23, (2, 3, 4, 1), (2, 0, 4, 3))
    x54 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x54 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x54 += einsum(x53, (0, 1, 2, 3), (3, 1, 2, 0))
    x55 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x55 += einsum(t1.aa, (0, 1), x54, (0, 2, 3, 4), (2, 3, 4, 1))
    x56 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x56 += einsum(x49, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x56 += einsum(x50, (0, 1, 2, 3), (2, 1, 0, 3)) * 2.0
    x56 += einsum(x51, (0, 1, 2, 3), (2, 1, 0, 3)) * 6.0
    x56 += einsum(x52, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x56 += einsum(x55, (0, 1, 2, 3), (1, 0, 2, 3))
    x57 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x57 += einsum(t1.aa, (0, 1), x56, (0, 2, 3, 4), (2, 3, 1, 4))
    x58 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x58 += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    x58 += einsum(x37, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x58 += einsum(x38, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x58 += einsum(x41, (0, 1, 2, 3), (1, 0, 3, 2))
    x58 += einsum(x48, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x58 += einsum(x57, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x58, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x58, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x59 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x59 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x60 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x60 += einsum(v.aabb.ooov, (0, 1, 2, 3), t3.abaaba, (4, 2, 1, 5, 3, 6), (4, 0, 5, 6))
    x61 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x61 += einsum(v.aaaa.ooov, (0, 1, 2, 3), t3.aaaaaa, (4, 1, 2, 5, 6, 3), (4, 0, 5, 6))
    x62 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x62 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x63 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x63 += einsum(t2.aaaa, (0, 1, 2, 3), x62, (4, 5, 0, 1), (4, 5, 2, 3))
    x64 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x64 += einsum(x25, (0, 1, 2, 3), t3.abaaba, (4, 0, 3, 5, 1, 6), (2, 4, 5, 6))
    x65 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x65 += einsum(x23, (0, 1, 2, 3), t3.aaaaaa, (4, 1, 2, 5, 6, 3), (0, 4, 5, 6)) * -1.0
    x66 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x66 += einsum(t1.aa, (0, 1), x13, (2, 1), (0, 2))
    x67 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x67 += einsum(f.aa.oo, (0, 1), (0, 1))
    x67 += einsum(x66, (0, 1), (0, 1))
    x68 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x68 += einsum(x67, (0, 1), t2.aaaa, (2, 1, 3, 4), (2, 0, 3, 4)) * -2.0
    x69 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x69 += einsum(t1.aa, (0, 1), x32, (0, 2, 3, 1), (2, 3))
    x70 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x70 += einsum(x29, (0, 1), (1, 0))
    x70 += einsum(x30, (0, 1), (1, 0))
    x70 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x70 += einsum(x69, (0, 1), (1, 0)) * -1.0
    x71 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x71 += einsum(x70, (0, 1), t2.aaaa, (2, 0, 3, 4), (2, 1, 3, 4)) * -2.0
    x72 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x72 += einsum(x59, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x72 += einsum(x60, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x72 += einsum(x61, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    x72 += einsum(x63, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x72 += einsum(x64, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x72 += einsum(x65, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.0
    x72 += einsum(x68, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x72 += einsum(x71, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x72, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x72, (0, 1, 2, 3), (1, 0, 2, 3))
    x73 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x73 += einsum(t1.aa, (0, 1), v.aaaa.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x74 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x74 += einsum(t1.aa, (0, 1), v.aabb.vvov, (2, 1, 3, 4), (3, 4, 0, 2))
    t2new_abab += einsum(x74, (0, 1, 2, 3), (2, 0, 3, 1))
    x75 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x75 += einsum(t2.abab, (0, 1, 2, 3), x74, (1, 3, 4, 5), (4, 0, 2, 5))
    x76 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x76 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x76 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 3, 1)) * -0.5
    x77 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x77 += einsum(x28, (0, 1, 2, 3), x76, (0, 4, 2, 5), (1, 4, 3, 5)) * 2.0
    x78 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x78 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2))
    x79 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x79 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x79 += einsum(x78, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x80 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x80 += einsum(t2.abab, (0, 1, 2, 3), x79, (1, 3, 4, 5), (0, 4, 2, 5))
    x81 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x81 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x81 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x82 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x82 += einsum(t1.aa, (0, 1), x81, (2, 1, 3, 4), (0, 2, 3, 4))
    x83 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x83 += einsum(t2.aaaa, (0, 1, 2, 3), x82, (4, 1, 5, 3), (0, 4, 2, 5)) * -2.0
    x84 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x84 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ooov, (4, 5, 1, 3), (0, 4, 5, 2))
    x85 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x85 += einsum(t1.aa, (0, 1), x62, (2, 3, 4, 0), (2, 4, 3, 1))
    x86 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x86 += einsum(t1.aa, (0, 1), x73, (2, 3, 1, 4), (0, 2, 3, 4))
    x87 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x87 += einsum(t2.abab, (0, 1, 2, 3), x25, (1, 3, 4, 5), (4, 0, 5, 2))
    x88 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x88 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x88 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x89 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x89 += einsum(t2.aaaa, (0, 1, 2, 3), x88, (4, 5, 1, 3), (0, 4, 5, 2)) * 2.0
    x90 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x90 += einsum(x23, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x90 += einsum(x23, (0, 1, 2, 3), (0, 2, 1, 3))
    x91 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x91 += einsum(t2.aaaa, (0, 1, 2, 3), x90, (4, 1, 5, 3), (0, 4, 5, 2)) * 2.0
    x92 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x92 += einsum(x84, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x92 += einsum(x85, (0, 1, 2, 3), (0, 2, 1, 3))
    x92 += einsum(x86, (0, 1, 2, 3), (0, 2, 1, 3))
    x92 += einsum(x87, (0, 1, 2, 3), (0, 2, 1, 3))
    x92 += einsum(x89, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x92 += einsum(x91, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    x93 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x93 += einsum(t1.aa, (0, 1), x92, (2, 0, 3, 4), (2, 3, 1, 4))
    x94 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x94 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3))
    x94 += einsum(x75, (0, 1, 2, 3), (0, 1, 2, 3))
    x94 += einsum(x77, (0, 1, 2, 3), (1, 0, 3, 2))
    x94 += einsum(x80, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x94 += einsum(x83, (0, 1, 2, 3), (1, 0, 2, 3))
    x94 += einsum(x93, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x94, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_aaaa += einsum(x94, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_aaaa += einsum(x94, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_aaaa += einsum(x94, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x95 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x95 += einsum(f.aa.vv, (0, 1), t2.aaaa, (2, 3, 4, 1), (2, 3, 0, 4))
    x96 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x96 += einsum(t2.abab, (0, 1, 2, 3), x7, (1, 4, 3, 5), (4, 5, 0, 2))
    x97 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x97 += einsum(t2.abab, (0, 1, 2, 3), x96, (1, 3, 4, 5), (0, 4, 2, 5)) * -1.0
    x98 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x98 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x98 += einsum(x95, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    x98 += einsum(x97, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_aaaa += einsum(x98, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_aaaa += einsum(x98, (0, 1, 2, 3), (0, 1, 2, 3))
    x99 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x99 += einsum(t2.aaaa, (0, 1, 2, 3), (0, 1, 2, 3))
    x99 += einsum(t1.aa, (0, 1), t1.aa, (2, 3), (0, 2, 1, 3))
    x100 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x100 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x100 += einsum(v.aaaa.ovov, (0, 1, 2, 3), x99, (4, 5, 1, 3), (0, 5, 2, 4))
    t2new_aaaa += einsum(t2.aaaa, (0, 1, 2, 3), x100, (0, 4, 1, 5), (4, 5, 2, 3)) * -2.0
    x101 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x101 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 2, 5, 3), (0, 1, 4, 5))
    x102 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x102 += einsum(t1.aa, (0, 1), x101, (2, 3, 0, 4), (2, 3, 4, 1)) * -1.0
    x102 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -0.5
    x102 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (2, 0, 1, 3)) * 0.5
    t2new_aaaa += einsum(t1.aa, (0, 1), x102, (2, 3, 0, 4), (2, 3, 1, 4)) * 2.0
    x103 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x103 += einsum(t1.bb, (0, 1), v.aabb.ovov, (2, 3, 0, 4), (1, 4, 2, 3))
    x104 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x104 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x104 += einsum(x103, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new_abab += einsum(x104, (0, 1, 2, 3), t3.abaaba, (4, 5, 2, 6, 0, 3), (4, 5, 6, 1)) * 2.0
    x105 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x105 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x105 += einsum(t1.bb, (0, 1), v.bbbb.ovov, (2, 3, 0, 4), (2, 1, 3, 4))
    t2new_abab += einsum(x105, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 2, 6, 3), (5, 4, 6, 1)) * 2.0
    x106 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x106 += einsum(t1.aa, (0, 1), v.aabb.ovov, (0, 2, 3, 4), (3, 4, 1, 2))
    x107 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x107 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1))
    x107 += einsum(x106, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_abab += einsum(x107, (0, 1, 2, 3), t3.babbab, (4, 5, 0, 6, 2, 1), (5, 4, 3, 6)) * 2.0
    x108 = np.zeros((nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x108 += einsum(v.aaaa.ovvv, (0, 1, 2, 3), (0, 2, 3, 1))
    x108 += einsum(t1.aa, (0, 1), v.aaaa.ovov, (2, 3, 0, 4), (2, 1, 3, 4))
    t2new_abab += einsum(x108, (0, 1, 2, 3), t3.abaaba, (4, 5, 0, 3, 6, 2), (4, 5, 1, 6)) * -2.0
    x109 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x109 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x109 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x109 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (4, 0, 5, 2))
    x109 += einsum(x39, (0, 1, 2, 3), x76, (0, 4, 2, 5), (1, 4, 3, 5)) * -2.0
    x109 += einsum(t1.aa, (0, 1), x45, (2, 3, 1, 4), (2, 0, 3, 4)) * -1.0
    x109 += einsum(t1.aa, (0, 1), x32, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x109, (0, 4, 2, 5), (4, 1, 5, 3))
    x110 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x110 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x110 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 3, 1)) * -0.5
    x111 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x111 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x111 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x112 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x112 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x112 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x113 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x113 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x113 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x113 += einsum(x110, (0, 1, 2, 3), x7, (0, 4, 5, 2), (4, 1, 5, 3)) * -2.0
    x113 += einsum(t1.bb, (0, 1), x111, (2, 3, 1, 4), (2, 0, 3, 4)) * -1.0
    x113 += einsum(t1.bb, (0, 1), x112, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x113, (1, 4, 3, 5), (0, 4, 2, 5)) * -1.0
    x114 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x114 += einsum(t1.bb, (0, 1), v.aabb.ovvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x115 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x115 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x115 += einsum(t1.bb, (0, 1), v.aabb.ovoo, (2, 3, 4, 0), (4, 1, 2, 3)) * -1.0
    x115 += einsum(x114, (0, 1, 2, 3), (0, 1, 2, 3))
    x115 += einsum(v.aabb.ovov, (0, 1, 2, 3), x110, (2, 4, 3, 5), (4, 5, 0, 1)) * 2.0
    t2new_abab += einsum(t2.aaaa, (0, 1, 2, 3), x115, (4, 5, 1, 3), (0, 4, 2, 5)) * 2.0
    x116 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x116 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 0, 4), (1, 4, 2, 3))
    x117 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x117 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x118 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x118 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x118 += einsum(x116, (0, 1, 2, 3), (1, 0, 3, 2))
    x118 += einsum(x117, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x118 += einsum(v.aabb.ovov, (0, 1, 2, 3), x6, (2, 4, 5, 1), (3, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x118, (3, 4, 0, 5), (5, 1, 2, 4))
    x119 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x119 += einsum(t1.aa, (0, 1), x26, (2, 3, 0, 4), (2, 3, 4, 1))
    x120 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x120 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x120 += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3))
    x120 += einsum(x119, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_abab += einsum(x110, (0, 1, 2, 3), x120, (0, 2, 4, 5), (4, 1, 5, 3)) * 2.0
    x121 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x121 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 4, 1), (0, 4, 2, 3))
    x122 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x122 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x122 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    x123 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x123 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x123 += einsum(x121, (0, 1, 2, 3), (1, 0, 3, 2))
    x123 += einsum(t1.aa, (0, 1), x122, (2, 3, 0, 4), (3, 2, 4, 1)) * -1.0
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x123, (1, 4, 2, 5), (0, 4, 5, 3)) * -1.0
    x124 = np.zeros((nvir[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x124 += einsum(v.aabb.vvvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x124 += einsum(t1.bb, (0, 1), v.aabb.vvov, (2, 3, 0, 4), (4, 1, 2, 3))
    x124 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 2, 3, 4), (3, 4, 2, 1))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x124, (3, 4, 2, 5), (0, 1, 5, 4)) * -1.0
    x125 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x125 += einsum(t1.bb, (0, 1), v.aabb.ooov, (2, 3, 4, 1), (0, 4, 2, 3))
    x126 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x126 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x127 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x127 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x127 += einsum(x125, (0, 1, 2, 3), (1, 0, 3, 2))
    x127 += einsum(x126, (0, 1, 2, 3), (1, 0, 3, 2))
    x127 += einsum(v.aabb.ovov, (0, 1, 2, 3), x6, (4, 3, 5, 1), (2, 4, 0, 5))
    t2new_abab += einsum(t2.abab, (0, 1, 2, 3), x127, (1, 4, 0, 5), (5, 4, 2, 3))
    x128 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x128 += einsum(t1.aa, (0, 1), v.aabb.ovvv, (0, 1, 2, 3), (2, 3))
    x129 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x129 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (0, 3, 1, 4), (2, 4)) * -1.0
    x130 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x130 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 1, 4), (3, 4))
    x131 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x131 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3))
    x131 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x132 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x132 += einsum(t1.bb, (0, 1), x131, (0, 1, 2, 3), (2, 3))
    x133 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x133 += einsum(f.bb.vv, (0, 1), (0, 1)) * -1.0
    x133 += einsum(x128, (0, 1), (1, 0)) * -1.0
    x133 += einsum(x129, (0, 1), (1, 0)) * 2.0
    x133 += einsum(x130, (0, 1), (1, 0))
    x133 += einsum(x132, (0, 1), (1, 0)) * -1.0
    x133 += einsum(t1.bb, (0, 1), x9, (0, 2), (2, 1))
    t2new_abab += einsum(x133, (0, 1), t2.abab, (2, 3, 4, 0), (2, 3, 4, 1)) * -1.0
    x134 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x134 += einsum(f.aa.vv, (0, 1), (0, 1)) * -1.0
    x134 += einsum(x42, (0, 1), (1, 0)) * -1.0
    x134 += einsum(x43, (0, 1), (1, 0))
    x134 += einsum(x44, (0, 1), (1, 0)) * 2.0
    x134 += einsum(x46, (0, 1), (0, 1)) * -1.0
    x134 += einsum(t1.aa, (0, 1), x13, (0, 2), (2, 1))
    t2new_abab += einsum(x134, (0, 1), t2.abab, (2, 3, 0, 4), (2, 3, 1, 4)) * -1.0
    x135 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x135 += einsum(f.aa.oo, (0, 1), (0, 1))
    x135 += einsum(x29, (0, 1), (1, 0))
    x135 += einsum(x30, (0, 1), (1, 0))
    x135 += einsum(x31, (0, 1), (1, 0)) * 2.0
    x135 += einsum(x69, (0, 1), (1, 0)) * -1.0
    x135 += einsum(x66, (0, 1), (1, 0))
    t2new_abab += einsum(x135, (0, 1), t2.abab, (0, 2, 3, 4), (1, 2, 3, 4)) * -1.0
    x136 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x136 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x136 += einsum(x117, (0, 1, 2, 3), (1, 0, 2, 3))
    x137 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x137 += einsum(t1.bb, (0, 1), x136, (1, 2, 3, 4), (0, 2, 3, 4))
    x138 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x138 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x138 += einsum(x126, (0, 1, 2, 3), (1, 0, 2, 3))
    x138 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (4, 2, 5, 3), (5, 1, 0, 4))
    x139 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x139 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x139 += einsum(x25, (0, 1, 2, 3), (0, 1, 3, 2))
    x139 += einsum(x137, (0, 1, 2, 3), (0, 1, 3, 2))
    x139 += einsum(t1.bb, (0, 1), x138, (0, 2, 3, 4), (2, 1, 4, 3)) * -1.0
    t2new_abab += einsum(t1.aa, (0, 1), x139, (2, 3, 0, 4), (4, 2, 1, 3)) * -1.0
    x140 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x140 += einsum(t1.aa, (0, 1), v.aabb.vvvv, (2, 1, 3, 4), (3, 4, 0, 2))
    x141 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x141 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1))
    x141 += einsum(x140, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_abab += einsum(t1.bb, (0, 1), x141, (1, 2, 3, 4), (3, 0, 4, 2))
    x142 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x142 += einsum(t1.aa, (0, 1), v.aabb.vvoo, (2, 1, 3, 4), (3, 4, 0, 2))
    x143 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x143 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x143 += einsum(x142, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_abab += einsum(t1.bb, (0, 1), x143, (0, 2, 3, 4), (3, 2, 4, 1)) * -1.0
    x144 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x144 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 0, 3, 4), (2, 3, 1, 4))
    x145 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x145 += einsum(v.bbbb.ooov, (0, 1, 2, 3), t3.bbbbbb, (4, 2, 1, 5, 6, 3), (4, 0, 5, 6)) * -1.0
    x146 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x146 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x147 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x147 += einsum(t2.bbbb, (0, 1, 2, 3), x146, (4, 5, 0, 1), (4, 5, 2, 3))
    x148 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x148 += einsum(v.aabb.ovoo, (0, 1, 2, 3), t3.babbab, (4, 0, 3, 5, 1, 6), (4, 2, 5, 6))
    x149 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x149 += einsum(x1, (0, 1, 2, 3), t3.bbbbbb, (4, 1, 2, 5, 6, 3), (0, 4, 5, 6)) * -1.0
    x150 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x150 += einsum(x3, (0, 1, 2, 3), t3.babbab, (4, 2, 1, 5, 3, 6), (0, 4, 5, 6))
    x151 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x151 += einsum(f.bb.oo, (0, 1), (0, 1))
    x151 += einsum(x20, (0, 1), (0, 1))
    x152 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x152 += einsum(x151, (0, 1), t2.bbbb, (2, 1, 3, 4), (0, 2, 3, 4)) * -2.0
    x153 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x153 += einsum(x15, (0, 1), (1, 0))
    x153 += einsum(x16, (0, 1), (1, 0)) * 2.0
    x153 += einsum(x17, (0, 1), (1, 0))
    x153 += einsum(x19, (0, 1), (1, 0)) * -1.0
    x154 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x154 += einsum(x153, (0, 1), t2.bbbb, (2, 0, 3, 4), (1, 2, 3, 4)) * -2.0
    x155 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x155 += einsum(x144, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x155 += einsum(x145, (0, 1, 2, 3), (0, 1, 3, 2)) * -6.0
    x155 += einsum(x147, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x155 += einsum(x148, (0, 1, 2, 3), (0, 1, 3, 2)) * -2.0
    x155 += einsum(x149, (0, 1, 2, 3), (0, 1, 3, 2)) * 6.0
    x155 += einsum(x150, (0, 1, 2, 3), (0, 1, 3, 2)) * 2.0
    x155 += einsum(x152, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x155 += einsum(x154, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_bbbb += einsum(x155, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x155, (0, 1, 2, 3), (1, 0, 2, 3))
    x156 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x156 += einsum(t1.bb, (0, 1), v.bbbb.vvvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x157 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x157 += einsum(t1.bb, (0, 1), x156, (2, 3, 1, 4), (0, 2, 3, 4))
    x158 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x158 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 0, 6, 1, 3), (4, 5, 6, 2))
    x159 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x159 += einsum(v.aabb.ovvv, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 3), (4, 5, 6, 2))
    x160 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x160 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x160 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x161 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x161 += einsum(t2.bbbb, (0, 1, 2, 3), x160, (1, 4, 5, 3), (4, 0, 5, 2))
    x162 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x162 += einsum(t2.bbbb, (0, 1, 2, 3), x161, (1, 4, 3, 5), (4, 0, 5, 2)) * -4.0
    x163 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x163 += einsum(t2.abab, (0, 1, 2, 3), x11, (0, 4, 5, 2), (1, 3, 4, 5))
    x164 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x164 += einsum(t2.abab, (0, 1, 2, 3), x163, (4, 5, 0, 2), (4, 1, 5, 3)) * -1.0
    x165 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x165 += einsum(x128, (0, 1), (1, 0)) * -1.0
    x165 += einsum(x129, (0, 1), (1, 0)) * 2.0
    x165 += einsum(x130, (0, 1), (1, 0))
    x165 += einsum(x132, (0, 1), (1, 0)) * -1.0
    x166 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x166 += einsum(x165, (0, 1), t2.bbbb, (2, 3, 4, 0), (2, 3, 1, 4)) * -2.0
    x167 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x167 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 2, 5, 3), (0, 1, 4, 5))
    x168 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x168 += einsum(v.bbbb.ovov, (0, 1, 2, 3), t3.bbbbbb, (4, 5, 2, 6, 1, 3), (4, 5, 0, 6))
    x169 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x169 += einsum(v.aabb.ovov, (0, 1, 2, 3), t3.babbab, (4, 0, 5, 6, 1, 3), (4, 5, 2, 6))
    x170 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x170 += einsum(x9, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4)) * -2.0
    x171 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x171 += einsum(t1.bb, (0, 1), x1, (2, 3, 4, 1), (2, 0, 4, 3))
    x172 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x172 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x172 += einsum(x171, (0, 1, 2, 3), (3, 1, 2, 0))
    x173 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x173 += einsum(t1.bb, (0, 1), x172, (0, 2, 3, 4), (2, 3, 4, 1))
    x174 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x174 += einsum(x167, (0, 1, 2, 3), (2, 1, 0, 3)) * -2.0
    x174 += einsum(x168, (0, 1, 2, 3), (2, 1, 0, 3)) * 6.0
    x174 += einsum(x169, (0, 1, 2, 3), (2, 1, 0, 3)) * 2.0
    x174 += einsum(x170, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x174 += einsum(x173, (0, 1, 2, 3), (1, 0, 2, 3))
    x175 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x175 += einsum(t1.bb, (0, 1), x174, (0, 2, 3, 4), (2, 3, 4, 1))
    x176 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x176 += einsum(x157, (0, 1, 2, 3), (0, 1, 2, 3))
    x176 += einsum(x158, (0, 1, 2, 3), (0, 1, 2, 3)) * -6.0
    x176 += einsum(x159, (0, 1, 2, 3), (0, 1, 2, 3)) * 2.0
    x176 += einsum(x162, (0, 1, 2, 3), (1, 0, 3, 2))
    x176 += einsum(x164, (0, 1, 2, 3), (1, 0, 3, 2))
    x176 += einsum(x166, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x176 += einsum(x175, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new_bbbb += einsum(x176, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new_bbbb += einsum(x176, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x177 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x177 += einsum(t1.bb, (0, 1), v.bbbb.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x178 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x178 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovov, (0, 2, 4, 5), (1, 4, 3, 5))
    x179 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x179 += einsum(t2.abab, (0, 1, 2, 3), x114, (4, 5, 0, 2), (4, 1, 3, 5))
    x180 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x180 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x180 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x180 += einsum(x178, (0, 1, 2, 3), (1, 0, 3, 2))
    x181 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x181 += einsum(t2.bbbb, (0, 1, 2, 3), x180, (1, 4, 3, 5), (4, 0, 5, 2)) * 2.0
    x182 = np.zeros((nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x182 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x182 += einsum(v.bbbb.ovvv, (0, 1, 2, 3), (0, 2, 1, 3))
    x183 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x183 += einsum(t1.bb, (0, 1), x182, (2, 3, 1, 4), (2, 0, 3, 4))
    x184 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x184 += einsum(t2.bbbb, (0, 1, 2, 3), x183, (1, 4, 3, 5), (4, 0, 5, 2)) * -2.0
    x185 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x185 += einsum(t1.bb, (0, 1), x146, (2, 3, 4, 0), (2, 4, 3, 1))
    x186 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x186 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.ovoo, (0, 2, 4, 5), (1, 4, 5, 3))
    x187 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x187 += einsum(t2.abab, (0, 1, 2, 3), x3, (4, 5, 0, 2), (4, 1, 5, 3))
    x188 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x188 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x188 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    x189 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x189 += einsum(t2.bbbb, (0, 1, 2, 3), x188, (1, 4, 5, 3), (4, 5, 0, 2)) * 2.0
    x190 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x190 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x190 += einsum(x1, (0, 1, 2, 3), (0, 2, 1, 3))
    x191 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x191 += einsum(t2.bbbb, (0, 1, 2, 3), x190, (4, 1, 5, 3), (4, 5, 0, 2)) * 2.0
    x192 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x192 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x192 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x192 += einsum(x177, (0, 1, 2, 3), (0, 1, 2, 3))
    x193 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x193 += einsum(t1.bb, (0, 1), x192, (2, 3, 1, 4), (2, 3, 0, 4))
    x194 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x194 += einsum(x185, (0, 1, 2, 3), (0, 2, 1, 3))
    x194 += einsum(x186, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x194 += einsum(x187, (0, 1, 2, 3), (0, 2, 1, 3))
    x194 += einsum(x189, (0, 1, 2, 3), (2, 1, 0, 3)) * -1.0
    x194 += einsum(x191, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x194 += einsum(x193, (0, 1, 2, 3), (2, 1, 0, 3))
    x195 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x195 += einsum(t1.bb, (0, 1), x194, (2, 0, 3, 4), (2, 3, 4, 1))
    x196 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x196 += einsum(x177, (0, 1, 2, 3), (0, 1, 2, 3))
    x196 += einsum(x178, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x196 += einsum(x179, (0, 1, 2, 3), (0, 1, 2, 3))
    x196 += einsum(x181, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x196 += einsum(x184, (0, 1, 2, 3), (0, 1, 3, 2))
    x196 += einsum(x195, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x196, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new_bbbb += einsum(x196, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new_bbbb += einsum(x196, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new_bbbb += einsum(x196, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x197 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x197 += einsum(f.bb.vv, (0, 1), t2.bbbb, (2, 3, 4, 1), (2, 3, 0, 4))
    x198 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x198 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x198 += einsum(x197, (0, 1, 2, 3), (1, 0, 3, 2)) * -2.0
    t2new_bbbb += einsum(x198, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new_bbbb += einsum(x198, (0, 1, 2, 3), (0, 1, 2, 3))
    x199 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x199 += einsum(t2.bbbb, (0, 1, 2, 3), (0, 1, 2, 3))
    x199 += einsum(t1.bb, (0, 1), t1.bb, (2, 3), (0, 2, 1, 3))
    x200 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x200 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x200 += einsum(v.bbbb.ovov, (0, 1, 2, 3), x199, (4, 5, 1, 3), (0, 5, 4, 2)) * -1.0
    t2new_bbbb += einsum(t2.bbbb, (0, 1, 2, 3), x200, (0, 4, 5, 1), (5, 4, 2, 3)) * -2.0
    x201 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x201 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovov, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x202 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x202 += einsum(t1.bb, (0, 1), x201, (2, 3, 0, 4), (2, 3, 4, 1)) * -2.0
    x202 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x202 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (2, 0, 1, 3))
    t2new_bbbb += einsum(t1.bb, (0, 1), x202, (2, 3, 0, 4), (2, 3, 1, 4))
    x203 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x203 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.oooo, (4, 5, 6, 1), (0, 4, 5, 6, 2, 3))
    x204 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x204 += einsum(t2.aaaa, (0, 1, 2, 3), x53, (4, 5, 1, 6), (5, 4, 0, 6, 2, 3))
    x205 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x205 += einsum(x62, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x205 += einsum(x62, (0, 1, 2, 3), (0, 2, 3, 1))
    x206 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x206 += einsum(t2.aaaa, (0, 1, 2, 3), x205, (4, 5, 6, 1), (4, 5, 6, 0, 2, 3)) * -1.0
    x207 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x207 += einsum(x203, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x207 += einsum(x204, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x207 += einsum(x206, (0, 1, 2, 3, 4, 5), (0, 3, 2, 1, 5, 4)) * -1.0
    x208 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x208 += einsum(t1.aa, (0, 1), x207, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    t3new_aaaaaa = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_aaaaaa += einsum(x208, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    x209 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x209 += einsum(t2.aaaa, (0, 1, 2, 3), x35, (4, 5, 3, 6), (4, 0, 1, 2, 6, 5))
    x210 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x210 += einsum(t2.aaaa, (0, 1, 2, 3), x23, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x211 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x211 += einsum(t1.aa, (0, 1), x210, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x212 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x212 += einsum(t2.aaaa, (0, 1, 2, 3), x82, (4, 5, 6, 3), (0, 1, 4, 5, 2, 6))
    x213 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x213 += einsum(x211, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x213 += einsum(x212, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x214 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x214 += einsum(t1.aa, (0, 1), x213, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x215 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x215 += einsum(x209, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -2.0
    x215 += einsum(x214, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_aaaaaa += einsum(x215, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x216 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x216 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovvv, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    x217 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x217 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x218 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x218 += einsum(t1.aa, (0, 1), x217, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x219 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x219 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x219 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x220 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x220 += einsum(t2.aaaa, (0, 1, 2, 3), x219, (4, 5, 3, 6), (4, 5, 0, 1, 6, 2)) * -1.0
    x221 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x221 += einsum(x218, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x221 += einsum(x220, (0, 1, 2, 3, 4, 5), (3, 2, 1, 0, 5, 4))
    x222 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x222 += einsum(t1.aa, (0, 1), x221, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x223 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x223 += einsum(x216, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x223 += einsum(x222, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_aaaaaa += einsum(x223, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x224 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x224 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ooov, (4, 1, 5, 6), (0, 4, 5, 2, 3, 6))
    x225 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x225 += einsum(t2.aaaa, (0, 1, 2, 3), x86, (4, 5, 1, 6), (4, 5, 0, 2, 3, 6))
    x226 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x226 += einsum(t1.aa, (0, 1), x219, (2, 3, 1, 4), (2, 3, 0, 4))
    x227 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x227 += einsum(t2.aaaa, (0, 1, 2, 3), x226, (4, 1, 5, 6), (5, 4, 0, 6, 2, 3)) * -2.0
    x228 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x228 += einsum(x224, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x228 += einsum(x225, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x228 += einsum(x227, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_aaaaaa += einsum(x228, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x229 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x229 += einsum(f.aa.ov, (0, 1), t1.aa, (2, 1), (0, 2))
    x230 = np.zeros((nocc[0], nocc[0]), dtype=np.float64)
    x230 += einsum(f.aa.oo, (0, 1), (0, 1))
    x230 += einsum(x229, (0, 1), (0, 1))
    t3new_babbab = np.zeros((nocc[1], nocc[0], nocc[1], nvir[1], nvir[0], nvir[1]), dtype=np.float64)
    t3new_babbab += einsum(x230, (0, 1), t3.babbab, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -2.0
    x231 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x231 += einsum(x230, (0, 1), t3.aaaaaa, (2, 3, 0, 4, 5, 6), (1, 2, 3, 4, 5, 6)) * 6.0
    t3new_aaaaaa += einsum(x231, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x231, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_aaaaaa += einsum(x231, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x232 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x232 += einsum(f.aa.ov, (0, 1), t1.aa, (0, 2), (1, 2))
    x233 = np.zeros((nvir[0], nvir[0]), dtype=np.float64)
    x233 += einsum(f.aa.vv, (0, 1), (0, 1))
    x233 += einsum(x232, (0, 1), (0, 1)) * -1.0
    t3new_babbab += einsum(x233, (0, 1), t3.babbab, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * 2.0
    x234 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x234 += einsum(x233, (0, 1), t3.aaaaaa, (2, 3, 4, 5, 6, 0), (2, 3, 4, 1, 5, 6)) * 6.0
    t3new_aaaaaa += einsum(x234, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new_aaaaaa += einsum(x234, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new_aaaaaa += einsum(x234, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x235 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x235 += einsum(f.aa.ov, (0, 1), t2.aaaa, (2, 3, 4, 1), (0, 2, 3, 4))
    x236 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0], nvir[0], nvir[0]), dtype=np.float64)
    x236 += einsum(t2.aaaa, (0, 1, 2, 3), x235, (1, 4, 5, 6), (5, 4, 0, 6, 2, 3)) * -1.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * 4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * 4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * 4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -4.0
    t3new_aaaaaa += einsum(x236, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * 4.0
    x237 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x237 += einsum(t2.abab, (0, 1, 2, 3), v.bbbb.ovvv, (4, 5, 6, 3), (1, 4, 5, 6, 0, 2))
    x238 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x238 += einsum(t2.abab, (0, 1, 2, 3), x156, (4, 5, 3, 6), (4, 1, 6, 5, 0, 2))
    x239 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x239 += einsum(t1.bb, (0, 1), v.bbbb.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x240 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x240 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x240 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x240 += einsum(x239, (0, 1, 2, 3), (1, 0, 2, 3))
    x241 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x241 += einsum(t2.abab, (0, 1, 2, 3), x240, (4, 5, 6, 3), (4, 5, 1, 6, 0, 2))
    x242 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x242 += einsum(t1.bb, (0, 1), x1, (2, 0, 3, 4), (2, 3, 1, 4))
    x243 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x243 += einsum(x242, (0, 1, 2, 3), (0, 1, 3, 2))
    x243 += einsum(x183, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x244 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x244 += einsum(t2.abab, (0, 1, 2, 3), x243, (4, 5, 3, 6), (4, 5, 1, 6, 0, 2))
    x245 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x245 += einsum(v.bbbb.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x245 += einsum(x171, (0, 1, 2, 3), (3, 1, 0, 2))
    x245 += einsum(x146, (0, 1, 2, 3), (2, 1, 0, 3))
    x245 += einsum(x146, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x246 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x246 += einsum(t2.abab, (0, 1, 2, 3), x245, (1, 4, 5, 6), (4, 5, 6, 3, 0, 2))
    x247 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x247 += einsum(t1.aa, (0, 1), v.aabb.ovoo, (0, 2, 3, 4), (3, 4, 1, 2))
    x248 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x248 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x248 += einsum(x247, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x249 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x249 += einsum(t2.abab, (0, 1, 2, 3), x248, (4, 5, 2, 6), (4, 5, 1, 3, 0, 6))
    x250 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x250 += einsum(t1.aa, (0, 1), x3, (2, 3, 0, 4), (2, 3, 1, 4))
    x251 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x251 += einsum(x121, (0, 1, 2, 3), (0, 1, 3, 2))
    x251 += einsum(x250, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x252 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x252 += einsum(t2.abab, (0, 1, 2, 3), x251, (4, 5, 2, 6), (4, 5, 1, 3, 0, 6))
    x253 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x253 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x253 += einsum(x126, (0, 1, 2, 3), (1, 0, 3, 2))
    x254 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x254 += einsum(t2.abab, (0, 1, 2, 3), x253, (4, 5, 0, 6), (4, 5, 1, 3, 6, 2))
    x255 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x255 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x255 += einsum(x25, (0, 1, 2, 3), (0, 1, 2, 3))
    x256 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x256 += einsum(t1.bb, (0, 1), x255, (2, 1, 3, 4), (2, 0, 3, 4))
    x257 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x257 += einsum(t2.abab, (0, 1, 2, 3), x256, (4, 5, 6, 0), (5, 4, 1, 3, 6, 2))
    x258 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x258 += einsum(x241, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x258 += einsum(x244, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x258 += einsum(x246, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    x258 += einsum(x249, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x258 += einsum(x252, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x258 += einsum(x254, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5)) * -1.0
    x258 += einsum(x257, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x259 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x259 += einsum(t1.bb, (0, 1), x258, (2, 0, 3, 4, 5, 6), (2, 3, 4, 1, 5, 6))
    x260 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x260 += einsum(v.bbbb.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x260 += einsum(x193, (0, 1, 2, 3), (2, 1, 0, 3))
    x261 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x261 += einsum(t2.abab, (0, 1, 2, 3), x260, (4, 1, 5, 6), (4, 5, 6, 3, 0, 2))
    x262 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x262 += einsum(f.aa.ov, (0, 1), t2.abab, (0, 2, 3, 4), (2, 4, 1, 3))
    x263 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x263 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x263 += einsum(x262, (0, 1, 2, 3), (0, 1, 2, 3))
    x263 += einsum(x106, (0, 1, 2, 3), (0, 1, 3, 2))
    x264 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x264 += einsum(t2.abab, (0, 1, 2, 3), x263, (4, 5, 2, 6), (4, 1, 5, 3, 0, 6))
    x265 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x265 += einsum(t1.bb, (0, 1), v.aabb.vvvv, (2, 3, 4, 1), (0, 4, 2, 3))
    x266 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x266 += einsum(t1.aa, (0, 1), x114, (2, 3, 0, 4), (2, 3, 1, 4))
    x267 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x267 += einsum(x265, (0, 1, 2, 3), (0, 1, 3, 2))
    x267 += einsum(x266, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x268 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x268 += einsum(t2.abab, (0, 1, 2, 3), x267, (4, 5, 2, 6), (4, 1, 5, 3, 0, 6))
    x269 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x269 += einsum(t2.abab, (0, 1, 2, 3), x26, (4, 5, 0, 6), (1, 4, 3, 5, 6, 2))
    x270 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x270 += einsum(t2.abab, (0, 1, 2, 3), x137, (4, 5, 6, 0), (4, 1, 5, 3, 6, 2))
    x271 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x271 += einsum(x237, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x271 += einsum(x238, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x271 += einsum(x259, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    x271 += einsum(x261, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x271 += einsum(x264, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x271 += einsum(x268, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x271 += einsum(x269, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x271 += einsum(x270, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    t3new_babbab += einsum(x271, (0, 1, 2, 3, 4, 5), (0, 4, 1, 2, 5, 3)) * -1.0
    t3new_babbab += einsum(x271, (0, 1, 2, 3, 4, 5), (0, 4, 1, 3, 5, 2))
    t3new_babbab += einsum(x271, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 5, 3))
    t3new_babbab += einsum(x271, (0, 1, 2, 3, 4, 5), (1, 4, 0, 3, 5, 2)) * -1.0
    x272 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x272 += einsum(f.bb.ov, (0, 1), t2.abab, (2, 3, 4, 1), (0, 3, 2, 4))
    x273 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x273 += einsum(t1.aa, (0, 1), x253, (2, 3, 0, 4), (2, 3, 4, 1))
    x274 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x274 += einsum(v.aabb.ovoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x274 += einsum(x272, (0, 1, 2, 3), (0, 1, 2, 3))
    x274 += einsum(x142, (0, 1, 2, 3), (1, 0, 2, 3))
    x274 += einsum(x273, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x275 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x275 += einsum(t2.bbbb, (0, 1, 2, 3), x274, (1, 4, 5, 6), (4, 0, 2, 3, 5, 6)) * -2.0
    x276 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x276 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x276 += einsum(x74, (0, 1, 2, 3), (0, 1, 2, 3))
    x277 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x277 += einsum(t1.bb, (0, 1), x276, (2, 1, 3, 4), (2, 0, 3, 4))
    x278 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x278 += einsum(t1.aa, (0, 1), x256, (2, 3, 4, 0), (3, 2, 4, 1))
    x279 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x279 += einsum(x277, (0, 1, 2, 3), (1, 0, 2, 3))
    x279 += einsum(x278, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x280 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x280 += einsum(t2.bbbb, (0, 1, 2, 3), x279, (4, 1, 5, 6), (4, 0, 2, 3, 5, 6)) * -2.0
    x281 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x281 += einsum(f.bb.ov, (0, 1), t1.bb, (2, 1), (0, 2))
    x282 = np.zeros((nocc[1], nocc[1]), dtype=np.float64)
    x282 += einsum(f.bb.oo, (0, 1), (0, 1))
    x282 += einsum(x281, (0, 1), (0, 1))
    t3new_abaaba = np.zeros((nocc[0], nocc[1], nocc[0], nvir[0], nvir[1], nvir[0]), dtype=np.float64)
    t3new_abaaba += einsum(x282, (0, 1), t3.abaaba, (2, 0, 3, 4, 5, 6), (2, 1, 3, 4, 5, 6)) * -2.0
    x283 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x283 += einsum(x282, (0, 1), t3.babbab, (2, 3, 0, 4, 5, 6), (1, 2, 4, 6, 3, 5)) * -2.0
    x284 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x284 += einsum(x275, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5)) * -1.0
    x284 += einsum(x280, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x284 += einsum(x283, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    t3new_babbab += einsum(x284, (0, 1, 2, 3, 4, 5), (0, 4, 1, 2, 5, 3))
    t3new_babbab += einsum(x284, (0, 1, 2, 3, 4, 5), (1, 4, 0, 2, 5, 3)) * -1.0
    x285 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x285 += einsum(f.bb.vv, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 1), (2, 4, 0, 5, 3, 6))
    x286 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x286 += einsum(f.bb.ov, (0, 1), t2.abab, (2, 0, 3, 4), (1, 4, 2, 3))
    x287 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x287 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x287 += einsum(x117, (0, 1, 2, 3), (1, 0, 3, 2))
    x288 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x288 += einsum(t1.aa, (0, 1), x287, (2, 3, 0, 4), (2, 3, 4, 1))
    x289 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x289 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x289 += einsum(x286, (0, 1, 2, 3), (0, 1, 2, 3))
    x289 += einsum(x140, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x289 += einsum(x288, (0, 1, 2, 3), (1, 0, 2, 3))
    x290 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x290 += einsum(t2.bbbb, (0, 1, 2, 3), x289, (3, 4, 5, 6), (0, 1, 4, 2, 5, 6)) * -2.0
    x291 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x291 += einsum(f.bb.ov, (0, 1), t3.babbab, (2, 3, 4, 5, 6, 1), (0, 2, 4, 5, 3, 6))
    x292 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x292 += einsum(t2.bbbb, (0, 1, 2, 3), x120, (4, 3, 5, 6), (0, 1, 4, 2, 5, 6)) * -1.0
    x293 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x293 += einsum(x291, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x293 += einsum(x292, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x294 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x294 += einsum(t1.bb, (0, 1), x293, (0, 2, 3, 4, 5, 6), (2, 3, 4, 1, 5, 6)) * 2.0
    x295 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x295 += einsum(x285, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x295 += einsum(x290, (0, 1, 2, 3, 4, 5), (1, 0, 3, 2, 4, 5))
    x295 += einsum(x294, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -1.0
    t3new_babbab += einsum(x295, (0, 1, 2, 3, 4, 5), (0, 4, 1, 2, 5, 3)) * -1.0
    t3new_babbab += einsum(x295, (0, 1, 2, 3, 4, 5), (0, 4, 1, 3, 5, 2))
    x296 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x296 += einsum(t2.abab, (0, 1, 2, 3), v.aaaa.ovvv, (4, 5, 6, 2), (1, 3, 0, 4, 5, 6))
    x297 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x297 += einsum(t2.abab, (0, 1, 2, 3), x35, (4, 5, 2, 6), (1, 3, 4, 0, 6, 5))
    x298 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x298 += einsum(t1.aa, (0, 1), v.aaaa.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x299 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x299 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x299 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x299 += einsum(x298, (0, 1, 2, 3), (1, 0, 2, 3))
    x300 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x300 += einsum(t2.abab, (0, 1, 2, 3), x299, (4, 5, 6, 2), (1, 3, 4, 5, 0, 6))
    x301 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x301 += einsum(t1.aa, (0, 1), x23, (2, 0, 3, 4), (2, 3, 1, 4))
    x302 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x302 += einsum(x301, (0, 1, 2, 3), (0, 1, 3, 2))
    x302 += einsum(x82, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x303 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x303 += einsum(t2.abab, (0, 1, 2, 3), x302, (4, 5, 2, 6), (1, 3, 4, 5, 0, 6))
    x304 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x304 += einsum(v.aaaa.oooo, (0, 1, 2, 3), (0, 1, 2, 3))
    x304 += einsum(x53, (0, 1, 2, 3), (3, 1, 0, 2))
    x304 += einsum(x62, (0, 1, 2, 3), (2, 1, 0, 3))
    x304 += einsum(x62, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x305 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x305 += einsum(t2.abab, (0, 1, 2, 3), x304, (0, 4, 5, 6), (1, 3, 4, 5, 6, 2))
    x306 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x306 += einsum(v.aabb.oovv, (0, 1, 2, 3), (2, 3, 0, 1))
    x306 += einsum(x116, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x307 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x307 += einsum(t2.abab, (0, 1, 2, 3), x306, (3, 4, 5, 6), (1, 4, 5, 6, 0, 2))
    x308 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x308 += einsum(t1.bb, (0, 1), x25, (0, 2, 3, 4), (1, 2, 3, 4))
    x309 = np.zeros((nvir[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x309 += einsum(x117, (0, 1, 2, 3), (1, 0, 2, 3))
    x309 += einsum(x308, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x310 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x310 += einsum(t2.abab, (0, 1, 2, 3), x309, (3, 4, 5, 6), (1, 4, 5, 6, 0, 2))
    x311 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x311 += einsum(v.aabb.oooo, (0, 1, 2, 3), (2, 3, 0, 1))
    x311 += einsum(x125, (0, 1, 2, 3), (1, 0, 3, 2))
    x312 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x312 += einsum(t2.abab, (0, 1, 2, 3), x311, (1, 4, 5, 6), (4, 3, 5, 6, 0, 2))
    x313 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x313 += einsum(t1.aa, (0, 1), x122, (2, 3, 4, 1), (2, 3, 0, 4))
    x314 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x314 += einsum(t2.abab, (0, 1, 2, 3), x313, (4, 1, 5, 6), (4, 3, 5, 6, 0, 2))
    x315 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x315 += einsum(x300, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5)) * -1.0
    x315 += einsum(x303, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x315 += einsum(x305, (0, 1, 2, 3, 4, 5), (0, 1, 3, 4, 2, 5))
    x315 += einsum(x307, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5))
    x315 += einsum(x310, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x315 += einsum(x312, (0, 1, 2, 3, 4, 5), (0, 1, 4, 3, 2, 5)) * -1.0
    x315 += einsum(x314, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x316 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x316 += einsum(t1.aa, (0, 1), x315, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1))
    x317 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x317 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 3, 1))
    x317 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x317 += einsum(x73, (0, 1, 2, 3), (0, 1, 2, 3))
    x318 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x318 += einsum(t1.aa, (0, 1), x317, (2, 3, 1, 4), (2, 3, 0, 4))
    x319 = np.zeros((nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x319 += einsum(v.aaaa.ooov, (0, 1, 2, 3), (0, 1, 2, 3))
    x319 += einsum(x318, (0, 1, 2, 3), (2, 1, 0, 3))
    x320 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x320 += einsum(t2.abab, (0, 1, 2, 3), x319, (4, 0, 5, 6), (1, 3, 4, 5, 6, 2))
    x321 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x321 += einsum(v.aabb.ovvv, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x321 += einsum(x286, (0, 1, 2, 3), (0, 1, 2, 3))
    x321 += einsum(x103, (0, 1, 2, 3), (1, 0, 2, 3))
    x322 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x322 += einsum(t2.abab, (0, 1, 2, 3), x321, (3, 4, 5, 6), (1, 4, 5, 0, 6, 2))
    x323 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x323 += einsum(t1.bb, (0, 1), x74, (0, 2, 3, 4), (1, 2, 3, 4))
    x324 = np.zeros((nvir[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x324 += einsum(x140, (0, 1, 2, 3), (1, 0, 2, 3))
    x324 += einsum(x323, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x325 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x325 += einsum(t2.abab, (0, 1, 2, 3), x324, (3, 4, 5, 6), (1, 4, 5, 0, 6, 2))
    x326 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x326 += einsum(t2.abab, (0, 1, 2, 3), x4, (1, 4, 5, 6), (4, 3, 0, 5, 2, 6))
    x327 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x327 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x327 += einsum(x121, (0, 1, 2, 3), (0, 1, 3, 2))
    x328 = np.zeros((nocc[1], nocc[1], nocc[0], nvir[0]), dtype=np.float64)
    x328 += einsum(t1.aa, (0, 1), x327, (2, 3, 1, 4), (2, 3, 0, 4))
    x329 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x329 += einsum(t2.abab, (0, 1, 2, 3), x328, (4, 1, 5, 6), (4, 3, 5, 0, 6, 2))
    x330 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x330 += einsum(x296, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x330 += einsum(x297, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    x330 += einsum(x316, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    x330 += einsum(x320, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x330 += einsum(x322, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x330 += einsum(x325, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x330 += einsum(x326, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5))
    x330 += einsum(x329, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -1.0
    t3new_abaaba += einsum(x330, (0, 1, 2, 3, 4, 5), (2, 0, 3, 4, 1, 5)) * -1.0
    t3new_abaaba += einsum(x330, (0, 1, 2, 3, 4, 5), (2, 0, 3, 5, 1, 4))
    t3new_abaaba += einsum(x330, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5))
    t3new_abaaba += einsum(x330, (0, 1, 2, 3, 4, 5), (3, 0, 2, 5, 1, 4)) * -1.0
    x331 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x331 += einsum(t1.bb, (0, 1), v.aabb.oovv, (2, 3, 4, 1), (0, 4, 2, 3))
    x332 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x332 += einsum(f.aa.ov, (0, 1), t2.abab, (2, 3, 1, 4), (3, 4, 0, 2))
    x333 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x333 += einsum(t1.bb, (0, 1), x311, (0, 2, 3, 4), (2, 1, 3, 4))
    x334 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x334 += einsum(v.aabb.ooov, (0, 1, 2, 3), (2, 3, 0, 1))
    x334 += einsum(x331, (0, 1, 2, 3), (0, 1, 3, 2))
    x334 += einsum(x332, (0, 1, 2, 3), (0, 1, 2, 3))
    x334 += einsum(x333, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x335 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x335 += einsum(t2.aaaa, (0, 1, 2, 3), x334, (4, 5, 1, 6), (4, 5, 6, 0, 2, 3)) * -2.0
    x336 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x336 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x336 += einsum(x114, (0, 1, 2, 3), (0, 1, 2, 3))
    x337 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x337 += einsum(t1.aa, (0, 1), x336, (2, 3, 4, 1), (2, 3, 4, 0))
    x338 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x338 += einsum(t1.bb, (0, 1), x313, (2, 0, 3, 4), (2, 1, 3, 4))
    x339 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0]), dtype=np.float64)
    x339 += einsum(x337, (0, 1, 2, 3), (0, 1, 3, 2))
    x339 += einsum(x338, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x340 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x340 += einsum(t2.aaaa, (0, 1, 2, 3), x339, (4, 5, 6, 1), (4, 5, 6, 0, 2, 3)) * -2.0
    x341 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x341 += einsum(x230, (0, 1), t3.abaaba, (2, 3, 0, 4, 5, 6), (3, 5, 1, 2, 4, 6)) * -2.0
    x342 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x342 += einsum(x335, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x342 += einsum(x340, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    x342 += einsum(x341, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_abaaba += einsum(x342, (0, 1, 2, 3, 4, 5), (2, 0, 3, 4, 1, 5))
    t3new_abaaba += einsum(x342, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5)) * -1.0
    x343 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x343 += einsum(f.aa.vv, (0, 1), t3.abaaba, (2, 3, 4, 5, 6, 1), (3, 6, 2, 4, 0, 5))
    x344 = np.zeros((nocc[1], nocc[1], nvir[0], nvir[0]), dtype=np.float64)
    x344 += einsum(v.aabb.vvoo, (0, 1, 2, 3), (2, 3, 0, 1))
    x344 += einsum(x121, (0, 1, 2, 3), (1, 0, 3, 2))
    x345 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x345 += einsum(t1.bb, (0, 1), x344, (0, 2, 3, 4), (2, 1, 3, 4))
    x346 = np.zeros((nocc[1], nvir[1], nvir[0], nvir[0]), dtype=np.float64)
    x346 += einsum(v.aabb.vvov, (0, 1, 2, 3), (2, 3, 0, 1)) * -1.0
    x346 += einsum(x262, (0, 1, 2, 3), (0, 1, 2, 3))
    x346 += einsum(x265, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x346 += einsum(x345, (0, 1, 2, 3), (0, 1, 3, 2))
    x347 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x347 += einsum(t2.aaaa, (0, 1, 2, 3), x346, (4, 5, 3, 6), (4, 5, 0, 1, 6, 2)) * -2.0
    x348 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x348 += einsum(f.aa.ov, (0, 1), t3.abaaba, (2, 3, 4, 5, 6, 1), (3, 6, 0, 2, 4, 5))
    x349 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x349 += einsum(t1.bb, (0, 1), x4, (0, 2, 3, 4), (2, 1, 3, 4))
    x350 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x350 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x350 += einsum(x114, (0, 1, 2, 3), (0, 1, 2, 3))
    x350 += einsum(x349, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x351 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x351 += einsum(t2.aaaa, (0, 1, 2, 3), x350, (4, 5, 6, 3), (4, 5, 6, 0, 1, 2)) * -1.0
    x352 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nocc[0], nvir[0]), dtype=np.float64)
    x352 += einsum(x348, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -1.0
    x352 += einsum(x351, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    x353 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x353 += einsum(t1.aa, (0, 1), x352, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x354 = np.zeros((nocc[1], nvir[1], nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x354 += einsum(x343, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5)) * -2.0
    x354 += einsum(x347, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    x354 += einsum(x353, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4))
    t3new_abaaba += einsum(x354, (0, 1, 2, 3, 4, 5), (3, 0, 2, 4, 1, 5))
    t3new_abaaba += einsum(x354, (0, 1, 2, 3, 4, 5), (3, 0, 2, 5, 1, 4)) * -1.0
    x355 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x355 += einsum(f.bb.ov, (0, 1), t1.bb, (0, 2), (1, 2))
    x356 = np.zeros((nvir[1], nvir[1]), dtype=np.float64)
    x356 += einsum(f.bb.vv, (0, 1), (0, 1))
    x356 += einsum(x355, (0, 1), (0, 1)) * -1.0
    t3new_abaaba += einsum(x356, (0, 1), t3.abaaba, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6)) * 2.0
    x357 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x357 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 1, 5, 6), (0, 4, 5, 2, 3, 6))
    x358 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x358 += einsum(t1.bb, (0, 1), x177, (2, 3, 1, 4), (0, 2, 3, 4))
    x359 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x359 += einsum(t2.bbbb, (0, 1, 2, 3), x358, (4, 5, 1, 6), (4, 5, 0, 2, 3, 6))
    x360 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x360 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x360 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 3, 1)) * -1.0
    x361 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x361 += einsum(t1.bb, (0, 1), x360, (2, 3, 1, 4), (2, 3, 0, 4))
    x362 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x362 += einsum(t2.bbbb, (0, 1, 2, 3), x361, (4, 1, 5, 6), (5, 4, 0, 6, 2, 3)) * -2.0
    x363 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x363 += einsum(x357, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x363 += einsum(x359, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5)) * -2.0
    x363 += einsum(x362, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3))
    t3new_bbbbbb = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 4, 5))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (1, 0, 2, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 3, 4))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 5, 4))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x363, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    x364 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x364 += einsum(x282, (0, 1), t3.bbbbbb, (2, 3, 0, 4, 5, 6), (1, 2, 3, 4, 5, 6)) * 6.0
    t3new_bbbbbb += einsum(x364, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x364, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x364, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    x365 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x365 += einsum(t2.bbbb, (0, 1, 2, 3), x156, (4, 5, 3, 6), (4, 0, 1, 2, 6, 5))
    x366 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x366 += einsum(t2.bbbb, (0, 1, 2, 3), x1, (4, 5, 6, 3), (4, 0, 1, 6, 5, 2))
    x367 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x367 += einsum(t1.bb, (0, 1), x366, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x368 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x368 += einsum(t2.bbbb, (0, 1, 2, 3), x183, (4, 5, 3, 6), (5, 4, 0, 1, 6, 2))
    x369 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x369 += einsum(x367, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -1.0
    x369 += einsum(x368, (0, 1, 2, 3, 4, 5), (0, 3, 2, 1, 5, 4)) * -1.0
    x370 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x370 += einsum(t1.bb, (0, 1), x369, (2, 3, 4, 0, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x371 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x371 += einsum(x365, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5)) * -2.0
    x371 += einsum(x370, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 0, 1, 3, 5, 4))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_bbbbbb += einsum(x371, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x372 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x372 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.oooo, (4, 5, 6, 1), (0, 4, 5, 6, 2, 3))
    x373 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x373 += einsum(t2.bbbb, (0, 1, 2, 3), x171, (4, 5, 1, 6), (5, 4, 0, 6, 2, 3))
    x374 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x374 += einsum(x146, (0, 1, 2, 3), (0, 2, 1, 3))
    x374 += einsum(x146, (0, 1, 2, 3), (0, 3, 2, 1)) * -1.0
    x375 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x375 += einsum(t2.bbbb, (0, 1, 2, 3), x374, (4, 1, 5, 6), (4, 5, 6, 0, 2, 3)) * -1.0
    x376 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x376 += einsum(x372, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    x376 += einsum(x373, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 5, 4)) * -1.0
    x376 += einsum(x375, (0, 1, 2, 3, 4, 5), (0, 3, 2, 1, 5, 4)) * -1.0
    x377 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x377 += einsum(t1.bb, (0, 1), x376, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 5, 3))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (2, 0, 1, 5, 4, 3))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (2, 0, 1, 4, 3, 5))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (1, 2, 0, 5, 4, 3))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_bbbbbb += einsum(x377, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    x378 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x378 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ovvv, (4, 5, 6, 3), (0, 1, 4, 2, 5, 6))
    x379 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x379 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.ooov, (4, 5, 6, 3), (0, 1, 4, 5, 6, 2))
    x380 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x380 += einsum(t1.bb, (0, 1), x379, (2, 3, 4, 5, 0, 6), (2, 3, 4, 5, 1, 6))
    x381 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x381 += einsum(t2.bbbb, (0, 1, 2, 3), x360, (4, 5, 3, 6), (4, 5, 0, 1, 6, 2)) * -1.0
    x382 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x382 += einsum(x380, (0, 1, 2, 3, 4, 5), (0, 1, 3, 2, 4, 5))
    x382 += einsum(x381, (0, 1, 2, 3, 4, 5), (3, 2, 1, 0, 5, 4))
    x383 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x383 += einsum(t1.bb, (0, 1), x382, (2, 3, 0, 4, 5, 6), (2, 3, 4, 5, 6, 1)) * 2.0
    x384 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x384 += einsum(x378, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * 2.0
    x384 += einsum(x383, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 4, 5)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 3, 5))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 1, 2, 4, 5, 3)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 4, 5))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 5, 3))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (2, 1, 0, 4, 5, 3))
    t3new_bbbbbb += einsum(x384, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * -1.0
    x385 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x385 += einsum(x356, (0, 1), t3.bbbbbb, (2, 3, 4, 5, 6, 0), (2, 3, 4, 1, 5, 6)) * 6.0
    t3new_bbbbbb += einsum(x385, (0, 1, 2, 3, 4, 5), (1, 2, 0, 3, 4, 5))
    t3new_bbbbbb += einsum(x385, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -1.0
    t3new_bbbbbb += einsum(x385, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 5, 3))
    x386 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1]), dtype=np.float64)
    x386 += einsum(f.bb.ov, (0, 1), t2.bbbb, (2, 3, 4, 1), (0, 2, 3, 4))
    x387 = np.zeros((nocc[1], nocc[1], nocc[1], nvir[1], nvir[1], nvir[1]), dtype=np.float64)
    x387 += einsum(t2.bbbb, (0, 1, 2, 3), x386, (1, 4, 5, 6), (5, 4, 0, 6, 2, 3)) * -1.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * 4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 4, 3)) * -4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * -4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * 4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * 4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 3, 4)) * -4.0
    t3new_bbbbbb += einsum(x387, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * 4.0

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

