import pandas as pd
import matplotlib.pyplot as plt

file = pd.read_csv('4FGL_J2202.7+4216_weekly_9_11_2023.csv')

#print(file)

#print(file.columns)

x=file['Julian Date']
y=file['Photon Flux [0.1-100 GeV](photons cm-2 s-1)']
ey=file['Photon Flux Error(photons cm-2 s-1)']
plt.rcParams["figure.figsize"]=[15,7]
plt.errorbar(x, y, yerr=ey, color='c', fmt='*')
plt.xlabel('Giorno Giuliano')
plt.ylabel('Flusso')
plt.yscale('log')
plt.savefig('grafico.png')
plt.show()
