# -*- coding: utf-8 -*-
"""Entrega_Final_RandomForest.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1j3nsWRsZEC5jBHIINuoAhXeg2OHEaC-1
"""

import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/russelr01/Aprendizaje-Maquina/main/StudentsPerformance.csv'

data = pd.read_csv(url)
data.head()

data.info()

data.columns

data['parental level of education'].value_counts()

data['race/ethnicity'].value_counts()

data['gender'].value_counts()

data['average'] = (data['writing score'] + data['reading score']) / 2

data.info()

relevant = ['gender', 'parental level of education', 'test preparation course', 'average', 'lunch']

data=data[relevant].copy()

data=data.join(pd.get_dummies(data['gender'],prefix="gender"),how="inner").copy()

data=data.join(pd.get_dummies(data['parental level of education'],prefix="parental_education"),how="inner").copy()

data=data.join(pd.get_dummies(data['test preparation course'],prefix="prep"),how="inner").copy()

data=data.join(pd.get_dummies(data['lunch'],prefix="lunch"),how="inner").copy()

data=data.drop(['gender', 'parental level of education', 'test preparation course', 'lunch'],axis=1).copy()

data.info()

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score,mean_absolute_error,mean_squared_error

Y=data['average']
X=data.drop(["average"],axis=1).copy()

X.head()

x_train,x_test,y_train,y_test=train_test_split(X,Y, test_size=0.15,random_state=52)

modelo_bosque=RandomForestRegressor(n_estimators=50,max_depth=5, random_state=52)

modelo_bosque.fit(x_train,y_train)

y_hat_train=modelo_bosque.predict(x_train)

mse_train=mean_squared_error(y_hat_train,y_train)
mae_train=mean_absolute_error(y_hat_train,y_train)
r2_train=r2_score(y_hat_train,y_train)

print("el modelo tiene las siguientes métricas en train:")
print("MSE=", mse_train)
print("MAE=", mae_train)
print("R2=" ,r2_train)

y_hat_test=modelo_bosque.predict(x_test)

mse_test=mean_squared_error(y_hat_test,y_test)
mae_test=mean_absolute_error(y_hat_test,y_test)
r2_test=r2_score(y_hat_test,y_test)

print("el modelo tiene las siguientes métricas en test:")
print("MSE=", mse_test)
print("MAE=", mae_test)
print("R2=" ,r2_test)

bias_test = abs(y_test - y_hat_test).mean()
bias_test

bias_train = abs(y_train - y_hat_train).mean()
bias_train