from numpy import *
from scipy import *
from scipy.special import *
a=poly1d([1,23,4,4])
#print a
for i in range(10):
    a=gamma(i+2j)
    print a
# for i in range(1,10):
#     print jv(i,1)