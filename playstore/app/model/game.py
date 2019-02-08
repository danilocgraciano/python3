from app import db

class Game(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    category = db.Column(db.String(40), nullable=False)
    device = db.Column(db.String(20), nullable=False)