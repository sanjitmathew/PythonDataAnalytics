import pandas
import numpy

    #series
a=numpy.array(['a','b','c'])
# print a
b=pandas.Series(a)
'its like array but different object'
# print b
'returns a series with true false'
# print b.str.contains('a')
# print b.str.upper()
# print b.str.replace('a','A')
'*3 for every element '
# print b.str.repeat(3)
'counts the a in each position'
# print b.str.count('a')
# print pandas.Series({'a':1,'peter':'paul'})
'all positions are 3s'
# print pandas.Series(3,index=[1,2,3])
# print a[1]
# print b.str.findall(r'\.')
    #dataframe
d=[['peter',3],['paul',4]]    #creating dataframe from list each row is a list
a=pandas.DataFrame(d,columns=['Name','age'],dtype=float)
# print a
'column names are keys and values are list of elements of each row'
d={'Name':['peter','paul'],'age':[1,2]}
a=pandas.DataFrame(d)
# print a
# print a['Name']   #selecting a column
a['class']=[10,10]  #adding a column
# print a

# del a['age']
# a.pop('class')
# print a
# print a.loc[0:]   #selecting rows
b=pandas.DataFrame([['peter',12,7]],columns=a.keys())
a=a.append(b)
#print a[1:2]    #dont use without slice
# print a
a=a.drop(0) #drops the row 0
# print a
    #panel
'2 matrices each has 4 rows and 5 columns'
x=numpy.random.rand(2,4,5)
# print x
'a collection of dataframes'
a=pandas.Panel(x,dtype=float)
# print a
# print a[0][1][1]
# print a[1][1]
# print a[1]      #selecting by items
# print a.major_xs(2)     #selecting by major axis (rows)
# print a.minor_xs(1)     #selecting by minor axis(columns)
# print a.values        #print the whole panel
# print a.axes            #describes each axes
# print a.empty         #checks
# print a.ndim            #dimension
# print a.size
# print b.head()          #returns first row
# print b.tail()          #returns last row
# print b.dtypes        #returns datatypes of each column
# print b.T         #transpose
# print a.sum()         #sum of all columns
# print a.sum(0)      #sum of all data frames
# print a.sum(1)      #again sum of all columns
# print a.sum(2)      #sum of all rows
# print a.mean()
# print a.mean(1)
# print a.mean(0)
# print a.mean(2)
# print a.std()           #standard deviation of each column in each dataframe
# print a.min()
# print a.max()
# print b.mode()
# print a.median()
# print a.abs()
# print a.prod()
# print a.cumsum()
# print a.cumprod()
c=pandas.DataFrame(a[1])
# print c.describe()
#ad
def ad(x,y):
    return x+y
# print a[0].pipe(ad,10)        # whole table application
# print c.apply(numpy.mean)     #row wise application
# print a.apply(numpy.mean,axis=0)
# print a.apply(lambda x:x.max()-x.min())
# print c[1].map(lambda x:x*100)
# for i,j in c.iteritems():
#     print i
#     print j                   #iterating as key value pairs
# for i in c.itertuples():
#     print i
# print c
# print c.sort_values(by=1)
# print pandas.set_option('display.max_columns',100)
# print pandas.get_option('display.max_columns')
# print pandas.get_option('display.max_rows')
# print c.loc[:,[1,2]]  #selects all values from column 2
# print c.loc[1:3]>0.5    #true or false
# print c[[1,0]]
# print c.pct_change()    #difference between consecutive elements
x=pandas.Series(numpy.random.rand(10))
y=pandas.Series(numpy.random.rand(10))
# print x.cov(y)    #covariance
# print x.corr(y)   #corelation
# print x.rank()    #ranking
# print x.fillna(0) #fills NA with 0
# print y.dropna()  #removes NA
# print x.replace({0:1})    #replaces 0 with 1
d= c.groupby(1) #same as dbms
# for i,j in d:
#     print i
#     print j
