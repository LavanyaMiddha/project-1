import jupyter
import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize']=(20.0,10.0)

data=pd.read_csv('heart.csv')
print(data.shape)
data.head()
x=data['age'].values
y=data['trestbps'].values

#mean of x and y
mean_x=np.mean(x)
mean_y=np.mean(y)

#total number of values
n=len(x)

#using formula to calculate b0 and b1
numer=0
denom=0
for i in range(n):
    numer=numer+((x[i]-mean_x)*(y[i]-mean_y))
    denom=denom+((x[i]-mean_x)**2)
b1=numer/denom
b0=mean_y-(b1*mean_x)

#print coefficients
print(b1,b0)

#plotting values and regression line
max_x=100
min_x=0

#calculating line values x and y
X=np.linspace(min_x,max_x,1000)
Y=b0+b1*X

#plotting line
plt.plot(X,Y,color='#58b970',label='Regression Line')

#plotting scatter points
plt.scatter(x,y,color='#ef5423',label='Scatter Plot')

plt.xlabel('Age')
plt.ylabel('resting blood pressure (in mm Hg on admission to the hospital)')
plt.legend()
plt.show()

#to calculate r^2 value to analyze the precision of our model
ss_t=0
ss_r=0
for i in range(n):
    y_pred=b0+b1*x[i]
    ss_t=ss_t+((y[i]-mean_y)**2)
    ss_r=ss_r+((y_pred-mean_y)**2)
r2=ss_r/ss_t
print("The R^2 value is:",r2)
