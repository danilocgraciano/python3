from app import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text, nullable=False, unique=True)
    publication_date = db.Column(db.Date, nullable=False)
    summary = db.Column(db.Text)
