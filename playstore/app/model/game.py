from app import db

class Game(db.Model):

    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    _category_id = db.Column("category_id", db.Integer, db.ForeignKey('categories.id'), nullable=False)
    category = db.relationship("Category", backref='games')
    device = db.Column(db.String(20), nullable=False)

    def __init__(self, id, name, category, device):
        self.id = id
        self.name = name
        self.category = category
        self.device = device