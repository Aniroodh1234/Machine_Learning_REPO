from flask import Flask,request,redirect,url_for,session,Response

app = Flask(__name__)

@app.route("/")
def welcome():
    return "welcome!!"
@app.route("/Home")
def Home():
    return "welcome to the home page"
@app.route("/Login")
def Login():
    return redirect(url_for("Home"))

if __name__=="__main__":
    app.run(debug=False,port=5004)