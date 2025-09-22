from flask import Flask,render_template,request,redirect,url_for,session

app=Flask(__name__)

@app.route("/")
def home():
    return redirect(url_for("feedback"))

@app.route("/11_feedback_feedback",methods=["GET","POST"])
def feedback():
    if request.method=="POST":
        name=request.form.get("name")
        message=request.form.get("message")
        return render_template("11_feedback_thankyou.html",user=name,message=message)
    return render_template("11_feedback_feedback.html")




if __name__== "__main__":
    app.run(debug=True,port=5011)