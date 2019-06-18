import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel('indo_12_1.xls', 'indo_12_1', header=3, index_col=0, nrows=34, na_values=['-'])

# df.to_csv('hasil.csv')
df1 = df[df[1971]==df[1971].min()]
df2 = df[df[2010]==df[2010].iloc[0:33].max()]
df3 = df[df[2010]==df[2010].max()]

sumbuX = np.array(df.columns)

# sumbu y
bengkulu1971 = df1.values[0]
jawa2010 = df2.values[0]
indo = df3.values[0]

# Legend
_indo = df3.index.values[0]
_1971min = df1.index.values[0]
_2010max = df2.index.values[0]

# print(_indo)
plt.plot(sumbuX, indo, 'r-', marker='o', label=_indo)
plt.plot(sumbuX, bengkulu1971, 'g-', marker='o', label=_1971min)
plt.plot(sumbuX, jawa2010, 'b-', marker='o', label=_2010max)

plt.title('Jumlah Penduduk Indonesia(1971-2010)', pad=30)
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk(Ratus Juta jiwa)')
plt.legend(loc='upper left')

plt.show()
