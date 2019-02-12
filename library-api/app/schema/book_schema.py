from app import ma
from app.model import Book

class BookSchema(ma.ModelSchema):
    class Meta:
        strict = True
        model = Book