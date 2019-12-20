from flask import Flask,redirect,render_template,request,url_for,session
import time
import re

app = Flask(__name__)

app.secret_key = "secret"

@app.route("/",methods=['GET','POST'])
def index():
  try:
    balance = session["balance"]
    count = session["count"]
  except KeyError:
    balance = session["balance"] =8000
    count = session["count"] =0

  if request.method == "GET":
    return render_template("index.html",balance=balance,msg="")

  if request.method == "POST":
    if request.form["amount"] == "":
      msg = "Amount cannot be blank!"
      return render_template("index.html",balance=balance,msg=msg)
    elif int(request.form["amount"]) < 0:
      msg = "Amount cannot be negative"
      return render_template("index.html", balance=balance, msg=msg)
    elif session["count"] == 5:
      msg="5 transactions completed"
      return render_template("index.html", balance=balance, msg=msg)
    elif request.form["action"] == "Withdraw":
      if int(request.form["amount"]) > session["balance"]:
        msg = "Cannot withdraw more than current balance"
        return render_template("index.html", balance=balance, msg=msg)
      elif int(request.form["amount"]) >5000:
        msg = "Cannot withdraw more than 5000"
        return render_template("index.html", balance=balance, msg=msg)
      else:
        balance = balance - int(request.form["amount"])
        session["balance"] = balance
        session["count"] += 1
        msg = "Amount withdrawn"
        return render_template("index.html", balance=balance, msg=msg)
    elif request.form["action"] == "Deposit":
      if int(request.form["amount"]) > 10000:
        msg = "Cannot deposit more than 10000"
        return render_template("index.html", balance=balance, msg=msg)
      else:
        balance = balance + int(request.form["amount"])
        session["balance"] = balance
        session["count"] += 1
        msg = "Amount deposited"
        return render_template("index.html", balance=balance, msg=msg)

if __name__ == "__main__":
  app.run("localhost",port=4000,debug=True)