# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2017-06-10
#
# Copyright (C) 2017 Taishi Matsumura
#


def function_cy(num):
    out = 0
    for i in range(num):
        for j in range(num):
            out += 1
    return out


def function_cy_cdef(int num):
    cdef int out = 0
    for n1 in range(num):
        for n2 in range(num):
            out += 1
    return out
