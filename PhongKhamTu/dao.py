import hashlib
# from flask_login import current_user
# from sqlalchemy import extract, func
from PhongKhamTu import utils
from PhongKhamTu.model import *


def get_user_by_id(user_id):
    return User.query.get(user_id)


<<<<<<< HEAD
def register(name, username, password, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(name=username, username=username.strip(), password=password, email=email, user_role=UserRole.KHACHHANG)
=======
def register(hoten, username, password, email):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
    u = User(hoten=username, username=username.strip(), password=password, email=email, user_role=UserRole.KHACHHANG)
>>>>>>> c742fa719d8ffa1e1e5c999c866f59d3bb8270b7
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