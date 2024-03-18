import os

SECRET_KEY = os.getenv("SECRET_KEY", 'aswunxqkxqlxnwza;lf')
# 定义一个名为SECRET_KEY的变量，并将其值设置为环境变量中的"SECRET_KEY"，如果环境变量中没有设置该值，则将其默认值设置为"secret string"。
SQLALCHEMY_TRACK_MODIFICATIONS = False


MAIL_SERVER = "smtp.qq.com"
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = "2368996924@qq.com"
MAIL_PASSWORD = "huxyljfxunyuebic"
MAIL_DEFAULT_SENDER = "2368996924@qq.com"

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'books'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI