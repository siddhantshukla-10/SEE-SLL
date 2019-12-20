from flask import Flask,redirect,render_template,request,url_for,session
import time
import re

app = Flask(__name__)

app.secret_key="secret"

@app.route("/",methods=['GET','POST'])
def index():
  if request.method == "GET":
    return render_template("index.html",msg="")

  if request.method == "POST":
    if(request.form["price1"].isdigit() and request.form["price2"].isdigit() and request.form["price3"].isdigit()):
      c = (int(request.form["price1"]) + int(request.form["price2"]) + int(request.form["price3"]))
      msg = "Total amount is "+str(c)
      return render_template("index.html",msg=msg)
    
    else:
      return render_template("index.html",msg="Enter valid price")

if __name__ == "__main__":
    app.run("localhost",port=4000,debug=True)
