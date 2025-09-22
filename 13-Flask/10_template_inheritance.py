from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("10_template_inheritance_home.html")

@app.route("/about")
def about():
    return render_template("10_template_inheritance_aboutus.html")

if __name__ == "__main__":
    app.run(debug=True, port=5010)
