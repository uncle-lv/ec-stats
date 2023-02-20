from datetime import datetime

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
migrate = Migrate()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now, nullable=False)
    modified_at = db.Column(db.DateTime)
    last_login = db.Column(db.DateTime)


class Role(db.Model):
    __tablename__ = 'role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255), nullable=False)


class Permssion(db.Model):
    __tablename__ = 'permission'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    description = db.Column(db.String(255), nullable=False)


class UserRole(db.Model):
    __tablename__ = 'user_role'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    rid = db.Column(db.Integer, db.ForeignKey('role.id'))


class RolePerm(db.Model):
    __tablename__ = 'role_perm'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    rid = db.Column(db.Integer, db.ForeignKey('role.id'))
    pid = db.Column(db.Integer, db.ForeignKey('permission.id'))


class Platform(db.Model):
    __tablename__ = 'platform'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    comment = db.Column(db.String(255))


class Shop(db.Model):
    __tablename__ = 'shop'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    platform = db.Column(db.Integer, db.ForeignKey('platform.id'))
    comment = db.Column(db.String(255))


class UserShop(db.Model):
    __tablename__ = 'user_shop'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(32), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey('user.id'))
    sid = db.Column(db.Integer, db.ForeignKey('shop.id'))
