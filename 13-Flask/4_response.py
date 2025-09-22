from flask import Flask,redirect,request,Response,url_for,session

app=Flask(__name__)

@app.route("/")
def welcome():
    return "welcome"
@app.route("/custom")
def custom():
    return Response("custom_stuff",status=202,mimetype="text/plain")

if __name__ == "__main__":
    app.run(debug=False,port=5006)