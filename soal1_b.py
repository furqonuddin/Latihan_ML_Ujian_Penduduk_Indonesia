import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_excel('indo_12_1.xls', 'indo_12_1', header=3, index_col=0, nrows=34, na_values=['-'])
# dfnext = df.fillna(0)

# df.to_csv('hasil.csv')
df1 = df[df[1971]==df[1971].min()]
df2 = df[df[2010]==df[2010].iloc[0:33].max()]
df3 = df[df[2010]==df[2010].max()]

# sumbu X
sumbuX = np.array(df.columns)

# sumbu Y
indo = df3.values[0]
bengkulu1971 = df1.values[0]
jawa2010 = df2.values[0]

# Legend
_indo = df3.index.values[0]
_1971min = df1.index.values[0]
_2010max = df2.index.values[0]

# =============================================================================

model1 = linear_model.LinearRegression()
model2 = linear_model.LinearRegression()
model3 = linear_model.LinearRegression()

# training .fit(dataIndependent[2D], data Dependent[1D])
t1 = model1.fit(sumbuX.reshape(-1, 1), indo)
t2 = model2.fit(sumbuX.reshape(-1, 1), bengkulu1971)
t3 = model3.fit(sumbuX.reshape(-1, 1), jawa2010)

# nilai y terbaik
yIndo = t1.predict(sumbuX.reshape(-1, 1))
yBengkulu1971 = t2.predict(sumbuX.reshape(-1, 1))
yJawa2010 = t3.predict(sumbuX.reshape(-1, 1))

# ==========================================================================
# plot origin
plt.plot(sumbuX, indo, 'r-', marker='o', label=_indo)
plt.plot(sumbuX, bengkulu1971, 'g-', marker='o', label=_1971min)
plt.plot(sumbuX, jawa2010, 'b-', marker='o', label=_2010max)

# ==========================================================================
# plot prediksi
plt.plot(sumbuX, yIndo, 'y-', label='Best Fit line')
plt.plot(sumbuX, yBengkulu1971, 'y-')
plt.plot(sumbuX, yJawa2010, 'y-')

plt.title('Jumlah Penduduk Indonesia(1971-2010)', pad=30)
plt.xlabel('Tahun')
plt.ylabel('Jumlah Penduduk(Ratus Juta jiwa)')
plt.legend(loc='upper left')

plt.show()
