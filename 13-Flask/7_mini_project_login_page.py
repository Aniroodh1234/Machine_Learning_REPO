from flask import Flask,redirect,request,Response,url_for,session

app=Flask(__name__)
app.secret_key="super_key"

@app.route("/")
def home():
    return "welcome to my Login portal"

@app.route('/Login',methods=["POST","GET"])
def Login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if username=='admin' and password=="1234":
            session['user']=username
            return redirect(url_for("welcome"))
        else:
            return Response("invalid credentials",mimetype="text/plain")
    return """
            <form method="POST">
            username: <input type = "text" name = "username"><br>
            Password: <input type = "password" name = "password"><br>
            <input type="Submit" value="login">
            </form>

"""
@app.route("/welcome")
def welcome():
    if "user" in session:
        return f"""
            <h2>welcome {session["user"]}!!!</h2>
            <a href={url_for("logout")}> Logout</a>
        """
    return redirect(url_for("Login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("Login"))





if __name__=="__main__":
    app.run(debug=False,port=5007)