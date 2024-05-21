from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def landing_Page():
    return render_template("index.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/input")
def input():
    return "<p>Output</p>"

if __name__ == "__main__":
    app.run(debug=True)