from app import db

class Category(db.Model):

    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)

    def __init__(self, id, name):
        self.id = id
        self.name = name