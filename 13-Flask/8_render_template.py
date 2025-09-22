from flask import Flask, render_template,request,session,redirect

app = Flask(__name__)
app.secret_key="super_key"

@app.route("/")
def home():
    return render_template("8_render_template_Login.html")

@app.route("/Login",methods=["GET","POST"])
def Login():
    if request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")

        valid_users={
            "aniroodh":"1234",
            "ram":"123"
        }
        if username in valid_users and password == valid_users[username]:
            session["user"]=username
            return render_template("8_render_template_welcome.html",name=username)
        else:
            return "invalid credentials"
        
    return render_template("8_render_template_Login.html")

@app.route("/welcome")
def welcome():
    if "user" in session:
        return render_template("8_render_template_welcome.html" ,name=session["user"])
    return redirect("/")

@app.route("/Logout")
def Logout():
    session.pop("user",None)
    return redirect("/")


if __name__=="__main__":
    app.run(debug=False,port=5008)