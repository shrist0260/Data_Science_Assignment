import numpy as np

data = np.array([12,7,15,10,18,20,8])

Q1= np.percentile(data,25)
Q2= np.percentile(data,50)
Q3= np.percentile(data,75)
IQR= Q3-Q1

print("Q1:",Q1)
print("Median:",Q2)
print("Q3:",Q3)
print("Interquartile Range:",IQR)
