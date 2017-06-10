# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2017-06-10
#
# Copyright (C) 2017 Taishi Matsumura
#
from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext

ext_modules = [Extension('cythonized_module', ['cythonized_module.pyx'])]
setup(
    name = 'cythonized_module',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
    )
