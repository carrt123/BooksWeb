from flask import Blueprint

book = Blueprint('book', __name__, url_prefix='/')


@book.route('/')
def hello():
    return "hello"

