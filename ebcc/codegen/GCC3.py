# Code generated by qwick.

import numpy as np
from ebcc.util import pack_2e, einsum, Namespace

def energy(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # energy
    e_cc = 0.0
    e_cc += einsum("ia,ia->", f.ov, t1)
    e_cc += einsum("ijab,ijab->", t2, v.oovv) * 0.25
    e_cc += einsum("ia,jb,ijab->", t1, t1, v.oovv) * 0.5

    return e_cc

def update_amps(f=None, v=None, nocc=None, nvir=None, t1=None, t2=None, t3=None, **kwargs):
    # T1 amplitudes
    t1new = np.zeros((nocc, nvir), dtype=np.float64)
    t1new += einsum("ia->ia", f.ov)
    t1new += einsum("ij,ja->ia", f.oo, t1) * -1.0
    t1new += einsum("ab,ib->ia", f.vv, t1)
    t1new += einsum("jb,ijab->ia", f.ov, t2)
    t1new += einsum("jb,ibja->ia", t1, v.ovov) * -1.0
    t1new += einsum("jkab,jkib->ia", t2, v.ooov) * -0.5
    t1new += einsum("ijbc,jabc->ia", t2, v.ovvv) * -0.5
    t1new += einsum("jkbc,ijkabc->ia", v.oovv, t3) * 0.25
    t1new += einsum("jb,ib,ja->ia", f.ov, t1, t1) * -1.0
    t1new += einsum("jb,ka,jkib->ia", t1, t1, v.ooov)
    t1new += einsum("ib,jc,jabc->ia", t1, t1, v.ovvv) * -1.0
    t1new += einsum("ib,jkac,jkbc->ia", t1, t2, v.oovv) * -0.5
    t1new += einsum("ja,ikbc,jkbc->ia", t1, t2, v.oovv) * -0.5
    t1new += einsum("jb,ikac,jkbc->ia", t1, t2, v.oovv)
    t1new += einsum("ib,jc,ka,jkbc->ia", t1, t1, t1, v.oovv)

    # T2 amplitudes
    t2new = np.zeros((nocc, nocc, nvir, nvir), dtype=np.float64)
    t2new += einsum("ijab->ijab", v.oovv)
    t2new += einsum("ik,jkab->ijab", f.oo, t2)
    t2new += einsum("jk,ikab->ijab", f.oo, t2) * -1.0
    t2new += einsum("ac,ijbc->ijab", f.vv, t2) * -1.0
    t2new += einsum("bc,ijac->ijab", f.vv, t2)
    t2new += einsum("ka,ijkb->ijab", t1, v.ooov) * -1.0
    t2new += einsum("kb,ijka->ijab", t1, v.ooov)
    t2new += einsum("ic,jcab->ijab", t1, v.ovvv) * -1.0
    t2new += einsum("jc,icab->ijab", t1, v.ovvv)
    t2new += einsum("kc,ijkabc->ijab", f.ov, t3)
    t2new += einsum("klab,ijkl->ijab", t2, v.oooo) * 0.5
    t2new += einsum("ikac,jckb->ijab", t2, v.ovov) * -1.0
    t2new += einsum("ikbc,jcka->ijab", t2, v.ovov)
    t2new += einsum("jkac,ickb->ijab", t2, v.ovov)
    t2new += einsum("jkbc,icka->ijab", t2, v.ovov) * -1.0
    t2new += einsum("ijcd,abcd->ijab", t2, v.vvvv) * 0.5
    t2new += einsum("klic,jklabc->ijab", v.ooov, t3) * 0.5
    t2new += einsum("kljc,iklabc->ijab", v.ooov, t3) * -0.5
    t2new += einsum("kacd,ijkbcd->ijab", v.ovvv, t3) * 0.5
    t2new += einsum("kbcd,ijkacd->ijab", v.ovvv, t3) * -0.5
    t2new += einsum("kc,ic,jkab->ijab", f.ov, t1, t2)
    t2new += einsum("kc,jc,ikab->ijab", f.ov, t1, t2) * -1.0
    t2new += einsum("kc,ka,ijbc->ijab", f.ov, t1, t2)
    t2new += einsum("kc,kb,ijac->ijab", f.ov, t1, t2) * -1.0
    t2new += einsum("ka,lb,ijkl->ijab", t1, t1, v.oooo)
    t2new += einsum("ic,ka,jckb->ijab", t1, t1, v.ovov)
    t2new += einsum("ic,kb,jcka->ijab", t1, t1, v.ovov) * -1.0
    t2new += einsum("jc,ka,ickb->ijab", t1, t1, v.ovov) * -1.0
    t2new += einsum("jc,kb,icka->ijab", t1, t1, v.ovov)
    t2new += einsum("ic,jd,abcd->ijab", t1, t1, v.vvvv)
    t2new += einsum("ic,klab,kljc->ijab", t1, t2, v.ooov) * -0.5
    t2new += einsum("jc,klab,klic->ijab", t1, t2, v.ooov) * 0.5
    t2new += einsum("ka,ilbc,kljc->ijab", t1, t2, v.ooov)
    t2new += einsum("ka,jlbc,klic->ijab", t1, t2, v.ooov) * -1.0
    t2new += einsum("kb,ilac,kljc->ijab", t1, t2, v.ooov) * -1.0
    t2new += einsum("kb,jlac,klic->ijab", t1, t2, v.ooov)
    t2new += einsum("kc,ilab,kljc->ijab", t1, t2, v.ooov)
    t2new += einsum("kc,jlab,klic->ijab", t1, t2, v.ooov) * -1.0
    t2new += einsum("ic,jkbd,kacd->ijab", t1, t2, v.ovvv) * -1.0
    t2new += einsum("ic,jkad,kbcd->ijab", t1, t2, v.ovvv)
    t2new += einsum("jc,ikbd,kacd->ijab", t1, t2, v.ovvv)
    t2new += einsum("jc,ikad,kbcd->ijab", t1, t2, v.ovvv) * -1.0
    t2new += einsum("ka,ijcd,kbcd->ijab", t1, t2, v.ovvv) * -0.5
    t2new += einsum("kb,ijcd,kacd->ijab", t1, t2, v.ovvv) * 0.5
    t2new += einsum("kc,ijbd,kacd->ijab", t1, t2, v.ovvv) * -1.0
    t2new += einsum("kc,ijad,kbcd->ijab", t1, t2, v.ovvv)
    t2new += einsum("ic,klcd,jklabd->ijab", t1, v.oovv, t3) * 0.5
    t2new += einsum("jc,klcd,iklabd->ijab", t1, v.oovv, t3) * -0.5
    t2new += einsum("ka,klcd,ijlbcd->ijab", t1, v.oovv, t3) * 0.5
    t2new += einsum("kb,klcd,ijlacd->ijab", t1, v.oovv, t3) * -0.5
    t2new += einsum("kc,klcd,ijlabd->ijab", t1, v.oovv, t3)
    t2new += einsum("ikac,jlbd,klcd->ijab", t2, t2, v.oovv)
    t2new += einsum("ikab,jlcd,klcd->ijab", t2, t2, v.oovv) * -0.5
    t2new += einsum("ikbc,jlad,klcd->ijab", t2, t2, v.oovv) * -1.0
    t2new += einsum("ikcd,jlab,klcd->ijab", t2, t2, v.oovv) * -0.5
    t2new += einsum("ijac,klbd,klcd->ijab", t2, t2, v.oovv) * -0.5
    t2new += einsum("ijbc,klad,klcd->ijab", t2, t2, v.oovv) * 0.5
    t2new += einsum("ijcd,klab,klcd->ijab", t2, t2, v.oovv) * 0.25
    t2new += einsum("ic,ka,lb,kljc->ijab", t1, t1, t1, v.ooov) * -1.0
    t2new += einsum("jc,ka,lb,klic->ijab", t1, t1, t1, v.ooov)
    t2new += einsum("ic,jd,ka,kbcd->ijab", t1, t1, t1, v.ovvv) * -1.0
    t2new += einsum("ic,jd,kb,kacd->ijab", t1, t1, t1, v.ovvv)
    t2new += einsum("ic,jd,klab,klcd->ijab", t1, t1, t2, v.oovv) * 0.5
    t2new += einsum("ic,ka,jlbd,klcd->ijab", t1, t1, t2, v.oovv) * -1.0
    t2new += einsum("ic,kb,jlad,klcd->ijab", t1, t1, t2, v.oovv)
    t2new += einsum("ic,kd,jlab,klcd->ijab", t1, t1, t2, v.oovv) * -1.0
    t2new += einsum("jc,ka,ilbd,klcd->ijab", t1, t1, t2, v.oovv)
    t2new += einsum("jc,kb,ilad,klcd->ijab", t1, t1, t2, v.oovv) * -1.0
    t2new += einsum("jc,kd,ilab,klcd->ijab", t1, t1, t2, v.oovv)
    t2new += einsum("ka,lb,ijcd,klcd->ijab", t1, t1, t2, v.oovv) * 0.5
    t2new += einsum("kc,la,ijbd,klcd->ijab", t1, t1, t2, v.oovv)
    t2new += einsum("kc,lb,ijad,klcd->ijab", t1, t1, t2, v.oovv) * -1.0
    t2new += einsum("ic,jd,ka,lb,klcd->ijab", t1, t1, t1, t1, v.oovv)

    # T3 amplitudes
    t3new = np.zeros((nocc, nocc, nocc, nvir, nvir, nvir), dtype=np.float64)
    t3new += einsum("il,jklabc->ijkabc", f.oo, t3) * -1.0
    t3new += einsum("jl,iklabc->ijkabc", f.oo, t3)
    t3new += einsum("kl,ijlabc->ijkabc", f.oo, t3) * -1.0
    t3new += einsum("ad,ijkbcd->ijkabc", f.vv, t3)
    t3new += einsum("bd,ijkacd->ijkabc", f.vv, t3) * -1.0
    t3new += einsum("cd,ijkabd->ijkabc", f.vv, t3)
    t3new += einsum("ilab,jklc->ijkabc", t2, v.ooov) * -1.0
    t3new += einsum("ilac,jklb->ijkabc", t2, v.ooov)
    t3new += einsum("ilbc,jkla->ijkabc", t2, v.ooov) * -1.0
    t3new += einsum("jlab,iklc->ijkabc", t2, v.ooov)
    t3new += einsum("jlac,iklb->ijkabc", t2, v.ooov) * -1.0
    t3new += einsum("jlbc,ikla->ijkabc", t2, v.ooov)
    t3new += einsum("klab,ijlc->ijkabc", t2, v.ooov) * -1.0
    t3new += einsum("klac,ijlb->ijkabc", t2, v.ooov)
    t3new += einsum("klbc,ijla->ijkabc", t2, v.ooov) * -1.0
    t3new += einsum("ikad,jdbc->ijkabc", t2, v.ovvv)
    t3new += einsum("ikbd,jdac->ijkabc", t2, v.ovvv) * -1.0
    t3new += einsum("ikcd,jdab->ijkabc", t2, v.ovvv)
    t3new += einsum("ijad,kdbc->ijkabc", t2, v.ovvv) * -1.0
    t3new += einsum("ijbd,kdac->ijkabc", t2, v.ovvv)
    t3new += einsum("ijcd,kdab->ijkabc", t2, v.ovvv) * -1.0
    t3new += einsum("jkad,idbc->ijkabc", t2, v.ovvv) * -1.0
    t3new += einsum("jkbd,idac->ijkabc", t2, v.ovvv)
    t3new += einsum("jkcd,idab->ijkabc", t2, v.ovvv) * -1.0
    t3new += einsum("ld,id,jklabc->ijkabc", f.ov, t1, t3) * -1.0
    t3new += einsum("ld,jd,iklabc->ijkabc", f.ov, t1, t3)
    t3new += einsum("ld,kd,ijlabc->ijkabc", f.ov, t1, t3) * -1.0
    t3new += einsum("ld,la,ijkbcd->ijkabc", f.ov, t1, t3) * -1.0
    t3new += einsum("ld,lb,ijkacd->ijkabc", f.ov, t1, t3)
    t3new += einsum("ld,lc,ijkabd->ijkabc", f.ov, t1, t3) * -1.0
    t3new += einsum("ld,ikad,jlbc->ijkabc", f.ov, t2, t2) * -1.0
    t3new += einsum("ld,ikbd,jlac->ijkabc", f.ov, t2, t2)
    t3new += einsum("ld,ikcd,jlab->ijkabc", f.ov, t2, t2) * -1.0
    t3new += einsum("ld,ilac,jkbd->ijkabc", f.ov, t2, t2) * -1.0
    t3new += einsum("ld,ilab,jkcd->ijkabc", f.ov, t2, t2)
    t3new += einsum("ld,ilbc,jkad->ijkabc", f.ov, t2, t2)
    t3new += einsum("ld,ijad,klbc->ijkabc", f.ov, t2, t2)
    t3new += einsum("ld,ijbd,klac->ijkabc", f.ov, t2, t2) * -1.0
    t3new += einsum("ld,ijcd,klab->ijkabc", f.ov, t2, t2)
    t3new += einsum("la,imbc,jklm->ijkabc", t1, t2, v.oooo) * -1.0
    t3new += einsum("la,jmbc,iklm->ijkabc", t1, t2, v.oooo)
    t3new += einsum("la,kmbc,ijlm->ijkabc", t1, t2, v.oooo) * -1.0
    t3new += einsum("lb,imac,jklm->ijkabc", t1, t2, v.oooo)
    t3new += einsum("lb,jmac,iklm->ijkabc", t1, t2, v.oooo) * -1.0
    t3new += einsum("lb,kmac,ijlm->ijkabc", t1, t2, v.oooo)
    t3new += einsum("lc,imab,jklm->ijkabc", t1, t2, v.oooo) * -1.0
    t3new += einsum("lc,jmab,iklm->ijkabc", t1, t2, v.oooo)
    t3new += einsum("lc,kmab,ijlm->ijkabc", t1, t2, v.oooo) * -1.0
    t3new += einsum("id,jlab,kdlc->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("id,jlac,kdlb->ijkabc", t1, t2, v.ovov)
    t3new += einsum("id,jlbc,kdla->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("id,klab,jdlc->ijkabc", t1, t2, v.ovov)
    t3new += einsum("id,klac,jdlb->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("id,klbc,jdla->ijkabc", t1, t2, v.ovov)
    t3new += einsum("jd,ilab,kdlc->ijkabc", t1, t2, v.ovov)
    t3new += einsum("jd,ilac,kdlb->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("jd,ilbc,kdla->ijkabc", t1, t2, v.ovov)
    t3new += einsum("jd,klab,idlc->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("jd,klac,idlb->ijkabc", t1, t2, v.ovov)
    t3new += einsum("jd,klbc,idla->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("kd,ilab,jdlc->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("kd,ilac,jdlb->ijkabc", t1, t2, v.ovov)
    t3new += einsum("kd,ilbc,jdla->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("kd,jlab,idlc->ijkabc", t1, t2, v.ovov)
    t3new += einsum("kd,jlac,idlb->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("kd,jlbc,idla->ijkabc", t1, t2, v.ovov)
    t3new += einsum("la,ikbd,jdlc->ijkabc", t1, t2, v.ovov)
    t3new += einsum("la,ikcd,jdlb->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("la,ijbd,kdlc->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("la,ijcd,kdlb->ijkabc", t1, t2, v.ovov)
    t3new += einsum("la,jkbd,idlc->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("la,jkcd,idlb->ijkabc", t1, t2, v.ovov)
    t3new += einsum("lb,ikad,jdlc->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("lb,ikcd,jdla->ijkabc", t1, t2, v.ovov)
    t3new += einsum("lb,ijad,kdlc->ijkabc", t1, t2, v.ovov)
    t3new += einsum("lb,ijcd,kdla->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("lb,jkad,idlc->ijkabc", t1, t2, v.ovov)
    t3new += einsum("lb,jkcd,idla->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("lc,ikad,jdlb->ijkabc", t1, t2, v.ovov)
    t3new += einsum("lc,ikbd,jdla->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("lc,ijad,kdlb->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("lc,ijbd,kdla->ijkabc", t1, t2, v.ovov)
    t3new += einsum("lc,jkad,idlb->ijkabc", t1, t2, v.ovov) * -1.0
    t3new += einsum("lc,jkbd,idla->ijkabc", t1, t2, v.ovov)
    t3new += einsum("id,jkce,abde->ijkabc", t1, t2, v.vvvv) * -1.0
    t3new += einsum("id,jkbe,acde->ijkabc", t1, t2, v.vvvv)
    t3new += einsum("id,jkae,bcde->ijkabc", t1, t2, v.vvvv) * -1.0
    t3new += einsum("jd,ikce,abde->ijkabc", t1, t2, v.vvvv)
    t3new += einsum("jd,ikbe,acde->ijkabc", t1, t2, v.vvvv) * -1.0
    t3new += einsum("jd,ikae,bcde->ijkabc", t1, t2, v.vvvv)
    t3new += einsum("kd,ijce,abde->ijkabc", t1, t2, v.vvvv) * -1.0
    t3new += einsum("kd,ijbe,acde->ijkabc", t1, t2, v.vvvv)
    t3new += einsum("kd,ijae,bcde->ijkabc", t1, t2, v.vvvv) * -1.0
    t3new += einsum("id,la,jmbc,lmkd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("id,la,kmbc,lmjd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("id,lb,jmac,lmkd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("id,lb,kmac,lmjd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("id,lc,jmab,lmkd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("id,lc,kmab,lmjd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("jd,la,imbc,lmkd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("jd,la,kmbc,lmid->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("jd,lb,imac,lmkd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("jd,lb,kmac,lmid->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("jd,lc,imab,lmkd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("jd,lc,kmab,lmid->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("kd,la,imbc,lmjd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("kd,la,jmbc,lmid->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("kd,lb,imac,lmjd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("kd,lb,jmac,lmid->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("kd,lc,imab,lmjd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("kd,lc,jmab,lmid->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("la,mb,ijcd,lmkd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("la,mb,ikcd,lmjd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("la,mb,jkcd,lmid->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("la,mc,ijbd,lmkd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("la,mc,ikbd,lmjd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("la,mc,jkbd,lmid->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("lb,mc,ijad,lmkd->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("lb,mc,ikad,lmjd->ijkabc", t1, t1, t2, v.ooov)
    t3new += einsum("lb,mc,jkad,lmid->ijkabc", t1, t1, t2, v.ooov) * -1.0
    t3new += einsum("id,je,klbc,lade->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("id,je,klac,lbde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("id,je,klab,lcde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("id,ke,jlbc,lade->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("id,ke,jlac,lbde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("id,ke,jlab,lcde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("id,la,jkce,lbde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("id,la,jkbe,lcde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("id,lb,jkce,lade->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("id,lb,jkae,lcde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("id,lc,jkbe,lade->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("id,lc,jkae,lbde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("jd,ke,ilbc,lade->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("jd,ke,ilac,lbde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("jd,ke,ilab,lcde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("jd,la,ikce,lbde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("jd,la,ikbe,lcde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("jd,lb,ikce,lade->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("jd,lb,ikae,lcde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("jd,lc,ikbe,lade->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("jd,lc,ikae,lbde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("kd,la,ijce,lbde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("kd,la,ijbe,lcde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("kd,lb,ijce,lade->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("kd,lb,ijae,lcde->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("kd,lc,ijbe,lade->ijkabc", t1, t1, t2, v.ovvv)
    t3new += einsum("kd,lc,ijae,lbde->ijkabc", t1, t1, t2, v.ovvv) * -1.0
    t3new += einsum("id,je,la,kmbc,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("id,je,lb,kmac,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("id,je,lc,kmab,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("id,ke,la,jmbc,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("id,ke,lb,jmac,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("id,ke,lc,jmab,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("id,la,mb,jkce,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("id,la,mc,jkbe,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("id,lb,mc,jkae,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("jd,ke,la,imbc,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("jd,ke,lb,imac,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("jd,ke,lc,imab,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("jd,la,mb,ikce,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("jd,la,mc,ikbe,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("jd,lb,mc,ikae,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("kd,la,mb,ijce,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0
    t3new += einsum("kd,la,mc,ijbe,lmde->ijkabc", t1, t1, t1, t2, v.oovv)
    t3new += einsum("kd,lb,mc,ijae,lmde->ijkabc", t1, t1, t1, t2, v.oovv) * -1.0

    return {"t1new": t1new, "t2new": t2new, "t3new": t3new}
