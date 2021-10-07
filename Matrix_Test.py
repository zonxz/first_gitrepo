#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 16:22:42 2021

@author: Calebium
"""
import numpy as np

def enterTheMatrix():
    a = int(input("Enter the number of rows:"))
    b = int(input("Enter the number of columns:"))
    print("Enter the number in a single line separated by , :")
    val = list(map(int, input().split(',' )))
    matrix = np.array(val).reshape(a,b)
    print(matrix)
    return matrix

def matrixProduct(foo,bar):
     return foo.dot(bar)
    
def matrixPower(matrix,power):
    return np.linalg.matrix_power(matrix, power)

valMatrix = list(map(int,input(2,2,3).split(',')))
initMatrix = np.array(valMatrix).reshape(3,1)