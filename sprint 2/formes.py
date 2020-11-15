#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 16:08:42 2020

@author: paulin
"""

import numpy as np
import matplotlib.pyplot as plt


# figure jaune en haut à gauche
yTetrisseP = array([2,  2,  3,  3,  4, 4, 3, 3,2])
xTetrisseP = array([-4, -1, -1, -2,-2,-3, -3,-4,-4])
plot(xTetrisseP, yTetrisseP, 'orange')


# figure violette en 
yTetrisseG = array([-3, -3,  -1, -1,  -2, -2, -3])
xTetrisseG = array([2,  6,   6,  5,   5,  2, 2])
plot(xTetrisseG, yTetrisseG,'purple')


# Enveloppe
xEnv = array([-3, -1,-2,-3,-3,-1,-1])
yEnv = array([0, 0, -1, 0,-2,-2,0])
plot(xEnv, yEnv,'b')


# Maison
xMai = array([2,3,3,2,2,0,0,4,2,0,4,4,3])
yMai = array([0,0,2,2,0,0,4,4,6,4,4,0,0])
plot(xMai, yMai,'g')


# cercle
circle = plt.Circle((7,2),1.5, fill=False);
plt.gcf().gca().add_artist(circle)


# grille
j=7
for i in range(0,4):
    ySegmentH= array([-1, -3])
    xSegmentH= array([j,j])
    plot(xSegmentH,ySegmentH,'red')
    j=j+1
    
i=-1
for j in range(0,3):
    ySegmentV=array([i, i])
    xSegmentV=array([7, 10])
    plot(xSegmentV,ySegmentV,'red')
    i=i-1


show() 