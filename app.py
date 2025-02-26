from flask import Flask
from flask import render_template
app = Flask(__name__) 

@app.route("/") 
def home():
    return render_template("home.html")

@app.route("/test")
def hello():
    return "This is test Page "

if __name__ == "__main__":
    app.run(debug = False,host='0.0.0.0',port=5000)