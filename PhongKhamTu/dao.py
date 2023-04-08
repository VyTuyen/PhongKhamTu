import hashlib
# from flask_login import current_user
# from sqlalchemy import extract, func
from PhongKhamTu import utils
from PhongKhamTu.model import *


def get_user_by_id(user_id):
    return User.query.get(user_id)


def register(name, username, password, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=username, username=username.strip(), password=password, email=email, user_role=UserRole.KHACHHANG)
    db.session.add(u)
    db.session.commit()

def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()

def check_login(username, password, role):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password),
                                 User.user_role.__eq__(role)).first()