from flask_apispec import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS  # 跨域伪造
from flask_restful_swagger_3 import Api, swagger

db = SQLAlchemy()
cors = CORS()
api = Api()
docs = FlaskApiSpec()
