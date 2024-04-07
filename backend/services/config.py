from flask_sqlalchemy import SQLAlchemy
from datetime import timedelta


db = SQLAlchemy()


class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:admin@localhost/BigData'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'your_secret_key'
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    userId = 'eGLlZWddZXrZAz7'
    token = '8oQd/7k1RqQALIrF97a0Oi2dVroNjtH59urSHrKIxPIfgYi3v8w6k+xJLwYvpiS6DtCjRL4j0HlvAWMnA4QLZQ=='

