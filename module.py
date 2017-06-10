# -*- coding: utf-8 -*-
# vim: set fileencoding=utf-8 :
# vim: set foldmethod=marker commentstring=\ \ #\ %s :
#
# Author:    Taishi Matsumura
# Created:   2017-06-10
#
# Copyright (C) 2017 Taishi Matsumura
#
import time


def function(num):
    out = 0
    for i in range(num):
        for j in range(num):
            out += 1
    return out


class StopWatch(object):
    def __init__(self):
        self.laps = []
        self.t_start = 0
        self.t_stop = 0
        self.t_lap = 0
    
    def start(self):
        self.laps = []
        self.t_start = time.time()
        self.t_lap = time.time()
        self.laps.append((time.time() - self.t_lap, time.time() - self.t_start, time.ctime()))

    def lap(self):
        self.laps.append((time.time() - self.t_lap, time.time() - self.t_start, time.ctime()))
        self.t_lap = time.time()
        
    def stop(self):
        self.laps.append((time.time() - self.t_lap, time.time() - self.t_start, time.ctime()))
        self.t_stop = time.time()
        self.laps = tuple(self.laps)

    def _sec2hms(self, seconds):
        sec = seconds % 60
        mnt = (int(seconds) / 60) % 60
        hr = (int(seconds) / 60) / 60
        return '{0} h {1} m {2:.1f} sec'.format(hr, mnt, sec)

    def save(self, **kwargs):
        with open('time.txt', mode='w') as f:
            for key, value in kwargs.items():
                f.write('{0} : {1}\n'.format(key, value))
            f.write('Simulation starts at {}\n'.format(self.laps[0][-1]))
            f.write('Simulation ends at {}\n'.format(self.laps[-1][-1]))
            f.write('Elapsed time : {}'.format(self._sec2hms(self.laps[-1][1])))
