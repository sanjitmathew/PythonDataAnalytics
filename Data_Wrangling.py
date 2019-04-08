import numpy as np
import pandas as pd
##########################################################################concatenating
# d={'Name':['peter','paul'],'age':[10,12]}
# a=pd.DataFrame(d)
# d={'Name':['simon','john'],'age':[11,12]}
# b=pd.DataFrame(d)
#
# # print a
# # print b
#
# 'concatenating'
# # print pd.concat([a,b])
# 'in reverse order'
# # print pd.concat([b,a])

#######################################################################     merging,joining

# d={'Name':['peter','paul'],'age':[10,12]}
# a=pd.DataFrame(d)
# d={'Name':['peter','paul'],'class':[5,7]}
# b=pd.DataFrame(d)
#
# 'join methods'
# # print pd.merge(a,b)

#################################################################### appending side by side

# d={'Name':['peter','paul'],'age':[10,12]}
# a=pd.DataFrame(d)
# d={'Name':['pet','simon'],'class':[5,7]}
# b=pd.DataFrame(d)

# print pd.concat([a,b],axis=1)   #for columnwise concatenation (side by side)