from flask import Flask,request,session,url_for,Response,redirect

app = Flask(__name__)

@app.route("/Login", methods = ["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["Username"]
        return f"hello!! {username}"
    return '''
        <form method="POST"> 
            <input name="username">
            <input type="submit">
        </form>
'''

if __name__=="__main__":
    app.run(debug=False,port=5003)