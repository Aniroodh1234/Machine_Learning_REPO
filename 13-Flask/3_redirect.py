from flask import Flask,request,Response,url_for,session,redirect

app = Flask(__name__)

@app.route("/Home")
def home():
    return "welcome to the home page"

@app.route("/Login")
def Login():
    return redirect('/Home')

if __name__=="__main__":
    app.run(debug=False,port=5002)
