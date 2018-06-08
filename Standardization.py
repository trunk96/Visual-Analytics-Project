import pandas as pd
import numpy as np

att=["X1", "X2", "ID", "SEX", "EDUCATION", "MARRIAGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "target"]
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

data_frame = pd.DataFrame(data = x, columns = features)
data_frame.to_csv("standardized_data.csv", sep=',', index=False)
