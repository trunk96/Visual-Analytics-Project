from flask import Flask, render_template, send_from_directory


app = Flask(__name__, static_folder='/static');

@app.route("/")
def index():
    return render_template("charts.html")

@app.route('/<path:path>')
def send_js(path):
    return send_from_directory('static', path)


if __name__ == "__main__":
    app.jinja_env.auto_reload = True
    app.run(host='0.0.0.0')
