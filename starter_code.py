#!env/bin/python3
# -*- coding: utf-8 -*-
"""
Starter code for basic level
Colomb-ia

"""

#Importar librerías
import pandas as pd

#Leer datos
train = pd.read_csv("data/iris_train.csv")
test = pd.read_csv("data/iris_test.csv")

#Explorar primeros registros
train.head()
# train.head()

print(train)