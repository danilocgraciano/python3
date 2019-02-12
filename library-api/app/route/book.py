from flask import Blueprint, jsonify, request, url_for
from werkzeug.exceptions import abort

from app import db
from app.model import Book
from app.schema import BookSchema

from app.config import PAGE_SIZE

book = Blueprint("book", __name__)

@book.route("/books", methods=["GET"])
def all():

    page = request.args.get('page', 1, type=int)
    pagination = db.session.query(Book).order_by(Book.name).paginate(page, per_page=PAGE_SIZE, error_out=False)
    all = pagination.items

    next = None
    prev = None

    if pagination.has_prev:
        prev = url_for('book.all', page=page - 1, _external=True)

    if pagination.has_next:
        next = url_for('book.all', page=page + 1, _external=True)

    result = BookSchema(many=True).dump(all)
    return jsonify({
        "data": result.data,
        'prev': prev,
        'next': next,
        'count': pagination.total
    })

@book.route("/books/<int:id>", methods=["GET"])
def one(id):
    one = db.session.query(Book).get_or_404(id)
    result = BookSchema().dump(one)
    return jsonify(result.data)

@book.route("/books", methods=["POST"])
def create():

    book_schema = BookSchema()
    result = book_schema.load(request.json)
    new_book = result.data
    db.session.add(new_book)
    db.session.commit()

    result = book_schema.dump(new_book)

    return jsonify(result.data),201,{'Location': url_for("book.one", id=new_book.id, _external=True)}

@book.route("/books/<int:id>", methods=["PUT"])
def update(id):

    if (not request.json):
        abort(400)

    book_schema = BookSchema()
    result = book_schema.load(request.json)
    new_book = result.data

    _book = db.session.query(Book).get_or_404(id)
    _book.name = new_book.name
    _book.publication_date = new_book.publication_date
    _book.summary = new_book.summary

    db.session.merge(_book)
    db.session.commit()

    result = book_schema.dump(new_book)

    return jsonify(result.data), 200

@book.route("/books/<int:id>", methods=["DELETE"])
def delete(id):

    if (not request.json):
        abort(400)

    _book = db.session.query(Book).get(id)

    if (not _book):
        abort(404)

    db.session.query(Book).filter(Book.id == id).delete()
    db.session.commit()

    return "", 204