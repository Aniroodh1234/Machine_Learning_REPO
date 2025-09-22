from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/")
def welcome():
    return render_template("9_jinja2_template_profile.html",name="Aniroodh",is_topper=True,subjects=["maths","science","english"])

if __name__=="__main__":
    app.run(debug=False,port=5009)