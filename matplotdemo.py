'use only section at a time'
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#######################################################################################    Charts
# x = np.arange(0,10)
# y = x ^ 2
# #Labeling the Axes and Title
# plt.title("Graph Drawing")
# plt.xlabel("Time")
# plt.ylabel("Distance")
#
# # Formatting the line colors
# plt.plot(x,y,'red')
#
# # Formatting the line type
# plt.plot(x,y,'>')
#
# #to write on graph
# plt.annotate(xy=[2,2],s='graphed')
#
# #to define the line at bottom right corner
# plt.legend(['line 1'],loc=1)    #loc to specify the position
#
# # save in pdf formats
# plt.savefig('timevsdist.pdf', format='pdf')
#
# #show the graph finally
# plt.show()

######################################################################################## Heat Maps

# x=np.array(([4,3,2],[1,2,3]))
# y=pd.DataFrame(x)
# plt.pcolor(y)
# plt.show()

########################################################################################
# # 8 observations in 1 to 10 and 1 in 60 to 70 is the histogram
# plt.hist([1,2,3,4,3,2,1,4,67],bins=10)
# plt.show()