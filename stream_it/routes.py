from stream_it.models import *
from flask import redirect, url_for, render_template, request, jsonify, flash
from stream_it import app,db
from stream_it.form import *
import json
# db = json.load(open("./static/videos/seriesDatabase.json"))
videos = []


def get_series_id(ser_name):
    return Series.query.filter(Series.name==ser_name).first().id

def get_season_id(s_no,ser_id):
    series = Series.query.get(ser_id)
    # print(series)
    seasons = series.Seasons
    for season in seasons:
        if season.number == s_no:
            required_season = season
            break
    return required_season.id


@app.route("/home")
@app.route("/")
def home():
    ser_list = Series.query.all()
    return render_template("index.html", ser_list=ser_list)


@app.route("/upload",  methods=['GET','POST'])
def upload():
    up_form = UploadForm()
    
    if request.method == 'POST':
        if up_form.validate_on_submit():
            
            ser = up_form.series.data
            ses = up_form.season.data
            ep_no = up_form.epNo.data
            ep_name = up_form.name.data
            desc = up_form.desc.data
            src = up_form.src.data
            new_episode = Episode(number = ep_no,name=ep_name,src=src,desc=desc,Season_id=ses)
            print(new_episode)
            flash(f'Episode was submitted successfully for Season {up_form.season.data} of {Series.query.get(up_form.series.data).name}!!' ,'success')
            return redirect(url_for('upload'))
        else:
            flash(f'Some validation failed episode not submitted successfully' ,'danger')
            return redirect(url_for('upload'))

    else:
      return render_template("upload.html",form=up_form)

@app.route('/getSeasons/<series_id>')
def getSeasons(series_id):
    seasons = Series.query.get(series_id).Seasons
    sesArr = []
    for ses in seasons:
        sesObj = {}
        sesObj['id'] = ses.id
        sesObj['number'] = ses.number
        sesObj['series'] = ses.Series_id
        sesArr.append(sesObj)
    return jsonify({'seasons':sesArr})

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

