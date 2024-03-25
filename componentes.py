#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

"""

from myhdl import *


def exe1(a, b, c, s):
    @always_comb
    def comb():
        s.next =(not(not(a) and not(b)) and a and not(b)) or (a and c and b)

    return instances()


def exe2(l, m, h, l_vd, l_am, l_vm, l_az, l_lj):
    @always_comb
    def comb():
        l_vd.next = False
        l_am.next = False
        l_vm.next = False
        l_az.next = False
        l_lj.next = False


        if l and not(m) and not(h):
            l_vd.next = True
        elif l and m and not(h):
            l_am.next = True
        elif l and m and h:
            l_vm.next = True
        elif not(l) and not(m) and not(h):
            l_az.next = True
        elif (h and not(l) and m) or (h and l and not(m)) or (h and not(l) and not(m)):
            l_lj.next = True
        elif not(h) and m and not(l):
            l_lj.next = True
    


    return instances()


def exe3(i3, i2, i1, i0, p1, p0, v):
    @always_comb
    def comb():
        pass

    return instances()


def exe4_simulando(a, b, c, d, e, f, g, h, i, j, k, l):
    @always_comb
    def comb():
        a.next = 0
        b.next = 0
        c.next = 0
        d.next = 0
        e.next = 0
        f.next = 0
        g.next = 0
        h.next = 0
        i.next = 0
        j.next = 0
        k.next = 0

    return instances()


def exe4_half_sub(x, y, b, d):
    @always_comb
    def comb():
        pass

    return instances()


def exe4_full_sub(x, y, z, b, d):
    @always_comb
    def comb():
        pass

    return instances()


def exe4_sub3(v2, v1, v0, p2, p1, p0, q2, q1, q0):
    return instances()
