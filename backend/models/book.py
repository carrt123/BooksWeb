from common.exts import db


class BooksModel(db.Model):
    __tablename__ = "book"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    number = db.Column(db.String(60), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(60), nullable=False)
    price = db.Column(db.Float, nullable=False)
    author = db.Column(db.String(60))
    publisher = db.Column(db.String(255))

    @staticmethod
    def init_db():
        books = [
            (1, '001', '活着', '小说', '30.2', '余华', '南京大小出版社'),
            (2, '002', '三体', '散文', '25.5', '鲁迅', '北京文学出版社'),
            (3, '003', '白鹿原', '小说', '28.8', '陈忠实', '湖南文艺出版社'),
            (4, '004', '围城', '小说', '26.0', '钱钟书', '人民文学出版社'),
            (5, '005', '1984', '小说', '32.0', '乔治·奥威尔', '外文出版社'),
            (6, '006', '红楼梦', '小说', '36.5', '曹雪芹', '人民文学出版社'),
            (7, '007', '天龙八部', '武侠小说', '24.8', '金庸', '生活·读书·新知三联书店'),
            (8, '008', '平凡的世界', '小说', '29.9', '路遥', '人民文学出版社')
        ]

        for book in books:
            model = BooksModel(number=book[1], name=book[2], type=book[3],
                               price=book[4], author=book[5], publisher=book[6])
            db.session.add(model)
        db.session.commit()

    def serialize(self):
        return {
            "id": self.id,
            "number": self.number,
            'name': self.name,
            'type': self.type,
            'price': self.price,
            'author': self.author,
            'publisher': self.publisher
        }
