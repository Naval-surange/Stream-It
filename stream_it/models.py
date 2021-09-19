from stream_it import db
from datetime import datetime

class Series(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(30),nullable=False)
    desc = db.Column(db.Text) 
    publish_date = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)
    thumbnail = db.Column(db.String(20),nullable = False,default='default.jpg')
    
    Seasons = db.relationship('Seasons', backref='Series', lazy=True)
    
    def __repr__(self):
        return f'Series({self.name},{self.thumbnail}, {self.Seasons} )'    

class Seasons(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer)
    publish_date = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)
    thumbnail = db.Column(db.String(20),nullable = False,default='default.jpg')
    desc = db.Column(db.Text) 
    
    Series_id = db.Column(db.Integer,db.ForeignKey('series.id'),nullable = False)
    
    episodes = db.relationship('Episode', backref='Season', lazy=True)
    
    def __repr__(self):
        return f'Seasons({self.id}, {self.number} ,{self.Series_id} ,{self.episodes})'
    
class Episode(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    number = db.Column(db.Integer)
    name = db.Column(db.String(30),nullable=False)
    publish_date = db.Column(db.DateTime,nullable = False,default=datetime.utcnow)
    desc = db.Column(db.Text) 
    thumbnail = db.Column(db.String(20),nullable = False,default='default.jpg')
    src = db.Column(db.Text,nullable=False)
    
    Season_id = db.Column(db.Integer,db.ForeignKey('seasons.id'),nullable = False)
    
    def __repr__(self):
        return f'Seasons({self.id}, {self.number},{self.name}, {self.desc} ,{self.Season_id},{self.src})'
  