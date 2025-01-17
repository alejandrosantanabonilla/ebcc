# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, direct_sum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(f.ov, (0, 1), t1, (0, 1), ())
    x0 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    e_cc += einsum(x0, (0, 1, 2, 3), v.oovv, (0, 1, 2, 3), ()) * 0.25

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, **kwargs):
    # T amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum(v.ovov, (0, 1, 2, 3), t1, (2, 1), (0, 3)) * -1.0
    t1new += einsum(f.vv, (0, 1), t1, (2, 1), (2, 0))
    t1new += einsum(f.ov, (0, 1), (0, 1))
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x0 += einsum(v.oovv, (0, 1, 2, 3), t1, (4, 3), (4, 0, 1, 2))
    x1 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x1 += einsum(v.ooov, (0, 1, 2, 3), (2, 1, 0, 3))
    x1 += einsum(x0, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    t1new += einsum(x1, (0, 1, 2, 3), t2, (1, 2, 3, 4), (0, 4)) * -0.5
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    x2 += einsum(t1, (0, 1), t1, (2, 3), (0, 2, 1, 3)) * 2.0
    t1new += einsum(x2, (0, 1, 2, 3), v.ovvv, (0, 4, 2, 3), (1, 4)) * 0.5
    t2new += einsum(x2, (0, 1, 2, 3), v.vvvv, (2, 3, 4, 5), (1, 0, 4, 5)) * -0.5
    x3 = np.zeros((nocc, nvir), dtype=np.float64)
    x3 += einsum(v.oovv, (0, 1, 2, 3), t1, (1, 3), (0, 2))
    x4 = np.zeros((nocc, nvir), dtype=np.float64)
    x4 += einsum(f.ov, (0, 1), (0, 1))
    x4 += einsum(x3, (0, 1), (0, 1))
    t1new += einsum(x4, (0, 1), t2, (0, 2, 1, 3), (2, 3))
    x5 = np.zeros((nocc, nocc), dtype=np.float64)
    x5 += einsum(t1, (0, 1), v.ooov, (0, 2, 3, 1), (2, 3)) * -1.0
    x6 = np.zeros((nocc, nocc), dtype=np.float64)
    x6 += einsum(f.oo, (0, 1), (1, 0))
    x6 += einsum(f.ov, (0, 1), t1, (2, 1), (0, 2))
    x6 += einsum(x5, (0, 1), (0, 1))
    x6 += einsum(v.oovv, (0, 1, 2, 3), x2, (0, 4, 2, 3), (1, 4)) * 0.5
    t1new += einsum(x6, (0, 1), t1, (0, 2), (1, 2)) * -1.0
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 0, 5, 2), (4, 1, 5, 3))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(t2, (0, 1, 2, 3), x7, (4, 1, 5, 3), (4, 0, 5, 2))
    x9 = np.zeros((nvir, nvir), dtype=np.float64)
    x9 += einsum(t1, (0, 1), v.ovvv, (0, 2, 1, 3), (2, 3)) * -1.0
    x10 = np.zeros((nvir, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 3, 4), (2, 4)) * -1.0
    x11 = np.zeros((nvir, nvir), dtype=np.float64)
    x11 += einsum(x9, (0, 1), (0, 1))
    x11 += einsum(x10, (0, 1), (0, 1)) * 0.5
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(x11, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    x13 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum(x2, (0, 1, 2, 3), v.ovvv, (4, 5, 2, 3), (4, 0, 1, 5)) * 0.5
    x14 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x14 += einsum(x4, (0, 1), t2, (2, 3, 1, 4), (2, 3, 0, 4))
    x15 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x15 += einsum(x13, (0, 1, 2, 3), (0, 2, 1, 3))
    x15 += einsum(x14, (0, 1, 2, 3), (2, 1, 0, 3))
    x16 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x16 += einsum(x15, (0, 1, 2, 3), t1, (0, 4), (1, 2, 3, 4))
    x17 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x17 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x17 += einsum(x12, (0, 1, 2, 3), (1, 0, 3, 2))
    x17 += einsum(x16, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x17, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x17, (0, 1, 2, 3), (0, 1, 3, 2))
    x18 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x18 += einsum(v.ovvv, (0, 1, 2, 3), t1, (4, 1), (4, 0, 2, 3))
    x19 = np.zeros((nocc, nocc), dtype=np.float64)
    x19 += einsum(t1, (0, 1), x4, (2, 1), (0, 2))
    x20 = np.zeros((nocc, nocc), dtype=np.float64)
    x20 += einsum(f.oo, (0, 1), (1, 0))
    x20 += einsum(x19, (0, 1), (0, 1))
    x21 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x21 += einsum(x20, (0, 1), t2, (1, 2, 3, 4), (0, 2, 3, 4))
    x22 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x22 += einsum(t1, (0, 1), v.ooov, (2, 3, 4, 1), (0, 2, 3, 4))
    x23 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x23 += einsum(x22, (0, 1, 2, 3), x2, (1, 2, 4, 5), (0, 3, 4, 5)) * 0.5
    x24 = np.zeros((nocc, nocc), dtype=np.float64)
    x24 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 0, 2, 3), (4, 1)) * -1.0
    x25 = np.zeros((nocc, nocc), dtype=np.float64)
    x25 += einsum(x5, (0, 1), (0, 1))
    x25 += einsum(x24, (0, 1), (1, 0)) * 0.5
    x26 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x26 += einsum(t2, (0, 1, 2, 3), x25, (0, 4), (4, 1, 2, 3))
    x27 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x27 += einsum(x18, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x27 += einsum(x21, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x27 += einsum(x23, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x27 += einsum(x26, (0, 1, 2, 3), (1, 0, 3, 2))
    t2new += einsum(x27, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x27, (0, 1, 2, 3), (1, 0, 2, 3))
    x28 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x28 += einsum(v.ovov, (0, 1, 2, 3), t2, (4, 2, 5, 1), (4, 0, 5, 3))
    x29 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x29 += einsum(t1, (0, 1), v.ovvv, (2, 3, 4, 1), (0, 2, 3, 4))
    x30 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x30 += einsum(t2, (0, 1, 2, 3), x29, (4, 1, 5, 3), (4, 0, 2, 5)) * -1.0
    x31 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x31 += einsum(v.ovov, (0, 1, 2, 3), t1, (4, 1), (4, 2, 0, 3))
    x32 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x32 += einsum(t2, (0, 1, 2, 3), v.ooov, (1, 4, 5, 3), (0, 4, 5, 2)) * -1.0
    x33 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x33 += einsum(x0, (0, 1, 2, 3), t2, (4, 1, 5, 3), (0, 4, 2, 5))
    x34 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x34 += einsum(x31, (0, 1, 2, 3), (0, 1, 2, 3))
    x34 += einsum(x32, (0, 1, 2, 3), (0, 1, 2, 3))
    x34 += einsum(x33, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x35 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x35 += einsum(x34, (0, 1, 2, 3), t1, (1, 4), (0, 2, 3, 4))
    x36 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x36 += einsum(x28, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    x36 += einsum(x30, (0, 1, 2, 3), (0, 1, 2, 3))
    x36 += einsum(x35, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x36, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x36, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    t2new += einsum(x36, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x36, (0, 1, 2, 3), (1, 0, 3, 2))
    x37 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x37 += einsum(t1, (0, 1), v.ooov, (2, 3, 0, 4), (2, 3, 1, 4))
    x38 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x38 += einsum(t2, (0, 1, 2, 3), f.vv, (4, 3), (0, 1, 4, 2))
    x39 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x39 += einsum(x37, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x39 += einsum(x38, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    t2new += einsum(x39, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x39, (0, 1, 2, 3), (0, 1, 3, 2))
    x40 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x40 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x40 += einsum(v.oovv, (0, 1, 2, 3), x2, (4, 5, 2, 3), (1, 0, 5, 4))
    t2new += einsum(x40, (0, 1, 2, 3), x2, (0, 1, 4, 5), (2, 3, 5, 4)) * -0.25

    return {"t1new": t1new, "t2new": t2new}

def energy_perturbative(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, l1=None, l2=None, **kwargs):
    e_ia = direct_sum("i-a->ia", np.diag(f.oo), np.diag(f.vv))
    denom3 = 1 / direct_sum("ia+jb+kc->ijkabc", e_ia, e_ia, e_ia)

    # energy
    x0 = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    x0 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 4, 5), denom3, (0, 6, 1, 4, 5, 3), l1, (3, 6), (6, 5, 4, 2)) * -1.0
    e_pert = 0
    e_pert += einsum(v.ovvv, (0, 1, 2, 3), x0, (0, 2, 3, 1), ()) * 0.25
    x1 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x1 += einsum(v.ovvv, (0, 1, 2, 3), l2, (4, 1, 5, 6), (6, 5, 0, 4, 2, 3)) * -1.0
    x2 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x2 += einsum(denom3, (0, 1, 2, 3, 4, 5), x1, (1, 2, 0, 4, 3, 5), t2, (2, 6, 4, 5), (1, 0, 6, 3)) * -1.0
    e_pert += einsum(v.ooov, (0, 1, 2, 3), x2, (1, 0, 2, 3), ())
    x3 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x3 += einsum(l1, (0, 1), v.oovv, (2, 3, 4, 5), (1, 3, 2, 0, 5, 4)) * -1.0
    x3 += einsum(x1, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4))
    x3 += einsum(x1, (0, 1, 2, 3, 4, 5), (0, 2, 1, 3, 5, 4)) * 0.5
    x3 += einsum(x1, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * 0.25
    x3 += einsum(x1, (0, 1, 2, 3, 4, 5), (2, 1, 0, 5, 4, 3)) * 0.5
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(denom3, (0, 1, 2, 3, 4, 5), v.ooov, (0, 2, 6, 3), v.oovv, (0, 2, 3, 4), (1, 6, 4, 5)) * -1.0
    x4 += einsum(v.oovv, (0, 1, 2, 3), denom3, (0, 1, 4, 2, 5, 3), v.ovvv, (0, 6, 2, 3), (4, 1, 6, 5)) * -1.0
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(v.ovvv, (0, 1, 2, 3), denom3, (4, 0, 5, 6, 3, 2), x3, (5, 0, 4, 3, 2, 6), (4, 5, 6, 1))
    x5 += einsum(l1, (0, 1), x4, (1, 2, 3, 0), (1, 2, 0, 3)) * 0.5
    e_pert += einsum(x5, (0, 1, 2, 3), t2, (0, 1, 2, 3), ()) * -1.0
    x6 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x6 += einsum(denom3, (0, 1, 2, 3, 4, 5), v.oovv, (0, 1, 3, 5), t2, (0, 6, 3, 5), (1, 2, 6, 4))
    x7 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir, nvir, nvir), dtype=np.float64)
    x7 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 6, 7), (3, 2, 5, 4, 1, 0, 7, 6))
    x7 += einsum(t2, (0, 1, 2, 3), l2, (4, 5, 6, 7), (0, 1, 6, 7, 3, 2, 5, 4))
    x8 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x8 += einsum(t2, (0, 1, 2, 3), v.ooov, (4, 5, 1, 6), (0, 5, 4, 2, 3, 6)) * -1.0
    x9 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x9 += einsum(v.ovvv, (0, 1, 2, 3), t2, (4, 5, 6, 1), (4, 5, 0, 6, 3, 2)) * -1.0
    x10 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x10 += einsum(x8, (0, 1, 2, 3, 4, 5), (0, 2, 1, 4, 3, 5)) * -1.0
    x10 += einsum(x8, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -2.0
    x10 += einsum(x8, (0, 1, 2, 3, 4, 5), (1, 0, 2, 4, 3, 5)) * -2.0
    x10 += einsum(x9, (0, 1, 2, 3, 4, 5), (0, 1, 2, 5, 3, 4)) * -4.0
    x10 += einsum(x9, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 4, 3)) * -2.0
    x10 += einsum(x9, (0, 1, 2, 3, 4, 5), (2, 1, 0, 3, 5, 4)) * -2.0
    x11 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x11 += einsum(l2, (0, 1, 2, 3), v.ooov, (4, 5, 3, 6), (2, 4, 5, 1, 0, 6))
    x11 += einsum(x1, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * 0.5
    x11 += einsum(x1, (0, 1, 2, 3, 4, 5), (0, 2, 1, 5, 3, 4)) * 0.5
    x12 = np.zeros((nocc, nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x12 += einsum(l2, (0, 1, 2, 3), x10, (3, 4, 5, 0, 1, 6), (3, 2, 5, 4, 1, 0, 6)) * -0.5
    x12 += einsum(t2, (0, 1, 2, 3), x11, (4, 1, 5, 6, 2, 3), (1, 0, 4, 5, 3, 2, 6)) * -2.0
    x13 = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    x13 += einsum(l1, (0, 1), x6, (2, 1, 3, 0), (1, 2, 3, 0))
    x13 += einsum(x7, (0, 1, 2, 3, 4, 5, 6, 7), denom3, (0, 2, 1, 5, 7, 6), v.ovvv, (2, 4, 6, 7), (0, 1, 3, 5)) * -0.5
    x13 += einsum(x12, (0, 1, 2, 3, 4, 5, 6), denom3, (0, 2, 3, 4, 6, 5), (2, 3, 1, 6))
    e_pert += einsum(v.ooov, (0, 1, 2, 3), x13, (0, 1, 2, 3), ()) * 0.5
    x14 = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    x14 += einsum(x9, (0, 1, 2, 3, 4, 5), (0, 1, 2, 3, 5, 4)) * -0.5
    x14 += einsum(x8, (0, 1, 2, 3, 4, 5), (1, 0, 2, 5, 4, 3))
    x14 += einsum(x8, (0, 1, 2, 3, 4, 5), (1, 2, 0, 4, 3, 5)) * -0.25
    x15 = np.zeros((nocc, nvir), dtype=np.float64)
    x15 += einsum(denom3, (0, 1, 2, 3, 4, 5), v.oovv, (0, 2, 3, 4), x14, (0, 2, 1, 4, 3, 5), (1, 5)) * 2.0
    e_pert += einsum(l1, (0, 1), x15, (1, 0), ()) * 0.5

    return e_pert

