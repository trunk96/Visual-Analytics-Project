import pandas as pd
from matplotlib import pyplot as plt
from sklearn import manifold
import numpy as np



def action():
    att=["ID", "LIMIT_BAL", "SEX", "EDUCATION", "MARRIAGE", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6", "default payment next month"]
    data = pd.io.parsers.read_csv('static/dataset.csv',
         delimiter=';',
         header=0,
        );

    from sklearn.preprocessing import StandardScaler
    features = ["AGE", "LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
    #features = ["AGE", "LIMIT_BAL", "BILL_AMT1", "PAY_AMT1"]


    # Separating out the features
    x = data.loc[:, features].values
    # Separating out the target
    y = data.loc[:,['default payment next month']].values
    # Standardizing the features
    x = StandardScaler().fit_transform(x)

    from sklearn.decomposition import PCA
    pca = PCA(n_components=6)
    #seed = np.random.RandomState(seed=3)
    #mds = manifold.MDS(n_components=2, max_iter=100, random_state=seed, dissimilarity="euclidean", n_jobs=-1)
    principalComponents = pca.fit_transform(x)
    #principalComponents=mds.fit_transform(x)
    principalDf = pd.DataFrame(data = principalComponents, columns = ['X1', 'X2', 'X3', 'X4', 'X5', 'X6'])
    midDf=pd.concat([principalDf, data[["ID"]]], axis=1)
    list_of_attributes=["SEX", "AGE", "EDUCATION", "MARRIAGE","LIMIT_BAL", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
    for elem in list_of_attributes:
        midDf=pd.concat([midDf, data[[elem]]], axis=1)
    finalDf = pd.concat([midDf, data[['default payment next month']]], axis = 1)
    finalDf=finalDf.rename(index=str, columns={"default payment next month": "target"})
    finalDf.to_csv("static/pca.csv", sep=',', index=False)
    return 0;

    '''fig = plt.figure(figsize = (8,8))
    ax = fig.add_subplot(1,1,1)
    ax.set_xlabel('Principal Component 1', fontsize = 15)
    ax.set_ylabel('Principal Component 2', fontsize = 15)
    ax.set_title('2 component PCA', fontsize = 20)
    targets = [0, 1]
    colors = ['g', 'r']
    for target, color in zip(targets,colors):
        indicesToKeep = finalDf['target'] == target
        ax.scatter(finalDf.loc[indicesToKeep, 'X1']
                   , finalDf.loc[indicesToKeep, 'X2']
                   , c = color
                   , s = 50)
    ax.legend(targets)
    ax.grid()
    plt.show()


    exit(0);'''

if __name__ == "__main__":
    action()
