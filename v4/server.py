from flask import Flask, render_template, send_from_directory, request, jsonify

import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import pandas as pd


import sys


import frequency, instances, pca, Standardization, preprocessing

clf=None;
last_id=30000;
app = Flask(__name__, static_folder='/static');

@app.route("/")
def index():
    return render_template("charts.html")

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/getValues', methods=['POST'])
def getValues():


    f=open("static/dataset.csv", "a")
    name = {}
    for key, value in request.form.items():
        name[ key ] = value
    global last_id;
    last_id+=1
    line=str(last_id)+"; "+"500000; "+name["sex"]+"; "+name["education"]+"; "+name["marriage"]+"; "+name["age"]+"; "+name["sep_bill"]+"; "+name["aug_bill"]+"; "+name["jul_bill"]+"; "+name["jun_bill"]+"; "+name["may_bill"]+"; "+name["apr_bill"]+"; "+name["sep_paid"]+"; "+name["aug_paid"]+"; "+name["jul_paid"]+"; "+name["jun_paid"]+"; "+name["may_paid"]+"; "+name["apr_paid"]+"; ";
    temp=np.array([name["sex"], name["education"], name["marriage"], name["age"], name["sep_bill"], name["aug_bill"], name["jul_bill"], name["jun_bill"], name["may_bill"], name["apr_bill"], name["sep_paid"], name["aug_paid"], name["jul_paid"], name["jun_paid"], name["may_paid"], name["apr_paid"] ]);
    x=temp.astype(np.int);
    x=x.reshape(1, -1)
    classification=clf.predict(x);
    line+=str(classification[0])+"\n";
    #print(line);
    f.write(line);
    f.close();
    pca.action();
    Standardization.action()
    frequency.action();
    instances.action();
    return str(last_id)

if __name__ == "__main__":
    if (len(sys.argv)!=2):
        print("You have to specify if you want the accuracy or not! Use 0 if not, 1 if yes")
        exit(-1);
    #start learning phase
    preprocessing.action();
    pca.action();
    Standardization.action()
    frequency.action();
    instances.action();
    features=["SEX", "EDUCATION", "MARRIAGE", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
    data_df = pd.read_csv("static/dataset.csv", delimiter=';', header=0)
    #data_df=data_df[:50]
    X = np.array(data_df[features].values);
    y = (data_df["default payment next month"].values.tolist());
    clf = svm.SVC(kernel="rbf", verbose=True)
    clf.fit(X,y)
    if (sys.argv[1]=="1"):
        print("Evaluating performances")
        scores=cross_val_score(clf, X, y, scoring='accuracy')
        print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))

    app.jinja_env.auto_reload = True
    #app.config["DEBUG"]=True
    #app.config["TEMPLATES_AUTO_RELOAD"]=True
    app.run(debug=True)
