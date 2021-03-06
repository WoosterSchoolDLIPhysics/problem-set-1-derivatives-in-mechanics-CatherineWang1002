#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 14:25:33 2017

@author: CATHERINEWANG
"""

from pylab import *

t0 = 0.0 #initial time
tf = 30.0 #how long I fall
dt = 0.5 # time step siza

t = arange(t0,tf,dt)
v = zeros(len(t))
v0 = 0
v[0] = v0

#define constansts
b = .10
g = 10 #meters per second sqr of course
m = 1.0 #kg

for i in arange(1,len(t)):
    dv = (-b/m*v[i-1]-g)*dt
    v[i] = v[i-1] + dv
    
figure(1)
clf()
plot(t,v,'bo',markersize=5)
vt = -m*g/b
plot(t,vt*(1-exp(-b*t/m)),'plum',lw=3)
text(20,-37,r'$v(t) = v_T(e^{-\frac{bt}{m}}-1)$',size=20,color='magenta')
plot(t,0*t+vt,'k--')
plot(t,-g*t,'c--')
ylim(-120,0)
