from flask import Flask,redirect,Response,url_for,request,session
app = Flask(__name__)

app.secret_key="super_secret"

@app.route("/")
def welcome():
    return "welcome"
@app.route("/set")
def set():
    session['username']='aniroodh'
    return "set"
@app.route("/get")
def get():
    return f"heeelo!! {session.get('username')}"

if __name__=="__main__":
    app.run(debug=False,port=5005)