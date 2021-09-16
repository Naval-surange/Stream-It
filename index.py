from flask import Flask, redirect, url_for, render_template, request
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
    return render_template("index.html", vids=videos)


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/season/<series_name>")
def seasons(series_name):
    flag = 1
    for ser in db:
        if ser['name'] == series_name:
            data = ser
            flag = 0
    if flag:
        return render_template("error.html",msg="series not found!!")
    else: 
        return render_template("season.html", data=data)

    # print(data)


@app.route("/episodes/<series>/<season>")
def episodes(series, season):
    flag = 1
    for ser in db:
        if ser['name'] == series:
            if int(season) > ser["No Seasons"]:
                return render_template("error.html",msg="season not found!!")
            else:
                data = ser["seasons"][season]
                flag = 0
    if flag:
        return render_template("error.html",msg="series not found!!")
    else: 
        return render_template("episodes.html", season=data)


@app.route("/player/<series_name>/<season_number>/<episode_index>")
def player(series_name,season_number,episode_index):
    flag = 1
    for ser in db:
        if ser['name'] == series_name:
            if int(season_number) > ser["No Seasons"]:
                return render_template("error.html",msg = "season not found!!")
            else:
                season = ser['seasons'][season_number]
                if int(episode_index) > season["No episodes"]:
                    return render_template("error.html",msg = "episode not found!!")
                else :
                    episode = season["episodes"][episode_index]                
                    flag = 0
  
    if flag:
        return render_template("error.html",msg = "series not found!!")
    else: 
        return render_template("player.html", episode=episode, series_name=series_name,season_number=season_number)

@app.route("/error/<message>")
def error(message):
    return render_template("error.html",msg=message)


if __name__ == "__main__":
    app.run(debug=True)
