# -*- coding: utf-8 -*-
"""
Created on Sun Jun 17 00:49:50 2018

@author: 1000091

Write a function so that the columns of the output matrix are powers of the input
vector.
The order of the powers is determined by the increasing boolean argument. Specifically,
when increasing is False, the i-th output column is the input vector raised element-wise
to the power of N - i - 1.
HINT: Such a matrix with a geometric progression in each row is named for Alexandre-
Theophile Vandermonde.
Note: Solution submitted via github must contain all the detailed steps.

"""
import os, sys
import numpy as np

def gen_vander_matrix(IPVector, n, increasing=False):
    if not increasing:
        op_matx = np.array([x**(n-1-i) for x in IPVector for i in range(n)]).reshape(IPVector.size,n)
    elif increasing:
        op_matx = np.array([x**i for x in IPVector for i in range(n)]).reshape(IPVector.size,n)
    
    return op_matx

IVector = np.array([11,22,33,44,55])
no_col_opmat = 8
op_matx_dec_order = gen_vander_matrix(IVector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(IVector,no_col_opmat,True)

print("The input array is:",IVector,"\n")
print("Number of columns :",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n",op_matx_inc_order,"\n")

IVector = np.array([11,22,44,66,88,100])
no_col_opmat = 7
op_matx_dec_order = gen_vander_matrix(IVector,no_col_opmat,False)
op_matx_inc_order = gen_vander_matrix(IVector,no_col_opmat,True)

print("The input array is:",IVector,"\n")
print("Number of columns:",no_col_opmat,"\n")
print("Vander matrix of the input array in decreasing order of powers:\n",op_matx_dec_order,"\n")
print("Vander matrix of the input array in increasing order of powers:\n",op_matx_inc_order,"\n")