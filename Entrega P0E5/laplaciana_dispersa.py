# -*- coding: utf-8 -*-
"""
Created on Thu Aug 26 18:59:56 2021

@author: diego
"""
import scipy.sparse as sparse

def laplaciana_dispersa(N, dtype):
    return 2*sparse.eye(N,dtype=dtype)-sparse.eye(N,N,1,dtype=dtype)-sparse.eye(N,N,-1,dtype=dtype)