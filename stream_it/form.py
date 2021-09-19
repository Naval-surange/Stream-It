from stream_it.models import *
from flask_wtf import FlaskForm
from wtforms import SelectField , StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired ,Length,Regexp,NumberRange

class UploadForm(FlaskForm):
    choices = [(s.id,s.name) for s in Series.query.all()]
    series = SelectField('series',choices=choices)
    
    choices = [(s.id , s.number) for s in Series.query.all()[0].Seasons]
    season = SelectField('season',choices=choices)

    name = StringField('name',validators=[DataRequired()])
    
    desc = StringField('desc',validators=[DataRequired() , Length(1,1000)])
    
    epNo = IntegerField('epNo' , validators=[DataRequired(),NumberRange(min=0) ])
    
    src = StringField('src',validators=[DataRequired()])
    
    submit = SubmitField('Submit!')