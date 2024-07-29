#Trivia game By Xarlos127

from flask import Flask,render_template,request,url_for
import random

app= Flask(__name__)

@app.route("/Home")
def Home():
    return render_template("index.html")

@app.route("/Sports",methods=["GET","POST"])
def Sports():
    responce = ""
    if request.method == "POST":
        awnser = request.form["awnser"]
        print(awnser)
        if awnser == "Cristiano Ronaldo":
            responce = "Correct"
        else:
            responce= "Incorrect"
    return render_template("sports.html",url = url_for('Sports'),responce=responce)

@app.route("/Music",methods=["GET","POST"])
def Music():
    responce = ""
    if request.method == "POST":
        awnser = request.form["awnser"]
        print(awnser)
        if awnser == "Not Like Us":
            responce = "Correct"
        else:
            responce= "Incorrect"
    return render_template("music.html",url = url_for('Music'), responce=responce)

@app.route("/Movies",methods=["GET","POST"])
def Movies():
    responce = ""
    if request.method == "POST":
        awnser = request.form["awnser"]
        print(awnser)
        if awnser == "Avatar":
            responce = "Correct"
        else:
            responce = "Incorrect"
    return render_template("movies.html",url = url_for('Movies'), responce=responce)

@app.route("/Boxing",methods=["GET","POST"])
def Boxing():
    responce = ""
    if request.method == "POST":
        awnser = request.form["awnser"]
        print(awnser)
        if awnser == "Manny Pacquiao":
            responce = "Correct"
        else:
            responce = "Incorrect"
    return render_template("boxing.html",url = url_for('Boxing'), responce=responce)



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=True)



