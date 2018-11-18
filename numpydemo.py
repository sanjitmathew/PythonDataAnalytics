from numpy import *
import pylab

a=arange(20).reshape(4,5)
# print a
# a.ravel()
# a.shape=(2,10)
# a.resize((10,2))
# a.reshape(5,-1)
# print a
# #print a[::-1]
# #print a[0:4,4]
# #print a
# #print a[2]
# a=array([(1,2),(3,4)])
# #print a<2
# #print a**2
# #print a
# a=zeros((2,3))
# #print a
# a=ones((2,3))
# #print a
# a=empty((2,2))
# #print a
# a=arange(0,2,0.3)
# #print a
# a=linspace(0,2,10)
# a=ones((3,3))
# #print a
# b=zeros((3,3))
# b=array([1,2])
# #print b[:,newaxis]
# #print b
# #print column_stack((a,b))
# c=b
# # print id(c)
# # print id(b)
# c=b.copy()
# # print id(c)
# # print id(b)
# a=arange(10)**2
# b=array([1,2,3])
# b=array(([1,2],[3,4]))
# # print a[b]
# # print hsplit(a,3)
# b=a>50
# a[b]=0
# # print a
# c=eye(3)
# # print c
#
# # Build a vector of 10000 normal deviates with variance 0.5^2 and mean 2
# mu, sigma = 2, 0.5
# v = random.normal(mu,sigma,10000)
# # Plot a normalized histogram with 50 bins
# pylab.hist(v, bins=50, normed=1)       # matplotlib version (plot)
# # pylab.show()
# # Compute the histogram with numpy and then plot it
# (n, bins) =histogram(v, bins=50, normed=True)  # NumPy version (no plot)
# pylab.plot(.5*(bins[1:]+bins[:-1]), n)
# # pylab.show()
