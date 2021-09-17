from flask import Flask, redirect, url_for, render_template, request
import os
import json
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streamit.db'
db = SQLAlchemy(app)

# db = json.load(open("./static/videos/seriesDatabase.json"))
# print(db)
videos = []


class Series(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    desc = db.Column(db.Text) 
    publish_date = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)
    thumbnail = db.Column(db.String(20),nullable = False,default='default.jpg')
    
    Seasons = db.relationship('Seasons', backref='Series', lazy=True)
    
    def __repr__(self):
        return f'Series({self.id}, {self.name}, {self.desc}, {self.publish_date}, {self.thumbnail})'

class Seasons(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer)
    publish_date = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)
    desc = db.Column(db.Text) 
    
    Series_id = db.Column(db.Integer,db.ForeignKey('series.id'),nullable = False)
    
    def __repr__(self):
        return f'Seasons({self.id}, {self.number}, {self.publish_date}, {self.desc} )'
    


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
