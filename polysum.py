#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 18:35:34 2019

@author: wanyanwang
"""

# polysum that takes 2 arguments, n and s. 
# it sums the area and square of the perimeter of the regular polygon. 
# The function returns the sum, rounded to 4 decimal places.

from math import *
def polysum(n, s):
    return round((0.25*n*s*s/tan(pi/n) + n*s*n*s), 4)
