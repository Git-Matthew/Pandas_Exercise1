# Import libraries
import pandas as pd

# 1 Create a series from a list
arr = [0, 1, 2, 3, 4]
s1 = pd.Series(arr)

# 2 Create a series from a dictionary
d={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}
s2 = pd.Series(d)

d={'B':10, 'C':10, 'D':10, 'E':10, 'a':50, 'b':50, 'c':50, 'd':50}
s3 = pd.Series(d)

# 3 Modify index of series
s1.index = ['A','B','C','D','E']

# 4 Append & drop
s4 = s1.append(s2)
s4 = s4.drop('e')
s4 = s4.drop('A')
print ("Before Operations:")
print (s4)

# 5 Operations
print ("\nAfter Operations:")
s4 = s4.mul(s3)
s5 = s4.add(s3)
print (s4)
print ("\n")

# 6 Max & Min
print('Max:', s5.max())
print('Max:', s5.min())

# 7 Median
print('Median:', s5.median())


