from flask import Flask,request,render_template,redirect,Response,url_for,session,flash,jsonify

app = Flask(__name__)

@app.route('/')
def welcome():
    return "<h1>welcome to our site<h1>"

@app.route('/success/<int:score>')  # this is called variable rule
def success(score):
    return f"<h2>the person is passed and secured {score} marks<h2>"

@app.route('/fail/<int:score>')
def fail(score):
    return f"<h2>the person is failed and scored {score} marks<h2>"

@app.route('/axis',methods=['POST','GET'])
def average_marks():
    if request.method=='POST':
        math = int(request.form.get('math'))
        science= int(request.form.get('science'))
        history= int(request.form.get('history'))

        avg_marks=(math+science+history)/3

        res=""
        if avg_marks>=50:
            res='success'
        else:
            res='fail'
        return redirect(url_for(res,score=int(avg_marks)))
    return render_template('axis.html')


## api creation --> this is implemented using postman
@app.route('/api',methods=['POST','GET'])
def sum():
    data = request.get_json()
    a_value = float(dict(data)['a'])
    b_value = float(dict(data)['b'])

    return jsonify(a_value+b_value)


if __name__=='__main__':
    app.run(debug=True,port=5020)