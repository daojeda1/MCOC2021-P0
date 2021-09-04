# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 21:00:10 2021

@author: diego
"""
from numpy import zeros
def b(N, dtype):
    b = zeros((N) , dtype=dtype)+1
    return(b.T)
