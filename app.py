from flask import Flask,render_template,request,jsonify

import sqlite3 as sql

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/enternew')
def new_student():
    return render_template('user.html')

@app.route('/search/<string:s>', methods=['GET'])
def search(s):
    con = sql.connect("database.db")
    # con.row_factory = sql.Row
    cur=con.cursor()

    exist = cur.execute("SELECT * FROM users WHERE first_name LIKE ",[s]).fetchone()
    if exist is None:
        return jsonify("Doesn't exist")
    else:
        return jsonify(exist)
    # usrs=[]
    # for user in users:
    #     if user == 'string':
    #         result={"users":[],"total":0,"skip":0,"limit":0}
    # return jsonify(result)


@app.route('/addrec',methods=['POST','GET'])
def addrec():
    if request.method == 'POST':
        try:
            id=request.form['id']
            fnm=request.form['fnm']
            lnm=request.form['lnm']
            age=request.form['age']
            gen=request.form['gen']
            eml=request.form['eml']
            pn=request.form['pn']
            dob=request.form['dob']

            with sql.connect("database.db") as con:

                cur = con.cursor()

                cur.execute("INSERT INTO users (id,first_name,last_name,age,gender,email,phone,Birth_date) VALUES (?,?,?,?,?,?,?,?)",(id,fnm,lnm,age,gen,eml,pn,dob) )

                

                msg = "record successfully added"

        except:
            con.rollback()
            msg="error in insertion"

        finally:
            return render_template("result.html",msg=msg)
            con.close()


@app.route('/list')
def list():
    con = sql.connect("database.db")
    con.row_factory = sql.Row
    cur=con.cursor()
    cur.execute("select * from users")
    rows=cur.fetchall()
    return render_template("list.html",rows=rows)


if __name__=='__main__':
    app.run(debug=True)

    # python -m flask run