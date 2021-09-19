from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///streamit.db'
app.config['SECRET_KEY'] = "secret"
db = SQLAlchemy(app)

from stream_it import routes