from sqlalchemy import Select
from models.book import BooksModel
from common.exts import db


class BookService:
    def get_book_by_id(self, book_id: int):
        return db.session.get(BooksModel, book_id)

    def get_all_book(self):
        query = Select(BooksModel).order_by(BooksModel.name)
        return db.session.scalars(query).all()

    def get_book_by_name(self, book_name: str):
        query = Select(BooksModel).where(BooksModel.name == book_name)
        return db.session.scalars(query).all()

    def update_book(self, book_model: BooksModel):
        exist_book_model = self.get_book_by_id(book_model.id)
        # 不存在这本书进行报错
        if not exist_book_model:
            raise Exception('数据库不存在id为{}的书籍'.format(book_model.id))
        else:
            # 判断是否传入字段对应的数据， 如果没有传入， 不修改字段对应数据
            if book_model.number:
                exist_book_model.number = book_model.number
            if book_model.name:
                exist_book_model.name = book_model.name
            if book_model.type:
                exist_book_model.type = book_model.type
            if book_model.price:
                exist_book_model.price = book_model.price
            if book_model.author:
                exist_book_model.author = book_model.author
            if book_model.publisher:
                exist_book_model.publisher = book_model.publisher
        db.session.commit()
        return exist_book_model

    def delete_book_by_id(self, book_id: int):
        exist_book_model = self.get_book_by_id(book_id)
        if exist_book_model:
            db.session.delete(exist_book_model)
            db.session.commit()
        else:
            raise Exception('不存在id为{}的书籍'.format(book_id))

    def create_book(self, book_model: BooksModel):
        name = book_model.name
        author = book_model.author
        exist_book_models= db.session.query(BooksModel).filter(BooksModel.name == name, BooksModel.author == author).all()
        if exist_book_models:
            raise Exception(' 已经存在同名和同作者的书籍: {}--{}'.format(book_model.name, book_model.author))
        db.session.add(book_model)
        db.session.commit()

        return book_model
