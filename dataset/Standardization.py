import pandas as pd
import numpy as np

att=["X1", "X2", "ID", "SEX", "AGE", "EDUCATION", "MARRIAGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "target"]
data = pd.io.parsers.read_csv('pca.csv',
     delimiter=',',
     header=0,
    );

from sklearn.preprocessing import StandardScaler
features = ["BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]

# Separating out the features
x = data.loc[:, features].values

# Standardizing the features
x = StandardScaler().fit_transform(x)

standard_data_frame = pd.DataFrame(data = x, columns = features)

midDf=pd.DataFrame()
list_of_attributes=["X1", "X2", "ID", "SEX", "AGE", "EDUCATION", "MARRIAGE", "LIMIT_BAL"]
for elem in list_of_attributes:
    midDf=pd.concat([midDf, data[[elem]]], axis=1)
almostFinalDF = pd.concat([midDf, standard_data_frame], axis = 1)
finalDf = pd.concat([almostFinalDF, data[["target"]]], axis = 1)
finalDf.to_csv("standardized_data.csv", sep=',', index=False)
