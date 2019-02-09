from app import db

class User(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)

    def __init__(self, id, name, password):
        self.id = id
        self.name = name
        self.password = password