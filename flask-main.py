from main import *
from flask import Flask, render_template,request,flash

app=Flask(__name__)

@app.route("/",methods=["PoST","GET"])
def home() :
    if request.method=="POST":
        s=(getSummary( str(request.form["t"])))
        return render_template("home.html",summary=s)
    else:
        return render_template("home.html")
if __name__== "__main__":
    app.run(debug=False)