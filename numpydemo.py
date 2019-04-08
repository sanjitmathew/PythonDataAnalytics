from numpy import *


'''numbers 1-20 as a  matrix of 4,5'''
a=arange(20).reshape(4,5)
# print a
'''to create a datatype in numpy'''
# print dtype(int32)  #int32 is in numpy
'''flattens and returns one dimen array'''
# print a.ravel()
'''changes the dimensions'''
a.shape=(2,10)
# print a
a.resize((10,2))
# print a
a.reshape(5,-1)
# print a
'''reverse order'''
# print a[::-1]
'''row,columns printing'''
# print a[0:4,1]
# print a
#print a[2]
'''makes an array of 2x2'''
a=array([(1,2),(3,4)])
'''checks whether elements of array are less than 2 and returns true or false for each'''
# print a<2
'''raises each element to its square'''
# print a**2
# print a
'makes a 2x3 array with zeroes'
a=zeros((2,3))
# print a
'makes a 2x3 array with ones'
a=ones((2,3))
#print a
'makes a 2x3 array with random no:'
a=empty((2,2))
#print a
'values from 0 to 2 with 0.3 as step'
a=arange(0,2,0.3)
# print a
'values from 0 to 2 in increasing order'
a=linspace(0,2,10)
# print a
b=zeros((3,3))
b=array([1,2])
# print b[:,newaxis]
#print b
#print column_stack((a,b))
c=b
# print id(c)
# print id(b)
c=b.copy()
# print id(c)
# print id(b)
a=arange(10)**2
b=array([1,2,3])
b=array(([1,2],[3,4]))
# print a[b]
'splits the array'
# print hsplit(a,2)
b=a>50
# print b
'wherever b is true insert 0'
a[b]=0
# print a
'unit matrix'
c=eye(3)
# print c

import pylab
# Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
mu, sigma = 2, 0.5
v = random.normal(mu,sigma,10000)
# Plot a normalized histogram with 50 bins
pylab.hist(v, bins=50, normed=1)       # matplotlib version (plot)
# pylab.show()
# Compute the histogram with numpy and then plot it
(n, bins) =histogram(v, bins=50, normed=True)  # NumPy version (no plot)
# print n
# print bins
pylab.plot(.5*(bins[1:]+bins[:-1]), n)
pylab.show()
