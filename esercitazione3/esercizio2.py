import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file= pd.read_csv('4LAC_DR2_sel.csv')

print(file.columns)

print(file.iloc[10:20])

y=file['PL_Index']
x=file['Flux1000']

plt.scatter(x, y, color='cyan')
plt.xscale('log')
plt.show()


y1=file['PL_Index']
x1=file['nu_syn']

plt.scatter(x1, y1, color='red')
plt.show()


#mmask = x1 >= 1
#print(x1[mmask])


loga= file.loc[( file['nu_syn'] >0)]

print(loga)
xx= np.log(loga['nu_syn'])

x2 = xx
y2=loga['PL_Index']

plt.scatter(x2, y2, color='royalblue')
plt.show()


bll1= loga.loc[( file['CLASS']=='bll')]
fsrq1 = loga.loc[( file['CLASS']=='fsrq')]

#print(bll1)
plt.scatter(np.log(bll1['nu_syn']), bll1['PL_Index'], color='c', alpha=0.5)
plt.scatter(np.log(fsrq1['nu_syn']), fsrq1['PL_Index'], color='red', alpha=0.5)
plt.errorbar(np.log(bll1['nu_syn']), bll1['PL_Index'], yerr=bll1['Unc_PL_Index'], color='c', alpha=0.3)
plt.show()


n, bins, p = plt.hist(bll1['PL_Index'], bins=100, color='gold', alpha=0.5)
n1, bins1, p1 = plt.hist(fsrq1['PL_Index'], bins=100, color='red', alpha=0.4)
plt.show()

m, bons, o = plt.hist(np.log(bll1['nu_syn']), bins=100, color='c', alpha=0.5)
m1, bons1, o1 = plt.hist(np.log(fsrq1['nu_syn']), bins=100, color='royalblue', alpha=0.3)
plt.show()
                      
