from stream_it.models import *
from flask import redirect, url_for, render_template, request
from stream_it import app,db
import json
# db = json.load(open("./static/videos/seriesDatabase.json"))
videos = []



@app.route("/home")
@app.route("/")
def home():
    ser_list = Series.query.all()
    return render_template("index.html", ser_list=ser_list)


@app.route("/upload")
def upload():
    return render_template("upload.html")


@app.route("/season/<series_id>")
def seasons(series_id):
    ser = Series.query.get(series_id)
    if not ser:
        return render_template("error.html",msg="series not found!!")
        
    ses_list = ser.Seasons
    ser_data = {"name" : ser.name, "desc" :ser.desc ,"number_of_seasons" : len(ses_list) ,"id" : ser.id}
    ses_data = {}
    
    for ses in ses_list:
        ses_data[str(ses.number)] = {"number_of_episodes" : 10 ,"desc" : ses.desc , "id" : ses.id, "thumbnail" : ses.thumbnail }
        
    return render_template("season.html", ser_data=ser_data , ses_data=ses_data)


@app.route("/episodes/<ser_id>/<ses_id>")
def episodes(ser_id, ses_id):
    flag = 0
    ser = Series.query.get(ser_id)
    ses = Seasons.query.get(ses_id)
    
    data = []
    
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

