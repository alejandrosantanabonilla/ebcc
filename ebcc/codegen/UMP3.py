# Code generated for ebcc.

from ebcc import numpy as np
from ebcc.util import pack_2e, einsum, direct_sum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t2=None, **kwargs):
    # energy
    x0 = np.zeros((nocc[1], nocc[1], nocc[0], nocc[0]), dtype=np.float64)
    x0 += einsum(t2.abab, (0, 1, 2, 3), t2.abab, (4, 5, 2, 3), (1, 5, 0, 4))
    e_mp = 0
    e_mp += einsum(v.aabb.oooo, (0, 1, 2, 3), x0, (2, 3, 0, 1), ())
    x1 = np.zeros((nocc[1], nocc[1], nocc[1], nocc[1]), dtype=np.float64)
    x1 += einsum(t2.bbbb, (0, 1, 2, 3), t2.bbbb, (4, 5, 2, 3), (0, 4, 5, 1))
    e_mp += einsum(v.bbbb.oooo, (0, 1, 2, 3), x1, (1, 2, 0, 3), ()) * -1.0
    x2 = np.zeros((nocc[0], nocc[0], nocc[0], nocc[0]), dtype=np.float64)
    x2 += einsum(t2.aaaa, (0, 1, 2, 3), t2.aaaa, (4, 5, 2, 3), (0, 4, 5, 1))
    e_mp += einsum(v.aaaa.oooo, (0, 1, 2, 3), x2, (3, 2, 0, 1), ())
    x3 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x3 += einsum(v.bbbb.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x3 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x4 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x4 += einsum(v.aaaa.oovv, (0, 1, 2, 3), (0, 1, 2, 3))
    x4 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3)) * -1.0
    x5 = np.zeros((nocc[1], nvir[1], nocc[0], nvir[0]), dtype=np.float64)
    x5 += einsum(v.aabb.ovov, (0, 1, 2, 3), (2, 3, 0, 1))
    x5 += einsum(t2.bbbb, (0, 1, 2, 3), v.aabb.ovov, (4, 5, 1, 3), (0, 2, 4, 5)) * 4.0
    x5 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvoo, (4, 2, 5, 1), (5, 3, 0, 4)) * -1.0
    x5 += einsum(t2.aaaa, (0, 1, 2, 3), v.aabb.ovov, (1, 3, 4, 5), (4, 5, 0, 2)) * 4.0
    x5 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.oovv, (4, 0, 5, 3), (1, 5, 4, 2)) * -1.0
    x5 += einsum(t2.abab, (0, 1, 2, 3), v.aabb.vvvv, (4, 2, 5, 3), (1, 5, 0, 4))
    x5 += einsum(t2.abab, (0, 1, 2, 3), x3, (1, 4, 3, 5), (4, 5, 0, 2)) * -1.0
    x5 += einsum(t2.abab, (0, 1, 2, 3), x4, (0, 4, 2, 5), (1, 3, 4, 5)) * -1.0
    e_mp += einsum(t2.abab, (0, 1, 2, 3), x5, (1, 3, 0, 2), ())
    x6 = np.zeros((nocc[0], nocc[0], nvir[0], nvir[0]), dtype=np.float64)
    x6 += einsum(v.aaaa.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x6 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.ovov, (4, 5, 1, 3), (0, 4, 2, 5)) * 4.0
    x6 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.oovv, (4, 1, 5, 3), (4, 0, 5, 2)) * -4.0
    x6 += einsum(t2.aaaa, (0, 1, 2, 3), v.aaaa.vvvv, (4, 2, 5, 3), (0, 1, 4, 5))
    e_mp += einsum(t2.aaaa, (0, 1, 2, 3), x6, (1, 0, 2, 3), ()) * -1.0
    x7 = np.zeros((nocc[1], nocc[1], nvir[1], nvir[1]), dtype=np.float64)
    x7 += einsum(v.bbbb.ovov, (0, 1, 2, 3), (0, 2, 1, 3))
    x7 += einsum(t2.bbbb, (0, 1, 2, 3), v.bbbb.vvvv, (4, 3, 5, 2), (0, 1, 4, 5)) * -1.0
    x7 += einsum(t2.bbbb, (0, 1, 2, 3), x3, (1, 4, 3, 5), (0, 4, 2, 5)) * -4.0
    e_mp += einsum(t2.bbbb, (0, 1, 2, 3), x7, (1, 0, 2, 3), ()) * -1.0

    return e_mp

