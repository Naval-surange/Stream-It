from flask import Flask,redirect,url_for,render_template,request
import os
from werkzeug.utils import html
import json

app = Flask(__name__)

db = json.load(open("./static/videos/seriesDatabase.json"))
# print(db)
videos = []


@app.route("/home")
@app.route("/")
def home():
    return render_template("index.html",vids=videos)

@app.route("/upload")
def upload():
    return render_template("upload.html")

@app.route("/season")
def seasons():
    data = db[0]
    # print(data)
    return render_template("season.html",data=data)

@app.route("/player/<video>")
def player(video):
    filePath = f'videos/{video}/{video}.mp4' 
    return render_template("player.html",path=filePath,video=video)


if __name__ == "__main__":
    app.run(debug=True)