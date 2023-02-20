import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    DEBUG = False
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = False


class DevConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI  = f'sqlite:///{os.path.join(BASE_DIR, "dev.sqlite3")}' # noqa


class ProdConfig(BaseConfig):
    pass


config = {
    'dev': DevConfig,
    'prod': ProdConfig
}
