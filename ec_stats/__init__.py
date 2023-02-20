from apiflask import APIFlask

from config import config
from .models import db, migrate
from .models import ( # noqa
    User,
    Role,
    Permssion,
    UserRole,
    RolePerm,
    Platform,
    Shop,
    UserShop,
)


def create_app(dev: bool):
    app = APIFlask(__name__, instance_relative_config=True)
    if dev:
        app.config.from_object(config['dev'])
    else:
        app.config.from_pyfile(config['prod'])

    init_db(app)

    return app


def init_db(app):
    db.init_app(app)
    migrate.init_app(app, db)
