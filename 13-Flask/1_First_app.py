# basic flask -- app.routes, functions, get,post requests

from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to the home page"
@app.route("/about")
def about():
    return "You are at the about page"
@app.route("/explore")
def explore():
    return "you are at the explore page"

@app.route("/submit",methods=["GET","POST"])
def submit():
    if request.method == "POST":
        return "you sent the data"
    else:
        return "You are only viewing the form"

if __name__ == "__main__":
    app.run(debug=False,port=5000)



