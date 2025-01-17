# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t2=None, **kwargs):
    # energy
    e_cc = 0
    e_cc += einsum(v.oovv, (0, 1, 2, 3), t2, (0, 1, 2, 3), ()) * 0.25

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t2=None, **kwargs):
    # T amplitudes
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum(v.vvvv, (0, 1, 2, 3), t2, (4, 5, 3, 2), (5, 4, 1, 0)) * -0.5
    t2new += einsum(v.oovv, (0, 1, 2, 3), (1, 0, 3, 2))
    x0 = np.zeros((nvir, nvir), dtype=np.float64)
    x0 += einsum(v.oovv, (0, 1, 2, 3), t2, (0, 1, 4, 2), (4, 3)) * -1.0
    x1 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), x0, (4, 3), (0, 1, 2, 4))
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 1, 5, 3), (0, 4, 2, 5))
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(t2, (0, 1, 2, 3), x2, (4, 1, 5, 3), (0, 4, 2, 5))
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(x1, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x4 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x4, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(t2, (0, 1, 2, 3), f.oo, (4, 1), (4, 0, 2, 3))
    x6 = np.zeros((nocc, nocc), dtype=np.float64)
    x6 += einsum(t2, (0, 1, 2, 3), v.oovv, (1, 4, 2, 3), (0, 4)) * -1.0
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(x6, (0, 1), t2, (2, 1, 3, 4), (2, 0, 3, 4))
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(x5, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x8 += einsum(x7, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    t2new += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3))
    t2new += einsum(x8, (0, 1, 2, 3), (1, 0, 2, 3)) * -1.0
    x9 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x9 += einsum(f.vv, (0, 1), t2, (2, 3, 4, 1), (2, 3, 0, 4))
    t2new += einsum(x9, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new += einsum(x9, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(t2, (0, 1, 2, 3), v.ovov, (4, 3, 1, 5), (0, 4, 2, 5))
    t2new += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * -1.0
    t2new += einsum(x10, (0, 1, 2, 3), (0, 1, 3, 2))
    t2new += einsum(x10, (0, 1, 2, 3), (1, 0, 2, 3))
    t2new += einsum(x10, (0, 1, 2, 3), (1, 0, 3, 2)) * -1.0
    x11 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x11 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x11 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 5, 2, 3), (5, 4, 1, 0))
    t2new += einsum(x11, (0, 1, 2, 3), t2, (0, 1, 4, 5), (2, 3, 5, 4)) * -0.25

    return {"t2new": t2new}

def update_lams(f=None, v=None, nocc=None, nvir=None, t2=None, l2=None, **kwargs):
    # L amplitudes
    l2new = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    l2new += einsum(l2, (0, 1, 2, 3), v.vvvv, (4, 5, 1, 0), (5, 4, 3, 2)) * -0.5
    l2new += einsum(v.oovv, (0, 1, 2, 3), (3, 2, 1, 0))
    x0 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x0 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    l2new += einsum(v.oovv, (0, 1, 2, 3), x0, (4, 5, 0, 1), (2, 3, 4, 5)) * 0.25
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), v.oovv, (4, 0, 2, 3), (1, 4)) * -1.0
    x2 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x2 += einsum(l2, (0, 1, 2, 3), x1, (3, 4), (2, 4, 0, 1))
    x3 = np.zeros((nocc, nocc), dtype=np.float64)
    x3 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 0), (4, 1)) * -1.0
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(v.oovv, (0, 1, 2, 3), x3, (4, 1), (4, 0, 2, 3)) * -1.0
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(x2, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    x5 += einsum(x4, (0, 1, 2, 3), (0, 1, 3, 2)) * -0.5
    l2new += einsum(x5, (0, 1, 2, 3), (3, 2, 0, 1))
    l2new += einsum(x5, (0, 1, 2, 3), (3, 2, 1, 0)) * -1.0
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(f.vv, (0, 1), l2, (2, 1, 3, 4), (3, 4, 0, 2))
    x7 = np.zeros((nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), v.oovv, (0, 1, 4, 2), (3, 4)) * -1.0
    x8 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x8 += einsum(x7, (0, 1), l2, (2, 0, 3, 4), (3, 4, 2, 1))
    x9 = np.zeros((nvir, nvir), dtype=np.float64)
    x9 += einsum(t2, (0, 1, 2, 3), l2, (4, 2, 0, 1), (4, 3)) * -1.0
    x10 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x10 += einsum(x9, (0, 1), v.oovv, (2, 3, 4, 1), (2, 3, 0, 4)) * -1.0
    x11 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x11 += einsum(x6, (0, 1, 2, 3), (1, 0, 2, 3))
    x11 += einsum(x8, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x11 += einsum(x10, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    l2new += einsum(x11, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x11, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    x12 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x12 += einsum(v.oovv, (0, 1, 2, 3), t2, (1, 4, 3, 5), (4, 0, 5, 2))
    x13 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x13 += einsum(v.ovov, (0, 1, 2, 3), (2, 0, 1, 3)) * -1.0
    x13 += einsum(x12, (0, 1, 2, 3), (0, 1, 2, 3))
    x14 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x14 += einsum(x13, (0, 1, 2, 3), l2, (2, 4, 0, 5), (5, 1, 4, 3))
    l2new += einsum(x14, (0, 1, 2, 3), (2, 3, 0, 1))
    l2new += einsum(x14, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x14, (0, 1, 2, 3), (2, 3, 1, 0)) * -1.0
    l2new += einsum(x14, (0, 1, 2, 3), (3, 2, 1, 0))
    x15 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x15 += einsum(f.oo, (0, 1), l2, (2, 3, 4, 1), (0, 4, 2, 3))
    l2new += einsum(x15, (0, 1, 2, 3), (3, 2, 0, 1)) * -1.0
    l2new += einsum(x15, (0, 1, 2, 3), (3, 2, 1, 0))
    x16 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x16 += einsum(v.oooo, (0, 1, 2, 3), (2, 3, 1, 0)) * -2.0
    x16 += einsum(v.oovv, (0, 1, 2, 3), t2, (4, 5, 2, 3), (5, 4, 1, 0))
    l2new += einsum(l2, (0, 1, 2, 3), x16, (2, 3, 4, 5), (1, 0, 4, 5)) * -0.25

    return {"l2new": l2new}

def make_rdm1_f(f=None, v=None, nocc=None, nvir=None, t2=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM1
    rdm1_f_oo = np.zeros((nocc, nocc), dtype=np.float64)
    rdm1_f_oo += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 1), (0, 4)) * -0.5
    rdm1_f_oo += einsum(delta.oo, (0, 1), (1, 0))
    rdm1_f_vv = np.zeros((nvir, nvir), dtype=np.float64)
    rdm1_f_vv += einsum(t2, (0, 1, 2, 3), l2, (4, 3, 0, 1), (4, 2)) * 0.5
    rdm1_f_ov = np.zeros((nocc, nvir), dtype=np.float64)
    rdm1_f_vo = np.zeros((nvir, nocc), dtype=np.float64)

    rdm1_f = np.block([[rdm1_f_oo, rdm1_f_ov], [rdm1_f_vo, rdm1_f_vv]])

    return rdm1_f

def make_rdm2_f(f=None, v=None, nocc=None, nvir=None, t2=None, l2=None, **kwargs):
    delta = Namespace(oo=np.eye(nocc), vv=np.eye(nvir))

    # RDM2
    rdm2_f_oooo = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 1, 2, 0))
    rdm2_f_oooo += einsum(delta.oo, (0, 1), delta.oo, (2, 3), (3, 0, 1, 2)) * -1.0
    rdm2_f_oovv = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvoo = np.zeros((nvir, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vvoo += einsum(l2, (0, 1, 2, 3), (1, 0, 3, 2))
    rdm2_f_vvvv = np.zeros((nvir, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vvvv += einsum(t2, (0, 1, 2, 3), l2, (4, 5, 0, 1), (5, 4, 3, 2)) * 0.5
    x0 = np.zeros((nocc, nocc, nocc, nocc), dtype=np.float64)
    x0 += einsum(l2, (0, 1, 2, 3), t2, (4, 5, 0, 1), (2, 3, 4, 5))
    rdm2_f_oooo += einsum(x0, (0, 1, 2, 3), (3, 2, 1, 0)) * 0.5
    rdm2_f_oovv += einsum(t2, (0, 1, 2, 3), x0, (0, 1, 4, 5), (5, 4, 3, 2)) * 0.25
    x1 = np.zeros((nocc, nocc), dtype=np.float64)
    x1 += einsum(t2, (0, 1, 2, 3), l2, (2, 3, 4, 1), (4, 0))
    rdm2_f_oooo += einsum(x1, (0, 1), delta.oo, (2, 3), (2, 1, 3, 0)) * -0.5
    rdm2_f_oooo += einsum(x1, (0, 1), delta.oo, (2, 3), (2, 1, 0, 3)) * 0.5
    rdm2_f_oooo += einsum(x1, (0, 1), delta.oo, (2, 3), (1, 3, 2, 0)) * 0.5
    rdm2_f_oooo += einsum(x1, (0, 1), delta.oo, (2, 3), (1, 3, 0, 2)) * -0.5
    x2 = np.zeros((nvir, nvir), dtype=np.float64)
    x2 += einsum(t2, (0, 1, 2, 3), l2, (3, 4, 0, 1), (4, 2)) * -1.0
    rdm2_f_ovov = np.zeros((nocc, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_ovov += einsum(x2, (0, 1), delta.oo, (2, 3), (2, 0, 3, 1)) * 0.5
    rdm2_f_ovvo = np.zeros((nocc, nvir, nvir, nocc), dtype=np.float64)
    rdm2_f_ovvo += einsum(x2, (0, 1), delta.oo, (2, 3), (2, 0, 1, 3)) * -0.5
    rdm2_f_voov = np.zeros((nvir, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_voov += einsum(x2, (0, 1), delta.oo, (2, 3), (0, 3, 2, 1)) * -0.5
    rdm2_f_vovo = np.zeros((nvir, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_vovo += einsum(x2, (0, 1), delta.oo, (2, 3), (0, 3, 1, 2)) * 0.5
    x3 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x3 += einsum(x2, (0, 1), t2, (2, 3, 4, 0), (2, 3, 4, 1))
    x4 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x4 += einsum(l2, (0, 1, 2, 3), t2, (4, 3, 5, 1), (2, 4, 0, 5))
    rdm2_f_ovov += einsum(x4, (0, 1, 2, 3), (1, 2, 0, 3)) * -1.0
    rdm2_f_ovvo += einsum(x4, (0, 1, 2, 3), (1, 2, 3, 0))
    rdm2_f_voov += einsum(x4, (0, 1, 2, 3), (2, 1, 0, 3))
    rdm2_f_vovo += einsum(x4, (0, 1, 2, 3), (2, 1, 3, 0)) * -1.0
    x5 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x5 += einsum(x4, (0, 1, 2, 3), t2, (4, 0, 5, 2), (1, 4, 3, 5))
    x6 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x6 += einsum(x3, (0, 1, 2, 3), (0, 1, 2, 3)) * -0.5
    x6 += einsum(x5, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x6, (0, 1, 2, 3), (0, 1, 2, 3))
    rdm2_f_oovv += einsum(x6, (0, 1, 2, 3), (0, 1, 3, 2)) * -1.0
    x7 = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    x7 += einsum(t2, (0, 1, 2, 3), x1, (1, 4), (0, 4, 2, 3))
    rdm2_f_oovv += einsum(x7, (0, 1, 2, 3), (0, 1, 3, 2)) * 0.5
    rdm2_f_oovv += einsum(x7, (0, 1, 2, 3), (1, 0, 3, 2)) * -0.5
    rdm2_f_ooov = np.zeros((nocc, nocc, nocc, nvir), dtype=np.float64)
    rdm2_f_oovo = np.zeros((nocc, nocc, nvir, nocc), dtype=np.float64)
    rdm2_f_ovoo = np.zeros((nocc, nvir, nocc, nocc), dtype=np.float64)
    rdm2_f_vooo = np.zeros((nvir, nocc, nocc, nocc), dtype=np.float64)
    rdm2_f_ovvv = np.zeros((nocc, nvir, nvir, nvir), dtype=np.float64)
    rdm2_f_vovv = np.zeros((nvir, nocc, nvir, nvir), dtype=np.float64)
    rdm2_f_vvov = np.zeros((nvir, nvir, nocc, nvir), dtype=np.float64)
    rdm2_f_vvvo = np.zeros((nvir, nvir, nvir, nocc), dtype=np.float64)

    rdm2_f = pack_2e(rdm2_f_oooo, rdm2_f_ooov, rdm2_f_oovo, rdm2_f_ovoo, rdm2_f_vooo, rdm2_f_oovv, rdm2_f_ovov, rdm2_f_ovvo, rdm2_f_voov, rdm2_f_vovo, rdm2_f_vvoo, rdm2_f_ovvv, rdm2_f_vovv, rdm2_f_vvov, rdm2_f_vvvo, rdm2_f_vvvv)

    rdm2_f = rdm2_f.swapaxes(1, 2)

    return rdm2_f

