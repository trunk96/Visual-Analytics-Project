from flask import Flask, render_template, send_from_directory, request, jsonify

import numpy as np
from sklearn import svm
from sklearn.model_selection import cross_val_score
import pandas as pd

clf=None;
app = Flask(__name__, static_folder='/static');

@app.route("/")
def index():
    return render_template("charts.html")

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)

@app.route('/getValues', methods=['POST'])
def getValues():
	f = open("static/prova.csv","a")
	line = ""
	name = {}
	for key, value in request.form.items():
		name[ key ] = value
		line += value+","
	f.write(line+"\n")
	f.close()
	return "done"

if __name__ == "__main__":
    #start learning phase
    features=["SEX", "EDUCATION", "MARRIAGE", "AGE", "BILL_AMT1", "BILL_AMT2", "BILL_AMT3", "BILL_AMT4", "BILL_AMT5", "BILL_AMT6", "PAY_AMT1", "PAY_AMT2", "PAY_AMT3", "PAY_AMT4", "PAY_AMT5", "PAY_AMT6"]
    data_df = pd.read_csv("static/dataset.csv", delimiter=';', header=0)
    #data_df=data_df[:50]
    X = np.array(data_df[features].values);
    y = (data_df["default payment next month"].values.tolist());
    clf = svm.SVC(kernel="rbf", verbose=True)
    clf.fit(X,y)
    print("Evaluating performances")
    scores=cross_val_score(clf, X, y, scoring='accuracy')
    print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))



    app.jinja_env.auto_reload = True
    #app.config["DEBUG"]=True
    #app.config["TEMPLATES_AUTO_RELOAD"]=True
    app.run(debug=True)
