# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 20:05:05 2021

@author: hp
"""
'''
import numpy as np
arr=np.arange(10)
#print(arr)
#print(arr[5])
#print(arr[5:8])
arr[5:8]=12
#print(arr)
arr_slice=arr[5:8]
#print(arr_slice)
arr_slice[1]=12345
#print(arr)
arr_slice[:]=64
print(arr)
'''
import numpy as np
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])
#print(arr2d[0][2])
#OR
#print(arr2d[0,2])
