from flask import Flask, render_template, send_from_directory, request, jsonify


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
    app.jinja_env.auto_reload = True
    #app.config["DEBUG"]=True
    #app.config["TEMPLATES_AUTO_RELOAD"]=True
    app.run(debug=True)
