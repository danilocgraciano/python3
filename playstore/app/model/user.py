from app import db

class User(db.Model):

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    password = db.Column(db.String(8), nullable=False)

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password