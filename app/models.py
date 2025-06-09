from .db import db

class Match(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    date = db.Column(db.String(100))
    location = db.Column(db.String(100))
    result = db.Column(db.String(200))

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(50))
    batting_style = db.Column(db.String(50))
    bowling_style = db.Column(db.String(50))
    team = db.Column(db.String(100), default="UNSTOPPABLES CC")
