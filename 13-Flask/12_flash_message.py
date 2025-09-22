from flask import Flask, request,redirect,url_for,render_template,flash

app = Flask(__name__)
app.secret_key="secret_ket_01"

@app.route("/",methods=["GET","POST"])
def feedback():
    if request.method == "POST":
        name = request.form.get("name")
        if not name:
            flash("Name needs to be given")
            return redirect(url_for("12_flash_message_form"))
        
        flash(f"Thanks {name} for filling form")
        return redirect(url_for("12_flash_message_thankyou"))
    return render_template("12_flash_message_form.html")


@app.route("/thankyou")
def thankyou():
    return render_template("12_flash_message_thankyou.html")



if __name__=="__main__":
    app.run(debug=True,port=5012)