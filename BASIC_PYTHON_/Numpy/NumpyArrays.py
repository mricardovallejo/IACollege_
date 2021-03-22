

import numpy as np

a = np.arange(15).reshape(3, 5)

a.shape
#(3, 5)
print(a.ndim)
#2
print (a.dtype.name)
#'int64'
print (a.itemsize)
#8
print (a.size)
#15
print(type(a))
#<type 'numpy.ndarray'>


b = np.array([6, 7, 8])
b = np.array([(1.5,2,3), (4,5,6)])
c = np.array( [ [1,2], [3,4] ], dtype=complex )

np.ones( (2,3,4), dtype=np.int16 )

np.zeros( (3,4) )

print(np.arange(5))
#[0 1 2 3 4 ]
np.arange(6)
#[0 1 2 3 4 5]

a = np.arange( 10, 30, 5 )
print(a)
#a([10, 15, 20, 25])

x = np.linspace( 0, 2, 9 )
#array([ 0. , 0.25, 0.5 , 0.75, 1. , 1.25, 1.5 , 1.75, 2. ])

f = np.sin(x)


B = np.arange(3)
np.sqrt(B)

# Function

def f(x,y):
   return 10*x+y

b = np.fromfunction(f,(5,4),dtype=int)
print(b)

x = b[2,3]
print(x)
y = b[0:5, 1]
print(y)
z = b[ : ,1]
print(z)
w = b[1:3, : ]
print(w)

# Array Creation arange, array, copy, empty, empty_like, eye, fromfile, fromfunction,
# identity, linspace, logspace, mgrid, ogrid, ones, ones_like, r, zeros, zeros_like
# Conversions ndarray.astype, atleast_1d, atleast_2d, atleast_3d, mat
# Manipulations array_split, column_stack, concatenate, diagonal, dsplit, dstack, hsplit,
# hstack, ndarray.item, newaxis, ravel, repeat, reshape, resize, squeeze, swapaxes,
# take, transpose, vsplit, vstack
# Questions all, any, nonzero, where
# Ordering argmax, argmin, argsort, max, min, ptp, searchsorted, sort
# Operations choose, compress, cumprod, cumsum, inner, ndarray.fill, imag, prod, put, putmask,
# real, sum
# Basic Statistics cov, mean, std, var
# Basic Linear Algebra cross, dot, outer, linalg.svd, vdot