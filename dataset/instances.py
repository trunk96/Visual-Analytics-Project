import pandas as pd

dataset="dataset.csv"

att=["ID", "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "default payment next month"]
data = pd.io.parsers.read_csv(dataset,
     delimiter=';',
     header=0,
    );

features = ["AGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
#features = ["AGE", "LIMIT_BAL", "BILL_AMT1", "PAY_AMT1"]

frequency_of=["SEX", "EDUCATION", "MARRIAGE", "AGE"]



for elem in frequency_of:
    table=pd.crosstab(index=data[elem], columns=data["default payment next month"])
    table.columns=["0", "1"]
    #table["total"]=table["0"]+table["1"]
    #table=table.transpose()
    table.to_csv(elem+"_instances.csv")
