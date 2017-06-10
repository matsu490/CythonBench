# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2017-06-10
#
# Copyright (C) 2017 Taishi Matsumura
#
import platform
import matplotlib.pyplot as plt
import module
import cythonized_module

plt.close('all')

N = 1000
s = module.StopWatch()

s.start()
module.function(N)
s.lap()
cythonized_module.function_cy(N)
s.lap()
cythonized_module.function_cy_cdef(N)
s.stop()

x = xrange(3)
y = [s.laps[1][0], s.laps[2][0], s.laps[3][0]]
labels = ['Pure python', 'Cython', 'Cython\n+cdef']
text = '''
    Task 1 ({0} loops)

    Platform : {1}
    Version : {2}
    CPU : {3}
    '''.format(N**2, platform.system(), platform.release(), platform.processor())

f = plt.figure()
ax = f.add_subplot(111)
ax.bar(x, y, align='center', tick_label=labels, width=0.5)
ax.set_ylabel('Elapsed time [sec]')
ax.text(0.5*max(x), max(y), text, ha='left', va='top')
f.show()
