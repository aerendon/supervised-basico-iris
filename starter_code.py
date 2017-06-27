#!env/bin/python3
# -*- coding: utf-8 -*-
"""
Starter code for basic level
Colomb-ia

"""

#Importar librerías
import pandas as pd
from pandas.tools.plotting import scatter_matrix
import matplotlib.pyplot as plt

#Leer datos
train = pd.read_csv("data/iris_train.csv", index_col=0)
test = pd.read_csv("data/iris_test.csv", index_col=0)

#Explorar primeros registros
# train.head()

# print(train)

# Data Visualization
# train.plot(kind='box', subplots=True, layout=(2,2), sharex=False, sharey=False)
# plt.show()

# histograms
# train.hist()
# plt.show()

# scatter plot matrix
scatter_matrix(train)
plt.show()