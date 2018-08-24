"""from flask_sqlalchemy import SQLAlchemy
from App.index import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SECRET_KEY']='aRFQWE34hjYUfrgtAfertA'

db = SQLAlchemy(app)
class User(db.Model):
    id=db.Column('id', db.Integer, primary_key=True)
    usuario = db.Column(db.String(100))
    passwd = db.Column(db.String(100))

    def __init__(self,usuario, passwd):
        self.usuario = usuario
        self.passwd = passwd"""
