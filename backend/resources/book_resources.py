from flask import request, Response
from flask_apispec import use_kwargs, doc

from common.exts import docs
from resources import api
from flask_restful import Resource
from models.book import BooksModel
from services.book_service import BookService
from Schemas.book_schemas import BookRequestSchema
from flask_apispec import MethodResource


class BookResourceApi(MethodResource, Resource):
    @doc(description="Get a book information", tags=['Book Request'])
    def get(self, book_id: int):
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            result = book_model.serialize()
            return {'status': "success", 'message': "数据查询成功", "result": result}
        else:
            return {'status': "fail", 'message': "没有找到对应id书本数据", "result": 'None'}, 404

    @doc(description="Update a book information", tags=['Book Request'])
    @use_kwargs(BookRequestSchema, location='json')  # 在json里， 按照BookRequestSchema定义提取参数
    def put(self, book_id: int, **kwargs):
        try:
            number = kwargs.get('number', None)
            name = kwargs.get('name', None)
            type = kwargs.get('type', None)
            price = kwargs.get('price', None)
            author = kwargs.get('author', None)
            publisher = kwargs.get('publisher', None)
            book_model = BooksModel(id=book_id, number=number, name=name, type=type,
                                    price=price, author=author, publisher=publisher)
            book_model = BookService().update_book(book_model)
            result = book_model.serialize()
            print(result)
            return {'status': "success", 'message': "数据修改成功", "result": result}
        except Exception as error:
            return {'status': "fail", 'message': '{}'.format(error)}

    @doc(description="Delete a book information", tags=['Book Request'])
    def delete(self, book_id: int):
        try:
            BookService().delete_book_by_id(book_id)
            return {'status': "fail", 'message': '成功删除书籍'}
        except Exception as error:
            return {'status': "fail", 'message': '{}'.format(error)}


class BookListResourceApi(MethodResource, Resource):
    @doc(description="Delete all book information", tags=['Book List Request'])
    def get(self):
        book_list = BookService().get_all_book()
        result = [book_model.serialize() for book_model in book_list]
        return {'status': "success", 'message': "数据查询成功", "result": result}

    @doc(description="Create book information", tags=['Book List Request'])
    @use_kwargs(BookRequestSchema, location='json')  # 在json里， 按照BookRequestSchema定义提取参数
    def post(self, **kwargs):
        try:
            number = kwargs.get('number', None)
            name = kwargs.get('name', None)
            type = kwargs.get('type', None)
            price = kwargs.get('price', None)
            author = kwargs.get('author', None)
            publisher = kwargs.get('publisher', None)
            book_model = BooksModel(number=number, name=name, type=type, price=price, author=author,
                                    publisher=publisher)
            book_model = BookService().create_book(book_model)
            result = book_model.serialize()
            return {'status': "success", 'message': "数创建成功", "result": result}
        except Exception as error:
            return {'status': "fail", 'message': '{}'.format(error)}, 404


api.add_resource(BookResourceApi, '/book/<int:book_id>')
api.add_resource(BookListResourceApi, '/book')

docs.register(BookResourceApi)
docs.register(BookListResourceApi)




