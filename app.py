from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def landing_Page():
    return render_template("index.html")

@app.route("/home")
def home_page():
    return render_template("home.html")

@app.route("/predict",methods=["POST"])
def prediction():
    if request.method == "POST":
        print(request.form)
        
    return render_template("output.html")

if __name__ == "__main__":
    app.run(debug=True)