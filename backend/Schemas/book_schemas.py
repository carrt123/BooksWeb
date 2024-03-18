from marshmallow import Schema, fields
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema
from models.book import BooksModel


class TokenSchema(Schema):
    token = fields.String(required=True)


class BookRequestSchema(Schema):
    number = fields.String(requied=True)
    name = fields.String(required=True)
    type = fields.String(required=True)
    price = fields.Float(required=True)
    author = fields.String(required=True)
    publisher = fields.String(required=True)